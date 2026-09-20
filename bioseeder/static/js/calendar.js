const escapeHtml = window.escapeHtml || (window.escapeHtml = function(str) {
  if (str === null || str === undefined) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
});

// BioSeeder Catalyst Calendar & Table Renderer
class CalendarManager {
  constructor() {
    this.tableBody = document.getElementById("catalysts-table-body");
    this.screenerBody = document.getElementById("screener-table-body");
    this.initClickHandlers();
  }

  initClickHandlers() {
    if (this.tableBody) {
      this.tableBody.addEventListener("click", (e) => {
        const cell = e.target.closest(".ticker-cell");
        if (cell && cell.dataset.ticker && window.dossierManager) {
          window.dossierManager.open(cell.dataset.ticker);
        }
      });
    }
    if (this.screenerBody) {
      this.screenerBody.addEventListener("click", (e) => {
        const cell = e.target.closest(".ticker-cell");
        if (cell && cell.dataset.ticker && window.dossierManager) {
          window.dossierManager.open(cell.dataset.ticker);
        }
      });
    }
  }

  getScoreBadgeClass(score) {
    if (score >= 75.0) return "score-high";
    if (score >= 50.0) return "score-med";
    return "score-low";
  }

  renderCatalysts(items) {
    if (!this.tableBody) return;

    if (items.length === 0) {
      this.tableBody.innerHTML = `
        <tr>
          <td colspan="9" style="text-align: center; color: var(--text-muted); padding: 40px;">
            No catalyst events matching current filters.
          </td>
        </tr>
      `;
      return;
    }

    this.tableBody.innerHTML = items.map(item => {
      const scoreClass = this.getScoreBadgeClass(item.bio_alpha_score);
      let countdownStr;
      if (item.days_to_event < 0) {
        countdownStr = `<span style="color: var(--text-muted); font-weight: 600;">COMPLETED (${Math.abs(item.days_to_event)}d ago)</span>`;
      } else if (item.days_to_event === 0) {
        countdownStr = `<span style="color: var(--accent-emerald); font-weight: 700;">TODAY</span>`;
      } else {
        countdownStr = `T-${item.days_to_event}d`;
      }

      const dilutionBadge = item.dilution_flag
        ? `<span class="dilution-alert-badge" title="Cash Runway < 6 Months: High probability of secondary equity offering upon catalyst">⚠️ DILUTION RISK</span>`
        : `<span style="color: var(--accent-emerald); font-family: var(--font-mono); font-size: 11px;">${item.cash_runway_months ? escapeHtml(item.cash_runway_months) + 'm runway' : 'Stable'}</span>`;

      const tickerSafe = escapeHtml(item.ticker);
      const drugNameSafe = escapeHtml(item.drug_name);
      const companyNameSafe = escapeHtml(item.company_name);
      const indicationSafe = escapeHtml(item.indication);
      const therapeuticAreaSafe = escapeHtml(item.therapeutic_area);
      const phaseSafe = escapeHtml(item.phase);
      const catalystTypeSafe = escapeHtml(item.catalyst_type);
      const detailsSafe = escapeHtml(item.details);
      const targetDateSafe = escapeHtml(item.target_date);

      const breakdown = item.score_breakdown || {};
      const breakdownTitle = `Proximity: ${breakdown.proximity_score ?? '--'} | PoS: ${breakdown.pos_score ?? '--'} | Asym: ${breakdown.asymmetry_score ?? '--'} | Fin: ${breakdown.dilution_hazard_score ?? '--'}`;

      return `
        <tr>
          <td>
            <span class="ticker-cell" data-ticker="${tickerSafe}">
              ${tickerSafe}
            </span>
          </td>
          <td>
            <div style="font-weight: 600; color: var(--text-primary);">${drugNameSafe}</div>
            <div style="font-size: 11px; color: var(--text-muted);">${companyNameSafe}</div>
          </td>
          <td>
            <div>${indicationSafe}</div>
            <div style="font-size: 10px; color: var(--text-secondary); text-transform: uppercase;">${therapeuticAreaSafe}</div>
          </td>
          <td>
            <span style="font-family: var(--font-mono); font-size: 11px; background: var(--bg-hover); padding: 2px 6px; border-radius: 3px;">
              ${phaseSafe}
            </span>
          </td>
          <td>
            <strong style="color: var(--text-primary);">${catalystTypeSafe}</strong>
            ${detailsSafe ? `<div style="font-size: 11px; color: var(--text-muted); max-width: 280px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">${detailsSafe}</div>` : ''}
          </td>
          <td style="font-family: var(--font-mono); font-size: 11px; color: var(--text-secondary);">
            ${targetDateSafe}
          </td>
          <td>
            <span class="countdown-timer">${countdownStr}</span>
          </td>
          <td>
            <span class="score-badge ${scoreClass}" title="${breakdownTitle}">
              ${item.bio_alpha_score !== null && item.bio_alpha_score !== undefined ? item.bio_alpha_score.toFixed(1) : '--'}
            </span>
          </td>
          <td>
            ${dilutionBadge}
          </td>
        </tr>
      `;
    }).join("");
  }

