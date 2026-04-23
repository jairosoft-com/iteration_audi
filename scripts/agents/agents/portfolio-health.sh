#!/bin/sh
# portfolio-health.sh — generate the portfolio health dashboard from today's audits.
#
# Wraps the `portfolio-health` shared skill (see .claude/skills/portfolio-health/SKILL.md).
# Reads the latest AUDIT_*.md per workspace from each ado_* and git_* directory,
# extracts scores, and writes a single self-contained HTML dashboard to
# portfolio_report/PORTFOLIO_YYYYMMDD_HHMM.html.
#
# Required:
#   PROJECT_DIR      — absolute path to the iteration_audit repo
# Optional:
#   AUDIT_MODEL      — claude model; default "sonnet"
#   AUDIT_MAX_TURNS  — default 15 (skill is tight: read ~10 audits, render 1 HTML)
#   AUDIT_TIMEOUT    — default 600 (10 min ceiling; observed runtime <3 min)
#
# Ordering:
#   This agent expects today's per-workspace audits to already exist on disk —
#   schedule it AFTER ado-audit-all and git-audit-all complete. The skill
#   degrades (it does not fail) on stale per-workspace audits: a workspace whose
#   latest audit is from a prior date is included in the dashboard with the
#   stale date marker, so a missed upstream run yields a flagged dashboard
#   rather than an aborted one.
#
# Notes:
#   - sync_repo is intentionally NOT called (same OneDrive dirty-tree reason as
#     the audit agents).
#   - Allowlist matches the skill's declared allowed-tools exactly: Read, Glob,
#     Grep, Bash, Write. No Edit, no Agent, no MCP servers needed — the skill
#     only reads local files and writes one HTML file.

. "$(dirname "$0")/../lib/macpilot.sh"

if [ -z "$PROJECT_DIR" ]; then
  echo "PROJECT_DIR not set" >&2
  notify "MacPilot: $AGENT_NAME" "PROJECT_DIR not set. Check .env or plist." "high"
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

run_agent "Use the portfolio-health skill. Execute the full workflow described in the skill: discover all ado_* and git_* workspaces, read each workspace's most recent audit/AUDIT_*.md, extract the scoring fields per the skill's regex rules, and render one self-contained HTML dashboard to portfolio_report/PORTFOLIO_YYYYMMDD_HHMM.html using the current local date and time. After the dashboard file is written to disk, stop immediately. Do not run /portfolio-email, do not run /portfolio-meeting-prep, do not open a browser, do not write to the wiki, do not write to any workspace folder, do not send any extra notifications, do not re-compute individual audit scores." \
  --model "${AUDIT_MODEL:-sonnet}" \
  --max-turns "${AUDIT_MAX_TURNS:-15}" \
  --timeout "${AUDIT_TIMEOUT:-600}" \
  --allowedTools "Read Write Bash Glob Grep"
