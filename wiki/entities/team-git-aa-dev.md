---
title: "Team — Auto Allies (Git)"
type: entity
tags: [team, git, auto-allies, safe]
sources:
  - "../../git_aa_dev/audit/AUDIT_20260419_1345.md"
  - "../../git_aa_dev/CLAUDE.md"
  - "../../portfolio_report/PORTFOLIO_20260419_1953.html"
created: 2026-04-19
updated: 2026-04-19
---

# Auto Allies Development Team (Git)

Product development team for **AutoAllies.com**, working across two GitHub repos (`jairosoft-com/autoallies-version2` frontend, `jairosoft-com/autoallies-api-core` backend) with story tracking in ADO project `Auto Allies` under team `AA Development Team`. Audits are iteration-bounded and combine GitHub developer productivity, SAFe compliance, and ADO-to-GitHub traceability.

## Current state (Iteration 7.1 — 2026-04-06 → 2026-04-19)

| Index | Score | Band |
|-------|------:|------|
| **UPS (Overall)** | **68.6** | 🟡 Moderate |
| ICS (×0.50) | 99.4% | 🟢 Low |
| HCI (×0.30) | 49 / 100 | 🟠 High (Section 9 breakdown: 48 — Critical) |
| SGPI (×0.20) | 21.2% | 🔴 Critical |

> UPS Moderate band masks a Critical SGPI and a High/Critical HCI. The 99.4% ICS (well-formed backlog items) pulls the composite up despite sprint-end delivery collapse. See [[concepts/scoring-git-ups]].

## Real fixable issues

1. **QA gating collapse** — 6 stories (14 SP) parked in QA Testing at sprint end, unchanged 2+ days. Jerlyn Ates contributed zero GitHub artifacts across all 14 sprint days; this is the third consecutive sprint where QA capacity is the binding constraint.
2. **Zero formal PR reviews** on ~48 merged sprint PRs (4.2% had a reviewer assigned, none with approval evidence). Retro spike `#202169` (PR reviews/branch protection) Active but unacted full sprint.
3. **No branch protection** on `develop`/`dev`/`staging`/`main` in either repo — self-merge continues on all branches. Day-1 of 7.2 action: Earl Carino to configure 1-reviewer minimum.
4. **Weekend dormancy** — April 18–19 produced zero PRs/commits; no mitigation window after Day 12 escalation. Sprint planning treats 14 days as working capacity when it is effectively 10.
5. **Commitment miscalibration** — 33 SP committed, 7 SP closed (21.2%) — third consecutive Red SGPI. Either reduce commitment to ~15 SP or invest in QA capacity.

## Structural / context notes

- **UPS masks Critical SGPI**: headline 68.6 (Moderate) hides 21.2% sprint delivery. The ICS weight of 0.50 rewards well-formed items regardless of whether they ship.
- **Healthy code delivery, failed QA gating**: Proxy SGPI (code-merged) = 63.6% vs Committed SGPI = 21.2% — 42.4 pp gap is the clearest signature of the failure mode.
- **Bus-factor risk**: 3 of 5 team members (Joseph, Cliff, Earl) produce 100% of GitHub output; Mary Secusana and Jerlyn Ates at zero contribution for full sprint.
- **Internal score inconsistency in audit**: headline/scorecard reports HCI 49; Section 9 body computes 48 with explicit Sprint Discipline −1 downgrade for sprint-end parking.
- **ICS rounding carry-over**: raw item-weighted ICS = 99.7%, preserved at 99.4% for continuity with Day 12 audit (`#201173` partial Integrity deduction).

## Git references

