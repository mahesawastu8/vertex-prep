import os

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"

SUPAHERO_CSS = """
    :root {
      --bg-canvas: #F3F5F8;
      --bg-surface: #FFFFFF;
      --bg-subtle: #EAEFF4;
      --bg-obsidian: #0B131A;
      --ink-900: #0B131A;
      --ink-700: #263645;
      --ink-500: #3E5263;
      --emerald: #0B6350;
      --emerald-soft: #E1F2EE;
      --crimson: #B82921;
      --crimson-soft: #FCECEB;
      --amber: #9E5400;
      --amber-soft: #FDF2E2;
      --cobalt: #164F73;
      --cobalt-soft: #E4F0F7;
      --border: #D4DEE7;
      --border-strong: #B6C6D4;
      --radius-xl: 20px;
      --radius-lg: 14px;
      --radius-md: 10px;
      --shadow-soft: 0 12px 32px -8px rgba(11, 19, 26, 0.06), 0 2px 6px rgba(11, 19, 26, 0.04);
      --shadow-float: 0 18px 42px -10px rgba(11, 19, 26, 0.12), 0 4px 12px rgba(11, 19, 26, 0.06);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html { scroll-behavior: smooth; }

    body {
      background-color: var(--bg-canvas);
      background-image: radial-gradient(#CBD6E2 1px, transparent 1px);
      background-size: 24px 24px;
      color: var(--ink-900);
      font-family: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      font-size: 16px;
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
    }

    /* =====================================================================
       SUPAHERO FLOATING PILL NAVBAR
       ===================================================================== */
    .supa-nav-wrap {
      position: sticky;
      top: 16px;
      z-index: 200;
      padding: 0 24px;
      margin-bottom: 12px;
    }

    .supa-navbar {
      max-width: 1240px;
      margin: 0 auto;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(16px);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 10px 18px;
      box-shadow: var(--shadow-float);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
    }

    .supa-brand {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .brand-dot {
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: var(--bg-obsidian);
      color: #FFFFFF;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }

    .course-switcher {
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      color: var(--ink-900);
      font-family: inherit;
      font-size: 0.86rem;
      font-weight: 700;
      padding: 8px 14px;
      border-radius: 999px;
      cursor: pointer;
    }

    .supa-pills {
      display: flex;
      align-items: center;
      gap: 4px;
      background: var(--bg-subtle);
      padding: 4px;
      border-radius: 999px;
    }

    .supa-pill-btn {
      border: none;
      background: transparent;
      color: var(--ink-700);
      font-family: inherit;
      font-size: 0.85rem;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.16s ease;
    }

    .supa-pill-btn.active {
      background: var(--bg-obsidian);
      color: #FFFFFF;
    }

    .supa-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .cmdk-trigger {
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      color: var(--ink-900);
      padding: 8px 14px;
      border-radius: 999px;
      font-family: inherit;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .cmdk-trigger:hover {
      border-color: var(--emerald);
    }

    .cmdk-trigger kbd {
      background: var(--bg-subtle);
      padding: 2px 7px;
      border-radius: 999px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
    }

    /* =====================================================================
       SUPAHERO SPLIT-SCREEN HERO SECTION
       ===================================================================== */
    .shell {
      max-width: 1280px;
      margin: 0 auto;
      padding: 20px 24px 96px;
    }

    .supa-hero {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 44px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-soft);
      display: grid;
      grid-template-columns: 1.25fr 1fr;
      gap: 40px;
      align-items: center;
    }

    @media (max-width: 980px) {
      .supa-hero {
        grid-template-columns: 1fr;
        padding: 28px;
      }
    }

    .hero-meta-line {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--ink-500);
      margin-bottom: 14px;
    }

    h1 {
      font-family: 'Newsreader', Georgia, serif;
      font-size: 3.1rem;
      line-height: 1.08;
      font-weight: 700;
      letter-spacing: -0.025em;
      color: var(--ink-900);
      margin-bottom: 18px;
    }

    h2 {
      font-family: 'Newsreader', Georgia, serif;
      font-size: 1.85rem;
      line-height: 1.2;
      font-weight: 700;
      letter-spacing: -0.015em;
      color: var(--ink-900);
    }

    h3 {
      font-size: 1.22rem;
      line-height: 1.32;
      font-weight: 700;
      color: var(--ink-900);
    }

    .hero-lead {
      font-size: 1.06rem;
      color: var(--ink-700);
      margin-bottom: 26px;
      max-width: 58ch;
    }

    .hero-cta-row {
      display: flex;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 28px;
    }

    .btn-primary {
      background: var(--bg-obsidian);
      color: #FFFFFF;
      border: 1px solid var(--bg-obsidian);
      padding: 13px 24px;
      border-radius: 999px;
      font-family: inherit;
      font-size: 0.92rem;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.15s ease, background 0.15s ease;
    }

    .btn-primary:hover {
      background: var(--emerald);
      border-color: var(--emerald);
      transform: translateY(-1px);
    }

    .btn-secondary {
      background: var(--bg-subtle);
      color: var(--ink-900);
      border: 1px solid var(--border-strong);
      padding: 13px 22px;
      border-radius: 999px;
      font-family: inherit;
      font-size: 0.92rem;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .btn-secondary:hover {
      border-color: var(--ink-900);
    }

    .hero-stats-row {
      display: flex;
      flex-wrap: wrap;
      gap: 24px;
      padding-top: 22px;
      border-top: 1px solid var(--border);
    }

    .stat-unit {
      display: flex;
      flex-direction: column;
    }

    .stat-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--ink-900);
    }

    .stat-lbl {
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--ink-500);
    }

    /* Hero Right Showcase Mockup Window */
    .hero-showcase {
      background: var(--bg-subtle);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .window-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
    }

    .window-dots {
      display: inline-flex;
      gap: 6px;
    }

    .w-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--border-strong);
    }

    .window-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--emerald);
      background: var(--emerald-soft);
      padding: 4px 10px;
      border-radius: 999px;
    }

    .hero-slide-preview {
      width: 100%;
      border-radius: 10px;
      border: 1px solid var(--border);
      cursor: zoom-in;
      display: block;
    }

    .showcase-caption {
      font-size: 0.84rem;
      color: var(--ink-700);
      font-weight: 600;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    /* =====================================================================
       CHAPTER QUICK-JUMP PILL STRIP
       ===================================================================== */
    .chapter-ribbon {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 28px;
    }

    .chapter-chip {
      text-decoration: none;
      background: var(--bg-surface);
      border: 1px solid var(--border);
      color: var(--ink-700);
      padding: 9px 16px;
      border-radius: 999px;
      font-size: 0.84rem;
      font-weight: 700;
      box-shadow: 0 2px 5px rgba(11, 19, 26, 0.03);
      transition: all 0.15s ease;
    }

    .chapter-chip:hover {
      border-color: var(--emerald);
      color: var(--emerald);
      transform: translateY(-1px);
    }

    /* =====================================================================
       SUPAHERO BENTO CHAPTER MODULES
       ===================================================================== */
    .view-section { display: none; }
    .view-section.active { display: block; }

    .bento-chapter {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 36px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-soft);
    }

    @media (max-width: 768px) {
      .bento-chapter { padding: 24px; }
    }

    .bento-header {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 12px;
    }

    .ch-index {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--emerald);
      text-transform: uppercase;
      letter-spacing: 0.06em;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 12px;
      border-radius: 999px;
      font-size: 0.76rem;
      font-weight: 700;
    }

    .badge-crimson { background: var(--crimson-soft); color: var(--crimson); }
    .badge-emerald { background: var(--emerald-soft); color: var(--emerald); }
    .badge-amber { background: var(--amber-soft); color: var(--amber); }
    .badge-cobalt { background: var(--cobalt-soft); color: var(--cobalt); }

    .bento-sub {
      color: var(--ink-700);
      font-size: 1rem;
      margin: 8px 0 24px;
      max-width: 76ch;
    }

    .bento-split {
      display: grid;
      grid-template-columns: 1.55fr 1fr;
      gap: 28px;
      align-items: start;
    }

    @media (max-width: 980px) {
      .bento-split { grid-template-columns: 1fr; }
    }

    /* Visual Step Tiles */
    .step-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(175px, 1fr));
      gap: 14px;
      margin-bottom: 18px;
    }

    .step-tile {
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
    }

    .step-tile.tone-emerald {
      background: var(--emerald-soft);
      border-color: #9ECBC0;
    }

    .step-tile.tone-crimson {
      background: var(--crimson-soft);
      border-color: #E5B2AE;
    }

    .step-tile.tone-amber {
      background: var(--amber-soft);
      border-color: #E8C99B;
    }

    .step-tile.tone-cobalt {
      background: var(--cobalt-soft);
      border-color: #A7CBE2;
    }

    .tile-kicker {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--ink-500);
      margin-bottom: 6px;
    }

    .tile-title {
      font-size: 1rem;
      font-weight: 700;
      color: var(--ink-900);
      margin-bottom: 6px;
    }

    .tile-body {
      font-size: 0.86rem;
      color: var(--ink-700);
      line-height: 1.5;
    }

    /* Callout Banner inside Bento */
    .exam-radar {
      background: var(--bg-subtle);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      padding: 20px 22px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
      gap: 18px;
    }

    .radar-col-title {
      font-size: 0.74rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--crimson);
      margin-bottom: 6px;
    }

    .radar-col-title.emerald { color: var(--emerald); }

    .radar-col-text {
      font-size: 0.9rem;
      color: var(--ink-900);
      line-height: 1.55;
    }

    /* Slide Proof Window (Right Column of Bento) */
    .slide-dock {
      background: var(--bg-subtle);
      border: 1px solid var(--border-strong);
      border-radius: var(--radius-lg);
      padding: 20px;
    }

    .dock-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 12px;
    }

    .dock-label {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.74rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--ink-500);
    }

    .dock-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }

    .dock-btn {
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      color: var(--ink-700);
      padding: 5px 11px;
      border-radius: 999px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
    }

    .dock-btn.active {
      background: var(--bg-obsidian);
      color: #FFFFFF;
      border-color: var(--bg-obsidian);
    }

    .dock-img {
      width: 100%;
      height: auto;
      border-radius: 10px;
      border: 1px solid var(--border);
      display: block;
      cursor: zoom-in;
    }

    .dock-foot {
      margin-top: 10px;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--ink-500);
      display: flex;
      justify-content: space-between;
    }

    /* Comparison Table inside Bento */
    .table-scroll {
      overflow-x: auto;
      margin-bottom: 18px;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.9rem;
    }

    th {
      text-align: left;
      padding: 13px 16px;
      background: var(--bg-subtle);
      color: var(--ink-900);
      font-weight: 700;
      border-bottom: 2px solid var(--border-strong);
    }

    td {
      padding: 13px 16px;
      border-bottom: 1px solid var(--border);
      color: var(--ink-700);
      vertical-align: top;
    }

    /* =====================================================================
       CBT EXAM SIMULATOR SECTION
       ===================================================================== */
    .cbt-header-bar {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 24px 32px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-soft);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .cbt-score-pill {
      font-family: 'JetBrains Mono', monospace;
      font-size: 1rem;
      font-weight: 700;
      color: var(--emerald);
      background: var(--emerald-soft);
      padding: 8px 16px;
      border-radius: 999px;
    }

    .cbt-filters {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .cbt-filter-btn {
      background: var(--bg-subtle);
      border: 1px solid var(--border-strong);
      color: var(--ink-700);
      padding: 8px 16px;
      border-radius: 999px;
      font-family: inherit;
      font-size: 0.84rem;
      font-weight: 700;
      cursor: pointer;
    }

    .cbt-filter-btn.active {
      background: var(--bg-obsidian);
      color: #FFFFFF;
      border-color: var(--bg-obsidian);
    }

    .q-module {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 32px;
      margin-bottom: 22px;
      box-shadow: var(--shadow-soft);
    }

    .q-top {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 10px;
      margin-bottom: 16px;
    }

    .q-stem-txt {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--ink-900);
      margin-bottom: 20px;
      line-height: 1.62;
    }

    .opt-stack {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .opt-row {
      text-align: left;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      font-family: inherit;
      font-size: 0.94rem;
      color: var(--ink-900);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.14s ease;
    }

    .opt-row:hover {
      background: #FFFFFF;
      border-color: var(--emerald);
    }

    .opt-row.is-correct {
      background: var(--emerald-soft);
      border-color: var(--emerald);
      font-weight: 700;
    }

    .opt-row.is-wrong {
      background: var(--crimson-soft);
      border-color: var(--crimson);
    }

    .opt-key {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--emerald);
      min-width: 24px;
    }

    .q-drawer {
      display: none;
      margin-top: 22px;
      padding-top: 22px;
      border-top: 1px solid var(--border);
      grid-template-columns: 1.45fr 1fr;
      gap: 24px;
      align-items: start;
    }

    .q-drawer.open { display: grid; }

    @media (max-width: 860px) {
      .q-drawer.open { grid-template-columns: 1fr; }
    }

    /* =====================================================================
       RAPID FLASHCARD GRID (H-1 EXAM)
       ===================================================================== */
    .flash-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 22px;
    }

    .flash-unit {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-xl);
      padding: 28px;
      box-shadow: var(--shadow-soft);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 16px;
    }

    .flash-q {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--ink-900);
      margin-top: 10px;
    }

    .flash-ans {
      display: none;
      padding-top: 16px;
      border-top: 1px solid var(--border);
      font-size: 0.92rem;
      color: var(--ink-700);
      line-height: 1.6;
    }

    .flash-unit.open .flash-ans { display: block; }

    /* =====================================================================
       LIGHTBOX & CMD+K MODAL
       ===================================================================== */
    .modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(11, 19, 26, 0.84);
      backdrop-filter: blur(6px);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .modal-overlay.open { display: flex; }

    .modal-window {
      max-width: 1060px;
      width: 100%;
      background: var(--bg-surface);
      border-radius: var(--radius-xl);
      padding: 22px;
      box-shadow: var(--shadow-float);
    }

    .modal-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }

    .modal-window img {
      width: 100%;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 10px;
    }

    .cmdk-box {
      max-width: 840px;
      width: 100%;
      background: var(--bg-surface);
      border-radius: var(--radius-xl);
      border: 1px solid var(--border);
      overflow: hidden;
      max-height: 80vh;
      display: flex;
      flex-direction: column;
      box-shadow: var(--shadow-float);
    }

    .cmdk-bar {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 18px 22px;
      border-bottom: 1px solid var(--border);
      background: var(--bg-subtle);
    }

    .cmdk-input {
      flex: 1;
      border: none;
      background: transparent;
      font-family: inherit;
      font-size: 1.02rem;
      font-weight: 600;
      color: var(--ink-900);
      outline: none;
    }

    .cmdk-results {
      overflow-y: auto;
      padding: 18px 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }

    .cmdk-hit {
      padding: 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      display: flex;
      gap: 16px;
      align-items: flex-start;
      background: var(--bg-surface);
    }

    .cmdk-hit img {
      width: 108px;
      border-radius: 8px;
      border: 1px solid var(--border);
      cursor: zoom-in;
    }

    /* World-class micro-interactions */
    .supa-pill-btn, .opt-row, .cbt-filter-btn, .action-btn {
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .supa-pill-btn:hover, .opt-row:hover {
      transform: translateY(-1px);
    }
    .opt-row:active {
      transform: scale(0.99);
    }
"""

