---
name: portfolio-email
description: Send the latest portfolio health dashboard as an email-safe HTML summary to specified recipients via Graph API.
argument-hint: [recipient-email or name] or [multiple emails comma-separated]
allowed-tools: Read, Glob, Grep, Bash, ToolSearch, mcp__mail__list_all_accounts, mcp__mail__graph_send_message
---

<!-- markdownlint-disable MD013 -->

# Portfolio Email Skill

Send the latest portfolio health dashboard as an email-safe inline HTML email to one or more recipients. The email body contains a fully styled, table-based HTML rendition of the dashboard that renders correctly in all major email clients (Outlook, Gmail, Apple Mail).

Do not use this skill for:

- Generating or re-computing portfolio dashboards (use `portfolio-health`)
- Running individual project audits (use `ado-safe-audit` or `git_iteration_audit`)
- Sending emails unrelated to portfolio dashboards

## Authority and precedence

This skill is the authoritative source for:

- Email-safe HTML conversion of the portfolio dashboard
- Email composition, recipient handling, and send workflow
- Inline style conventions for email compatibility

This skill defers to:

- `portfolio-health` SKILL.md for dashboard generation and scoring methodology
- Memory files for recipient contact information (check `memory/user_*.md` files)
- `mcp__mail__list_all_accounts` for determining the correct send method

## Accepted inputs

### Single recipient

```text
/portfolio-email kcaumban@jairosoft.com
/portfolio-email Karl
```

### Multiple recipients

```text
/portfolio-email kcaumban@jairosoft.com, another@example.com
/portfolio-email Karl, Ramon
```

### Recipient resolution

1. If input is an email address, use it directly
2. If input is a name, search memory files (`memory/user_*.md`) for a matching contact and extract their email
3. If no match found, ask the user for the email address before proceeding
4. **Never guess or fabricate email addresses**

## Required workflow

### Step 1 — Identify recipients

Parse the argument to extract recipient email(s). Resolve names to emails via memory files. Confirm recipients with the user if ambiguous.

### Step 2 — Find the latest portfolio dashboard

```text
Glob pattern: portfolio_report/PORTFOLIO_*.html
```

Select the most recent file by filename timestamp (files are named `PORTFOLIO_YYYYMMDD_HHMM.html`). Exclude `_SUMMARY.html` and `_TREND` files — use the main dashboard only.

### Step 3 — Read the dashboard HTML

Read the full HTML file to extract all data needed for the email body:

- Header metrics (Portfolio Mean, Median, Teams at Risk)
- Scorecard table (all teams with scores, types, risk bands, trends, audit dates)
- Notes/annotations (e.g., sprint evacuated, scoring artifacts)
- Tier analysis summaries
- Cross-cutting themes
- Trend analysis table (prior vs current UPS, deltas, band transitions)
- Evidence gaps
- Footer methodology and legend

### Step 4 — Determine send method

Call `mcp__mail__list_all_accounts` to determine the available send method (Graph API, SMTP, or EWS). Use the appropriate send tool.

### Step 5 — Build email-safe HTML body

Convert the dashboard into email-compatible HTML following these rules:

#### Email HTML rules

- **No external dependencies**: No `<script>`, no CDN links (Tailwind, Google Fonts), no `<link>` tags
- **No SVG**: Replace SVG charts with table-based equivalents or omit
- **No CSS variables**: Replace `var(--color)` with literal hex values
- **No flexbox/grid**: Use `<table>` layout exclusively
- **All styles inline**: Every element gets `style="..."` attributes
- **Safe fonts only**: `font-family: Arial, Helvetica, sans-serif`
- **No `<style>` blocks**: Some email clients strip `<head>` entirely

#### Email structure (in order)

1. **Greeting** — `Hi [Name],` with brief intro paragraph
2. **Header banner** — Dark background with title, iteration info, and 3 metric cards (Mean, Median, Teams at Risk)
3. **Scorecard table** — Full 9-team table with columns: #, Team, Type (ADO/Git pill), UPS Score (color-coded), Risk Band (pill), Trend (arrow + delta), Latest Audit date
4. **Notes** — Amber background box for any scoring annotations
5. **Tier analysis** — 4 blocks with colored left borders (green/yellow/orange/red) summarizing each tier
6. **Cross-cutting themes** — Numbered circles (1-5) with theme title and brief description
7. **Footer** — Methodology, generation timestamp, risk band legend with colored dots

