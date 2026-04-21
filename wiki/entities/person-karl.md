---
title: "Karl Caumban — Portfolio Delivery Manager"
type: entity
tags: [person, karl, pdm, stakeholder, portfolio]
sources:
  - "../../CLAUDE.md"
  - "../../ado_admin/CLAUDE.md"
  - "../../ado_shared/CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Karl Caumban

**Portfolio Delivery Manager (PDM).** Co-reviewer of portfolio-level audits with [[entities/person-ramon]]; the primary technical-delivery counterpart to Ramon's CEO/owner role.

- **Email:** <kcaumban@jairosoft.com>
- **Role:** Portfolio Delivery Manager — bridge between portfolio-level outcomes and team-level delivery
- **Scope:** All 10 teams (portfolio-wide)

## Why he has an entity page

Named in every workspace `CLAUDE.md` as PDM stakeholder; recipient of portfolio health emails; co-participant in the recurring **portfolio review meetings with Ramon** documented in memory. The portfolio meeting agendas (`portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_*.html`) are produced specifically for these reviews — see [[concepts/stakeholder-roles]] for role definition.

## Primary workflows

Inferred from the audit portfolio layout:

1. **Portfolio review meeting** — joint with Ramon, uses the agenda output of `/portfolio-meeting-prep [duration]`. Reviews scores, assigns actions, plans PI.
2. **Portfolio health emails** — receives `/portfolio-email` output (also sent to [[entities/person-grace]] and Bomar Sinday).
3. **Cross-team coordination** — likely fields the team-level action items flowing out of [[synthesis/iteration-7.1-close]] and [[synthesis/pi7-plan]].

## Relationship to audit skills

He doesn't appear to run audits directly (that's Ramon), but he **consumes the output**:

- [[synthesis/iteration-7.1-close]] — retrospective he'd review with Ramon
- [[synthesis/pi7-plan]] — the forward-look he'd operationalize across teams
- Individual team entity pages — the drill-in path when a team lands in High/Critical

## Stakeholder context

| Role | Who | Karl's relationship |
|------|-----|---------------------|
| CEO / Audit owner | [[entities/person-ramon]] | Co-reviewer; joint meeting cadence |
| Finance/Admin + JIT | [[entities/person-grace]] | Cross-functional stakeholder in audits |
| Engineering Manager | Bomar Sinday ([[entities/person-bomar]]) | Peer — engineering-delivery counterpart |
| Project Manager | [[entities/person-carol]] | Team-PM he'd interface with for Shared Services / Flawless |
| Admin Team | [[entities/person-mark-colina]] | Bus-factor-1 conversation he'd escalate |

## Open questions

- Does Karl also sign off on rubric changes (e.g., the proposals in [[synthesis/scoring-artifacts]] and [[synthesis/service-model-scoring]]), or is that Ramon-only?
- Is there a standing Karl-owned cadence beyond the Ramon joint meeting? (e.g., daily standups with teams)
- Are his action items from portfolio meetings tracked anywhere? Candidate feature: a Karl-owned action log in `portfolio_report/actions/`.

## Related

- [[entities/person-ramon]] — co-reviewer
- [[concepts/stakeholder-roles]] — PDM role definition
- [[synthesis/iteration-7.1-close]] · [[synthesis/pi7-plan]] — primary review inputs
