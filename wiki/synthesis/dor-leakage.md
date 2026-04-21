---
title: "DoR Leakage — Items Committed Without Definition of Ready"
type: synthesis
tags: [dor, planning, compliance, portfolio, pi7]
sources:
  - "../summaries/audit-ado-shared-20260419-1947.md"
  - "../summaries/audit-ado-admin-20260419-1345.md"
  - "../summaries/audit-ado-fl-dev-20260419-1345.md"
  - "../summaries/audit-ado-hr-20260419-1345.md"
  - "../summaries/audit-ado-ls-dev-20260419-1345.md"
  - "../summaries/audit-ado-otp-20260419-1345.md"
  - "../summaries/audit-ado-fin-20260419-1345.md"
  - "../summaries/audit-ado-jit-20260419-1345.md"
  - "../summaries/audit-git-cc-dev-20260419-1345.md"
  - "../summaries/audit-ado-fl-dev-20260408-0900.md"
  - "../summaries/audit-ado-fl-dev-20260412-0900.md"
  - "../summaries/audit-ado-fl-dev-20260413-0900.md"
  - "../summaries/audit-ado-fl-dev-20260416-0900.md"
  - "../summaries/audit-ado-fl-dev-20260417-0900.md"
created: 2026-04-20
updated: 2026-04-20
---

# DoR Leakage — Items Committed Without Definition of Ready

Cross-team thesis drawn from the Iteration 7.1 Day-14 audit set plus eight earlier PI7.1 checkpoints. The pattern: items enter the sprint commitment without a Description, Acceptance Criteria, or Story Points — and the rubric only catches them at close, not at planning.

## Headline

**3 of 10 teams carried DoR-incomplete items into Iteration 7.1 commitment, and a 4th created a DoR-failing item on Day 14 itself.** Shared Services committed 3 of 5 iteration items in `Grooming` state with no Description, no AC, and no SP ([[summaries/audit-ado-shared-20260419-1947]]); Flawless closed #202381 and #202150 without remediating thin Descriptions ([[summaries/audit-ado-fl-dev-20260419-1345]]); Admin created #202894 Day 14 with a typo'd title, no SP, no Description, no AC ([[summaries/audit-ado-admin-20260419-1345]]); Flawless' DoR Compliance stood at 28.6 Critical as recently as Apr 12 — 8 of 11 sprint items failing ([[summaries/audit-ado-fl-dev-20260412-0900]]).

## What DoR means here

Per [[concepts/scoring-ado-rubric]], DoR Compliance is the 4th of 7 ADO dimensions: the percentage of committed iteration items meeting Definition of Ready. Operationally that means **Description ≥ 30 non-whitespace chars AND Acceptance Criteria ≥ 20 non-whitespace chars**, plus a non-null Story-Point estimate for point-eligible types. Items in `Grooming` state are definitionally not Ready and fail all three checks when committed to an iteration.

## The evidence — team-by-team

