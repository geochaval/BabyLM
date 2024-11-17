import re
import unicodedata
from pathlib import Path
from typing import List, Dict, Pattern
from functools import lru_cache
from tqdm import tqdm

# Define cleaning patterns
CLEANING_PATTERNS: Dict[str, tuple[str, str]] = {
    'invisible_chars': (r'[\u200B-\u200D\uFEFF]', ''),
    'quotes': (r'[""''‹›«»]', '"'),
    'apostrophes': (r'[`′´'']', "'"),
    'references': (r'\([^)]*(?:q\.v\.|cf\.)[^)]*\)', ''),
    'dashes': (r'[‒–—―]', '-'),
    'space_before_punct': (r'\s*([,.!?:;)])', r'\1'),
    'space_after_paren': (r'(\()\s*', r'\1'),
    'whitespace': (r'[^\S\n]+', ' '),
    'line_edges': (r'^ +| +$', ''),
    'multiple_newlines': (r'\n{3,}', '\n\n'),
    'ocr_numbers': (r'l(?=\d)|O(?=\d)', lambda m: '1' if m.group() == 'l' else '0'),
    'date_suffixes': (r'(?<=\d)(?:A\.D\.|B\.C\.)', ''),
    'extra_spaces': (r' +', ' ')
}

@lru_cache(maxsize=100)
def compile_patterns() -> List[tuple[Pattern, str]]:
    """Compile regex patterns once and cache them for better performance."""
    compiled_patterns = []
    for pattern, replacement in CLEANING_PATTERNS.values():
        flags = re.MULTILINE if pattern.startswith('^') or pattern.endswith('$') else 0
        compiled_pattern = re.compile(pattern, flags=flags)
        compiled_patterns.append((compiled_pattern, replacement))
    return compiled_patterns

def clean_text(text: str) -> str:
    """Clean text using predefined patterns."""
    text = unicodedata.normalize('NFKD', text)
    patterns = compile_patterns()
    for pattern, replacement in patterns:
        if callable(replacement):
            text = pattern.sub(replacement, text)
        else:
            text = pattern.sub(replacement, text)
    return text.strip()

def process_file(
    input_file: str, 
    output_file: str, 
    encoding: str = 'utf-8',
    chunk_size: int = 1024 * 1024  # 1MB chunks
) -> None:
    """Process a text file in chunks with progress indication."""
    input_path = Path(input_file)
    output_path = Path(output_file)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")
        
    output_path.parent.mkdir(parents=True, exist_ok=True)
    file_size = input_path.stat().st_size
    chunks_total = (file_size + chunk_size - 1) // chunk_size
    
    with open(input_path, 'r', encoding=encoding) as infile, \
         open(output_path, 'w', encoding=encoding) as outfile:
        
        with tqdm(total=chunks_total, 
                 desc="Processing file", 
                 unit="MB",
                 bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]') as pbar:
            
            while True:
                chunk = infile.read(chunk_size)
                if not chunk:
                    break
                cleaned_chunk = clean_text(chunk)
                outfile.write(cleaned_chunk)
                pbar.update(1)

def main():
    try:
        process_file(
            "combined_encyclopedia.txt",
            "encyclopedia_cleaned.txt"
        )
    except Exception as e:
        print(f"\nError: {str(e)}")
        raise

if __name__ == "__main__":
    main()