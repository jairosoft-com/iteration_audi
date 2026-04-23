import os
import re
from pathlib import Path
from collections import defaultdict

dirs = ["ado_fin", "ado_fl_dev", "ado_ls_dev", "ado_otp"]
files_list = []
for directory in dirs:
    dir_path = Path(directory)
    for md_file in sorted(dir_path.rglob("*.md")):
        files_list.append(str(md_file))

print(f"Total files to process: {len(files_list)}\n")

# Initialize counters
stats = {
    "filesProcessed": 0,
    "issuesFixed": 0,
    "errors": [],
    "unfixableIssues": []
}

rule_counts = defaultdict(int)

for idx, file_path in enumerate(files_list, 1):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        stats["filesProcessed"] += 1
        
        # Rule 1: Setext headings (detect, not fixing in this pass)
        for i in range(len(lines)-1):
            if lines[i] and i > 0:
                if re.match(r'^=+\s*$', lines[i+1]):
                    rule_counts["setext_h1"] += 1
                    stats["unfixableIssues"].append({
                        "filePath": file_path,
                        "line": i+1,
                        "rule": "inconsistent-heading-style",
                        "description": f"Setext-style H1 heading at line {i+1}"
                    })
                elif re.match(r'^-{3,}\s*$', lines[i+1]) and not lines[i].startswith('-') and not re.match(r'^-{3,}\s*$', lines[i]):
                    if lines[i].strip():
                        rule_counts["setext_h2"] += 1
                        stats["unfixableIssues"].append({
                            "filePath": file_path,
                            "line": i+1,
                            "rule": "inconsistent-heading-style",
                            "description": f"Setext-style H2 heading at line {i+1}"
                        })
        
        # Rule 3 & 4: Check blank lines around headings and code blocks
        for i, line in enumerate(lines):
            if line.startswith('#') and line[1] == ' ':
                # ATX heading found
                if i > 0 and lines[i-1].strip() and not lines[i-1].startswith('#'):
                    rule_counts["missing_blank_before_heading"] += 1
                if i < len(lines)-1 and lines[i+1].strip() and not lines[i+1].startswith('#') and not lines[i+1].startswith('```'):
                    rule_counts["missing_blank_after_heading"] += 1
            
            if line.startswith('```'):
                # Code block delimiter
                if i > 0 and lines[i-1].strip() and not lines[i-1].startswith('```'):
                    rule_counts["missing_blank_before_code"] += 1
                if i < len(lines)-1 and lines[i+1].strip() and not lines[i+1].startswith('```'):
                    # Check if this is a closing ```
                    if i > 0:
                        in_code = False
                        for j in range(i-1, -1, -1):
                            if lines[j].startswith('```'):
                                in_code = True
                                break
                        if in_code:
                            rule_counts["missing_blank_after_code"] += 1
        
        # Rule 5: List formatting (check for inconsistent markers)
        list_markers = set()
        for line in lines:
            if re.match(r'^(\s*)[-*+]\s', line):
                m = re.match(r'^(\s*)([-*+])\s', line)
                if m:
                    indent = len(m.group(1))
                    marker = m.group(2)
                    list_markers.add((indent // 2, marker))
        
        # Check for mixed markers at same level
        level_markers = defaultdict(set)
        for level, marker in list_markers:
            level_markers[level].add(marker)
        
        for level, markers in level_markers.items():
            if len(markers) > 1:
                rule_counts["inconsistent_list_markers"] += 1
        
        # Rule 6: Broken link references (detect)
        link_refs = set()
        for line in lines:
            matches = re.findall(r'\[([^\]]+)\]\[([^\]]+)\]', line)
            for text, ref in matches:
                link_refs.add(ref.lower())
        
        ref_defs = set()
        for line in lines:
            m = re.match(r'^\[([^\]]+)\]:\s+', line)
            if m:
                ref_defs.add(m.group(1).lower())
        
        for ref in link_refs:
            if ref not in ref_defs:
                rule_counts["broken_link_ref"] += 1
                stats["unfixableIssues"].append({
                    "filePath": file_path,
                    "line": "unknown",
                    "rule": "broken-link-reference",
                    "description": f"Link reference [{ref}] has no corresponding definition"
                })
        
        # Rule 7: Broken image references (detect)
        img_refs = set()
        for line in lines:
            matches = re.findall(r'!\[([^\]]*)\]\[([^\]]+)\]', line)
            for alt, ref in matches:
                img_refs.add(ref.lower())
        
        for ref in img_refs:
            if ref not in ref_defs:
                rule_counts["broken_img_ref"] += 1
                stats["unfixableIssues"].append({
                    "filePath": file_path,
                    "line": "unknown",
                    "rule": "broken-image-reference",
                    "description": f"Image reference ![...][{ref}] has no corresponding definition"
                })
        
        if idx % 30 == 0:
            print(f"[Agent-2] Processing file {idx}/{len(files_list)} ({100*idx/len(files_list):.1f}%): {file_path}")
        
    except Exception as e:
        stats["errors"].append({
            "filePath": file_path,
            "operation": "read",
            "message": str(e)
        })

print(f"\n=== COMPREHENSIVE LINTING REPORT ===\n")
print(f"Files processed: {stats['filesProcessed']}")
print(f"Issues fixed so far: {stats['issuesFixed']}")
print(f"Unfixable issues detected: {len(stats['unfixableIssues'])}")
print(f"Errors: {len(stats['errors'])}")

print(f"\nIssue breakdown by rule:")
for rule, count in sorted(rule_counts.items()):
    if count > 0:
        print(f"  - {rule}: {count}")

if stats['unfixableIssues']:
    print(f"\nSample unfixable issues (first 5):")
    for issue in stats['unfixableIssues'][:5]:
        print(f"  - {issue['filePath']}: {issue['rule']} - {issue['description']}")

print(f"\nAgent-2 assignment: {len(files_list)} files total")
print(f"Completion: {100*stats['filesProcessed']/len(files_list):.1f}%")

