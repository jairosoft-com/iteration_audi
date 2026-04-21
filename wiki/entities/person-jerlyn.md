---
title: "Jerlyn Ates — Auto Allies Team Member"
type: entity
tags: [person, jerlyn, git-aa-dev, blocker, auto-allies]
sources:
  - "../../git_aa_dev/audit/AUDIT_20260419_1345.md"
  - "../../git_aa_dev/audit/AUDIT_20260417_0900.md"
  - "../../git_aa_dev/audit/AUDIT_20260416_0900.md"
  - "../../git_aa_dev/audit/AUDIT_20260413_0900.md"
  - "../../git_aa_dev/audit/AUDIT_20260412_0900.md"
  - "../../git_aa_dev/audit/AUDIT_20260409_0900.md"
  - "../../git_aa_dev/CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Jerlyn Ates

QA / Requirements on the Auto Allies Development Team. Configured ADO capacity **6 h/day** (Requirements 2h + Testing 4h), nominal 84h per 14-day iteration. GitHub handle for `jates@jairosoft.com` is **not confirmed** in the audit record (see [[entities/team-git-aa-dev]] §Stakeholders, and 04-19 §Data gaps).

- **Email:** <jates@jairosoft.com>
- **Team:** [[entities/team-git-aa-dev]] — Auto Allies (Git)
- **Role:** QA + Requirements (sole QA resource on the team)

## Why she has an entity page

Jerlyn is the **single-point QA gate** on Auto Allies, and she has contributed **zero GitHub artifacts across the full 14-day Iteration 7.1** ([../../git_aa_dev/audit/AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) §Capacity Balance). This is the **third consecutive sprint** the audit record calls out the same pattern, and it is the proximate cause of the [[synthesis/ups-masking-pattern|UPS masking]] failure mode — healthy code delivery (63.6% proxy SGPI) collapsing at the QA gate to **21.2% Committed SGPI**.

## Timeline — Iteration 7.1

| Audit | Day | Jerlyn GitHub activity | Audit evidence |
|-------|----:|------------------------|----------------|
| [[summaries/audit-git-aa-dev-20260408-0900]] | 3 | 0 commits — resolved AC on Enabler `#201564` at 01:15 UTC (non-GitHub) | ICS reaches 100.0% on her fix |
| [[summaries/audit-git-aa-dev-20260409-0900]] | 4 | 0 items, 0 commits — no testing assignments visible | Listed P5: "Assign Jerlyn to testing tasks" |
| [[summaries/audit-git-aa-dev-20260412-0900]] | 7 | 0 GitHub contributions all 7 days | "Mary Secusana, Jerlyn Ates: zero GitHub contributions all 7 days" |
| [[summaries/audit-git-aa-dev-20260413-0900]] | 8 | 0 commits, 8th consecutive day | "most critical underutilized capacity in the sprint"; owns Enabler `#201564` still Ready-for-Dev |
| [[summaries/audit-git-aa-dev-20260416-0900]] | 11 | Still 0 GitHub, QA not executing | Portfolio [[summaries/portfolio-20260416-0900]] flags "QA Crisis — Jerlyn Ates 0 contributions" |
| [[summaries/audit-git-aa-dev-20260417-0900]] | 12 | 0 GitHub, `#201564` still Ready-for-Dev | 13 SP in QA Testing queue, no QA engagement |
| [[summaries/audit-git-aa-dev-20260419-1345]] | 14 | **0 GitHub artifacts, full 14-day sprint** | §8 risk register: "Worsened (full sprint now)" |

Pattern extends back at least to Iteration 6.5 — the 04-19 audit explicitly calls this **the third consecutive sprint** at zero contribution ([../../git_aa_dev/audit/AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) §P5 forward ask). Earlier iteration audits (e.g. [../../git_aa_dev/audit/AUDIT_2026-03-18_000000.md](../../git_aa_dev/audit/AUDIT_2026-03-18_000000.md), [../../git_aa_dev/audit/AUDIT_2026-03-11_234100.md](../../git_aa_dev/audit/AUDIT_2026-03-11_234100.md)) show the same structural gate: QA tasks assigned but New, blocked on dev completion.

## Impact on team UPS composite

Jerlyn's zero-output sprint hits two of three UPS components ([[concepts/scoring-git-ups]]):

- **SGPI 21.2% 🔴 Critical** — 14 SP of 33 committed parked in QA Testing at sprint close, unchanged 2+ days ([../../git_aa_dev/audit/AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) §7). Proxy SGPI (code merged) is 63.6% — the **42.4 pp gap** is the QA-gate signature.
- **HCI 49/100 🟠 High** — Capacity Balance sub-score 3/10 names Jerlyn and Mary Secusana as the zero-contributor drag ([../../git_aa_dev/audit/AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) §9 item 10).
- **ICS 99.4% 🟢** — unaffected; ICS rewards backlog hygiene, not delivery. This is the core of the [[synthesis/ups-masking-pattern|UPS masking pattern]]: Jerlyn's non-participation is invisible in the dominant 0.50-weight component.

## Pattern observation

Jerlyn is a **different blocker shape** from [[entities/person-grace]]. Grace is *structurally over-committed* — 2 Documentation items against a 1 h/day allocation, where even full engagement cannot clear the backlog. Jerlyn has **6 h/day configured capacity** (84h nominal per sprint) and the QA pipeline is loaded (6 stories / 14 SP Ready-for-QA by Day 12), yet ship zero GitHub artifacts and zero ADO QA state transitions. The gap is **engagement / execution**, not arithmetic.

Both patterns converge at the same portfolio symptom — a single team-member dependency driving a team's Delivery Predictability / SGPI Critical — but the remediation differs: Grace needs a re-baselined commitment; Jerlyn needs an execution protocol or a redistribution/escalation decision.

## Recommended actions (7.2 forward asks)

Per [../../git_aa_dev/audit/AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) §P5 ("Jerlyn Ates QA onboarding plan") and [[entities/team-git-aa-dev]] §Open questions:

1. **Karl Caumban addresses directly on 7.2 Day 1** — three consecutive zero-contribution sprints is the escalation trigger.
2. **Pick one of three paths:** (a) concrete QA execution protocol (test plan template, daily QA standup, ADO comment cadence), (b) redistribute QA responsibility to Cliff Carcueva or Earl Carino, or (c) escalate to HR/management review.
3. **Confirm GitHub identity** for `jates@jairosoft.com` so future audits can measure activity rather than inferring zero from absence ([../../git_aa_dev/audit/AUDIT_20260419_1345.md](../../git_aa_dev/audit/AUDIT_20260419_1345.md) §Data gaps).
4. **Re-baseline Auto Allies commitment** to effective QA capacity (~15 SP) if the team continues with a single QA resource at current throughput.

## Related

- [[entities/team-git-aa-dev]] — primary team; open question #3 tracks the escalation path
- [[synthesis/ups-masking-pattern]] — canonical case where her non-participation drives the Critical SGPI
- [[entities/person-grace]] — parallel single-point blocker (different shape: over-commitment vs. non-engagement)
- [[synthesis/iteration-7.1-close]] — 7.2 forward ask lists "reinstate Jerlyn Ates and Mary Secusana"
- [[concepts/scoring-git-ups]] — UPS component weights that mask her impact on the composite