| Team | 7.1 items | DoR-failing | Work-item IDs | Source |
|------|----------:|------------:|---------------|--------|
| Shared Services | 5 | **3** (DoR 40.0) | #202928, #202929, #202932 (all `Grooming`, Enabler, no SP/Desc/AC) | [[summaries/audit-ado-shared-20260419-1947]] |
| Flawless | 11 | **2** (DoR 81.8) | #202381 (~29 nws Desc), #202150 (~13 nws Desc) — closed without remediation | [[summaries/audit-ado-fl-dev-20260419-1345]] |
| Admin | 17 visible (new on Day 14) | **1** (#202894 not on 7.1 but polluting 7.2 pipeline) | #202894 — "Goverment payables for" typo, no SP/Desc/AC | [[summaries/audit-ado-admin-20260419-1345]] |
| Flawless | 11 (Apr 12 reading) | **8** (DoR 28.6 🔴) | #202381, #202150, #201569 Netlify Spike, plus 5 others | [[summaries/audit-ado-fl-dev-20260412-0900]] |
| HR | 11 | 0 (DoR 100) | baseline clean | [[summaries/audit-ado-hr-20260419-1345]] |
| Life Style | 7 | 0 (DoR 100) | baseline clean | [[summaries/audit-ado-ls-dev-20260419-1345]] |
| Finance | 5 | 0 (DoR 100) | Desc ≥30 / AC ≥20 across all sprint items | [[summaries/audit-ado-fin-20260419-1345]] |
| OTP | 2 (visible) | 0 (DoR 100) | — | [[summaries/audit-ado-otp-20260419-1345]] |
| JIT | 6 | 0 (DoR 100) | — | [[summaries/audit-ado-jit-20260419-1345]] |
| Colina | 11 | 0 in scope; 1 trailing Desc null (#199597 at ICS rev 40) | — | [[summaries/audit-git-cc-dev-20260419-1345]] |

Net: **3 teams fail at sprint close**; **1 additional team (Admin) spawned a DoR-failing item on Day 14** that is structurally the same pathology.

## Pattern observations

- **Sprint-start leakage.** Flawless opened PI7.1 with DoR 20.0 on Apr 8 — 8 of 10 items non-compliant at Day 3 ([[summaries/audit-ado-fl-dev-20260408-0900]]). The team only climbed to 81.8 on Apr 13 after mid-sprint grooming added AC to 3 Defects ([[summaries/audit-ado-fl-dev-20260413-0900]]). DoR is being fixed *during* the sprint, not before it.
- **Grooming-state commitments.** Shared Services' 3 of 5 `Grooming` enablers (#202928, #202929, #202932) are the purest form of the anti-pattern: items with no SP, no Description, and no AC were assigned an iteration path. The rubric registers DoR 40.0 and Estimation 40.0 as a direct consequence ([[summaries/audit-ado-shared-20260419-1947]]).
- **New-items-mid-iteration.** Admin #202894 was created **on Day 14 itself** with a typo'd title and zero DoR fields — a brand-new DoR failure appearing after sprint planning closed ([[summaries/audit-ado-admin-20260419-1345]]).
- **Late-iteration additions cascade elsewhere.** Colina's ICS lost 9.1 points for `System.Description` still null at revision 40 on item #199597 ([[summaries/audit-git-cc-dev-20260419-1345]]); earlier in PI7.1 a mid-sprint add dropped the ICS component on Apr 7 ([[summaries/portfolio-20260407-1800]], referenced via [[synthesis/portfolio-trend]]).
- **Closure-without-remediation.** Flawless' #202381 and #202150 were closed with DoR gaps unchanged — delivery was credited, DoR was not repaired ([[summaries/audit-ado-fl-dev-20260419-1345]]).
- **Stale Spikes never graduate.** #201569 Netlify/GitHub Transfer Spike has been Ready/Active since Day 3 and is still open at Day 14 without progress ([[summaries/audit-ado-fl-dev-20260419-1345]], [[summaries/audit-ado-fl-dev-20260413-0900]]).

## Why this happens

Three hypotheses, all supported by the evidence set:

1. **Sprint-planning pressure.** Teams that miss the planning deadline accept `Grooming`-state items into commitment rather than leave capacity empty. Shared Services' baseline is the textbook case: capacity not configured, 5 items pulled onto the iteration board mostly because they existed rather than because they were ready.
2. **Stakeholder-pushed items mid-sprint.** Admin #202894 and Colina's mid-sprint add share a signature — items land on the board after planning because a stakeholder (CEO, Finance, Ops) needs them tracked. DoR fields get back-filled later or never.
3. **No enforcement gate.** DoR Compliance is measured *retrospectively* at audit time. Nothing in the current ceremony rejects a commitment with missing Description/AC/SP at planning close. Teams learn that DoR failures are a score penalty, not a blocker — so they ship anyway and absorb the penalty.

## Proposed "DoR Gate" at sprint planning

Add an explicit gate at the end of sprint planning:

1. **Filter at planning close.** Any item on the next iteration's board lacking Description ≥30 nws OR AC ≥20 nws OR (SP null AND type is point-eligible) is flagged `provisional`.
2. **Auto-eject provisional items** back to Product Backlog unless the PO attaches a grooming commitment (target date within 2 days of kickoff). After kickoff +2 days, still-provisional items are removed from iteration path automatically.
3. **Scoring consequence.** Auditors compute DoR Compliance on the **post-gate** item set; `provisional` carve-outs are reported separately and do not pollute the rubric. Teams that skip the gate take the current penalty; teams that run it cleanly get rewarded.
4. **Closure check.** Items closed with DoR fields still below threshold (Flawless #202381 / #202150 pattern) flag a `closed-with-debt` marker in the audit output — delivery credited, DoR debt tracked.

## Downstream effects

DoR leakage is rarely just a DoR score issue. It cascades:

- **Iteration Planning** (dim 1) drops because the sprint goal doesn't tie to items that can't be described. Flawless 6.7 Critical is partly a PI8-denominator artifact but partly DoR-driven ([[summaries/audit-ado-fl-dev-20260419-1345]]).
- **Delivery Predictability** (dim 7) collapses when unready items stall mid-sprint. Shared Services 0 / 3 SP closed, JIT 0 / 14 SP on visible items, and Flawless' stuck #201569 Netlify Spike all trace back to "the item was never ready to execute" ([[summaries/audit-ado-shared-20260419-1947]], [[summaries/audit-ado-jit-20260419-1345]]).
- **Portfolio mean.** Three teams at DoR 40–81.8 drag the 10-team mean by ~2 points directly (via dim 4) and another ~3 points indirectly through Iteration Planning and Delivery Predictability cascades — enough to flip the median from Low to Moderate in a tight window ([[synthesis/portfolio-trend]]).

## Dashboard addition

Add a **DoR Compliance %** column per team in the portfolio dashboard, colored on the shared [[concepts/risk-bands]] thresholds. Pair with a **DoR-failing work-item count** badge so the Shared Services `Grooming`-commitment case is visible at the team-row level — right now it's only surfaced two clicks deep in the audit. This is the same dashboard pattern already recommended for UPS composite masking in [[synthesis/ups-masking-pattern]] and tier-aware service scoring in [[synthesis/service-model-scoring]].

## Related

- [[synthesis/iteration-7.1-close]] — retrospective already flags DoR-at-edges as Theme 2
- [[synthesis/capacity-planning]] — parallel synthesis on the other recurring systemic gap
- [[synthesis/scoring-artifacts]] — close-day reads that interact with DoR failures
- [[synthesis/portfolio-trend]] — portfolio-level impact
- [[concepts/scoring-ado-rubric]] — DoR Compliance definition
- [[entities/team-ado-shared]] · [[entities/team-ado-admin]] · [[entities/team-ado-fl-dev]] · [[entities/team-git-cc-dev]]
