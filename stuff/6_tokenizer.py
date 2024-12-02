from pathlib import Path
from tokenizers import (Tokenizer, decoders, models, pre_tokenizers,
                       processors, trainers)
from tokenizers.normalizers import NFKC

def train_tokenizer():
    # Define paths
    corpus_path = Path("corpus_split/train.txt")
    output_dir = Path("models")
    output_dir.mkdir(exist_ok=True)

    # Initialize tokenizer with BPE (Byte-Pair Encoding) model
    # BPE is great for handling subword units and works well with most languages
    tokenizer = Tokenizer(models.BPE())

    # Set up the tokenizer components
    # ByteLevel components work well with UTF-8 text and handle spaces intelligently
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
    tokenizer.decoder = decoders.ByteLevel()
    tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)
    
    # NFKC normalization ensures consistent handling of unicode characters
    tokenizer.normalizer = NFKC()

    # Set up the trainer
    # We include <pad> as a special token even though it's not in your corpus
    # because it's often needed during model training for handling batches
    trainer = trainers.BpeTrainer(
        vocab_size=16000,          # Total size of vocabulary
        min_frequency=2,           # Token must appear at least twice to be included
        special_tokens=["<pad>", "<s>", "</s>"]  # Special tokens the model should know about
    )

    # Train the tokenizer on your corpus
    print("Training tokenizer...")
    tokenizer.train([str(corpus_path)], trainer)

    # Save the trained tokenizer
    tokenizer_path = output_dir / "tokenizer-clean.json"
    tokenizer.save(str(tokenizer_path), pretty=True)
    print(f"Tokenizer saved to {tokenizer_path}")

    # Let's test the tokenizer to make sure it works correctly
    print("\nTesting tokenizer with a sample from the corpus:")
    # Read first 100 characters of your corpus for testing
    sample_text = corpus_path.read_text()[:100]
    encoded = tokenizer.encode(sample_text)
    print(f"Sample encoded tokens: {encoded.tokens[:10]}...")  # Show first 10 tokens
    decoded = tokenizer.decode(encoded.ids)
    print(f"Decoded correctly? {sample_text[:50]} == {decoded[:50]}")

if __name__ == "__main__":
    train_tokenizer()