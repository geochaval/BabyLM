# BabyLM

## Outline

- What **problem** are we solving?
    - Why is it important?
- What **data** are we using?
    - What dataset did we choose?
    - How are we dealing with **text**?
        - How we tokenized the text
    - Are we doing data augmentation?
- What **architecture** are we using?
    - How we changed the standard transformer
- How are we **training** the model?
    - How are we **pre-training** it?
    - How are **fine-tuning** it?
- How are we **evaluating** it?

## Dataset 

Between 100M and 10M words. 

Still to be picked.

## Resources

### Papers

- GPT or BERT: why not both?
- Not all layers are equally as important: Every Layer Counts BERT
- Mean BERTs make erratic language teachers: the effectiveness of latent bootstrapping in low-resource settings
- WARP: Word-level Adversarial ReProgramming (I guess?)
- DeBERTa: Decoding-enhanced BERT with Disentangled Attention
- RoBERTa: A Robustly Optimized BERT Pretraining Approach
- Textbooks Are All You Need

### Books

- Build a Large Language Model from Scratch

### Summary 
- use optimization from roberta for better training
- nsp tasks don't really help in the end, stick to MSM
- using a combination of MSM and next token prediction is an option
- changing the attention to disetangled is an option (but i dont like it)
- use textbooks or encyclopedia for pretraining
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

