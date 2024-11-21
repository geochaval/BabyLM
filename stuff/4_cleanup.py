import regex as re
import unicodedata
from pathlib import Path
from typing import Dict, Union, Callable
from tqdm import tqdm

# Define cleaning patterns
PATTERNS: Dict[str, tuple[str, Union[str, Callable]]] = {
    # Convert words with 2+ uppercase letters to title case (e.g., "ABC" → "Abc")
    'uppercase_words': (r'\b[A-Z]{2,}\b', lambda m: m.group(0).title()),

    # Remove all special characters
    'special_chars': (r'[^\p{L}\p{N}\p{Z}\p{P}\p{S}\n]', ''),
    
    # Remove zero-width spaces and other invisible Unicode characters
    'invisible_chars': (r'[\u200B-\u200D\uFEFF]', ''),
    
    # Standardize various types of quotation marks to straight double quotes
    'quotes': (r'[""''‹›«»]', '"'),
    
    # Standardize various types of apostrophes to straight single quote
    'apostrophes': (r'[`′´'']', "'"),
    
    # Remove parenthetical references containing "q.v." or "cf."
    # e.g., "(q.v. something)" or "(cf. something)" → ""
    'references': (r'\([^)]*(?:q\.v\.|cf\.)[^)]*\)', ''),
    
    # Standardize various types of dashes to simple hyphen
    'dashes': (r'[‒–—―]', '-'),
    
    # Remove spaces before punctuation marks and closing parenthesis
    # e.g., "word ," → "word,", "word )" → "word)"
    'space_before_punct': (r'\s*([,.!?:;)])', r'\1'),
    
    # Remove spaces after opening parenthesis and before closing parenthesis
    # e.g., "( word )" → "(word)"
    'paren_spaces': (r'(\()\s*|\s*(\))', r'\1\2'),
    
    # Replace multiple spaces with single space (preserving newlines)
    'whitespace': (r'[^\S\n]+', ' '),
    
    # Remove spaces at the start and end of each line
    'line_edges': (r'^ +| +$', ''),
    
    # Replace three or more consecutive newlines with just two
    'multiple_newlines': (r'\n{3,}', '\n\n'),
    
    # Replace multiple spaces with a single space
    # This is a final cleanup step after other replacements
    'extra_spaces': (r' +', ' ')
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