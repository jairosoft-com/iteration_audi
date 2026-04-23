---
title: "PI6 Close — Retrospective"
type: synthesis
tags: [pi6, close, retrospective, portfolio, pre-pi7]
sources:
  - "../summaries/portfolio-20260331-0900.md"
  - "../summaries/portfolio-20260330-0900.md"
  - "../summaries/portfolio-20260328-0900.md"
  - "../summaries/portfolio-20260326-1651.md"
  - "../summaries/portfolio-20260325-1900.md"
  - "../summaries/audit-ado-admin-20260331-0900.md"
  - "../summaries/audit-ado-admin-20260330-0900.md"
  - "../summaries/audit-ado-admin-20260330-1000.md"
  - "../summaries/audit-ado-fin-20260331-0900.md"
  - "../summaries/audit-ado-fl-dev-20260331-0900.md"
  - "../summaries/audit-ado-hr-20260331-0900.md"
  - "../summaries/audit-ado-jit-20260331-0900.md"
  - "../summaries/audit-ado-ls-dev-20260331-0900.md"
  - "../summaries/audit-ado-otp-20260331-0900.md"
  - "../summaries/audit-git-aa-dev-20260330-0900.md"
  - "../summaries/audit-git-aa-dev-20260331-0900.md"
  - "../summaries/audit-git-cc-dev-20260331-0900.md"
created: 2026-04-20

## updated: 2026-04-20

# PI6 Close — Retrospective

Retrospective on PI6 close (Iteration 6.6 IP, 2026-03-23 → 2026-04-05). The closest-to-close snapshot on the record is 2026-03-31 09:00 (Day 9 of 14) — the last pre-boundary capture before the PI6 → PI7 transition + Holy Week broke the slope. Understanding this state is the pre-history of [[synthesis/iteration-7.1-close]]: the +22.1 / +19.5 close-day jumps set expectations that PI7.1 would inherit, and the projection-vs-reality gap is documented in [[synthesis/scoring-artifacts]].

## Headline

- **Portfolio mean 72.4 (Moderate) / median 77.1 (Moderate, near Low)** at PI6 close-adjacent — 9-team portfolio, Shared Services not yet onboarded ([[summaries/portfolio-20260331-0900]]).
- **Band distribution:** 3 Low · 3 Moderate · 3 High · **0 Critical** — second consecutive zero-Critical day; the last holdout Auto Allies had exited Critical the prior morning on a +11.3 surge ([[summaries/portfolio-20260330-0900]]).
- **Two biggest single-day movers in the ingest window:** [[entities/team-ado-admin]] **+22.1** (51.0 → 73.1, High → Moderate) and [[entities/team-git-cc-dev]] **+19.5** (59.0 → 78.5, High → Moderate). Combined effect lifted median +16.8 in one day and the mean +4.8 ([[summaries/portfolio-20260331-0900]]).
- **Trend rollup projected 77.7 mean / 79.5 median by Day 14** extrapolating the +1.31/day slope (original PORTFOLIO_TREND_20260331.html since deleted; projection reconstructed in [[synthesis/portfolio-trend]]). The projection was never verified — PI boundary + rubric change + Holy Week broke the slope before Day 14 scored.

## Where teams landed (PI6 close scoreboard, 2026-03-31)

