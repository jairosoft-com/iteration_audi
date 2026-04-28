# Context Audit — iteration_audit project (2026-04-28)

## Context Breakdown (from /context)

| Category | Tokens | % |
|---|---|---|
| System prompt | 6.7k | 3.4% |
| System tools | 8.7k | 4.4% |
| Custom agents | 56 | 0.0% |
| Memory files | 2k | 1.0% |
| Skills | 1.6k | 0.8% |
| Messages | 51.6k | 25.8% |
| **Total used** | **70.2k** | **35%** |
| Free space | 96.2k | 48.1% |
| Autocompact buffer | 33k | 16.5% |

Overall context health: **healthy for this session**. The 51.6k messages cost is expected (long wiki-ingest session today). Structural settings are well-configured.

---

## Score: 71/100 — NEEDS WORK

---

## Issues Found

### [INFO] Stale + redundant allow-list entries in settings.local.json

The allow list has accumulated one-off entries that are now dead weight:

| Entry | Problem |
|---|---|
| `Bash(kill 56493)` | Hardcoded PID — process is long dead. Bandaid. |
| `Bash(open "/Users/jairo/Library/CloudStorage/.../PORTFOLIO_TREND_20260331.html")` | Hardcoded path to March 2026 file. Stale. |
| `Bash(python3 -c "import sys,json; d=json.load...")` (×2) | Redundant — `Bash(python3:*)` is already allowed. Covers these. |
| `mcp__stitch__create_project` / `mcp__stitch__list_projects` | Stitch not listed in CLAUDE.md as active MCP server. Likely stale. |

**Fix:** Remove 5 stale entries from `settings.local.json` allow list.

### [WARNING] 5 skills exceed 200 lines

Skills are lazy-loaded (confirmed: only 1.6k tokens total in /context). No idle token cost. But line bloat still risks quality degradation when active — verbose instructions dilute signal.

| Skill | Lines | Flag |
|---|---|---|
| ado-safe-audit | 327 | −5 |
| git_iteration_audit | 300 | −5 |
| portfolio-meeting-prep | 289 | −5 |
| portfolio-health | 266 | −5 |
| portfolio-email | 207 | −5 |

**Mitigation:** Lazy-load means zero idle cost. Deduction applied per rubric but real impact is low.
**Fix:** Run `/caveman:compress` on each skill to strip filler while preserving all technical rules.

### [INFO] MCP servers — 3 active (azure-devops, github, mail)

Per /context: MCP tools are deferred (loaded on-demand). **Zero idle token cost.** Standard rubric deduction applies (−3 each = −9) but actual overhead is 0 when not in use.

**No fix needed** — on-demand loading is optimal.

### [INFO] CLAUDE.md — 1 minor redundancy

Line: `"The user prefers YAML-structured responses (configured in settings.local.json)"`
`outputStyle` is already set in `settings.local.json` AND enforced via system prompt. Redundant.

**Fix:** Remove 2 lines from CLAUDE.md Output Style section.

### [✅ PASS] autocompact_percentage_override

Set to 75 in `~/.claude/settings.json`. Correct.

### [✅ PASS] BASH_MAX_OUTPUT_LENGTH

Set to 150000 in `~/.claude/settings.json`. Correct.

### [✅ PASS] CLAUDE.md size

105 lines. Well under 200 limit. No progressive disclosure needed.

### [✅ PASS] Bloat directories

No `node_modules`, `dist`, `__pycache__`, `.venv` exist. No deny rules needed.

---

## Score Breakdown

| Issue | Deduction |
|---|---|
| 5 skills >200 lines | −25 |
| 3 MCP servers (deferred — mitigated) | −9 |
| CLAUDE.md redundancy (<5 rules flagged) | −0 |
| All settings correct | +0 |
| No bloat dirs | +0 |
| **Score** | **71/100** |

---

## Top 3 Fixes (ordered by impact)

1. **Compress 5 skills** — run `/caveman:compress` on each. Reduces active-session overhead when skills fire.
2. **Clean stale allow entries** — remove 5 dead entries from `settings.local.json`. Low risk, immediate cleanup.
3. **Remove CLAUDE.md redundancy** — delete 2 lines from Output Style section. Trivial.

---

## Execution Plan (if approved)

**Safe to auto-apply:**
- Remove 5 stale allow-list entries from `settings.local.json`
- Remove 2 redundant lines from `CLAUDE.md`

**Show diff first (user confirms):**
- Compress ado-safe-audit, git_iteration_audit, portfolio-meeting-prep, portfolio-health, portfolio-email skills via `/caveman:compress`
