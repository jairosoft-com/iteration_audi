---
title: "Ramon Aseniero Jr — CEO & Audit Owner"
type: entity
tags: [person, ramon, ceo, stakeholder, owner]
sources:
  - "../../CLAUDE.md"
  - "../../ado_shared/CLAUDE.md"
  - "../../ado_admin/CLAUDE.md"
  - "../../ado_jit/CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Ramon Aseniero Jr

**CEO of Jairosoft LLC.** Project owner for every audit workspace in this portfolio, primary requester and consumer of the SAFe iteration audits, and the operator who runs audits via Claude Code CLI.

- **Email:** <ramon@jairosoft.com>
- **Role:** Project owner / audit requester / Agile PM consultant in audit framing
- **Scope:** All 10 team workspaces (every `ado_*` and `git_*` folder lists him as project owner)

## Why he has an entity page

Most-referenced stakeholder in the wiki (30+ mentions). Every workspace `CLAUDE.md` names him as the audit requester; he also sets the auditing conventions documented in [../../CLAUDE.md](../../CLAUDE.md) (root schema) and in [[CLAUDE]] (this wiki's schema). His preferences define **how audits are produced** and what gets filed where.

## Conventions he owns

These live in the root [../../CLAUDE.md](../../CLAUDE.md) and shape every page in this wiki:

- **Scoring rubric selection** — ADO 7-dim, Git UPS; see [[concepts/scoring-ado-rubric]], [[concepts/scoring-git-ups]], [[concepts/risk-bands]]
- **Output locations** — audits to `[workspace]/audit/`, portfolio HTML to `portfolio_report/`, todos to `[workspace]/todo/`
- **Format constraints** — markdown-only audits; HTML-only portfolio dashboards; manual PDF export via Obsidian
- **Mermaid rules** — no `xychart-beta` (Obsidian can't render it)
- **Batch conventions** — ADO batches use 3 parallel agent teams; Git batches use 2; never mix
- **Email delivery** — Graph API send, never IMAP drafts (see feedback memories)

## Decision authority

Decisions the wiki attributes to him:

- Portfolio audit cadence (roughly daily 09:00 snapshots + ad-hoc close-day audits)
- Workspace structure (adding Shared Services as 10th team on 2026-04-19)
- Forward-look asks (PI7.2 planning themes from [[synthesis/iteration-7.1-close]])
- Rubric-change approvals (implicit — rubric transitions on 2026-04-05 and earlier; see [[synthesis/scoring-artifacts]])

## Stakeholder relationships

| Person | Relationship to Ramon | Reference |
|--------|----------------------|-----------|
| [[entities/person-grace]] | Finance/Admin direct report + portfolio email recipient | root [[CLAUDE]] |
| [[entities/person-carol]] | PM for multiple teams; reports into the same portfolio | root [[CLAUDE]] |
| [[entities/person-mark-colina]] | Sole Administration team member | [[entities/team-ado-admin]] |
| Karl Caumban (PDM) | Co-reviewer of portfolio audits; joint meeting prep | root [[CLAUDE]] |
| Bomar Sinday (Engineering Mgr) | Portfolio email recipient | root [[CLAUDE]] |

## Typical working session (what "runs an audit" means)

Based on the wiki's log and summary patterns:

1. Invokes a Claude Code skill (e.g., `/ado-safe-audit [workspace]` or `/all-projects`) — see root [../../.claude/skills/](../../.claude/skills/)
2. Reviews the generated audit markdown in Obsidian
3. Invokes `/portfolio-health` for the cross-team dashboard
4. Reviews, emails via `/portfolio-email`, or prepares agenda via `/portfolio-meeting-prep` for review with Karl
5. Files compliance fixes to `[workspace]/todo/`

## Related

- [../../CLAUDE.md](../../CLAUDE.md) — root conventions file he authored
- [[CLAUDE]] — wiki schema (co-authored with this agent)
- [[synthesis/iteration-7.1-close]] — latest retrospective feeding his 7.2 planning decisions
- [[entities/person-grace]] · [[entities/person-carol]] · [[entities/person-mark-colina]] — direct working relationships

## Open questions

- Does he want individual person pages for Karl and Bomar (both have portfolio-email stake but haven't been profiled)?
- What is the planned cadence for LLM Wiki upkeep alongside the audit cadence? (Schema change approvals, synthesis drafting, lint passes.)
