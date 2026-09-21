---
name: biOF
description: Institutional-Grade Biotech Financial Intelligence & Catalyst Arbitrage Terminal
colors:
  primary: "#00e5ff"
  primary-glow: "rgba(0, 229, 255, 0.25)"
  approval-emerald: "#00f59b"
  hazard-crimson: "#ff3366"
  countdown-amber: "#ffb800"
  neutral-void: "#05080f"
  neutral-base: "#080c14"
  neutral-surface: "#0d1320"
  neutral-raised: "#121929"
  border-subtle: "#141c2c"
  border-medium: "#1f2b40"
  border-strong: "#2c3c58"
  text-primary: "#f8fafc"
  text-secondary: "#94a3b8"
  text-muted: "#5e718d"
typography:
  display:
    fontFamily: "Chivo, -apple-system, sans-serif"
    fontSize: "22px"
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: "-0.5px"
  headline:
    fontFamily: "Chivo, -apple-system, sans-serif"
    fontSize: "14px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "0.4px"
  body:
    fontFamily: "Chivo, -apple-system, sans-serif"
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: "normal"
  label:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: "10.5px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "0.5px"
rounded:
  xs: "2px"
  sm: "4px"
  md: "6px"
  lg: "8px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
components:
  button-primary:
    backgroundColor: "rgba(0, 229, 255, 0.10)"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "5px 12px"
  button-primary-hover:
    backgroundColor: "rgba(0, 229, 255, 0.20)"
---

# Design System: biOF

## Overview

**Creative North Star: "The Bloomberg of Biopharma Catalyst Arbitrage"**

biOF is an institutional-grade financial intelligence interface designed for biopharmaceutical equity analysts, healthcare hedge funds, and quantitative risk managers. In biopharma trading, capital allocation is governed by binary regulatory milestones (FDA PDUFA target action dates, Phase 1/2/3 trial readouts, AdCom panel votes, and Complete Response Letters) rather than quarterly accounting cycles.

The design rejects generic consumer SaaS cards, pastel gradients, and decorative empty whitespace. Instead, it adopts the calibrated density, visual authority, and low-latency interaction models of institutional financial terminals (Bloomberg, FactSet, Reuters Eikon), optimized for multi-display continuous monitoring.

**Key Characteristics:**
- **Zero-Latency Information Architecture:** High-density data grid tables with instant multi-parameter filtering and client-side sorting.
- **Deterministic Regulatory Semantics:** Color is strictly informational and never ornamental: emerald signals approval/stability, crimson flags dilution hazard/rejection, amber denotes impending countdowns, and laser cyan provides telemetry.
- **Dual-Stack Typography:** Chivo provides ultra-crisp UI legibility, while JetBrains Mono ensures monospace tabular numeric alignment across all financial figures, market caps, and alpha scores.

## Colors

The palette is engineered for prolonged viewing in low-light trading desk environments, maintaining high contrast ratios (WCAG AA compliant) with dark slate base tones.

### Primary
- **Laser Cyan** (`#00e5ff`): The primary telemetry and interactive accent. Used for active navigation tabs, interactive symbol tickers, brand badges, and focused controls.

### Secondary
- **Approval Emerald** (`#00f59b`): Deterministic positive regulatory signal. Designates FDA approvals, high Bio-Alpha scores ($\ge 75.0$), and cash runway safety ($\ge 6\text{ months}$).
- **Hazard Crimson** (`#ff3366`): Deterministic negative risk signal. Flags dilution hazards (cash runway $< 6\text{ months}$), Complete Response Letters (CRLs), and low alpha scores.
- **Countdown Amber** (`#ffb800`): Temporal and binary advisory signal. Designates countdown timers, pending PDUFA target dates, and AdCom advisory committee meetings.

### Neutral
- **Void Black** (`#05080f`): Ticker tape floor and backdrop scrim.
- **Base Slate** (`#080c14`): Terminal workspace canvas.
- **Surface Deep** (`#0d1320`): Panel backgrounds, data table rows, and KPI ribbons.
- **Surface Raised** (`#121929`): Table header backgrounds and elevated modal cards.
- **Border Subtle** (`#141c2c`): Grid dividers and row borders.
- **Border Medium** (`#1f2b40`): Card borders and table wrapper outlines.

