import aiohttp
import asyncio
from bs4 import BeautifulSoup
import time
import logging
from pathlib import Path
import json
from urllib.parse import urljoin
import pickle
from datetime import datetime
from tqdm.asyncio import tqdm_asyncio
import sys
from dataclasses import dataclass, asdict
from typing import Set, Dict, List, Optional
import backoff
import aiodns
import cchardet
import aiofiles
from contextlib import asynccontextmanager

@dataclass
class ArticleData:
    url: str
    title: str
    content: str
    timestamp: str

class ProgressStats:
    def __init__(self):
        self.start_time = datetime.now()
        self.articles_processed = 0
        self.total_articles = 0
        self.current_volume = 1
        self.current_part = 1
        self._lock = asyncio.Lock()
        self.articles_per_minute = 0
        self.eta = None
        
    async def update(self, articles_increment: int = 0):
        async with self._lock:
            self.articles_processed += articles_increment
            elapsed_time = (datetime.now() - self.start_time).total_seconds() / 60.0
            if elapsed_time > 0:
                self.articles_per_minute = self.articles_processed / elapsed_time
                if self.total_articles > 0:
                    remaining_articles = self.total_articles - self.articles_processed
                    self.eta = remaining_articles / self.articles_per_minute if self.articles_per_minute > 0 else 0

    def get_stats(self) -> Dict:
        return {
            "Articles Processed": self.articles_processed,
            "Articles/minute": f"{self.articles_per_minute:.2f}",
            "ETA (minutes)": f"{self.eta:.2f}" if self.eta else "N/A",
            "Elapsed (minutes)": f"{(datetime.now() - self.start_time).total_seconds() / 60.0:.2f}",
            "Current Volume": self.current_volume,
            "Current Part": self.current_part
        }

