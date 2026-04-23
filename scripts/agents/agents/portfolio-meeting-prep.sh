#!/bin/sh
# portfolio-meeting-prep.sh — generate today's portfolio review meeting agenda.
#
# Wraps the `portfolio-meeting-prep` shared skill (see
# .claude/skills/portfolio-meeting-prep/SKILL.md). Renders a single self-contained
# interactive HTML agenda from the latest portfolio dashboard, the latest
# per-workspace audit reports, any workspace todo lists, and the user memory
# files (for attendee identification).
#
# Required:
#   PROJECT_DIR        — absolute path to the iteration_audit repo
# Optional:
#   MEETING_DURATION   — agenda time budget; one of "30m" (default), "45m", "60m"
#   MEETING_MODEL      — claude model; default "sonnet"
#   MEETING_MAX_TURNS  — default 20 (skill reads more sources than portfolio-health:
#                        per-workspace audits + todos + memory + multiple portfolio
#                        HTMLs for trend)
#   MEETING_TIMEOUT    — default 600 (10 min ceiling; observed runtime 2–5 min)
#
# Output:
#   portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_YYYYMMDD.html
#   (skill auto-appends "_HHMM" on same-day collision, so manual re-runs by Ramon
#   before a meeting do not clobber the morning's auto-generated file)
#
# No freshness guard. The skill itself degrades gracefully on missing/stale
# inputs (skips trend chart if <3 portfolio reports exist; flags individual
# missing audits with "No recent audit"; warns if all audits >7 days old).
# A degraded agenda is harmless to leave on disk — Ramon can ignore it. This
# contrasts with portfolio-email.sh, which DOES need a freshness guard because
# its action is shared-state.
#
# Notes:
#   - sync_repo is intentionally NOT called (same OneDrive dirty-tree reason as
#     the other audit agents).
#   - Allowlist matches the skill's declared allowed-tools exactly: Read, Glob,
#     Grep, Bash, Write, Agent. No MCP servers needed.

. "$(dirname "$0")/../lib/macpilot.sh"

if [ -z "$PROJECT_DIR" ]; then
  echo "PROJECT_DIR not set" >&2
  notify "MacPilot: $AGENT_NAME" "PROJECT_DIR not set. Check .env or plist." "high"
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

DURATION="${MEETING_DURATION:-30m}"

run_agent "Use the portfolio-meeting-prep skill with duration '${DURATION}'. Execute the full workflow described in the skill: discover the most recent portfolio_report/PORTFOLIO_*.html (excluding _SUMMARY, _TREND, and _MEETING_PREP variants), read it plus the latest audit/AUDIT_*.md per ado_* and git_* workspace, plus any workspace todo/*.md files, plus memory/user_*.md for attendee identification, and render a single self-contained interactive HTML agenda to portfolio_meeting_agenda/PORTFOLIO_MEETING_AGENDA_YYYYMMDD.html (the skill will auto-append _HHMM if a file with today's date already exists). After the agenda file is written to disk, stop immediately. Do not run /portfolio-health, do not run /portfolio-email, do not run any individual project audits, do not open a browser, do not write to the wiki, do not write to any workspace folder, do not modify the source dashboard or audit files, do not send any notifications beyond the standard MacPilot one." \
  --model "${MEETING_MODEL:-sonnet}" \
  --max-turns "${MEETING_MAX_TURNS:-20}" \
  --timeout "${MEETING_TIMEOUT:-600}" \
  --allowedTools "Read Write Bash Glob Grep Agent Skill"
