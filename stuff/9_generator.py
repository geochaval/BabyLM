from transformers import LlamaForCausalLM, GPT2TokenizerFast, LlamaConfig
from safetensors import safe_open
import torch

def generate_text(
    prompt,
    model_path="models/Baby-Llama",
    tokenizer_path="models/tokenizer-clean.json",
    max_length=100
):
    # Load tokenizer
    tokenizer = GPT2TokenizerFast(tokenizer_file=tokenizer_path)
    tokenizer.bos_token = "<s>"
    tokenizer.eos_token = "</s>"
    tokenizer.pad_token = "<pad>"
    print("Tokenizer loaded")

    # Create model with exact same config as training
    config = LlamaConfig(
        vocab_size=tokenizer.vocab_size,
        hidden_size=512,
        num_hidden_layers=16,
        intermediate_size=1024,
        num_attention_heads=8,
        max_position_embeddings=256
    )
    
    # Initialize model
    #model = LlamaForCausalLM(config)
    model = LlamaForCausalLM.from_pretrained(model_path)
    print("Model loaded")

    # Set device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()
    print(device)

    # Generate
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        temperature=0.7,
        do_sample=True,
        top_p=0.95
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Test it
if __name__ == "__main__":
    prompt = "<s> London was"
    try:
        text = generate_text(prompt)
        print(f"Generated: {text}")
    except Exception as e:
        print(f"Error: {str(e)}")
