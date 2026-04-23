import os
import re
from pathlib import Path

dirs = ["ado_fin", "ado_fl_dev", "ado_ls_dev", "ado_otp"]
files_to_process = []
for directory in dirs:
    dir_path = Path(directory)
    for md_file in sorted(dir_path.rglob("*.md")):
        files_to_process.append(str(md_file))

print(f"Found {len(files_to_process)} markdown files")

issues_found = []
files_processed = 0
total_issues = 0

for file_path in files_to_process:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
            
        file_issues = 0
        
        # Rule 1: Setext headings (convert to ATX)
        for i in range(len(lines)-1):
            if lines[i] and i > 0:
                if re.match(r'^=+\s*$', lines[i+1]):
                    issues_found.append(f"{file_path}:{i+1}: setext-h1")
                    file_issues += 1
                elif re.match(r'^-{3,}\s*$', lines[i+1]) and not re.match(r'^-\s', lines[i]) and not re.match(r'^---\s*$', lines[i]):
                    # Avoid false positives for horizontal rules
                    prev_text = lines[i].strip()
                    if prev_text and len(prev_text) > 0:
                        issues_found.append(f"{file_path}:{i+1}: setext-h2")
                        file_issues += 1
        
        # Rule 2: Trailing whitespace
        for i, line in enumerate(lines, 1):
            if line and (line[-1] == ' ' or line[-1] == '\t'):
                issues_found.append(f"{file_path}:{i}: trailing-whitespace")
                file_issues += 1
        
        files_processed += 1
        total_issues += file_issues
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

print(f"\nProcessed: {files_processed} files")
print(f"Total issues found: {total_issues}")

if issues_found:
    print(f"\nIssue summary (first 20):")
    for issue in issues_found[:20]:
        print(f"  {issue}")
else:
    print("\nNo linting issues detected in the first comprehensive scan.")

