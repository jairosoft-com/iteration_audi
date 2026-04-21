---
title: "Mark Colina — Administration Team (Sole Member)"
type: entity
tags: [person, mark-colina, admin, bus-factor-1, stakeholder]
sources:
  - "../../ado_admin/CLAUDE.md"
  - "../../ado_admin/audit/AUDIT_20260419_1345.md"
created: 2026-04-20
updated: 2026-04-20
---

# Mark Colina

**Sole member of the [[entities/team-ado-admin|Administration Team]].** Handles all Administration work items — a bus-factor-1 situation that's been called out in every recent audit.

- **Email:** <mcolina@jairosoft.com>
- **Role:** Single-person delivery for the Administration Team
- **Team:** [[entities/team-ado-admin]]

## Why he has an entity page

7+ mentions across the wiki; more importantly, he's the **single named assignee for 27 SP of Administration work** in Iteration 7.1. Bus-factor-1 risk flagged in the latest audit:

> **Bus factor 1** — Mark Colina is the sole assignee for 27 SP; any absence halts delivery.
> — [[summaries/audit-ado-admin-20260419-1345]] · `../../ado_admin/audit/AUDIT_20260419_1345.md`

## Iteration 7.1 delivery pattern (notable)

Despite bus-factor-1, Mark closed **18 of 27 SP (67%) on 2026-04-17 in a single burst**, pushing Administration to **87.0 Low Risk** at close. Clean execution; unsustainable structure.

Signals from [[entities/team-ado-admin]] and its audit history:

- Capacity configured at **5h/day**, but the Apr 17 burst likely required substantially more
- Back-loaded delivery is a **repeating pattern** across prior audits in the workspace — see audit history on [[entities/team-ado-admin]]
- **Iteration Planning score of 39.3** on the close audit is a rubric artifact (closed items exit the backlog API; denominator grew Day 14 from new 7.2 items) — sprint execution itself was 100%

## Risks

1. **Single-point dependency.** If Mark is unavailable, Administration work stops — no backup assignee.
2. **Burst-delivery masking.** The 18-SP burst says the capacity config doesn't reflect reality; future sprints may silently under-run if a burst day doesn't materialize.
3. **Work Item Balance penalty.** 100% User Story dominance (no Spike/Enabler mix) carries a −30 penalty — not his fault, but the team's structure makes balance impossible with one person.

## Recommended actions (PI7.2 forward asks — link to [[synthesis/iteration-7.1-close]])

1. **Pair-assign or add a backup** to Administration work to reduce bus-factor-1.
2. **Reset capacity config** to reflect actual working hours (5h/day is probably understated given burst days).
3. **Pace the sprint** to reduce reliance on Day 17–18 bursts.
4. **Introduce a Spike or Enabler** in 7.2 to resolve the Work Item Balance penalty — see also [[synthesis/service-model-scoring]] for related rubric critique.

## Related

- [[entities/team-ado-admin]] — primary team; audit history shows the pattern in depth
- [[summaries/audit-ado-admin-20260419-1345]] — latest audit flagging bus-factor-1 explicitly
- [[entities/person-ramon]] — project owner; would be the approver of a backup-assignee plan
- [[synthesis/capacity-planning]] — portfolio-wide capacity weak-spot synthesis (cites Admin bus-factor-1)
- [[synthesis/iteration-7.1-close]] — retro themes

## Open questions

- Is there an organizational plan to hire an Administration backup, or is bus-factor-1 an accepted operational risk?
- Does Mark consistently carry unpaid overtime on burst days? (If so, that's a sustainability concern beyond the audit rubric.)
