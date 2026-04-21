---
title: "Bomar Sinday — Engineering Manager"
type: entity
tags: [person, bomar, engineering-manager, stakeholder]
sources:
  - "../../CLAUDE.md"
created: 2026-04-20
updated: 2026-04-20
---

# Bomar Sinday

**Engineering Manager (EM).** Portfolio-level engineering stakeholder; receives portfolio health emails. Engineering-delivery counterpart to [[entities/person-karl]]'s portfolio-delivery role.

- **Email:** <bsinday@jairosoft.com>
- **Role:** Engineering Manager
- **Scope:** Portfolio-wide engineering concerns (Git teams + ADO dev teams)

## Why he has an entity page

Named in the root `CLAUDE.md` and in memory as a **portfolio email recipient**. That places him in the distribution for `/portfolio-email` output alongside [[entities/person-ramon]], [[entities/person-karl]], and [[entities/person-grace]]. Least-profiled of the four primary stakeholders — this page is a **stub with room to grow** as the wiki accumulates his involvement.

## Likely focus areas (inferred from role)

Based on typical EM responsibilities and the wiki's current signal:

- **Dev team health** — [[entities/team-git-aa-dev]] (Auto Allies), [[entities/team-git-cc-dev]] (Colina Health), [[entities/team-ado-fl-dev]] (Flawless), [[entities/team-ado-ls-dev]] (Life Style) — where engineering-specific issues surface (UPS masking, DoR at sprint-start, stale enablers)
- **Cross-team engineering practice** — branch protection (Colina HIPAA PR #BE55), CI health, code review latency — contributors to HCI in the Git UPS formula
- **Capacity negotiations** — if capacity overbooking is a systemic issue (see [[synthesis/capacity-planning]]), the EM typically owns resourcing conversations

## What's not yet in the wiki

Evidence-limited. No audit directly attributes actions to Bomar. As the audit record grows, his page should expand with:

- Direct decision citations (e.g., "Bomar approved the HIPAA PR triage on 2026-04-xx")
- Team-specific escalations he handled
- Engineering-practice guidelines he's championed

## Stakeholder relationships

| Person | Relationship |
|--------|--------------|
| [[entities/person-ramon]] | Reports alongside; portfolio email distribution |
| [[entities/person-karl]] | Peer — engineering-delivery counterpart to PDM |
| [[entities/person-grace]] | Finance/Admin peer; joint portfolio audience |

## Related

- [[entities/person-karl]] · [[entities/person-ramon]] · [[entities/person-grace]]
- [[concepts/stakeholder-roles]] — EM role definition
- [[synthesis/ups-masking-pattern]] · [[synthesis/capacity-planning]] — engineering-specific synthesis pages he'd likely consume

## Open questions

- Does Bomar have a standing review cadence with the Git teams (Auto Allies / Colina), or does he only engage on escalations?
- Is there engineering-tier guidance (CI standards, branch protection policy, review SLAs) he owns that should be captured in a concept page?
- How are engineering decisions recorded — comments on ADO items, GitHub PRs, Slack? (Affects audit evidence-gathering.)
