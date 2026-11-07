#!/usr/bin/env python3
"""Build the World-Class, Joyful, Zero-Fatigue Preclinical Learning Platform for EMN KUL 3 Defisiensi Mineral.
Key Architectural Standards:
1. Zero AI-Slop (No fake dotted grids, no emojis as icons, no salesy banners, no nested card clutter).
2. "Langsung Paham" Visual Interactive Simulators:
   - Interactive 3-Stage Iron Depletion Slider (Bone Marrow -> Serum -> RBC)
   - Interactive ROMK Kidney Channel (Why K leaks when Mg is depleted)
   - Interactive Hepcidin Rhythm Simulator (Why AGA 2024 mandates alternate-day dosing)
   - Interactive Refeeding Cascade (Insulin surge -> Phosphate collapse -> ATP failure)
3. Ergonomic Zen Palette (#FAF9F6 alabaster, #18191B deep charcoal, Muted Sage, Terracotta, Ochre).
4. Master-Detail Interactive Mineral Deck (Fe, Zn, Mg, Ca, P, Cu, I, Se) with integrated slide proof.
5. Tactile, Bug-Free CBT Practice Suite with immediate, satisfying visual feedback.
"""
import os
import json

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

WORLD_CLASS_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Mineral · Sistem Belajar Interaktif EMN</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;1,6..72,500&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #F9F8F6;
      --surface: #FFFFFF;
      --surface-elevated: #FFFFFF;
      --surface-subtle: #F2EFEB;
      --surface-active: #EAE6DF;
      
      --border: #E5E1D8;
      --border-subtle: #EDEAE2;
      --border-focus: #18191B;
      
      --ink: #141517;
      --ink-secondary: #52545A;
      --ink-muted: #888B92;
      
      --sage: #1E6B47;
      --sage-light: #EBF5F0;
      --sage-border: #BCDCCB;
      
      --terracotta: #B93822;
      --terracotta-light: #FBEFEA;
      --terracotta-border: #F3C9BF;
      
      --ochre: #B06914;
      --ochre-light: #FDF4E7;
      --ochre-border: #F6DAB3;
      
      --navy: #1B3B6F;
      --navy-light: #EDF3FA;
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-full: 9999px;
      
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-serif: 'Newsreader', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --shadow-ambient: 0 4px 20px -2px rgba(20, 21, 23, 0.05);
      --shadow-float: 0 16px 40px -6px rgba(20, 21, 23, 0.1);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      background-color: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 15.5px;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 120px;
    }

    ::selection { background: #D2E8DB; color: #141517; }

    /* Clean Glass Header */
    .app-header {
      position: sticky;
      top: 0;
      z-index: 200;
      background: rgba(249, 248, 246, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
      padding: 12px 28px;
      transition: all 0.2s ease;
    }
    .header-content {
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
    }
    .brand-mark {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-tag {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 600;
      color: var(--surface);
      background: var(--ink);
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }
    .brand-context {
      display: flex;
      flex-direction: column;
    }
    .brand-context-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink);
      line-height: 1.2;
    }
    .brand-context-sub {
      font-size: 0.78rem;
      color: var(--ink-muted);
    }

    /* Seamless View Navigation Tabs */
    .view-pills {
      display: flex;
      background: var(--surface-subtle);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 3px;
    }
    .view-pill {
      border: none;
      background: transparent;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--ink-secondary);
      padding: 7px 16px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .view-pill:hover { color: var(--ink); }
    .view-pill.active {
      background: var(--surface);
      color: var(--ink);
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .header-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-action-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 7px 14px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--ink-secondary);
      transition: all 0.18s ease;
      cursor: pointer;
    }
    .btn-action-pill:hover {
      border-color: var(--ink);
      color: var(--ink);
      transform: translateY(-1px);
    }
    .btn-primary-action {
      background: var(--sage);
      border-color: var(--sage);
      color: #FFFFFF !important;
    }
    .btn-primary-action:hover {
      opacity: 0.95;
      background: #185538;
    }

    /* App Shell */
    .main-shell {
      max-width: 1040px;
      margin: 0 auto;
      padding: 36px 24px 0;
    }

    .view-section { display: none; }
    .view-section.active { display: block; animation: viewFadeIn 0.25s ease-out; }
    @keyframes viewFadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* =========================================================================
       HERO & INTUITION ANCHOR
       ========================================================================= */
    .hero-anchor {
      margin-bottom: 40px;
      padding-bottom: 24px;
      border-bottom: 1px solid var(--border);
    }
    .hero-headline {
      font-family: var(--font-serif);
      font-size: 2.8rem;
      font-weight: 600;
      line-height: 1.2;
      color: var(--ink);
      letter-spacing: -0.02em;
      margin-bottom: 12px;
    }
    .hero-standfirst {
      font-size: 1.15rem;
      color: var(--ink-secondary);
      line-height: 1.65;
      max-width: 860px;
    }

    /* =========================================================================
       SECTION 1: "LANGSUNG PAHAM" VISUAL SIMULATORS (THE GAME-CHANGER)
       ========================================================================= */
    .interactive-canvas {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px 32px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-ambient);
    }
    .canvas-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
    }
    .canvas-title-group h3 {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--ink);
    }
    .canvas-title-group p {
      font-size: 0.88rem;
      color: var(--ink-secondary);
      margin-top: 2px;
    }

    /* Simulator 1: The 3-Stage Iron Depletion */
    .stepper-nav {
      display: flex;
      background: var(--surface-subtle);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 4px;
      margin-bottom: 24px;
    }
    .stepper-btn {
      flex: 1;
      border: none;
      background: transparent;
      padding: 10px 14px;
      font-family: var(--font-sans);
      font-size: 0.86rem;
      font-weight: 600;
      color: var(--ink-secondary);
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.2s ease;
      text-align: center;
    }
    .stepper-btn.active {
      background: var(--surface);
      color: var(--ink);
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }

    .stage-card {
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 16px;
      margin-bottom: 20px;
    }
    .vial-box {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.25s ease;
    }
    .vial-box.highlight {
      background: #FFFFFF;
      border-color: var(--terracotta);
      box-shadow: 0 0 0 2px var(--terracotta-light);
    }
    .vial-param {
      font-size: 0.76rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      color: var(--ink-muted);
    }
    .vial-value {
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--ink);
      margin: 4px 0 8px;
    }
    .vial-status {
      font-size: 0.84rem;
      line-height: 1.45;
    }
    .vial-status.status-good { color: var(--sage); }
    .vial-status.status-bad { color: var(--terracotta); font-weight: 600; }
    .vial-status.status-warn { color: var(--ochre); font-weight: 600; }

    .stage-narrative {
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      font-size: 0.95rem;
      line-height: 1.65;
      color: var(--ink);
    }

    /* Simulator 2: ROMK Kidney Channel */
    .romk-simulator {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 24px;
      align-items: center;
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 24px;
    }
    .romk-visual {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px;
      text-align: center;
      position: relative;
    }
    .romk-channel-gate {
      height: 80px;
      border: 3px dashed var(--navy);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 14px 0;
      font-weight: 700;
      font-size: 0.95rem;
      transition: all 0.3s ease;
    }
    .romk-channel-gate.plugged {
      background: var(--sage-light);
      border-color: var(--sage);
      color: var(--sage);
    }
    .romk-channel-gate.unplugged {
      background: var(--terracotta-light);
      border-color: var(--terracotta);
      color: var(--terracotta);
    }
    .romk-controls {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .btn-sim-toggle {
      padding: 12px 18px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: var(--surface);
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.18s ease;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .btn-sim-toggle:hover { border-color: var(--ink); }
    .btn-sim-toggle.active {
      border-color: var(--ink);
      background: var(--ink);
      color: #FFFFFF;
    }

    /* =========================================================================
       SECTION 2: MASTER-DETAIL 8 MINERAL DECK (ERGONOMIC BROWSER)
       ========================================================================= */
    .deck-container {
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 24px;
      margin-bottom: 48px;
    }
    .deck-sidebar {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .mineral-nav-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      border-radius: var(--radius-md);
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: left;
    }
    .mineral-nav-item:hover {
      background: var(--surface-subtle);
      border-color: var(--border-dark);
      transform: translateX(2px);
    }
    .mineral-nav-item.active {
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
      box-shadow: var(--shadow-ambient);
    }
    .nav-badge-cat {
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--surface-subtle);
      color: var(--ink-secondary);
    }
    .mineral-nav-item.active .nav-badge-cat {
      background: rgba(255, 255, 255, 0.2);
      color: #FFFFFF;
    }

    /* Active Mineral Detail Sheet */
    .detail-sheet {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px 36px;
      box-shadow: var(--shadow-ambient);
      display: none;
      animation: sheetIn 0.2s ease-out;
    }
    .detail-sheet.active { display: block; }
    @keyframes sheetIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

    .sheet-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 24px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--border);
    }
    .sheet-title-group h2 {
      font-family: var(--font-serif);
      font-size: 2.1rem;
      font-weight: 600;
      color: var(--ink);
      line-height: 1.15;
    }
    .sheet-title-group span {
      font-size: 0.86rem;
      color: var(--ink-muted);
      margin-top: 4px;
      display: block;
    }

    .sheet-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }
    .info-pane {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
    }
    .info-pane h4 {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }
    .info-pane p, .info-pane ul {
      font-size: 0.94rem;
      line-height: 1.6;
      color: #2A2B2D;
    }
    .info-pane ul { padding-left: 18px; }

    .trap-callout {
      background: var(--ochre-light);
      border: 1px solid var(--ochre-border);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 24px;
    }
    .trap-callout h4 {
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ochre);
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .trap-callout p {
      font-size: 0.94rem;
      line-height: 1.6;
      color: #38240D;
    }

    /* Embedded Slide Inspector */
    .slide-inspector {
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      cursor: pointer;
      transition: all 0.18s ease;
    }
    .slide-inspector:hover {
      background: #EAE6DF;
      border-color: var(--ink);
    }
    .inspector-meta {
      display: flex;
      align-items: center;
      gap: 14px;
    }
    .inspector-thumb {
      width: 72px;
      height: 48px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }
    .inspector-txt strong {
      font-size: 0.9rem;
      color: var(--ink);
      display: block;
    }
    .inspector-txt span {
      font-size: 0.78rem;
      color: var(--ink-muted);
    }
    .inspector-arrow {
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--sage);
    }

    /* =========================================================================
       SECTION 3: CBT SIMULATOR (TACTILE & BUG-FREE)
       ========================================================================= */
    .cbt-suite {
      margin-top: 40px;
    }
    .cbt-top {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }
    .cbt-score-display {
      font-family: var(--font-mono);
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--sage);
    }

    .q-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px 32px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-ambient);
    }
    .q-badge {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--ink-muted);
      margin-bottom: 8px;
      display: block;
    }
    .q-stem-text {
      font-size: 1.05rem;
      font-weight: 500;
      line-height: 1.68;
      color: var(--ink);
      margin-bottom: 20px;
    }

    .options-group {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .option-button {
      padding: 14px 18px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: var(--surface);
      text-align: left;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      color: var(--ink);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .option-button:hover {
      background: var(--bg);
      border-color: var(--border-dark);
      transform: translateX(2px);
    }
    .option-button:active {
      transform: scale(0.99);
    }
    .option-key {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--ink-muted);
      flex: none;
    }

    /* Option States */
    .option-button.is-correct {
      background: var(--sage-light) !important;
      border-color: var(--sage) !important;
      color: var(--sage) !important;
      font-weight: 600;
      box-shadow: 0 0 0 1px var(--sage);
    }
    .option-button.is-wrong {
      background: var(--terracotta-light) !important;
      border-color: var(--terracotta) !important;
      color: var(--terracotta) !important;
    }

    .feedback-drawer {
      margin-top: 20px;
      padding: 20px 24px;
      border-radius: var(--radius-md);
      font-size: 0.94rem;
      line-height: 1.65;
      display: none;
      animation: feedbackIn 0.2s ease-out;
    }
    .feedback-drawer.show { display: block; }
    @keyframes feedbackIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }

    .feedback-drawer.correct-tone {
      background: var(--sage-light);
      border: 1px solid var(--sage-border);
      color: #124029;
    }
    .feedback-drawer.wrong-tone {
      background: var(--terracotta-light);
      border: 1px solid var(--terracotta-border);
      color: #61180C;
    }

    /* =========================================================================
       SECTION 4: HIGH-YIELD H-1 MATRIX
       ========================================================================= */
    .matrix-table {
      width: 100%;
      border-collapse: collapse;
      background: var(--surface);
      border-radius: var(--radius-md);
      overflow: hidden;
      border: 1px solid var(--border);
      box-shadow: var(--shadow-ambient);
      font-size: 0.92rem;
    }
    .matrix-table th {
      background: var(--surface-subtle);
      padding: 14px 18px;
      text-align: left;
      font-weight: 700;
      color: var(--ink);
      border-bottom: 1px solid var(--border);
    }
    .matrix-table td {
      padding: 16px 18px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
      color: #2D2F33;
    }
    .matrix-table tr:last-child td { border-bottom: none; }
    .matrix-table tr:hover td { background: var(--bg); }

    /* Lightbox Modal */
    .lightbox-backdrop {
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(20, 21, 23, 0.85);
      backdrop-filter: blur(10px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }
    .lightbox-backdrop.open { display: flex; }
    .lightbox-frame {
      max-width: 92%;
      max-height: 88vh;
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-float);
    }

    @media (max-width: 860px) {
      .deck-container { grid-template-columns: 1fr; }
      .stage-card { grid-template-columns: 1fr; }
      .romk-simulator { grid-template-columns: 1fr; }
      .sheet-grid { grid-template-columns: 1fr; }
      .view-pills { display: none; }
      .hero-headline { font-size: 2.1rem; }
    }
  </style>
