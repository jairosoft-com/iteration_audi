---
title: "Headless Skill Mode"
type: concept
tags: [skills, automation, scripts, macpilot, gating]
sources: ["../../.claude/skills/portfolio-email/SKILL.md", "../../scripts/agents/agents/portfolio-email.sh"]
created: 2026-04-23
updated: 2026-04-23
---

# Headless Skill Mode

The pattern by which a Claude Code skill that ordinarily requires interactive human confirmation is made safe to invoke from an unattended scheduler (launchd, cron, CI). Introduced 2026-04-23 in `portfolio-email` Step 6.5.

## Problem

Some skills include an explicit "wait for human confirmation" step before performing a shared-state or irreversible action — e.g., sending email, posting to a chat platform, merging a PR. The mail MCP server enforces a similar protocol-level gate: *"Before sending ANY email, show FULL preview … Then ask for explicit confirmation. Never send without approval."*

A scheduled agent invoked via `claude -p "…" --no-session-persistence` cannot satisfy this gate — there is no human at the prompt. Naive scheduling either hangs until timeout or fails outright.

## Solution

Patch the skill itself (not the agent prompt, not the MCP) to add an env-var-gated bypass with **three** variables working together:

| Variable                            | Role                       | Failure mode if unset                                        |
| ----------------------------------- | -------------------------- | ------------------------------------------------------------ |
| `<SKILL>_AUTO_SEND` (or analogue)   | trigger — opt-in only      | falls back to interactive confirmation (no harm)             |
| `<SKILL>_AUTHORIZED_<TARGETS>`      | safety — allowlist         | fail-closed if `AUTO_SEND` is set but allowlist isn't        |
| `<SKILL>_DRY_RUN`                   | escape hatch — preview-only | (no failure mode; safe by design)                            |

The skill's behavior:

1. **All three unset** (default): unchanged — interactive flow with confirmation.
2. **`AUTO_SEND` only**: fail-closed; refuse to act without the safety allowlist.
3. **`AUTO_SEND` + allowlist, but a target isn't on the list**: fail-closed; print which target failed; do not perform the action even for the targets that *do* match.
4. **`AUTO_SEND` + allowlist, all targets on the list**: print the full preview to stdout (so the launchd log captures who/what/when), then perform the action.
5. **`DRY_RUN` set**: print preview, do not perform the action, regardless of `AUTO_SEND` or allowlist state.

## Why three vars and not one

A single "skip confirmation" boolean is footgun-shaped — a typo or an inherited env var would defeat the safety. Three vars create a deliberate handshake:

- The trigger (`AUTO_SEND`) is the human's act of saying *"yes, this is the unattended invocation."*
- The safety (`AUTHORIZED_<TARGETS>`) is the human's act of saying *"and only these targets are allowed."*
- The escape hatch (`DRY_RUN`) is the verification path — used during development and after every recipient-list change.

Failure is **always** closed: any mismatch, any partial setup, refuses to act. Interactive use is unaffected because all three vars default unset.

## Defense in depth

The pattern works best when both layers enforce the gate:

1. **Skill layer** — the canonical authority. Step 6.5 in the skill SKILL.md defines the contract; an interactive invocation without env vars is unaffected.
2. **Wrapper layer** — re-checks the allowlist *before* invoking the Claude CLI, so a misconfiguration fails immediately and locally without burning tokens or starting a partial conversation.

The wrapper layer's check is redundant by design — the skill is the source of truth — but the redundancy is cheap (one bash loop) and pays off on misconfiguration.

## Reference implementation

[[entities/system-macpilot]] `portfolio-email.sh` (2026-04-23) is the first instance:

- Plist sets all three trigger/safety vars: `PORTFOLIO_EMAIL_AUTO_SEND=true`, `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS=ramon,kcaumban,grace,bsinday @jairosoft.com`, `PORTFOLIO_EMAIL_RECIPIENTS=<same list>` (the actual targets, validated against the allowlist).
- The wrapper script *also* enforces the allowlist before invoking the CLI — see [[entities/system-macpilot]] §Conventions for the bash idiom.
- See `.claude/skills/portfolio-email/SKILL.md` Step 6.5 for the canonical wording.

## When NOT to apply

- The confirmation step is verifying an **LLM-derived artifact** (e.g., a generated email body where hallucinations could change meaning). An allowlist on recipients doesn't fix bad content. Keep the skill interactive and reduce the agent's autonomy on body generation instead.
- The action is **destructive** beyond a single recoverable artifact (e.g., dropping a database, force-pushing). The `DRY_RUN` escape hatch isn't strong enough — require a separate manual gate or a multi-step quorum.
- The skill is **rarely invoked**. The cost of building and maintaining the headless mode exceeds the cost of one human keystroke per invocation.

## Related

- [[entities/system-macpilot]] — host of the reference implementation
- [`.claude/skills/portfolio-email/SKILL.md`](../../.claude/skills/portfolio-email/SKILL.md) §Step 6.5 — canonical specification
