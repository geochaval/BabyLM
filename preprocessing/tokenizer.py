from tokenizers import Tokenizer, decoders, models, pre_tokenizers, processors, trainers
from tokenizers.normalizers import NFKC
import os
from collections import Counter

train_file = '../pretrain/train_cleaned.txt'
validation_file = '../pretrain/validation_cleaned.txt'
vocab_path = '../pretrain/bpe.json'
tokenizer = Tokenizer(models.BPE(unk_token="[UNK]"))

tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
tokenizer.decoder = decoders.ByteLevel()
tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)
tokenizer.normalizer = NFKC()

trainer = trainers.BpeTrainer(
    vocab_size= 2**13,
    special_tokens=["<PAD>", "<UNK>", "<s>", "</s>"],
)
print("Training the tokenizer", flush=True)
tokenizer.train([train_file], trainer)

print("Saving the tokenizer", flush=True)
tokenizer.save(vocab_path)

def calculate_f95(tokenizer, f):
    counter = Counter()
    for sentence in f.readlines():
        sentence = sentence.strip()
        if len(sentence) > 0:
            counter.update(tokenizer.encode(sentence).tokens)

    sorted_subwords = counter.most_common()
    #print("100 most common subwords:\n" + '\n'.join(str(x) for x in sorted_subwords[:100]) + '\n')

    with open(vocab_path + "_freqs", 'w', encoding='utf-8') as f_freq:
        f_freq.write('\n'.join(f"{subword}: {freq}" for subword, freq in sorted_subwords))

    subword95 = sorted_subwords[len(sorted_subwords) * 95 // 100]
    return subword95[1]

with open(train_file, 'r', encoding= 'utf-8') as f:
    f95 = calculate_f95(tokenizer, f)
print(f"F_{{95%}} is {f95}\n")

tokenizer = Tokenizer.from_file(vocab_path)

# text = 'Shiro Okada (岡田志郎, "Okada Shirō", June 9, 1949; Hirakata, Osaka {age 71} - ) is a Japanese guitarist who participate in the Group Sound band, the Ox. His nickname was Shiro (シロー) and his real name is Shiro Okamoto (岡田史郎).'
text = "The quick brown fox jumps over the lazy dog."

encoded = tokenizer.encode(text)
print(f"Encoded String: {encoded.tokens}")

print(f"Encoded IDs: {encoded.ids}")

decoded = tokenizer.decode(encoded.ids)
print(f"Decoded String: {decoded}")