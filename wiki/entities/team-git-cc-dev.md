---
title: "Team — Colina Health (Git)"
type: entity
tags: [team, git, colina-health, safe, healthcare]
sources:
  - "../../git_cc_dev/audit/AUDIT_20260425_1533.md"
  - "../../git_cc_dev/audit/AUDIT_20260424_0902.md"
  - "../../git_cc_dev/audit/AUDIT_20260423_1515.md"
  - "../../git_cc_dev/audit/AUDIT_20260422_0900.md"
  - "../../git_cc_dev/audit/AUDIT_20260421_0055.md"
  - "../../git_cc_dev/audit/AUDIT_20260419_1345.md"
  - "../../git_cc_dev/CLAUDE.md"
created: 2026-04-19
updated: 2026-04-25
---

# Colina Health Product Team (Git)

Healthcare (EMR) product team delivering the Colina Health application via three GitHub repos under the `jairosoft-com` org: `colinahealth-fe` (frontend), `colinahealth-be` (backend), and `colina-health-ai-agent-code-fixing`. ADO planning lives in `Jairosoft Portfolio` under the `Colina Health Product Team` board (`Stories and Deliverables`). Sprint work is primarily defect-fix and architecture enablers, with HIPAA / PHI audit trail being the current high-stakes thread.

## Latest (Iteration 7.2 Day 6 — 2026-04-25 15:33 PHT) — GitHub token 404 ongoing

**UPS 69.85 🟡 Moderate · −1.0 vs Day 5 (rounding correction, not regression) · ICS 90.5 fragile Green · HCI 82/100 (carry-forward) · SGPI 0.0% headline / 26.7% proxy** · **4 items in `Passed QA Testing` = 8 SP ready to credit** — ADO closure clicks are the only velocity unlock needed. **#202028 PRN defect (2 SP) in `Ready for Dev` for 11+ days** with no GitHub branch or PR — most overdue delivery failure in sprint. FE repo: 3 commits in Apr 24 window; BE repo: no commits since Apr 20 (5-day dead window). Data mode: `partial` — raseniero token 404 since Apr 21; HCI dims 1–6 carry-forward from Day 5. 8 days remaining in sprint. See [[summaries/audit-git-cc-dev-20260425-1533]].

## Previous (Iteration 7.2 Day 5 — 2026-04-24 09:02 PHT) — GitHub API restored

**UPS 70.85 🟡 Moderate · Δ +2.30 · ICS 90.5 fragile Green (+0.2) · HCI 82/100 (+4 on live GitHub) · SGPI 0.0% early-sprint.** **All 3 repos fully live** — raseniero token fix confirmed (4-day partial/denied window closed). **#202033 back on track** (Kyaa-A shipped FE#162 → FE#163 in <2h; ADO advanced Ready for QA 10:08 UTC). **#200828 merged to `main`** (FE#161, 08:01 UTC — production). Compounding risks: **#202028 PRN defect 10 days in Ready-for-Dev**, **untriaged defect backlog at 11** (+2 today), **BE#55 HIPAA Day 8+ CHANGES_REQUESTED** (pcoronia-blocked). See [[summaries/audit-git-cc-dev-20260424-0902]].

## Current state (Iteration 7.2 Day 3 — 2026-04-22 09:00 PHT, partial)

| Score | Value | Band |
|-------|------:|------|
| **ICS — Iteration Compliance** | 90.3% | 🟢 Green (fragile — 0.3 above Yellow) |
| **SGPI — Committed Scope** | 0.0% headline / 20.0% Delivered-Proxy | 🔴 Red headline; 🟡 activating via QA funnel |
| **HCI — Engineering Health** | 77/100 | 🟡 Moderate |

Source: [[summaries/audit-git-cc-dev-20260423-0856]] (partial). Day 4 Movement Day — **net positive**: #202690 + #200828 advanced to Peer Testing (resolving Day-3 HIPAA urgency); #202033 regressed Active → Back to Dev (QA failure). HCI +1 to 78 (Traceability 8→9, 9/11 items now have GitHub artifacts). **ICS still fragile 90.3** — 3 DoD failures (#200093, #200828, #202028) unremediated 2nd day. **BE#55 HIPAA rework Day 6** — critical.

## Historical (Iter 7.1 close — 2026-04-19, UPS 90.6 Low)

Iteration 7.1 closed at UPS **90.6 Green** — all 11 committed defects (21 SP) Closed. See [[summaries/audit-git-cc-dev-20260419-1345]]. First AI-assisted PR in team history (BE#55 with Claude Code assistance). Weekend pause real. Governance max at 10/10 HCI enabler re-scoping.

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

- **2026-04-25 15:33** — [[summaries/audit-git-cc-dev-20260425-1533]] · [raw](../../git_cc_dev/audit/AUDIT_20260425_1533.md) (partial — GitHub 404)
- **2026-04-23 08:56** — [[summaries/audit-git-cc-dev-20260423-0856]] · [raw](../../git_cc_dev/audit/AUDIT_20260423_0856.md) (partial — GitHub 404)
- **2026-04-22 09:00** — [[summaries/audit-git-cc-dev-20260422-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260422_0900.md) (partial — GitHub 404)
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

## Notes on project exceptions (added 2026-04-23)

- **Non-developer team members** (Luzmibel QA, Jaszmeine Design) are not penalized for GitHub absence per the same principle Ramon established for AA on 2026-04-23. Filed in `git_cc_dev/CLAUDE.md` Project Exceptions. See [[summaries/transcript-lpm-review-2026-04-23]].
- **GitHub API 404 (Apr 21 onward)** — token access-scope issue affecting all 3 Colina repos. Audits through resolution carry `data_mode: partial` and conservative HCI carry-forwards. Not a team failure.
