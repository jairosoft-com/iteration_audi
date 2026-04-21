---
title: "Carol Cuison — Project Manager"
type: entity
tags: [person, carol, pm, stakeholder]
sources:
  - "../../ado_shared/CLAUDE.md"
  - "../../ado_fl_dev/audit/AUDIT_20260419_1345.md"
  - "../../ado_fl_dev/audit/AUDIT_20260417_0900.md"
  - "../../ado_fl_dev/audit/AUDIT_20260416_0900.md"
  - "../../ado_fl_dev/audit/AUDIT_20260401_0900.md"
  - "../../ado_fl_dev/audit/AUDIT_2026-03-25_094818.md"
  - "../../ado_fl_dev/audit/AUDIT_2026-03-12_003043.md"
created: 2026-04-20
updated: 2026-04-20
---

# Carol Cuison

Project Manager at Jairosoft LLC, rostered on the [[entities/team-ado-shared]] Shared Services Team stakeholder list ([ado_shared/CLAUDE.md](../../ado_shared/CLAUDE.md)). In audit evidence she appears almost exclusively as an **individual contributor / assignee on [[entities/team-ado-fl-dev]] Flawless Wedding App spikes**, not in a PM capacity — a dual-hat pattern similar to [[entities/person-grace]] but inverted (PM on paper, IC in practice).

- **Email:** <carol@jairosoft.com>
- **Primary team (roster):** [[entities/team-ado-shared]] — Project Manager
- **Secondary team (audit evidence):** [[entities/team-ado-fl-dev]] — spike assignee, not in ADO capacity config

## Why she has an entity page

33 mentions across the wiki ([[log.md]]). All concrete audit evidence comes from Flawless, where her assignment to sprint spikes **without a matching ADO capacity entry** has held Team Capacity at 66.7 for 8+ consecutive audits ([[summaries/audit-ado-fl-dev-20260419-1345]], [[summaries/audit-ado-fl-dev-20260325-094818]]). Closing or reassigning #201569 would push Flawless Overall from 79.3 to ~84.1 (Low Risk) per [[synthesis/iteration-7.1-close]].

## Cross-team involvement

| Team | Capacity | Evidence |
|------|---------|----------|
| [[entities/team-ado-shared]] | Listed as PM on roster | [ado_shared/CLAUDE.md](../../ado_shared/CLAUDE.md) line 61 — no audit-evidence activity yet |
| [[entities/team-ado-fl-dev]] | Spike assignee, **not in capacity config** | [[summaries/audit-ado-fl-dev-20260419-1345]], [[summaries/audit-ado-fl-dev-20260312-003043]] (first flag) |

Evidence-limited elsewhere: no mentions in `ado_admin`, `ado_fin`, `ado_hr`, `ado_jit`, `ado_ls_dev`, `ado_otp`, or either Git workspace.

## Known work items she owns or reviews

| Work item | Team | Role | Status history |
|-----------|------|------|----------------|
| #201569 Netlify/GitHub Transfer Spike | Flawless | Assignee (orig.), reassigned Ramon on Mar 31, returned Carol by Apr 16 | [[summaries/audit-ado-fl-dev-20260416-0900]], [[summaries/audit-ado-fl-dev-20260417-0900]], [[summaries/audit-ado-fl-dev-20260419-1345]], [[summaries/audit-ado-fl-dev-20260331-0900]] |
| #199682 Spike | Flawless | Unplanned contributor (first capacity flag) | [[summaries/audit-ado-fl-dev-20260312-003043]] |
| #202087 Retro Spike | Flawless | Assignee (one of two undocumented Retro Spikes added Apr 1) | [[summaries/audit-ado-fl-dev-20260401-0900]], [[summaries/audit-ado-fl-dev-20260405-0900]] |

## Pattern observation

Carol is a **structural capacity-config gap**, not an execution blocker:

1. **Recurring flag, not a stall.** Unlike [[entities/person-grace]]'s untouched JIT items, Carol's assignments do move — #201569 was reassigned Carol → Ramon → Carol across the sprint ([[summaries/audit-ado-fl-dev-20260331-0900]], [[summaries/audit-ado-fl-dev-20260416-0900]]). The issue is ADO hygiene, not delivery.
2. **Specialist profile.** She shows up on Netlify/GitHub transfer and Retro Spikes — infrastructure-adjacent work that Flawless core devs (Luke, Ressa) don't own.
3. **PM role unverified in evidence.** The `ado_shared/CLAUDE.md` roster entry is the only source calling her a Project Manager; no Shared Services audit summary references her activity as a PM (evidence-limited).
4. **Persistent escalation target.** Flagged 15+ consecutive times on Flawless ([[summaries/audit-ado-fl-dev-20260330-1030]] = 15th flag, [[summaries/audit-ado-fl-dev-20260322-2329]] marked "formal escalation needed").

## Recommended actions

1. **Add Carol to ADO capacity config** on [[entities/team-ado-fl-dev]] before 7.2 kickoff (see 7.2 forward asks in [[synthesis/iteration-7.1-close]]), or formally move spike work to a capacity-configured assignee.
2. **Clarify her role split** — if she is PM for [[entities/team-ado-shared]], Flawless spike assignments should either be delegated or her PM allocation should be reduced to reflect actual IC time.
3. **Close or reassign #201569** today per [[synthesis/iteration-7.1-close]] 7.1-close action; leaving it open at Ready is the single highest-leverage Flawless fix.

## Related

- [[entities/team-ado-fl-dev]] — where all her audit-evidence activity occurs
- [[entities/team-ado-shared]] — where she is rostered as PM
- [[entities/person-grace]] — parallel dual-hat stakeholder pattern (IC + primary role elsewhere)
- [[entities/person-ramon]] — took over #201569 temporarily on Mar 31 before it returned to Carol
- [[synthesis/iteration-7.1-close]] — 7.2 forward ask: add Carol to capacity config
