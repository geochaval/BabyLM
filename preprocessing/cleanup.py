import os
import regex as re

train_file = '../pretrain/train.txt'
validation_file = '../pretrain/validation.txt'

def clean_text(text):
    #text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

with open(train_file, 'r', encoding='utf-8') as infile, open('../pretrain/train_cleaned.txt', 'w', encoding='utf-8') as outfile:
    text = infile.read()
    text = clean_text(text)
    outfile.write(text)


with open(validation_file, 'r', encoding='utf-8') as infile, open('../pretrain/validation_cleaned.txt', 'w', encoding='utf-8') as outfile:
    text = infile.read()
    text = clean_text(text)
    outfile.write(text)