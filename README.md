# BabyLM

## Files

- [`1_scraper.py`](1_scraper.py): The script downloads articles, saving them as JSON files in a folder structure organized by volume and part. File names reflect the article's title. 
- [`2_convert_britannica.py`](2_convert_britannica.py): JSON files → clean text files (content only)
- 3x: Text combiner: Individual text files → single encyclopedia file with articles separated by newlines
- 4x: Text cleaner: Raw encyclopedia text → standardized text with consistent formatting
- 5x: Dataset splitter: Clean text → training/validation sets in 'corpus_split' with LLM tokens
- 6x: Tokenizer trainer: Training text → BPE tokenizer (16K vocab) saved as JSON in 'models'
- 7x: Model trainer: Training data + tokenizer → trained language model (config via YAML)
- 8x: Knowledge distiller: Two large models (360M, 705M params) → smaller model (58M params)


## Dataset 

British Encyclopedia ([wiki](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica))

You can download it from ([HuggingFace](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)).