- **GitHub org:** `jairosoft-com`
- **Frontend repo:** [autoallies-version2](https://github.com/jairosoft-com/autoallies-version2) (default branch `develop`)
- **Backend repo:** [autoallies-api-core](https://github.com/jairosoft-com/autoallies-api-core) (default branch `dev`)
- **ADO project:** `Auto Allies` (`2d7af571-6ef6-4ad0-a509-c440e008b0fb`)
- **ADO team:** `AA Development Team` (`330e6bf1-3515-443c-a2d8-b84f46c38f57`)
- **Workspace:** [../../git_aa_dev/](../../git_aa_dev/)

## Stakeholders

| Who | Role | Email |
|-----|------|-------|
| Ramon Aseniero Jr | Project Owner | <ramon@jairosoft.com> |
| Karl Caumban | Portfolio Delivery Manager / Project Manager | <kcaumban@jairosoft.com> |
| Bomar Sinday | Engineering Manager (review enforcement owner) | <bsinday@jairosoft.com> |
| Jerlyn Ates | QA / Requirements | <jates@jairosoft.com> |
| Joseph Gerona | Developer (FE/BE) | — |
| Cliff Carcueva | Developer | — |
| Earl Carino | Developer / DevOps | — |
| Mary Secusana | Documentation | <msecusana@jairosoft.com> |

## Linked concepts

- [[concepts/scoring-git-ups]] — UPS = ICS·0.50 + HCI·0.30 + SGPI·0.20
- [[concepts/risk-bands]] — Moderate 60–79.9 (current band), Critical <40 (SGPI component)

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-04-19 13:45** — [[summaries/audit-git-aa-dev-20260419-1345]] · [raw](../../git_aa_dev/audit/AUDIT_20260419_1345.md)
- **2026-04-17 09:00** — [[summaries/audit-git-aa-dev-20260417-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260417_0900.md)
- **2026-04-16 09:00** — [[summaries/audit-git-aa-dev-20260416-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260416_0900.md)
- **2026-04-13 09:00** — [[summaries/audit-git-aa-dev-20260413-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260413_0900.md)
- **2026-04-12 09:00** — [[summaries/audit-git-aa-dev-20260412-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260412_0900.md)
- **2026-04-09 09:00** — [[summaries/audit-git-aa-dev-20260409-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260409_0900.md)
- **2026-04-08 09:00** — [[summaries/audit-git-aa-dev-20260408-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260408_0900.md)
- **2026-04-07 17:19** — [[summaries/audit-git-aa-dev-20260407-1719]] · [raw](../../git_aa_dev/audit/AUDIT_20260407_1719.md)
- **2026-04-06 09:00** — [[summaries/audit-git-aa-dev-20260406-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260406_0900.md)
- **2026-04-05 09:00** — [[summaries/audit-git-aa-dev-20260405-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260405_0900.md)
- **2026-04-04 08:45** — [[summaries/audit-git-aa-dev-20260404-0845]] · [raw](../../git_aa_dev/audit/AUDIT_20260404_0845.md)
- **2026-04-02 09:00** — [[summaries/audit-git-aa-dev-20260402-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260402_0900.md)
- **2026-04-01 09:00** — [[summaries/audit-git-aa-dev-20260401-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260401_0900.md)
- **2026-03-31 09:00** — [[summaries/audit-git-aa-dev-20260331-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260331_0900.md)
- **2026-03-30 09:00** — [[summaries/audit-git-aa-dev-20260330-0900]] · [raw](../../git_aa_dev/audit/AUDIT_20260330_0900.md)
- **2026-03-26 16:30** — [[summaries/audit-git-aa-dev-20260326-1630]] · [raw](../../git_aa_dev/audit/AUDIT_20260326_1630.md)
- **2026-03-25 18:00** — [[summaries/audit-git-aa-dev-20260325-1800]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-25_1800.md)
- **2026-03-22 23:29** — [[summaries/audit-git-aa-dev-20260322-2329]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-22_2329.md)
- **2026-03-18 00:00:00** — [[summaries/audit-git-aa-dev-20260318-000000]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-18_000000.md)
- **2026-03-17 17:00:00** — [[summaries/audit-git-aa-dev-20260317-170000]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-17_170000.md)
- **2026-03-16 00:00:00** — [[summaries/audit-git-aa-dev-20260316-000000]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-16_000000.md)
- **2026-03-12 15:09:17** — [[summaries/audit-git-aa-dev-20260312-150917]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-12_150917.md)
- **2026-03-11 23:41:00** — [[summaries/audit-git-aa-dev-20260311-234100]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-11_234100.md)
- **2026-03-10 20:25:00** — [[summaries/audit-git-aa-dev-20260310-202500]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-10_202500.md)
- **2026-03-10 00:00:00** — [[summaries/audit-git-aa-dev-20260310-000000]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-10_000000.md)
- **2026-03-09 00:00:00** — [[summaries/audit-git-aa-dev-20260309-000000]] · [raw](../../git_aa_dev/audit/AUDIT_2026-03-09_000000.md)

## Open questions

- Should the team adopt a **QA-capacity-weighted commitment model** (effective ~15 SP vs committed 33 SP) to produce Green SGPI?
- Will retro spikes `#202168` (descriptions/AC) and `#202169` (PR reviews/branch protection) carry into 7.2 as concrete Day-1 deliverables with acceptance criteria?
- What is the escalation path for Jerlyn Ates' third consecutive zero-contribution sprint — redistribution, protocol change, or HR review?
- Should weekend days be formally excluded from sprint capacity planning (10-day effective sprint for a 14-day cadence)?
