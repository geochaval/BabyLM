# BabyLM

## Files

- [`1_scraper.py`](1_scraper.py): The script downloads the articles from ([WikiSource](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica)), saving them as JSON files in a folder structure organized by volume and part. File names reflect the article's title. 
- [`2_convert_britannica.py`](2_convert_britannica.py): This script takes the output of the first script and converts all JSON files to TXT, keeping only the content. The TXT files are saved in a directory structure that mirrors the original JSON file structure.
- [`3_combiner.py`](3_combiner.py): This script takes the output of the second script and combines all individual text files into a single TXT file, with each article separated by a new line. The resulting file is named `combined_encyclopedia.txt`, which can be downloaded from ([HuggingFace](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)).
- [`4_cleanup.py`](4_cleanup.py): takes the `combined_encyclopedia.txt` and applies various regular expressions to clean and standardize the text, ensuring consistent formatting. Additionally, it adds `<s>` and `</s>` tokens between each article. The resulting file is `encyclopedia_cleaned.txt`.
- [`5_splitter.py`](5_splitter.py): takes the `encyclopedia_cleaned.txt` and generates a folder named "corpus_split" with two files: `train.txt` and `val.txt`. You can specify the number of words for each file, ensuring that articles are not broken up.
- [`6_tokenizer.py`](6_tokenizer.py): trains a tokenizer using the `corpus_split/train.txt`. It applies Byte Pair Encoding (BPE) with special tokens (`<pad>`, `<s>`, `</s>`) and saves the tokenizer model in the models directory as `tokenizer-clean.json`.
- 7x: Model trainer: Training data + tokenizer → trained language model (config via YAML)
- 8x: Knowledge distiller: Two large models (360M, 705M params) → smaller model (58M params)


## Dataset 

British Encyclopedia ([WikiSource](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica))

You can download it from ([HuggingFace](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)).