from transformers import PreTrainedTokenizerFast, Trainer, TrainingArguments
from datasets import Dataset
from tokenizers import Tokenizer
from modeling_ltgbert import LtgBertForMaskedLM
from configuration_ltgbert import LtgBertConfig
import os
import torch_optimizer as optim

tokenizer_file = './bpe.json'
train_file = '../datasets/train_cleaned.txt'
eval_file = '../datasets/validation_cleaned.txt'
output_dir = '../models'

os.system(f"mkdir {output_dir}")

bpe_tokenizer = Tokenizer.from_file(tokenizer_file)

tokenizer = PreTrainedTokenizerFast(tokenizer_object=bpe_tokenizer)
tokenizer.pad_token = "[PAD]"  # Ensure special tokens are set
tokenizer.eos_token = "[EOS]"
tokenizer.bos_token = "[BOS]"

vocab = tokenizer.get_vocab()
if "<PAD>" in vocab:
    tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("<PAD>")
else:
    print("Pad token <PAD> not found in vocab. Adding <PAD> to the tokenizer.") 
    tokenizer.add_special_tokens({"pad_token": "<PAD>"})
    tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("<PAD>")

def tokenize(dataset):
    return tokenizer(
        dataset["text"],          # or text.splitlines() or [text] for full text
        truncation=True,     # Truncate to model's max length
        max_length=128,      # Adjust based on your model
        padding="max_length", # Pad to the model's max length
    )

with open(train_file, "r", encoding="utf-8") as file:
    train_text = file.read()

paragraphs = train_text.split('\n\n')

train_dataset = Dataset.from_dict({"text": paragraphs})

with open(eval_file, "r", encoding="utf-8") as file:
    eval_text = file.read()

paragraphs = eval_text.split('\n\n')

valid_dataset = Dataset.from_dict({"text": paragraphs})


config = LtgBertConfig(
    vocab_size=len(tokenizer),
    attention_probs_dropout_prob = 0.1,
    hidden_dropout_prob =  0.1,
    hidden_size = 768,
    intermediate_size = 2048,
    layer_norm_eps = 1e-05,
    max_position_embeddings = 512,
    num_attention_heads = 12,
    num_hidden_layers = 12,
    position_bucket_size = 32,
)

model = LtgBertForMaskedLM(config)


training_args = TrainingArguments(
    output_dir=output_dir,
    overwrite_output_dir=True,
    save_strategy = "steps",
    save_steps=3000,
    evaluation_strategy = "steps",
    eval_steps=3000,
    per_device_train_batch_size=32768,    # Batch size for training
    per_device_eval_batch_size=32768,     # Batch size for evaluation
    gradient_accumulation_steps=1, 
    save_total_limit=3,  # Set to zero to avoid saving
    warmup_steps=500, 
    lr_scheduler_type="cosine",
    learning_rate=0.01,
    weight_decay=0.1,
    final_lr=0.001,
    max_steps=31250,       # Total number of steps
    max_seq_length=128,  
    logging_steps=500,
    max_grad_norm=2.0,
    fp16=True,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
)

def get_optimizer(model, training_args):
    # LAMB optimizer setup
    optimizer = optim.Lamb(
        model.parameters(),
        lr=training_args.learning_rate,
        betas=(0.9, 0.98),  # default betas for LAMB, can be changed
        eps=1e-6,
        weight_decay=training_args.weight_decay,
    )
    return optimizer

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,
    tokenizer=tokenizer,  # Pass the tokenizer to handle padding/truncation, etc.
    optimizers=(get_optimizer(model, training_args), None),
)

# Start training
trainer.train()

