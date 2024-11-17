import re
from collections import Counter
from pathlib import Path
from math import log
import string

def calculate_statistics(file_path):
    """Calculate comprehensive statistics useful for LLM training preparation."""
    
    print(f"Analyzing file: {file_path}")
    print("=" * 50)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    # Basic file stats
    file_size_bytes = Path(file_path).stat().st_size
    file_size_mb = file_size_bytes / (1024 * 1024)
    total_chars = len(text)
    total_lines = len(text.split('\n'))
    
    print("\n1. BASIC FILE STATISTICS")
    print("-" * 30)
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"Total characters: {total_chars:,}")
    print(f"Total lines: {total_lines:,}")
    print(f"Average chars per line: {total_chars/total_lines:.2f}")
    
    # Word-level analysis
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words))
    word_freq = Counter(words)
    
    print("\n2. WORD STATISTICS")
    print("-" * 30)
    print(f"Total words: {total_words:,}")
    print(f"Unique words: {unique_words:,}")
    print(f"Vocabulary richness (unique/total): {(unique_words/total_words)*100:.2f}%")
    print(f"Average word length: {sum(len(word) for word in words) / total_words:.2f} characters")
    
    # Frequency distributions
    hapax_legomena = sum(1 for word, count in word_freq.items() if count == 1)
    dis_legomena = sum(1 for word, count in word_freq.items() if count == 2)
    high_freq_words = sum(1 for word, count in word_freq.items() if count >= 100)
    
    print("\n3. FREQUENCY DISTRIBUTIONS")
    print("-" * 30)
    print(f"Words appearing once: {hapax_legomena:,} ({(hapax_legomena/unique_words)*100:.2f}%)")
    print(f"Words appearing twice: {dis_legomena:,} ({(dis_legomena/unique_words)*100:.2f}%)")
    print(f"Words appearing 100+ times: {high_freq_words:,}")
    print("\nTop 20 most frequent words:")
    for word, count in word_freq.most_common(20):
        print(f"{word}: {count:,} ({(count/total_words)*100:.2f}%)")
    
    # Sentence analysis
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    total_sentences = len(sentences)
    sentence_lengths = [len(re.findall(r'\b\w+\b', s)) for s in sentences]
    avg_sentence_length = sum(sentence_lengths) / total_sentences
    max_sentence_length = max(sentence_lengths)
    min_sentence_length = min(sentence_lengths)
    
    print("\n4. SENTENCE STATISTICS")
    print("-" * 30)
    print(f"Total sentences: {total_sentences:,}")
    print(f"Average sentence length: {avg_sentence_length:.2f} words")
    print(f"Shortest sentence: {min_sentence_length} words")
    print(f"Longest sentence: {max_sentence_length} words")
    
    # Character-level analysis
    char_freq = Counter(text)
    
    print("\n5. CHARACTER STATISTICS")
    print("-" * 30)
    print("Character type distribution:")
    print(f"Letters: {sum(c.isalpha() for c in text):,}")
    print(f"Digits: {sum(c.isdigit() for c in text):,}")
    print(f"Whitespace: {sum(c.isspace() for c in text):,}")
    print(f"Punctuation: {sum(c in string.punctuation for c in text):,}")
    
    # Text complexity metrics
    word_lengths = [len(word) for word in words]
    avg_word_length = sum(word_lengths) / len(word_lengths)
    
    # Type-Token Ratio (TTR)
    ttr = unique_words / total_words
    
    # Calculate entropy
    prob_dist = [count/total_words for count in word_freq.values()]
    entropy = -sum(p * log(p, 2) for p in prob_dist)
    
    print("\n6. COMPLEXITY METRICS")
    print("-" * 30)
    print(f"Type-Token Ratio: {ttr:.4f}")
    print(f"Vocabulary Entropy: {entropy:.2f} bits")
    print(f"Average Word Length: {avg_word_length:.2f}")
    
    # Sequence Analysis (useful for tokenization)
    bigrams = Counter(zip(words, words[1:]))
    repeated_bigrams = sum(1 for count in bigrams.values() if count > 1)
    
    print("\n7. SEQUENCE ANALYSIS")
    print("-" * 30)
    print(f"Unique bigrams: {len(bigrams):,}")
    print(f"Repeated bigrams: {repeated_bigrams:,}")
    print("\nMost common bigrams:")
    for (w1, w2), count in bigrams.most_common(10):
        print(f"'{w1} {w2}': {count:,}")

if __name__ == "__main__":
    calculate_statistics("encyclopedia_cleaned.txt")