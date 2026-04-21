---
title: "Grace Garcia — Finance/Admin + JIT Documentation"
type: entity
tags: [person, grace, jit, fin, stakeholder, blocker]
sources:
  - "../../ado_jit/audit/AUDIT_20260419_1345.md"
  - "../../ado_jit/CLAUDE.md"
  - "../../CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Grace Garcia

Finance/Admin at Jairosoft LLC; also wears a **Documentation** hat on the JIT Operation Team at **1 hour/day** configured capacity. Recipient of portfolio health emails.

- **Email:** <grace@jairosoft.com>
- **Primary team:** Finance/Admin (stakeholder)
- **Secondary team:** [[entities/team-ado-jit]] — Documentation, 1h/day

## Why she has an entity page

88+ mentions across the wiki, almost all on [[entities/team-ado-jit]] audits and summaries, where her **two unstarted work items repeatedly block Delivery Predictability**. The JIT team's 68.8 Moderate score on Iteration 7.1 close is driven in large part by those items — see [[summaries/audit-ado-jit-20260419-1345]].

## Recurring JIT blocker pattern

| Work item | Status at 2026-04-19 | Days untouched |
|-----------|----------------------|---------------:|
| #201504 | Not started | 16 |
| #201514 | Not started | 16 |

Combined story-point commitment is the main driver of JIT's **Delivery Predictability 0.0** on Iteration 7.1 close (0 SP closed Day 12→14). See:

- [[summaries/audit-ado-jit-20260419-1345]] — explicit callout: "Grace's #201504/#201514 untouched 16 days"
- [[summaries/audit-ado-jit-20260417-0900]] — Day 12 snapshot of the same two items unstarted
- [[summaries/audit-ado-jit-20260416-0900]] and earlier — pattern extends further back

## Structural observation

Grace's JIT capacity is **1 h/day** — the smallest allocation on any team in the portfolio. At that allocation, a 2-item sprint commitment is a **capacity-overrun**, not just a delivery miss. Root cause is likely:

1. **Commitment vs. available time** — 2 Documentation items likely exceed 14h (full iteration at 1h/day).
2. **Competing priorities** — her primary Finance/Admin role consumes the rest of her time (eAFS BIR deadline on Apr 15 is hers — see [[concepts/compliance-deadlines]]).
3. **Bus factor 1** — no JIT backup assigned to Documentation work.

## Recommended actions (feed to [[synthesis/iteration-7.1-close]] → 7.2 forward asks)

1. **Rebaseline JIT commitment** to fit 1h/day Documentation capacity (likely ≤1 small item per sprint).
2. **Reassign or de-scope** #201504 and #201514 for 7.2 — pulling them forward compounds the problem.
3. **Check compliance calendar** before committing — if a BIR / eAFS deadline lands mid-iteration, Documentation work should be protected or skipped.
4. **Pair-assign** Documentation work going forward to eliminate the single-point dependency.

## Linked work items

- `#201504` — see JIT audits 04-16 through 04-19
- `#201514` — see JIT audits 04-16 through 04-19
- Finance `#201448` (eAFS Portal Submission, BIR deadline Apr 15) — see [[entities/team-ado-fin]] and [[concepts/compliance-deadlines]]

## Related

- [[entities/team-ado-jit]] — primary board where the blocker surfaces
- [[entities/team-ado-fin]] — her principal role
- [[concepts/compliance-deadlines]] — eAFS/BIR timing conflicts with JIT commitments
- [[synthesis/iteration-7.1-close]] — 7.2 forward ask