SUPAHERO_JS = """
  function switchView(viewId, btn) {
    document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.supa-pill-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('view-' + viewId).classList.add('active');
    if (btn) btn.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function jumpToQuiz() {
    const btns = document.querySelectorAll('.supa-pill-btn');
    switchView('soal', btns[1]);
  }

  function swapDockSlide(dockId, imgSrc, capText, btn) {
    const img = document.getElementById('dock-img-' + dockId);
    const cap = document.getElementById('dock-cap-' + dockId);
    if (img) img.src = imgSrc;
    if (cap) cap.textContent = capText;
    btn.parentElement.querySelectorAll('.dock-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }

  function openZoom(src, title) {
    document.getElementById('zoom-img').src = src;
    document.getElementById('zoom-title').textContent = title || 'Bukti Slide Asli Dosen';
    document.getElementById('zoom-modal').classList.add('open');
  }

  function closeZoom() {
    document.getElementById('zoom-modal').classList.remove('open');
  }

  // Persistent CBT Quiz Engine
  const QUIZ_KEY = 'supahero_vertex_' + window.MOD_KEY;
  let userAns = {};
  try { userAns = JSON.parse(localStorage.getItem(QUIZ_KEY) || '{}'); } catch (e) {}

  function pickAnswer(qIdx, oIdx) {
    userAns[qIdx] = oIdx;
    try { localStorage.setItem(QUIZ_KEY, JSON.stringify(userAns)); } catch (e) {}
    syncQuizUI();
  }

  function clearQuiz() {
    userAns = {};
    try { localStorage.removeItem(QUIZ_KEY); } catch (e) {}
    syncQuizUI();
  }

  function filterCBT(cat, btn) {
    document.querySelectorAll('.cbt-filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.q-module').forEach(el => {
      el.style.display = (cat === 'all' || el.dataset.cat === cat) ? 'block' : 'none';
    });
  }

  function syncQuizUI() {
    let right = 0, done = 0;
    window.QUIZ_DATA.forEach((q, i) => {
      const pick = userAns[i];
      const mod = document.getElementById('qm-' + i);
      if (!mod) return;
      const rows = mod.querySelectorAll('.opt-row');
      const drawer = document.getElementById('qd-' + i);
      rows.forEach((r, rIdx) => {
        r.classList.remove('is-correct', 'is-wrong');
        if (pick !== undefined) {
          if (rIdx === q.ans) r.classList.add('is-correct');
          else if (rIdx === pick && pick !== q.ans) r.classList.add('is-wrong');
        }
      });
      if (pick !== undefined) {
        done++;
        if (pick === q.ans) right++;
        if (drawer) drawer.classList.add('open');
      } else if (drawer) {
        drawer.classList.remove('open');
      }
    });
    const pill = document.getElementById('cbt-score-pill');
    if (pill) pill.textContent = `Skor Anda: ${right}/${window.QUIZ_DATA.length} Benar (${done} Dijawab)`;
  }

  // Instant Cmd+K Search across 51 UAB files & slides
  function openSearchModal() {
    document.getElementById('search-modal').classList.add('open');
    const inp = document.getElementById('cmdk-inp');
    inp.focus();
    execSearch();
  }

  function closeSearchModal() {
    document.getElementById('search-modal').classList.remove('open');
  }

  function execSearch() {
    const q = (document.getElementById('cmdk-inp').value || '').trim().toLowerCase();
    const out = document.getElementById('cmdk-out');
    const data = window.VERTEX_SEARCH_INDEX || [];
    const words = q.split(/\\s+/).filter(Boolean);
    const res = [];
    for (let i = 0; i < data.length; i++) {
      const it = data[i];
      if (words.length) {
        const hay = (it.source + ' ' + it.block + ' ' + it.text).toLowerCase();
        if (!words.every(w => hay.includes(w))) continue;
      }
      res.push(it);
      if (res.length >= 28) break;
    }
    if (!res.length) {
      out.innerHTML = '<div style="padding:24px;text-align:center;color:#3E5263;">Tidak ditemukan hasil. Coba ketik: Sentinel, KCl, Gelang, B12, Metformin, Anemia.</div>';
      return;
    }
    out.innerHTML = res.map(r => `
      <div class="cmdk-hit">
        ${r.img ? `<img src="${r.img}" alt="Slide" onclick="closeSearchModal();openZoom('${r.img}','${r.source}')" />` : ''}
        <div>
          <div style="font-size:0.74rem;font-weight:700;color:#0B6350;margin-bottom:4px;">${r.type} · ${r.block} · ${r.source}</div>
          <div style="font-size:0.9rem;color:#0B131A;">${r.text}</div>
        </div>
      </div>
    `).join('');
  }

  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openSearchModal();
    } else if (e.key === 'Escape') {
      closeZoom();
      closeSearchModal();
    }
  });

  document.addEventListener('DOMContentLoaded', () => {
    syncQuizUI();
  });
"""

# ==============================================================================
# 1. BDT KUL 3 PATIENT SAFETY — SUPAHERO EDITION
# ==============================================================================
BDT_SUPAHERO = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VERTEX-PREP · BDT Kuliah 3: Patient Safety (Supahero Edition)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
  <style>{SUPAHERO_CSS}</style>
