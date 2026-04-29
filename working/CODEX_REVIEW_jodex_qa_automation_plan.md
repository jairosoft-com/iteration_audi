# Codex Adversarial Review — Jodex QA Automation Plan

**Date:** 2026-04-28
**Target:** plans/PLAN_jodex_qa_automation_board.md
**Verdict:** needs-attention

---

## Findings

### [HIGH] ADO creation flow is not idempotent
**Location:** Execution Steps (lines 382-392)

The execution path creates the Feature, six child items, and 32 tasks, then links them afterward. There is no preflight lookup, persisted ID manifest, retry/resume rule, or rollback plan. If this run is interrupted, repeated, or ADO already contains a subset of the work, it can duplicate backlog items or leave orphaned tasks assigned into the iteration.

**Recommendation:** Add a dry-run/preflight query by Feature 003/title/parent, persist every created work item ID, make the workflow resumable, and define cleanup for partially created items before executing against ADO.

---

### [HIGH] Unattended email lacks guardrails
**Location:** US4 Acceptance Criteria (lines 226-235)

The email criteria allow any valid HTML file and any valid recipient to be sent through the authenticated Outlook account. Combined with the scheduled pipeline, this implies unattended outbound email without explicit account confirmation, recipient allowlist, preview/dry-run, HTML sanitization, rate limiting, or audit requirements. A bad input or misconfigured schedule could send arbitrary HTML to unintended recipients with weak traceability.

**Recommendation:** Add acceptance criteria and tasks for recipient allowlisting, sender/account confirmation, dry-run or preview, HTML sanitization, send audit logs, and schedule-specific approval controls.

---

### [MEDIUM] Lifecycle checks omit report and email commands
**Location:** US1 Install/Uninstall Scenarios (lines 49-53)

Install and uninstall verification only checks `/qa-ai:extract`, `/qa-ai:generate`, and `/qa-ai:browser` in command completion, but later stories depend on `/qa-ai:report` and `/qa-ai:email`. The plugin could pass the lifecycle story while never registering two advertised commands.

**Recommendation:** Include `/qa-ai:report` and `/qa-ai:email` in install and uninstall completion checks, and add packaging/registration tasks that verify all plugin commands are exported.

---

## Next Steps

- Patch plan before running ADO creation
- Re-review after idempotency, email safety, and full command registration criteria are added
