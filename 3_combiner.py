import re
from pathlib import Path
from tqdm import tqdm

def remove_header(text: str) -> str:
    """Remove the title/header and return the main content."""
    # Split on zero-width space if present
    if '\u200b' in text:
        parts = text.split('\u200b', 1)  # Split on first occurrence
        return parts[1].strip() if len(parts) > 1 else text.strip()
    return text.strip()

def clean_text(text: str) -> str:
    """Clean up text by removing extra whitespace."""
    # Simply join all lines and normalize whitespace
    content = ' '.join(text.splitlines())
    content = re.sub(r'\s+', ' ', content)
    return content.strip()

def get_number_from_path(path: Path) -> int:
    """Extract the numeric part from a path name (e.g., 'volume_01' -> 1)."""
    match = re.search(r'_(\d+)', path.name)
    return int(match.group(1)) if match else 0

def process_directory(source_dir: str, output_file: str, clean_files: bool = True) -> tuple[int, int]:
    """
    Process encyclopedia files: remove headers, clean them and combine into a single file.
    Returns (total_processed, total_errors)
    """
    root_path = Path(source_dir)
    total_processed = 0
    total_errors = 0
    
    # Get and sort volumes numerically
    volumes = sorted(
        [d for d in root_path.iterdir() if d.is_dir()],
        key=get_number_from_path
    )
    
    # Count total files
    total_files = sum(
        len(list(part.glob('*.txt')))
        for volume in volumes
        for part in volume.iterdir()
        if part.is_dir()
    )
    
    print(f"Found {len(volumes)} volumes containing {total_files} files to process...")
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        with tqdm(total=total_files, desc="Processing files") as pbar:
            for volume in volumes:
                # Sort parts numerically (part_01, part_02, etc.)
                parts = sorted(
                    [d for d in volume.iterdir() if d.is_dir()],
                    key=get_number_from_path
                )
                
                for part in parts:
                    # Sort text files numerically/alphabetically
                    txt_files = sorted(part.glob('*.txt'))
                    
                    for txt_file in txt_files:
                        try:
                            with open(txt_file, 'r', encoding='utf-8') as infile:
                                content = infile.read()
                            
                            # First remove the header
                            content = remove_header(content)
                            
                            # Then apply the cleaning if requested
                            if clean_files:
                                content = clean_text(content)
                                
                            if clean_files:  # Write back cleaned content
                                with open(txt_file, 'w', encoding='utf-8') as f:
                                    f.write(content)
                                    
                            outfile.write(content + "\n\n")  # Add double newline between articles
                            total_processed += 1
                            pbar.update(1)
                            
                        except Exception as e:
                            print(f"\nError processing {txt_file}: {str(e)}")
                            total_errors += 1
                            pbar.update(1)
                            continue
    
    print(f"\nProcessing complete!")
    print(f"Total files processed: {total_processed}")
    print(f"Total errors encountered: {total_errors}")
    print(f"Combined encyclopedia is available at: {output_file}")
    
    return total_processed, total_errors

def main():
    source_dir = "britannica_txt"
    output_file = "combined_encyclopedia.txt"
    clean_files = True
    process_directory(source_dir, output_file, clean_files)

if __name__ == "__main__":
    main()