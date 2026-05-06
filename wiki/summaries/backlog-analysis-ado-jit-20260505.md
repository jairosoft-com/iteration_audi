---
title: "JIT — Full Backlog Analysis | Iter 7.3 Day 2 | 2026-05-05"
type: summary
tags: [ado, jit, backlog, iter-7.3, structural-analysis]
sources:
  - "../../ado_jit/BACKLOG_ANALYSIS_20260505.md"
created: 2026-05-05
updated: 2026-05-05
---

# JIT Full Backlog Analysis — May 5, 2026

Live ADO data pull (all calls used project/team/iteration GUIDs). First full backlog analysis for JIT using the ado_fin analysis format.

## Inventory

| Level | Count | SP |
|---|---|---|
| PI Objectives / Features | **None** | — |
| Stories & Deliverables (open) | 39 | 56 SP open + 5 closed |
| Task children (estimated) | ~61 | not fetched |

**Key structural finding:** JIT has no ADO Feature or Epic hierarchy. All 39 items are flat at the Requirement level (User Story, Training, Spike, Courseware). PI-level progress is invisible without Features. Contrast with [[entities/team-ado-fin]] which has 7 Features grouping 7 sprint items.

## Workstream breakdown (5 identified)

| Workstream | Owner | Items 7.3 | SP |
|---|---|---|---|
| CSS NC II Training Modules | Teofilo | 7 | 21 |
| Marketing & Enrollment | Armelita | 10 | 25 |
| EBET Scholarship | Armelita | 4 | 7 |
| TESDA Compliance | Grace | 2 | 5 |
| Social Media Content | Samantha | 4 | 4 |

## Backlog beyond current sprint

- **Iter 7.4** (5): UM Matina/HCDC intern demos, Tech Talk (unassigned), 2 Teofilo Training modules
- **Iter 7.5** (3): UM Digos intern demo, 2 Tech Talk spikes (both unassigned; one misnamed "IT7.6" in 7.5)
- **PI7 root, unsprinted** (3): 203805–203807 — Teofilo's next Training sequence, no iteration assigned
- **PI8** (1): #200766 ODOO OpenCat SIS — Active in PI8 while PI7 is running (cross-PI state risk)
- **Root / no iteration** (1): #193054 SAFe RTE MC — Blocked, no unblock criteria

## CSS NC II Training sequence (Teofilo)

Linear delivery sequence across Iter 7.3:

```
[CLOSED]    3.2-1 DHCP (#203156)         ← done May 5
[MARKETING] 3.2-2 DNS (#203157)          ← in progress
[NEW ⚠️]   3.2-3 Remote Desktop (#203158) ← DoR FAIL
[NEW]       3.2-4 Folder Redirection (#203159)
[NEW]       3.2-5 Printer Deployment (#203160)
[NEW]       3.3-1 Server Pre-Deployment (#203161)
[NEW]       3.3-2 Server Security (#203162)
```

Teofilo executing in correct sequential order. At 4.8 pts/day capacity, all 7 items feasible within Iter 7.3. Critical: #203158 must get Description + AC before Teofilo arrives (est. Day 4–5).

## Key findings

| # | Finding | Severity |
|---|---|---|
| 1 | #203158 DoR fail — no Desc/AC since Apr 27, next in sequence | High |
| 2 | Grace: 0 Active items Day 2 (5 SP all in Ready for Dev) | High |
| 3 | No Feature hierarchy — PI-level tracking invisible | Medium |
| 4 | 3 future Tech Talk Spikes unassigned (203243, 203244, 203245) | Medium |
| 5 | #203245 misnamed "IT7.6" parked in Iter 7.5 | Medium |
| 6 | #200766 Active in PI8 during PI7 sprint | Medium |
| 7 | 203805–803807 in PI7 root — no iteration assigned | Medium |
| 8 | #193054 Blocked, no iteration, no unblock criteria | Medium |
| 9 | Samantha: 4 items in Grooming with no task breakdown | Low |
| 10 | No Iteration 7.3 Goal defined | Low |

## Same-day audit responsiveness

Team addressed 4 of 5 urgent Day-2 recommendations within hours of the morning audit:
- #203156 DHCP Closed (urgent: close today) → **closed 14:40 UTC** ✅
- #203157 DNS started (Marketing state) → **May 6 01:06 UTC** ✅
- #203242 Spike assigned (persistent: assign Armelita) → **May 6 00:43 UTC** ✅
- #200771 stale updated (persistent: update or close) → **May 6 00:40 UTC** ✅
- #203158 DoR fix (urgent: add Desc/AC) → **still failing** ⚠️

This is the first documented same-day multi-item audit response pattern for JIT. Worth tracking as a behavioral signal.

## Capacity check

| Contributor | Remaining capacity (12 days) | SP Open | Feasible? |
|---|---|---|---|
| Armelita | 6 pts/day × 12 = 72 | 30 | Yes |
| Teofilo | 4.8 pts/day × 12 = 57.6 | 18 | Yes |
| Grace | 1 pt/day × 12 = 12 | 5 | Yes (but 0 Active) |
| Samantha | 1 pt/day × 12 = 12 | 4 | Yes (but all Grooming) |

Sprint fully deliverable at current capacity. Execution risk, not capacity risk.

## Links

- [[entities/team-ado-jit]] · [[entities/person-armelita]] · [[entities/person-teofilo]]
- [[summaries/audit-ado-jit-20260505-0900]] (same-day audit)
- [[concepts/scoring-ado-rubric]] · [[synthesis/bus-factor]]
