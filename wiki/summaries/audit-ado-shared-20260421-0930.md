---
title: "Shared Services Audit — 2026-04-21 0930"
type: summary
tags: [ado, ado-shared, iteration-7.2, audit]
sources: ["../../ado_shared/audit/AUDIT_20260421_0930.md"]
created: 2026-04-21

## updated: 2026-04-21

# Shared Services Audit — 2026-04-21 0930

Source: [AUDIT_20260421_0930.md](../../ado_shared/audit/AUDIT_20260421_0930.md) · 2026-04-21 09:30 PDT · Iteration 7.2 (Day 2 of 14 — early-sprint)

## TL;DR

**37.7/100 (Critical, Δ +5.5)** — Shared Services improves modestly over the 2026-04-19 baseline (32.2), driven by a +43.3 DoR gain (5/6 items now have Desc+AC). But **Team Capacity is STILL NOT configured for Iteration 7.2** despite being the P1 item from baseline (2026-04-19) — identical API error, deterministic 0 persists. The 12 PI7-parent orphan User Stories (#202059–#202071) also remain un-iterated (baseline P1 #2 unactioned).

## Scores

| Dimension | Score | Band |
|-----------|------:|------|
| **Overall** | 37.7 | 🔴 Critical |
| Iteration Planning | 20.7 | 🔴 Critical |
| Team Capacity | 0.0 | 🔴 Critical (STILL not configured — P1 unfixed since baseline) |
| Estimation | 50.0 | 🟠 High |
| DoR Compliance | 83.3 | 🟢 Low |
| Work Item Balance | 30.0 | 🔴 Critical (service-model: no User Story → −40) |
| Backlog Refinement | 80.0 | 🟢 Low |
| Delivery Predictability | 0.0 | 🔴 Critical (early-sprint — low delivery expected) |

## Top issues

- **Team Capacity STILL NOT configured for 7.2** — identical API error to baseline; P1 #1 recommendation from 2026-04-19 not actioned. Single highest-leverage fix (configuring even 1 h/day for any contributor lifts Overall ~7 pts).
- **12 PI7-parent User Stories (#202059–#202071) still orphan** in Estimation state with no sub-iteration — baseline P1 #2 unactioned; caps Iteration Planning at 20.7.
- **3 Design items unsized** (#202553, #202687, #202724) — native Estimation-state behavior but rubrically drags Estimation to 50.0.
- **2/6 current items untouched since sprint start** (#202551, #202687) → Backlog Refinement −20 (from 100 at baseline → 80).
- **Work Item Balance −70 structural**: service-model team writes Design/Enabler work (no User Stories) → triggers −40 no_US + −30 dominant_type.

## Delta vs prior

Previous: [[summaries/audit-ado-shared-20260419-1947]] — 32.2 (Critical); this: 37.7 (Critical); Δ +5.5 (DoR +43.3 and Estimation +10 offset Backlog Refinement −20; Team Capacity unchanged at 0).

## Linked concepts / entities

- [[entities/team-ado-shared]]
- [[concepts/scoring-ado-rubric]]
- [[concepts/risk-bands]]
- [[synthesis/capacity-planning]]
- [[synthesis/service-model-scoring]]