  renderScreener(items) {
    if (!this.screenerBody) return;

    if (items.length === 0) {
      this.screenerBody.innerHTML = `
        <tr>
          <td colspan="12" style="text-align: center; color: var(--text-muted); padding: 40px;">
            No screener results matching criteria.
          </td>
        </tr>
      `;
      return;
    }

    this.screenerBody.innerHTML = items.map((item, idx) => {
      const scoreClass = this.getScoreBadgeClass(item.composite_score);
      const tickerSafe = escapeHtml(item.ticker);
      const drugNameSafe = escapeHtml(item.drug_name);
      const indicationSafe = escapeHtml(item.indication);
      const phaseSafe = escapeHtml(item.phase);
      const targetDateSafe = escapeHtml(item.target_date);

      return `
        <tr>
          <td style="font-family: var(--font-mono); color: var(--text-muted); font-size: 11px;">#${idx + 1}</td>
          <td>
            <span class="ticker-cell" data-ticker="${tickerSafe}">${tickerSafe}</span>
          </td>
          <td>
            <div style="font-weight: 600;">${drugNameSafe}</div>
            <div style="font-size: 11px; color: var(--text-muted);">${indicationSafe}</div>
          </td>
          <td><span style="font-family: var(--font-mono); font-size: 11px;">${phaseSafe}</span></td>
          <td style="font-family: var(--font-mono); font-size: 11px;">${targetDateSafe}</td>
          <td style="font-family: var(--font-mono); font-size: 11px;">${item.market_cap ? '$' + item.market_cap.toLocaleString() + 'M' : '--'}</td>
          <td style="font-family: var(--font-mono); font-size: 11px;">${item.cash_runway_months ? item.cash_runway_months + 'm' : '--'}</td>
          <td>
            <span class="score-badge ${scoreClass}">
              ${item.composite_score !== null && item.composite_score !== undefined ? item.composite_score.toFixed(1) : '--'}
            </span>
          </td>
          <td style="font-family: var(--font-mono); font-size: 11px;">${item.proximity_score !== null && item.proximity_score !== undefined ? item.proximity_score.toFixed(1) : '--'}</td>
          <td style="font-family: var(--font-mono); font-size: 11px;">${item.pos_score !== null && item.pos_score !== undefined ? item.pos_score.toFixed(1) : '--'}</td>
          <td style="font-family: var(--font-mono); font-size: 11px;">${item.asymmetry_score !== null && item.asymmetry_score !== undefined ? item.asymmetry_score.toFixed(1) : '--'}</td>
          <td>
            ${item.dilution_flag 
              ? `<span class="dilution-alert-badge">HAZARD</span>` 
              : `<span style="color: var(--accent-emerald); font-family: var(--font-mono); font-size: 11px;">SAFE</span>`}
          </td>
        </tr>
      `;
    }).join("");
  }
}

window.calendarManager = new CalendarManager();
