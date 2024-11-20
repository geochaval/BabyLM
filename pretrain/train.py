from transformers import PreTrainedTokenizerFast, Trainer, TrainingArguments
from datasets import Dataset
from tokenizers import Tokenizer
from modeling_ltgbert import LtgBertForMaskedLM
from configuration_ltgbert import LtgBertConfig
import os
import torch_optimizer as optim
from transformers import DataCollatorForLanguageModeling

tokenizer_file = './bpe.json'
train_file = '../datasets/train_cleaned.txt'
eval_file = '../datasets/validation_cleaned.txt'
output_dir = os.path.abspath('../models')

os.makedirs(output_dir, exist_ok=True)

bpe_tokenizer = Tokenizer.from_file(tokenizer_file)

tokenizer = PreTrainedTokenizerFast(tokenizer_object=bpe_tokenizer,
                                    truncation=True,     # Truncate to model's max length
                                    max_length=128,      # Adjust based on your model
                                    padding="max_length",
                                    )
tokenizer.pad_token = "<PAD>"  # Ensure special tokens are set
tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("<PAD>")
tokenizer.eos_token = "<EOS>"
tokenizer.eos_token_id = tokenizer.convert_tokens_to_ids("<EOS>")
tokenizer.bos_token = "<BOS>"
tokenizer.bos_token_id = tokenizer.convert_tokens_to_ids("<BOS>")
tokenizer.mask_token = "<MASK>"
tokenizer.mask_token_id = tokenizer.convert_tokens_to_ids("<MASK>")

def tokenize(dataset):
    return tokenizer(
        dataset["text"],          # or text.splitlines() or [text] for full text
        truncation=True,     # Truncate to model's max length
        max_length=128,      # Adjust based on your model
        padding="max_length", # Pad to the model's max length
        add_special_tokens=True,
    )

with open(train_file, "r", encoding="utf-8") as file:
    train_text = file.read()

paragraphs = train_text.split('\n\n')

train_dataset = Dataset.from_dict({"text": paragraphs})

tokenized_train_dataset = train_dataset.map(tokenize, batched=True)

train_dataset = tokenized_train_dataset.remove_columns(["text"])

with open(eval_file, "r", encoding="utf-8") as file:
    eval_text = file.read()

paragraphs = eval_text.split('\n\n')

valid_dataset = Dataset.from_dict({"text": paragraphs})

tokenized_valid_dataset = valid_dataset.map(tokenize, batched=True)

valid_dataset = tokenized_valid_dataset.remove_columns(["text"])

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
print("model configured")
model = LtgBertForMaskedLM(config)


training_args = TrainingArguments(
    output_dir=output_dir,
    report_to=[],
    overwrite_output_dir=True,
    save_strategy = "steps",
    save_steps=500,
    eval_strategy = "steps",
    eval_steps=500,
    per_device_train_batch_size=2**6,    # Batch size for training
    per_device_eval_batch_size=2**6,     # Batch size for evaluation
    gradient_accumulation_steps=1, 
    save_total_limit=3,  # Set to zero to avoid saving
    warmup_steps=500, 
    lr_scheduler_type="cosine",
    learning_rate=0.01,
    weight_decay=0.1,
    max_steps=31250*(2**9),       # Total number of steps
    logging_steps=500,
    max_grad_norm=2.0,
    fp16=True,
    load_best_model_at_end=True,
    metric_for_best_model="eval_loss",
    remove_unused_columns=False,
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

class CustomDataCollatorForMLM(DataCollatorForLanguageModeling):
    def __call__(self, features):
        # Apply the original data collator logic
        batch = super().__call__(features)
        
        # Remove token_type_ids if they exist
        if 'token_type_ids' in batch:
            del batch['token_type_ids']
        
        return batch
    
data_collator = CustomDataCollatorForMLM(
    tokenizer=tokenizer,
    mlm=True,  # Use MLM (Masked Language Modeling)
    mlm_probability=0.15,  # Probability of masking tokens
)
# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=valid_dataset,
    tokenizer=tokenizer,  # Pass the tokenizer to handle padding/truncation, etc.
    optimizers=(get_optimizer(model, training_args), None),
    data_collator=data_collator,
)
print("train start")
# Start training
trainer.train()

