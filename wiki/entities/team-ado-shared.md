---
title: "Team — Shared Services (ADO)"
type: entity
tags: [team, ado, shared-services, safe]
sources:
  - "../../ado_shared/audit/AUDIT_20260419_1947.md"
  - "../../portfolio_report/PORTFOLIO_20260419_1953.html"
  - "../../ado_shared/CLAUDE.md"
created: 2026-04-19
updated: 2026-04-19
---

# Shared Services Team (ADO)

Cross-cutting services function covering **UIUX, IT, and DevOps** inside ADO project `Jairosoft Portfolio`. Work routinely flows through other product teams' boards, so this team's own backlog under-reports real delivery.

## Current state (Iteration 7.1 — 2026-04-06 → 2026-04-19)

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | **32.2** | 🔴 Critical |
| Iteration Planning | 15.6 | 🔴 Critical |
| Team Capacity | 0.0 | 🔴 Critical (not configured) |
| Estimation | — | see source |
| DoR Compliance | — | see source |
| Work Item Balance | penalty −70 | 🔴 Critical (Enabler-dominant, no User Stories) |
| Backlog Refinement | 100 | 🟢 Low |
| Delivery Predictability | 0.0 | 🔴 Critical (0 / 3 SP closed Day 14) |

**Baseline audit** — first audit in `ado_shared/`. Score is a mix of real issues and service-model rubric artifacts. See notes below.

## Real fixable issues

1. **Team capacity not configured** for Iteration 7.1 — deterministic zero on that dimension.
2. **3 of 5 iteration items are in `Grooming`** with no Story Points, Description, or Acceptance Criteria — committed without DoR.
3. **0 SP closed out of 3 SP committed** on Day 14 (sprint close today).

## Structural (don't over-weight)

- **Enabler-dominant work mix** is natural for a cross-cutting services team — the −70 penalty on Work Item Balance is a rubric artifact, not a team failure.
- **User Story scarcity** on a services board is expected; product outcomes show up on *consuming* teams' boards.
- **Low Iteration Planning share** (5 of 32 visible root items on current iteration) reflects how Shared Services work gets absorbed elsewhere.

## Portfolio context

- First appearance in portfolio dashboard: [[summaries/portfolio-20260419-1953]] (2026-04-19).
- 10-team portfolio mean 76.1 (Moderate); Shared Services is the sole Critical.
- All other ADO teams are Low/Moderate; see [[summaries/portfolio-20260419-1953]] § Risk Distribution.

## ADO references

- Project: `Jairosoft Portfolio` (`666bb99a-6acd-4999-bb34-efd0e4ea90dc`)
- Team ID: `bd9578fd-5773-48fc-bd80-988dfe5de806`
- Scoped backlog: `Microsoft.RequirementCategory` (board focus: `Stories`)
- Workspace: [../../ado_shared/](../../ado_shared/)

## Stakeholders

| Who | Role | Email |
|-----|------|-------|
| Ramon Aseniero Jr | Project owner | <ramon@jairosoft.com> |
| Carol | Project Manager | <carol@jairosoft.com> |
| Karl Caumban | Portfolio Delivery Manager | <kcaumban@jairosoft.com> |

Team roster TBD — capture from ADO capacity/assignees at next audit.

## Linked concepts

- [[concepts/scoring-ado-rubric]] — 7-dimension rubric used above
- [[concepts/risk-bands]] — Critical < 40

## Audit history

Every audit in this workspace is ingested as a wiki summary. Click any entry for the compact per-audit report.

- **2026-04-21 09:30** — [[summaries/audit-ado-shared-20260421-0930]] · [raw](../../ado_shared/audit/AUDIT_20260421_0930.md)
- **2026-04-19 19:47** — [[summaries/audit-ado-shared-20260419-1947]] · [raw](../../ado_shared/audit/AUDIT_20260419_1947.md)

## Open questions

- Should Shared Services adopt a **service-model scoring adjustment** (reweight or drop Work Item Balance) to make the score comparable to product teams?
- Where does Shared Services' delivery actually show up? Cross-reference FINOPS product team boards on next ingest.
