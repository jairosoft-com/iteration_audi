import os
import re
from pathlib import Path

dirs = ["ado_fin", "ado_fl_dev", "ado_ls_dev", "ado_otp"]
files_to_process = []
for directory in dirs:
    dir_path = Path(directory)
    for md_file in sorted(dir_path.rglob("*.md")):
        files_to_process.append(str(md_file))

print(f"Processing {len(files_to_process)} files for code block spacing fixes...\n")

files_fixed = 0
issues_fixed = 0
errors = []

for idx, file_path in enumerate(files_to_process, 1):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        modified = False
        new_lines = []
        i = 0
        
        while i < len(lines):
            line = lines[i]
            new_lines.append(line)
            
            # Check if this is a code block opening
            if line.strip().startswith('```'):
                # Check if previous line needs a blank line
                if i > 0 and new_lines[-2].strip() and not new_lines[-2].strip().startswith('```'):
                    # Need to insert blank line before ``` 
                    if not new_lines[-2].strip().endswith('\n'):
                        new_lines.insert(-1, '\n')
                        modified = True
                        issues_fixed += 1
                
                # Find the closing ```
                j = i + 1
                code_block_end = None
                while j < len(lines):
                    if lines[j].strip().startswith('```'):
                        code_block_end = j
                        break
                    j += 1
                
                # Add lines between ``` markers
                while i + 1 < len(lines) and i < code_block_end:
                    i += 1
                    new_lines.append(lines[i])
                
                # Check if next line after closing ``` needs blank line
                if i < len(lines) - 1:
                    next_line_idx = i + 1
                    if next_line_idx < len(lines) and lines[next_line_idx].strip() and not lines[next_line_idx].strip().startswith('```'):
                        # Insert blank line if not already there
                        if new_lines[-1].strip():
                            new_lines.append('\n')
                            modified = True
                            issues_fixed += 1
            
            i += 1
        
        if modified:
            with open(file_path, 'w') as f:
                f.writelines(new_lines)
            files_fixed += 1
            if idx % 30 == 0:
                print(f"[Agent-2] Processing file {idx}/{len(files_to_process)} ({100*idx/len(files_to_process):.1f}%): Fixed {file_path}")
        
    except Exception as e:
        errors.append({"file": file_path, "error": str(e)})

print(f"\n=== CODE BLOCK SPACING FIX RESULTS ===")
print(f"Files processed: {len(files_to_process)}")
print(f"Files fixed: {files_fixed}")
print(f"Issues fixed: {issues_fixed}")
print(f"Errors: {len(errors)}")

if errors:
    print(f"\nErrors encountered (first 3):")
    for err in errors[:3]:
        print(f"  - {err['file']}: {err['error']}")

