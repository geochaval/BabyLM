import os
from pathlib import Path

def count_words(text):
    return len(text.split())

def split_text_preserve_formatting(text, train_word_count):
    words = text.split()
    total_words_processed = 0
    current_position = 0
    
    # Find the position in original text where we hit our target word count
    while total_words_processed < train_word_count and current_position < len(text):
        if text[current_position].isspace():
            current_position += 1
            continue
            
        # Find the end of the current word
        word_end = current_position
        while word_end < len(text) and not text[word_end].isspace():
            word_end += 1
            
        total_words_processed += 1
        current_position = word_end
    
    # Split the text at that position, preserving all formatting
    train_text = text[:current_position]
    val_text = text[current_position:]
    
    return train_text, val_text

def main():
    # Get the current file's directory and navigate to datasets
    current_dir = Path(__file__).parent
    datasets_dir = current_dir.parent / 'datasets'
    input_file = datasets_dir / 'full_text.txt'
    
    # Check if input file exists
    if not input_file.exists():
        raise FileNotFoundError(f"Input file not found at {input_file}")
    
    # Read the full text
    with open(input_file, 'r', encoding='utf-8') as f:
        full_text = f.read()
    
    # Count total words
    total_words = count_words(full_text)
    print(f"\nTotal words in the text: {total_words:,}")
    
    # Get user input for split sizes
    while True:
        try:
            train_size = int(input("\nHow many words for training set? "))
            val_size = int(input("How many words for validation set? "))
            
            if train_size + val_size > total_words:
                print(f"\nError: Requested sizes ({train_size + val_size:,}) exceed total words ({total_words:,})")
                continue
                
            if train_size <= 0 or val_size <= 0:
                print("\nError: Please enter positive numbers")
                continue
                
            break
            
        except ValueError:
            print("\nError: Please enter valid numbers")
    
    # Split the text
    train_text, remaining_text = split_text_preserve_formatting(full_text, train_size)
    val_text, _ = split_text_preserve_formatting(remaining_text, val_size)
    
    # Create output files
    train_file = datasets_dir / 'train.txt'
    val_file = datasets_dir / 'validation.txt'
    
    # Save files
    with open(train_file, 'w', encoding='utf-8') as f:
        f.write(train_text)
    
    with open(val_file, 'w', encoding='utf-8') as f:
        f.write(val_text)
    
    # Print summary
    actual_train_words = count_words(train_text)
    actual_val_words = count_words(val_text)
    
    print("\nSplit complete!")
    print(f"Training set   : {actual_train_words:,} words saved to {train_file}")
    print(f"Validation set : {actual_val_words:,} words saved to {val_file}")
    print(f"Unused words   : {total_words - actual_train_words - actual_val_words:,}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")