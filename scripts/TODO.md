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

- [x] `agents/ado-audit-all.sh` + `plists/com.macpilot.ado-audit-all.plist` — **shipped (commit `60f4dce`); patched 2026-04-23 to add `Skill` to --allowedTools.**
  - Wraps `/ado-safe-audit all-projects`.
  - Schedule: daily 08:30. Final budget: `--max-turns 60`, `--timeout 2400s`.
- [x] `agents/git-audit-all.sh` + `plists/com.macpilot.git-audit-all.plist` — **shipped 2026-04-23 (commit `d03f6ec`).**
  - Wraps `/git_iteration_audit all-git-projects`.
  - Schedule: daily 09:00. Final budget: `--max-turns 40`, `--timeout 1200s`.
- [x] `agents/portfolio-health.sh` + `plists/com.macpilot.portfolio-health.plist` — **shipped 2026-04-23 (commit `d03f6ec`); max-turns bumped 15→25 same day after Skill-tool fix.**
  - Wraps `/portfolio-health`. Must run *after* ADO + Git audits have written their reports.
  - Time-gap chosen (09:30 daily) over a single `daily-portfolio.sh` chain runner — see [[wiki/entities/system-macpilot]] §"Production agents".

### P2 — email + lint

- [x] `agents/portfolio-email.sh` + plist — **shipped 2026-04-23 (commit `d03f6ec`); recipient allowlist hardcoded in plist (ramon, kcaumban, grace, bsinday @jairosoft.com).**
  - Wraps `/portfolio-email <allowlist>`. Schedule: daily 09:45.
  - **Gate satisfied via [[wiki/concepts/headless-skill-mode]]:** patched `.claude/skills/portfolio-email/SKILL.md` to add Step 6.5 — env-var-gated bypass of the otherwise non-negotiable confirmation. Three-var handshake (`AUTO_SEND` + `AUTHORIZED_RECIPIENTS` + `DRY_RUN`); fails closed on any mismatch.
- [x] `agents/portfolio-meeting-prep.sh` + plist — **shipped 2026-04-23 (commits `b156c15` + `de0323d`); not in the original TODO.**
  - Wraps `/portfolio-meeting-prep [duration]`. Schedule: daily 09:50. `MEETING_DURATION` env var defaults to `30m` (also accepts `45m`, `60m`).
  - No freshness guard — skill degrades gracefully on stale inputs and output is local-only.
- [ ] Consolidate `scripts/lint/` — merge the 6 Python files into one `lint.py --paths ... --fix`.
  - Expand scope to all 10 workspaces + `wiki/` + `portfolio_report/` + `portfolio_meeting_agenda/`.
  - Deliver either (a) a weekly plist, or (b) a pre-commit hook.
  - Delete dead duplicates (`comprehensive_lint.py` vs `comprehensive_linting.py`, `fix_linting.py` vs `fix_code_blocks.py`).
- [x] **Switch `lib/macpilot.sh` from `--output-format json` to `--output-format stream-json` + `--verbose`** — **SHIPPED 2026-04-23 same session.**
  - **Why:** `portfolio-meeting-prep` watchdog kill (2026-04-23 13:09) yielded empty stdout because `json` mode buffers the full response and only flushes at the end. The 3-line JSON-preservation patch from earlier in the session couldn't help on SIGTERM — by the time the lib reads the tmpfile, claude was killed before it could write anything.
  - **Implementation that landed:** swapped `--output-format json` for `--output-format stream-json --verbose` (line 236); changed the result/subtype/turns parsers from "single object/array" to "JSONL stream → filter type=='result' → tail -n 1" (lines 271, 286, 297); added explicit `WATCHDOG_KILL after ${timeout}s` label in the failure branch when exit code is 143 (line 261). All preserved-on-failure logic continues to work — now with partial events on SIGTERM kills, not empty payloads.
  - **Test result:** `scripts/agents/test.sh` 55/55 passed. End-to-end validation pending the next kickstart.

### P3 — ergonomics

- [ ] Consider a single `agents/daily-portfolio.sh` chain-runner instead of 3 time-gapped plists.
- [ ] Wire `lib/rotate-logs.sh` (30-day cleanup) if not already on a Sunday schedule.
- [ ] Ensure host Mac stays awake for scheduled times — `pmset repeat wakeorpoweron` or dedicated Mac Mini.

## Completed 2026-04-23 session — cross-cutting fixes

- [x] **`Skill` tool added to all 5 wrapper allowlists.** Discovered when launchd run hit `error_max_turns` due to silent `Skill`-tool denial → manual fallback exhaustion. See [[wiki/log.md]] entry [11:55].
- [x] **`lib/macpilot.sh` JSON preservation patch (3 lines).** Writes the claude CLI JSON response to the agent's `.log` on failure (was previously deleted by the `mktemp` cleanup trap). Made the Skill-tool-denial diagnosis possible.
- [x] **`portfolio-email` SKILL.md Step 6.5 — Headless mode.** Env-var-gated bypass of the previously non-negotiable interactive confirmation step. Recipient allowlist + auto-send flag + dry-run escape hatch. Documented as a generalizable pattern in [[wiki/concepts/headless-skill-mode]].
- [x] **OneDrive correction.** Project moved out of `~/Library/CloudStorage/OneDrive-…/`; `system-macpilot.md` `sync_repo` rationale updated; OneDrive demoted to a historical-notes parenthetical.
- [x] **`com.macpilot.example.plist` uninstalled.** Resolved the harmless 09:00 collision with `git-audit-all`.
- [x] **Wiki kept reconciled.** `entities/system-macpilot.md` rewritten with Production agents table + Conventions section; new [[wiki/concepts/headless-skill-mode]] page; index counts updated; 5 chronological log entries spanning the session.
- [x] **`portfolio-meeting-prep` model bumped sonnet→opus + timeout 600→1200s.** Cascade: (a) first run blew Sonnet 4.6's 200k context window during agenda render — `result: "Prompt is too long"`, `terminal_reason: "blocking_limit"`. (b) Switched to Opus 4.7 (1M context) — but plist edit didn't auto-apply, so the next run still used Sonnet, exhausted context again, AND yet still successfully wrote the output file before the parent agent's wrap-up ran out of room. The `_1600.html` agenda IS on disk despite the harness reporting exit 1.

## Caveats

- MacPilot default `--timeout 300s` (5 min) is too short for full portfolio audits — override per-agent.
- Upstream MIT `LICENSE` attributes Raul Riera; keep it intact if this repo is ever published.
- `config/.env` reads are blocked by the repo's pre-tool-use hook; verify that file via shell directly, not via Claude's Read tool.
- **Plist env-var changes require `launchctl bootout` + `bootstrap` to take effect.** launchd caches the EnvironmentVariables block at first load — editing the plist file alone does not propagate to subsequent kickstarts. Discovered 2026-04-23 when MEETING_MODEL=opus edit didn't reach the running service. Fix: `launchctl bootout gui/$(id -u)/com.macpilot.<name> && launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.macpilot.<name>.plist`. Verify with `launchctl print gui/$(id -u)/com.macpilot.<name> | grep <ENV>`.
