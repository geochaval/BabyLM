import random
from pathlib import Path
import re
from tqdm import tqdm

def count_words(text):
    """Count words in text using simple whitespace splitting"""
    return len(text.split())

def split_into_articles(text):
    """Split text into articles based on newline boundaries"""
    articles = [article.strip() for article in text.split('\n\n') if article.strip()]
    return articles

def format_for_llm(articles):
    """Format articles for LLM training by adding start/end tokens between articles"""
    # Join articles with end token + start token combination
    formatted_articles = " </s> <s> ".join(articles)
    # Add start token at beginning and end token at the end
    return f"<s> {formatted_articles} </s>"

def create_dataset(articles, target_words, desc):
    """
    Create a dataset with approximately target_words by randomly selecting articles
    Returns the selected articles and actual word count
    """
    selected_articles = []
    current_words = 0
    available_articles = articles.copy()
    
    pbar = tqdm(total=target_words, desc=desc, unit='words')
    while current_words < target_words and available_articles:
        article = random.choice(available_articles)
        available_articles.remove(article)
        article_words = count_words(article)
        current_words += article_words
        selected_articles.append(article)
        pbar.n = min(current_words, target_words)
        pbar.refresh()
    pbar.close()
    
    return selected_articles, current_words

def main():
    output_dir = Path('corpus_split')
    output_dir.mkdir(exist_ok=True)
    
    print("Reading input file...")
    input_file = Path('encyclopedia_cleaned.txt')
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    print("Processing text...")
    articles = split_into_articles(text)
    total_words = count_words(text)
    print(f"\nTotal words in corpus: {total_words:,}")
    
    while True:
        try:
            train_words = int(input("\nHow many words for training set? "))
            val_words = int(input("How many words for validation set? "))
            if train_words + val_words > total_words:
                print(f"Error: Requested {train_words + val_words:,} words but corpus only has {total_words:,} words")
                continue
            break
        except ValueError:
            print("Please enter valid numbers")
    
    # Create datasets
    random.seed(42)
    print("\nCreating training set...")
    train_articles, actual_train_words = create_dataset(articles, train_words, "Creating training set")
    remaining_articles = [a for a in articles if a not in train_articles]
    print("\nCreating validation set...")
    val_articles, actual_val_words = create_dataset(remaining_articles, val_words, "Creating validation set")
    
    # Format articles for LLM training
    formatted_train = format_for_llm(train_articles)
    formatted_val = format_for_llm(val_articles)
    
    # Calculate percentages and unused words
    unused_words = total_words - actual_train_words - actual_val_words
    train_percent = (actual_train_words / total_words) * 100
    val_percent = (actual_val_words / total_words) * 100
    unused_percent = (unused_words / total_words) * 100
    
    # Write files
    print("\nWriting files...")
    with open(output_dir / 'train.txt', 'w', encoding='utf-8') as f:
        f.write(formatted_train)
    with open(output_dir / 'val.txt', 'w', encoding='utf-8') as f:
        f.write(formatted_val)
    
    # Print results with percentages
    print(f"\nDatasets created in '{output_dir}' directory:")
    print(f"\nData split:")
    print(f"Training: {actual_train_words:,} words ({train_percent:.1f}%)")
    print(f"Validation: {actual_val_words:,} words ({val_percent:.1f}%)")
    print(f"Unused: {unused_words:,} words ({unused_percent:.1f}%)")

if __name__ == "__main__":
    main()