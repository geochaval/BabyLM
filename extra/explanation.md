# Encyclopedia Processing Scripts

## Overview
A collection of scripts to scrape, process, and analyze Encyclopedia content.

## File Structure

```text
britannica_data/
│   volume_01/
│   │   part_01/
│   │   │   article1.json
│   │   │   article2.json
│   │   │   article3.json
│   │   │   ...
│   │   part_02/
│   │   part_03/
│   volume_02/
│   volume_03/
britannica_txt/
corpus_split/
│   train.txt
│   val.txt
combined_encyclopedia.txt
encyclopedia_cleaned.txt
```

## Scripts

### 1. `1_scraper.py`
- Scrapes the Encyclopedia content from the website
- Saves articles in JSON format
- Creates directory structure: `britannica_data/volume_XX/part_XX/`

### 2. `2_convert_britannica.py`
- Converts JSON files to TXT format
- Some articles are with an empty content. It's not a mistake of the scraper, but a mistake of the website. They aren't too many (~400), so they just get ignored.
- Output directory: `britannica_txt/`

### 3. `3_combiner.py`
- Merges all TXT files into a single corpus
- Output: `combined_encyclopedia.txt`

### 4. `4_cleanup.py`
- Applies regex patterns for text cleanup
- Output: `encyclopedia_cleaned.txt`

### 5. `5_splitter.py`
- Splits the full corpus `encyclopedia_cleaned.txt` into train and validation set. Based on words count.
- It takes the full corpus and randomizes the article before splitting. 
- Output directory: `corpus_split/`

### 6. `statistics.py`
- Analyzes `encyclopedia_cleaned.txt`
- Generates statistics like word count and other metrics

## Output Files
- `combined_encyclopedia.txt`: Raw merged corpus
- `encyclopedia_cleaned.txt`: Final cleaned version of the corpus

# Some notes for myself

If you use BPE the UNK token is useless. Nothing is out of the "vocabulary" (hopefully).