#### Color reference

| Element | Hex |
|---------|-----|
| Low Risk / Green | `#22c55e` |
| Moderate / Yellow | `#eab308` |
| High Risk / Orange | `#f97316` |
| Critical / Red | `#ef4444` |
| Header background | `linear-gradient(135deg, #1e1b4b 0%, #312e81 100%)` |
| Body text | `#113069` |
| ADO pill bg/text | `#e0f2fe` / `#0369a1` |
| Git pill bg/text | `#f3e8ff` / `#7e22ce` |
| Trend up | `#16a34a` |
| Trend down | `#dc2626` |
| Trend flat | `#9ca3af` |
| Note background | `#fffbeb` |
| Note text | `#92400e` |

### Step 6 — Attach the original HTML file

Attach the original portfolio HTML file so recipients can open the full interactive dashboard in a browser. Use the `attachments` parameter with `file_path`.

### Step 6.5 — Headless mode (scheduled invocation)

If the environment satisfies ALL of the following, skip Step 7's confirmation prompt and proceed directly to Step 8:

1. `PORTFOLIO_EMAIL_AUTO_SEND` is set to `true`.
2. `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS` is set to a non-empty comma-separated allowlist of email addresses.
3. **Every** recipient resolved in Step 1 (after name → email lookup) appears in the allowlist (case-insensitive, trimmed of whitespace).

When proceeding in headless mode, still **print the full preview to stdout** (the To / Subject / Body summary / Attachment block from Step 7) so the launchd log captures exactly what was sent, who it went to, and which dashboard file was attached.

If `PORTFOLIO_EMAIL_AUTO_SEND` is `true` but `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS` is unset/empty, OR any resolved recipient is not on the allowlist, **fail closed**: print which recipient failed the check and exit without sending. Do NOT fall back silently to interactive mode and do NOT send to the subset that does match.

`PORTFOLIO_EMAIL_DRY_RUN=true` overrides headless send — print the full preview as above but **do not invoke** `mcp__mail__graph_send_message`. Use this for verification.

When all three env vars are unset (the default), behavior is unchanged from the existing interactive flow described in Step 7.

### Step 7 — Preview and confirm

Before sending, show the user a preview:

```text
To: [recipients]
Subject: Portfolio Health Dashboard — [date]
Body: Email-safe HTML dashboard (scorecard, tiers, themes)
Attachment: PORTFOLIO_YYYYMMDD_HHMM.html
```

**Wait for explicit user confirmation before sending.** This is non-negotiable in interactive mode. The only exception is the headless mode in Step 6.5, where the env-var-gated allowlist check substitutes for live human confirmation.

### Step 8 — Send

Use the appropriate send tool (e.g., `mcp__mail__graph_send_message`). Set:

- `subject`: `Portfolio Health Dashboard — [Month Day, Year]`
- `body_html`: The email-safe HTML from Step 5
- `attachments`: The original dashboard HTML file
- `save_to_sent`: `true`

### Step 9 — Confirm delivery

Report the send result to the user with recipient(s) and status.

## Subject line format

```text
Portfolio Health Dashboard — [Month Day, Year]
```

Example: `Portfolio Health Dashboard — April 2, 2026`

## Output policy

- This skill does **not** write any files to disk
- This skill does **not** create drafts via IMAP (they lack a Send button in Outlook)
- This skill sends directly via Graph API (or SMTP/EWS as available)
- The original HTML dashboard is attached for full interactive viewing

## Failure behavior

- If no portfolio dashboard exists: Tell the user to run `/portfolio-health` first
- If recipient email cannot be resolved: Ask the user for the email address
- If mail account is not configured: Show error and suggest running `mcp__mail__list_all_accounts`
- If send fails: Report the error and suggest the user check their mail configuration
- If `PORTFOLIO_EMAIL_AUTO_SEND=true` but a resolved recipient is not in `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS`: fail closed, print the offending recipient, do not send

## Completion checklist

1. Recipients resolved to valid email addresses
2. Latest portfolio dashboard identified and read
3. Email-safe HTML built with inline styles only (no external deps)
4. Original HTML attached
5. User confirmed the send (interactive mode) OR headless allowlist check passed (Step 6.5)
6. Email sent successfully
7. Delivery status reported to user
