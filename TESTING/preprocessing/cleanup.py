import os
import regex as re
from pathlib import Path

# File paths
INPUT_TRAIN = '../datasets/train.txt'
INPUT_VALID = '../datasets/validation.txt'

OUTPUT_TRAIN = '../pretrain/train_cleaned.txt'
OUTPUT_VALID = '../pretrain/validation_cleaned.txt'

# Compile regex patterns once
PATTERNS = {
    'nonstandard_chars': re.compile(r'[^a-zA-Z0-9\s.,!?\'":-]'),
    'multiple_spaces': re.compile(r'\s+'),
    'multiple_periods': re.compile(r'\.{3,}'),
    'multiple_puncts': re.compile(r'([!?])\1+'),
    'space_before_punct': re.compile(r'\s+([.,!?])')
}

def clean_text(text):
    """Clean and normalize text."""
    # Remove non-standard characters
    text = PATTERNS['nonstandard_chars'].sub('', text)
    
    # Normalize punctuation and spaces
    text = PATTERNS['multiple_spaces'].sub(' ', text)
    text = PATTERNS['multiple_periods'].sub('...', text)
    text = PATTERNS['multiple_puncts'].sub(r'\1', text)
    text = PATTERNS['space_before_punct'].sub(r'\1', text)
    
    # Add space after punctuation if missing
    for punct in '.,!?':
        text = text.replace(f'{punct}', f'{punct} ')
    
    # Final cleanup of any double spaces
    text = PATTERNS['multiple_spaces'].sub(' ', text)
    return text.strip()

def process_file(input_file, output_file):
    """Process a single file."""
    # Create output directory if needed
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    # Read and clean text
    with open(input_file, 'r', encoding='utf-8') as infile:
        text = infile.read()
    
    cleaned_text = clean_text(text)
    
    # Write cleaned text
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(cleaned_text)
    
    return len(text), len(cleaned_text)

def main():
    # Process training file
    print("\nCleaning training file...")
    orig_size, clean_size = process_file(INPUT_TRAIN, OUTPUT_TRAIN)
    print(f"Training file: {clean_size:,} chars (reduced from {orig_size:,})")
    
    # Process validation file
    print("\nCleaning validation file...")
    orig_size, clean_size = process_file(INPUT_VALID, OUTPUT_VALID)
    print(f"Validation file: {clean_size:,} chars (reduced from {orig_size:,})")

if __name__ == "__main__":
    main()