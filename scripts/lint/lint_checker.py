import os
import re
from pathlib import Path

dirs = ["ado_fin", "ado_fl_dev", "ado_ls_dev", "ado_otp"]
issues = {
    "trailing_whitespace": [],
    "setext_headings": [],
    "missing_blank_before_heading": [],
    "missing_blank_after_heading": [],
    "missing_blank_before_code": [],
    "missing_blank_after_code": [],
    "list_formatting": [],
    "broken_links": [],
    "broken_images": []
}

files_to_process = []
for directory in dirs:
    dir_path = Path(directory)
    for md_file in sorted(dir_path.rglob("*.md")):
        files_to_process.append(str(md_file))

print(f"Total files found: {len(files_to_process)}")

# Check first 10 files for issues
for idx, file_path in enumerate(files_to_process[:10]):
    print(f"\n[{idx+1}] {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
        # Check for trailing whitespace
        trailing_ws = []
        for i, line in enumerate(lines, 1):
            if line and line[-1] in ' \t':
                trailing_ws.append(i)
        if trailing_ws:
            print(f"  - Trailing whitespace on lines: {trailing_ws[:3]}")
            
        # Check for Setext headings
        setext = []
        for i in range(len(lines)-1):
            if lines[i] and re.match(r'^=+\s*$', lines[i+1]) and i > 0:
                setext.append(i+1)
            elif lines[i] and re.match(r'^-+\s*$', lines[i+1]) and i > 0 and not re.match(r'^- ', lines[i]):
                setext.append(i+1)
        if setext:
            print(f"  - Setext headings at lines: {setext[:3]}")
            
    except Exception as e:
        print(f"  - Error: {e}")

print(f"\nProcessed first 10 files.")
