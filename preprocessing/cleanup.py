import os
import regex as re

train_file = '../datasets/train.txt'
validation_file = '../datasets/validation.txt'

def clean_text(text):
    #text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s.,!?\'"-]', '', text)
    text = re.sub(r'[\n]{3,}', '\n\n', text)
    return text

with open(train_file, 'r', encoding='utf-8') as infile, open('../datasets/train_cleaned.txt', 'w', encoding='utf-8') as outfile:
    text = infile.read()
    text = clean_text(text)
    outfile.write(text)


with open(validation_file, 'r', encoding='utf-8') as infile, open('../datasets/validation_cleaned.txt', 'w', encoding='utf-8') as outfile:
    text = infile.read()
    text = clean_text(text)
    outfile.write(text)