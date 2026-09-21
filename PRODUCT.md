# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Vanilla ES6, Semantic HTML5, CSS Custom Properties (zero-build, served directly by FastAPI without Node.js tooling dependencies).

## Users

Institutional biotech investors, hedge fund quantitative analysts, healthcare equity research analysts, and clinical portfolio managers tracking US-listed biopharmaceutical equities (NASDAQ/NYSE) approaching binary clinical/regulatory catalyst events.

## Product Purpose

biOF provides institutional-grade biotech financial intelligence and quantitative catalyst scoring. In biopharma, market valuations are dominated by discrete binary events (FDA PDUFA target dates, Phase 1/2/3 trial readouts, AdCom panel votes, Complete Response Letters) rather than quarterly trailing earnings. biOF automates multi-factor risk/reward scoring (Bio-Alpha Score, 0-100), detects dilution hazards before event windows, and displays high-density market intelligence.

## Positioning

Unlike generic stock screeners or clinical trial databases, biOF mathematically combines clinical probability of success (PoS), proximity time-decay velocity, addressable market asymmetry, and balance sheet runway into a single quantitative composite score designed specifically for biopharma event-driven trading.

## Operating Context

Desktop and multi-monitor financial terminal environments; high-stress, rapid-scanning execution environments where information density, color semantics (emerald approvals, crimson CRLs, amber countdowns/alerts), and keyboard-friendly navigation outperform consumer-grade whitespace.

## Capabilities and Constraints

- High-density data grid tables with instant multi-parameter filtering and full click-to-sort headers.
- Real-time continuous streaming regulatory news ticker marquee.
- Interactive multi-parameter Catalyst Calendar and Bio-Alpha Screener.
- Clinical progress dossier modal detailing company drug pipelines and direct ClinicalTrials.gov NCT integration.
- Fast, zero-dependency vanilla web stack with instant loading.

## Brand Commitments

- Aesthetic: Institutional Dark Cyber-Biotech Terminal.
- Color Philosophy: Deep slate `#0a0e17` base, `#00f59b` emerald approval/high-alpha, `#ff3366` crimson hazard/crl, `#00e5ff` cyan telemetry, `#ffb800` amber countdowns.
- Monospace typographic accents for financial/numerical figures and dates.

## Evidence on Hand

- Real biopharma catalyst records, pipeline drugs, trial datasets, and market telemetry seeded in local SQLite database (`bioseeder.db`).
- REST API endpoints (`/api/v1/catalysts`, `/api/v1/screener`, `/api/v1/ticker`, `/api/v1/dossier/{ticker}`).

## Product Principles

1. **Information Density & Speed First:** Maximize visible data and actionable intelligence without unnecessary layout padding or ornamental clutter.
2. **Deterministic Financial Semantics:** Green is strictly positive (regulatory approval, high alpha, cash safety), Red is danger (dilution risk, CRL), Amber is binary pending.
3. **Auditability:** Every composite score reveals its mathematical factor breakdown (proximity, PoS, asymmetry, dilution).
