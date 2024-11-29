import os
import torch
from torch.utils.data import Dataset
from random import randrange
from pathlib import Path

class CustomDataset(Dataset):
    def __init__(self, data_path: str, seq_length: int, tokenizer, offset: int=0, random_chunk: bool=False):
        self.seq_length = seq_length
        self.offset = offset
        self.tokenizer = tokenizer
        self.random_chunk = random_chunk
        
        # Create cache filename based on tokenizer and data
        tokenizer_name = tokenizer.__class__.__name__
        data_name = Path(data_path).stem  # Gets filename without extension
        cache_dir = Path("cache")
        cache_dir.mkdir(exist_ok=True)
        tokenized_file = cache_dir / f"tokenized_{data_name}_{tokenizer_name}_{tokenizer.vocab_size}.pt"
        chck = False
        if chck:
            print(f"Loading cached data from {tokenized_file}")
            self.data = torch.load(tokenized_file)
        else:
            print(f"Tokenizing data from {data_path}")
            text = Path(data_path).read_text(encoding="utf-8")
            encoded = self.tokenizer.encode(text)
            print(f"Encoded length: {len(encoded)}")
            self.data = torch.tensor(encoded)
            # Save tokenized data
            
    
    def __len__(self):
        if self.random_chunk:
            return len(self.data) // self.seq_length - 1
        else:
            return (len(self.data) - self.offset) // self.seq_length
    
    def __getitem__(self, i):
        if self.random_chunk:
            offset = randrange(self.seq_length)  # Sample random offset between 0 and seq_length-1
            return self.data[i*self.seq_length+offset:(i+1)*self.seq_length+offset]
        else:
            return self.data[i*self.seq_length+self.offset:(i+1)*self.seq_length+self.offset]
