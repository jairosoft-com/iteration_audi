---
title: "Git Audit — Unified Performance Score (UPS)"
type: concept
tags: [scoring, git, audit]
sources: ["../../.claude/skills/git_iteration_audit/SKILL.md", "../../CLAUDE.md"]
created: 2026-04-19
updated: 2026-04-19
---

# Git Audit — Unified Performance Score (UPS)

Canonical definition of how Git-based teams are scored. UPS is a weighted composite of three indices.

## Formula

```
UPS = ICS × 0.50 + HCI × 0.30 + SGPI × 0.20
```

| Index | Weight | Measures |
|-------|--------|----------|
| ICS — Iteration Compliance Score | 0.50 | Branching, PR hygiene, commit cadence, merge discipline |
| HCI — Health Check Index | 0.30 | Repo health: CI status, test coverage, open-PR age, review latency |
| SGPI — Sprint Goal Progress Index | 0.20 | Sprint-goal-linked commits / merges as % of total |

## Risk bands

Applies to UPS *and* to each component index. See [[risk-bands]].

## Notes

- **UPS can mask critical components.** E.g., Auto Allies 7.1: UPS 68.6 (Moderate) while HCI 49 (Critical) and SGPI 21.2% (Red). Always report the components alongside the composite.
- Compare to the ADO rubric at [[scoring-ado-rubric]]. The two are intentionally non-comparable on absolute scores because the underlying signal sources differ.

## Related

- [[risk-bands]]
- [[scoring-ado-rubric]]
- Referenced by: [[entities/team-git-aa-dev]], [[entities/team-git-cc-dev]] (once created), Git audit summaries
