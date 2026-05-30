---
title: "Team — Colina Health (Git)"
type: entity
tags: [team, git, colina-health, safe, healthcare]
sources:
  - "../../git_cc_dev/audit/AUDIT_20260529_0900.md"
  - "../../git_cc_dev/audit/AUDIT_20260521_1500.md"
  - "../../git_cc_dev/audit/AUDIT_20260426_2215.md"
  - "../../git_cc_dev/audit/AUDIT_20260425_1533.md"
  - "../../git_cc_dev/audit/AUDIT_20260424_0902.md"
  - "../../git_cc_dev/audit/AUDIT_20260423_1515.md"
  - "../../git_cc_dev/audit/AUDIT_20260422_0900.md"
  - "../../git_cc_dev/audit/AUDIT_20260421_0055.md"
  - "../../git_cc_dev/audit/AUDIT_20260419_1345.md"
  - "../../git_cc_dev/CLAUDE.md"
created: 2026-04-19
updated: 2026-05-29
---

# Colina Health Product Team (Git)

> **Tooling note (2026-05-28):** GitHub MCP access was restored after a `401` token expiry — a new `raseniero` fine-grained PAT now returns 200 on all three Colina repos. Future audits can run `data_mode: full` (ending the long carry-forward window) once verified against an actual run. The source `git_cc_dev/CLAUDE.md` still carries the older 404 note — intentionally left as-is for now. See [[concepts/github-mcp-call-patterns]].

Healthcare (EMR) product team delivering the Colina Health application via three GitHub repos under the `jairosoft-com` org: `colinahealth-fe` (frontend), `colinahealth-be` (backend), and `colina-health-ai-agent-code-fixing`. ADO planning lives in `Jairosoft Portfolio` under the `Colina Health Product Team` board (`Stories and Deliverables`). Sprint work is primarily defect-fix and architecture enablers, with HIPAA / PHI audit trail being the current high-stakes thread.

## Latest (Iteration 7.4 Day 12 — 2026-05-29 09:00)

**UPS 68.0 🟡 Yellow (Moderate) · ICS 92.5% (🟢) · HCI 71/100 · SGPI 2.1% headline / 78.7% proxy.** `data_mode: full` — GitHub token restored ~2026-05-20; the 5/29 run is the first full-evidence audit in ~11 days (HCI D1–D6 live again, ending the long carry-forward). Recovery from the Day-10 trough: UPS 5/27 63.4 → 5/28 66.3 → 5/29 68.0. **AB#202585** (co-located-folders enabler, 5 SP) **Passed UAT**. **AB#202588 RSC migration (13 SP) deferred to Iteration 7.5** (moved 2026-05-22) — out of 7.4 scope. **SGPI headline 2.1% vs 78.7% proxy** = ADO closure-state lag (work effectively done, items stacked at Passed QA/UAT, not transitioned to Closed). 3 items "Back to Dev" rework (AB#198098 PRN modal 5 SP; AB#199041 viewport regression 2 SP; AB#204942 missing parent 3 SP). Paul bus-factor persists. Sprint ends 2026-05-31. See [[summaries/audit-git-cc-dev-20260529-0900]].

> **AB#200219 decision note (Ramon, 2026-05-24):** the MAR Hawaii-date defect (Defect, 5 SP, Asnari Pacalna / `Kyaa-A`) was pulled from the active sprint to the backlog. FE shipped (`colinahealth-fe` #199 5/18, #204 5/22, #209 5/25 by `pcoronia`; child task 204153 "Followup Fix" Closed), but **BE PR #77** (`colinahealth-be`) was converted to draft — *per a PR #77 comment by `Kyaa-A` citing Ramon's 2026-05-24 note* that a dependent item must resolve first (decision secondhand via the PR comment; the note itself was not seen). Live ADO confirms `System.IterationPath = "Jairosoft Portfolio"` (root/backlog), State Grooming, as of 2026-05-27 — **not** Iteration 7.5.

## Previous (Iteration 7.4 Day 4 PM — 2026-05-21 15:00)

**UPS 62.9 🟡 Yellow (Moderate) · ICS 86.1% · HCI 66/100 · SGPI 0.0%.** `data_mode: partial` — GitHub 401, 12th carry-forward from 2026-05-10. Sole intra-day movement: AB#202585 Active→Peer Testing at 12:59 UTC (Paul, 5 SP co-located folders); Proxy SGPI 22%→32%; HCI D7 +1. Five ICS hygiene failures uncorrected for 4 days (AB#204700+204791 missing parent/SP; AB#199041+200027+200194 missing description) — full remediation restores ICS 100% and UPS ~73. **Critical: AB#202588 RSC migration (13 SP) still New Day 4 — activate by Day 5 or 21 SP gated.** Luzmibel QA gate: 3 items (12 SP) in Peer Testing + days off May 25–26. Paul bus factor: sole owner 31 SP. See [[summaries/audit-git-cc-dev-20260521-1500]].