| Team | Overall / UPS | Band | Δ vs 03-30 | Note |
|------|--------------:|------|:-----------|:-----|
| [[entities/team-ado-hr]] HR Recruitment | 90.1 | 🟢 Low | −0.7 | 4 follow-ups landed at project root, diluted IP ratio ([[summaries/audit-ado-hr-20260331-0900]]) |
| [[entities/team-ado-fin]] Finance | 89.5 | 🟢 Low | ±0 | 7th consecutive static audit; 0 closures Day 9 ([[summaries/audit-ado-fin-20260331-0900]]) |
| [[entities/team-ado-jit]] JIT Operation | 85.3 | 🟢 Low | +1.3 | First 6.6 closures (4 items, 5 SP); WIB 70→100 ([[summaries/audit-ado-jit-20260331-0900]]) |
| [[entities/team-git-cc-dev]] Colina Health | 78.5 | 🟡 Moderate | **+19.5** | ICS 92.1 / HCI 58 / SGPI 75.0 — SGPI 0→75 breakthrough ([[summaries/audit-git-cc-dev-20260331-0900]]) |
| [[entities/team-ado-otp]] OTP | 77.1 | 🟡 Moderate | −0.6 | Stationary across 3 audits; IP period underutilized ([[summaries/audit-ado-otp-20260331-0900]]) |
| [[entities/team-ado-admin]] Administration | 73.1 | 🟡 Moderate | **+22.1** | Mark capacity finally configured; sprint pruned 21→12 items ([[summaries/audit-ado-admin-20260331-0900]]) |
| [[entities/team-ado-ls-dev]] Life Style | 59.2 | 🟠 High | −1.1 | DoR ratio worsened as a compliant item closed ([[summaries/audit-ado-ls-dev-20260331-0900]]) |
| [[entities/team-ado-fl-dev]] Flawless Wedding | 49.8 | 🟠 High | −1.1 | 3 Blocked unblocked but 0 closures ([[summaries/audit-ado-fl-dev-20260331-0900]]) |
| [[entities/team-git-aa-dev]] Auto Allies | 49.1 | 🟠 High | +3.5 | ICS 64.3 / HCI 28 / SGPI 42.9 — SGPI +14.3 but 2 rework regressions ([[summaries/audit-git-aa-dev-20260331-0900]]) |

[[entities/team-ado-shared]] Shared Services was not in the portfolio at PI6 close — it debuted as a 10th team on 2026-04-19 at baseline 32.2 ([[synthesis/portfolio-trend]]).

## What drove the close-day jumps

### Administration +22.1 (51.0 → 73.1)

Three mechanical changes between 03-30 AM and 03-31 AM ([[summaries/audit-ado-admin-20260330-0900]] → [[summaries/audit-ado-admin-20260331-0900]]):

1. **Team Capacity 0.0 → 100.0** — Mark's capacity finally wired at 5 h/day (Deployment 1h + Documentation 2h + Requirements 2h). Had been zero for all 8 prior IP-week audits.
2. **Sprint pruned 21 → 12 items, backlog 30 → 20** — a messy 03-30 10:00 bulk-add that had crashed DoR to 4.8% ([[summaries/audit-ado-admin-20260330-1000]]) was rolled back; Estimation 95.2 → 91.7, Backlog Refinement held 100.0.
3. **#201835 added with full DoR** lifted the DoR pass-count from 1 to 2, barely — DoR still only 16.7% on the 12-item residual.

Composition matters: the jump was not delivery progress. Mark's one-person sprint delivered zero state transitions. The +22.1 came from **fixing rubric-inputs** (capacity config + scope right-sizing), not from closing items.

### Colina Health +19.5 (59.0 → 78.5)

Day 9 breakthrough on a genuine delivery event ([[summaries/audit-git-cc-dev-20260331-0900]]):

