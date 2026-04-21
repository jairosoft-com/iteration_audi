---
title: "Auto Allies Audit — 2026-04-19 13:45 (Iteration 7.1 Final)"
type: summary
tags: [audit, git, auto-allies, iteration-7.1, safe]
sources:
  - "../../git_aa_dev/audit/AUDIT_20260419_1345.md"
created: 2026-04-19
updated: 2026-04-19
---

# Auto Allies Audit — Iteration 7.1 Day 14 (Final)

Source: [AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) · 2026-04-19 13:45 PDT · Iteration 7.1 (2026-04-06 → 2026-04-19)

## TL;DR

Sprint 7.1 closes Red: **UPS 68.6 (Moderate) masks SGPI 21.2% (Critical)** — only 7 SP closed of 33 committed. The composite is propped up by a 99.4% ICS on well-formed backlog items; the real story is **healthy code delivery (63.6% proxy SGPI) failing at the QA gate** (14 SP parked in QA Testing at sprint end, third consecutive Red-SGPI sprint). The portfolio dashboard [[summaries/portfolio-20260419-1953]] flagged the same UPS-masks-Critical pattern.

## Headline scores

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | **68.6** | 🟡 Moderate |
| ICS (×0.50) | 99.4% | 🟢 Low |
| HCI (×0.30) | 49 / 100 | 🟠 High (Section 9 body: 48 — Critical) |
| SGPI (×0.20) | 21.2% | 🔴 Critical |

## Key claims

- **SGPI 21.2%**: 7 SP closed / 33 committed. SGPI trajectory Day 1 → Day 14: 3.0% → 3.0% → 15.2% → 21.2% → 21.2%. Zero movement in final 48 hours (weekend dormancy).
- **14 SP stuck in QA Testing** (6 stories) at sprint end, unchanged 2+ days. Proxy-SGPI (merged code) = 63.6%; gap vs Committed-SGPI = 42.4 pp.
- **Zero formal PR reviews on ~48 merged sprint PRs** — 2 PRs (FE #103, #105, 4.2%) had `requested_reviewers` populated, none with approval evidence. Retro spike `#202169` (PR review enforcement) Active but unacted full sprint.
- **Two team members at zero contribution for full 14-day sprint**: Jerlyn Ates (QA — 3rd consecutive sprint), Mary Secusana (Documentation). Three developers (Joseph Gerona, Cliff Carcueva, Earl Carino) produced 100% of ~48 merged PRs.
- **ICS 99.4% (Green)**: 16 non-spike items all pass Alignment/Estimation/Quality; only deduction is `#201173` Revenue Cat Migration (Integrity 15/20 — unblocked Blocked→Active Day 14 but no code merged).
- **HCI 49/100 Critical**: PR Review 2/10, Branch Protection 1/10, Capacity Balance 3/10 are the binding lows; Backlog Hygiene 8/10 and Traceability 7/10 are the highs. Section 9 explicitly downgrades Sprint Discipline 7→6 (total 48) while headline tables retain 49.

## Entities touched

- [[entities/team-git-aa-dev]]

## Contradictions / notes

- None — baseline for this ingest. Prior audits in `git_aa_dev/audit/` (Day 1–Day 12 of Iteration 7.1) establish the trajectory cited above but have not been ingested as wiki summaries.
- **Internal audit inconsistency flagged (not a contradiction with prior wiki)**: audit headline/scorecard cites HCI 49; Section 9 breakdown computes 48 with Sprint Discipline −1. Entity page notes both.

## Open questions

- Should the Auto Allies team entity track **Committed-SGPI vs Proxy-SGPI gap** as a first-class metric to surface the QA-gating failure mode?
- Are the retro spikes `#202168` and `#202169` creating a recurring carry-over pattern worth promoting to a `synthesis/` page on "retro-spike rot"?
- Does `#201173` Revenue Cat Migration late unblock (Day 14) indicate an ADO state-hygiene issue worth comparing across Git teams?

## Linked concepts

- [[concepts/scoring-git-ups]] — UPS = ICS·0.50 + HCI·0.30 + SGPI·0.20
- [[concepts/risk-bands]] — Moderate 60–79.9 (headline UPS), Critical <40 (SGPI component)