## Previous (Iteration 7.2 Day 10 — 2026-04-29 02:41 UTC)

**UPS 75.3 🟡 Yellow (Moderate) · ICS 90.5 · HCI 69/100 · SGPI 46.7%.** GitHub 404 exception RESOLVED — live data used, no partial mode. All 5 defects Closed (12 SP, 100% defect velocity). 6 enablers in "Passed QA Testing" (16 SP) — ADO state hygiene gap suppresses SGPI headline. FE PR#172 (AB#203322) merged — iteration drift (item not in 7.2). 5 PRs queued for raseniero review (reviewer bottleneck, 4 days left). CI/CD improvement: ci-pr.yml added to FE + BE repos (#202690). 3 DoR fails persist (200093, 200828, 202028). See [[summaries/audit-git-cc-dev-20260429-0241]].

## Previous (Iteration 7.2 Day 9 — 2026-04-28 02:41 PHT)

**UPS 69.39 🟡 Moderate · ICS 90.5 · HCI 76 · SGPI 6.7%.** BE#55 merged. 28 SP at Passed QA Testing. See [[summaries/audit-git-cc-dev-20260428-0241]].

## Previous (Iteration 7.2 Day 8 Late — 2026-04-27, re-run with full token)

**UPS 68.49 🟡 Moderate · Δ +0.30 · ICS 90.5 (fragile) · HCI 73/100 (fully evidence-based) · SGPI 6.7% headline / 50.0% extended proxy.** FE#146 (202595, 3 SP) merged by raseniero 01:50 PHT Apr 28 — last non-HIPAA development blocker cleared. **BE#55 HIPAA CHANGES_REQUESTED Day 11+ — dominant sprint risk with 5 days remaining.** 2 open PRs in raseniero queue (FE#145 Day 16, BE#55 Day 11+). 19 SP administratively incomplete in ADO. 3 DoD failures unchanged (200093/200828 null Desc; 202028 null AC). BE CI gate weakened (lint + unit tests removed from `ci-pr.yml`). Data mode: `full` — GitHub token restored. See [[summaries/audit-git-cc-dev-20260427-0902]].

## Previous (Iteration 7.2 Day 7 Evening — 2026-04-26 22:15 PHT) — GitHub token 404 ongoing

**UPS 68.19 🟡 Moderate · Δ +1.64 · ICS 90.5 · HCI 82/100 (carry-forward) · SGPI 6.7% headline / 43.3% proxy.** **First sprint closure: #202810 closed (2 SP)**. BE#55 HIPAA CHANGES_REQUESTED Day 10+. 5 PRs await `raseniero` review (18 SP = 60% of sprint blocked). Data mode: `partial` — raseniero token 404 ongoing. See [[summaries/audit-git-cc-dev-20260426-2215]].

