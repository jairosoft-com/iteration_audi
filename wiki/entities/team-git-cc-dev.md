---
title: "Team — Colina Health (Git)"
type: entity
tags: [team, git, colina-health, safe, healthcare]
sources:
  - "../../git_cc_dev/audit/AUDIT_20260419_1345.md"
  - "../../git_cc_dev/CLAUDE.md"
created: 2026-04-19
updated: 2026-04-19
---

# Colina Health Product Team (Git)

Healthcare (EMR) product team delivering the Colina Health application via three GitHub repos under the `jairosoft-com` org: `colinahealth-fe` (frontend), `colinahealth-be` (backend), and `colina-health-ai-agent-code-fixing`. ADO planning lives in `Jairosoft Portfolio` under the `Colina Health Product Team` board (`Stories and Deliverables`). Sprint work is primarily defect-fix and architecture enablers, with HIPAA / PHI audit trail being the current high-stakes thread.

## Current state (Iteration 7.1 — 2026-04-06 → 2026-04-19)

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | **90.6** | 🟢 Low |
| ICS (×0.50) | 96.8% | 🟢 Low |
| HCI (×0.30) | 74/100 | 🟡 Moderate |
| SGPI (×0.20) | 100.0% | 🟢 Low (Sprint Complete) |

Sprint closes Green on Day 14. All 11 committed defect items (21 SP) Closed. UPS improved +0.3 from Day 12 on a +1 HCI tick driven by FE PR#144 actually merging to `develop`.

## Real fixable issues

1. **BE PR#55 (HIPAA structured logging + PHI audit trail, 42 files, item 202696) unreviewed for 2 days** — `raseniero` is requested reviewer, no approval yet. Highest-risk outstanding artifact; PHI redaction correctness must be verified before merge in Iteration 7.2.
2. **FE PR#145 (Husky + lint-staged, 202594) and FE PR#146 (generateMetadata, 202595) open 4–5 days** pending `raseniero` review — blocks pre-commit gate activation and iteration 7.2 kickoff.
3. **No branch protection on `main` or `develop` in FE or BE** — all observed branches return `"protected": false`; self-merge pattern exploited during defect sprint. Persistent carry-forward gap.
4. **11 new defects (202269, 202273, 202274, 202436, 202439, 202442, 202444, 202448, 202477, 202480, 202483) sit at project root / PI-level** with `State = New`, assigned to Jaszmeine — need triage into Iteration 7.2 or PI backlog.
5. **Item 199597 `System.Description` field still null** (rev 40) — drags Quality/DoD to 90.9% and holds ICS below 100%.

## Structural / context notes

- First AI-assisted PR in team history: BE#55 generated with Claude Code assistance.
- Weekend pause (Sat Apr 18 / Sun Apr 19) is a real sprint behavior, not missing evidence — no PR activity after Apr 18 07:23 UTC.
- `merged_at` populated but `merged: false` on FE#144 — likely a squash/rebase-merge API quirk; treated as merged for audit.
- Contributor load is pcoronia-dominant (18 PRs) with Kyaa-A (12 PRs) inactive in the final week; Luzmibel closed Spike 202134 on Day 12.
- Enabler re-scoping to Iteration 7.2 (202592, 202594, 202595, 202810, 202696) held firm through sprint close — governance discipline maxed at 10/10 on HCI.

## Git references

- GitHub org: `jairosoft-com`
- Frontend: <https://github.com/jairosoft-com/colinahealth-fe>
- Backend: <https://github.com/jairosoft-com/colinahealth-be>
- AI Agent: <https://github.com/jairosoft-com/colina-health-ai-agent-code-fixing>
- ADO project: `Jairosoft Portfolio` (`666bb99a-6acd-4999-bb34-efd0e4ea90dc`), team `Colina Health Product Team` (`66cdeb09-df38-4c3e-9418-0ed0d68c39f2`)
- Workspace: [../../git_cc_dev/](../../git_cc_dev/)

## Stakeholders

| Who | Role | Email |
|-----|------|-------|
| Ramon Aseniero Jr | Project Owner / Reviewer (`raseniero`) | <ramon@jairosoft.com> |
| Karl Caumban | Project Manager / PDM | <kcaumban@jairosoft.com> |
| Paul Coronia | Lead Dev (`pcoronia`) | — |
| Asnari Pacalna | Dev (`Kyaa-A`) | — |
| Luzmibel Paculanang | QA | — |
| Jaszmeine | Backlog / Retro owner | — |

