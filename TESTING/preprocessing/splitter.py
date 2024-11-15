import os
import glob
from pathlib import Path

# ============= CONFIGURATION PARAMETERS =============
INPUT_DIRECTORY = "../datasets/bnc"
TRAIN_FILE = "../datasets/train.txt"
VALIDATION_FILE = "../datasets/validation.txt"
ADD_FILE_SEPARATORS = True

# ============= WORD COUNTING FUNCTION =============
def count_total_words():
    """Count total words in all files before splitting."""
    total_words = 0
    total_files = 0
    all_files = list(glob.glob(f"{INPUT_DIRECTORY}/*/*/*.md"))
    
    for file_path in all_files:
        with open(file_path, 'r', encoding="utf-8") as infile:
            filtered_content = [
                line for line in infile.read().splitlines()
                if not line.lstrip().startswith('#')
            ]
            content = '\n'.join(filtered_content)
            words = content.split()
            total_words += len(words)
            total_files += 1
    
    return total_words, total_files, all_files

def get_user_split_sizes(total_words):
    """Get user input for train and validation split sizes."""
    while True:
        print(f"Total words available: {total_words:,}")
        try:
            train_size = int(input("How many words for training dataset? "))
            valid_size = int(input("How many words for validation dataset? "))
            
            total_requested = train_size + valid_size
            
            if total_requested > total_words:
                print(f"Error: Requested total ({total_requested:,}) exceeds available words ({total_words:,})")
                print("Please enter smaller values.")
                continue
                
            if train_size <= 0 or valid_size <= 0:
                print("Error: Please enter positive numbers for both splits.")
                continue
            
            # Show split percentages
            train_percent = (train_size / total_words) * 100
            valid_percent = (valid_size / total_words) * 100
            unused_percent = 100 - train_percent - valid_percent
            
            print("\nSplit Summary:")
            print(f"Training:   {train_size:,} words ({train_percent:.1f}%)")
            print(f"Validation: {valid_size:,} words ({valid_percent:.1f}%)")
            print(f"Unused:     {total_words - total_requested:,} words ({unused_percent:.1f}%)")
            
            confirm = input("\nProceed with this split? (y/n): ")
            if confirm.lower() == 'y':
                return train_size, valid_size
                
        except ValueError:
            print("Error: Please enter valid numbers.")

# ============= SCRIPT EXECUTION =============
# Count total words
total_word_count, total_file_count, all_files = count_total_words()

# Get user input for split sizes
TRAIN_WORD_LIMIT, VALID_WORD_LIMIT = get_user_split_sizes(total_word_count)

train_word_count = 0
valid_word_count = 0
files_processed = 0

def get_partial_content(words, limit_remaining):
    """Helper function to get exact number of words needed"""
    return ' '.join(words[:limit_remaining]) + '\n'

# Create output directories if they don't exist
os.makedirs(os.path.dirname(TRAIN_FILE), exist_ok=True)
os.makedirs(os.path.dirname(VALIDATION_FILE), exist_ok=True)

with open(TRAIN_FILE, 'w', newline='\n', encoding="utf-8") as train_out, \
     open(VALIDATION_FILE, 'w', newline='\n', encoding="utf-8") as valid_out:

    for file_path in all_files:
        with open(file_path, 'r', encoding="utf-8") as infile:
            filtered_content = [
                line for line in infile.read().splitlines()
                if not line.lstrip().startswith('#')
            ]
            content = '\n'.join(filtered_content)
            words = content.split()
            word_count = len(words)

        file_separator = '\n\n' if ADD_FILE_SEPARATORS else '\n'
        
        # Handle training set
        if train_word_count < TRAIN_WORD_LIMIT:
            remaining_train = TRAIN_WORD_LIMIT - train_word_count
            if word_count <= remaining_train:
                # Add entire file
                train_out.write(content + file_separator)
                train_word_count += word_count
            else:
                # Add partial file to exactly hit the limit
                partial_content = get_partial_content(words, remaining_train)
                train_out.write(partial_content)
                train_word_count = TRAIN_WORD_LIMIT
                
                # Add remaining words to validation if needed
                remaining_words = words[remaining_train:]
                if valid_word_count < VALID_WORD_LIMIT:
                    remaining_valid = VALID_WORD_LIMIT - valid_word_count
                    valid_out.write('\n')  # Ensure clean separation
                    if len(remaining_words) <= remaining_valid:
                        valid_out.write(' '.join(remaining_words) + file_separator)
                        valid_word_count += len(remaining_words)
                    else:
                        valid_out.write(' '.join(remaining_words[:remaining_valid]) + '\n')
                        valid_word_count = VALID_WORD_LIMIT
                        break
                
        # Handle validation set
        elif valid_word_count < VALID_WORD_LIMIT:
            remaining_valid = VALID_WORD_LIMIT - valid_word_count
            if word_count <= remaining_valid:
                # Add entire file
                valid_out.write(content + file_separator)
                valid_word_count += word_count
            else:
                # Add partial file to exactly hit the limit
                partial_content = get_partial_content(words, remaining_valid)
                valid_out.write(partial_content)
                valid_word_count = VALID_WORD_LIMIT
                break
        else:
            break

        files_processed += 1

# Print final results
print("\nDataset splitting complete!")
print(f"Train file created with {train_word_count:,} words")
print(f"Validation file created with {valid_word_count:,} words")