- **SGPI 0.0 → 75.0** as 3 of 4 committed stories (200188, 200189, 200373) reached Closed overnight — first non-zero SGPI of iteration 6.6.
- **ICS 90.0 → 92.1 Green** from cleaner iteration-item ratio after closures.
- **HCI 55 → 58** on peer-review breakthrough (Colina's first formal reviews ever landed earlier in IP week, sustained through 03-31).
- Real work closed; **this is the only PI6-close jump that was driven by actual delivery signal**.

### Auto Allies exit from Critical (03-30, +11.3 to 45.6)

Exit preceded the 03-31 capture but defined PI6 close's headline ([[summaries/portfolio-20260330-0900]]):

- **SGPI 0% → 28.6%** on 3 closures (8 SP) plus 4 items entered Ready for QA (10 SP) — 18 SP of 28 committed in pipeline at 60% time ([[summaries/audit-git-aa-dev-20260330-0900]]).
- **HCI 20 → 26** (+6) — modest but enough to lift ICS-weighted composite.
- **Structural gaps unchanged** across 11 audits: 0 code reviews, 0 branch protection, 0 ADO-GitHub traceability, 0 CI/CD. The exit was a delivery burst against a broken engineering-discipline baseline.
- By 03-31 the team re-regressed on **2 Ready-for-QA items pushed back to Active** (#201111, #201110 = 6 SP) ([[summaries/audit-git-aa-dev-20260331-0900]]). The Critical-exit held, but the "breakthrough" was fragile.

## What did NOT carry into PI7.1

The trend rollup projection of 77.7 / 79.5 by Day 14 was plausible inside a single PI but the PI boundary broke it ([[synthesis/portfolio-trend]], [[synthesis/scoring-artifacts]]):

- **PI boundary effect (04-01 → 04-05):** mean regressed 72.4 → 64.7 → 59.6 → 60.4 → 56.9 (nadir). Ten mean points evaporated in five days.
- **HR perfect-sprint artifact (04-01):** 90.1 Low → **26.7 Critical** on empty-commitment zero-denominators — not a regression, a rubric edge case ([[synthesis/scoring-artifacts]] Artifact 2).
- **Admin Holy Week evacuation (04-02):** 72.3 → 26.7 (−45.6) as 9 sprint items were intentionally moved to PI7.1 / removed ahead of IP + Holy Week — structural, not performance ([[synthesis/portfolio-trend]]).
- **Rubric transition 6-dim → 7-dim (04-05):** portfolio mean −3.5 in one day; JIT −22.1, Finance −12.1 from methodology change alone ([[synthesis/scoring-artifacts]] Artifact 1).
- **Auto Allies' fragile +11.3 exit** did not generalize: by 04-19 UPS was still Moderate but component HCI 49 / SGPI 21.2% told the masking story that defines [[synthesis/ups-masking-pattern]]. The Critical-exit was real on headline UPS; the underlying engineering-discipline baseline never moved.

Net: projection **77.7 mean** at PI6 Day 14 was never tested directly; what we have is PI7.1 Day 14 closing at **81.0 mean / 82.4 median** ([[summaries/portfolio-20260419-1345]]) — so the PI6 slope was recoverable, but not across the boundary.

## Open questions at PI6 close (backcast from PI7.1 close)

1. **Were the close-day jumps real improvements?** Admin +22.1: **partially** — capacity config was a genuine fix that held into PI7.1 (Team Capacity 100.0 at [[summaries/audit-ado-admin-20260419-1345]]); but the scope-prune didn't carry — by PI7.1 Day 14 the 7.2 pipeline was again over-committed at 32 SP vs 27 SP ceiling. Colina +19.5: **yes** — cleanest trajectory in the dataset ([[synthesis/portfolio-trend]]); team sustained Low all PI7.1 and closed at 90.6 UPS. Auto Allies Critical-exit: **band-wise yes, structurally no** — never re-entered Critical on composite UPS but HCI/SGPI components did.
2. **Would the 77.7 projection have held absent PI boundary?** Given PI7.1's +1.36/day in-PI slope on clean data ([[synthesis/scoring-artifacts]]) the +1.31/day PI6 slope was plausible. Projection failure is a boundary story, not a slope story.
3. **Why didn't Auto Allies' engineering-discipline gaps show up in the close-day numbers?** Because UPS is a composite; the PI6-close zero-Critical day masked persistent HCI Critical the same way PI7.1 close did ([[synthesis/ups-masking-pattern]]). Same pattern, 20 days earlier, already present.
4. **Was HR's 90.1 at PI6 close a warning for the 04-01 artifact?** Retrospectively yes — 14/14 SP delivered is the exact precondition for the perfect-sprint collapse ([[synthesis/scoring-artifacts]] Artifact 2). No carve-out existed at the time.

## Related

- [[synthesis/portfolio-trend]] — cross-PI timeline context
- [[synthesis/iteration-7.1-close]] — PI7.1 close retrospective (the successor state)
- [[synthesis/scoring-artifacts]] — why the projection missed; PI boundary + rubric + Holy Week
- [[synthesis/ups-masking-pattern]] — Auto Allies composite-vs-component pattern originating at PI6 close
- [[concepts/scoring-ado-rubric]] · [[concepts/scoring-git-ups]] · [[concepts/risk-bands]]
- [[entities/team-ado-admin]] · [[entities/team-git-cc-dev]] · [[entities/team-git-aa-dev]] — key PI6-close stories
