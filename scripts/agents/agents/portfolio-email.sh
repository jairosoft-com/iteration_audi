#!/bin/sh
# portfolio-email.sh — send today's portfolio health dashboard to the authorized recipients.
#
# Wraps the `portfolio-email` shared skill (see .claude/skills/portfolio-email/SKILL.md).
# Runs in the skill's headless mode (Step 6.5) so launchd can fire it unattended:
# the skill validates every recipient against PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS
# and refuses to send if the lists don't match.
#
# Required:
#   PROJECT_DIR                           — absolute path to the iteration_audit repo
#   PORTFOLIO_EMAIL_RECIPIENTS            — comma-separated send targets (passed to the skill)
#   PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS — comma-separated allowlist (skill validates;
#                                            this script ALSO pre-checks to fail fast)
# Optional:
#   PORTFOLIO_EMAIL_AUTO_SEND  — default "true" in plist; setting "false" reverts the skill
#                                to interactive (which will hang in headless launchd context).
#   PORTFOLIO_EMAIL_DRY_RUN    — set to "true" to preview-only (no Graph API call). Use for
#                                verification.
#   EMAIL_MODEL                — claude model; default "sonnet"
#   EMAIL_MAX_TURNS            — default 20
#   EMAIL_TIMEOUT              — default 300 (5 min ceiling; observed runtime ~1 min)
#
# Pre-flight guards (run BEFORE invoking the CLI to save tokens):
#   1. Required env vars must be set.
#   2. Every PORTFOLIO_EMAIL_RECIPIENTS entry must appear in
#      PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS (the skill repeats this check;
#      we duplicate to fail fast and log locally).
#   3. Today's portfolio_report/PORTFOLIO_<YYYYMMDD>_*.html must exist; otherwise
#      portfolio-health didn't run successfully and we MUST NOT email a stale
#      dashboard. Notify and exit 0 cleanly.
#
# Notes:
#   - sync_repo is intentionally NOT called (same OneDrive dirty-tree reason as the
#     other audit agents).
#   - Tool allowlist is the tight set the skill actually uses: file ops + Bash +
#     ToolSearch + the two specific mail MCP tools (list_all_accounts and
#     graph_send_message). No SMTP, no IMAP, no browser, no other MCPs.

. "$(dirname "$0")/../lib/macpilot.sh"

if [ -z "$PROJECT_DIR" ]; then
  echo "PROJECT_DIR not set" >&2
  notify "MacPilot: $AGENT_NAME" "PROJECT_DIR not set. Check .env or plist." "high"
  exit 1
fi

if [ -z "$PORTFOLIO_EMAIL_RECIPIENTS" ]; then
  echo "PORTFOLIO_EMAIL_RECIPIENTS not set" >&2
  notify "MacPilot: $AGENT_NAME" "PORTFOLIO_EMAIL_RECIPIENTS not set. Check plist." "high"
  exit 1
fi

if [ -z "$PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS" ] && [ "$PORTFOLIO_EMAIL_DRY_RUN" != "true" ]; then
  echo "PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS not set (and not in dry-run)" >&2
  notify "MacPilot: $AGENT_NAME" "Recipient allowlist missing. Check plist." "high"
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

# Pre-flight guard #2: every send target must be on the allowlist (case-insensitive,
# whitespace-trimmed). Skipped in dry-run since dry-run never actually sends.
if [ "$PORTFOLIO_EMAIL_DRY_RUN" != "true" ]; then
  ALLOW=$(printf "%s" "$PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
  for r in $(printf "%s" "$PORTFOLIO_EMAIL_RECIPIENTS" | tr ',' ' '); do
    norm=$(printf "%s" "$r" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
    [ -z "$norm" ] && continue
    case ",$ALLOW," in
      *",$norm,"*) ;;
      *)
        echo "Recipient '$r' not in PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS — fail-closed" >&2
        notify "MacPilot: $AGENT_NAME" "Recipient '$r' not on allowlist. Send aborted." "high"
        exit 1
        ;;
    esac
  done
fi

# Pre-flight guard #3: today's PORTFOLIO_*.html must exist. If portfolio-health
# didn't run (or failed), exit cleanly without emailing a stale dashboard.
TODAY=$(date +%Y%m%d)
if ! ls portfolio_report/PORTFOLIO_${TODAY}_*.html >/dev/null 2>&1; then
  echo "No portfolio_report/PORTFOLIO_${TODAY}_*.html found — portfolio-health did not produce a dashboard today" >&2
  notify "MacPilot: $AGENT_NAME" "No dashboard for today. Skipping email." "default"
  exit 0
fi

run_agent "Use the portfolio-email skill with recipients '${PORTFOLIO_EMAIL_RECIPIENTS}'. Run in headless mode per Step 6.5 of the skill: env vars PORTFOLIO_EMAIL_AUTO_SEND and PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS are set, so skip Step 7's interactive confirmation but still print the full preview (To, Subject, Body summary, Attachment) to stdout for the log. Find today's PORTFOLIO_*.html in portfolio_report/ (the most recent file matching PORTFOLIO_${TODAY}_*.html) and use it as both the dashboard source and the email attachment. After the send completes (or is skipped per PORTFOLIO_EMAIL_DRY_RUN), stop immediately. Do not run /portfolio-health, do not run /portfolio-meeting-prep, do not open a browser, do not write to the wiki, do not write to any workspace folder, do not send any extra emails beyond the one to the configured recipients." \
  --model "${EMAIL_MODEL:-sonnet}" \
  --max-turns "${EMAIL_MAX_TURNS:-20}" \
  --timeout "${EMAIL_TIMEOUT:-300}" \
  --allowedTools "Read Bash Glob Grep ToolSearch mcp__mail__list_all_accounts mcp__mail__graph_send_message"