class BritannicaVolumeScraper:
    def __init__(self, base_url: str, save_dir: str = "britannica_data", concurrent_requests: int = 50):
        self.base_url = base_url
        self.save_dir = Path(save_dir)
        self.save_dir.mkdir(exist_ok=True)
        self.progress_file = self.save_dir / "progress.pkl"
        self.scraped_urls = self._load_progress()
        self.concurrent_requests = concurrent_requests
        self.stats = ProgressStats()
        self._semaphore = asyncio.Semaphore(concurrent_requests)
        self.pbar = None
        self.retry_delay = 60  # Delay in seconds after too many requests

        # Setup logging
        logging.basicConfig(
            filename=self.save_dir / "scraper.log",
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def _load_progress(self) -> Dict[str, Set[str]]:
        """Load progress from pickle file"""
        if self.progress_file.exists():
            with open(self.progress_file, 'rb') as f:
                return pickle.load(f)
        return {
            'parts': set(),
            'articles': set()
        }

    async def _save_progress(self):
        """Save progress to pickle file asynchronously"""
        async with aiofiles.open(self.progress_file, 'wb') as f:
            await f.write(pickle.dumps(self.scraped_urls))

    @asynccontextmanager
    async def _create_session(self):
        """Create aiohttp session with optimal settings"""
        connector = aiohttp.TCPConnector(
            limit=self.concurrent_requests,
            ttl_dns_cache=300,
            use_dns_cache=True
        )
        
        async with aiohttp.ClientSession(
            connector=connector,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5'
            },
            timeout=aiohttp.ClientTimeout(total=30)
        ) as session:
            yield session

    @backoff.on_exception(
        backoff.expo,
        (aiohttp.ClientError, asyncio.TimeoutError),
        max_tries=5,  # Increased from 3 to 5
        max_time=120  # Increased from 30 to 120
    )
    async def _fetch_with_retry(self, session: aiohttp.ClientSession, url: str) -> Optional[str]:
        """Fetch URL with improved retry logic"""
        async with self._semaphore:
            try:
                async with session.get(url) as response:
                    if response.status == 404:
                        return None
                    elif response.status == 429:  # Too Many Requests
                        logging.warning(f"Rate limit hit for {url}. Waiting {self.retry_delay} seconds...")
                        await asyncio.sleep(self.retry_delay)
                        self.retry_delay *= 1.5  # Increase delay for subsequent retries
                        raise aiohttp.ClientError("Rate limit exceeded")  # Trigger backoff retry
                    response.raise_for_status()
                    self.retry_delay = 60  # Reset delay on successful request
                    return await response.text()
            except aiohttp.ClientError as e:
                if "Too Many Requests" in str(e):
                    logging.warning(f"Rate limit hit for {url}. Waiting {self.retry_delay} seconds...")
                    await asyncio.sleep(self.retry_delay)
                    self.retry_delay *= 1.5  # Increase delay for subsequent retries
                raise  # Re-raise to trigger backoff

    def page_exists(self, html: str) -> bool:
        """Check if page exists and is not a 'not found' page"""
        if not html:
            return False
        
        soup = BeautifulSoup(html, 'lxml')
        not_found_msg = "Wikisource does not have a text with this exact name"
        return not_found_msg not in soup.get_text()

    def get_articles_from_part(self, part_html: str, part_url: str) -> List[str]:
        """Extract article URLs from a part page"""
        if not part_html:
            return []
            
        soup = BeautifulSoup(part_html, 'lxml')
        article_links = []
        
        content_div = soup.find('div', {'class': 'mw-parser-output'})
        if content_div:
            for link in content_div.find_all('a'):
                href = link.get('href', '')
                if (href and '/wiki/' in href and 
                    not any(x in href for x in ['File:', 'Category:', 'Template:', 'Help:', 'Vol_'])):
                    full_url = urljoin(self.base_url, href)
                    article_links.append(full_url)
        
        return article_links

    def parse_article(self, html: str, url: str) -> Optional[ArticleData]:
        """Parse article content from HTML"""
        if not html:
            return None
            
        soup = BeautifulSoup(html, 'lxml')
        content = soup.find('div', {'class': 'mw-parser-output'})
        
        if not content:
            logging.warning(f"No content found for {url}")
            return None
        
        return ArticleData(
            url=url,
            title=soup.find('h1', {'id': 'firstHeading'}).text.strip() if soup.find('h1', {'id': 'firstHeading'}) else '',
            content=content.get_text(separator='\n', strip=True),
            timestamp=time.strftime('%Y-%m-%d %H:%M:%S')
        )

    async def save_article(self, article_data: ArticleData, volume_number: int, part_number: int):
        """Save article data to JSON file asynchronously"""
        volume_dir = self.save_dir / f"volume_{volume_number:02d}"
        part_dir = volume_dir / f"part_{part_number:02d}"
        part_dir.mkdir(parents=True, exist_ok=True)
        
        safe_title = "".join(c for c in article_data.title if c.isalnum() or c in (' ', '-', '_')).rstrip()
        filename = part_dir / f"{safe_title}.json"
        
        async with aiofiles.open(filename, 'w', encoding='utf-8') as f:
            await f.write(json.dumps(asdict(article_data), ensure_ascii=False, indent=2))

    async def process_article(
        self, 
        session: aiohttp.ClientSession,
        article_url: str, 
        volume_number: int, 
        part_number: int
    ) -> Optional[str]:
        """Process a single article with progress tracking"""
        if article_url in self.scraped_urls['articles']:
            return None
            
        try:
            article_html = await self._fetch_with_retry(session, article_url)
            if not article_html:
                return None
                
            article_data = self.parse_article(article_html, article_url)
            if article_data:
                await self.save_article(article_data, volume_number, part_number)
                await self.stats.update(articles_increment=1)
                
                if self.pbar:
                    self.pbar.update(1)
                    if self.stats.articles_per_minute > 0:
                        self.pbar.set_description(
                            f"Vol {volume_number} Part {part_number} "
                            f"({self.stats.articles_per_minute:.1f} articles/min)"
                        )
                
                self.scraped_urls['articles'].add(article_url)
                await self._save_progress()
                
            return article_url
        except Exception as e:
            logging.error(f"Error processing article {article_url}: {str(e)}")
            return None

    async def process_volume_part(
        self, 
        session: aiohttp.ClientSession,
        volume_number: int, 
        part_number: int
    ) -> Optional[List[str]]:
        """Process a single part with improved error handling"""
        part_url = f"{self.base_url}/Vol_{volume_number}:{part_number}"
        logging.info(f"Checking part URL: {part_url}")
        
        try:
            part_html = await self._fetch_with_retry(session, part_url)
            if not part_html or not self.page_exists(part_html):
                return None
            
            self.scraped_urls['parts'].add(part_url)
            await self._save_progress()
            
            return self.get_articles_from_part(part_html, part_url)
        except Exception as e:
            logging.error(f"Error processing part {part_url}: {str(e)}")
            # Don't return None here - instead retry the whole part
            raise

    async def process_volume(self, session: aiohttp.ClientSession, volume_number: int):
        """Process all parts of a volume with retry logic"""
        self.stats.current_volume = volume_number
        part_number = 1
        
        while True:
            try:
                self.stats.current_part = part_number
                article_urls = await self.process_volume_part(session, volume_number, part_number)
                
                if not article_urls:
                    break
                    
                self.stats.total_articles += len(article_urls)
                if self.pbar:
                    self.pbar.total = self.stats.total_articles
                
                # Process articles with chunking to avoid overwhelming the server
                chunk_size = 10  # Process 10 articles at a time
                for i in range(0, len(article_urls), chunk_size):
                    chunk = article_urls[i:i + chunk_size]
                    tasks = [
                        self.process_article(session, url, volume_number, part_number)
                        for url in chunk
                        if url not in self.scraped_urls['articles']
                    ]
                    
                    if tasks:
                        await asyncio.gather(*tasks)
                        await asyncio.sleep(1)  # Small delay between chunks
                
                part_number += 1
            except Exception as e:
                logging.error(f"Error processing volume {volume_number} part {part_number}: {str(e)}")
                # Wait before retrying the current part
                await asyncio.sleep(self.retry_delay)
                continue  # Retry the current part

    async def print_stats(self):
        """Print current statistics"""
        stats = self.stats.get_stats()
        print("\nCurrent Progress:")
        for key, value in stats.items():
            print(f"{key}: {value}")
        print("-" * 50)

    async def run(self):
        """Main scraping function with improved error handling"""
        try:
            print("Starting async scraper...")
            
            async with self._create_session() as session:
                self.pbar = tqdm_asyncio(total=0, dynamic_ncols=True, unit='article')
                
                for volume in range(1, 29):
                    while True:
                        try:
                            logging.info(f"Processing Volume {volume}")
                            await self.process_volume(session, volume)
                            await self.print_stats()
                            break  # Only break if volume completes successfully
                        except Exception as e:
                            logging.error(f"Error processing volume {volume}: {str(e)}")
                            await asyncio.sleep(self.retry_delay)
                            # Don't break - retry the current volume
                
        except KeyboardInterrupt:
            print("\nScraping interrupted by user")
            await self.print_stats()
            await self._save_progress()
        except Exception as e:
            print(f"\nUnexpected error: {str(e)}")
            await self.print_stats()
            await self._save_progress()
            raise
        finally:
            if self.pbar:
                self.pbar.close()

async def main():
    BASE_URL = "https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica"
    scraper = BritannicaVolumeScraper(BASE_URL, concurrent_requests=50)
    await scraper.run()

if __name__ == "__main__":
    asyncio.run(main())