---
title: "UPS Masking Pattern — Auto Allies as Canonical Case"
type: synthesis
tags: [git, ups, scoring, auto-allies]
sources:
  - "../entities/team-git-aa-dev.md"
  - "../concepts/scoring-git-ups.md"
  - "../concepts/risk-bands.md"
  - "../summaries/audit-git-aa-dev-20260419-1345.md"
  - "../summaries/audit-git-aa-dev-20260417-0900.md"
  - "../summaries/audit-git-aa-dev-20260416-0900.md"
  - "../summaries/audit-git-aa-dev-20260413-0900.md"
  - "../summaries/audit-git-aa-dev-20260412-0900.md"
  - "../summaries/audit-git-aa-dev-20260409-0900.md"
  - "../summaries/audit-git-aa-dev-20260408-0900.md"
  - "../summaries/audit-git-aa-dev-20260407-1719.md"
  - "../summaries/portfolio-20260419-1953.md"
  - "../summaries/portfolio-20260417-0900.md"
created: 2026-04-20
updated: 2026-04-20
---

# UPS Masking Pattern — Auto Allies as Canonical Case

## Headline

The Git **UPS = ICS·0.50 + HCI·0.30 + SGPI·0.20** composite can show Moderate/Low while one or two components are Critical. **[[entities/team-git-aa-dev|Auto Allies]] has run with a Critical SGPI and a Critical-to-High HCI for the entire Iteration 7.1 (9 consecutive audits, 2026-04-07 → 2026-04-19)** while the headline UPS never dropped below 59.6 and finished Moderate at 68.6.

## The pattern

Iteration 7.1 Auto Allies component trajectory — UPS stays High-Moderate while HCI and SGPI are Critical throughout:

| Audit | UPS (band) | ICS % (band) | HCI /100 (band) | SGPI % (band) |
|-------|-----------:|-------------:|----------------:|--------------:|
| [[summaries/audit-git-aa-dev-20260407-1719|04-07 Day 2]] | 59.6 🟠 High | 97.5 🟢 Low | 36 🔴 Critical | 0.0 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260408-0900|04-08 Day 3]] | 61.4 🟡 Moderate | 100.0 🟢 Low | 38 🔴 Critical | 0.0 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260409-0900|04-09 Day 4]] | 61.3 🟡 Moderate | 96.1 🟢 Low | 44 🟠 High | 0.0 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260412-0900|04-12 Day 7]] | 60.4 🟡 Moderate | 99.3 🟢 Low | 36 🔴 Critical | 0.0 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260413-0900|04-13 Day 8]] | 60.0 🟠 High | 94.7 🟢 Low | 40 🟠 High | 3.0 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260416-0900|04-16 Day 11]] | 66.8 🟡 Moderate | 99.4 🟢 Low | 47 🟠 High | 15.2 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260417-0900|04-17 Day 12]] | 68.6 🟡 Moderate | 99.4 🟢 Low | 49 🟠 High | 21.2 🔴 Critical |
| [[summaries/audit-git-aa-dev-20260419-1345|04-19 Day 14]] | **68.6** 🟡 Moderate | 99.4 🟢 Low | 49 🟠 High (48 Crit in §9) | **21.2** 🔴 Critical |

**Duration:** 9 of 9 audits in Iteration 7.1 have SGPI Critical. 8 of 9 have HCI High or Critical. Zero audits in the window have a component-band floor better than Critical. Headline UPS has been Moderate on 6 of 9 — a band that does not trigger intervention in portfolio rollups ([[concepts/risk-bands]]).

## Why the math hides it

The weights are lopsided toward ICS, and ICS rewards **backlog hygiene**, not delivery:

| Component | Weight | What it rewards |
|-----------|-------:|-----------------|
| ICS | 0.50 | Alignment, Estimation, Quality of backlog items — independent of whether they ship |
| HCI | 0.30 | Repo health — PR reviews, branch protection, review latency |
| SGPI | 0.20 | % of committed SP actually delivered |

A team with a well-formed backlog can post a Moderate UPS while shipping nothing:

```
ICS = 100, HCI = 40, SGPI = 0
UPS = 100·0.50 + 40·0.30 + 0·0.20 = 50 + 12 + 0 = 62   → Moderate
```

Auto Allies' 04-19 final is the live version of this: **ICS 99.4 carries 49.7 points (72% of the composite) while only 7 of 33 SP shipped** ([[summaries/audit-git-aa-dev-20260419-1345]]). The 0.20 SGPI weight means a full Critical SGPI (0%) only costs 20 composite points — not enough to push UPS below the 60 Moderate floor when ICS is Green.

## Portfolio has already noticed

The portfolio layer has been manually hacking around the masking for three snapshots:

- **[[summaries/portfolio-20260417-0900]]** (Day 12): "Auto Allies 68.6 **color-coded Orange/High Risk** per `git_iteration_audit` standard despite spec band being Moderate (60–79.9) — HCI 49 Critical, SGPI 21.2% Red." The band override is a symptom, not a fix.
- **[[summaries/portfolio-20260419-1953]]** (Day 14 close): "Auto Allies UPS 68.6 is misleading. Composite is Moderate but components split hard: HCI 49 (Critical), SGPI 21.2% (Red). Illustrates [[concepts/scoring-git-ups]] masking — always report components."
- **[[synthesis/portfolio-trend]]** logs the same finding under "persistent flagged issues": "headline Moderate hides Critical HCI/SGPI."

Manual overrides don't scale to 10+ teams and break the reproducibility of the dashboard. A scoring-policy change is the durable fix.

## Proposed remedy

Three reporting-policy options, ordered by disruption:

1. **(A) Component floor in the dashboard row.** Keep UPS math unchanged, but render **min-component band alongside UPS** in every portfolio row (`UPS 68.6 🟡 / min-component 🔴 Critical SGPI`). Low-cost; preserves historical continuity; makes the masking self-evident.
2. **(B) Worst-band override.** Formalize the 04-17 hack: if **any** component is Critical, the team's displayed band is **downgraded to the worst component's band**, regardless of UPS. UPS numeric stays as-is. This is what the portfolio authors already did manually for Auto Allies.
3. **(C) Mandatory component-breakdown row.** Require every portfolio dashboard and executive summary to list ICS/HCI/SGPI with bands next to the composite. No band logic change; forces visibility. Cheapest to implement; weakest enforcement.

**Recommendation:** ship **(A) + (C)** together — show components always, and surface the min-component band as a second pill beside UPS. Reserve **(B)** for the executive summary band-count tally (teams-with-any-Critical-component counts as Critical), so portfolio headlines like "1 Critical / 4 Moderate" stop underselling compound risk.

All three options should be codified in [[concepts/scoring-git-ups]] (update the formula page) before the next iteration audit batch so the scoring artifact stops being flagged each cycle.

## Related

- [[entities/team-git-aa-dev]] — canonical case
- [[concepts/scoring-git-ups]] — formula under discussion
- [[concepts/risk-bands]] — band definitions the remedy would amend
- [[synthesis/portfolio-trend]] — lists this as an Open Question (#3) across the PI6→PI7.1 window
