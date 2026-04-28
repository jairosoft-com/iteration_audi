---
name: portfolio-email
description: Send the latest portfolio health dashboard as an email-safe HTML summary to specified recipients via Graph API.
argument-hint: "[recipient-email or name] or [multiple emails comma-separated]"
allowed-tools: Read, Glob, Grep, Bash, ToolSearch, mcp__mail__list_all_accounts, mcp__mail__graph_send_message
---

<!-- markdownlint-disable MD013 -->

# Portfolio Email Skill

Send latest portfolio health dashboard as email-safe inline HTML to one or more recipients. Body = fully styled table-based HTML. Renders in Outlook, Gmail, Apple Mail.

Do not use for:

- Generating/recomputing portfolio dashboards (use `portfolio-health`)
- Running individual project audits (use `ado-safe-audit` or `git_iteration_audit`)
- Sending emails unrelated to portfolio dashboards

## Authority and precedence

This skill owns:

- Email-safe HTML conversion of portfolio dashboard
- Email composition, recipient handling, send workflow
- Inline style conventions for email compatibility

Defers to:

- `portfolio-health` SKILL.md for dashboard generation and scoring methodology
- Memory files for recipient contact info (check `memory/user_*.md`)
- `mcp__mail__list_all_accounts` for determining correct send method

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

1. Input is email → use directly
2. Input is name → search `memory/user_*.md` for match, extract email
3. No match → ask user for email before proceeding
4. **Never guess or fabricate email addresses**

## Required workflow

### Step 1 — Identify recipients

Parse argument, extract email(s). Resolve names via memory files. Confirm if ambiguous.

### Step 2 — Find the latest portfolio dashboard

```text
Glob pattern: portfolio_report/PORTFOLIO_*.html
```

Select most recent by filename timestamp (`PORTFOLIO_YYYYMMDD_HHMM.html`). Exclude `_SUMMARY.html` and `_TREND` files — main dashboard only.

### Step 3 — Read the dashboard HTML

Read full HTML file. Extract:

- Header metrics (Portfolio Mean, Median, Teams at Risk)
- Scorecard table (all teams: scores, types, risk bands, trends, audit dates)
- Notes/annotations (sprint evacuated, scoring artifacts, etc.)
- Tier analysis summaries
- Cross-cutting themes
- Trend analysis table (prior vs current UPS, deltas, band transitions)
- Evidence gaps
- Footer methodology and legend

### Step 4 — Determine send method

Call `mcp__mail__list_all_accounts`. Use appropriate send tool (Graph API, SMTP, or EWS).

### Step 5 — Build email-safe HTML body

Convert dashboard to email-compatible HTML per these rules:

#### Email HTML rules

- **No external dependencies**: No `<script>`, no CDN links (Tailwind, Google Fonts), no `<link>` tags
- **No SVG**: Replace SVG charts with table-based equivalents or omit
- **No CSS variables**: Replace `var(--color)` with literal hex values
- **No flexbox/grid**: Use `<table>` layout exclusively
- **All styles inline**: Every element gets `style="..."` attributes
- **Safe fonts only**: `font-family: Arial, Helvetica, sans-serif`
- **No `<style>` blocks**: Some email clients strip `<head>` entirely

#### Email structure (in order)

1. **Greeting** — `Hi [Name],` + brief intro
2. **Header banner** — Dark bg, title, iteration info, 3 metric cards (Mean, Median, Teams at Risk)
3. **Scorecard table** — Full 9-team table: #, Team, Type (ADO/Git pill), UPS Score (color-coded), Risk Band (pill), Trend (arrow + delta), Latest Audit date
4. **Notes** — Amber bg box for scoring annotations
5. **Tier analysis** — 4 blocks with colored left borders (green/yellow/orange/red) per tier
6. **Cross-cutting themes** — Numbered circles (1-5) with theme title + brief description
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

Attach original portfolio HTML file so recipients can open full interactive dashboard in browser. Use `attachments` parameter with `file_path`.

### Step 6.5 — Headless mode (scheduled invocation)

Skip Step 7 confirmation and proceed to Step 8 if ALL true:

1. `PORTFOLIO_EMAIL_AUTO_SEND` = `true`
2. `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS` = non-empty comma-separated allowlist
3. **Every** resolved recipient appears in allowlist (case-insensitive, whitespace-trimmed)

In headless mode: still **print full preview to stdout** (To / Subject / Body summary / Attachment block from Step 7) so launchd log captures what was sent, who received it, which file attached.

If `PORTFOLIO_EMAIL_AUTO_SEND=true` but `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS` unset/empty, OR any resolved recipient not on allowlist — **fail closed**: print offending recipient, exit without sending. No silent fallback to interactive mode. No partial sends.

`PORTFOLIO_EMAIL_DRY_RUN=true` overrides headless send — print full preview but **do not invoke** `mcp__mail__graph_send_message`. Use for verification.

When all three env vars unset (default): existing interactive flow from Step 7 unchanged.

### Step 7 — Preview and confirm

Show user preview before sending:

```text
To: [recipients]
Subject: Portfolio Health Dashboard — [date]
Body: Email-safe HTML dashboard (scorecard, tiers, themes)
Attachment: PORTFOLIO_YYYYMMDD_HHMM.html
```

**Wait for explicit user confirmation before sending.** Non-negotiable in interactive mode. Only exception: headless mode in Step 6.5 with env-var-gated allowlist check.

### Step 8 — Send

Use appropriate send tool (e.g., `mcp__mail__graph_send_message`). Set:

- `subject`: `Portfolio Health Dashboard — [Month Day, Year]`
- `body_html`: Email-safe HTML from Step 5
- `attachments`: Original dashboard HTML file
- `save_to_sent`: `true`

### Step 9 — Confirm delivery

Report send result with recipient(s) and status.

## Subject line format

```text
Portfolio Health Dashboard — [Month Day, Year]
```

Example: `Portfolio Health Dashboard — April 2, 2026`

## Output policy

- Skill writes no files to disk
- Skill creates no IMAP drafts (no Send button in Outlook)
- Sends directly via Graph API (or SMTP/EWS as available)
- Original HTML dashboard attached for full interactive viewing

## Failure behavior

- No portfolio dashboard exists → tell user to run `/portfolio-health` first
- Recipient email unresolvable → ask user for address
- Mail account not configured → show error, suggest `mcp__mail__list_all_accounts`
- Send fails → report error, suggest user check mail config
- `PORTFOLIO_EMAIL_AUTO_SEND=true` but resolved recipient not in `PORTFOLIO_EMAIL_AUTHORIZED_RECIPIENTS` → fail closed, print offending recipient, do not send

## Completion checklist

1. Recipients resolved to valid emails
2. Latest dashboard identified and read
3. Email-safe HTML built with inline styles only (no external deps)
4. Original HTML attached
5. User confirmed send (interactive) OR headless allowlist check passed (Step 6.5)
6. Email sent
7. Delivery status reported