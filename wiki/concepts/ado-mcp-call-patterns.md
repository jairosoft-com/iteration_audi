---
title: "ADO MCP Call Patterns"
type: concept
tags: [ado, mcp, tooling, api, operational]
sources: []
created: 2026-05-05
updated: 2026-05-05
---

# ADO MCP Call Patterns

Operational rules for calling Azure DevOps MCP tools within this portfolio. Violations cause silent failures that produce broken audits.

## Rule 1 — Always use IDs, never display names

**Applies to:** all ADO MCP tool calls — project, team, iteration, board.

Pass GUIDs for `project`, `team`, and `iterationId` parameters. Display names (e.g., `"Jairosoft FINOPS"`, `"OTP Team"`) silently return empty results on certain projects.

**Confirmed failure (2026-05-05):**

```
tool: work_list_team_iterations
project: "Jairosoft FINOPS"  → "No iterations found"  ❌
project: "e7739905-28a3-4ae1-9173-7f6cd13b3494"  → 19 iterations  ✅
```

**Rule generalized by Ramon 2026-05-05:** apply to all ADO project/team/board calls, not just OTP.

## Known Project IDs

| Workspace | ADO Project | Project ID |
|-----------|------------|------------|
| `ado_otp` | OTP (Jairosoft FINOPS) | `e7739905-28a3-4ae1-9173-7f6cd13b3494` |
| `ado_shared` | Jairosoft Portfolio | see [[entities/team-ado-shared]] |
| all others | Jairosoft FINOPS | see individual workspace CLAUDE.md |

## Known Team IDs (OTP)

| Team | ID |
|------|----|
| OTP Team | `64de61f0-1203-4b01-aee2-6b4415aec52b` |

## Known Iteration IDs (OTP)

| Iteration | ID |
|-----------|----|
| 7.1 | `ce4205d6-4038-4752-a0b8-dda248031686` |
| 7.2 | `611496a8-1907-483b-94b9-4e3ee575faf5` |
| 7.3 (current) | `86aab8f1-cd46-4fe6-a810-00fba59b46a3` |
| 8.1 | `b0d3947d-9c73-4fea-a5c3-d214c6be52e7` |

## ID Discovery Pattern

If a GUID is unknown, do a one-time name-based discovery call, extract the ID, then use ID for all subsequent calls in that session.

```
1. Call tool with name → get ID from response
2. All further calls: use ID only
```

## Related

- [[entities/team-ado-otp]] — OTP-specific ADO references
