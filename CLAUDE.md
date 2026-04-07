# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **SAFe iteration audit portfolio** for Jairosoft LLC. It contains workspace folders for 9 teams across Azure DevOps and GitHub, plus shared audit skills and portfolio-level reporting. The primary user is Ramon Aseniero (CEO), who runs audits via Claude Code CLI skills.

## Repository Structure

```
iteration_audit/
├── ado_*/           # Azure DevOps workspace audits (7 teams)
├── git_*/           # GitHub workspace audits (2 teams)
├── portfolio_report/          # Generated portfolio health dashboards (HTML)
├── portfolio_meeting_agenda/  # Meeting agenda/prep documents (HTML)
├── .claude/skills/            # Shared skill definitions (audit workflow authority)
├── logs/                      # Session logs (gitignored)
└── temp/                      # Draft artifacts (gitignored)
```

### Workspaces

| Folder | Team | Type | ADO Project / GitHub Repos |
|--------|------|------|---------------------------|
| `ado_admin` | Administration | ADO | Jairosoft FINOPS |
| `ado_fin` | Finance | ADO | Jairosoft FINOPS |
| `ado_fl_dev` | Flawless Wedding App | ADO | Jairosoft FINOPS |
| `ado_hr` | HR Recruitment | ADO | Jairosoft FINOPS |
| `ado_jit` | JIT Operation | ADO | Jairosoft FINOPS |
| `ado_ls_dev` | Life Style Help App | ADO | Jairosoft FINOPS |
| `ado_otp` | Office of the President | ADO | Jairosoft FINOPS |
| `git_aa_dev` | Auto Allies | Git | GitHub repos |
| `git_cc_dev` | Colina Health | Git | GitHub repos |

Each workspace contains:
- `CLAUDE.md` — local context, team members, audit history, project exceptions
- `audit/` — timestamped audit reports (`AUDIT_YYYYMMDD_HHMM.md`)
- `todo/` — compliance fix lists (when applicable)

### Shared Skills (`.claude/skills/`)

Skills are the authority for workflow, scoring, and output policy. Workspace `CLAUDE.md` files provide local context but defer to skills on process.

| Skill | Purpose | Invocation |
|-------|---------|------------|
| `ado-safe-audit` | ADO SAFe iteration audit | `/ado-safe-audit [folder]` or `all-projects` |
| `git_iteration_audit` | GitHub iteration audit | `/git_iteration_audit [folder]` or `all-git-projects` |
| `portfolio-health` | Aggregate dashboard (HTML) | `/portfolio-health` |
| `portfolio-email` | Email dashboard to recipients | `/portfolio-email [name or email]` |
| `portfolio-meeting-prep` | Meeting agenda (HTML) | `/portfolio-meeting-prep [duration]` |

## Key Conventions

### Skill Authority Hierarchy

1. **Shared skills** govern: workflow steps, scoring formulas, evidence rules, output policy, batch behavior
2. **Workspace CLAUDE.md** governs: team context, audit history, people, project exceptions
3. If conflict: shared skill wins unless workspace has an explicit `Project Exceptions` section

### Scoring

- **ADO teams:** 7-dimension rubric (Iteration Planning, Team Capacity, Estimation, DoR Compliance, Work Item Balance, Backlog Refinement, Delivery Predictability). Overall = average of seven.
- **Git teams:** ICS (Iteration Compliance), HCI (Health Check Index), SGPI (Sprint Goal Progress Index). UPS = ICS x 0.50 + HCI x 0.30 + SGPI x 0.20.
- **Risk bands:** Low >= 80 (green), Moderate 60-79.9 (yellow), High 40-59.9 (orange), Critical < 40 (red).

### Output Policies

- **Audit reports:** Markdown only, saved to `[workspace]/audit/AUDIT_YYYYMMDD_HHMM.md`
- **Portfolio dashboards:** Self-contained HTML to `portfolio_report/PORTFOLIO_YYYYMMDD_HHMM.html`
- **Meeting agendas:** Self-contained HTML to `portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_YYYYMMDD.html`
- **Todo lists:** Markdown to `[workspace]/todo/`
- **PDFs:** Never auto-generated. Manual export via Obsidian only.
- **Mermaid diagrams:** Use standard chart types only. No `xychart-beta` (Obsidian can't render it).

### Batch Audits

- ADO batch (`all-projects`): 3 parallel agent teams (3+2+2 workspace split), Team Lead ranks non-critical to critical
- Git batch (`all-git-projects`): 2 parallel agents
- Audits never mix ADO and Git in the same batch

## MCP Servers

This repo relies on these MCP integrations:
- **azure-devops** — iterations, work items, backlogs, capacity, team data
- **github** — PRs, commits, branches, code search
- **mail** — send via Graph API (`ramon@jairosoft.com`), read via IMAP
- **claude-in-chrome** — browser automation for Outlook, dashboard viewing

## Output Style

The user prefers YAML-structured responses (configured in `settings.local.json`). Structure responses with `task`, `status`, `details`, `files`, `notes` keys.