</head>
<body>

  <!-- SUPAHERO FLOATING PILL NAVBAR -->
  <div class="supa-nav-wrap">
    <header class="supa-navbar">
      <div class="supa-brand">
        <span class="brand-dot">VX</span>
        <select class="course-switcher" aria-label="Pilih Kuliah" onchange="window.location.href=this.value">
          <option value="BDT_KUL3_Patient_Safety.html" selected>Blok 7 BDT · Kuliah 3: Patient Safety (dr. Riskiyah)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html">Blok 9 EMN · Kuliah 2: Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
        </select>
      </div>

      <nav class="supa-pills" aria-label="Mode Belajar">
        <button type="button" class="supa-pill-btn active" onclick="switchView('materi', this)">7 Bab Visual (Pengganti PPT)</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('soal', this)">9 Soal Asli UAB BDT</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('flash', this)">Cek Cepat H-1 Ujian</button>
      </nav>

      <div class="supa-actions">
        <button type="button" class="cmdk-trigger" onclick="openSearchModal()">
          <span>Cari 51 File UAB</span>
          <kbd>⌘K</kbd>
        </button>
      </div>
    </header>
  </div>

  <main class="shell">

    <!-- =================================================================== -->
    <!-- VIEW 1: SUPAHERO HERO + 7 BENTO VISUAL CHAPTERS                     -->
    <!-- =================================================================== -->
    <div id="view-materi" class="view-section active">

      <!-- SUPAHERO SPLIT-SCREEN HERO -->
      <section class="supa-hero">
        <div>
          <h1>Kuasai 80 Slide Patient Safety Tanpa Buka PPT Sekalipun.</h1>
          <div class="hero-meta-line">Blok 7 BDT · Kuliah Pakar 3 · dr. Riskiyah, MMRS</div>
          <p class="hero-lead">Setelah kami membedah arsip Bank Soal UAB BDT angkatan terdahulu, <strong>100% dari 9 soal ujian Patient Safety hanya keluar dari 14 slide inti</strong>. Seluruh 80 slide telah diperas menjadi 7 modul visual di bawah ini, lengkap dengan bukti tangkapan layar slide aslinya.</p>

          <div class="hero-cta-row">
            <a href="#ch-01" class="btn-primary">Mulai Pelajari 7 Bab Visual ↓</a>
            <button type="button" class="btn-secondary" onclick="jumpToQuiz()">Kerjakan 9 Soal Asli UAB →</button>
          </div>

          <div class="hero-stats-row">
            <div class="stat-unit">
              <span class="stat-num">80 → 7 Bab</span>
              <span class="stat-lbl">Pemadatan Materi Utuh</span>
            </div>
            <div class="stat-unit">
              <span class="stat-num">14 Slide Inti</span>
              <span class="stat-lbl">Penghasil 100% Soal UAB</span>
            </div>
            <div class="stat-unit">
              <span class="stat-num">9 Soal Asli</span>
              <span class="stat-lbl">UAB & Remidi BDT Terbukti</span>
            </div>
          </div>
        </div>

        <div class="hero-showcase">
          <div class="window-bar">
            <div class="window-dots">
              <span class="w-dot"></span><span class="w-dot"></span><span class="w-dot"></span>
            </div>
            <span class="window-tag">Bukti Slide #48 · Sumber Soal Remidi No. 39</span>
          </div>
          <img src="slides_bdt_kul3/slide_48.jpg" alt="Bukti Slide 48 High Alert" class="hero-slide-preview" onclick="openZoom('slides_bdt_kul3/slide_48.jpg', 'Slide 48 · Label HIGH ALERT! MEDICATION pada Botol KCl Pekat')" />
          <div class="showcase-caption">
            <span>Slide 48 Asli dr. Riskiyah (Opsi soal diambil persis dari kotak biru)</span>
            <span>Klik untuk Zoom ↗</span>
          </div>
        </div>
      </section>

      <!-- CHAPTER QUICK-JUMP RIBBON -->
      <div class="chapter-ribbon">
        <a href="#ch-01" class="chapter-chip">01 · Tangga 5 Insiden (3 Soal UAB)</a>
        <a href="#ch-02" class="chapter-chip">02 · 7 Standar vs 6 SKP vs 7 Langkah (2 Soal UAB)</a>
        <a href="#ch-03" class="chapter-chip">03 · SKP 1 Identifikasi & Gelang (1 Soal UAB)</a>
        <a href="#ch-04" class="chapter-chip">04 · SKP 2 Komunikasi TBaK & SBAR</a>
        <a href="#ch-05" class="chapter-chip">05 · SKP 3 Obat High-Alert & KCl (1 Soal UAB)</a>
        <a href="#ch-06" class="chapter-chip">06 · SKP 4 Operasi & Time-Out (1 Soal UAB)</a>
        <a href="#ch-07" class="chapter-chip">07 · SKP 5–6, Lapor 2x24J & RCA (2 Soal UAB)</a>
      </div>

      <!-- BENTO CHAPTER 01 -->
      <article id="ch-01" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 01 · Merangkum Slide 1–22</span>
          <span class="badge badge-crimson">Keluar di 3 Soal Asli UAB BDT</span>
        </div>
        <h2>Tangga 5 Insiden Keselamatan Pasien</h2>
        <p class="bento-sub">Jangan menghafal kalimat panjang. Untuk menjawab soal skenario insiden di ujian dalam 5 detik, cukup cek <strong>2 hal</strong>: (1) Apakah kesalahan sudah mengenai tubuh pasien? dan (2) Apakah timbul cedera atau kematian?</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-amber">
                <div class="tile-kicker">1 · Belum Insiden</div>
                <div class="tile-title">KPC (Potensial)</div>
                <div class="tile-body">Kondisi sangat berpotensi cedera, tetapi <strong>belum ada tindakan salah</strong>. Contoh: defibrilator IGD rusak, lantai licin.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">2 · Belum Ke Pasien</div>
                <div class="tile-title">KNC (Near Miss)</div>
                <div class="tile-body">Kesalahan sudah terjadi tetapi <strong>ketahuan sebelum terpapar ke pasien</strong>. Contoh: salah siapkan dosis obat tapi batal diberikan.</div>
              </div>
              <div class="step-tile">
                <div class="tile-kicker">3 · Terpapar, Aman</div>
                <div class="tile-title">KTC (Tanpa Cedera)</div>
                <div class="tile-body">Obat/tindakan salah <strong>sudah mengenai pasien</strong>, tetapi beruntung pasien <strong>tidak mengalami cedera</strong> sama sekali.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">4 · Pasien Cedera</div>
                <div class="tile-title">KTD (Adverse Event)</div>
                <div class="tile-body">Sudah terpapar ke pasien dan <strong>mengakibatkan cedera ringan/sedang</strong> yang bersifat reversibel.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">5 · Kematian / Cacat</div>
                <div class="tile-title">Kejadian Sentinel</div>
                <div class="tile-body">Suatu KTD fatal yang mengakibatkan <strong>kematian, cacat permanen, salah sisi operasi, atau bayi tertukar</strong>.</div>
              </div>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title emerald">Fakta Eksplisit Slide 18–20</div>
                <div class="radar-col-text">Prinsip utama: <em>Being Safe Means Do No Harm</em> (Slide 19). Tiga kasus latihan di slide dosen: (1) Bayi tertukar = <strong>Sentinel</strong>, (2) Salah dosis KCl meninggal = <strong>Sentinel</strong>, (3) Salah siapkan obat ketahuan sebelum diberikan = <strong>KNC</strong>.</div>
              </div>
              <div>
                <div class="radar-col-title">Jebakan Soal UAB (No. 29 & UAB 22 No. 70)</div>
                <div class="radar-col-text">Pasien disuntik Antalgin → syok anafilaktik → <strong>meninggal dunia</strong>. Jangan pilih KTD biasa! Begitu ada kata <strong>meninggal dunia</strong>, sesuai baris terakhir Slide 18 jawabannya wajib <strong>Kejadian Sentinel</strong>.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d1','slides_bdt_kul3/slide_18.jpg','Slide 18 · Definisi Resmi 5 Insiden (KTD, KNC, KTC, KPC, Sentinel)',this)">Slide 18</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d1','slides_bdt_kul3/slide_19.jpg','Slide 19 · Prinsip Utama: Do No Harm',this)">Slide 19</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d1','slides_bdt_kul3/slide_20.jpg','Slide 20 · 4 Tujuan Patient Safety di RS',this)">Slide 20</button>
              </div>
            </div>
            <img id="dock-img-d1" src="slides_bdt_kul3/slide_18.jpg" alt="Slide 18" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d1').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d1">Slide 18 · Definisi Resmi 5 Insiden</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- BENTO CHAPTER 02 -->
      <article id="ch-02" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 02 · Merangkum Slide 23–33 & Slide 60–68</span>
          <span class="badge badge-crimson">Keluar di 2 Soal Asli UAB BDT (No. 32 & 44)</span>
        </div>
        <h2>Pembeda 7 Standar vs 6 SKP vs 7 Langkah</h2>
        <p class="bento-sub">Di UAB BDT, dosen mengeluarkan 2 soal yang menanyakan <strong>"Yang termasuk 7 Standar Keselamatan Pasien adalah..."</strong>, lalu mengambil 4 opsi pengecohnya dari <strong>7 Langkah Menuju Keselamatan Pasien (Slide 61)</strong>.</p>

        <div class="bento-split">
          <div>
            <div class="table-scroll">
              <table>
                <thead>
                  <tr>
                    <th>7 Standar Keselamatan Pasien<br><small>Slide 23–24 · Ciri: KATA BENDA</small></th>
                    <th>6 Sasaran Keselamatan Pasien (SKP)<br><small>Slide 32–33 · Ciri: 6 Prosedur Klinis</small></th>
                    <th>7 Langkah Menuju Keselamatan Pasien<br><small>Slide 61 · Ciri: KATA KERJA AKTIF (Me-)</small></th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>1. <strong>Hak pasien</strong> <em>(UAB No. 44)</em></td>
                    <td>1. Ketepatan identifikasi pasien</td>
                    <td>1. Membangun kesadaran nilai keselamatan</td>
                  </tr>
                  <tr>
                    <td>2. Pendidikan bagi pasien & keluarga</td>
                    <td>2. Peningkatan komunikasi efektif</td>
                    <td>2. <strong>Memimpin dan mendukung staf</strong> <em>(Pengecoh!)</em></td>
                  </tr>
                  <tr>
                    <td>3. Keselamatan dlm kesinambungan layanan</td>
                    <td>3. Keamanan obat <em>High-Alert</em></td>
                    <td>3. Mengintegrasikan aktivitas kelola risiko</td>
                  </tr>
                  <tr>
                    <td>4. Metode peningkatan kinerja & evaluasi</td>
                    <td>4. Tepat-lokasi, prosedur, pasien operasi</td>
                    <td>4. <strong>Mengembangkan sistem pelaporan</strong> <em>(Pengecoh!)</em></td>
                  </tr>
                  <tr>
                    <td>5. <strong>Peran kepemimpinan</strong> <em>(UAB No. 32)</em></td>
                    <td>5. Pengurangan risiko infeksi (cuci tangan)</td>
                    <td>5. Melibatkan & berkomunikasi dgn pasien</td>
                  </tr>
                  <tr>
                    <td>6. Pendidikan staf ttg keselamatan pasien</td>
                    <td>6. Pengurangan risiko pasien jatuh</td>
                    <td>6. Belajar & berbagi pengalaman (RCA)</td>
                  </tr>
                  <tr>
                    <td>7. Komunikasi merupakan kunci bagi staf</td>
                    <td>— <em>(Hanya 6 Sasaran)</em></td>
                    <td>7. Mencegah cedera lewat sistem</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title emerald">Trik Cepat 3 Detik di Ruang Ujian</div>
                <div class="radar-col-text">Jika soal menanyakan <strong>7 Standar</strong>, langsung cari opsi yang diawali <strong>Kata Benda</strong>: <strong>"Hak pasien"</strong> atau <strong>"Peran kepemimpinan dalam meningkatkan keselamatan pasien"</strong>.</div>
              </div>
              <div>
                <div class="radar-col-title">Cara Mengenali Pengecoh 7 Langkah</div>
                <div class="radar-col-text">Semua poin <strong>7 Langkah (Slide 61)</strong> diawali kata kerja berawalan <strong>Me- / Belajar</strong>: <em>Membangun, Memimpin, Mengintegrasikan, Mengembangkan, Melibatkan, Mencegah</em>.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d2','slides_bdt_kul3/slide_23.jpg','Slide 23 · 7 Standar Keselamatan Pasien (Standar 1: Hak Pasien)',this)">Slide 23</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d2','slides_bdt_kul3/slide_24.jpg','Slide 24 · 7 Standar Keselamatan Pasien (Standar 5: Peran Kepemimpinan)',this)">Slide 24</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d2','slides_bdt_kul3/slide_61.jpg','Slide 61 · 7 Langkah Keselamatan Pasien (Dipakai Dosen Jadi Pengecoh!)',this)">Slide 61</button>
              </div>
            </div>
            <img id="dock-img-d2" src="slides_bdt_kul3/slide_23.jpg" alt="Slide 23" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d2').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d2">Slide 23 · 7 Standar Keselamatan Pasien</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- BENTO CHAPTER 03 -->
      <article id="ch-03" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 03 · Merangkum Slide 32, 34–38</span>
          <span class="badge badge-crimson">Keluar di Soal UAB BDT-1 Hal. 5</span>
        </div>
        <h2>SKP 1: Ketepatan Identifikasi & 4 Warna Gelang</h2>
        <p class="bento-sub">Wajib memverifikasi minimal <strong>2 dari 4 identitas resmi</strong> (Nama lengkap, Tanggal lahir, Nomor RM, NIK). <strong>Dilarang keras</strong> menggunakan nomor kamar atau nomor tempat tidur.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Gelang Biru</div>
                <div class="tile-title">Pasien Laki-Laki</div>
                <div class="tile-body">Identitas pasien rawat inap laki-laki (dipasang saat admisi).</div>
              </div>
              <div class="step-tile">
                <div class="tile-kicker">Gelang Pink</div>
                <div class="tile-title">Pasien Perempuan</div>
                <div class="tile-body">Identitas pasien rawat inap perempuan.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Gelang Merah</div>
                <div class="tile-title">Alergi Tinggi</div>
                <div class="tile-body">Penanda alergi obat / makanan / lateks derajat berat.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Gelang Kuning</div>
                <div class="tile-title">Risiko Jatuh</div>
                <div class="tile-body">Pasien berisiko jatuh tinggi (Skala Morse / Humpty Dumpty).</div>
              </div>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title emerald">4 Momen Wajib Identifikasi (Slide 37)</div>
                <div class="radar-col-text">Sebelum: (1) Pemberian obat, (2) Transfusi darah/produk darah, (3) Pengambilan sampel darah/spesimen lab, (4) Tindakan invasif & operasi.</div>
              </div>
              <div>
                <div class="radar-col-title">Verifikasi Verbal Terbuka (Slide 34)</div>
                <div class="radar-col-text">Wajib bertanya aktif: <strong>"Siapa nama Bapak?"</strong> (✓). Jangan bertanya pasif/tertutup: <em>"Apakah Bapak Tn. Budi?"</em> (✗).</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d3','slides_bdt_kul3/slide_35.jpg','Slide 35 · Foto Gelang Merah (Alergi), Kuning (Jatuh), dan Biru (Laki-laki)',this)">Slide 35</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d3','slides_bdt_kul3/slide_34.jpg','Slide 34 · Aturan 2 Identitas & Pertanyaan Terbuka',this)">Slide 34</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d3','slides_bdt_kul3/slide_37.jpg','Slide 37 · 4 Momen Wajib Identifikasi Pasien',this)">Slide 37</button>
              </div>
            </div>
            <img id="dock-img-d3" src="slides_bdt_kul3/slide_35.jpg" alt="Slide 35" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d3').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d3">Slide 35 · Foto 3 Gelang Pasien</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- BENTO CHAPTER 04 -->
      <article id="ch-04" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 04 · Merangkum Slide 39–42</span>
          <span class="badge badge-cobalt">SKP 2 · Komunikasi Tim Medis</span>
        </div>
        <h2>SKP 2: Komunikasi Efektif (TBaK & SBAR)</h2>
        <p class="bento-sub">Instruksi lisan atau via telepon sangat rawan salah dengar nama obat (LASA) dan dosis. Wajib menggunakan siklus <strong>TBaK (Tulis Lengkap – Baca Ulang – Konfirmasi 1x24 Jam)</strong>.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile">
                <div class="tile-kicker">Langkah 1 · Tulis</div>
                <div class="tile-title">Write Down</div>
                <div class="tile-body">Penerima instruksi mencatat lengkap nama obat, dosis, rute, & frekuensi di rekam medis.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Langkah 2 · Baca Ulang</div>
                <div class="tile-title">Read Back & Eja</div>
                <div class="tile-body">Membacakan ulang catatan; untuk obat <em>Sound-Alike</em> wajib dieja huruf demi huruf.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Langkah 3 · Paraf</div>
                <div class="tile-title">Konfirmasi 1x24 Jam</div>
                <div class="tile-body">DPJP wajib menandatangani kotak stempel <strong>NOTASI</strong> maksimal dalam 1x24 jam.</div>
              </div>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title emerald">Metode Pelaporan SBAR (Slide 41)</div>
                <div class="radar-col-text"><strong>S</strong>ituation (masalah saat ini) → <strong>B</strong>ackground (riwayat klinis) → <strong>A</strong>ssessment (tanda vital & lab) → <strong>R</strong>ecommendation (usulan terapi ke DPJP).</div>
              </div>
              <div>
                <div class="radar-col-title">Syarat Resep Lengkap (Slide 42)</div>
                <div class="radar-col-text">Wajib mencantumkan: Nama pasien, Tanggal/jam resep, Nama obat, Dosis & satuan (mg/unit), Rute pemberian, serta Frekuensi/durasi.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d4','slides_bdt_kul3/slide_41.jpg','Slide 41 · Lembar SBAR & Stempel Notasi Verifikasi DPJP',this)">Slide 41</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d4','slides_bdt_kul3/slide_42.jpg','Slide 42 · Syarat Medication Order Lengkap',this)">Slide 42</button>
              </div>
            </div>
            <img id="dock-img-d4" src="slides_bdt_kul3/slide_41.jpg" alt="Slide 41" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d4').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d4">Slide 41 · Rekam Medis SBAR & Notasi</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- BENTO CHAPTER 05 -->
      <article id="ch-05" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 05 · Merangkum Slide 43–50</span>
          <span class="badge badge-crimson">Keluar di Soal Remidi BDT No. 39</span>
        </div>
        <h2>SKP 3: Keamanan Obat High-Alert & Elektrolit Pekat</h2>
        <p class="bento-sub">Obat <strong>High-Alert</strong> adalah obat yang berisiko tinggi menyebabkan kematian/cedera berat bila terjadi kesalahan. Meliputi: <strong>Elektrolit Konsentrat Pekat</strong>, <strong>Obat LASA (NORUM)</strong>, dan <strong>Heparin/Insulin/Kemoterapi</strong>.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Elektrolit Pekat #1</div>
                <div class="tile-title">KCl Pekat (≥2 mEq/mL)</div>
                <div class="tile-body"><em>Concentrated Potassium Chloride</em>. Bolus IV langsung memicu henti jantung fatal (Sentinel).</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Elektrolit Pekat #2–4</div>
                <div class="tile-title">NaCl >0,9% & MgSO4</div>
                <div class="tile-body">Mencakup Glukosa Hipertonik ≥20%, MgSO4 ≥20%, Natrium Bikarbonat, & Heparin pekat.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Aturan Penyimpanan</div>
                <div class="tile-title">Tarik dari Bangsal!</div>
                <div class="tile-body">Dilarang disimpan di ruang rawat biasa; wajib di Instalasi Farmasi / troli emergensi terkunci.</div>
              </div>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title">Bedah Soal Remidi BDT No. 39 (Slide 48)</div>
                <div class="radar-col-text">Pertanyaan: <em>"Label apakah yang wajib dipasang pada Concentrated Potassium Chloride?"</em><br>Lihat gambar botol di <strong>Slide 48</strong>: pada badan botol tertulis besar <strong>HIGH ALERT! MEDICATION</strong>. Dosen mengambil kata <em>Distinct</em>, <em>Warning</em>, dan <em>Harmful</em> dari kotak keterangan biru di sekeliling botol sebagai pengecoh!</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d5','slides_bdt_kul3/slide_48.jpg','Slide 48 · Botol HIGH ALERT! MEDICATION (Sumber Soal Remidi No. 39)',this)">Slide 48</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d5','slides_bdt_kul3/slide_46.jpg','Slide 46 · Daftar Cairan High Concentration (KCl, Heparin, NaCl)',this)">Slide 46</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d5','slides_bdt_kul3/slide_47.jpg','Slide 47 · 5 Langkah Mengurangi Risiko High-Alert',this)">Slide 47</button>
              </div>
            </div>
            <img id="dock-img-d5" src="slides_bdt_kul3/slide_48.jpg" alt="Slide 48" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d5').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d5">Slide 48 · Botol HIGH ALERT! MEDICATION</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- BENTO CHAPTER 06 -->
      <article id="ch-06" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 06 · Merangkum Slide 51–54</span>
          <span class="badge badge-crimson">Keluar di UAB BDT Axonation No. 43</span>
        </div>
        <h2>SKP 4: Tepat Lokasi, Prosedur, & Pasien Operasi</h2>
        <p class="bento-sub">Protokol wajib untuk mencegah salah sisi/lokasi operasi (<em>Wrong-Site Surgery</em>): <strong>Surgical Marking</strong> di ruang rawat dan <strong>Surgical Time-Out</strong> di meja operasi.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile">
                <div class="tile-kicker">1 · Sebelum Ke OK</div>
                <div class="tile-title">Surgical Marking</div>
                <div class="tile-body">Penandaan lokasi oleh dokter operator dengan <strong>melibatkan pasien saat masih sadar</strong>.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">2 · Tepat Sebelum Insisi</div>
                <div class="tile-title">Surgical Time-Out</div>
                <div class="tile-body">Jeda verifikasi aktif seluruh tim (bedah, anestesi, perawat) <strong>tepat sebelum insisi kulit</strong>.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">3 · Penyebab Error #1</div>
                <div class="tile-title">Komunikasi Tim Buruk</div>
                <div class="tile-body">Tertulis urutan #1 di Slide 54: <strong>Komunikasi yang tidak efektif antara anggota tim bedah</strong>.</div>
              </div>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title">Bedah Soal UAB BDT Axonation No. 43 (Slide 54)</div>
                <div class="radar-col-text">Kasus pasien dijadwalkan operasi thoraks tetapi tungkai kaki ikut dioperasi. Sesuai <strong>Slide 54 baris ke-1</strong>, penyebab utamanya adalah <strong>komunikasi tidak efektif antar tim medis/bedah</strong>.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d6','slides_bdt_kul3/slide_54.jpg','Slide 54 · Causes of Surgical Errors (Sumber Soal UAB No. 43)',this)">Slide 54</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d6','slides_bdt_kul3/slide_51.jpg','Slide 51 · 6 Ceklis Verifikasi & Time-Out Sebelum Operasi',this)">Slide 51</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d6','slides_bdt_kul3/slide_52.jpg','Slide 52 · Prosedur Surgical Timeout',this)">Slide 52</button>
              </div>
            </div>
            <img id="dock-img-d6" src="slides_bdt_kul3/slide_54.jpg" alt="Slide 54" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d6').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d6">Slide 54 · Causes of Surgical Errors</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- BENTO CHAPTER 07 -->
      <article id="ch-07" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 07 · Merangkum Slide 55–59 & Slide 69–80</span>
          <span class="badge badge-crimson">Keluar di UAB 22 No. 85 & Remidi Costa No. 36</span>
        </div>
        <h2>SKP 5–6, Pelaporan 2x24 Jam, Grading Risiko & RCA</h2>
        <p class="bento-sub">Semua insiden (KNC, KTD, Sentinel) wajib dilaporkan secara internal ke Tim KPRS maksimal <strong>2 x 24 jam</strong>. Metode investigasinya ditentukan oleh <strong>Warna Grading Risiko</strong>:</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile">
                <div class="tile-kicker">SKP 5 · Infeksi</div>
                <div class="tile-title">5 Moments Cuci Tangan</div>
                <div class="tile-body">2 Sebelum (kontak pasien & tindakan aseptik) + 3 Sesudah (cairan tubuh, kontak pasien, lingkungan pasien) + Injeksi <em>single-use</em>.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Grading Biru & Hijau</div>
                <div class="tile-title">Investigasi Sederhana</div>
                <div class="tile-body">Dilakukan oleh atasan langsung unit kerja (Biru maks. 1 minggu, Hijau maks. 2 minggu).</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Grading Kuning & Merah</div>
                <div class="tile-title">Root Cause Analysis (RCA)</div>
                <div class="tile-body">Analisis akar masalah sistemik secara komprehensif oleh Tim KPRS (maksimal <strong>45 hari</strong>).</div>
              </div>
            </div>

            <div class="exam-radar">
              <div>
                <div class="radar-col-title">Bedah Soal UAB 22 No. 85 (Slide 69 & 75)</div>
                <div class="radar-col-text">Pasien jatuh dari brankar saat ditransfer dari UGD ke Kamar Operasi. Tim RS melakukan investigasi mendalam untuk mencari akar masalah agar tidak terulang. Metode tersebut adalah <strong>Root Cause Analysis (RCA)</strong>.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('d7','slides_bdt_kul3/slide_69.jpg','Slide 69 · Alur Pelaporan Insiden 2x24 Jam, Grading & RCA',this)">Slide 69</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d7','slides_bdt_kul3/slide_71.jpg','Slide 71 · Formulir Laporan Insiden Internal (Maks 2x24 Jam)',this)">Slide 71</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d7','slides_bdt_kul3/slide_73.jpg','Slide 73 · Grading Risiko: Biru, Hijau, Kuning, Merah',this)">Slide 73</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('d7','slides_bdt_kul3/slide_75.jpg','Slide 75 · Prinsip Analisis Akar Penyebab Masalah (RCA)',this)">Slide 75</button>
              </div>
            </div>
            <img id="dock-img-d7" src="slides_bdt_kul3/slide_69.jpg" alt="Slide 69" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d7').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d7">Slide 69 · Pelaporan 2x24 Jam & RCA</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

    </div>

    <!-- =================================================================== -->
    <!-- VIEW 2: 9 SOAL ASLI UAB & REMIDI BDT                                -->
    <!-- =================================================================== -->
    <div id="view-soal" class="view-section">
      <div class="cbt-header-bar">
        <span class="cbt-score-pill" id="cbt-score-pill">Skor Anda: 0/9 Benar (0 Dijawab)</span>
        <div class="cbt-filters">
          <button type="button" class="cbt-filter-btn active" onclick="filterCBT('all', this)">Semua Soal (9)</button>
          <button type="button" class="cbt-filter-btn" onclick="filterCBT('uab', this)">Soal Asli UAB BDT (7)</button>
          <button type="button" class="cbt-filter-btn" onclick="filterCBT('remidi', this)">Soal Remidi BDT (2)</button>
          <button type="button" class="cbt-filter-btn" onclick="clearQuiz()">Reset Jawaban</button>
        </div>
      </div>

      <div id="cbt-list"></div>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 3: CEK CEPAT H-1 UJIAN (ACTIVE RECALL CARDS)                   -->
    <!-- =================================================================== -->
    <div id="view-flash" class="view-section">
      <div class="flash-grid">
        <div class="flash-unit">
          <div>
            <span class="badge badge-crimson">Slide 18 · Sering Keluar</span>
            <div class="flash-q">1. Apa pembeda mutlak KPC, KNC, KTC, KTD, dan Sentinel?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">
            • <strong>KPC</strong>: Kondisi berpotensi cedera, belum ada insiden.<br>
            • <strong>KNC</strong>: Salah tindakan, tapi BELUM kena pasien.<br>
            • <strong>KTC</strong>: SUDAH kena pasien, tapi TIDAK cedera.<br>
            • <strong>KTD</strong>: SUDAH kena pasien dan TIMBUL cedera.<br>
            • <strong>Sentinel</strong>: KTD berujung KEMATIAN / cacat permanen.
          </div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-crimson">Slide 23–24 vs 61 · Jebakan Utama</span>
            <div class="flash-q">2. Bagaimana cara membedakan opsi soal "7 Standar" vs "7 Langkah" dalam 5 detik?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">
            • <strong>7 Standar (Slide 23–24)</strong> diawali KATA BENDA: <em>"Hak pasien"</em>, <em>"Peran kepemimpinan..."</em>.<br>
            • <strong>7 Langkah (Slide 61)</strong> diawali KATA KERJA AKTIF: <em>"Membangun..."</em>, <em>"Memimpin..."</em>, <em>"Mengembangkan..."</em>.
          </div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-emerald">Slide 34–35 · SKP 1</span>
            <div class="flash-q">3. Sebutkan arti 4 warna gelang pasien dan 4 identitas resmi!</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">
            • Gelang: <strong>Biru</strong> (Laki-laki), <strong>Pink</strong> (Perempuan), <strong>Merah</strong> (Alergi), <strong>Kuning</strong> (Risiko Jatuh).<br>
            • Minimal 2 dari 4 identitas: Nama lengkap, Tanggal lahir, No. RM, NIK (Dilarang pakai nomor kamar!).
          </div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-amber">Slide 46–48 · SKP 3</span>
            <div class="flash-q">4. Apa label resmi untuk botol Concentrated Potassium Chloride (KCl pekat)?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">
            • Label resmi: <strong>HIGH ALERT! MEDICATION</strong> (Slide 48).<br>
            • Wajib ditarik dari ruang rawat biasa dan hanya disimpan di Instalasi Farmasi / troli emergensi terkunci.
          </div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-cobalt">Slide 51–54 · SKP 4</span>
            <div class="flash-q">5. Apa penyebab #1 kesalahan lokasi operasi (Wrong-Site Surgery) menurut Slide 54?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">
            • Urutan #1 di Slide 54: <strong>Komunikasi yang tidak efektif antara anggota tim bedah</strong>.<br>
            • Pencegahan: Surgical Marking (melibatkan pasien sadar) + Surgical Time-Out tepat sebelum insisi.
          </div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-crimson">Slide 69–75 · Pelaporan & RCA</span>
            <div class="flash-q">6. Berapa batas waktu lapor insiden internal, dan kapan dipakai RCA vs Investigasi Sederhana?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">
            • Lapor internal maksimal <strong>2 x 24 jam</strong>.<br>
            • Grading Biru/Hijau = Investigasi Sederhana (1–2 minggu).<br>
            • Grading Kuning/Merah = <strong>Root Cause Analysis / RCA</strong> (maksimal 45 hari).
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- ZOOM MODAL -->
  <div id="zoom-modal" class="modal-overlay" onclick="closeZoom()">
    <div class="modal-window" onclick="event.stopPropagation()">
      <div class="modal-top">
        <strong id="zoom-title">Bukti Slide Asli Dosen</strong>
        <button type="button" class="cmdk-trigger" onclick="closeZoom()">Tutup (ESC)</button>
      </div>
      <img id="zoom-img" src="slides_bdt_kul3/slide_18.jpg" alt="Slide Zoom" />
    </div>
  </div>

  <!-- CMD+K MODAL -->
  <div id="search-modal" class="modal-overlay" onclick="closeSearchModal()">
    <div class="cmdk-box" onclick="event.stopPropagation()">
      <div class="cmdk-bar">
        <input type="text" id="cmdk-inp" class="cmdk-input" placeholder="Ketik kata kunci soal UAB / slide (contoh: Sentinel, KCl, Gelang, B12, Metformin)..." oninput="execSearch()" />
        <button type="button" class="cmdk-trigger" onclick="closeSearchModal()">ESC</button>
      </div>
      <div id="cmdk-out" class="cmdk-results"></div>
    </div>
  </div>

  <script src="vendor/uab_search_data.js"></script>
  <script>
    window.MOD_KEY = 'bdt_kul3_supahero';
    window.QUIZ_DATA = [
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 29',
        slide: 'slides_bdt_kul3/slide_18.jpg',
        slideCap: 'Bukti Slide 18 · Definisi Kejadian Sentinel',
        stem: 'Seorang perempuan berusia 35 tahun datang ke klinik pratama dengan keluhan nyeri perut. Dokter memberikan suntikan Antalgin untuk mengatasi rasa sakitnya. Beberapa menit kemudian pasien mengalami syok anafilaktik dan meninggal dunia. Termasuk insiden keselamatan pasien manakah kejadian tersebut?',
        opts: ['Kejadian Potensial Cedera (KPC)', 'Kejadian Nyaris Cedera (KNC)', 'Kejadian Tidak Cedera (KTC)', 'Kejadian Tidak Diharapkan (KTD)', 'Kejadian Sentinel'],
        ans: 4,
        exp: '<strong>Kunci: E (Kejadian Sentinel).</strong> Sesuai Slide 18 baris terakhir, <em>Kejadian Sentinel adalah suatu KTD yang mengakibatkan kematian atau cedera yang serius</em>. Karena pasien meninggal dunia pasca-injeksi, insiden ini masuk kategori Sentinel.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · UAB 22 No. 70',
        slide: 'slides_bdt_kul3/slide_18.jpg',
        slideCap: 'Bukti Slide 18 · Sentinel vs KTD',
        stem: 'Pasien datang ke IGD karena nyeri kolik abdomen akut. Setelah diberikan injeksi analgetik, pasien mengalami henti jantung akibat reaksi anafilaksis berat dan dinyatakan meninggal. Kategori insiden keselamatan pasien pada kasus ini adalah...',
        opts: ['Kejadian Tidak Diharapkan (KTD)', 'Kejadian Sentinel', 'Kejadian Nyaris Cedera (KNC)', 'Kejadian Potensial Cedera (KPC)', 'Kejadian Tidak Cedera (KTC)'],
        ans: 1,
        exp: '<strong>Kunci: B (Kejadian Sentinel).</strong> Setiap KTD yang berujung kematian mendadak di luar perjalanan alamiah penyakit wajib diklasifikasikan sebagai Kejadian Sentinel (Slide 18).'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT-1 · Hal. 9–10',
        slide: 'slides_bdt_kul3/slide_18.jpg',
        slideCap: 'Bukti Slide 18 · Definisi KNC (Belum Terpapar ke Pasien)',
        stem: 'Dokter meresepkan obat dengan dosis yang salah akibat kelelahan. Petugas farmasi telah menyiapkan obat tersebut, namun perawat ruangan menyadari ketidaksesuaian dosis saat melakukan pengecekan ulang sehingga obat batal diberikan kepada pasien. Disebut apakah insiden ini?',
        opts: ['Kejadian Potensial Cedera (KPC)', 'Kejadian Nyaris Cedera (KNC)', 'Kejadian Tidak Cedera (KTC)', 'Kejadian Tidak Diharapkan (KTD)', 'Kejadian Sentinel'],
        ans: 1,
        exp: '<strong>Kunci: B (KNC / Near Miss).</strong> Sesuai Slide 18: <em>KNC adalah terjadinya insiden yang belum sampai terpapar ke pasien</em>.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 32',
        slide: 'slides_bdt_kul3/slide_24.jpg',
        slideCap: 'Bukti Slide 24 · Standar 5: Peran Kepemimpinan',
        stem: 'Manakah di bawah ini yang termasuk dalam 7 Standar Keselamatan Pasien Rumah Sakit?',
        opts: [
          'Membangun kesadaran akan nilai keselamatan pasien',
          'Memimpin dan mendukung staf dalam keselamatan pasien',
          'Peran kepemimpinan dalam meningkatkan keselamatan pasien',
          'Mengembangkan sistem pelaporan insiden keselamatan pasien',
          'Mengintegrasikan aktivitas pengelolaan risiko'
        ],
        ans: 2,
        exp: '<strong>Kunci: C (Peran kepemimpinan dalam meningkatkan keselamatan pasien).</strong> Sesuai Slide 24 baris pertama, poin ke-5 dari 7 Standar Keselamatan Pasien adalah <em>Peran kepemimpinan dalam meningkatkan keselamatan pasien</em>. Opsi A, B, D, E diambil dari Slide 61 (7 Langkah).'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 44',
        slide: 'slides_bdt_kul3/slide_23.jpg',
        slideCap: 'Bukti Slide 23 · Standar 1: Hak Pasien',
        stem: 'Standar keselamatan pasien rumah sakit merupakan acuan bagi fasyankes untuk melaksanakan pelayanannya. Yang termasuk dalam 7 Standar Keselamatan Pasien adalah...',
        opts: [
          'Hak pasien',
          'Ketepatan identifikasi pasien',
          'Peningkatan keamanan obat yang perlu diwaspadai',
          'Pengurangan risiko infeksi terkait pelayanan kesehatan',
          'Membangun kesadaran akan nilai keselamatan pasien'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Hak pasien).</strong> Sesuai Slide 23 poin pertama, <em>Hak Pasien</em> adalah Standar ke-1 dari 7 Standar Keselamatan Pasien.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT-1 · Hal. 5 & 14',
        slide: 'slides_bdt_kul3/slide_35.jpg',
        slideCap: 'Bukti Slide 32 & 35 · SKP 1 Identifikasi & Gelang Biru',
        stem: 'Seorang pasien laki-laki berusia 58 tahun dirawat di bangsal paru dengan diagnosis pneumonia. Karena petugas admisi sibuk, pasien belum dipasangkan gelang identitas berwarna biru sehingga saat pemberian antibiotik injeksi, obat pasien tertukar dengan pasien di sebelah tempat tidurnya. Sasaran Keselamatan Pasien (SKP) manakah yang dilanggar?',
        opts: [
          'Ketepatan identifikasi pasien',
          'Peningkatan komunikasi yang efektif',
          'Peningkatan keamanan obat yang perlu diwaspadai',
          'Kepastian tepat-lokasi, tepat-prosedur, tepat-pasien operasi',
          'Pengurangan risiko infeksi terkait pelayanan kesehatan'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Ketepatan identifikasi pasien — SKP 1).</strong> Pemasangan gelang identitas (biru untuk laki-laki sesuai Slide 35) dan verifikasi minimal 2 identitas sebelum pemberian obat adalah inti dari SKP 1.'
      }},
      {{
        cat: 'remidi',
        source: 'Soal Asli Remidi BDT · No. 39',
        slide: 'slides_bdt_kul3/slide_48.jpg',
        slideCap: 'Bukti Slide 48 · Botol HIGH ALERT! MEDICATION',
        stem: 'Cairan elektrolit pekat seperti Concentrated Potassium Chloride (KCl) dapat menyebabkan kejadian fatal bila diberikan tanpa pengenceran. Berdasarkan standar keselamatan pasien, label apakah yang wajib dipasang pada obat tersebut?',
        opts: ['Distinct', 'High Alert', 'Warning', 'Harmful', 'Caution'],
        ans: 1,
        exp: '<strong>Kunci: B (High Alert).</strong> Lihat langsung gambar botol di <strong>Slide 48</strong>: pada badan botol tertulis <em>HIGH ALERT! MEDICATION</em>. Dosen mengambil kata <em>Distinct</em>, <em>Warning</em>, dan <em>Harmful</em> dari kotak keterangan biru di sekeliling gambar botol pada Slide 48.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 43',
        slide: 'slides_bdt_kul3/slide_54.jpg',
        slideCap: 'Bukti Slide 54 · Causes of Surgical Errors (#1)',
        stem: 'Seorang pasien dijadwalkan menjalani operasi di daerah thoraks, namun saat selesai operasi ternyata bagian tungkai kaki pasien juga ikut dioperasi akibat kesalahpahaman instruksi di meja operasi. Berdasarkan materi Patient Safety, apakah penyebab utama terjadinya kesalahan bedah tersebut?',
        opts: [
          'Komunikasi tidak efektif antar tim medis / bedah',
          'Kurangnya fasilitas kamar operasi',
          'Efek samping obat anestesi',
          'Keluarga pasien terlambat menandatangani informed consent',
          'Tidak tersednya antibiotik profilaksis'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Komunikasi tidak efektif antar tim medis / bedah).</strong> Tertulis persis pada urutan nomor 1 di <strong>Slide 54 (Causes of Surgical Errors)</strong>: <em>1. Komunikasi yang tidak efektif antara anggota tim bedah</em>.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · UAB 22 No. 85 & Remidi Costa No. 36',
        slide: 'slides_bdt_kul3/slide_75.jpg',
        slideCap: 'Bukti Slide 69 & 75 · Root Cause Analysis (RCA)',
        stem: 'Seorang pasien terjatuh dari brankar saat proses transfer dari UGD menuju kamar operasi sehingga mengalami cedera kepala. Tim keselamatan pasien rumah sakit segera melakukan investigasi terstruktur untuk mencari akar penyebab sistemik agar kejadian serupa tidak terulang. Metode apakah yang digunakan tim tersebut?',
        opts: [
          'Root Cause Analysis (RCA)',
          'Failure Mode and Effects Analysis (FMEA)',
          'Audit Medis Internal',
          'Visum et Repertum',
          'Informed Consent'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Root Cause Analysis / RCA).</strong> Sesuai Slide 69 dan Slide 75, setiap insiden keselamatan pasien dengan derajat risiko Kuning/Merah dianalisis akar masalahnya menggunakan metode <strong>Root Cause Analysis (RCA)</strong>.'
      }}
    ];

    document.getElementById('cbt-list').innerHTML = window.QUIZ_DATA.map((q, idx) => `
      <article class="q-module" id="qm-${{idx}}" data-cat="${{q.cat}}">
        <div class="q-top">
          <span class="badge badge-crimson">${{q.source}}</span>
          <span class="ch-index">Soal #${{idx + 1}}</span>
        </div>
        <div class="q-stem-txt">${{q.stem}}</div>
        <div class="opt-stack">
          ${{q.opts.map((opt, oIdx) => `
            <button type="button" class="opt-row" onclick="pickAnswer(${{idx}}, ${{oIdx}})">
              <span class="opt-key">${{String.fromCharCode(65 + oIdx)}}.</span>
              <span>${{opt}}</span>
            </button>
          `).join('')}}
        </div>
        <div class="q-drawer" id="qd-${{idx}}">
          <div style="font-size:0.94rem;color:#263645;line-height:1.6;">${{q.exp}}</div>
          <div class="slide-dock">
            <img src="${{q.slide}}" alt="${{q.slideCap}}" class="dock-img" onclick="openZoom('${{q.slide}}', '${{q.slideCap}}')" />
            <div class="dock-foot"><span>${{q.slideCap}}</span><span>Zoom ↗</span></div>
          </div>
        </div>
      </article>
    `).join('');

    {SUPAHERO_JS}
  </script>
