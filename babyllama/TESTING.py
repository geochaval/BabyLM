from transformers import (
    GPT2Config, GPT2LMHeadModel, 
    LlamaConfig, LlamaForCausalLM, 
    GPTJConfig, GPTJForCausalLM
)
from transformers import Trainer, TrainingArguments, DataCollatorForLanguageModeling
from transformers import GPT2TokenizerFast
from torch.utils.data import Subset
from random import sample, seed
from pathlib import Path
import yaml
import argparse

from babylm_dataset import BabylmDataset


config_f="./gpt-705M.yaml"
with open(config_f, 'r') as f:
    config = yaml.safe_load(f)
SEQ_LENGTH = config['data']['seq_length']


# Dynamic Model Configuration
if config['model']['type'] == "Llama":
    model_config = LlamaConfig(
        vocab_size=16000,
        max_position_embeddings=SEQ_LENGTH,
        hidden_size=config['model']['hidden_size'],
        intermediate_size=config['model']['intermediate_size'],
        num_hidden_layers=config['model']['n_layer'],
        num_attention_heads=config['model']['n_head'],
        tie_word_embeddings=config['model'].get('tie_word_embeddings', False),
    )
    model = LlamaForCausalLM(model_config)
elif config['model']['type'] == "GPT2":
    model_config = GPT2Config(
        vocab_size=16000,
        n_positions=SEQ_LENGTH,
        n_embd=config['model']['hidden_size'],
        n_layer=config['model']['n_layer'],
        n_head=config['model']['n_head'],
        #resid_pdrop = config['model']['resid_pdrop'],
        #embd_pdrop = config['model']['embd_pdrop'],
        #attn_pdrop = config['model']['attn_pdrop'],
        #pad_token_id=tokenizer.convert_tokens_to_ids("<pad>"),
    )
    model = GPT2LMHeadModel(model_config)
elif config['model']['type'] == "GPTJ":
    model_config = GPTJConfig(
        vocab_size=16000,
        n_positions=SEQ_LENGTH,
        n_embd=config['model']['hidden_size'],
        n_layer=config['model']['n_layer'],
        n_head=config['model']['n_head'],
        #resid_pdrop = config['model']['resid_pdrop'],
        #embd_pdrop = config['model']['embd_pdrop'],
        #attn_pdrop = config['model']['attn_pdrop'],
        tie_word_embeddings=config['model']['tie_word_embeddings'],
        #pad_token_id=tokenizer.convert_tokens_to_ids("<pad>"),
    )
    model = GPTJForCausalLM(model_config)

print(f'model parameters = {model.num_parameters()}')
