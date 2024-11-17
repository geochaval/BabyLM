import json
import re
from pathlib import Path
from tqdm import tqdm

def should_skip_file(file_path: Path) -> bool:
    """
    Determine if a file should be skipped based on its location and name.
    """
    if "part_01" in str(file_path):
        if file_path.name == "1911 Encyclopædia Britannica.json":
            return True
        
        pattern = r"1911 Encyclopædia BritannicaVol \d+ .+ to .+\.json"
        if re.match(pattern, file_path.name):
            return True
    
    return False

def extract_content(text: str) -> str:
    """Extract content after the second occurrence of 'Volume'"""
    if not text:
        return ""
    
    parts = text.split('Volume')
    if len(parts) < 3:
        return ""
        
    content = parts[2]
    content = content.split('—', 1)[-1] if '—' in content else content
    return content.strip()

def process_json_file(json_path: Path, txt_path: Path) -> bool:
    """
    Process a single JSON file and return True if content was extracted
    """
    try:
        if should_skip_file(json_path):
            return False
            
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        content = extract_content(data.get('content', ''))
        if not content:
            return False
            
        txt_path.parent.mkdir(parents=True, exist_ok=True)
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
            
    except Exception as e:
        print(f"\nError processing {json_path}: {str(e)}")
        return False

def convert_dataset(source_dir: str = "britannica_data", target_dir: str = "britannica_txt") -> tuple[int, int, int]:
    """
    Convert all JSON files to TXT and return (processed_files, empty_files, skipped_files)
    """
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    
    # Get list of files and count skipped files first
    json_files = list(source_path.rglob("*.json"))
    skipped_files = sum(1 for f in json_files if should_skip_file(f))
    total_to_process = len(json_files) - skipped_files
    
    processed_files = 0
    empty_files = 0
    
    print(f"Found {len(json_files)} total files ({skipped_files} will be skipped)")
    
    with tqdm(total=total_to_process, desc="Converting files") as pbar:
        for json_path in json_files:
            if should_skip_file(json_path):
                continue
                
            relative_path = json_path.relative_to(source_path)
            txt_path = target_path / relative_path.with_suffix('.txt')
            
            if not process_json_file(json_path, txt_path):
                empty_files += 1
            
            processed_files += 1
            pbar.update(1)
    
    print(f"\nConversion complete!")
    print(f"Total files found: {len(json_files)}")
    print(f"Files skipped: {skipped_files}")
    print(f"Files processed: {processed_files}")
    print(f"Files with empty content: {empty_files}")
    print(f"Files converted: {processed_files - empty_files}")
    print(f"TXT files are available in: {target_path}")
    
    return processed_files, empty_files, skipped_files

if __name__ == "__main__":
    convert_dataset()