# Plan: Wiki Lint Fixes — P1 + P2 (2026-04-28)

## Context

Wiki lint (Day-9 session) surfaced 3 issue classes. P1 = broken structure/links that affect parser and navigation. P2 = missing prefix that makes links non-navigable in Obsidian. All fixes are mechanical edits to existing wiki files — no new pages created.

---

## P1a — YAML Frontmatter Bug (11 synthesis pages)

**Problem:** `updated:` date written as `## updated: YYYY-MM-DD` in the markdown body instead of `updated: YYYY-MM-DD` inside the YAML frontmatter block. Parsers (Obsidian, wiki tooling) cannot read the date.

**Fix:** For each file, move the date line from body into frontmatter. Pattern:

```
# Before (in body):
---
title: "..."
created: 2026-04-XX
---
## updated: 2026-04-20
```

```
# After (in frontmatter):
---
title: "..."
created: 2026-04-XX
updated: 2026-04-20
---
```

**Files (11):**
- `wiki/synthesis/scoring-artifacts.md`
- `wiki/synthesis/dor-leakage.md`
- `wiki/synthesis/ci-health.md`
- `wiki/synthesis/pi7-plan.md`
- `wiki/synthesis/service-model-scoring.md`
- `wiki/synthesis/audit-automation.md`
- `wiki/synthesis/github-compliance-issues.md`
- `wiki/synthesis/iteration-7.1-close.md`
- `wiki/synthesis/pi6-close.md`
- `wiki/synthesis/bus-factor.md`
- `wiki/synthesis/compliance-misalignment.md`

**Execution:** Run in parallel — 2 agents, ~5-6 files each, 1 file gets overlap handled by either.

---

## P1b — Broken Cross-Links (3 summary files)

**Problem:** Apr 24 audit summaries reference Apr 23 summaries by wrong timestamp slug. Links are dead — Obsidian shows them as unresolved.

**Fix:** Replace wrong slug with correct slug in each file.

| File (contains broken link) | Wrong slug | Correct slug |
|---|---|---|
| `wiki/summaries/audit-ado-admin-20260424-*.md` | `audit-ado-admin-20260423-0900` | `audit-ado-admin-20260423-0113` |
| `wiki/summaries/audit-git-aa-dev-20260424-*.md` | `audit-git-aa-dev-20260423-1515` | `audit-git-aa-dev-20260423-0855` |
| `wiki/summaries/audit-git-cc-dev-20260424-*.md` | `audit-git-cc-dev-20260423-1515` | `audit-git-cc-dev-20260423-0856` |

**Note:** Exact Apr 24 filenames unknown — use `find wiki/summaries -name "audit-ado-admin-20260424*"` to resolve before editing.

---

## P2 — Bare-Slug Links (26 links across ~25 files)

**Problem:** `[[audit-ado-ls-dev-YYYYMMDD-HHMM]]` instead of `[[summaries/audit-ado-ls-dev-YYYYMMDD-HHMM]]`. Obsidian requires full path from wiki root for cross-folder links to resolve.

**Scope:**
- 25 links in early LS Dev summary chain (files in `wiki/summaries/audit-ado-ls-dev-*.md`)
- 1 link in `wiki/summaries/meeting-agenda-20260427.md`

**Fix:** Add `summaries/` prefix to bare audit slugs inside `[[...]]` links.

**Find command to locate all instances:**
```bash
grep -rn '\[\[audit-ado-ls-dev-[0-9]' wiki/summaries/ | grep -v 'summaries/audit'
grep -rn '\[\[audit-' wiki/summaries/meeting-agenda-20260427.md | grep -v 'summaries/'
```

---

## Execution Sequence

### Phase 1 — Parallel (P1a + P1b + P2 simultaneously)

**Agent A** — Fix P1a YAML bug, files 1-6:
scoring-artifacts, dor-leakage, ci-health, pi7-plan, service-model-scoring, audit-automation

**Agent B** — Fix P1a YAML bug, files 7-11:
github-compliance-issues, iteration-7.1-close, pi6-close, bus-factor, compliance-misalignment

**Agent C** — Fix P1b broken links (3 files) + P2 bare-slug links (26 links):
- Resolve Apr 24 filenames with find
- Fix the 3 broken slug references
- Fix all bare-slug `[[audit-ado-ls-dev-*]]` links
- Fix bare-slug link in meeting-agenda-20260427

### Phase 2 — Append to wiki/log.md

Single agent appends lint-fix entry to `wiki/log.md`.

---

## Files Modified

| File | Fix | Phase |
|---|---|---|
| `wiki/synthesis/scoring-artifacts.md` | P1a YAML | 1 |
| `wiki/synthesis/dor-leakage.md` | P1a YAML | 1 |
| `wiki/synthesis/ci-health.md` | P1a YAML | 1 |
| `wiki/synthesis/pi7-plan.md` | P1a YAML | 1 |
| `wiki/synthesis/service-model-scoring.md` | P1a YAML | 1 |
| `wiki/synthesis/audit-automation.md` | P1a YAML | 1 |
| `wiki/synthesis/github-compliance-issues.md` | P1a YAML | 1 |
| `wiki/synthesis/iteration-7.1-close.md` | P1a YAML | 1 |
| `wiki/synthesis/pi6-close.md` | P1a YAML | 1 |
| `wiki/synthesis/bus-factor.md` | P1a YAML | 1 |
| `wiki/synthesis/compliance-misalignment.md` | P1a YAML | 1 |
| `wiki/summaries/audit-ado-admin-20260424-*.md` | P1b broken link | 1 |
| `wiki/summaries/audit-git-aa-dev-20260424-*.md` | P1b broken link | 1 |
| `wiki/summaries/audit-git-cc-dev-20260424-*.md` | P1b broken link | 1 |
| `wiki/summaries/audit-ado-ls-dev-*.md` (~25 files) | P2 bare slugs | 1 |
| `wiki/summaries/meeting-agenda-20260427.md` | P2 bare slug | 1 |
| `wiki/log.md` | lint-fix entry | 2 |

Total: 16+ files edited, 0 files created.

---

## Verification

1. After Phase 1: `grep -r '## updated:' wiki/synthesis/` → 0 results
2. After Phase 1: `grep 'audit-ado-admin-20260423-0900\|audit-git-aa-dev-20260423-1515\|audit-git-cc-dev-20260423-1515' wiki/summaries/` → 0 results
3. After Phase 1: `grep -r '\[\[audit-ado-ls-dev-[0-9]' wiki/summaries/ | grep -v 'summaries/'` → 0 results
4. After Phase 2: `tail -10 wiki/log.md` shows lint-fix entry
