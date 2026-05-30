---
title: "Audit — Colina Health (Git) — Iteration 7.4 Day 1 (2026-05-18 09:00)"
type: summary
tags: [audit, git, colina-health, iteration-7.4, partial-data]
sources:
  - "../../git_cc_dev/audit/AUDIT_20260518_0900.md"
created: 2026-05-29
updated: 2026-05-29
---

# Colina Health (Git) — Iteration 7.4 Day 1 (2026-05-18 09:00)

> `data_mode: partial` — GitHub 401 (raseniero token, fresh attempt confirmed 5/18); HCI D1–D6 carry-forward now 8 audits deep from the 2026-05-10 baseline.

**UPS 67.0 🟡 Moderate** · ICS 91.3% · HCI 71/100 · SGPI 0.0%. Iteration 7.4 Day 1 of 14 (7.1% elapsed; window 2026-05-18 → 2026-05-31).

## Scores

| Metric | Value | Band | Notes |
|--------|------:|------|-------|
| **UPS** | 67.0 | 🟡 Moderate | ICS×0.50 + HCI×0.30 + SGPI×0.20 = 45.65 + 21.30 + 0.00; suppressed by Day-1 0% SGPI |
| **ICS — Iteration Compliance** | 91.3% | 🟢 Low | Quality/DoD 75% — 3 defects (199041, 200027, 200194) null Description; Alignment/Estimation/Integrity 100% |
| **HCI — Health Check Index** | 71/100 | 🟡 Moderate | Flat vs 7.3 final; D8 +1, D10 +1 (Asnari on roster); D6 −1, D9 −1 |
| **SGPI — Sprint Goal Progress** | 0.0% headline / 18.8% proxy | early sprint (Day 1) | 0 of 48 committed SP Closed; proxy = 3 defects (9 SP) already Ready-for-QA |

## Top signals

- Largest committed scope in team history: **12 ICS-eligible items, 48 SP** (6 defects + 6 Enablers) in the 7.4 path.
- Carryover scope-hygiene gap: **AB#204200** (OTP blocker) and **AB#202586** (/lib restructure) appear in the 7.4 hierarchy but still carry IterationPath = 7.3 — Day-1 path-correction action (excluded from ICS eligible set).
- **AB#202588** (RSC migration, 13 SP = 27% of scope) opens in New — no branch/plan; flagged for Day-2 activation.
- Roster fixed: **Asnari Pacalna** now formally on ADO capacity (7 h/day) — resolves the gap flagged since 7.2. New process contributor Carol Cuison on a PR-automation Spike (AB#204232).
- Warm start: Asnari advanced 2 defects to Ready for QA in first hours (06:17). Stale AI-agent PR#9 now 90+ days (8th audit); ADO↔GitHub traceability 0%.

## Δ vs prior

Prior wiki page is 2026-05-16 (Iteration 7.3 Day 13, UPS 82.3 / ICS 95.9 / HCI 73 / SGPI 62.1%). New sprint resets the picture: UPS 82.3 → 67.0 (−15.3, driven by SGPI reset to 0% at Day 1), ICS 95.9 → 91.3 (−4.6, 3 missing descriptions), **HCI 73 → 71 (−2)**. (The source labels HCI delta "0 vs 7.3 final" because 7.3-final on 5/17 had HCI 71; against the wiki prior of 5/16 (HCI 73) the move is −2.)

## Entities

- [[entities/team-git-cc-dev]] · [[entities/person-pcoronia]] · [[entities/person-luzmibel]] · [[concepts/scoring-git-ups]] · [[concepts/risk-bands]]

## Open questions

- Will AB#204200 + AB#202586 paths be corrected to 7.4 (raising committed denominator 48 → 59 SP)?
- Will AB#202588 (13 SP) activate by Day 2, or become the sprint's carryover risk?
- Will the PR-approval Spike (AB#204232) actually configure branch protection and lift HCI D1/D2?

## Notes

- Source audit: `../../git_cc_dev/audit/AUDIT_20260518_0900.md` (partial — GitHub 401, HCI D1–D6 carry-forward 8 audits deep)
- SGPI 0.0% is the expected Day-1 pattern ("trajectory not yet knowable"); source treats ICS+HCI as the meaningful Day-1 headline — carried here rather than stamping a Critical band on early-sprint SGPI.
