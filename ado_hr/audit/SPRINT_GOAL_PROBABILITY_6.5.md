# Sprint Goal Probability Analysis — Iteration 6.5

**Sprint:** Iteration 6.5 (PI6) — Mar 10 – Mar 22, 2026
**Team:** Human Resource Recruitment Team (Almera Kleer Tayao, sole contributor)
**Analysis Date:** March 17, 2026 (Sprint Day 6 of 9)
**Methodology:** Blended model — capacity-based, velocity-based, and scenario-weighted

---

## 1. Sprint Goal Probability Trend

| Day | Date   | Commitment | Remaining SP | WIP | P(100%) | Key Event |
|-----|--------|-----------|-------------|-----|---------|-----------|
| 1   | Mar 10 | 33 SP     | 33 SP       | 3   | **40.7%** | Sprint Planning — clean start |
| 2   | Mar 11 | 41 SP     | 41 SP       | 11  | **10.3%** | +4 S&M mid-sprint, WIP exploded |
| 5   | Mar 16 | 41 SP     | 41 SP       | 11  | **6.9%**  | Day off, 5-day stall, 13 items overdue |
| 6   | Mar 17 | 35 SP*    | 30 SP       | 10  | **10.3%** | Stall broken, 3 closed, scope reduced |

*Revised after 3 items (6 SP) de-committed to Iteration 6.6 IP

```
P(100% Sprint Goal) Over Time
═══════════════════════════════════════════════════════════

  Day 1 (Mar 10): ████████████████████░░░░░░░░░░░░░░░  40.7%  ← Sprint Start
  Day 2 (Mar 11): █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  10.3%  ← Scope creep, WIP explosion
  Day 5 (Mar 16): ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░   6.9%  ← 5-day stall, day off
  Day 6 (Mar 17): █████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  10.3%  ← Stall broken, scope cut
```

---

## 2. Probability by Completion Target (Day 6)

| Target | SP Needed | Probability | Assessment |
|--------|-----------|-------------|------------|
| 100% complete | 30 SP | 10.3% | Very unlikely |
| ≥80% complete | 24 SP | 13.0% | Unlikely |
| ≥60% complete | 18 SP | 18.0% | Possible but challenging |
| ≥50% complete | 15 SP | 22.8% | Plausible |
| ≥40% complete | 12 SP | 31.3% | Moderate chance |

```
Day 6 Probability by Completion Target
═══════════════════════════════════════════════════════════

100% (30 SP): █████░░░░░░░░░░░░░░░░░░░░░░░░  10.3%
≥80% (24 SP): ██████░░░░░░░░░░░░░░░░░░░░░░░  13.0%
≥60% (18 SP): █████████░░░░░░░░░░░░░░░░░░░░  18.0%
≥50% (15 SP): ███████████░░░░░░░░░░░░░░░░░░  22.8%
≥40% (12 SP): ███████████████░░░░░░░░░░░░░░  31.3%
```

---

## 3. Methodology

Three probability models are computed and blended:

**A. Capacity-Based:** Compares theoretical available hours (6.5 hrs/day × remaining days × WIP efficiency factor) against estimated hours needed (1.5 hrs/SP baseline from Iteration 6.4).

**B. Velocity-Based:** Blends demonstrated velocity (this sprint) with historical velocity (Iteration 6.4: ~4 SP/day). Weights shift toward demonstrated velocity as the sprint progresses. Day 6 burst velocity (5 SP/day) used as current signal.

**C. Scenario-Weighted:** Three scenarios (optimistic at burst pace, realistic at 70% of burst, pessimistic at 35% of burst) weighted 25/50/25.

**WIP Penalty:** Based on Gerald Weinberg's multitasking research — each item above a WIP limit of 5 reduces effective throughput by ~8%. At WIP=11, effective capacity drops to ~52%. At WIP=10, ~60%.

**Blended Probability:** Simple average of all three models.

---

## 4. Risk Factor Decomposition

| Factor | Day 1 | Day 2 | Day 5 | Day 6 |
|--------|-------|-------|-------|-------|
| Commitment (SP) | 33 | 41 (+24%) | 41 | 35 (-15%) |
| Remaining SP | 33 | 41 | 41 | 30 |
| Required Velocity | 4.7 SP/d | 6.8 SP/d | 10.3 SP/d | 10.0 SP/d |
| Demonstrated Velocity | 0.0 | 0.0 | 0.0 | 1.0 SP/d* |
| WIP Items | 3 | 11 | 11 | 10 |
| WIP Penalty | 100% | 52% | 52% | 60% |
| Velocity Gap | 4.7 | 6.8 | 10.3 | 9.0 |

*Day 6 demonstrated velocity is diluted by the 5-day stall average. Burst velocity on Day 6 alone was 5.0 SP/day.

---

## 5. Key Insights

**Insight 1 — The sprint was effectively lost on Day 2.**
When scope increased 24% (33→41 SP) and WIP exploded from 3 to 11, the probability of 100% completion dropped from 41% to 10%. The sprint never recovered from this inflection point.

**Insight 2 — WIP overload caused the delivery stall.**
With 11 items Active for a single contributor, context-switching paralysis set in. Zero items were closed for 5 consecutive days — the worst stall in the audit series. This validates SAFe's recommendation of WIP limits of 3-5 for individual contributors.

**Insight 3 — Scope discipline was the right corrective action.**
The Day 6 de-commitment of 3 items (6 SP) was necessary damage control. Combined with the first 3 closures, it moved the probability needle from 6.9% to 10.3% — a 49% relative improvement.

**Insight 4 — Partial completion is the realistic goal.**
At current trajectory, **49-57% completion** (17-20 of 35 SP) is the most likely outcome. The team should formally plan for ~9-10 items carrying over to Iteration 6.6.

---

## 6. Forecast — Remaining 3 Days (Mar 18-20)

| Scenario | SP/day | SP Closed | Total Done | % of 35 SP | Items Closed |
|----------|--------|-----------|------------|------------|-------------|
| Optimistic | 6.0 | 18 | 23/35 | 66% | ~12 |
| **Day 6 pace** | **5.0** | **15** | **20/35** | **57%** | **~10** |
| Realistic | 4.0 | 12 | 17/35 | 49% | ~9 |
| Conservative | 2.5 | 8 | 13/35 | 37% | ~7 |

**Most Likely Outcome:** 49-57% completion, ~9-10 items carryover to 6.6

---

*Analysis generated March 17, 2026 — Companion to AUDIT_2026-03-17_0900.md*
