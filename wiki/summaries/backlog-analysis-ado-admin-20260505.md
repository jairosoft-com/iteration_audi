---
title: "Administration Team — Full Backlog Analysis | Iter 7.3 Day 2 | 2026-05-05"
type: summary
tags: [ado, admin, backlog, iter-7.3, structural-analysis, pi-objective, ghost-tasks]
sources:
  - "../../ado_admin/BACKLOG_ANALYSIS_20260505.md"
created: 2026-05-05
updated: 2026-05-05
---

# Administration Team Full Backlog Analysis — May 5, 2026

Live ADO data pull (all calls used project/team/iteration GUIDs). First full-depth backlog analysis for Admin using the ado_fin format. Solo contributor: [[entities/person-mark-colina]].

## Inventory

| Level | Count | SP / Effort |
|---|---|---|
| PI Objectives | 2 | — |
| Features (active PI7) | 6 | 35 effort pts |
| Features (floaters / stale) | 10 | — |
| Stories & Deliverables (Iter 7.3) | 12 + 2 future-staged | 31 SP committed |
| Tasks (sprint — open) | 29 active/new | 39 hrs remaining |
| Tasks (sprint — closed Day 1–2) | 13 | — |
| **Ghost tasks (old iterations)** | **10** | — |

## PI Objective hygiene — critical failure

**Both PI Objectives are in "New" state. Zero Active PI Objectives in PI7.** This means all sprint execution is running without a formally activated PI Objective.

| ID | Title | State | PI | Issue |
|---|---|---|---|---|
| 200570 | Safety, Training, and Compliance Certifications | New | **PI6** | Stale — PI6 closed, never activated |
| 200577 | Government Accreditation and Eligibility | New | (root — no PI) | Well-written AC (PhilGEPS) but never anchored |

Contrast with Finance team: both teams use Jairosoft FINOPS but Finance has #202535 (PI7, Active). Admin's PI Objective layer is dark.

## Feature layer — 6 Active, 3 Blocked, 7 floating

6 Active features simultaneously all assigned to Mark — high Feature WIP for a 1-member team:
- **#203553** PI7 Admin Support Services (Effort 10) → parent of Davao Adhoc story
- **#203554** Payables Iter 7.3 (Effort 10) → parent of 4 payables stories
- **#203559** JIT BFP renewal 2026 (Effort 5) → task #203561 Closed Day 2 (inspection done)
- **#203654** Admin CR sink cabinet (Effort 5) → execution via Defect #203693 (type mismatch)
- **#202272** Jairosoft Philgeps renewal (Effort 5) → child #202366 in sprint
- **#170869** Jairosoft Signage Installation → children staged Iter 7.4 + 7.5

**Stale features:** #193386 (Aircon PI6, Blocked), #196417 (Re-sealant PI5, Requirements Gathering). PI5 artifact in active backlog is the deepest stale penetration found.

**Floating features (no PI):** 7 features with no PI assignment — #158382, #176942, #196418, #196448, #196752, #200668, #201829. Facilities, solar panel, PhilGEPS document management. These need PI grooming.

## Sprint stories (Iter 7.3) — DoR clean, execution active

12 stories/items committed (31 SP). DoR PASS across the board — all have AC, SP, assignee.

**Day 2 delivery signals:**
- **#203651** (Fixation of post at Davao rooftop) — **Closed May 5 PHT**. Mark's first story closure of Iter 7.3. SP field was null — no velocity credit until SP backfilled.
- **#203556** (Internet payables, Active) — 6 of 8 tasks Closed Day 2
- **#203557** (Utilities payables, Active) — 2 of 7 tasks Closed Day 2
- **#203560** (JIT BFP compliance, Active) — inspection task #203561 Closed Day 2

This is an early-execution pattern — contrast with Iter 7.2 where 0 SP were closed through Day 8 ([[entities/team-ado-admin]] §Previous).

**Type mismatch:** Defect #203693 "Admin CR sink cabinet" (3 SP, Active) is new construction work, not a defect fix. Overlaps Feature #203654. Should be reclassified to User Story and Feature used as parent.

## Ghost tasks — 10 items, 3 eras

Full list in [[summaries/backlog-analysis-ado-admin-20260505]]. Highlights:

| Era | Task IDs | Assigned | Age |
|---|---|---|---|
| xPI1 / Iteration 1.4 (Feb 2025) | 175921–175927 | **Roche Casipong** | ~15 mos |
| xPI1 / Iteration 1.3 (Jan 2025) | 175958–175964 | **Almera K. Tayao** | ~15 mos |
| PI4 / Iteration 4.3 (Oct 2025) | 193234 | Mark Colina | ~7 mos |
| PI6 / Iteration 6.5 (Mar 2026) | 199736 | Mark Colina | ~2 mos |

Roche Casipong and Almera Tayao do not appear elsewhere in active PI7 work. If they are no longer on the team, the items should be closed or reassigned. This adds 10 new entries to [[synthesis/stale-work-items]] Admin section.

## Orphaned training task — cross-team pattern

Task **#203709** "Complete Claude CPN 4 Courses and get Certification" (10 hrs, no parent story) is floating in Iter 7.3 with no parent story. Identical pattern to Finance team's **#203599** "Complete Claude CPN 4 Courses" (10 hrs, orphaned) in the same sprint.

Same training (Claude CPN 4), same sprint, same orphaned structure, both teams (Admin + Finance). This is a portfolio-wide training initiative being tracked as orphaned task-level work rather than as a proper Learning Spike under a Feature. Neither team has a training Feature to parent it to (though Admin's #203553 Admin Support Services could serve).

## Capacity — tight but feasible

| Metric | Value |
|---|---|
| Sprint remaining work | 39 hrs |
| Mark remaining capacity (12 days) | 36–48 hrs |
| Risk item | #203709 (Claude training, 10 hrs = 26% of remaining work, no parent) |

Recommend: link #203709 to Learning Spike under Feature #203553, or stage to Iter 7.4.

## Links

- [[entities/team-ado-admin]] · [[entities/person-mark-colina]]
- [[synthesis/stale-work-items]] — ghost task entries updated
- [[summaries/backlog-analysis-ado-jit-20260505]] — JIT analysis same day
- [[summaries/backlog-analysis-ado-fin-20260505]] (if exists) — Finance analysis with cross-team training task parallel