</body>
</html>
"""

# ==============================================================================
# 2. EMN KUL 2 DEFISIENSI VITAMIN — SUPAHERO EDITION
# ==============================================================================
EMN_SUPAHERO = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VERTEX-PREP · EMN Kuliah 2: Defisiensi Vitamin (Supahero Edition)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
  <style>{SUPAHERO_CSS}</style>
</head>
<body>

  <!-- SUPAHERO FLOATING PILL NAVBAR -->
  <div class="supa-nav-wrap">
    <header class="supa-navbar">
      <div class="supa-brand">
        <span class="brand-dot">VX</span>
        <select class="course-switcher" aria-label="Pilih Kuliah" onchange="window.location.href=this.value">
          <option value="BDT_KUL3_Patient_Safety.html">Blok 7 BDT · Kuliah 3: Patient Safety (dr. Riskiyah)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html" selected>Blok 9 EMN · Kuliah 2: Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
        </select>
      </div>

      <nav class="supa-pills" aria-label="Mode Belajar">
        <button type="button" class="supa-pill-btn active" onclick="switchView('materi', this)">6 Bab Visual (Pengganti PPT)</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('soal', this)">6 Soal Kasus Slide & Prediksi</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('flash', this)">Cek Cepat H-1 Ujian</button>
      </nav>

      <div class="supa-actions">
        <button type="button" class="cmdk-trigger" onclick="openSearchModal()">
          <span>Cari 51 File UAB</span>
          <kbd>⌘K</kbd>
        </button>
      </div>
    </header>
  </div>

  <main class="shell">

    <div id="view-materi" class="view-section active">

      <!-- SUPAHERO SPLIT-SCREEN HERO -->
      <section class="supa-hero">
        <div>
          <h1>Kuasai 28 Slide Defisiensi Vitamin Tanpa Buka PPT.</h1>
          <div class="hero-meta-line">Blok 9 EMN · Kuliah Pakar 2 · dr. Iwal Reza Ahdi, Sp.PD</div>
          <p class="hero-lead">Seluruh <strong>28 slide dr. Iwal Reza Ahdi, Sp.PD</strong> (Vitamin Larut Lemak A, D, E, K & Larut Air B1–B12, C) telah dipadatkan menjadi <strong>6 Modul Bento Visual</strong> beserta pembeda laboratorium dan 3 kasus diskusi asli slide dosen.</p>

          <div class="hero-cta-row">
            <a href="#emn-01" class="btn-primary">Mulai Pelajari 6 Bab Visual ↓</a>
            <button type="button" class="btn-secondary" onclick="jumpToQuiz()">Kerjakan 6 Soal Latihan →</button>
          </div>

          <div class="hero-stats-row">
            <div class="stat-unit">
              <span class="stat-num">28 → 6 Bab</span>
              <span class="stat-lbl">Pemadatan Materi Utuh</span>
            </div>
            <div class="stat-unit">
              <span class="stat-num">3 Kasus Slide</span>
              <span class="stat-lbl">Kasus Diskusi Asli dr. Iwal</span>
            </div>
            <div class="stat-unit">
              <span class="stat-num">100% Jujur</span>
              <span class="stat-lbl">0 Klaim Palsu Soal UAB EMN</span>
            </div>
          </div>
        </div>

        <div class="hero-showcase">
          <div class="window-bar">
            <div class="window-dots">
              <span class="w-dot"></span><span class="w-dot"></span><span class="w-dot"></span>
            </div>
            <span class="window-tag">Bukti Slide #17 · Pembeda B9 vs B12</span>
          </div>
          <img src="slides_kul2/slide_17.jpg" alt="Bukti Slide 17 Folat vs B12" class="hero-slide-preview" onclick="openZoom('slides_kul2/slide_17.jpg', 'Slide 17 · Tabel Pembeda Defisiensi Folat (B9) vs Kobalamin (B12)')" />
          <div class="showcase-caption">
            <span>Slide 17 Asli dr. Iwal (MMA naik spesifik pada defisiensi B12)</span>
            <span>Klik untuk Zoom ↗</span>
          </div>
        </div>
      </section>

      <div class="chapter-ribbon">
        <a href="#emn-01" class="chapter-chip">01 · 4 Jalur Etiologi & Obat</a>
        <a href="#emn-02" class="chapter-chip">02 · Vitamin A (Mata & Epitel)</a>
        <a href="#emn-03" class="chapter-chip">03 · Vitamin D, E, & K</a>
        <a href="#emn-04" class="chapter-chip">04 · Vitamin B1, B2, B3, B6</a>
        <a href="#emn-05" class="chapter-chip">05 · Pembeda B9 (Folat) vs B12</a>
        <a href="#emn-06" class="chapter-chip">06 · Pembeda Skorbut (Vit C) vs Vit K</a>
      </div>

      <!-- EMN BAB 1 -->
      <article id="emn-01" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 01 · Merangkum Slide 1–7</span>
          <span class="badge badge-emerald">Fondasi Klinis & Interaksi Obat</span>
        </div>
        <h2>4 Jalur Penyebab Defisiensi & Interaksi Obat Khas</h2>
        <p class="bento-sub">Defisiensi vitamin selalu berawal dari salah satu dari 4 mekanisme berikut: kurang asupan, malabsorpsi GI/hepatobilier, lonjakan kebutuhan fisiologis, atau interaksi obat kronik.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile">
                <div class="tile-kicker">01 · Asupan</div>
                <div class="tile-title">Diet & Alkohol</div>
                <div class="tile-body">Diet sangat restriktif, vegan murni tanpa fortifikasi (B12), kemiskinan, alkoholisme kronik (B1).</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">02 · Absorpsi</div>
                <div class="tile-title">Ileum & Empedu</div>
                <div class="tile-body">Celiac, reseksi ileum terminal / Crohn (B12), operasi bariatrik, kolestasis (Vit A, D, E, K).</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">03 · Kebutuhan</div>
                <div class="tile-title">Hamil & Tumbuh</div>
                <div class="tile-body">Kehamilan & laktasi (kebutuhan Folat/B9 melonjak), masa pertumbuhan, penyakit kritis.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">04 · Interaksi Obat</div>
                <div class="tile-title">3 Obat Wajib Hafal</div>
                <div class="tile-body"><strong>Metformin → Def. B12</strong><br><strong>Isoniazid (INH) → Def. B6</strong><br><strong>Warfarin → Antagonis Vit K</strong></div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('e1','slides_kul2/slide_5.jpg','Slide 5 · Empat Jalur Menuju Defisiensi & Interaksi Obat',this)">Slide 5</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e1','slides_kul2/slide_6.jpg','Slide 6 · Algoritma 4 Langkah: Curiga → Uji → Tangani',this)">Slide 6</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e1','slides_kul2/slide_3.jpg','Slide 3 · Kasus Pemicu: Metformin & MCV 112 fL',this)">Slide 3</button>
              </div>
            </div>
            <img id="dock-img-e1" src="slides_kul2/slide_5.jpg" alt="Slide 5" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-e1').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-e1">Slide 5 · Empat Jalur Defisiensi</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- EMN BAB 2 -->
      <article id="emn-02" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 02 · Merangkum Slide 8 & 19</span>
          <span class="badge badge-cobalt">Vitamin Larut Lemak · Mata & Epitel</span>
        </div>
        <h2>Vitamin A: Siklus Visual (Retinal) & Epitel (Retinoat)</h2>
        <p class="bento-sub">Bedakan fungsi 2 metabolit aktif Vitamin A: <strong>Retinal</strong> menyusun pigmen rodopsin di sel batang retina (penglihatan gelap), sedangkan <strong>Asam Retinoat</strong> mengatur diferensiasi epitel mukosa.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Tahap 1 · Paling Dini</div>
                <div class="tile-title">Nyctalopia</div>
                <div class="tile-body">Rabun senja akibat terganggunya regenerasi rodopsin di retina.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Tahap 2 · Metaplasia</div>
                <div class="tile-title">Xerophthalmia & Bitot</div>
                <div class="tile-body">Kekeringan konjungtiva disertai bercak putih keperakan berbusa (<strong>Bercak Bitot</strong>).</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Tahap 3 · Darurat</div>
                <div class="tile-title">Keratomalasia</div>
                <div class="tile-body">Pelunakan & nekrosis kornea yang berujung kebutaan permanen.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('e2','slides_kul2/slide_8.jpg','Slide 8 · Vitamin A: Penglihatan, Epitel, & Foto Bercak Bitot',this)">Slide 8</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e2','slides_kul2/slide_19.jpg','Slide 19 · Tabel Ringkasan Vitamin Larut Lemak (A, D, E, K)',this)">Slide 19</button>
              </div>
            </div>
            <img id="dock-img-e2" src="slides_kul2/slide_8.jpg" alt="Slide 8" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-e2').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-e2">Slide 8 · Vitamin A & Bercak Bitot</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- EMN BAB 3 -->
      <article id="emn-03" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 03 · Merangkum Slide 9, 10, 19</span>
          <span class="badge badge-amber">Vitamin Larut Lemak · D, E, & K</span>
        </div>
        <h2>Vitamin D (Tulang), E (Antioksidan), & K (Koagulasi)</h2>
        <p class="bento-sub">Perhatikan perbedaan antara bentuk biologis aktif Vitamin D (`1,25-(OH)2-D`) dan parameter laboratorium untuk memeriksa status Vitamin D (`25(OH)D`):</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">1 · Hati (25-OHase)</div>
                <div class="tile-title">25(OH)D = Parameter Lab!</div>
                <div class="tile-body">Kalsidiol (`25(OH)D`) memiliki waktu paruh panjang dan menjadi <strong>baku emas penanda status Vitamin D</strong> di darah.</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">2 · Ginjal (1α-OHase)</div>
                <div class="tile-title">1,25-(OH)2-D = Aktif!</div>
                <div class="tile-body">Kalsitriol bekerja meningkatkan absorpsi Ca & P. Defisiensi pada anak = <strong>Rakitis</strong>; pada dewasa = <strong>Osteomalasia</strong>.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">3 · Vit E & Vit K</div>
                <div class="tile-title">Saraf vs Koagulasi</div>
                <div class="tile-body"><strong>Vit E</strong>: antioksidan → defisiensi: ataksia/neuropati.<br><strong>Vit K</strong>: Faktor II, VII, IX, X → defisiensi: <strong>PT/INR memanjang</strong>.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('e3','slides_kul2/slide_9.jpg','Slide 9 · Jalur Aktivasi Vitamin D & Rakitis vs Osteomalasia',this)">Slide 9</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e3','slides_kul2/slide_10.jpg','Slide 10 · Vitamin E (Antioksidan) & Vitamin K (Koagulasi)',this)">Slide 10</button>
              </div>
            </div>
            <img id="dock-img-e3" src="slides_kul2/slide_9.jpg" alt="Slide 9" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-e3').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-e3">Slide 9 · Aktivasi Vitamin D</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- EMN BAB 4 -->
      <article id="emn-04" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 04 · Merangkum Slide 11, 12, 13, 25</span>
          <span class="badge badge-crimson">Keluar di Kasus Diskusi Slide 25</span>
        </div>
        <h2>Vitamin B1 (Tiamin), B2, B3 (Pellagra), & B6</h2>
        <p class="bento-sub">Setiap vitamin B memiliki sindrom defisiensi klasik yang sangat khas di soal vignette:</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Vit B1 · Tiamin (TPP)</div>
                <div class="tile-title">Beriberi & Wernicke</div>
                <div class="tile-body">Kofaktor PDH, α-KGDH, Transketolase. Defisiensi: <strong>Beriberi kering</strong> (neuropati), <strong>Beriberi basah</strong> (gagal jantung edema), <strong>Ensefalopati Wernicke</strong>.</div>
              </div>
              <div class="step-tile">
                <div class="tile-kicker">Vit B2 · Riboflavin</div>
                <div class="tile-title">Lesi Mukokutan</div>
                <div class="tile-body">Kofaktor FMN/FAD. Defisiensi: <em>Angular cheilitis</em> (fisura sudut bibir), glositis magenta, dermatitis seboroik.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Vit B3 · Niasin</div>
                <div class="tile-title">Pellagra (Trias 3D)</div>
                <div class="tile-body">Kofaktor NAD+/NADP+. Defisiensi menyebabkan <strong>Pellagra</strong>: <em>Dermatitis</em> fotosensitif (Casal necklace), <em>Diare</em>, <em>Demensia</em>.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Vit B6 · Piridoksin</div>
                <div class="tile-title">Neuropati Obat TB (INH)</div>
                <div class="tile-body">Kofaktor PLP (sintesis GABA & heme). Defisiensi akibat <strong>Isoniazid (INH)</strong> → neuropati perifer & kejang.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('e4','slides_kul2/slide_11.jpg','Slide 11 · Vitamin B1 (Tiamin): Enzim TPP, Beriberi, & Wernicke',this)">Slide 11</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e4','slides_kul2/slide_13.jpg','Slide 13 · Vitamin B2, B3 (Pellagra & Casal Necklace), dan B6',this)">Slide 13</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e4','slides_kul2/slide_25.jpg','Slide 25 · Diskusi Kasus 2: Kebingungan Akut & Ataksia (Wernicke)',this)">Slide 25</button>
              </div>
            </div>
            <img id="dock-img-e4" src="slides_kul2/slide_11.jpg" alt="Slide 11" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-e4').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-e4">Slide 11 · Vitamin B1 (Tiamin)</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- EMN BAB 5 -->
      <article id="emn-05" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 05 · Merangkum Slide 16, 17, 24</span>
          <span class="badge badge-crimson">Keluar di Kasus Pembuka Slide 3 & Kasus 1 Slide 24</span>
        </div>
        <h2>Pembeda Utama: Folat (B9) vs Kobalamin (B12)</h2>
        <p class="bento-sub">Keduanya sama-sama menimbulkan <strong>Anemia Megaloblastik (MCV > 100 fL)</strong> dan peningkatan homosistein, tetapi <strong>defisit neurologis dan peningkatan MMA hanya terjadi pada defisiensi B12</strong>.</p>

        <div class="bento-split">
          <div>
            <div class="table-scroll">
              <table>
                <thead>
                  <tr>
                    <th>Parameter Pembeda (Slide 17)</th>
                    <th>Defisiensi Vitamin B9 (Folat)</th>
                    <th>Defisiensi Vitamin B12 (Kobalamin)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>MCV / Anemia</strong></td>
                    <td>Makrositik, megaloblastik (MCV > 100 fL)</td>
                    <td>Makrositik, megaloblastik (MCV > 100 fL)</td>
                  </tr>
                  <tr>
                    <td><strong>Neuropati / Vibrasi / Ataksia</strong></td>
                    <td><strong>Tidak khas / Tidak ada</strong></td>
                    <td><strong>Khas!</strong> (Bisa muncul walau Hb/MCV belum abnormal)</td>
                  </tr>
                  <tr>
                    <td><strong>Homosistein Serum</strong></td>
                    <td>Meningkat</td>
                    <td>Meningkat</td>
                  </tr>
                  <tr>
                    <td><strong>Asam Metilmalonat (MMA)</strong></td>
                    <td><strong>Normal</strong></td>
                    <td><strong>Meningkat Spesifik!</strong></td>
                  </tr>
                  <tr>
                    <td><strong>Faktor Risiko Utama</strong></td>
                    <td>Kehamilan, kurang sayur hijau, alkohol</td>
                    <td><strong>Metformin lama</strong>, vegan, gastritis autoimun, reseksi ileum</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('e5','slides_kul2/slide_17.jpg','Slide 17 · Tabel Perbandingan B9 (Folat) vs B12 (Kobalamin)',this)">Slide 17</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e5','slides_kul2/slide_16.jpg','Slide 16 · Jalur Absorpsi B12 (Faktor Intrinsik & Ileum Terminal)',this)">Slide 16</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e5','slides_kul2/slide_24.jpg','Slide 24 · Diskusi Kasus 1: Metformin, Parestesia, MCV 112 fL',this)">Slide 24</button>
              </div>
            </div>
            <img id="dock-img-e5" src="slides_kul2/slide_17.jpg" alt="Slide 17" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-e5').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-e5">Slide 17 · Folat vs B12</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

      <!-- EMN BAB 6 -->
      <article id="emn-06" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 06 · Merangkum Slide 14, 15, 26</span>
          <span class="badge badge-crimson">Keluar di Kasus Diskusi Slide 26</span>
        </div>
        <h2>Pembeda Perdarahan: Skorbut (Vit C) vs Defisiensi Vit K</h2>
        <p class="bento-sub">Bila pasien mengalami perdarahan gusi dan mudah memar, periksa nilai <strong>PT/INR</strong> untuk membedakan defek kolagen kapiler (Vitamin C) vs defek faktor koagulasi (Vitamin K):</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Defisiensi Vitamin C (Skorbut)</div>
                <div class="tile-title">Defek Kolagen · PT/INR Normal</div>
                <div class="tile-body">Gagal hidroksilasi prolin & lisin → kapiler rapuh. Gejala: <strong>gusi berdarah, petechiae perifolikular, corkscrew hair, luka lama sembuh, namun PT/INR NORMAL</strong>.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Defisiensi Vitamin K</div>
                <div class="tile-title">Defek Faktor II, VII, IX, X · PT/INR Naik</div>
                <div class="tile-body">Gagal karboksilasi glutamat faktor koagulasi di hati. Gejala: perdarahan mukosa disertai <strong>pemanjangan PT/INR dan aPTT</strong>.</div>
              </div>
            </div>
          </div>

          <aside class="slide-dock">
            <div class="dock-bar">
              <span class="dock-label">Bukti Slide Dosen</span>
              <div class="dock-tabs">
                <button type="button" class="dock-btn active" onclick="swapDockSlide('e6','slides_kul2/slide_26.jpg','Slide 26 · Diskusi Kasus 3: Perdarahan Gingiva & PT/INR Normal (Skorbut)',this)">Slide 26</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e6','slides_kul2/slide_14.jpg','Slide 14 · Vitamin C: Sintesis Kolagen & Gambaran Skorbut',this)">Slide 14</button>
                <button type="button" class="dock-btn" onclick="swapDockSlide('e6','slides_kul2/slide_21.jpg','Slide 21 · Pemilihan Pemeriksaan Lab Sesuai Pertanyaan Klinis',this)">Slide 21</button>
              </div>
            </div>
            <img id="dock-img-e6" src="slides_kul2/slide_26.jpg" alt="Slide 26" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-e6').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-e6">Slide 26 · Skorbut vs Vitamin K</span>
              <span>Klik untuk Zoom ↗</span>
            </div>
          </aside>
        </div>
      </article>

    </div>

    <!-- VIEW 2: SOAL LATIHAN -->
    <div id="view-soal" class="view-section">
      <div class="cbt-header-bar">
        <span class="cbt-score-pill" id="cbt-score-pill">Skor Anda: 0/6 Benar (0 Dijawab)</span>
        <div class="cbt-filters">
          <button type="button" class="cbt-filter-btn active" onclick="filterCBT('all', this)">Semua Soal (6)</button>
          <button type="button" class="cbt-filter-btn" onclick="filterCBT('kasus', this)">Kasus Asli Slide Dosen (3)</button>
          <button type="button" class="cbt-filter-btn" onclick="filterCBT('prediksi', this)">Prediksi Berbasis Slide (3)</button>
          <button type="button" class="cbt-filter-btn" onclick="clearQuiz()">Reset Jawaban</button>
        </div>
      </div>

      <div id="cbt-list"></div>
    </div>

    <!-- VIEW 3: CEK CEPAT H-1 -->
    <div id="view-flash" class="view-section">
      <div class="flash-grid">
        <div class="flash-unit">
          <div>
            <span class="badge badge-crimson">Slide 17 & 24</span>
            <div class="flash-q">1. Pasien DM konsumsi Metformin lama + kesemutan + MCV 112 fL. Defisiensi apa dan metabolit apa yang naik spesifik?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">Defisiensi Vitamin B12 (Kobalamin). Metabolit yang meningkat spesifik adalah Asam Metilmalonat (MMA) — sedangkan pada defisiensi Folat (B9), MMA normal.</div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-crimson">Slide 11 & 25</span>
            <div class="flash-q">2. Apa trias Ensefalopati Wernicke dan enzim apa yang membutuhkan kofaktor Tiamin Pirofosfat (TPP)?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">Trias Wernicke: Kebingungan akut (ensefalopati), Ataksia, dan Gangguan gerak bola mata (nistagmus/oftalmoplegia). Enzim: Piruvat dehidrogenase, α-ketoglutarat dehidrogenase, Transketolase.</div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-emerald">Slide 26</span>
            <div class="flash-q">3. Gusi berdarah + petechiae perifolikular + luka lama sembuh + PT/INR normal. Defisiensi vitamin apa?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">Defisiensi Vitamin C (Skorbut / Scurvy) akibat gangguan hidroksilasi kolagen dinding pembuluh darah kapiler.</div>
        </div>

        <div class="flash-unit">
          <div>
            <span class="badge badge-cobalt">Slide 9</span>
            <div class="flash-q">4. Apa perbedaan bentuk metabolit Vitamin D yang paling aktif secara biologis vs yang diukur di laboratorium?</div>
          </div>
          <button type="button" class="btn-secondary" onclick="this.parentElement.classList.toggle('open')">Buka Kunci Jawaban</button>
          <div class="flash-ans">Paling aktif secara biologis: 1,25-(OH)2-D (Kalsitriol, produk ginjal). Yang diukur di lab untuk menilai status Vitamin D: 25(OH)D (Kalsidiol, produk hati).</div>
        </div>
      </div>
    </div>

  </main>

  <!-- ZOOM MODAL -->
  <div id="zoom-modal" class="modal-overlay" onclick="closeZoom()">
    <div class="modal-window" onclick="event.stopPropagation()">
      <div class="modal-top">
        <strong id="zoom-title">Bukti Slide Asli Dosen</strong>
        <button type="button" class="cmdk-trigger" onclick="closeZoom()">Tutup (ESC)</button>
      </div>
      <img id="zoom-img" src="slides_kul2/slide_17.jpg" alt="Slide Zoom" />
    </div>
  </div>

  <!-- CMD+K MODAL -->
  <div id="search-modal" class="modal-overlay" onclick="closeSearchModal()">
    <div class="cmdk-box" onclick="event.stopPropagation()">
      <div class="cmdk-bar">
        <input type="text" id="cmdk-inp" class="cmdk-input" placeholder="Ketik kata kunci soal UAB / slide (contoh: B12, Metformin, Anemia, Vitamin, Kalsium)..." oninput="execSearch()" />
        <button type="button" class="cmdk-trigger" onclick="closeSearchModal()">ESC</button>
      </div>
      <div id="cmdk-out" class="cmdk-results"></div>
    </div>
  </div>

  <script src="vendor/uab_search_data.js"></script>
  <script>
    window.MOD_KEY = 'emn_kul2_supahero';
    window.QUIZ_DATA = [
      {{
        cat: 'kasus',
        source: 'Kasus Asli Slide Dosen · Slide 3 & Slide 24',
        slide: 'slides_kul2/slide_24.jpg',
        slideCap: 'Bukti Slide 24 · Diskusi Kasus 1 (Metformin & Defisiensi B12)',
        stem: 'Seorang laki-laki berusia 62 tahun dengan riwayat DM tipe 2 dan konsumsi metformin jangka panjang datang dengan keluhan kesemutan pada kedua kaki selama 6 bulan, mudah lelah, dan lidah terasa nyeri (glossitis). Pemeriksaan fisik menunjukkan gangguan sensasi vibrasi. Laboratorium: Hb 9,8 g/dL dan MCV 112 fL. Defisiensi vitamin manakah yang paling mungkin beserta pemeriksaan metabolit konfirmasinya?',
        opts: [
          'Vitamin B9 (Folat) — kadar homosistein normal',
          'Vitamin B12 (Kobalamin) — peningkatan asam metilmalonat (MMA)',
          'Vitamin B1 (Tiamin) — penurunan aktivitas transketolase',
          'Vitamin B6 (Piridoksin) — peningkatan feritin serum',
          'Vitamin E (Tokoferol) — pemanjangan PT/INR'
        ],
        ans: 1,
        exp: '<strong>Kunci: B (Defisiensi Vitamin B12 — peningkatan MMA).</strong> Sesuai Slide 3, 17, dan 24, penggunaan metformin jangka panjang menghambat absorpsi B12 di ileum terminal, memicu anemia megaloblastik (MCV 112 fL) disertai neuropati sensorik/vibrasi dengan peningkatan MMA.'
      }},
      {{
        cat: 'kasus',
        source: 'Kasus Asli Slide Dosen · Slide 25',
        slide: 'slides_kul2/slide_25.jpg',
        slideCap: 'Bukti Slide 25 · Diskusi Kasus 2 (Ensefalopati Wernicke)',
        stem: 'Seorang pasien dengan riwayat malnutrisi berat dan muntah berkepanjangan dibawa ke IGD dalam kondisi kebingungan akut (konfusi), langkah jalan sempoyongan (ataksia), serta gangguan gerak bola mata (nistagmus/oftalmoplegia) setelah sebelumnya mendapat cairan infus dekstrosa. Defisiensi vitamin apakah yang mendasari kegawatan neurologis ini?',
        opts: [
          'Vitamin B1 (Tiamin)',
          'Vitamin B2 (Riboflavin)',
          'Vitamin B3 (Niasin)',
          'Vitamin B12 (Kobalamin)',
          'Vitamin C (Asam Askorbat)'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Vitamin B1 / Tiamin).</strong> Sesuai Slide 11 dan Slide 25, trias konfusi akut, ataksia, dan oftalmoplegia/nistagmus adalah tanda klasik <strong>Ensefalopati Wernicke</strong> akibat defisiensi Tiamin Pirofosfat (TPP).'
      }},
      {{
        cat: 'kasus',
        source: 'Kasus Asli Slide Dosen · Slide 26',
        slide: 'slides_kul2/slide_26.jpg',
        slideCap: 'Bukti Slide 26 · Diskusi Kasus 3 (Skorbut / Defisiensi Vit C)',
        stem: 'Seorang pria berusia 41 tahun dengan diet sangat terbatas datang dengan keluhan gusi sering berdarah, mudah memar, bintik perdarahan perifolikular di kedua tungkai, dan luka yang lama sembuh. Hasil pemeriksaan darah menunjukkan jumlah trombosit normal serta nilai PT dan INR normal. Diagnosis yang paling tepat adalah...',
        opts: [
          'Defisiensi Vitamin K',
          'Defisiensi Vitamin C (Skorbut)',
          'Defisiensi Vitamin D (Osteomalasia)',
          'Defisiensi Vitamin B3 (Pellagra)',
          'Defisiensi Vitamin A (Xerophthalmia)'
        ],
        ans: 1,
        exp: '<strong>Kunci: B (Defisiensi Vitamin C / Skorbut).</strong> Sesuai Slide 26, perdarahan gusi + petechiae perifolikular + luka lama sembuh dengan <strong>PT/INR yang normal</strong> membuktikan bahwa kelainannya terletak pada kerapuhan kolagen dinding kapiler (Vitamin C).'
      }},
      {{
        cat: 'prediksi',
        source: 'Prediksi Berbasis Slide · Slide 8',
        slide: 'slides_kul2/slide_8.jpg',
        slideCap: 'Bukti Slide 8 · Peran Retinal vs Retinoat & Bercak Bitot',
        stem: 'Seorang anak berusia 4 tahun dibawa ibunya karena sering menabrak benda saat senja hari. Pada pemeriksaan konjungtiva tampak bercak putih keperakan berbusa di sisi temporal (Bercak Bitot). Bentuk aktif vitamin manakah yang berperan menjaga diferensiasi epitel konjungtiva agar tidak mengalami metaplasia keratin tersebut?',
        opts: [
          'Asam retinoat',
          '11-cis-retinal',
          'Kalsitriol',
          'Alfa-tokoferol',
          'Menakuinon'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Asam retinoat).</strong> Sesuai Slide 8: <em>Retinal → siklus visual (rodopsin)</em>, sedangkan <em>Retinoat → diferensiasi epitel</em>.'
      }},
      {{
        cat: 'prediksi',
        source: 'Prediksi Berbasis Slide · Slide 9',
        slide: 'slides_kul2/slide_9.jpg',
        slideCap: 'Bukti Slide 9 · Parameter Status Vitamin D: 25(OH)D',
        stem: 'Seorang perempuan berusia 50 tahun mengeluhkan nyeri tulang difus dan kelemahan otot proksimal. Dokter mencurigai adanya osteomalasia akibat defisiensi Vitamin D. Pemeriksaan laboratorium manakah yang paling tepat dipilih untuk mencerminkan status cadangan Vitamin D tubuh pasien?',
        opts: [
          '1,25-dihidroksivitamin D [1,25(OH)2D]',
          '25-hidroksivitamin D [25(OH)D]',
          '7-dehidrokolesterol',
          'Kalsitonin serum',
          'Alkaline phosphatase urin'
        ],
        ans: 1,
        exp: '<strong>Kunci: B (25-hidroksivitamin D / 25(OH)D).</strong> Sesuai catatan kaki di Slide 9: <em>25(OH)D mencerminkan status vitamin D</em>.'
      }},
      {{
        cat: 'prediksi',
        source: 'Prediksi Berbasis Slide · Slide 13',
        slide: 'slides_kul2/slide_13.jpg',
        slideCap: 'Bukti Slide 13 · Defisiensi B3 (Niasin) → Pellagra',
        stem: 'Seorang petani yang hanya mengonsumsi jagung tanpa variasi protein hewani datang dengan keluhan ruam kulit hiperpigmentasi simetris di area leher yang terpapar matahari (Casal necklace), disertai diare kronik dan penurunan daya ingat. Defisiensi kofaktor vitamin apakah yang dialami pasien?',
        opts: [
          'Vitamin B1 (Tiamin)',
          'Vitamin B2 (Riboflavin)',
          'Vitamin B3 (Niasin / NAD+ & NADP+)',
          'Vitamin B6 (Piridoksin)',
          'Vitamin B7 (Biotin)'
        ],
        ans: 2,
        exp: '<strong>Kunci: C (Vitamin B3 / Niasin).</strong> Sesuai Slide 13, trias Dermatitis fotosensitif (Casal necklace), Diare, dan Demensia adalah sindrom klasik <strong>Pellagra</strong>.'
      }}
    ];

    document.getElementById('cbt-list').innerHTML = window.QUIZ_DATA.map((q, idx) => `
      <article class="q-module" id="qm-${{idx}}" data-cat="${{q.cat}}">
        <div class="q-top">
          <span class="badge badge-amber">${{q.source}}</span>
          <span class="ch-index">Soal #${{idx + 1}}</span>
        </div>
        <div class="q-stem-txt">${{q.stem}}</div>
        <div class="opt-stack">
          ${{q.opts.map((opt, oIdx) => `
            <button type="button" class="opt-row" onclick="pickAnswer(${{idx}}, ${{oIdx}})">
              <span class="opt-key">${{String.fromCharCode(65 + oIdx)}}.</span>
              <span>${{opt}}</span>
            </button>
          `).join('')}}
        </div>
        <div class="q-drawer" id="qd-${{idx}}">
          <div style="font-size:0.94rem;color:#263645;line-height:1.6;">${{q.exp}}</div>
          <div class="slide-dock">
            <img src="${{q.slide}}" alt="${{q.slideCap}}" class="dock-img" onclick="openZoom('${{q.slide}}', '${{q.slideCap}}')" />
            <div class="dock-foot"><span>${{q.slideCap}}</span><span>Zoom ↗</span></div>
          </div>
        </div>
      </article>
    `).join('');

    {SUPAHERO_JS}
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "BDT_KUL3_Patient_Safety.html"), "w", encoding="utf-8") as f:
    f.write(BDT_SUPAHERO)

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(BDT_SUPAHERO)

with open(os.path.join(BASE_DIR, "VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html"), "w", encoding="utf-8") as f:
    f.write(EMN_SUPAHERO)

print("Successfully built Supahero Edition for BDT KUL 3 and EMN KUL 2!")
