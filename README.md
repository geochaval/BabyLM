# Small Models, Big Impact: The BabyLM Challenge

## Introduction

This project focuses on training language models using high-quality data instead of large amounts of data. We use the Encyclopedia Britannica as our main source, a reliable and well-organized corpus, to achieve two goals:

1. Competing in the BabyLM Challenge, which limits the dataset to 10 million words.
2. Building a model that can generate encyclopedic text using the full 38-million-word dataset.

We use knowledge distillation, a technique where smaller student models learn from larger teacher models. This allows us to create smaller, faster models that still perform well. Based on the BabyLlama architecture, our work shows that combining high-quality data with efficient training methods can produce excellent results, even for specific tasks or when resources are limited.

## Files

- [`1_scraper.py`](1_scraper.py): downloads the articles from ([WikiSource](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica)), saving them as JSON files in a folder structure organized by volume and part. File names reflect the article's title. 
- [`2_convert_britannica.py`](2_convert_britannica.py): takes the output of the first script and converts all JSON files to TXT, keeping only the content. The TXT files are saved in a directory structure that mirrors the original JSON file structure.
- [`3_combiner.py`](3_combiner.py): takes the output of the second script and combines all individual text files into a single TXT file, with each article separated by a new line. The resulting file is named `combined_encyclopedia.txt`, which can be downloaded from ([HuggingFace](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)).
- [`4_cleanup.py`](4_cleanup.py): takes the `combined_encyclopedia.txt` and applies various regular expressions to clean and standardize the text, ensuring consistent formatting. Additionally, it adds `<s>` and `</s>` tokens between each article. The resulting file is `encyclopedia_cleaned.txt`.
- [`5_splitter.py`](5_splitter.py): takes the `encyclopedia_cleaned.txt` and generates a folder named "corpus_split" with two files: `train.txt` and `val.txt`. You can specify the number of words for each file, ensuring that articles are not broken up.
- [`6_tokenizer.py`](6_tokenizer.py): trains a tokenizer using the `corpus_split/train.txt`. It applies Byte Pair Encoding (BPE) with special tokens (`<pad>`, `<s>`, `</s>`) and saves the tokenizer model in the models directory as `tokenizer-clean.json`.
- [`7_train_teachers.py`](7_train_teachers.py): trains a teacher model using the tokenizer from the previous script. It applies knowledge distillation, using a configuration specified in a YAML file to guide the training process.
- [`8_train_student.py`](8_train_student.py): performs knowledge distillation from the two large models to a smaller model.
- [`9_generator.py`](9_generator.py): uses the student model to generate encyclopedia-style text based on a given prompt (e.g., `"<s> London was"`).


## Dataset 

We provide a downloadable dataset on Hugging Face:

- ([Encyclopedia Britannica Dataset](https://huggingface.co/datasets/EdoVaira/Encyclopedia-Britannica)): This includes the combined text corpus prepared through our scripts.

The dataset is sourced from the Encyclopedia Britannica available on ([WikiSource](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica)).

## Get the Paper and Presentation

For a detailed explanation of our work, methodology, and results, you can access:

- Our [`paper`](paper.pdf), which outlines the entire process and findings.
- Our [`presentation`](presentation.pdf) slides, summarizing the project’s highlights.
