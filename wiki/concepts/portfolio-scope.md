---
title: "Portfolio Scope — Workspace Inclusion / Exclusion"
type: concept
tags: [portfolio, governance, exclusion, scope, skills]
sources:
  - "../../CLAUDE.md"
  - "../../.claude/skills/portfolio-health/SKILL.md"
  - "../../.claude/skills/portfolio-meeting-prep/SKILL.md"
created: 2026-05-25
updated: 2026-05-25
---

# Portfolio Scope — Workspace Inclusion / Exclusion

Defines which workspaces appear in portfolio-level reporting and how the exclusion list is maintained.

## Default scope

`portfolio-health` and `portfolio-meeting-prep` include every top-level workspace directory matching `ado_*` or `git_*` that contains a `CLAUDE.md`.

## Exclusion mechanism

A workspace can be removed from portfolio analysis without deleting or renaming its folder. The authoritative list lives in the root [`CLAUDE.md`](../../CLAUDE.md) under the heading **`Excluded Workspaces (Portfolio Analysis)`**:

| Folder | Team | Reason |
| -------- | ------ | ------ |
| `ado_ls_dev` | Life Style Help App | Removed from portfolio analysis per owner request (2026-05-21) |

Both skills read this table and skip listed workspaces early in their workflow (step 2 in `portfolio-health`; step 4 preamble in `portfolio-meeting-prep`).

**To add an exclusion:** append a row to the table in root `CLAUDE.md`. No skill code changes required.

**To reinstate:** remove the row from the table.

## What exclusion does (and does not) affect

| Capability | Excluded? |
|---|---|
| `portfolio-health` dashboard — scoring, charts, tier analysis | ✅ Skipped |
| `portfolio-meeting-prep` agenda — scorecard, discussion points | ✅ Skipped |
| `ado-safe-audit ado_ls_dev` (individual) | ❌ Still runs |
| `ado-safe-audit all-projects` batch | ❌ Still included |
| Workspace audit history (`ado_ls_dev/audit/`) | ❌ Untouched |

## Current excluded workspaces

| Workspace | Excluded since | Reason |
|---|---|---|
| `ado_ls_dev` | 2026-05-21 | Owner request |

## Related pages

- [[entities/team-ado-ls-dev]] — first team excluded
- [[concepts/scoring-ado-rubric]] — ADO scoring used in portfolio
- [[concepts/scoring-git-ups]] — Git UPS scoring used in portfolio
- [[synthesis/portfolio-trend]] — historical portfolio scores (LS Dev included through 2026-04-29)