## Linked concepts

- [[concepts/scoring-git-ups]] — UPS = ICS × 0.50 + HCI × 0.30 + SGPI × 0.20
- [[concepts/risk-bands]] — Low ≥ 80 band

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-04-21 00:55** — [[summaries/audit-git-cc-dev-20260421-0055]] · [raw](../../git_cc_dev/audit/AUDIT_20260421_0055.md)
- **2026-04-19 13:45** — [[summaries/audit-git-cc-dev-20260419-1345]] · [raw](../../git_cc_dev/audit/AUDIT_20260419_1345.md)
- **2026-04-17 09:00** — [[summaries/audit-git-cc-dev-20260417-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260417_0900.md)
- **2026-04-16 09:00** — [[summaries/audit-git-cc-dev-20260416-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260416_0900.md)
- **2026-04-13 09:00** — [[summaries/audit-git-cc-dev-20260413-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260413_0900.md)
- **2026-04-12 09:00** — [[summaries/audit-git-cc-dev-20260412-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260412_0900.md)
- **2026-04-09 09:00** — [[summaries/audit-git-cc-dev-20260409-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260409_0900.md)
- **2026-04-08 09:00** — [[summaries/audit-git-cc-dev-20260408-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260408_0900.md)
- **2026-04-07 17:08** — [[summaries/audit-git-cc-dev-20260407-1708]] · [raw](../../git_cc_dev/audit/AUDIT_20260407_1708.md)
- **2026-04-06 09:00** — [[summaries/audit-git-cc-dev-20260406-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260406_0900.md)
- **2026-04-05 09:00** — [[summaries/audit-git-cc-dev-20260405-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260405_0900.md)
- **2026-04-04 09:30** — [[summaries/audit-git-cc-dev-20260404-0930]] · [raw](../../git_cc_dev/audit/AUDIT_20260404_0930.md)
- **2026-04-02 09:00** — [[summaries/audit-git-cc-dev-20260402-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260402_0900.md)
- **2026-04-01 09:00** — [[summaries/audit-git-cc-dev-20260401-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260401_0900.md)
- **2026-03-31 09:00** — [[summaries/audit-git-cc-dev-20260331-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260331_0900.md)
- **2026-03-30 09:00** — [[summaries/audit-git-cc-dev-20260330-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260330_0900.md)
- **2026-03-26 16:21** — [[summaries/audit-git-cc-dev-20260326-1621]] · [raw](../../git_cc_dev/audit/AUDIT_20260326_1621.md)
- **2026-03-25 18:00** — [[summaries/audit-git-cc-dev-20260325-1800]] · [raw](../../git_cc_dev/audit/AUDIT_20260325_1800.md)
- **2026-03-22 10:30** — [[summaries/audit-git-cc-dev-20260322-1030]] · [raw](../../git_cc_dev/audit/AUDIT_20260322_1030.md)
- **2026-03-18 10:30** — [[summaries/audit-git-cc-dev-20260318-1030]] · [raw](../../git_cc_dev/audit/AUDIT_20260318_1030.md)
- **2026-03-17 17:00** — [[summaries/audit-git-cc-dev-20260317-1700]] · [raw](../../git_cc_dev/audit/AUDIT_20260317_1700.md)
- **2026-03-12 15:36** — [[summaries/audit-git-cc-dev-20260312-1536]] · [raw](../../git_cc_dev/audit/AUDIT_20260312_1536.md)
- **2026-03-11 23:29** — [[summaries/audit-git-cc-dev-20260311-2329]] · [raw](../../git_cc_dev/audit/AUDIT_20260311_2329.md)

## Open questions

- Can server-side CI enforcement on `main` (FE and BE) be confirmed, or are CI gates still effectively advisory?
- Do the 11 project/PI-level defects belong to Iteration 7.2, or should they land in a later PI?
- What is the review SLA commitment for HIPAA-critical PRs like BE#55 — is 2+ days acceptable?
- Should Kyaa-A's final-week inactivity trigger a capacity/ownership review before 7.2 planning?
