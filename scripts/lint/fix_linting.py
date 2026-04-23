import os
import re
from pathlib import Path

dirs = ["ado_fin", "ado_fl_dev", "ado_ls_dev", "ado_otp"]
files_to_process = []
for directory in dirs:
    dir_path = Path(directory)
    for md_file in sorted(dir_path.rglob("*.md")):
        files_to_process.append(str(md_file))

print(f"Processing {len(files_to_process)} files for linting fixes...")

files_fixed = 0
issues_fixed = 0
errors = []
unfixable_issues = []

for file_path in files_to_process:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
            content = original_content
            lines = content.split('\n')
            
        file_modified = False
        
        # Rule 2: Fix trailing whitespace
        new_lines = []
        for line in lines:
            if line and (line[-1] == ' ' or line[-1] == '\t'):
                new_line = line.rstrip()
                new_lines.append(new_line)
                file_modified = True
                issues_fixed += 1
            else:
                new_lines.append(line)
        
        if file_modified:
            new_content = '\n'.join(new_lines)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            files_fixed += 1
            print(f"✓ Fixed {file_path}")
        
    except Exception as e:
        errors.append({"file": file_path, "error": str(e)})
        print(f"✗ Error in {file_path}: {e}")

print(f"\n=== LINTING RESULTS ===")
print(f"Files processed: {len(files_to_process)}")
print(f"Files fixed: {files_fixed}")
print(f"Issues fixed: {issues_fixed}")
print(f"Errors: {len(errors)}")

if errors:
    print(f"\nErrors encountered:")
    for err in errors[:5]:
        print(f"  - {err['file']}: {err['error']}")

