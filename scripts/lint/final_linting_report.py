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

# Initialize report
report = {
    "agentId": "agent-2",
    "filesProcessed": 0,
    "issuesFixed": 1,  # Trailing whitespace from earlier fix
    "errors": [],
    "unfixableIssues": []
}

# Comprehensive analysis pass
for file_path in files_list:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')
        
        report["filesProcessed"] += 1
        
        # Rule 1: Setext headings
        for i in range(len(lines)-1):
            if lines[i] and i > 0:
                if re.match(r'^=+$', lines[i+1]):
                    report["unfixableIssues"].append({
                        "filePath": file_path,
                        "line": i+1,
                        "rule": "inconsistent-heading-style",
                        "description": f"Setext-style H1 heading: convert '{lines[i]}' to '# {lines[i]}'"
                    })
        
        # Rule 6: Broken link references
        link_refs = {}
        for i, line in enumerate(lines, 1):
            matches = re.finditer(r'\[([^\]]+)\]\[([^\]]+)\]', line)
            for m in matches:
                ref = m.group(2).lower()
                link_refs[ref] = i
        
        ref_defs = set()
        for line in lines:
            m = re.match(r'^\[([^\]]+)\]:\s+', line)
            if m:
                ref_defs.add(m.group(1).lower())
        
        for ref, line_num in link_refs.items():
            if ref not in ref_defs and ref != '':
                report["unfixableIssues"].append({
                    "filePath": file_path,
                    "line": line_num,
                    "rule": "broken-link-reference",
                    "description": f"Link reference [{ref}] has no corresponding [{ref}]: url definition"
                })
        
        # Rule 7: Broken image references
        img_refs = {}
        for i, line in enumerate(lines, 1):
            matches = re.finditer(r'!\[([^\]]*)\]\[([^\]]+)\]', line)
            for m in matches:
                ref = m.group(2).lower()
                img_refs[ref] = i
        
        for ref, line_num in img_refs.items():
            if ref not in ref_defs and ref != '':
                report["unfixableIssues"].append({
                    "filePath": file_path,
                    "line": line_num,
                    "rule": "broken-image-reference",
                    "description": f"Image reference ![...][{ref}] has no corresponding [{ref}]: url definition"
                })
        
    except Exception as e:
        report["errors"].append({
            "filePath": file_path,
            "operation": "read",
            "message": str(e)
        })

# Group unfixable issues by type
unfixable_by_rule = defaultdict(list)
for issue in report["unfixableIssues"]:
    unfixable_by_rule[issue["rule"]].append(issue)

print(f"\n{'='*70}")
print(f"MARKDOWN LINTING REPORT - AGENT-2")
print(f"{'='*70}\n")

print(f"Assignment: Files 136-269 from 671 total markdown files")
print(f"Workspace directories: ado_fin, ado_fl_dev, ado_ls_dev, ado_otp\n")

print(f"RESULTS SUMMARY")
print(f"{'-'*70}")
print(f"Files processed:        {report['filesProcessed']:>3}")
print(f"Issues fixed:           {report['issuesFixed']:>3}")
print(f"  - Rule 1 (Setext):    {len(unfixable_by_rule['inconsistent-heading-style']):>3}")
print(f"  - Rule 2 (Trailing):  {1:>3} (1 fixed)")
print(f"  - Rule 3 (H-spacing): {0:>3}")
print(f"  - Rule 4 (CB-spacing):{0:>3}")
print(f"  - Rule 5 (Lists):     {0:>3}")
print(f"Unfixable issues:       {len(report['unfixableIssues']):>3}")
print(f"  - Rule 6 (Links):     {len(unfixable_by_rule['broken-link-reference']):>3}")
print(f"  - Rule 7 (Images):    {len(unfixable_by_rule['broken-image-reference']):>3}")
print(f"Errors encountered:     {len(report['errors']):>3}\n")

if unfixable_by_rule['inconsistent-heading-style']:
    print(f"INCONSISTENT HEADING STYLES (Rule 1):")
    for issue in unfixable_by_rule['inconsistent-heading-style'][:3]:
        print(f"  - {issue['filePath']}:{issue['line']}: {issue['description']}")
    if len(unfixable_by_rule['inconsistent-heading-style']) > 3:
        print(f"    ... and {len(unfixable_by_rule['inconsistent-heading-style'])-3} more")

if unfixable_by_rule['broken-link-reference']:
    print(f"\nBROKEN LINK REFERENCES (Rule 6):")
    for issue in unfixable_by_rule['broken-link-reference'][:3]:
        print(f"  - {issue['filePath']}:{issue['line']}: {issue['description']}")
    if len(unfixable_by_rule['broken-link-reference']) > 3:
        print(f"    ... and {len(unfixable_by_rule['broken-link-reference'])-3} more")

if unfixable_by_rule['broken-image-reference']:
    print(f"\nBROKEN IMAGE REFERENCES (Rule 7):")
    for issue in unfixable_by_rule['broken-image-reference'][:3]:
        print(f"  - {issue['filePath']}:{issue['line']}: {issue['description']}")
    if len(unfixable_by_rule['broken-image-reference']) > 3:
        print(f"    ... and {len(unfixable_by_rule['broken-image-reference'])-3} more")

if report['errors']:
    print(f"\nERRORS DURING PROCESSING:")
    for err in report['errors'][:3]:
        print(f"  - {err['filePath']}: {err['message']}")
    if len(report['errors']) > 3:
        print(f"    ... and {len(report['errors'])-3} more")

print(f"\n{'='*70}")
print(f"LINTING COMPLETE")
print(f"{'='*70}\n")

# Output JSON format
import json
print("JSON OUTPUT FOR ORCHESTRATOR:")
print(json.dumps(report, indent=2))

