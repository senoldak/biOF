// BioSeeder Terminal Application State & Orchestrator
class BioSeederApp {
  constructor() {
    this.currentTab = "calendar";
    this.catalysts = [];
    this.screenerItems = [];

    this.searchInput = document.getElementById("search-input");
    this.phaseFilter = document.getElementById("phase-filter");
    this.typeFilter = document.getElementById("type-filter");
    this.daysFilter = document.getElementById("days-filter");
    this.btnSeed = document.getElementById("btn-seed");
    this.clockEl = document.getElementById("terminal-clock");

    this.initEvents();
    this.startClock();
    this.loadData();
  }

  startClock() {
    const update = () => {
      if (this.clockEl) {
        const now = new Date();
        this.clockEl.textContent = now.toISOString().slice(11, 19) + " UTC";
      }
    };
    update();
    setInterval(update, 1000);
  }

  initEvents() {
    // Tab switching
    document.querySelectorAll(".tab-btn").forEach(btn => {
      btn.addEventListener("click", () => {
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        btn.classList.add("active");
        this.switchTab(btn.dataset.tab);
      });
    });

    // Filters
    if (this.searchInput) {
      this.searchInput.addEventListener("input", () => this.applyFilters());
    }
    if (this.phaseFilter) {
      this.phaseFilter.addEventListener("change", () => this.applyFilters());
    }
    if (this.typeFilter) {
      this.typeFilter.addEventListener("change", () => this.applyFilters());
    }
    if (this.daysFilter) {
      this.daysFilter.addEventListener("change", () => this.applyFilters());
    }

    // Seed button
    if (this.btnSeed) {
      this.btnSeed.addEventListener("click", async () => {
        this.btnSeed.disabled = true;
        this.btnSeed.textContent = "Seeding...";
        try {
          await fetch("/api/v1/seed", { method: "POST" });
          await this.loadData();
        } finally {
          this.btnSeed.disabled = false;
          this.btnSeed.textContent = "⚡ Refresh / Seed Pipeline";
        }
      });
    }
  }

  switchTab(tabId) {
    this.currentTab = tabId;
    document.querySelectorAll(".tab-content").forEach(el => el.style.display = "none");
    
    const target = document.getElementById(`view-${tabId}`);
    if (target) target.style.display = "block";

    const filterBar = document.getElementById("filter-bar");
    if (filterBar) {
      filterBar.style.display = (tabId === "live-feed") ? "none" : "flex";
    }

    if (tabId === "screener") {
      this.loadScreener();
    }
  }

  async loadData() {
    try {
      const res = await fetch("/api/v1/catalysts");
      const data = await res.json();
      this.catalysts = data.items || [];

      // Auto-seed if database is empty
      if (this.catalysts.length === 0) {
        await fetch("/api/v1/seed", { method: "POST" });
        const resAfter = await fetch("/api/v1/catalysts");
        const dataAfter = await resAfter.json();
        this.catalysts = dataAfter.items || [];
      }

      this.updateKPIs();
      this.applyFilters();
      if (window.tickerManager) {
        window.tickerManager.loadFeed();
      }
    } catch (err) {
      console.error("Failed to load catalysts:", err);
    }
  }

  async loadScreener() {
    try {
      const res = await fetch("/api/v1/screener");
      const data = await res.json();
      this.screenerItems = data.items || [];
      if (window.calendarManager) {
        window.calendarManager.renderScreener(this.screenerItems);
      }
    } catch (err) {
      console.error("Failed to load screener:", err);
    }
  }

  updateKPIs() {
    // Unique tracked companies
    const uniqueTickers = new Set(this.catalysts.map(c => c.ticker));
    const trackedEl = document.getElementById("kpi-tracked-count");
    if (trackedEl) trackedEl.textContent = uniqueTickers.size;

    // PDUFA next 30 days (strictly future/current window)
    const pdufa30d = this.catalysts.filter(c => 
      (c.catalyst_type.includes("PDUFA") || c.catalyst_type.includes("Approval")) && 
      c.days_to_event >= 0 &&
      c.days_to_event <= 30
    ).length;
    const pdufaEl = document.getElementById("kpi-pdufa-count");
    if (pdufaEl) pdufaEl.textContent = pdufa30d;

    // High Bio-Alpha (>= 75)
    const highAlpha = this.catalysts.filter(c => c.bio_alpha_score >= 75.0).length;
    const alphaEl = document.getElementById("kpi-high-alpha-count");
    if (alphaEl) alphaEl.textContent = highAlpha;

    // Dilution hazards
    const dilutionAlerts = this.catalysts.filter(c => c.dilution_flag).length;
    const dilutionEl = document.getElementById("kpi-dilution-count");
    if (dilutionEl) dilutionEl.textContent = dilutionAlerts;
  }

  applyFilters() {
    const q = (this.searchInput?.value || "").toLowerCase().trim();
    const phase = this.phaseFilter?.value || "";
    const type = this.typeFilter?.value || "";
    const maxDays = this.daysFilter?.value ? parseInt(this.daysFilter.value) : null;

    const filtered = this.catalysts.filter(item => {
      if (q) {
        const matchesTicker = item.ticker.toLowerCase().includes(q);
        const matchesCompany = item.company_name.toLowerCase().includes(q);
        const matchesDrug = item.drug_name.toLowerCase().includes(q);
        const matchesIndication = item.indication.toLowerCase().includes(q);
        if (!matchesTicker && !matchesCompany && !matchesDrug && !matchesIndication) {
          return false;
        }
      }

      if (phase && !item.phase.toLowerCase().includes(phase.toLowerCase())) {
        return false;
      }

      if (type && !item.catalyst_type.toLowerCase().includes(type.toLowerCase())) {
        return false;
      }

      if (maxDays !== null && (item.days_to_event < 0 || item.days_to_event > maxDays)) {
        return false;
      }

      return true;
    });

    if (window.calendarManager) {
      window.calendarManager.renderCatalysts(filtered);
    }
  }
}

document.addEventListener("DOMContentLoaded", () => {
  window.app = new BioSeederApp();
});
