# Auto Allies Iteration Audit Context

## Shared Skill Authority

- The shared Git audit skill at `.claude/skills/git_iteration_audit/SKILL.md` governs workflow, scoring, evidence rules, report structure, output policy, and batch behavior for this workspace.
- This `CLAUDE.md` file is the local source of truth for project scope, repository scope, audit history, people, glossary, and explicit project exceptions.
- If this file conflicts with the shared skill on workflow, scoring, evidence, or output policy, the shared skill wins unless the difference is explicitly documented under `Project Exceptions`.

## Project Context

### Objective

Audit the **Auto Allies Development Team** for the **current active Azure DevOps iteration** using the shared Git standard:

- GitHub developer productivity
- SAFe compliance
- ADO-to-GitHub traceability

This is an iteration-bounded audit. It is not a general repository audit, an organization-wide productivity review, or a multi-project assessment.

### In Scope

- **ADO Org:** `jairo`
- **ADO Project:** `Auto Allies`
- **ADO Project ID:** `2d7af571-6ef6-4ad0-a509-c440e008b0fb`
- **ADO Team:** `AA Development Team`
- **ADO Team ID:** `330e6bf1-3515-443c-a2d8-b84f46c38f57`
- **ADO Team Board URL (human reference only):** `https://dev.azure.com/jairo/Auto%20Allies/_boards/board/t/AA%20Development%20Team/Stories%20and%20Deliverables`
- **ADO Backlog ID:** `Microsoft.RequirementCategory`
- **ADO Backlog Focus:** `Stories and Deliverables`
- **GitHub Repo 1:** `jairosoft-com/autoallies-version2`
- **GitHub Repo 2:** `jairosoft-com/autoallies-api-core`
- **Time Window:** the current active iteration returned by `AA Development Team` team settings in Azure DevOps

### Out of Scope

- Any other Azure DevOps board
- Any other Azure DevOps team
- Any other Azure DevOps project
- Any GitHub repository outside:
  - `jairosoft-com/autoallies-version2`
  - `jairosoft-com/autoallies-api-core`

## Project Exceptions

- **Jerlyn Ates and Mary Secusana are not developers.** Jerlyn is QA/Requirements; Mary is Documentation. Their absence of GitHub commits, PRs, and reviews is expected and **must not be scored as a team compliance gap or HCI penalty**. Source: LPM Review meeting with Ramon Aseniero on 2026-04-23 — "we can just put that in the knowledge base that they're not developers, so they don't need GitHub." See [[wiki/summaries/transcript-lpm-review-2026-04-23]].
- **GitHub API 404 on `raseniero` token (2026-04-21 onward)** is a known access-scope issue pending Ramon's fix. Audit runs during this window should carry `data_mode: partial` in frontmatter and treat HCI dimensions 1–6 as Day-2 (2026-04-21) carry-forward rather than fresh-evidence scoring. Do not penalize the team for stale GitHub evidence while the token issue is unresolved.

---

# Memory

## Me

**Ramon** (Ramon Aseniero Jr), `ramon@jairosoft.com`. Manages ADO projects at Jairo organization. Uses SAFe framework for project auditing.

## People

| Who | Role |
|-----|------|
| **Ramon** | Ramon Aseniero Jr, Project Owner, `ramon@jairosoft.com` |
| **Karl** | Karl Caumban, Project Manager, `kcaumban@jairosoft.com` |

> Full list: `memory/glossary.md`, profiles: `memory/people/`

## Terms

| Term | Meaning |
|------|---------|
| **AA** | AutoAllies |

> Full glossary: `memory/glossary.md`

## Projects

| Name | What |
|------|------|
| **AutoAllies** | AutoAllies.com |

> Details: `memory/projects/`

## ADO Context

- **Org:** `jairo` (`dev.azure.com/jairo`)
- **Project:** `Auto Allies`
- **Project ID:** `2d7af571-6ef6-4ad0-a509-c440e008b0fb`
- **Project URL:** `https://dev.azure.com/jairo/Auto%20Allies`
- **Team:** `AA Development Team`
- **Team ID:** `330e6bf1-3515-443c-a2d8-b84f46c38f57`
- **Team Board URL (human reference only):** `https://dev.azure.com/jairo/Auto%20Allies/_boards/board/t/AA%20Development%20Team/Stories%20and%20Deliverables`
- **Backlog ID:** `Microsoft.RequirementCategory`
- **Backlog Focus:** `Stories and Deliverables`

## GitHub Repositories

| Repo | URL |
|------|-----|
| **Frontend** | `https://github.com/jairosoft-com/autoallies-version2` |
| **Backend** | `https://github.com/jairosoft-com/autoallies-api-core` |

## Audit History

| Date | File | Status |
|------|------|--------|
| 2026-03-09 | `audit/AUDIT_2026-03-09_000000.md` | Complete |
| 2026-03-10 | `audit/AUDIT_2026-03-10_000000.md` | Complete |
| 2026-03-10 | `audit/AUDIT_2026-03-10_202500.md` | Complete |
| 2026-03-11 | `audit/AUDIT_2026-03-11_234100.md` | Complete |
| 2026-03-16 | `audit/AUDIT_2026-03-16_000000.md` | Complete |
| 2026-03-17 | `audit/AUDIT_2026-03-17_170000.md` | Complete |
| 2026-03-18 | `audit/AUDIT_2026-03-18_000000.md` | Complete |
| 2026-03-22 | `audit/AUDIT_2026-03-22_2329.md` | Complete |
| 2026-03-25 | `audit/AUDIT_20260325_1800.md` | Complete |
| 2026-03-26 | `audit/AUDIT_20260326_1630.md` | Complete |
| 2026-03-30 | `audit/AUDIT_20260330_0900.md` | Complete |
| 2026-03-31 | `audit/AUDIT_20260331_0900.md` | Complete |
| 2026-04-01 | `audit/AUDIT_20260401_0900.md` | Complete |
| 2026-04-02 | `audit/AUDIT_20260402_0900.md` | Complete |
| 2026-04-04 | `audit/AUDIT_20260404_0845.md` | Complete |
| 2026-04-05 | `audit/AUDIT_20260405_0900.md` | Complete |
| 2026-04-06 | `audit/AUDIT_20260406_0900.md` | Complete |
| 2026-04-07 | `audit/AUDIT_20260407_1719.md` | Complete |
| 2026-04-08 | `audit/AUDIT_20260408_0900.md` | Complete |
| 2026-04-09 | `audit/AUDIT_20260409_0900.md` | Complete |
| 2026-04-12 | `audit/AUDIT_20260412_0900.md` | Complete |
| 2026-04-13 | `audit/AUDIT_20260413_0900.md` | Complete |
| 2026-04-16 | `audit/AUDIT_20260416_0900.md` | Complete |
| 2026-04-17 | `audit/AUDIT_20260417_0900.md` | Complete |
| 2026-04-29 | `audit/AUDIT_20260429_0242.md` | Complete |

## Preferences

- Audit reports authored as Markdown in `audit/` folder
- PDF export is done manually by Ramon via Obsidian (Export to PDF)
- Exported PDFs are saved to the `report/` folder for sharing with colleagues
- The `report/` folder is only for manually exported PDFs, not source Markdown audit reports
- Do NOT automate PDF creation — Obsidian handles the Markdown → PDF conversion
- Mermaid diagrams for visualization (Obsidian renders these natively)
- Do not use `xychart-beta` in Mermaid diagrams because it does not render reliably in Obsidian
- The `temp/` folder is a repository for drafts, snippets, and temporary working artifacts generated by Claude or Codex
- Final audit reports do not belong in the `temp/` folder