### Named Rules
**The Strict Semantic Color Rule.** Emerald and Crimson are strictly reserved for financial safety/gain and regulatory risk/loss respectively. They must never be applied for aesthetic decoration or generic button fills.

## Typography

**Display & UI Font:** Chivo (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif fallback)  
**Numerical / Tabular Font:** JetBrains Mono (ui-monospace, SFMono-Regular, Menlo, monospace fallback)

**Character:** Chivo delivers dense, modern, geometric sans clarity for dense clinical and financial labeling. JetBrains Mono delivers strict tabular alignment for scores, countdowns, timestamps, and balance sheet metrics.

### Hierarchy
- **Display** (800, 22px, line-height 1.2): Modal headers and primary metric values.
- **Headline** (700, 14px, line-height 1.3): Section titles and modal sub-headings.
- **Title / Subhead** (600, 12.5px, line-height 1.4): Navigation tabs and feed card headlines.
- **Body** (400/500, 12px, line-height 1.45): Table cells, drug indications, and trial summaries.
- **Label / Tabular** (600/700, 10.5px, line-height 1.2, monospace): Column headers, dates, ticker badges, and countdown clocks.

## Layout

A modular terminal layout comprising:
1. **Ceiling Marquee:** Sticky 32px live regulatory streaming ticker.
2. **Telemetry Header:** Brand insignia, real-time UTC terminal clock, and pipeline refresh button.
3. **Institutional KPI Ribbon:** 4-quadrant summary bar displaying tracked equities, 30d PDUFA events, high-alpha setups, and dilution hazard counts.
4. **Unified Filter Deck:** Multi-variable text search, clinical phase, catalyst type, timeframe, market cap, score tier, and financial health selectors.
5. **Data Workspace:** Responsive horizontal-scroll data grid with fixed header cells and zebra hover states.

## Elevation & Depth

Surfaces rely on structural tonal layering (`#080c14` $\rightarrow$ `#0d1320` $\rightarrow$ `#121929`) separated by 1px borders (`#1f2b40`). Ambient shadows carry soft multi-stage Gaussian blurs with zero offset (`box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5)`).

### Named Rules
**The Zero-Costume Depth Rule.** Never use hard cartoonish block shadows (`4px 4px 0`). All depth must come from surface tonal steps and subtle glow boundaries.

## Shapes

Precise, technical industrial contours:
- Input fields, badges, and button elements use tight 2px to 4px corners (`--radius-xs` / `--radius-sm`).
- Outer workspace modules and modal containers use 6px to 8px corners (`--radius-md` / `--radius-lg`).

## Components

### Buttons
- **Shape:** Tight rounded rectangle (2px).
- **Primary:** `rgba(0, 229, 255, 0.10)` background, `#00e5ff` laser cyan text, `1px solid rgba(0, 229, 255, 0.30)` border. Hover introduces subtle ambient glow.
- **Secondary:** `#121929` background, `#94a3b8` text, `1px solid #1f2b40` border.

### Data Tables
- **Header:** `#090e18` dark ground with 10.5px uppercase labels and interactive click-to-sort indicators (`⇅`, `▲`, `▼`).
- **Rows:** 10px 12px padding with `#141c2c` subtle dividers and `#00e5ff08` hover illumination.
- **Ticker Cells:** JetBrains Mono bold cyan text with interactive dossier modal trigger on click.

### Badges & Tags
- **High Bio-Alpha:** Emerald pill (`rgba(0, 245, 155, 0.12)` fill, `#00f59b` text).
- **Dilution Risk:** Crimson alert (`rgba(255, 51, 102, 0.12)` fill, `#ff3366` text, warning emoji `⚠️`).
- **Countdown:** Monospace amber indicator (`#ffb800`).

## Do's and Don'ts

### Do:
- **Do** align all numbers, dates, timestamps, and ticker codes in monospace font (`JetBrains Mono`).
- **Do** preserve 1px precision structural borders between all data columns and panel modules.
- **Do** maintain high visual contrast ratios against dark backgrounds for rapid triage.

### Don't:
- **Don't** use generic consumer pastel gradients, decorative illustration cartoons, or playful rounded pills.
- **Don't** apply colored border-left strips wider than 1px.
- **Don't** use green or red for non-financial or non-regulatory statuses.
