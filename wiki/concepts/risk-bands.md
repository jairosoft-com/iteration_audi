---
title: "Risk Bands"
type: concept
tags: [scoring, risk, portfolio]
sources: ["../../CLAUDE.md"]
created: 2026-04-19
updated: 2026-04-19
---

# Risk Bands

Shared banding applied to every score in the portfolio — ADO overall/dimensions, Git UPS/components, and portfolio aggregates.

| Band | Range | Color | Meaning |
|------|-------|-------|---------|
| Low | ≥ 80 | 🟢 green (`#22c55e`) | Healthy; sustain cadence |
| Moderate | 60 – 79.9 | 🟡 yellow (`#eab308`) | Monitor; targeted coaching |
| High | 40 – 59.9 | 🟠 orange (`#f97316`) | Intervene; likely delivery risk |
| Critical | < 40 | 🔴 red (`#ef4444`) | Escalate; structural remediation |

## Usage conventions

- Apply to **overall** scores *and* individual sub-scores. A team can be Low overall but Critical on a single dimension — the sub-score wins for intervention triggers.
- **Baseline exception:** first-time audits on service-model teams (e.g., Shared Services) may score Critical by default because capacity and DoR instrumentation hasn't been configured. Flag as "baseline" in the team entity page, not a regression.
- Colors are fixed to these hex values across all portfolio HTML artifacts — see [../portfolio_report/](../../portfolio_report/).

## Related

- [[scoring-ado-rubric]]
- [[scoring-git-ups]]