## Previous (Iteration 7.2 Day 6 — 2026-04-25 15:33 PHT) — GitHub token 404 ongoing

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
- [[concepts/github-mcp-call-patterns]] — GitHub MCP server / PAT rotation ops (root cause of the `partial` carry-forward window)

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-05-29 09:00** — [[summaries/audit-git-cc-dev-20260529-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260529_0900.md) (full — token restored, Iter 7.4 Day 12, current)
- **2026-05-28 09:05** — [[summaries/audit-git-cc-dev-20260528-0905]] · [raw](../../git_cc_dev/audit/AUDIT_20260528_0905.md) (Iter 7.4 Day 11 — P0 AB#204200 path fix, ICS Green, +2.9)
- **2026-05-27 02:43** — [[summaries/audit-git-cc-dev-20260527-0243]] · [raw](../../git_cc_dev/audit/AUDIT_20260527_0243.md) (Iter 7.4 Day 10 — sprint low 63.4, Day-10 zero-closure)
- **2026-05-23 09:00** — [[summaries/audit-git-cc-dev-20260523-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260523_0900.md) (Iter 7.4 Day 6 — recovery wave +4.7)
- **2026-05-22 09:00** — [[summaries/audit-git-cc-dev-20260522-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260522_0900.md) (Iter 7.4 Day 5 — AB#202588 RSC deferred to 7.5, +3.9)
- **2026-05-21 15:00** — [[summaries/audit-git-cc-dev-20260521-1500]] · [raw](../../git_cc_dev/audit/AUDIT_20260521_1500.md) (partial — GitHub 401, Iter 7.4 Day 4 PM)
- **2026-05-20 02:04** — [[summaries/audit-git-cc-dev-20260520-0204]] · [raw](../../git_cc_dev/audit/AUDIT_20260520_0204.md) (Iter 7.4 Day 3 — sprint low 62.6, ungroomed adds)
- **2026-05-19 02:41** — [[summaries/audit-git-cc-dev-20260519-0241]] · [raw](../../git_cc_dev/audit/AUDIT_20260519_0241.md) (Iter 7.4 Day 2 — −2.0, AB#202588 still New)
- **2026-05-18 09:00** — [[summaries/audit-git-cc-dev-20260518-0900]] · [raw](../../git_cc_dev/audit/AUDIT_20260518_0900.md) (Iter 7.4 Day 1 — sprint open, 48 SP scope)
- **2026-05-16 02:41** — [[summaries/audit-git-cc-dev-20260516-0241]] · [raw](../../git_cc_dev/audit/AUDIT_20260516_0241.md) (Iter 7.3 sprint-end — closed 🟢 81.7)
- **2026-05-11 02:43** — [[summaries/audit-git-cc-dev-20260511-0243]] · [raw](../../git_cc_dev/audit/AUDIT_20260511_0243.md) (Iter 7.3 Day 7 — 🟢 Green 85.2, +13.6 delivery wave)
- **2026-05-03 09:03** — [[summaries/audit-git-cc-dev-20260503-0903]] · [raw](../../git_cc_dev/audit/AUDIT_20260503_0903.md) (Iter 7.3 Day 1 — sprint open)
- *Curated chain: 11 signal audits ingested above for 2026-05-03 → 2026-05-29. 21 flat daily re-runs in this window (Iter 7.3/7.4) were intentionally skipped (< ~2-pt variance, no new signal); raw files remain in `git_cc_dev/audit/`.*
- **2026-04-28 02:41** — [[summaries/audit-git-cc-dev-20260428-0241]] · [raw](../../git_cc_dev/audit/AUDIT_20260428_0241.md) (partial label; full evidence used — BE#55 merged, 28 SP at QA/UAT, ADO state lag)
- **2026-04-27 09:02** — [[summaries/audit-git-cc-dev-20260427-0902]] · [raw](../../git_cc_dev/audit/AUDIT_20260427_0902.md) (full — GitHub token restored)
- **2026-04-26 22:15** — [[summaries/audit-git-cc-dev-20260426-2215]] · [raw](../../git_cc_dev/audit/AUDIT_20260426_2215.md) (partial — GitHub 404)
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

- **ADO state lag (Day 9+):** 28 SP sit at Passed QA Testing / Ready for UAT but ADO Closed count is 2 SP. Will Karl/QA advance and close 202594, 202595, 202690, 202696, 202028 in Days 9–11 to unlock headline SGPI?
- **202844 (5 SP, Role-based route guard):** Active with no PR and 5 days remaining — will a branch + PR appear Day 10, or will this be formally scope-reduced?
- Can server-side CI enforcement on `main` (FE and BE) be confirmed, or are CI gates still effectively advisory?
- Do the 11 project/PI-level defects belong to Iteration 7.2, or should they land in a later PI?
- What is the review SLA commitment for HIPAA-critical PRs like BE#55 — is 2+ days acceptable? (BE#55 now resolved; applies to future HIPAA items.)
- Should Kyaa-A's final-week inactivity trigger a capacity/ownership review before 7.2 planning?

## Notes on project exceptions (added 2026-04-23)

- **Non-developer team members** (Luzmibel QA, Jaszmeine Design) are not penalized for GitHub absence per the same principle Ramon established for AA on 2026-04-23. Filed in `git_cc_dev/CLAUDE.md` Project Exceptions. See [[summaries/transcript-lpm-review-2026-04-23]].
- **GitHub API 404 (Apr 21 onward)** — token access-scope issue affecting all 3 Colina repos. Audits through resolution carry `data_mode: partial` and conservative HCI carry-forwards. Not a team failure. **Update 2026-05-28:** token recurred as a `401` expiry and was rotated to a new `raseniero` PAT; access restored to all 3 repos. See [[concepts/github-mcp-call-patterns]].
