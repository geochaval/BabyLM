# BabyLM

- What **problem** are we solving?
    - Why is it important?
- What **data** are we using?
    - What dataset did we choose?
        - BNC
    - How are we dealing with **text**?
        - How we tokenized the text?
            - BPE
    - How did we create the dataset?
        - spitter
    - Are we doing data augmentation?
        - Probably not
    - How did we evaluate the quality of the data?
- What **architecture** are we using?
    - BabyLlama
    - LTG - Bert
- How are we **training** the model?
    - How are we **pre-training** it?
    - How are **fine-tuning** it?
- How are we **evaluating** it?

## Files

Getting the Dataset:
- [`convert_bnc.py`](preprocessing/convert_bnc.py): converts the BNC dataset from XML to MD. Tbh I don't wanna touch this file.
- [`splitter.py`](preprocessing/splitter.py): takes the MD and creates a 10 M words txt file.
- [`first-names.txt`](preprocessing/first-names.txt): A file with random names. It's used in the spoken section of the BNC.
Processing the text:


## Dataset 

(The better the data the better the model)
Between 100M and 10M words. It's better to start with 10M words.

Main:
- British Encyclopedia ([wiki](https://en.wikisource.org/wiki/1911_Encyclop%C3%A6dia_Britannica))
- British National Corpus
(Both of the above don't contain information about the 21st century)

## Resources

### Papers

- Textbooks Are All You Need
    - If you have good data you have a good model duh. And it doesn't have to be that big too.
    - But you probably have to make the data yourself ^_^
    - Use textbooks - encyclopedia - questions and answers.
- Trained on 100 million words and still in shape: BERT meets British National Corpus
    - [github](https://github.com/ltgoslo/ltg-bert)
    - LTG-BERT - the winner of 10M words in 2023
    - BERT structure (Masked Words)
    - Uses the BNC dataset, we can use it with their preprocessing. Everything is already made in their github.
    - They improved the architecture quite a bit from BERT:
        - NormFormer. (Normalization before and after).
        - GEGLU Activation Function. Variation of GELU. Should be better than RELU.
        - Disentangled Attention. More complicated. You treat content and position differently. 
        - Initialization Scaling. Making the NN smaller and smaller during training (?).
    - They tried different ways to do MLM stuff and NSP stuff.
    - They used BPE: "... use the largest possible BPE vocabulary such that at least 95% of classes have 100 or more examples in training"
    - Took on average 8 hours to train.
    - There are a lot of combinations and changes you can make with this architecture.
- GPT or BERT: why not both?
    - You can train a model like BERT (finding masked words) and GPT (finding the next word) at the same time.
    - (They don't use NSP anymore) 
    - This gives better results rather than doing only one of them.
    - They go into details how they did this and the architecture they used.
    - It's interesting to see the ratio (of the dataset) between masked and casual. Masked > Casual gives better results.
- Not all layers are equally as important: Every Layer Counts BERT
    - [github](https://github.com/ltgoslo/elc-bert)
    - ELC Bert - Winners of BabyLM 2023
    - Based on the LTG-BERT model.
    - Instead of having residual connections each layer decides which layer to consider.
    - Main idea is the layer importance/weighting.
    - Similar perfomance with LTG-BERT
- Baby Llama: knowledge distillation from an ensemble of teachers trained on a small dataset with no performance penalty
- Mean BERTs make erratic language teachers: the effectiveness of latent bootstrapping in low-resource settings
- WARP: Word-level Adversarial ReProgramming
- RoBERTa: A Robustly Optimized BERT Pretraining Approach
- BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- BERTs are Generative In-Context Learners
    - Haven't read this yet. But this should say that BERT model can generate text as good as GPT-style models.
- DeBERTa: Decoding-enhanced BERT with Disentangled Attention
- DeBERTaV3: Improving DeBERTa using ELECTRA-Style Pre-Training with Gradient-Disentangled Embedding Sharing
- Should You Mask 15% in Masked Language Modeling?
    - Should be interesting

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

