# Wiki TODO

Persistent cross-session to-do list for items surfaced in conversations — things we identified but deferred, decisions captured but not yet executed, wiki bookkeeping that's worth doing but not urgent. Agent appends items as they're identified; closes them (moving to the archive) when completed.

**Format per item:** status checkbox · date-added · category tag · one-line description · (links to source context if applicable).

**Conventions:**
- `[ ]` open · `[x]` closed · `[~]` in progress / partially done
- `⏳` waiting on external action (not the agent's to execute)
- When closing an item, move to the Archive at the bottom and add a `closed: YYYY-MM-DD` note with the outcome.
- Re-open only if the original item was closed prematurely.
- This file is wiki-maintained. Source of truth. Agent updates it; human curates priorities.

---

## Open — external / waiting on others (⏳)

- [ ] ⏳ **2026-04-23 · karl-action** · Share hiring-risk register with Grace + capture mitigation meeting minutes. Source: transcript.
- [ ] ⏳ **2026-04-23 · karl-action** · Execute Admin 12 SP de-scope in ADO (Ramon authorized in meeting — move 3–4 items to 7.3 backlog, e.g., #202937 Solar quotation, #202945 Grass cutting, #202939 Professional fee). Source: transcript + [[summaries/audit-ado-admin-20260423-0113]]
- [ ] ⏳ **2026-04-23 · program-action** · Claude partner workflow → epic migration (structural ADO change, owner TBD). Source: transcript.
- [ ] ⏳ **2026-04-23 · mark-action** · DoR remediation on #202898 + #202909 — deadline missed Day 3. Source: [[summaries/audit-ado-admin-20260423-0113]]
- [ ] ⏳ **2026-04-23 · pcoronia-action** · BE#55 HIPAA rework — 10 CHANGES_REQUESTED findings (5 Critical HIPAA). **Day 11+ still CHANGES_REQUESTED** — 8 SP blocked with 5 days left in sprint. Source: [[summaries/audit-git-cc-dev-20260423-0856]], [[summaries/audit-git-cc-dev-20260427-0902]]
- [ ] ⏳ **2026-04-23 · ike-action** · Dispose #187240 (248 days stale, 12 audits). Source: [[summaries/audit-ado-ls-dev-20260423-0900]]
- [ ] ⏳ **2026-04-26 · ike-action** · Activate #195727 ASAP — **BR trap race condition**: if Samantha closes #203239 first, untouched ratio crosses 33.3% → BR collapses 24.3→4.3 → LS Dev overall ~57 (High Risk). Source: [[summaries/audit-ado-ls-dev-20260426-2205]].
- [ ] ⏳ **2026-04-27 · ike-samantha-action** · LS Dev WIB collapse — **Day 2 High Risk (47.9, −2.8 continued decline, reactive-only sprint)**. No User Stories in sprint, 0 SP closed. Recovery path: add ≥1 User Story (restores −40 WIB penalty), estimate #203247 Spike SP, close #203239 Defect → lifts to ~63+ Moderate. Ike must activate #195727 FIRST to avoid BR trap (see prior item). Source: [[summaries/audit-ado-ls-dev-20260427-1110]], Day 9 audit 2026-04-28
- [ ] ⏳ **2026-04-27 · pcoronia-action** · BE#55 HIPAA rework Day 11+ still CHANGES_REQUESTED — 8 SP blocked with 5 days left in sprint. Source: [[summaries/audit-git-cc-dev-20260427-0902]]
- [ ] ⏳ **2026-04-23 · cliff-earl-action** · Configure branch protection on develop/dev/main both AA repos — single action from HCI Moderate (+3 to +4). Source: [[summaries/audit-git-aa-dev-20260423-0855]]
- [ ] ⏳ **2026-04-23 · almera-action** · De-scope HR 7.2 to ≤22 SP (currently 38 SP, 73% overbook). P0 unactioned 4 audits. Source: [[summaries/audit-ado-hr-20260423-0914]]
- [ ] ⏳ **2026-04-23 · luke-action** · Add ≥1 User Story to Flawless 7.2 sprint (structural WIB 30 ceiling — 4 audits). Source: [[summaries/audit-ado-fl-dev-20260423-0910]]
- [ ] **2026-04-28 · milestone** · Shared Services reached Low Risk (84.6) — Day 9 milestone, first ever. Monitor for sustainability. Source: Day 9 audit 2026-04-28, [[synthesis/team-rankings]]
- [ ] **2026-04-28 · jit-watch** · JIT DP reset to 0.0 (Audit #44) — formula change exposed structural gap; 9 closed items exited visible board. Watch Day 10 for recovery or continued decline. Source: Day 9 audit 2026-04-28, [[entities/team-ado-jit]]

## Open — wiki bookkeeping (agent-executable)

- [ ] **2026-04-23 · synthesis** · Create `synthesis/dor-form-vs-content.md` — "DoR passes but content is wrong" pattern now surfaced in 3 workspaces (Shared #202687 empty, Flawless #202827 1-char-short, HR #203057+#203063 wrong-candidate copy-paste). Rubric measures character counts, not accuracy. Worth a dedicated synthesis page. Trigger: wait until a 4th instance or when pattern directly affects a scoring dispute.
- [ ] **2026-04-23 · convention** · Formalize in `wiki/CLAUDE.md` schema: *"Wiki may propagate meeting-documented decisions to source CLAUDE.md Project Exceptions, additively, with source citation and log entry."* First precedent set this session (AA + Colina non-dev exceptions). Not in schema yet.
- [ ] **2026-04-23 · bookkeeping** · Spot-check the ~25 4/22 same-day re-run audits for distinct signal (most expected flat holds or degraded-mode; skip if no change). Low priority.
- [ ] **2026-04-23 · bookkeeping** · Spot-check the ~7 4/23 afternoon re-run audits (_1100, _1254, _1505, _1510, _1515) for distinct signal. The 4/23 1535 portfolio dashboard indicates some of these moved (LS-Dev 41.0 → 39.7, Shared 35.3 → 41.1, OTP 63.3 → 65.2, JIT 75.5 → 73.2); ingesting these would surface the real Day-4 closing state.
- [ ] **2026-04-23 · bookkeeping** · Verify whether `PORTFOLIO_MEETING_AGENDA_20260423.html` (non-timestamped) is distinct from the ingested `_1600` version. Skip if duplicate; ingest if distinct.
- [ ] **2026-04-23 · bookkeeping** · JIT transcript cut off at 46:24 with Ramon pivoting to "let me just jump to the JIT program" — the JIT program discussion content was not captured. If a continuation transcript exists or if a follow-up meeting transcript arrives, ingest and link.
- [ ] **2026-04-24 · bookkeeping** · Investigate silent-stdout regression on batch-audit agents. `ado-audit-all` 2026-04-22 + 2026-04-23 runs emitted a full YAML batch summary to stdout (~70 lines each); the 2026-04-24 08:30 run logged only `OK (turns: 1/60)` followed by an empty ``` fence, and `.out` was not appended. `git-audit-all` followed the same pattern: `OK (turns: 5/40)` + empty fence. AUDIT_20260424_*.md files *were* written (visible in git status), so the work happened — but the customary summary is gone and `turns: 1/60` for an 8-workspace batch is implausible (suggests the turn counter or stream-json emit path changed). Diagnose before 2026-04-25 08:30 — overnight scan-ability of agent output is broken until fixed. Source: `scripts/agents/logs/ado-audit-all.log` lines 155-158, `git-audit-all.log` lines 50-53.

## Open — context / settings optimization (from context-audit 2026-04-26)

- [x] **2026-04-26 · P1 · settings** · Add `"autocompact_percentage_override": 75` to `~/.claude/settings.json`. Missing setting causes premature compaction during heavy batch audit sessions. Agent-executable, safe, reversible. Source: context-audit 2026-04-26. `closed: 2026-04-26` — applied directly to `~/.claude/settings.json`.
- [x] **2026-04-26 · P1 · settings** · Add `"BASH_MAX_OUTPUT_LENGTH": "150000"` to the `env` block in `~/.claude/settings.json`. Default (~30–50k chars) truncates long ADO/GitHub API responses during audit runs. Agent-executable, safe, reversible. Source: context-audit 2026-04-26. `closed: 2026-04-26` — applied directly to `~/.claude/settings.json`.
- [ ] ⏳ **2026-04-26 · ramon-action · mcp** · Locate and remove the duplicate `"ado"` MCP server registration. Both `mcp__ado__*` and `mcp__azure-devops__*` tool prefixes appear in the deferred tool list; all allow rules in `settings.local.json` use `mcp__azure-devops__*`, so the `ado` registration is stale. Find the config file that defines it (check `~/.claude/` and project `.claude/` for mcpServers entries named "ado") and remove it. Source: context-audit 2026-04-26.
- [ ] **2026-04-26 · P2 · skills** · Fix skill name inconsistency in `git_iteration_audit/SKILL.md`: frontmatter says `name: git-iteration-audit` (hyphen) but the folder, CLAUDE.md invocation, and `/context` display all use `git_iteration_audit` (underscore). Align frontmatter to `git_iteration_audit`. Agent-executable. Source: context-audit 2026-04-26.
- [ ] **2026-04-26 · P3 · skills** · Extract duplicated color/hex reference tables from `portfolio-health`, `portfolio-email`, and `portfolio-meeting-prep` skills (~15 lines each, identical content) into a shared reference file (e.g. `.claude/skills/PORTFOLIO_COLORS.md`) and replace with a single-line pointer in each skill. Saves ~30 lines of redundant context on every portfolio run. Agent-executable. Source: context-audit 2026-04-26.

## Open — scripts/agents/ tooling (from earlier wiki log)

- [ ] **earlier · P0** · Localize `CLAUDE.md` in `scripts/agents/` (upstream Raul Riera doc still in place — superficial cleanup).
- [ ] ⏳ **earlier · P0** · Verify `config/.env` — Ramon's manual check, hook-blocked from tool reads.
- [ ] **earlier · P2** · Lint consolidation: add parsing rule in lint.py — "if prompt contains 'Use the X skill', allowlist must contain `Skill`." Would have caught the 2026-04-23 launchd Skill-tool-missing defect earlier.
- [ ] **earlier · P3** · `daily-portfolio.sh`, `rotate-logs`, `pmset` ergonomics (3 items).
- [ ] **earlier · P2** · MacPilot: P1 + portfolio-email + portfolio-meeting-prep TODO checkboxes (most items shipped this session but boxes still open).
- [ ] **2026-04-24 · P0** · `portfolio-email` watchdog-killed at 300s (exit 143) on 2026-04-24 09:45–09:50 — `PORTFOLIO_20260424_0935.html` was generated but never distributed. Cause TBD (Graph send stall? MCP stall? hook-startup cost?); yesterday's 12:36 retry succeeded in 9 turns. Actions: (a) re-send today's dashboard manually, (b) diagnose stall (mail MCP responsiveness, Graph auth token freshness), (c) consider raising the plist timeout or splitting preview/send into two stages. Source: `scripts/agents/logs/portfolio-email.log` (2026-04-24 entries).
- [ ] **2026-04-24 · P1 (was P2)** · `portfolio-health` stale loaded plist: repo plist = `AUDIT_MAX_TURNS 25`, loaded plist at `~/Library/LaunchAgents/` = `15`. 2026-04-23 bump committed but `install.sh` never re-run, so launchd is still executing the pre-fix plist. Confirmed root cause 2026-04-24 via `launchctl print` returning `15`. Execute as a checklist:
    1. **Safety diff first** (catch any intentional local overrides before `install.sh` clobbers them): `for p in ~/Library/LaunchAgents/com.macpilot.*.plist; do diff "$p" "scripts/agents/plists/$(basename "$p")"; done` — review each diff; non-zero only expected on `portfolio-health` (the 15 vs 25 delta). If any other plist differs, triage before proceeding.
    2. **Fix:** `cd scripts/agents && ./install.sh` — propagates all repo plists into `~/Library/LaunchAgents/` and `launchctl bootstrap`s them. *(Alternative for a single-service fix: `launchctl bootout gui/$(id -u)/com.macpilot.portfolio-health && cp scripts/agents/plists/com.macpilot.portfolio-health.plist ~/Library/LaunchAgents/ && launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.macpilot.portfolio-health.plist` — keeps blast radius to one service.)*
    3. **Verify:** `launchctl print gui/$(id -u)/com.macpilot.portfolio-health | grep -i max` → should return `25` (currently `15`).
    4. **Next-fire confirmation:** after tomorrow's 09:30 fire, check `scripts/agents/logs/portfolio-health.log` for `turns: N/25` (not `N/15`) — the cap value in the display should move.

    Source: [[entities/system-macpilot]] §Caveats (the ⚠️ blockquote on the Skill-allowlist convention).

- [ ] **2026-04-24 · P2** · Disambiguate `--max-turns` behavior: stream-json log shows `turns: 32/15` completing OK, which shouldn't happen if 15 is a hard parent-only cap. Run a diagnostic kickstart and observe halt vs completion:
    1. **Temporarily force a low cap** — edit the loaded plist override directly so the fix doesn't persist beyond the experiment: `launchctl bootout gui/$(id -u)/com.macpilot.portfolio-health` · `/usr/libexec/PlistBuddy -c "Set :EnvironmentVariables:AUDIT_MAX_TURNS 3" ~/Library/LaunchAgents/com.macpilot.portfolio-health.plist` · `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.macpilot.portfolio-health.plist`.
    2. **Kickstart:** `launchctl kickstart -k gui/$(id -u)/com.macpilot.portfolio-health`.
    3. **Read result** from `scripts/agents/logs/portfolio-health.log`:
       - If `FAILED (exit 1)` with `error_max_turns` at `num_turns: 4` → `--max-turns` is a hard parent-only cap; today's 32/15 readings mean `num_turns` in the display rolls up sub-agent turns and the caps are fine. Resolution: update the log display format, not the caps.
       - If `OK (turns: N/3)` with N > 3 → `--max-turns` is advisory on success paths; the caps are genuinely drifting. Resolution: tighten skill prompts (not raise caps).
    4. **Restore:** re-run the P1 remediation above to put the plist back at 25 — *must execute after this P2 regardless of outcome, or next scheduled fire runs against cap 3.*

    Decides whether `portfolio-meeting-prep` (33/20) has an actual drift problem or a display artifact — same root cause, same resolution path. Source: [[entities/system-macpilot]] §Caveats ("Budget drift — under investigation").
- [ ] **2026-04-24 · P3** · `SessionStart` hook registered in agent settings references `.claude/hooks/session_start.py`, which is missing on disk (ENOENT on every agent run). Persistent since ≥2026-04-22 — `ado-audit-all.log` 2026-04-22 23:48 shows the same ENOENT against a `SessionEnd` hook (`session-lifecycle-hook.mjs`), so the broader pattern is a hook-path drift, not a single missing file. Non-fatal — stream-json logs the `hook_response` as exit 2 and continues — but it's noise and future-debugging-hostile. Either create the hooks or remove the registrations from `settings.json` / `settings.local.json`. Source: `scripts/agents/logs/portfolio-email.log` (hook_response events), `scripts/agents/logs/ado-audit-all.log` line 5.

---

## Archive — closed items

*(Move items here with `[x]` + `closed: YYYY-MM-DD` + one-line outcome. Keep chronological, newest first.)*

- [x] **2026-04-23 · grace-action** · DoR remediation on #202911, #202913. `closed: 2026-04-26` — Grace remediated #202911 (DoR complete) and #202913 (DoR+SP fixed) at ~23:15–23:29 PHT Apr 26; OTP A39 score 74.8 (+6.1, largest 7.2 single-session gain). Source: [[summaries/audit-ado-otp-20260426-2210]].
- [x] **2026-04-23 · ramon-action** · Fix `raseniero` GitHub token access-scope. `closed: 2026-04-24` — confirmed restored on Day 5 audit; all 3 Colina repos + both AA repos return live GitHub data; HCI dims 1–6 now scored on live evidence for first time in 4 days (Colina HCI 78 → 82 on evidence-quality alone). Source: [[summaries/audit-git-aa-dev-20260424-0902]], [[summaries/audit-git-cc-dev-20260424-0902]].
- [x] **2026-04-23 · team-action** · LS-Dev configure capacity for 7.2. `closed: 2026-04-24` — Samantha (1h/day Dev), Luzmibel (1h/day Test), Ike (1h/day Dev) all configured overnight; TC 0.0 → 100.0; Overall +14.3 → contributed to the +21.4 single-session gain. Source: [[summaries/audit-ado-ls-dev-20260424-0834]].
- [x] **2026-04-23 · carol-ramon-action** · Configure Shared Services capacity for 7.2. `closed: 2026-04-24` — Teofilo (6h/day Dev), Jaszmeine (3h/day Design), Vicsante (6h/day Dev) configured overnight; ends 5-audit zero-streak; TC 0.0 → 100.0; Overall +14.3 → contributed to +15.0 single-session gain. Source: [[summaries/audit-ado-shared-20260424-0835]].
- [x] **2026-04-23 · synthesis** · Annotate `synthesis/team-rankings.md` re AA + Colina HCI token-side cap. `closed: 2026-04-24` — superseded by token fix above; rather than annotate the cap, the 2026-04-24 update section on team-rankings now documents the current live rankings with notes on AA masking pattern persistence and Colina HCI recovery.
- [x] **2026-04-23 · synthesis** · Update `synthesis/portfolio-trend.md` past 4/19. `closed: 2026-04-24` — timeline extended through 2026-04-24 Day 5; added "PI7.2 window" analysis section documenting the reset dip and Day-5 recovery; also flagged the audit-to-action feedback-loop candidate pattern.
