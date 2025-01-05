# BabyLM

## Files

- [`1_scraper.py`](1_scraper.py): The script downloads the articles from ([WikiSource](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica)), saving them as JSON files in a folder structure organized by volume and part. File names reflect the article's title. 
- [`2_convert_britannica.py`](2_convert_britannica.py): This script takes the output of the first script and converts all JSON files to TXT, keeping only the content. The TXT files are saved in a directory structure that mirrors the original JSON file structure.
- [`3_combiner.py`](3_combiner.py): This script takes the output of the second script and combines all individual text files into a single TXT file, with each article separated by a new line. The resulting file is named `combined_encyclopedia.txt`, which can be downloaded from ([HuggingFace](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)).
- 4x: Text cleaner: Raw encyclopedia text → standardized text with consistent formatting
- 5x: Dataset splitter: Clean text → training/validation sets in 'corpus_split' with LLM tokens
- 6x: Tokenizer trainer: Training text → BPE tokenizer (16K vocab) saved as JSON in 'models'
- 7x: Model trainer: Training data + tokenizer → trained language model (config via YAML)
- 8x: Knowledge distiller: Two large models (360M, 705M params) → smaller model (58M params)


## Dataset 

British Encyclopedia ([WikiSource](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica))

You can download it from ([HuggingFace](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)).