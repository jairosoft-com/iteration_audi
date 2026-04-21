---
title: "Stakeholder Roles — PDM · PM · EM · PO · SM · Auditor"
type: concept
tags: [stakeholder, roles, safe, governance, definitions]
sources:
  - "../../CLAUDE.md"
  - "../../ado_shared/CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Stakeholder Roles

Canonical role definitions as used in the Jairosoft SAFe portfolio. Capture who owns what so audit summaries + syntheses can link to this page rather than re-define terms inline.

## Portfolio-level roles

| Role | Abbreviation | Responsibility | Example |
|------|--------------|----------------|---------|
| **CEO / Audit owner** | — | Sets audit cadence, conventions, scoring rubric; commissions audits | [[entities/person-ramon]] |
| **Portfolio Delivery Manager** | PDM | Bridges portfolio outcomes and team-level delivery; co-reviews audits; operationalizes PI plans | [[entities/person-karl]] (Karl Caumban) |
| **Engineering Manager** | EM | Owns engineering-practice quality (CI, reviews, branch policy, capacity); consumes engineering-specific findings | [[entities/person-bomar]] (Bomar Sinday) |
| **Finance / Admin** | — | Compliance deadlines, payroll, financial reporting; stakeholder in Finance/Admin audits | [[entities/person-grace]] (Grace Garcia) |

## Team-level roles

| Role | Abbreviation | Responsibility | Example |
|------|--------------|----------------|---------|
| **Product Owner** | PO | Owns the backlog; accepts/rejects stories; defines DoR | varies per team — see workspace CLAUDE.md |
| **Scrum Master** | SM | Facilitates ceremonies; removes blockers; tracks velocity | varies per team |
| **Project Manager** | PM | Team-level delivery coordination; work-item status tracking; often overlaps PO in Jairosoft practice | [[entities/person-carol]] (Carol Cuison — Shared Services / Flawless spikes) |
| **Team Member / IC** | — | Does the work; owns assigned items | everyone else |

## Audit-workflow roles

| Role | Responsibility |
|------|----------------|
| **Auditor** | The Claude Code skill (`/ado-safe-audit`, `/git_iteration_audit`) that produces the audit report; driven by [[entities/person-ramon]] |
| **Audit reviewer** | PDM + CEO in the joint review meeting |
| **Remediation owner** | Team PM or Team PO; responsible for acting on `[workspace]/todo/` items |

## Role vs. individual — the practitioner-vs-role distinction

Important in this portfolio: **people wear multiple role-hats**. Two patterns:

1. **Dual-hat IC + role-owner** — e.g., [[entities/person-carol]] is rostered as PM on [[entities/team-ado-shared]] but operates as an IC/assignee on [[entities/team-ado-fl-dev]] spikes. Her PM designation doesn't match her audit-evidence activity.
2. **Tiny-capacity role-holder** — e.g., [[entities/person-grace]] holds a Documentation role on [[entities/team-ado-jit]] at 1h/day, while her primary role is Finance/Admin. See [[synthesis/capacity-planning]] wrong-mix failure mode.

**Implication:** audit recommendations that assume "the PM will handle it" can miss when the PM is actually an IC elsewhere. Always name the individual + check their actual capacity allocation.

## SAFe framework alignment

These roles map to SAFe 6.0 ceremonies as follows:

- **PI Planning** — PDM chairs; CEO attends; POs/SMs facilitate per-team breakout
- **System Demo / Sprint Review** — PO-owned; EM + PDM attend
- **Retrospective** — SM-owned; PDM consumes via audit summaries (e.g., [[synthesis/iteration-7.1-close]])
- **IP (Innovation Planning) Week** — portfolio-level; see PI-boundary artifacts in [[synthesis/scoring-artifacts]]

## Related

- All [[entities/person-*]] pages for concrete examples
- [[synthesis/capacity-planning]] — the wrong-mix failure mode where role vs. capacity mismatches
- [[synthesis/iteration-7.1-close]] — where forward-asks per role are enumerated

## Open questions

- Should teams without a dedicated PO have one assigned? (Several workspaces don't explicitly name a PO in their `CLAUDE.md`.)
- Is the PM role at Jairosoft a formal title, or an informal one that overlaps with IC duties? (Evidence suggests informal — see Carol case.)
- Who owns the **rubric** itself — CEO (Ramon) or is there a joint Ramon+Karl approval process? (See [[synthesis/scoring-artifacts]] for proposed carve-outs needing sign-off.)
