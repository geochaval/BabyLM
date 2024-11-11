# BabyLM

## TODO

- Get the Dataset. Encyclopedia Britannica. ([url](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica))
- Simulate the Baby Llama.


## Outline

- What **problem** are we solving?
    - Why is it important?
- What **data** are we using?
    - What dataset did we choose?
    - How are we dealing with **text**?
        - How we tokenized the text?
            - BPE?
    - How did we create the dataset?
    - Are we doing data augmentation?
    - How did we evaluate the quality of the data?
- What **architecture** are we using?
    - How we changed the standard transformer
- How are we **training** the model?
    - How are we **pre-training** it?
    - How are **fine-tuning** it?
- How are we **evaluating** it?

## Dataset 

Between 100M and 10M words. 
It's better to start with 10M words.

(Remember the idea that the better the data the better the model)

- WikiText-103 (More or less 100 M)
- OpenSubtitles (To trim - but fun idea of just having movies dialogues)
- Tatoeba (Again?)
- Project Gutenberg (To trim)
- The Enron Email Dataset
- In a paper they talk about "British National Corpus" - didn't check this yet. + LTG_BERT

## Resources

### Papers

- Textbooks Are All You Need
    - If you have good data you have a good model duh. And it doesn't have to be that big too.
    - But you probably have to make the data yourself ^_^
    - Use textbooks - encyclopedia - questions and answers.
- GPT or BERT: why not both?
    - You can train a model like BERT (finding masked words) and GPT (finding the next word) at the same time.
    - (They don't use NSP anymore) 
    - This gives better results rather than doing only one of them.
    - They go into details how they did this and the architecture they used.
    - It's interesting to see the ratio (of the dataset) between masked and casual. Masked > Casual gives better results.
- Not all layers are equally as important: Every Layer Counts BERT
    - Added weight decay in the LTG-BERT model.
    - main idea is the layer importance
    - quite similar perfomance with LTG-BERT
- Mean BERTs make erratic language teachers: the effectiveness of latent bootstrapping in low-resource settings
- WARP: Word-level Adversarial ReProgramming
- Trained on 100 million words and still in shape: BERT meets British National Corpus
    - Uses the BNC dataset, we can use it with their preprocessing
    - LTG-BERT, the winner of 10M words in 2023
    - Has different transformer architecture, with disetangled attention, more norm layers and different fully connected configuration
    - i don't know how long it takes to train
    - I think i prefer it from babyllama
    - it has more room for modifications and comparisson between baseline and something more
- DeBERTa: Decoding-enhanced BERT with Disentangled Attention
- RoBERTa: A Robustly Optimized BERT Pretraining Approach
- BERTs are Generative In-Context Learners
    - Haven't read this yet. But this should say that BERT model can generate text as good as GPT-style models.

Ideas: (Ignore this)
- How do you evaluate the quality of the data? 
    - How can you say a textbook > a comment on reddit? Mathematically speaking.

### Books

- Build a Large Language Model from Scratch

### Summary 
- use optimization from roberta for better training
- changing the attention to disetangled is an option (but i dont like it)
- slight modifications in the transformer architecture can help, such as adding norm layers or weight skip connections

## A note on how to use Virtual Enviroments in Python

This is for having a requirements.txt file with all the libraries for the project. Also so that we will be working with the same libraries and versions.

| Task                                  | macOS/Linux Command                       | Windows Command                  |
|---------------------------------------|-------------------------------------------|----------------------------------|
| **Create virtual environment**        | `python -m venv <env_name>`               | `python -m venv <env_name>`      |
| **Activate virtual environment**      | `source <env_name>/bin/activate`          | `<env_name>\Scripts\activate`    |
| **Deactivate virtual environment**    | `deactivate`                              | `deactivate`                     |
| **Install package**                   | `pip install <package_name>`              | `pip install <package_name>`     |
| **Save packages to requirements.txt** | `pip freeze > requirements.txt`           | `pip freeze > requirements.txt`  |
| **Install from requirements.txt**     | `pip install -r requirements.txt`         | `pip install -r requirements.txt`|
| **Delete virtual environment**        | `rm -rf <env_name>`                       | `rmdir /s /q <env_name>`         |

