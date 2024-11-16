import os
import pathlib
from pathlib import Path

def combine_md_files():
    # Get the current file's directory (preprocessing folder)
    current_dir = Path(__file__).parent
    
    # Navigate to the directories
    datasets_dir = current_dir.parent / 'datasets'
    bmc_dir = datasets_dir / 'bnc_md'
    
    # Create output file path in the datasets directory
    output_file = datasets_dir / 'full_text.txt'
    
    # Check if bmc_md directory exists
    if not bmc_dir.exists():
        raise FileNotFoundError(f"BMC_MD directory not found at {bmc_dir}")
    
    # Initialize counter for processed files
    processed_files = 0
    
    # Open the output file in write mode
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # Recursively iterate through all subdirectories
        for md_file in bmc_dir.rglob('*.md'):
            try:
                # Read content from each MD file
                with open(md_file, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    
                # Write content to output file with just a newline separator
                outfile.write(content)
                outfile.write('\n')
                
                processed_files += 1
                
            except Exception as e:
                print(f"Error processing {md_file}: {str(e)}")
    
    print(f"Processing complete! Combined {processed_files} files into {output_file}")
    return processed_files

if __name__ == "__main__":
    try:
        num_files = combine_md_files()
        print(f"Successfully processed {num_files} files.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")