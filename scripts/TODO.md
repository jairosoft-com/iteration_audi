# scripts/ TODO

Automation roadmap for the iteration-audit portfolio. Owner: Ramon.
See [[wiki/entities/system-macpilot]] for context.

## Next step

- [x] **Decide git-tracking for `scripts/agents/`** — **RESOLVED 2026-04-23 as Option A (vendor as subtree).** Whole `scripts/` tree committed across 3 commits: `60f4dce` (initial bulk add), `a4708d6` (portfolio-email follow-up), `b156c15` (portfolio-meeting-prep follow-up). 28 files tracked; `.claude/data/sessions/*.json` correctly excluded by root `.gitignore`'s `**/.claude/data/sessions/` rule; `scripts/agents/.gitignore` preserved inside the subtree.

## Roadmap (priority order)

### P0 — prerequisites

- [x] Decide git tracking (see above) — **resolved 2026-04-23 as Option A (subtree).**
- [ ] Localize `scripts/agents/CLAUDE.md` — strip upstream Xcode/BugSnag/digest examples; document the 4 target agents and this repo's `PROJECT_DIR`.
- [ ] Verify `scripts/agents/config/.env` holds `PROJECT_DIR=/Users/jairo/.../iteration_audit` and a valid `NTFY_TOPIC`. (File is hook-blocked from tool reads — check manually.)

### P1 — core audit agents

- [ ] `agents/ado-audit-all.sh` + `plists/com.macpilot.ado-audit-all.plist`
  - Wraps `/ado-safe-audit all-projects`.
  - Suggested schedule: daily 08:30 (before 09:00 standup).
  - Budget: `--max-turns 40+`, `--timeout 1800+` (batch audit is 3×3-agent fan-out).
- [ ] `agents/git-audit-all.sh` + `plists/com.macpilot.git-audit-all.plist`
  - Wraps `/git_iteration_audit all-git-projects`.
  - Budget: `--max-turns 20`, `--timeout 600`.
- [ ] `agents/portfolio-health.sh` + `plists/com.macpilot.portfolio-health.plist`
  - Wraps `/portfolio-health`. Must run *after* ADO + Git audits have written their reports.
  - launchd has no DAG — either time-gap (e.g. 09:15) or chain all three inside a single `daily-portfolio.sh` (simpler failure reasoning).

### P2 — email + lint

- [ ] `agents/portfolio-email.sh` + plist — wraps `/portfolio-email <recipient>`.
  - **Gate:** do not schedule until Ramon explicitly authorizes the recipient list in `.env` or the plist. Email dispatch is a shared-state action; should not auto-fire without that authorization per project guardrails.
- [ ] Consolidate `scripts/lint/` — merge the 6 Python files into one `lint.py --paths ... --fix`.
  - Expand scope to all 10 workspaces + `wiki/` + `portfolio_report/` + `portfolio_meeting_agenda/`.
  - Deliver either (a) a weekly plist, or (b) a pre-commit hook.
  - Delete dead duplicates (`comprehensive_lint.py` vs `comprehensive_linting.py`, `fix_linting.py` vs `fix_code_blocks.py`).

### P3 — ergonomics

- [ ] Consider a single `agents/daily-portfolio.sh` chain-runner instead of 3 time-gapped plists.
- [ ] Wire `lib/rotate-logs.sh` (30-day cleanup) if not already on a Sunday schedule.
- [ ] Ensure host Mac stays awake for scheduled times — `pmset repeat wakeorpoweron` or dedicated Mac Mini.

## Caveats

- MacPilot default `--timeout 300s` (5 min) is too short for full portfolio audits — override per-agent.
- Upstream MIT `LICENSE` attributes Raul Riera; keep it intact if this repo is ever published.
- `config/.env` reads are blocked by the repo's pre-tool-use hook; verify that file via shell directly, not via Claude's Read tool.
