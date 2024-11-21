from pathlib import Path
from tokenizers import (
    Tokenizer, 
    decoders, 
    models, 
    pre_tokenizers,
    processors, 
    trainers
)
from tokenizers.normalizers import NFKC
from collections import Counter
import json

def create_byte_level_bpe_tokenizer(vocab_size: int, min_frequency: int = 2):
    """Create a byte-level BPE tokenizer with specified configuration"""
    tokenizer = Tokenizer(models.BPE())
    
    # Set up tokenizer components
    tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
    tokenizer.decoder = decoders.ByteLevel()
    tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)
    tokenizer.normalizer = NFKC()
    
    # Configure trainer with special tokens
    trainer = trainers.BpeTrainer(
        vocab_size=vocab_size,
        min_frequency=min_frequency,
        special_tokens=["<pad>", "<s>", "</s>"],
        show_progress=True
    )
    
    return tokenizer, trainer

def analyze_token_distribution(tokenizer, file_path: str):
    """Analyze token distribution in the dataset"""
    token_counts = Counter()
    print("Analyzing token distribution...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
        encoded = tokenizer.encode(text)
        token_counts.update(encoded.ids)
    
    # Calculate statistics
    total_tokens = sum(token_counts.values())
    unique_tokens = len(token_counts)
    tokens_with_100_or_more = sum(1 for count in token_counts.values() if count >= 100)
    percentage = (tokens_with_100_or_more / unique_tokens) * 100
    
    return {
        'total_tokens': total_tokens,
        'unique_tokens': unique_tokens,
        'tokens_with_100_or_more': tokens_with_100_or_more,
        'percentage': percentage
    }

def test_tokenizer(tokenizer, text=None):
    """Test the tokenizer on a sample text"""
    if text is None:
        text = "The quick brown fox jumps over the lazy dog."
    
    encoded = tokenizer.encode(text)
    
    print("\n=== Tokenizer Test ===")
    print(f"Original text: {text}")
    print(f"Encoded String: {encoded.tokens}")
    print(f"Encoded IDs: {encoded.ids}")
    print(f"Decoded String: {tokenizer.decode(encoded.ids)}")

def main():
    # Setup paths
    data_dir = Path("corpus_split")
    output_dir = Path("models")
    output_dir.mkdir(exist_ok=True)
    
    # Get training files
    train_path = data_dir / "train.txt"
    assert train_path.exists(), "Training file not found"
    
    # Set tokenizer parameters
    VOCAB_SIZE = 16000
    MIN_FREQUENCY = 2
    
    # Create and train tokenizer
    print(f"Training tokenizer with vocabulary size {VOCAB_SIZE}...")
    tokenizer, trainer = create_byte_level_bpe_tokenizer(VOCAB_SIZE, MIN_FREQUENCY)
    tokenizer.train([str(train_path)], trainer)
    
    # Analyze distribution
    stats = analyze_token_distribution(tokenizer, str(train_path))
    
    # Print statistics
    print("\n=== Vocabulary Statistics ===")
    print(f"Total tokens in corpus: {stats['total_tokens']:,}")
    print(f"Unique tokens (vocabulary size): {stats['unique_tokens']:,}")
    print(f"Tokens with ≥100 examples: {stats['tokens_with_100_or_more']:,}")
    print(f"Percentage of tokens with ≥100 examples: {stats['percentage']:.2f}%")
    
    # Test tokenizer
    test_tokenizer(tokenizer)
    
    # Save tokenizer
    tokenizer_path = output_dir / "tokenizer-clean.json"
    tokenizer.save(str(tokenizer_path), pretty=True)
    print(f"\nTokenizer saved to {tokenizer_path}")

if __name__ == "__main__":
    main()