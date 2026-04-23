#!/bin/sh
# git-audit-all.sh — run the GitHub iteration audit across all git workspaces.
#
# Wraps the `git_iteration_audit` shared skill (see .claude/skills/git_iteration_audit/SKILL.md).
# For target "all-git-projects" the skill fans out to 2 parallel agents (one per
# git_* workspace: git_aa_dev, git_cc_dev) and writes AUDIT_YYYYMMDD_HHMM.md into
# each workspace's audit/ folder. For a single workspace, it runs the single-
# workspace flow.
#
# Required:
#   PROJECT_DIR      — absolute path to the iteration_audit repo
# Optional:
#   AUDIT_TARGET     — "all-git-projects" (default), or a single workspace folder
#                      (e.g. "git_cc_dev")
#   AUDIT_MODEL      — claude model; default "sonnet"
#   AUDIT_MAX_TURNS  — default 40 (smaller fan-out than the ADO batch)
#   AUDIT_TIMEOUT    — default 1200 (20 min ceiling; observed runtime ~10 min wall)
#
# Notes:
#   - sync_repo is intentionally NOT called. Audit files are append-only new paths,
#     and the OneDrive-hosted working tree is routinely dirty from in-progress work.
#   - Tool allowlist covers file ops, shell, sub-agent orchestration, GitHub MCP
#     (repo activity is the primary evidence source), and ADO MCP both prefix
#     variants (iteration + team context — the audit is hybrid GitHub + ADO SAFe).

. "$(dirname "$0")/../lib/macpilot.sh"

if [ -z "$PROJECT_DIR" ]; then
  echo "PROJECT_DIR not set" >&2
  notify "MacPilot: $AGENT_NAME" "PROJECT_DIR not set. Check .env or plist." "high"
  exit 1
fi

cd "$PROJECT_DIR" || exit 1

TARGET="${AUDIT_TARGET:-all-git-projects}"

run_agent "Use the git_iteration_audit skill with target '${TARGET}'. Execute the full workflow described in the skill. For 'all-git-projects' this means fanning out to 2 parallel agents (one per git_* workspace: git_aa_dev, git_cc_dev). For a single workspace folder, run the single-workspace flow. Write each audit report to its workspace's audit/ folder using the AUDIT_YYYYMMDD_HHMM.md naming from the skill's output policy. After the audit files are written to disk, stop immediately. Do not generate a cross-team synthesis, do not run /portfolio-health, do not send email, do not open a browser, do not verify in the ADO or GitHub UI, do not write to the wiki, do not write to portfolio_report/." \
  --model "${AUDIT_MODEL:-sonnet}" \
  --max-turns "${AUDIT_MAX_TURNS:-40}" \
  --timeout "${AUDIT_TIMEOUT:-1200}" \
  --allowedTools "Read Write Edit Bash Glob Grep Agent TodoWrite mcp__ado mcp__azure-devops mcp__github"
