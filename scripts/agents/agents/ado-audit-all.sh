#!/bin/sh
# ado-audit-all.sh — run the ADO SAFe iteration audit across all ADO workspaces.
#
# Wraps the `ado-safe-audit` shared skill (see .claude/skills/ado-safe-audit/SKILL.md).
# For target "all-projects" the skill fans out to 3 parallel agent teams (3+3+2 split
# across 8 ADO workspaces) and writes AUDIT_YYYYMMDD_HHMM.md into each workspace's
# audit/ folder. For a single workspace, it runs the single-workspace flow.
#
# Required:
#   PROJECT_DIR      — absolute path to the iteration_audit repo
# Optional:
#   AUDIT_TARGET     — "all-projects" (default) or a single workspace folder (e.g. "ado_fin")
#   AUDIT_MODEL      — claude model; default "sonnet" (use "opus" for heavier synthesis)
#   AUDIT_MAX_TURNS  — default 60 (batch fan-out needs more than the 10 default)
#   AUDIT_TIMEOUT    — default 2400 (40 min; the 300s default is far too short for a full batch)
#
# Notes:
#   - sync_repo is intentionally NOT called. Audit files are append-only new paths,
#     and the OneDrive-hosted working tree is routinely dirty from in-progress work.
#   - Tool allowlist covers file ops, shell, sub-agent orchestration, and the ADO MCP
#     server prefixes (both `mcp__ado__*` and `mcp__azure-devops__*` variants).

. "$(dirname "$0")/../lib/macpilot.sh"

if [ -z "$PROJECT_DIR" ]; then
  echo "PROJECT_DIR not set" >&2
  notify "MacPilot: $AGENT_NAME" "PROJECT_DIR not set. Check .env or plist." "high"
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

TARGET="${AUDIT_TARGET:-all-projects}"

run_agent "Use the ado-safe-audit skill with target '${TARGET}'. Execute the full workflow described in the skill. For 'all-projects' this means fanning out to 3 parallel agent teams (3+3+2 split across the 8 ADO workspaces). For a single workspace folder, run the single-workspace flow. Write each audit report to its workspace's audit/ folder using the AUDIT_YYYYMMDD_HHMM.md naming from the skill's output policy. After the audit files are written to disk, stop immediately. Do not generate a cross-team synthesis, do not run /portfolio-health, do not send email, do not open a browser, do not verify in the ADO UI." \
  --model "${AUDIT_MODEL:-sonnet}" \
  --max-turns "${AUDIT_MAX_TURNS:-60}" \
  --timeout "${AUDIT_TIMEOUT:-2400}" \
  --allowedTools "Read Write Edit Bash Glob Grep Agent TodoWrite mcp__ado mcp__azure-devops"
