import regex as re
import unicodedata
from pathlib import Path
from typing import Dict, Union, Callable
from tqdm import tqdm

# Define cleaning patterns
PATTERNS: Dict[str, tuple[str, Union[str, Callable]]] = {
    # Convert words with 2+ uppercase letters to title case
    'uppercase_words': (r'\b\p{Lu}{2,}\b', lambda m: m.group(0).title()),
    
    # Remove problematic Unicode characters
    'special_chars': (r'[^\p{L}\p{N}\p{Z}\p{P}\p{S}\n]', ''),
    
    # Standardize whitespace and remove invisible characters
    'whitespace_cleanup': (r'[\u200B-\u200F\uFEFF\p{Z}]', ' '),
    
    # Standardize quotes and apostrophes
    'quotes': (r'[""''‹›«»]', '"'),
    'apostrophes': (r'[`′´'']', "'"),
    
    # Remove parenthetical references
    'references': (r'\([^)]*(?:q\.v\.|cf\.)[^)]*\)', ''),
    
    # Standardize dashes
    'dashes': (r'[‒–—―]', '-'),
    
    # Fix spacing around punctuation
    'space_before_punct': (r'\s*([,.!?:;)])', r'\1'),
    'paren_spaces': (r'(\()\s*|\s*(\))', r'\1\2'),
    
    # Clean up whitespace
    'whitespace': (r'^ +| +$|[^\S\n]+', ' '),
    'multiple_newlines': (r'\n{3,}', '\n\n')
}

# Compile patterns once at module level
COMPILED_PATTERNS = [
    (re.compile(pattern, re.MULTILINE if pattern.startswith('^') or pattern.endswith('$') else 0), replacement)
    for pattern, replacement in PATTERNS.values()
]

def clean_text(text: str) -> str:
    """Clean text using predefined patterns."""
    text = unicodedata.normalize('NFKD', text)
    
    # Show progress for each pattern
    for pattern, replacement in tqdm(COMPILED_PATTERNS, desc="Applying patterns"):
        if callable(replacement):
            text = pattern.sub(replacement, text)
        else:
            text = pattern.sub(replacement, text)
    
    return text.strip()

def process_file(input_file: str, output_file: str, encoding: str = 'utf-8') -> None:
    """Process a text file with progress indication."""
    input_path = Path(input_file)
    output_path = Path(output_file)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_file}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Show progress for file operations
    with tqdm(total=2, desc="Processing file") as pbar:
        # Reading file
        with open(input_path, 'r', encoding=encoding) as infile:
            pbar.set_description("Reading file")
            text = infile.read()
            pbar.update(1)
        
        # Cleaning and writing file
        cleaned_text = clean_text(text)
        with open(output_path, 'w', encoding=encoding) as outfile:
            pbar.set_description("Writing file")
            outfile.write(cleaned_text)
            pbar.update(1)

def main():
    try:
        process_file(
            "combined_encyclopedia.txt",
            "encyclopedia_cleaned.txt"
        )
    except Exception as e:
        print(f"\nError: {str(e)}")
        raise

if __name__ == "__main__":
    main()