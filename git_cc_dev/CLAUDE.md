# Colina Health Iteration Audit Context

## Shared Skill Authority

- The shared Git audit skill at `.claude/skills/git_iteration_audit/SKILL.md` governs workflow, scoring, evidence rules, report structure, output policy, and batch behavior for this workspace.
- This `CLAUDE.md` file is the local source of truth for project scope, repository scope, audit history, people, glossary, and explicit project exceptions.
- If this file conflicts with the shared skill on workflow, scoring, evidence, or output policy, the shared skill wins unless the difference is explicitly documented under `Project Exceptions`.

## Project Context

### Objective

Audit the **Colina Health Product Team** for the **current active Azure DevOps iteration** using the shared Git standard:
- GitHub developer productivity
- SAFe compliance
- ADO-to-GitHub traceability

This is an iteration-bounded audit. It is not a general repository audit, an organization-wide productivity review, or a multi-project assessment.

### In Scope

- **ADO Org:** `jairo`
- **ADO Project:** `Jairosoft Portfolio`
- **ADO Project ID:** `666bb99a-6acd-4999-bb34-efd0e4ea90dc`
- **ADO Team:** `Colina Health Product Team`
- **ADO Team ID:** `66cdeb09-df38-4c3e-9418-0ed0d68c39f2`
- **ADO Team Board URL (human reference only):** `https://dev.azure.com/jairo/Jairosoft%20Portfolio/_boards/board/t/Colina%20Health%20Product%20Team/Stories%20and%20Deliverables`
- **ADO Backlog ID:** `Microsoft.RequirementCategory`
- **ADO Backlog Focus:** `Stories and Deliverables`
- **GitHub Repo 1:** `https://github.com/jairosoft-com/colinahealth-fe.git`
- **GitHub Repo 2:** `https://github.com/jairosoft-com/colinahealth-be.git`
- **GitHub Repo 3:** `https://github.com/jairosoft-com/colina-health-ai-agent-code-fixing.git`
- **Time Window:** the current active iteration returned by `Colina Health Product Team` team settings in Azure DevOps

### Out of Scope

- Any other Azure DevOps board
- Any other Azure DevOps team
- Any other Azure DevOps project
- Any GitHub repository outside:
  - `https://github.com/jairosoft-com/colinahealth-fe.git`
  - `https://github.com/jairosoft-com/colinahealth-be.git`
  - `https://github.com/jairosoft-com/colina-health-ai-agent-code-fixing.git`

## Project Exceptions

- Historical `SCORECARD_*.md` files remain in `audit/` as legacy artifacts. New audits for this workspace use one integrated `AUDIT_<date>_<time>.md` report only.

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
| **EMR** | Electronic Medical Record |

> Full glossary: `memory/glossary.md`

## Projects

| Name | What |
|------|------|
| **Colina Health** | Colina Health Project |

> Details: `memory/projects/`

## ADO Context

- **Org:** `jairo` (`dev.azure.com/jairo`)
- **Project:** `Jairosoft Portfolio`
- **Project ID:** `666bb99a-6acd-4999-bb34-efd0e4ea90dc`
- **Project URL:** `https://dev.azure.com/jairo/Jairosoft%20Portfolio`
- **Team:** `Colina Health Product Team`
- **Team ID:** `66cdeb09-df38-4c3e-9418-0ed0d68c39f2`
- **Team Board URL (human reference only):** `https://dev.azure.com/jairo/Jairosoft%20Portfolio/_boards/board/t/Colina%20Health%20Product%20Team/Stories%20and%20Deliverables`
- **Backlog ID:** `Microsoft.RequirementCategory`
- **Backlog Focus:** `Stories and Deliverables`

## GitHub Repositories

| Repo | URL |
|------|-----|
| **Frontend** | `https://github.com/jairosoft-com/colinahealth-fe.git` |
| **Backend** | `https://github.com/jairosoft-com/colinahealth-be.git` |
| **AI Agent Code Fixing** | `https://github.com/jairosoft-com/colina-health-ai-agent-code-fixing.git` |

## Audit History

| Date | File | Status |
|------|------|--------|
| 2026-03-11 | `audit/AUDIT_20260311_2329.md` | Complete |
| 2026-03-12 | `audit/AUDIT_20260312_1536.md` | Complete |
| 2026-03-17 | `audit/AUDIT_20260317_1700.md` | Complete |
| 2026-03-18 | `audit/AUDIT_20260318_1030.md` | Complete |
| 2026-03-22 | `audit/AUDIT_20260322_1030.md` | Complete |
| 2026-03-25 | `audit/AUDIT_20260325_1800.md` | Complete |
| 2026-04-04 | `audit/AUDIT_20260404_0930.md` | Complete |
| 2026-04-05 | `audit/AUDIT_20260405_0900.md` | Complete |
| 2026-04-06 | `audit/AUDIT_20260406_0900.md` | Complete |
| 2026-04-07 | `audit/AUDIT_20260407_1708.md` | Complete |
| 2026-04-08 | `audit/AUDIT_20260408_0900.md` | Complete |
| 2026-04-09 | `audit/AUDIT_20260409_0900.md` | Complete |
| 2026-04-12 | `audit/AUDIT_20260412_0900.md` | Complete |
| 2026-04-13 | `audit/AUDIT_20260413_0900.md` | Complete |
| 2026-04-16 | `audit/AUDIT_20260416_0900.md` | Complete |
| 2026-04-17 | `audit/AUDIT_20260417_0900.md` | Complete |

## Preferences

- Audit reports authored as Markdown in `audit/` folder
- PDF export is done manually by Ramon via Obsidian (Export to PDF)
- Do NOT automate PDF creation — Obsidian handles the Markdown → PDF conversion
- Mermaid diagrams for visualization (Obsidian renders these natively)
- Do not use `xychart-beta` in Mermaid diagrams because it does not render reliably in Obsidian
- The `temp/` folder is a repository for drafts, snippets, and temporary working artifacts generated by Claude or Codex
- Final audit reports do not belong in the `temp/` folder
