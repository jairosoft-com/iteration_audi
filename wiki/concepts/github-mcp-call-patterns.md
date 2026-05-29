---
title: "GitHub MCP Call Patterns"
type: concept
tags: [github, mcp, tooling, token, operational]
sources: []
created: 2026-05-28
updated: 2026-05-28
---

# GitHub MCP Call Patterns

Operational rules for the `github` MCP server that powers the Git-team audits ([[entities/team-git-aa-dev]], [[entities/team-git-cc-dev]]). Sibling to [[concepts/ado-mcp-call-patterns]]. Token/auth failures here are the root cause of the recurring `data_mode: partial` carry-forwards in the Git audit history.

## Server topology

- **Transport:** local **stdio binary** — `/Users/jairo/Projects/github-mcp-server/bin/github-mcp-server stdio`.
- **Defined where:** the GLOBAL/user config `~/.claude.json` → `mcpServers.github`. It is **not** in this project's `.mcp.json` (which defines only the `ado` server). The github tools are inherited from the global config.
- **Auth:** env var `GITHUB_PERSONAL_ACCESS_TOKEN`, a fine-grained PAT for GitHub user `raseniero`.
- A separate `http` github server (`https://api.githubcopilot.com/mcp`) is scoped to the `notes` project only — not used by this portfolio.

## Rule 1 — Token edits do NOT hot-reload a running server

Editing the PAT in `~/.claude.json` has **no effect on an already-running stdio server** — the process keeps the old token in its environment. To pick up a rotated token you must **reconnect via `/mcp`** (or restart the session).

**Confirmed 2026-05-28:** PAT rotated in `~/.claude.json`, but `mcp__github__*` kept returning `401` until `/mcp` reconnect. Direct `curl` with the new token succeeded the whole time — proving the file was correct and the running server was stale.

## Rule 2 — Diagnose by status code

| Code | Meaning | Scope |
|------|---------|-------|
| **401 Bad credentials** | invalid / expired / revoked token | **all** repos (auth failure) |
| **404** | repo missing OR token lacks permission on it | **per-repo** (scope gap) |

A 401 across every repo ⇒ rotate the token. A 404 on one repo ⇒ check that repo's grant.

## Rule 3 — Verify a rotated PAT independently of the server

To confirm a new token works without waiting on the MCP reconnect, read it straight from the config and curl GitHub directly (bypasses the stale server):

```bash
TOKEN=$(python3 -c "import json;print(json.load(open('$HOME/.claude.json'))['mcpServers']['github']['env']['GITHUB_PERSONAL_ACCESS_TOKEN'])")
curl -s -o /dev/null -w "%{http_code}\n" -H "Authorization: Bearer $TOKEN" https://api.github.com/user
```

`200` ⇒ token is valid; remaining MCP `401`s are purely the stale-server problem (fix with `/mcp`).

## Scoped repositories (all return 200 on the 2026-05-28 PAT)

| Team | Repos (`jairosoft-com/…`) |
|------|---------------------------|
| Auto Allies | `autoallies-version2`, `autoallies-api-core` |
| Colina Health | `colinahealth-fe`, `colinahealth-be`, `colina-health-ai-agent-code-fixing` |

## Token-expiry history

- **404 window 2026-04-21 → 2026-05-20** — scope/access issue; drove `data_mode: partial` + HCI D1–D6 carry-forward across AA and CC audits (filed as Project Exceptions in both workspace `CLAUDE.md`s). AA resolved 2026-05-20; CC `CLAUDE.md` still carried the note as of 2026-05-21.
- **401 recurrence 2026-05-28** — token expired/revoked; rotated to a new `raseniero` fine-grained PAT; access restored to all 5 repos after `/mcp` reconnect. 2nd recurrence — token expiry is a chronic operational risk for the Git audits. Tracked in [[summaries/transcript-jit-review-2026-04-23]] ("GitHub PAT fix" action).

## Related

- [[concepts/ado-mcp-call-patterns]] — ADO MCP equivalent (always use IDs)
- [[entities/team-git-aa-dev]] · [[entities/team-git-cc-dev]] — the Git teams whose audits depend on this server
- [[synthesis/github-compliance-issues]] — Git-team compliance findings built on this evidence