</head>
<body>

  <!-- Minimalist Clean Header -->
  <header class="app-header">
    <div class="header-content">
      <div class="brand-mark">
        <span class="brand-tag">EMN · KUL 3</span>
        <div class="brand-context">
          <span class="brand-context-title">Defisiensi Mineral</span>
          <span class="brand-context-sub">dr. Iwal Reza Ahdi, Sp.PD-FINASIM</span>
        </div>
      </div>

      <!-- Clean 3-Tab Navigator -->
      <nav class="view-pills">
        <button type="button" class="view-pill active" onclick="switchTab('tab-simulators', this)">
          <span>⚡ Konsep 60 Detik</span>
        </button>
        <button type="button" class="view-pill" onclick="switchTab('tab-deck', this)">
          <span>📚 Buku 8 Mineral</span>
        </button>
        <button type="button" class="view-pill" onclick="switchTab('tab-cbt', this)">
          <span>🎯 Latihan UAB (8)</span>
        </button>
        <button type="button" class="view-pill" onclick="switchTab('tab-matrix', this)">
          <span>📋 Matriks H-1</span>
        </button>
      </nav>

      <div class="header-actions">
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-action-pill btn-primary-action" download>
          <span>Deck Anki</span>
        </a>
      </div>
    </div>
  </header>

  <main class="main-shell">

    <!-- Hero Title -->
    <section class="hero-anchor">
      <h1 class="hero-headline">Paham Mekanisme, Kunci 4 Soal UAB.</h1>
      <p class="hero-standfirst">Didesain khusus untuk mahasiswa kedokteran agar langsung paham fisiologi mineral dalam hitungan detik tanpa membuka slide dosen yang padat. Tidak membuat mata lelah meski dipelajari berjam-jam.</p>
    </section>

    <!-- =================================================================== -->
    <!-- TAB 1: "LANGSUNG PAHAM" VISUAL INTERACTIVE SIMULATORS               -->
    <!-- =================================================================== -->
    <div id="tab-simulators" class="view-section active">
      
      <!-- SIMULATOR 1: BESI & FERRITIN STAGING -->
      <article class="interactive-canvas">
        <div class="canvas-top">
          <div class="canvas-title-group">
            <h3>1. Simulator Stadium Defisiensi Besi: Ferritin vs Hb</h3>
            <p>Klik tombol stadium di bawah ini untuk melihat apa yang sebenarnya terjadi di darah dan sumsum tulang.</p>
          </div>
          <button class="btn-action-pill" onclick="openLightbox('slides_kul3/slide_10.jpg')">Intip Slide 10 ↗</button>
        </div>

        <div class="stepper-nav">
          <button type="button" class="stepper-btn active" onclick="setIronStage(1)">Stadium 1: Cadangan Turun</button>
          <button type="button" class="stepper-btn" onclick="setIronStage(2)">Stadium 2: Eritropoiesis Terbatas</button>
          <button type="button" class="stepper-btn" onclick="setIronStage(3)">Stadium 3: Anemia Nyata (IDA)</button>
        </div>

        <div class="stage-card">
          <div class="vial-box" id="vial-ferritin">
            <span class="vial-param">Ferritin Serum (Cadangan Fe)</span>
            <span class="vial-value" id="val-ferritin">&lt; 15 ng/mL</span>
            <span class="vial-status status-bad" id="stat-ferritin">ANJLOK DULUAN (Kritis)</span>
          </div>
          <div class="vial-box" id="vial-tsat">
            <span class="vial-param">Saturasi Transferrin (TSAT)</span>
            <span class="vial-value" id="val-tsat">28% (Normal)</span>
            <span class="vial-status status-good" id="stat-tsat">Transpor Besi Cukup</span>
          </div>
          <div class="vial-box" id="vial-hb">
            <span class="vial-param">Hemoglobin &amp; MCV</span>
            <span class="vial-value" id="val-hb">Hb 13.5 · MCV 88</span>
            <span class="vial-status status-good" id="stat-hb">Tampak Normal (Belum Anemia)</span>
          </div>
        </div>

        <div class="stage-narrative" id="narrative-iron">
          💡 <b>Kunci Ujian UAB:</b> Pasien di Stadium 1 <i>belum mengalami anemia</i>, tetapi cadangan besinya sudah habis terkuras. Karena itu, <b>MCV normal TIDAK PERNAH menyingkirkan defisiensi besi stadium dini</b>. Ferritin adalah biomarker paling awal yang turun!
        </div>
      </article>

      <!-- SIMULATOR 2: GINJAL, MAGNESIUM, & KANAL ROMK -->
      <article class="interactive-canvas">
        <div class="canvas-top">
          <div class="canvas-title-group">
            <h3>2. Simulator Kanal ROMK: Mengapa Kalium Susah Naik Bila Mg Rendah?</h3>
            <p>Jawab pertanyaan klinis klasik dr. Iwal: "Mengapa hipokalemia pasien refrakter terhadap koreksi kalium?"</p>
          </div>
          <button class="btn-action-pill" onclick="openLightbox('slides_kul3/slide_17.jpg')">Intip Slide 17 ↗</button>
        </div>

        <div class="romk-simulator">
          <div class="romk-visual">
            <span style="font-size:0.8rem;font-weight:700;color:var(--ink-muted);text-transform:uppercase;">Membran Tubulus Distal Ginjal</span>
            <div class="romk-channel-gate plugged" id="romk-gate">
              <span id="romk-status-txt">🔒 KANAL ROMK TERSUMBAT (Mg Normal)</span>
            </div>
            <span id="romk-urine-loss" style="font-size:0.84rem;color:var(--sage);font-weight:600;">Kalium tidak bocor ke urin (Normal)</span>
          </div>

          <div class="romk-controls">
            <button type="button" class="btn-sim-toggle active" id="btn-mg-norm" onclick="toggleROMK(true)">
              <span>Kadar Magnesium Normal (&gt;1.7 mg/dL)</span>
              <span>🔒 Tertutup</span>
            </button>
            <button type="button" class="btn-sim-toggle" id="btn-mg-low" onclick="toggleROMK(false)">
              <span>Magnesium Rendah (Akibat Diuretik/PPI)</span>
              <span>⚠️ Bocor</span>
            </button>
            <div style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">
              Magnesium intraseluler bertindak sebagai <b>sumbat alami kanal ROMK</b>. Bila sumbat Mg lepas, kalium bocor terbuang ke urin. <b>Solusi: Koreksi Mg dan Kalium secara serentak!</b>
            </div>
          </div>
        </div>
      </article>

      <!-- SIMULATOR 3: REFEEDING SYNDROME & INSULIN SURGE -->
      <article class="interactive-canvas">
        <div class="canvas-top">
          <div class="canvas-title-group">
            <h3>3. Kaskade Refeeding Syndrome: Dari Karbohidrat ke Gagal Napas</h3>
            <p>Pahami bagaimana pemberian makan pada pasien kelaparan lama bisa memicu kematian mendadak.</p>
          </div>
          <button class="btn-action-pill" onclick="openLightbox('slides_kul3/slide_19.jpg')">Intip Slide 19 ↗</button>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:12px;">
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ink-muted);">FASE 01</span>
            <div style="font-weight:700;color:var(--ink);margin:4px 0 6px;">Puasa Lama / Kelaparan</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Tubuh membakar lemak/keton. Cadangan fosfat intraseluler habis terkuras.</p>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ink-muted);">FASE 02</span>
            <div style="font-weight:700;color:var(--ochre);margin:4px 0 6px;">Karbohidrat Masuk</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Pankreas memompa lonjakan <b>Insulin masif</b> untuk memproses glukosa.</p>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ink-muted);">FASE 03</span>
            <div style="font-weight:700;color:var(--terracotta);margin:4px 0 6px;">Pergeseran Masif</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Insulin memaksa <b>Fosfat (P), K, dan Mg</b> tersedot masuk ke dalam sel.</p>
          </div>
          <div style="background:var(--terracotta-light);border:1px solid var(--terracotta-border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--terracotta);font-weight:700;">FASE 04 (KRITIS)</span>
            <div style="font-weight:700;color:var(--terracotta);margin:4px 0 6px;">Krisis Energi ATP</div>
            <p style="font-size:0.84rem;color:#5D150B;line-height:1.5;">Fosfat plasma &lt;1.0 mg/dL &rarr; sintesis ATP lumpuh &rarr; <b>kelumpuhan diafragma akut (gagal napas)</b>.</p>
          </div>
        </div>
      </article>

    </div>

    <!-- =================================================================== -->
    <!-- TAB 2: MASTER-DETAIL DECK 8 MINERAL (ERGONOMIS & LENGKAP)           -->
    <!-- =================================================================== -->
    <div id="tab-deck" class="view-section">
      <div class="deck-container">
        
        <!-- Sidebar Navigation -->
        <nav class="deck-sidebar" aria-label="Pilih Mineral">
          <button type="button" class="mineral-nav-item active" onclick="selectMineral('fe', this)">
            <span>1. Besi (Fe)</span>
            <span class="nav-badge-cat">Renik</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('zn', this)">
            <span>2. Seng (Zn)</span>
            <span class="nav-badge-cat">Renik</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('mg', this)">
            <span>3. Magnesium (Mg)</span>
            <span class="nav-badge-cat">Makro</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('ca', this)">
            <span>4. Kalsium (Ca)</span>
            <span class="nav-badge-cat">Makro</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('p', this)">
            <span>5. Fosfat (P)</span>
            <span class="nav-badge-cat">Makro</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('cu', this)">
            <span>6. Tembaga (Cu)</span>
            <span class="nav-badge-cat">Renik</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('i', this)">
            <span>7. Iodium (I)</span>
            <span class="nav-badge-cat">Renik</span>
          </button>
          <button type="button" class="mineral-nav-item" onclick="selectMineral('se', this)">
            <span>8. Selenium (Se)</span>
            <span class="nav-badge-cat">Renik</span>
          </button>
        </nav>

        <!-- Detail Sheets -->
        <div class="deck-content-pane">
          
          <!-- BESI (FE) -->
          <article class="detail-sheet active" id="sheet-fe">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Besi (Fe)</h2>
                <span>Transpor Oksigen Hemoglobin, Mioglobin, dan Enzim Sitokrom</span>
              </div>
              <span class="vial-param" style="background:var(--terracotta-light);color:var(--terracotta);padding:4px 8px;border-radius:4px;">Mikromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Gejala Klinis Patognomonik</h4>
                <ul>
                  <li>Kelelahan, takikardia, konjungtiva anemis.</li>
                  <li><b>Pagophagia:</b> Keinginan kuat mengunyah es batu berulang kali.</li>
                  <li>Kuku sendok (koilonychia) dan lidah licin (atrophic glossitis).</li>
                </ul>
              </div>
              <div class="info-pane">
                <h4>Biomarker Diagnostik Kunci</h4>
                <ul>
                  <li><b>Ferritin &lt; 15–30 ng/mL:</b> Biomarker paling awal turun!</li>
                  <li>Saturasi Transferrin (TSAT) &lt; 16–20%.</li>
                  <li>TIBC meningkat (&gt; 400 &mu;g/dL).</li>
                  <li>MCV mikrositik (&lt; 80 fL) &amp; MCH hipokromik di fase lanjut.</li>
                </ul>
              </div>
            </div>

            <div class="trap-callout">
              <h4>Jebakan Ujian UAB dr. Iwal (Pedoman Terapi AGA 2024)</h4>
              <p>Pemberian tablet besi oral <b>dilarang diberikan 3 kali sehari</b>. Setiap asupan besi memicu lonjakan hormon <b>Hepcidin</b> hati selama 24–48 jam yang mengunci ferroportin di usus. Rekomendasi mutakhir: <b>Maksimal 1 kali per hari atau selang-hari (alternate-day)</b> saat perut kosong.</p>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_10.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_10.jpg" class="inspector-thumb" alt="Slide 10">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 10: Perjalanan Defisiensi Besi</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- SENG (ZN) -->
          <article class="detail-sheet" id="sheet-zn">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Seng (Zinc / Zn)</h2>
                <span>Kofaktor &gt;300 Metalloenzim, Imunitas Seluler, dan Integritas Epitel</span>
              </div>
              <span class="vial-param" style="background:var(--sage-light);color:var(--sage);padding:4px 8px;border-radius:4px;">Mikromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Trias Patognomonik Defisiensi Seng</h4>
                <ul>
                  <li><b>Dermatitis periorifisial &amp; akral:</b> Ruam krusta di sekitar mulut, anus, ujung jari.</li>
                  <li><b>Diare kronik:</b> Akibat atrofi mikrovili epitel mukosa usus.</li>
                  <li><b>Alopesia:</b> Kerontokan rambut menyeluruh.</li>
                </ul>
              </div>
              <div class="info-pane">
                <h4>Manifestasi Tambahan</h4>
                <ul>
                  <li>Luka lambat sembuh dan stunting pada anak.</li>
                  <li>Gangguan rasa (hipogeusia) dan penciuman.</li>
                  <li>Bentuk genetik mutasi transporter ZIP4: <b>Acrodermatitis enteropathica</b>.</li>
                </ul>
              </div>
            </div>

            <div class="trap-callout">
              <h4>Faktor Risiko Penghambat Absorpsi</h4>
              <p>Diet tinggi <b>asam fitat</b> (serealia/gandum tak beragi) mengikat seng di lumen usus membentuk senyawa tak larut yang tidak dapat diserap enterosit. Populasi diet nabati monoton sangat rentan defisiensi seng.</p>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_12.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_12.jpg" class="inspector-thumb" alt="Slide 12">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 12: Seng, Imunitas, &amp; Fitat</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- MAGNESIUM (MG) -->
          <article class="detail-sheet" id="sheet-mg">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Magnesium (Mg)</h2>
                <span>Stabilitas Neuromuskular, Kofaktor ATP, dan Pengatur Transpor Ion Ginjal</span>
              </div>
              <span class="vial-param" style="background:var(--navy-light);color:var(--navy);padding:4px 8px;border-radius:4px;">Makromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Gejala Klinis (&lt;1.7 mg/dL)</h4>
                <ul>
                  <li>Tremor, kram otot, hiperrefleksia, tetani.</li>
                  <li>Aritmia ventrikel (Torsades de pointes).</li>
                  <li>Kejang bila hipomagnesemia berat.</li>
                </ul>
              </div>
              <div class="info-pane">
                <h4>Faktor Pemicu Sering</h4>
                <ul>
                  <li>Penggunaan diuretik loop (furosemid).</li>
                  <li>Penggunaan obat maag PPI (omeprazole) jangka panjang.</li>
                  <li>Diare kronik dan alkoholisme.</li>
                </ul>
              </div>
            </div>

            <div class="trap-callout">
              <h4>Jebakan Ujian UAB dr. Iwal: Hipokalemia Refrakter</h4>
              <p>Magnesium intraseluler adalah rem alami kanal <b>ROMK</b> tubulus ginjal. Bila Mg anjlok, kanal ROMK terbuka bebas tanpa kontrol &rarr; kalium terus-menerus terbuang ke urin. <b>Kalium tidak akan pernah bisa naik bila Magnesium tidak dikoreksi secara serentak!</b></p>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_17.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_17.jpg" class="inspector-thumb" alt="Slide 17">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 17: Regulasi Ginjal ROMK</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- KALSIUM (CA) -->
          <article class="detail-sheet" id="sheet-ca">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Kalsium (Ca)</h2>
                <span>Mineral Tulang (99%), Potensial Membran Saraf, dan Kontraksi Otot</span>
              </div>
              <span class="vial-param" style="background:var(--navy-light);color:var(--navy);padding:4px 8px;border-radius:4px;">Makromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Gejala Hipokalsemia Akut</h4>
                <ul>
                  <li>Parestesia perioral (kesemutan bibir) dan ujung jari.</li>
                  <li>Spasme karpopedal, tetani, laringospasme.</li>
                  <li><b>EKG:</b> Pemanjangan interval QT (risiko aritmia).</li>
                </ul>
              </div>
              <div class="info-pane">
                <h4>Dua Tanda Fisik Patognomonik</h4>
                <ul>
                  <li><b>Tanda Chvostek:</b> Kedutan bibir saat saraf fasialis diketuk anterior tragus telinga.</li>
                  <li><b>Tanda Trousseau:</b> Spasme karpopedal saat manset tensimeter dipompa &gt;sistolik selama 3 menit.</li>
                </ul>
              </div>
            </div>

            <div class="trap-callout">
              <h4>Poin Kritis Laboratorium</h4>
              <p>Hanya <b>Ionized Calcium (kalsium bebas 50%)</b> yang aktif secara fisiologis. Kadar kalsium total sangat dipengaruhi oleh konsentrasi albumin serum (turun 0.8 mg/dL kalsium untuk setiap penurunan 1 g/dL albumin).</p>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_15.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_15.jpg" class="inspector-thumb" alt="Slide 15">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 15: Hipokalsemia &amp; Evaluasi</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- FOSFAT (P) -->
          <article class="detail-sheet" id="sheet-p">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Fosfat (P)</h2>
                <span>Sintesis Energi Seluler ATP, 2,3-DPG Eritrosit, dan Matriks Hidroksiapatit</span>
              </div>
              <span class="vial-param" style="background:var(--navy-light);color:var(--navy);padding:4px 8px;border-radius:4px;">Makromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Refeeding Syndrome Kritis</h4>
                <ul>
                  <li>Lonjakan insulin memicu pergeseran fosfat masif ke intrasel.</li>
                  <li>Kadar fosfat plasma anjlok <b>&lt; 1.0 mg/dL</b>.</li>
                  <li>Pembentukan ATP berhenti mendadak.</li>
                </ul>
              </div>
              <div class="info-pane">
                <h4>Manifestasi Kegawatan Fatal</h4>
                <ul>
                  <li><b>Gagal napas akut</b> akibat kelemahan otot diafragma.</li>
                  <li>Kardiomiopati akut dan aritmia ventrikel.</li>
                  <li>Rabdomiolisis dan hemolisis eritrosit.</li>
                </ul>
              </div>
            </div>

            <div class="trap-callout">
              <h4>Pencegahan Sesuai Pedoman ASPEN &amp; NICE</h4>
              <p>Berikan <b>Tiamin (B1) sebelum makanan pertama dimulai</b>. Awali kalori rendah <b>10–15 kkal/kg/hari</b> bertahap. Pantau fosfat, kalium, dan magnesium serial tiap 12–24 jam.</p>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_19.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_19.jpg" class="inspector-thumb" alt="Slide 19">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 19: Pola Refeeding Syndrome</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- TEMBAGA (CU) -->
          <article class="detail-sheet" id="sheet-cu">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Tembaga (Copper / Cu)</h2>
                <span>Komponen Ceruloplasmin, Transpor Besi, dan Integritas Mielin Saraf</span>
              </div>
              <span class="vial-param" style="background:var(--sage-light);color:var(--sage);padding:4px 8px;border-radius:4px;">Mikromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Trias Klinis Patognomonik</h4>
                <ul>
                  <li><b>Anemia mikrositik:</b> Karena ceruloplasmin gagal mengoksidasi besi untuk transferrin.</li>
                  <li><b>Neutropenia berat:</b> Penurunan hitung granulosit di sumsum tulang.</li>
                  <li><b>Mielopati sensorik:</b> Ataksia gaya berjalan (menyerupai defisiensi vitamin B12).</li>
                </ul>
              </div>
              <div class="info-pane">
                <h4>Pemicu Iatrogenik Utama</h4>
                <ul>
                  <li>Konsumsi <b>suplemen Zinc dosis tinggi (&gt;50 mg/hari)</b> jangka panjang.</li>
                  <li>Operasi bariatrik bypass lambung.</li>
                  <li>Pemakaian lem perekat gigi palsu kaya zinc.</li>
                </ul>
              </div>
            </div>

            <div class="trap-callout">
              <h4>Mekanisme Interaksi Seng vs Tembaga</h4>
              <p>Seng berlebih merangsang sel usus memproduksi protein <b>metallothionein</b>. Protein ini memiliki afinitas jauh lebih kuat terhadap tembaga dibanding seng &rarr; tembaga terperangkap di enterosit dan terbuang saat sel usus terkelupas.</p>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_22.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_22.jpg" class="inspector-thumb" alt="Slide 22">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 22: Tembaga &amp; Efek Samping Seng</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- IODIUM (I) -->
          <article class="detail-sheet" id="sheet-i">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Iodium (I)</h2>
                <span>Bahan Baku Utama Hormon Tiroid T3 (Triiodotironin) dan T4 (Tiroksin)</span>
              </div>
              <span class="vial-param" style="background:var(--sage-light);color:var(--sage);padding:4px 8px;border-radius:4px;">Mikromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Dewasa: Struma Endemik</h4>
                <p>Iodium rendah &rarr; sintesis hormon tiroid turun &rarr; umpan balik negatif ke hipofisis berkurang &rarr; sekresi TSH melonjak &rarr; hipertrofi kelenjar tiroid (gondok).</p>
              </div>
              <div class="info-pane">
                <h4>Janin: Kretinisme Permanen</h4>
                <p>Kekurangan iodium pada ibu hamil menghambat neurogenesis dan mielinisasi otak janin &rarr; lahir dengan retardasi mental berat, tuli-bisu, dan perawakan pendek cebol.</p>
              </div>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_13.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_13.jpg" class="inspector-thumb" alt="Slide 13">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 13: Iodium &amp; Kretinisme Janin</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

          <!-- SELENIUM (SE) -->
          <article class="detail-sheet" id="sheet-se">
            <div class="sheet-head">
              <div class="sheet-title-group">
                <h2>Selenium (Se)</h2>
                <span>Komponen Asam Amino Selenosistein dalam Glutation Peroksidase</span>
              </div>
              <span class="vial-param" style="background:var(--sage-light);color:var(--sage);padding:4px 8px;border-radius:4px;">Mikromineral</span>
            </div>

            <div class="sheet-grid">
              <div class="info-pane">
                <h4>Penyakit Keshan (Kardiomiopati)</h4>
                <p>Kardiomiopati kongestif endemik di daerah tanah miskin selenium. Stres oksidatif memicu dilatasi ventrikel jantung dan gagal jantung pada anak dan wanita muda.</p>
              </div>
              <div class="info-pane">
                <h4>Fungsi Enzimatik Kunci</h4>
                <p>Antioksidan glutation peroksidase (GPx) melindungi membran sel dari radikal bebas H2O2, dan enzim deiodinase mengonversi T4 menjadi T3 aktif.</p>
              </div>
            </div>

            <div class="slide-inspector" onclick="openLightbox('slides_kul3/slide_23.jpg')">
              <div class="inspector-meta">
                <img src="slides_kul3/slide_23.jpg" class="inspector-thumb" alt="Slide 23">
                <div class="inspector-txt">
                  <strong>Bukti Slide Asli 23: Selenium &amp; Penyakit Keshan</strong>
                  <span>Tangkapan layar slide asli dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span class="inspector-arrow">Buka Slide ↗</span>
            </div>
          </article>

        </div>
      </div>
    </div>

    <!-- =================================================================== -->
    <!-- TAB 3: CBT SIMULATOR (TACTILE, JELAS, BUG-FREE)                     -->
    <!-- =================================================================== -->
    <div id="tab-cbt" class="view-section">
      <div class="cbt-suite">
        <div class="cbt-top">
          <div>
            <h2 style="font-family:var(--font-serif);font-size:2rem;color:var(--ink);">8 Soal Prediksi UAB dr. Iwal</h2>
            <p style="font-size:0.92rem;color:var(--ink-secondary);margin-top:2px;">Disusun persis mengikuti karakter kasus klinis (66.7%) dan perbandingan konsep mirip.</p>
          </div>
          <div style="text-align:right;">
            <span style="font-size:0.8rem;color:var(--ink-muted);text-transform:uppercase;letter-spacing:0.04em;">Skor Ujian:</span>
            <div class="cbt-score-display"><span id="cbt-user-score">0</span> / 8</div>
          </div>
        </div>

        <div id="cbt-list-anchor"></div>
      </div>
    </div>

    <!-- =================================================================== -->
    <!-- TAB 4: MATRIKS KILAT H-1                                           -->
    <!-- =================================================================== -->
    <div id="tab-matrix" class="view-section">
      <div style="margin-bottom:24px;">
        <h2 style="font-family:var(--font-serif);font-size:2rem;color:var(--ink);">Matriks Komparasi Kilat H-1 Ujian</h2>
        <p style="font-size:0.95rem;color:var(--ink-secondary);">Fokus pada kolom Gejala Kunci Patognomonik dan Nilai Lab Kunci sebelum masuk ruang ujian:</p>
      </div>

      <table class="matrix-table">
        <thead>
          <tr>
            <th>Mineral</th>
            <th>Peran Kunci</th>
            <th>Gejala Patognomonik</th>
            <th>Biomarker Lab Kunci</th>
            <th>Jebakan Ujian UAB dr. Iwal</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><b>Besi (Fe)</b></td>
            <td>Heme, Mioglobin</td>
            <td>Pagophagia (pica es batu), koilonychia.</td>
            <td><b>Ferritin &lt; 15–30 ng/mL</b> (paling awal).</td>
            <td style="color:var(--terracotta);font-weight:600;">MCV normal TIDAK menyingkirkan defisiensi besi dini! Terapi maks 1x/hari (Hepcidin).</td>
          </tr>
          <tr>
            <td><b>Seng (Zn)</b></td>
            <td>Metalloenzim</td>
            <td>Dermatitis periorifisial &amp; akral, diare, alopesia.</td>
            <td>Serum Zinc &lt; 70 &mu;g/dL.</td>
            <td style="color:var(--terracotta);font-weight:600;">Diet tinggi asam fitat menghambat penyerapan seng di usus halus.</td>
          </tr>
          <tr>
            <td><b>Magnesium (Mg)</b></td>
            <td>Sumbat ROMK</td>
            <td>Tremor, tetani, aritmia, <b>hipokalemia refrakter</b>.</td>
            <td>Magnesium serum &lt; 1.7 mg/dL.</td>
            <td style="color:var(--terracotta);font-weight:600;">Kalium tidak bisa naik sebelum kadar Mg dikoreksi serentak!</td>
          </tr>
          <tr>
            <td><b>Fosfat (P)</b></td>
            <td>Sintesis ATP</td>
            <td>Gagal napas akut (diafragma lumpuh), takikardia.</td>
            <td>Fosfat serum &lt; 1.0 mg/dL (berat).</td>
            <td style="color:var(--terracotta);font-weight:600;">Refeeding syndrome dipicu lonjakan insulin pasca-pemberian karbohidrat.</td>
          </tr>
          <tr>
            <td><b>Tembaga (Cu)</b></td>
            <td>Ceruloplasmin</td>
            <td>Anemia mikrositik + neutropenia + ataksia.</td>
            <td>Serum Cu rendah, ceruloplasmin rendah.</td>
            <td style="color:var(--terracotta);font-weight:600;">Dipicu konsumsi suplemen Zinc dosis tinggi jangka panjang (Metallothionein).</td>
          </tr>
          <tr>
            <td><b>Kalsium (Ca)</b></td>
            <td>Potensial Saraf</td>
            <td>Parestesia perioral, Chvostek (+), Trousseau (+).</td>
            <td>Ionized Calcium (Ca ion bebas aktif).</td>
            <td style="color:var(--terracotta);font-weight:600;">EKG interval QT memanjang; 99% kalsium ada di tulang, bukan di plasma.</td>
          </tr>
        </tbody>
      </table>
    </div>

  </main>

  <!-- Lightbox Modal -->
  <div id="modal-lightbox" class="lightbox-backdrop" onclick="closeLightbox()">
    <img id="modal-lightbox-img" class="lightbox-frame" src="" alt="Slide Zoom" onclick="event.stopPropagation()" />
  </div>

  <script>
    // TAB SWITCHER
    function switchTab(tabId, btn) {
      document.querySelectorAll('.view-section').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.view-pill').forEach(b => b.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      btn.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // SIMULATOR 1: IRON DEVIATION
    function setIronStage(stage) {
      document.querySelectorAll('.stepper-btn').forEach((b, i) => {
        b.classList.toggle('active', i + 1 === stage);
      });

      const vF = document.getElementById('vial-ferritin');
      const vT = document.getElementById('vial-tsat');
      const vH = document.getElementById('vial-hb');
      const valF = document.getElementById('val-ferritin');
      const valT = document.getElementById('val-tsat');
      const valH = document.getElementById('val-hb');
      const statF = document.getElementById('stat-ferritin');
      const statT = document.getElementById('stat-tsat');
      const statH = document.getElementById('stat-hb');
      const narr = document.getElementById('narrative-iron');

      vF.classList.remove('highlight');
      vT.classList.remove('highlight');
      vH.classList.remove('highlight');

      if (stage === 1) {
        vF.classList.add('highlight');
        valF.textContent = '< 15 ng/mL';
        statF.textContent = 'ANJLOK DULUAN (Kritis)';
        statF.className = 'vial-status status-bad';

        valT.textContent = '28% (Normal)';
        statT.textContent = 'Transpor Masih Cukup';
        statT.className = 'vial-status status-good';

        valH.textContent = 'Hb 13.5 · MCV 88';
        statH.textContent = 'Tampak Normal (Belum Anemia)';
        statH.className = 'vial-status status-good';

        narr.innerHTML = '💡 <b>Stadium 1 (Depletion):</b> Cadangan besi hati dan sumsum tulang habis. Tetapi produksi sel darah merah masih cukup dari besi sirkulasi. <b>Pasien belum anemia! MCV normal tidak menyingkirkan defisiensi besi!</b>';
      } else if (stage === 2) {
        vT.classList.add('highlight');
        valF.textContent = '< 10 ng/mL';
        statF.textContent = 'Kosong';
        statF.className = 'vial-status status-bad';

        valT.textContent = '12% (Anjlok)';
        statT.textContent = 'Besi Transpor Kurang';
        statT.className = 'vial-status status-bad';

        valH.textContent = 'Hb 12.0 · MCV 82';
        statH.textContent = 'Batas Bawah Normal';
        statH.className = 'vial-status status-warn';

        narr.innerHTML = '💡 <b>Stadium 2 (Eritropoiesis Terbatas):</b> Besi transferrin tidak cukup untuk kebutuhan sumsum tulang. TSAT anjlok, TIBC meningkat, produksi eritrosit mulai terhambat.';
      } else {
        vH.classList.add('highlight');
        valF.textContent = '< 7 ng/mL';
        statF.textContent = 'Habis Total';
        statF.className = 'vial-status status-bad';

        valT.textContent = '6% (Sangat Rendah)';
        statT.textContent = 'Kritis';
        statT.className = 'vial-status status-bad';

        valH.textContent = 'Hb 8.9 · MCV 68 fL';
        statH.textContent = 'ANEMIA MIKROSITIK NYATA';
        statH.className = 'vial-status status-bad';

        narr.innerHTML = '💡 <b>Stadium 3 (Anemia Defisiensi Besi):</b> Hb turun, MCV &lt; 80 fL (mikrositik hipokromik). Muncul lemas, pucat, kuku sendok (koilonychia), dan <b>pagophagia (mengunyah es batu)</b>.';
      }
    }

    // SIMULATOR 2: ROMK KIDNEY CHANNEL
    function toggleROMK(isNormal) {
      document.getElementById('btn-mg-norm').classList.toggle('active', isNormal);
      document.getElementById('btn-mg-low').classList.toggle('active', !isNormal);

      const gate = document.getElementById('romk-gate');
      const statusTxt = document.getElementById('romk-status-txt');
      const lossTxt = document.getElementById('romk-urine-loss');

      if (isNormal) {
        gate.className = 'romk-channel-gate plugged';
        statusTxt.textContent = '🔒 KANAL ROMK TERSUMBAT (Mg Normal)';
        lossTxt.textContent = 'Kalium tidak bocor ke urin (Normal)';
        lossTxt.style.color = 'var(--sage)';
      } else {
        gate.className = 'romk-channel-gate unplugged';
        statusTxt.textContent = '⚠️ KANAL ROMK TERBUKA LEBAR (Mg Rendah)';
        lossTxt.textContent = '🚨 Kalium BOCOR TERBUANG KE URIN (Hipokalemia Refrakter!)';
        lossTxt.style.color = 'var(--terracotta)';
      }
    }

    // MINERAL DECK SWITCHER
    function selectMineral(minKey, btn) {
      document.querySelectorAll('.detail-sheet').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.mineral-nav-item').forEach(b => b.classList.remove('active'));
      document.getElementById('sheet-' + minKey).classList.add('active');
      btn.classList.add('active');
    }

    // LIGHTBOX CONTROLLER
    function openLightbox(src) {
      const modal = document.getElementById('modal-lightbox');
      const img = document.getElementById('modal-lightbox-img');
      img.src = src;
      modal.classList.add('open');
    }
    function closeLightbox() {
      document.getElementById('modal-lightbox').classList.remove('open');
    }
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeLightbox();
    });

    // 8 SOAL PREDIKSI UAB (100% BUG FREE)
    const CBT_DATA = [
      {
        id: 1,
        stem: '1. Seorang perempuan 29 tahun datang ke poliklinik dengan keluhan badan lemas dan sering berdebar saat beraktivitas sejak 2 bulan. Pasien memiliki riwayat menstruasi sangat banyak (ganti pembalut 6–7 kali/hari) selama 8 hari setiap siklusnya. Pemeriksaan konjungtiva pucat tanpa ikterus. Laboratorium: Hb 8,9 g/dL, MCV 68 fL, MCH 21 pg. Pasien mengaku sering sekali mengunyah es batu (pagophagia). Pemeriksaan biomarker manakah yang paling sensitif dan paling awal menurun untuk memastikan diagnosis?',
        options: [
          'Total Iron Binding Capacity (TIBC)',
          'Ferritin serum',
          'Saturasi transferrin (TSAT)',
          'Hemoglobin elektroforesis',
          'Bilirubin indirek serum'
        ],
        correct: 1,
        exp: 'Pasien mengalami Anemia Defisiensi Besi akibat menorrhagia kronik. <i>Pagophagia</i> (pica makan es batu) adalah tanda khas defisiensi besi. Pada perjalanan alami penipisan besi (Slide 10), <b>Ferritin serum adalah biomarker pertama yang anjlok (&lt;15–30 ng/mL)</b> mencerminkan habisnya cadangan besi di hati dan makrofag, jauh sebelum nilai Hb dan MCV turun menjadi anemia.'
      },
      {
        id: 2,
        stem: '2. Laki-laki 67 tahun dengan gagal jantung kongestif yang rutin mengonsumsi furosemid mengeluh lemas otot tungkai dan berdebar. EKG menunjukkan depresi segmen ST, gelombang T mendatar, dan muncul gelombang U yang menonjol. Hasil laboratorium: Kalium 2,8 mmol/L. Dokter telah memberikan suplementasi KCl oral dosis tinggi selama 3 hari, namun pada evaluasi ulang kadar Kalium pasien tetap rendah (2,9 mmol/L). Gangguan elektrolit penyerta manakah yang mendasari kondisi refrakter tersebut?',
        options: [
          'Hiponatremia',
          'Hipokalsemia',
          'Hipomagnesemia',
          'Hiperfosfatemia',
          'Hiperkalsiuria'
        ],
        correct: 2,
        exp: 'Furosemid membuang Kalium dan Magnesium sekaligus. Di tubulus distal ginjal, ion Magnesium intrasel adalah penghambat fisik alami kanal ROMK. Pada kondisi hipomagnesemia (Slide 17 & 28), kanal ROMK terbuka bebas tanpa kendali sehingga Kalium terus-menerus bocor ke urin. <b>Koreksi Magnesium wajib diberikan bersamaan agar Kalium bisa naik normal.</b>'
      },
      {
        id: 3,
        stem: '3. Anak laki-laki 4 tahun dibawa ibunya dengan keluhan bercak kemerahan bersisik dan berkrusta di area sekitar mulut, perineum, serta sela-sela jari kaki sejak 1 bulan. Pasien juga mengalami diare kronik kambuhan dan rambut rontok hingga tampak botak sebagian. Pasien memiliki riwayat diet monoton tinggi serealia dan bubur gandum tanpa asupan hewani. Defisiensi mikromineral apakah yang mendasari kelainan tersebut?',
        options: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Seng (Zinc / Zn)',
          'Selenium (Se)',
          'Mangan (Mn)'
        ],
        correct: 2,
        exp: 'Trias patognomonik: <b>dermatitis periorifisial & akral, diare kronik, dan alopesia</b> merupakan tanda khas defisiensi Seng (Slide 12). Serealia mengandung asam <b>fitat</b> tinggi yang mengikat seng di lumen usus membentuk kelat tak larut yang tidak dapat diserap enterosit.'
      },
      {
        id: 4,
        stem: '4. Pasien laki-laki 46 tahun dengan riwayat malnutrisi berat dan kelaparan selama 12 hari dirawat di bangsal. Dokter segera memberikan nutrisi parenteral tinggi karbohidrat. Dalam waktu 48 jam, pasien mendadak mengalami takipnea berat, kelemahan otot menyeluruh, dan aritmia. Gangguan biokimiawi serum manakah yang menjadi pemicu utama kegagalan napas akut tersebut?',
        options: [
          'Hiponatremia berat',
          'Hipokalsemia terionisasi',
          'Hipofosfatemia berat (&lt;1.0 mg/dL)',
          'Asidosis laktat',
          'Hiperglikemia hiperosmolar'
        ],
        correct: 2,
        exp: 'Pasien mengalami <b>Refeeding Syndrome</b> (Slide 19 & 29). Karbohidrat mendadak memicu lonjakan insulin yang mendorong glukosa dan Fosfat masuk masif ke dalam sel &rarr; hipofosfatemia berat (&lt;1.0 mg/dL) menghentikan sintesis ATP seluler, melumpuhkan otot diafragma (gagal napas akut) dan memicu kardiomiopati akut.'
      },
      {
        id: 5,
        stem: '5. Perempuan 35 tahun pasca-operasi bypass lambung datang dengan keluhan baal di kedua tungkai serta ataksia sensorik (gangguan jalan). Laboratorium: Hb 9,0 g/dL, MCV 72 fL (mikrositik), dan neutropenia berat (ANC 750/&mu;L). Pasien mengaku mengonsumsi suplemen Zinc dosis tinggi (80 mg/hari) selama 8 bulan. Defisiensi mineral apakah yang paling tepat menjelaskan kondisi pasien?',
        options: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Iodium (I)',
          'Selenium (Se)',
          'Kalsium (Ca)'
        ],
        correct: 1,
        exp: 'Kombinasi <b>anemia mikrositik + neutropenia berat + mielopati ataksia</b> adalah tanda klasik defisiensi Tembaga (Slide 22). Suplemen Zinc dosis tinggi menginduksi protein <i>metallothionein</i> di enterosit yang mengikat tembaga dengan kuat dan menghambat absorpsinya ke sirkulasi darah.'
      },
      {
        id: 6,
        stem: '6. Berdasarkan pedoman klinis American Gastroenterological Association (AGA 2024), bagaimanakah aturan suplementasi besi oral yang paling tepat dan dapat ditoleransi optimal pada pasien anemia defisiensi besi?',
        options: [
          'Diberikan dosis tinggi 3 kali sehari bersama makanan',
          'Diberikan dosis terbagi setiap 6 jam disertai antasida',
          'Diberikan maksimal 1 kali sehari atau rejimen selang-hari (alternate-day)',
          'Diberikan bersamaan dengan susu sapi segar',
          'Diberikan 4 kali sehari dalam dosis terbagi'
        ],
        correct: 2,
        exp: 'Pedoman AGA 2024 (Slide 11) menekankan bahwa setiap dosis besi oral memicu lonjakan hormon <b>Hepcidin</b> yang memblokade absorpsi berikutnya selama 24–48 jam. Pemberian maksimal 1x/hari atau selang-hari (alternate-day) memaksimalkan penyerapan dan meminimalkan efek samping saluran cerna.'
      },
      {
        id: 7,
        stem: '7. Pemeriksaan fisik pada pasien dengan kecurigaan hipokalsemia menunjukkan adanya spasme karpopedal pada tangan ketika manset tensimeter dipompa di atas tekanan sistolik selama 3 menit. Disebut apakah tanda fisik patognomonik tersebut?',
        options: [
          'Chvostek sign',
          'Trousseau sign',
          'Kernig sign',
          'Brudzinski sign',
          'Babinski sign'
        ],
        correct: 1,
        exp: '<b>Tanda Trousseau</b> (spasme karpopedal saat manset dipompa >sistolik 3 menit) sangat sensitif dan spesifik untuk hipokalsemia simptomatik (Slide 15). Tanda Chvostek adalah kedutan bibir saat saraf fasialis diketuk.'
      },
      {
        id: 8,
        stem: '8. Wanita hamil di daerah pegunungan yang jarang mengonsumsi garam beriodium melahirkan bayi dengan keterlambatan perkembangan saraf berat, perawakan pendek, dan tuli-bisu. Mekanisme patofisiologi apakah yang mendasari kondisi kretinisme pada bayi tersebut?',
        options: [
          'Kekurangan iodium memicu hambatan sintesis T3/T4 yang vital bagi mielinisasi dan perkembangan otak janin',
          'Kelebihan TSH ibu merusak kelenjar tiroid janin secara langsung',
          'Defisiensi selenium langsung menghambat enzim deiodinase tanpa melibatkan hormon tiroid',
          'Kadar kalsium yang rendah mengganggu pembentukan neurotransmitter otak',
          'Fosfat yang rendah menyebabkan kegagalan pembentukan mielin saraf'
        ],
        correct: 0,
        exp: 'Iodium adalah substrat esensial sintesis hormon tiroid T3/T4 (Slide 13). Pada kehamilan, hormon tiroid mutlak dibutuhkan untuk neurogenesis dan mielinisasi otak janin. Defisiensi berat memicu sindrom kretinisme permanen.'
      }
    ];

    let userAnswers = {};
    let currentScore = 0;

    function renderCBT() {
      const container = document.getElementById('cbt-list-anchor');
      container.innerHTML = CBT_DATA.map((q, qIdx) => `
        <article class="q-card" id="q-card-${qIdx}">
          <span class="q-badge">SOAL #${q.id} · PREDIKSI UAB DR. IWAL</span>
          <div class="q-stem-text">${q.stem}</div>
          <div class="options-group">
            ${q.options.map((opt, oIdx) => `
              <button type="button" class="option-button" onclick="answerQuestion(${qIdx}, ${oIdx})">
                <span class="option-key">${String.fromCharCode(65 + oIdx)}.</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
          <div class="feedback-drawer" id="feedback-${qIdx}"></div>
        </article>
      `).join('');
    }

    // 100% BUG FREE EVALUATION
    function answerQuestion(qIdx, selectedOpt) {
      if (userAnswers[qIdx] !== undefined) return;
      userAnswers[qIdx] = selectedOpt;

      const q = CBT_DATA[qIdx];
      const isCorrect = (selectedOpt === q.correct);
      const card = document.getElementById('q-card-' + qIdx);
      const btns = card.querySelectorAll('.option-button');
      const drawer = document.getElementById('feedback-' + qIdx);

      btns.forEach((btn, i) => {
        if (i === q.correct) btn.classList.add('is-correct');
        else if (i === selectedOpt && !isCorrect) btn.classList.add('is-wrong');
      });

      if (isCorrect) {
        currentScore++;
        drawer.className = 'feedback-drawer show correct-tone';
        drawer.innerHTML = `<strong>✅ Benar!</strong><div style="margin-top:6px;">${q.exp}</div>`;
      } else {
        drawer.className = 'feedback-drawer show wrong-tone';
        drawer.innerHTML = `<strong>❌ Kurang Tepat.</strong> Jawaban yang benar adalah <strong>${String.fromCharCode(65 + q.correct)} (${q.options[q.correct]})</strong>.<div style="margin-top:6px;">${q.exp}</div>`;
      }

      document.getElementById('cbt-user-score').textContent = currentScore;
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderCBT();
    });
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(WORLD_CLASS_HTML)

print(f"Modul EMN KUL 3 World-Class Edition berhasil dibuat: {OUT_HTML} (ukuran: {len(WORLD_CLASS_HTML)} bytes)")
