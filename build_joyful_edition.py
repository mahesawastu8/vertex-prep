#!/usr/bin/env python3
"""Build a Joyful, Calm, Human-Crafted Medical Learning Edition for EMN KUL 3 Defisiensi Mineral.
Eliminates all AI-slop visual tropes:
- No fake dotted grids, no aggressive marketing hero banners, no emoji clutter
- Warm paper palette (#FDFCF7, #1A1A1A, Sage, Warm Coral, Honey Ochre)
- Apple Books / Amboss / Notion aesthetic: serene, distraction-free, deeply readable
- Seamless interactive features: AMBOSS Tooltips, Active Cloze Mode, UWorld Confidence, Cross-Block Bridges
"""
import os
import json

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

# Helper for AMBOSS Medical Tooltips
def tt(term, title, desc, pearl):
    return f"""<span class="med-term" tabindex="0">{term}<span class="med-tooltip"><span class="tt-kicker">Catatan Klinis</span><span class="tt-title">{title}</span><span class="tt-desc">{desc}</span><span class="tt-pearl">💡 {pearl}</span></span></span>"""

# Helper for Cloze Masking (Osmosis active recall)
def cl(text):
    return f"""<span class="cloze-mask" onclick="this.classList.toggle('revealed')" title="Klik untuk membuka">{text}</span>"""

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Mineral · Modul Belajar EMN</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #FAF8F5;
      --surface: #FFFFFF;
      --surface-hover: #F5F3ED;
      --border: #E8E5DC;
      --border-focus: #2D6A4F;
      
      --ink: #1F2022;
      --ink-secondary: #5C5E62;
      --ink-muted: #8E9094;
      
      --sage: #2D6A4F;
      --sage-light: #EBF4EF;
      --coral: #C84B31;
      --coral-light: #FBEFEA;
      --ochre: #B87333;
      --ochre-light: #FAF2EA;
      --navy: #1D3557;
      --navy-light: #EDF2F7;
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-full: 999px;
      
      --shadow-sm: 0 1px 3px rgba(31, 32, 34, 0.04);
      --shadow-md: 0 4px 12px rgba(31, 32, 34, 0.06);
      --shadow-lg: 0 12px 32px rgba(31, 32, 34, 0.08);
      
      --font-serif: 'Newsreader', Georgia, serif;
      --font-sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    
    body {{
      background-color: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 80px;
    }}

    /* Global Typography Selection */
    ::selection {{ background: #D8EADF; color: #1F2022; }}

    /* Top Navigation Header */
    .top-header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(250, 248, 245, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
    }}
    .nav-inner {{
      max-width: 1060px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .nav-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .nav-title-group {{
      display: flex;
      flex-direction: column;
    }}
    .nav-super {{
      font-size: 0.74rem;
      font-weight: 600;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--sage);
    }}
    .nav-course-select {{
      font-family: var(--font-sans);
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--ink);
      background: transparent;
      border: none;
      cursor: pointer;
      outline: none;
    }}

    .nav-modes {{
      display: flex;
      background: rgba(232, 229, 220, 0.6);
      padding: 3px;
      border-radius: var(--radius-full);
      gap: 2px;
    }}
    .mode-btn {{
      border: none;
      background: transparent;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--ink-secondary);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.2s ease;
      white-space: nowrap;
    }}
    .mode-btn:hover {{ color: var(--ink); }}
    .mode-btn.active {{
      background: var(--surface);
      color: var(--ink);
      box-shadow: var(--shadow-sm);
    }}

    .nav-right {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    /* Controls & Toggles */
    .btn-toggle {{
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--ink-secondary);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
    }}
    .btn-toggle:hover {{
      border-color: var(--sage);
      color: var(--ink);
    }}
    .btn-toggle.active {{
      background: #1F2022;
      color: #FFFFFF;
      border-color: #1F2022;
    }}
    .badge-status {{
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 1px 6px;
      border-radius: 4px;
      background: var(--bg);
      color: var(--ink);
    }}
    .btn-toggle.active .badge-status {{
      background: var(--sage);
      color: #FFFFFF;
    }}

    .btn-anki {{
      background: var(--sage);
      color: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      text-decoration: none;
      transition: opacity 0.2s ease;
    }}
    .btn-anki:hover {{ opacity: 0.9; }}

    /* Layout Shell */
    .shell {{
      max-width: 820px;
      margin: 0 auto;
      padding: 40px 24px 0;
    }}

    /* Calm Article Header */
    .article-header {{
      margin-bottom: 48px;
    }}
    .meta-tag {{
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--sage);
      background: var(--sage-light);
      padding: 3px 10px;
      border-radius: var(--radius-full);
      margin-bottom: 14px;
    }}
    .article-title {{
      font-family: var(--font-serif);
      font-size: 2.6rem;
      font-weight: 700;
      line-height: 1.25;
      color: var(--ink);
      letter-spacing: -0.015em;
      margin-bottom: 14px;
    }}
    .article-subtitle {{
      font-size: 1.1rem;
      color: var(--ink-secondary);
      line-height: 1.6;
    }}
    .author-bar {{
      margin-top: 20px;
      padding-top: 18px;
      border-top: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.85rem;
      color: var(--ink-muted);
    }}

    /* Study View Sections */
    .study-pane {{ display: none; }}
    .study-pane.active {{ display: block; }}

    /* Natural Reading Chapters (Editorial Flow) */
    .chapter-section {{
      margin-bottom: 56px;
    }}
    .chapter-title {{
      font-family: var(--font-serif);
      font-size: 1.7rem;
      font-weight: 600;
      color: var(--ink);
      letter-spacing: -0.01em;
      margin-bottom: 12px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }}
    .chapter-body p {{
      margin-bottom: 18px;
      color: #2D2F33;
    }}

    /* High-Yield Callout Boxes (Warm, subtle, non-screaming) */
    .callout-pearl {{
      background: var(--ochre-light);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 24px 0;
      position: relative;
    }}
    .callout-title {{
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ochre);
      margin-bottom: 6px;
    }}
    .callout-body {{
      font-size: 0.95rem;
      line-height: 1.65;
      color: #3A2E1D;
    }}

    .callout-danger {{
      background: var(--coral-light);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 24px 0;
    }}
    .danger-title {{
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--coral);
      margin-bottom: 6px;
    }}
    .danger-body {{
      font-size: 0.95rem;
      line-height: 1.65;
      color: #3B1C16;
    }}

    /* Clean Editorial Tables */
    .table-wrap {{
      overflow-x: auto;
      margin: 24px 0;
      background: var(--surface);
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
    }}
    .reading-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      line-height: 1.5;
    }}
    .reading-table th {{
      background: #F5F3EC;
      text-align: left;
      padding: 12px 16px;
      font-weight: 600;
      color: var(--ink);
      border-bottom: 1px solid var(--border);
    }}
    .reading-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
      color: #2D2F33;
    }}
    .reading-table tr:last-child td {{ border-bottom: none; }}
    .reading-table tr:hover td {{ background: #FAF9F6; }}

    /* Human Slide Evidence Cards */
    .slide-evidence {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px;
      margin: 24px 0;
      display: flex;
      align-items: center;
      gap: 16px;
      cursor: pointer;
      transition: all 0.2s ease;
    }}
    .slide-evidence:hover {{
      border-color: var(--sage);
      box-shadow: var(--shadow-sm);
      transform: translateY(-1px);
    }}
    .evidence-thumb {{
      width: 100px;
      height: 64px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
      flex: none;
    }}
    .evidence-meta {{
      flex: 1;
    }}
    .evidence-num {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .evidence-title {{
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--ink);
      margin-top: 2px;
    }}
    .evidence-hint {{
      font-size: 0.8rem;
      color: var(--ink-muted);
      margin-top: 2px;
    }}

    /* 1. AMBOSS SMART MEDICAL TOOLTIPS */
    .med-term {{
      border-bottom: 1.5px dotted var(--navy);
      color: var(--navy);
      font-weight: 600;
      cursor: help;
      position: relative;
      display: inline-block;
      transition: background 0.15s ease;
    }}
    .med-term:hover {{
      background: var(--navy-light);
      border-radius: 3px;
    }}
    .med-tooltip {{
      visibility: hidden;
      opacity: 0;
      position: absolute;
      bottom: 135%;
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      width: 290px;
      background: #1A1A1A;
      color: #FFFFFF;
      border-radius: var(--radius-md);
      padding: 14px 16px;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 400;
      line-height: 1.5;
      box-shadow: var(--shadow-lg);
      z-index: 500;
      pointer-events: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      text-align: left;
    }}
    .med-tooltip::after {{
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      margin-left: -6px;
      border-width: 6px;
      border-style: solid;
      border-color: #1A1A1A transparent transparent transparent;
    }}
    .med-term:hover .med-tooltip,
    .med-term:focus .med-tooltip {{
      visibility: visible;
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}
    .tt-kicker {{
      font-size: 0.68rem;
      font-weight: 700;
      color: #A3D9C9;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      display: block;
      margin-bottom: 2px;
    }}
    .tt-title {{
      font-size: 0.92rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 4px;
      display: block;
    }}
    .tt-desc {{
      color: #D6D6D6;
      display: block;
    }}
    .tt-pearl {{
      margin-top: 8px;
      padding-top: 8px;
      border-top: 1px solid #333333;
      color: #F8E7C9;
      font-size: 0.78rem;
      display: block;
    }}

    /* 2. OSMOSIS ACTIVE CLOZE MASKING */
    body.cloze-active .cloze-mask {{
      background: #E8E5DC !important;
      color: transparent !important;
      border-radius: 4px;
      padding: 1px 6px;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
      display: inline-block;
    }}
    body.cloze-active .cloze-mask:hover {{
      background: #D8D4C8 !important;
    }}
    body.cloze-active .cloze-mask.revealed {{
      background: var(--sage-light) !important;
      color: var(--sage) !important;
      font-weight: 600;
      padding: 1px 6px;
      border-radius: 4px;
    }}

    /* 3. UWORLD CBT QUESTIONS WITH METRICS */
    .cbt-container {{
      margin-top: 24px;
    }}
    .diag-dashboard {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin-bottom: 32px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }}
    .diag-card {{
      display: flex;
      flex-direction: column;
    }}
    .diag-val {{
      font-family: var(--font-mono);
      font-size: 1.5rem;
      font-weight: 700;
      line-height: 1.2;
    }}
    .diag-lbl {{
      font-size: 0.78rem;
      color: var(--ink-secondary);
      margin-top: 4px;
    }}

    .q-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .q-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}
    .q-number {{
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--ink-muted);
    }}
    .confidence-picker {{
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 0.8rem;
      color: var(--ink-secondary);
    }}
    .conf-btn {{
      border: 1px solid var(--border);
      background: transparent;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      color: var(--ink-secondary);
      transition: all 0.15s ease;
    }}
    .conf-btn.active-high {{
      background: var(--sage);
      color: #FFFFFF;
      border-color: var(--sage);
    }}
    .conf-btn.active-low {{
      background: var(--ochre);
      color: #FFFFFF;
      border-color: var(--ochre);
    }}

    .q-stem {{
      font-size: 1.02rem;
      font-weight: 500;
      line-height: 1.7;
      color: var(--ink);
      margin-bottom: 20px;
    }}

    .q-options-stack {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .opt-choice {{
      padding: 12px 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      background: var(--surface);
      text-align: left;
      font-family: var(--font-sans);
      font-size: 0.94rem;
      color: var(--ink);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.15s ease;
    }}
    .opt-choice:hover {{
      background: #FAF8F5;
      border-color: #BDB7AB;
    }}
    .opt-key-txt {{
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--ink-muted);
      flex: none;
    }}
    .opt-choice.is-correct {{
      background: var(--sage-light);
      border-color: var(--sage);
      color: #174230;
      font-weight: 600;
    }}
    .opt-choice.is-wrong {{
      background: var(--coral-light);
      border-color: var(--coral);
      color: #7A2818;
    }}

    .q-explanation-box {{
      margin-top: 20px;
      padding: 18px 20px;
      background: #F7F5EE;
      border-radius: var(--radius-sm);
      font-size: 0.92rem;
      line-height: 1.65;
      display: none;
    }}
    .q-explanation-box.show {{
      display: block;
    }}
    .outcome-pill {{
      display: inline-block;
      font-size: 0.78rem;
      font-weight: 700;
      padding: 2px 10px;
      border-radius: var(--radius-full);
      margin-bottom: 10px;
    }}
    .pill-mastered {{ background: var(--sage-light); color: var(--sage); }}
    .pill-lucky {{ background: var(--ochre-light); color: var(--ochre); }}
    .pill-danger {{ background: var(--coral-light); color: var(--coral); }}
    .pill-gap {{ background: var(--navy-light); color: var(--navy); }}

    /* 4. CROSS-BLOCK CLINICAL BRIDGE */
    .bridge-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px;
      margin-bottom: 24px;
    }}
    .bridge-tabs {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin: 20px 0 24px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }}
    .bridge-tab-btn {{
      background: transparent;
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--ink-secondary);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .bridge-tab-btn:hover {{
      border-color: var(--ink);
      color: var(--ink);
    }}
    .bridge-tab-btn.active {{
      background: var(--navy);
      color: #FFFFFF;
      border-color: var(--navy);
    }}
    .bridge-pane {{ display: none; }}
    .bridge-pane.active {{ display: block; }}
    
    .bridge-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 16px;
      margin-top: 16px;
    }}
    .bridge-box {{
      background: #FAF8F5;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 18px;
    }}
    .bridge-tag {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
      margin-bottom: 8px;
    }}
    .tag-emn {{ background: var(--sage-light); color: var(--sage); }}
    .tag-bms {{ background: var(--navy-light); color: var(--navy); }}
    .tag-hi  {{ background: var(--coral-light); color: var(--coral); }}
    .tag-bdt {{ background: var(--ochre-light); color: var(--ochre); }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(26, 26, 26, 0.75);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .lightbox-modal.open {{ display: flex; }}
    .lightbox-img {{
      max-width: 90%;
      max-height: 85vh;
      border-radius: 8px;
      box-shadow: var(--shadow-lg);
    }}

    @media (max-width: 768px) {{
      .article-title {{ font-size: 2rem; }}
      .diag-dashboard {{ grid-template-columns: 1fr 1fr; }}
      .nav-modes {{ display: none; }}
    }}
  </style>
</head>
<body>

  <!-- Minimalist Sticky Navigation Header -->
  <header class="top-header">
    <div class="nav-inner">
      <div class="nav-left">
        <div class="nav-title-group">
          <span class="nav-super">Blok 9 EMN · Kuliah 3</span>
          <select class="nav-course-select" onchange="window.location.href=this.value">
            <option value="EMN_KUL3_Defisiensi_Mineral.html" selected>Defisiensi Mineral (dr. Iwal, Sp.PD)</option>
            <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html">Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
            <option value="BDT_KUL3_Patient_Safety.html">Patient Safety (dr. Riskiyah)</option>
          </select>
        </div>
      </div>

      <nav class="nav-modes">
        <button type="button" class="mode-btn active" onclick="switchView('view-materi', this)">Rangkuman Materi</button>
        <button type="button" class="mode-btn" onclick="switchView('view-bridge', this)">Jembatan Lintas Blok</button>
        <button type="button" class="mode-btn" onclick="switchView('view-cbt', this)">Latihan CBT (8)</button>
        <button type="button" class="mode-btn" onclick="switchView('view-flash', this)">Matriks Cek H-1</button>
      </nav>

      <div class="nav-right">
        <!-- Feature 2: Active Masking Toggle -->
        <button type="button" id="cloze-toggle" class="btn-toggle" onclick="toggleCloze()" title="Tekan M di keyboard untuk toggle">
          <span>Uji Ingatan</span>
          <span class="badge-status" id="cloze-status">OFF</span>
        </button>
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-anki" download>Deck Anki</a>
      </div>
    </div>
  </header>

  <main class="shell">

    <!-- =================================================================== -->
    <!-- VIEW 1: RANGKUMAN MATERI EDITORIAL (ENAK & NYAMAN DIBACA)           -->
    <!-- =================================================================== -->
    <div id="view-materi" class="study-pane active">
      
      <div class="article-header">
        <span class="meta-tag">Catatan Kuliah Pakar</span>
        <h1 class="article-title">Defisiensi Mineral: Patofisiologi, Peta Klinis, dan Keputusan Terapi</h1>
        <p class="article-subtitle">Rangkuman komprehensif 32 slide dr. Iwal Reza Ahdi, Sp.PD-FINASIM. Disusun terfokus pada mekanisme sebab-akibat, interpretasi biomarker laboratorium, dan jebakan ujian UAB.</p>
        <div class="author-bar">
          <span>Narasumber: <b>dr. Iwal Reza Ahdi, Sp.PD-FINASIM</b></span>
          <span>Target Evaluasi: <b>4 Soal Kasus UAB</b></span>
        </div>
      </div>

      <!-- BAB 1 -->
      <section class="chapter-section">
        <h2 class="chapter-title">1. Klasifikasi Mineral &amp; Homeostasis Tubuh</h2>
        <div class="chapter-body">
          <p>Kebutuhan harian suatu mineral tidak menentukan tingkat kepentingannya bagi kelangsungan hidup. Mineral esensial terbagi menjadi dua kelompok besar:</p>
          
          <div class="table-wrap">
            <table class="reading-table">
              <thead>
                <tr>
                  <th>Kelompok</th>
                  <th>Daftar Mineral</th>
                  <th>Karakteristik &amp; Peran Fisiologis</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>Makromineral</b></td>
                  <td>{cl("Ca, P, Mg, Na, K, Cl")}</td>
                  <td>Dibutuhkan dalam jumlah gram per hari. Berperan dalam struktur kristal tulang dan gigi, pembentukan gradien potensial aksi saraf dan otot, serta menjaga osmolaritas kompartemen cairan.</td>
                </tr>
                <tr>
                  <td><b>Mikromineral (Trace)</b></td>
                  <td>{cl("Fe, Zn, I, Se, Cu, Mn")}</td>
                  <td>Dibutuhkan dalam miligram atau mikrogram per hari. Bertindak sebagai kofaktor enzim reaksi redoks seluler, sintesis DNA, serta struktur hormon tiroid.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <p>Kadar mineral dalam serum darah hanyalah cerminan kompartemen transport. Penurunan konsentrasi serum tidak selalu berarti tubuh kekurangan asupan makanan. Empat mekanisme yang mendasari defisiensi klinis meliputi:</p>
          <ul style="padding-left: 20px; margin-bottom: 18px; color: #2D2F33;">
            <li><b>Asupan rendah:</b> Diet monoton, kelaparan, atau kebutuhan fisiologis yang meningkat pesat (misal kehamilan dan masa pertumbuhan anak).</li>
            <li><b>Malabsorpsi usus:</b> Kerusakan mukosa usus halus akibat penyakit celiac, pemotongan saluran cerna pasca-operasi bariatrik, atau infeksi diare kronik.</li>
            <li><b>Kehilangan berlebih:</b> Perdarahan haid yang banyak (menorrhagia), perdarahan saluran cerna terselubung, atau kehilangan lewat ginjal akibat obat diuretik.</li>
            <li><b>Redistribusi kompartemen:</b> Pergeseran elektrolit dari ekstraseluler masuk ke intraseluler, seperti pada {tt("Refeeding syndrome", "Refeeding Syndrome", "Krisis metabolik akibat pemberian makan terburu-buru pasca-malnutrisi berat.", "Lonjakan insulin mendorong glukosa, fosfat, kalium, dan magnesium masuk ke dalam sel secara serentak -> memicu hipofosfatemia berat (<1.0 mg/dL).")}, terapi insulin pada DKA, atau kondisi alkalosis metabolik.</li>
          </ul>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_5.jpg')">
            <img src="slides_kul3/slide_5.jpg" class="evidence-thumb" alt="Slide 5" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 5 &amp; 6</span>
              <div class="evidence-title">Bagan Homeostasis: Usus, Darah, Jaringan, dan Ginjal</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

      <!-- BAB 2 -->
      <section class="chapter-section">
        <h2 class="chapter-title">2. Besi (Fe): Perjalanan Defisiensi &amp; Panduan Terapi AGA 2024</h2>
        <div class="chapter-body">
          <p>Besi memiliki peran vital dalam transpor oksigen (sebagai inti heme hemoglobin dan mioglobin) serta enzim rantai pernapasan sitokrom mitokondria. Karena tubuh tidak memiliki mekanisme aktif untuk mengekskresikan kelebihan besi, homeostasis diatur ketat di tingkat penyerapan usus oleh hormon {tt("Hepcidin", "Hepcidin", "Hormon peptida hati pengatur utama besi sistemik.", "Mengunci dan mendegradasi ferroportin di enterosit usus dan makrofag, sehingga pelepasan besi ke sirkulasi terhenti selama 24–48 jam.")}.</p>

          <p>Penipisan besi terjadi dalam tiga stadium berurutan. Sangat penting diingat untuk ujian UAB bahwa <b>nilai MCV dan Hb yang normal tidak menyingkirkan defisiensi besi stadium dini</b>:</p>

          <div class="table-wrap">
            <table class="reading-table">
              <thead>
                <tr>
                  <th>Stadium</th>
                  <th>Kondisi Cadangan Besi</th>
                  <th>Profil Laboratorium Kunci</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>Stadium 1: Cadangan Turun (Depletion)</b></td>
                  <td>Besi di makrofag hati dan sumsum tulang habis. Eritrosit baru masih bisa dibuat normal dari besi sirkulasi.</td>
                  <td><b>{cl("Ferritin serum turun (&lt;15–30 ng/mL)")}</b>. Kadar Hb dan MCV masih dalam rentang normal.</td>
                </tr>
                <tr>
                  <td><b>Stadium 2: Eritropoiesis Terbatas</b></td>
                  <td>Besi yang berikatan dengan transferrin tidak mencukupi untuk kecepatan produksi eritrosit di sumsum tulang.</td>
                  <td><b>{cl("Saturasi transferrin (TSAT) anjlok (&lt;16–20%)")}</b>, TIBC meningkat, sTfR mulai naik. Hb berada di ambang batas bawah.</td>
                </tr>
                <tr>
                  <td><b>Stadium 3: Anemia Defisiensi Besi (IDA)</b></td>
                  <td>Cadangan dan sirkulasi habis total, memicu sintesis eritrosit yang kecil dan pucat.</td>
                  <td><b>{cl("Hb turun (&lt;12 g/dL)")}</b>, <b>{cl("MCV mikrositik (&lt;80 fL)")}</b>, MCH hipokromik. Muncul gejala lelah, koilonychia, dan {tt("Pagophagia", "Pagophagia", "Bentuk pica spesifik berupa dorongan tak tertahankan untuk mengunyah es batu.", "Merupakan tanda klinis patognomonik defisiensi besi; mekanismenya berkaitan dengan aktivasi sirkulasi serebral.")}.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="callout-pearl">
            <div class="callout-title">Pembaruan Terapi Klinis: Konsensus AGA 2024 (Slide 11)</div>
            <div class="callout-body">
              Pemberian tablet besi oral (ferrous sulfate/fumarate) <b>dilarang diberikan 3 kali sehari</b>. Setiap asupan besi merangsang sekresi hormon hepcidin di hati yang bertahan selama 24–48 jam. Dosis kedua dan ketiga tidak akan terserap di usus dan hanya memicu efek samping mual, kram lambung, serta konstipasi hitam pekat.<br>
              <b>Rekomendasi Mutakhir:</b> Berikan besi oral {cl("maksimal 1 kali per hari di pagi hari saat lambung kosong")}, atau gunakan rejimen <b>selang-hari (alternate-day)</b> untuk memaksimalkan absorpsi fraksional dan toleransi pasien.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_10.jpg')">
            <img src="slides_kul3/slide_10.jpg" class="evidence-thumb" alt="Slide 10" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 10 &amp; 11</span>
              <div class="evidence-title">Perjalanan Alami Defisiensi Besi &amp; Protokol Suplementasi AGA 2024</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

      <!-- BAB 3 -->
      <section class="chapter-section">
        <h2 class="chapter-title">3. Seng (Zn): Integritas Epitel Kulit &amp; Interaksi Fitat</h2>
        <div class="chapter-body">
          <p>Seng adalah kofaktor untuk lebih dari 300 enzim metalloenzim, termasuk RNA polimerase, DNA polimerase, alkalin fosfatase, serta protein jari-seng (zinc fingers) yang mengatur ekspresi gen. Oleh karena itu, jaringan dengan laju pembelahan sel tertinggi (kulit, mukosa usus, dan sistem imun) paling cepat terdampak saat terjadi kekurangan seng.</p>

          <p>Trias klinis khas defisiensi seng yang sering keluar dalam soal skenario kasus adalah:</p>
          <ul style="padding-left: 20px; margin-bottom: 18px; color: #2D2F33;">
            <li><b>{cl("Dermatitis periorifisial dan akral:")}</b> Bercak eritematosa bersisik, vesikobulosa, dan berkrusta di sekeliling mulut, hidung, anus, serta ujung jari tangan dan kaki. Kondisi ini identik dengan kelainan genetik {tt("Acrodermatitis enteropathica", "Acrodermatitis Enteropathica", "Kelainan resesif langka akibat mutasi transporter seng ZIP4 di enterosit usus.", "Menyebabkan kegagalan penyerapan seng makanan; diobati dengan suplementasi seng oral dosis tinggi seumur hidup.")}.</li>
            <li><b>Diare kronik:</b> Akibat atrofi mikrovili epitel mukosa usus halus.</li>
            <li><b>Alopesia:</b> Kerontokan rambut menyeluruh akibat gangguan pembelahan folikel rambut.</li>
          </ul>

          <div class="callout-pearl">
            <div class="callout-title">Faktor Inhibitor Absorpsi: Asam Fitat (Slide 12)</div>
            <div class="callout-body">
              {tt("Fitat", "Asam Fitat (Inositol Hexakisphosphate)", "Senyawa organik pengikat fosfor yang melimpah pada kulit ari gandum, beras merah, kedelai, dan serealia.", "Fitat mengikat kation divalen (Zn2+, Fe2+, Ca2+) membentuk kompleks kelat tak larut di pH lumen duodenum yang tidak dapat diserap enterosit usus.")} pada makanan serealia dan bubur gandum mentah adalah musuh utama penyerapan seng. Diet tinggi nabati tanpa protein hewani membuat seng tidak dapat diserap tubuh.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_12.jpg')">
            <img src="slides_kul3/slide_12.jpg" class="evidence-thumb" alt="Slide 12" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 12</span>
              <div class="evidence-title">Seng (Zn): Pertumbuhan, Kulit, Imunitas, dan Faktor Risiko Fitat</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

      <!-- BAB 4 -->
      <section class="chapter-section">
        <h2 class="chapter-title">4. Kalsium (Ca) &amp; Magnesium (Mg): Eksitabilitas Saraf &amp; Hubungan ROMK Ginjal</h2>
        <div class="chapter-body">
          <p>Hampir 99% kalsium tubuh tersimpan dalam matriks hidroksiapatit tulang, sedangkan kalsium dalam plasma berada dalam tiga bentuk: terikat albumin (40%), membentuk kompleks anion (10%), dan <b>kalsium ionisasi bebas (50%)</b>. Hanya kalsium ionisasi yang aktif secara fisiologis mengatur potensial ambang membran sel saraf dan eksitasi kontraksi otot.</p>

          <p>Pada kondisi hipokalsemia akut, ambang batas potensial aksi saraf turun mendekati potensial istirahat, memicu hipereksitabilitas neuromuskular berupa:</p>
          <ul style="padding-left: 20px; margin-bottom: 18px; color: #2D2F33;">
            <li>Parestesia perioral (kesemutan di sekitar bibir) dan ujung jari.</li>
            <li>{tt("Chvostek sign", "Tanda Chvostek", "Respon kedutan involunter pada otot sudut mulut atau wajah saat nervus fasialis diketuk ringan tepat di anterior tragus telinga.", "Tanda fisik sensitif hipokalsemia simptomatik.")}: kedutan sudut bibir saat saraf fasialis diketuk.</li>
            <li>{tt("Trousseau sign", "Tanda Trousseau", "Spasme karpopedal yang muncul saat manset sfigmomanometer dipompa 20 mmHg di atas tekanan darah sistolik selama 3 menit.", "Lebih spesifik dibanding Chvostek; iskemia transien memicu spasme fleksi sendi metakarpofalangeal dan adduksi ibu jari (main d'accoucheur).")}: spasme karpopedal saat manset tensimeter dipompa.</li>
            <li>Gambaran EKG menunjukkan {cl("pemanjangan interval QT")} yang berisiko memicu aritmia ventrikel.</li>
          </ul>

          <div class="callout-danger">
            <div class="danger-title">Mekanisme Ginjal Kritis: Mengapa Kalium Susah Naik Bila Magnesium Rendah? (Slide 17)</div>
            <div class="danger-body">
              Pada pasien hipokalemia yang sudah diberikan kalium oral atau infus KCl tetapi kadar kalium darahnya tidak kunjung normal, <b>penyebab utamanya adalah hipomagnesemia tersembunyi</b> ({cl("&lt;1.7 mg/dL")}).<br><br>
              <b>Patofisiologi Molekuler:</b> Di dalam sel tubulus ginjal, ion Magnesium intraseluler bertindak sebagai penghambat fisik alami pada kanal {tt("ROMK", "Renal Outer Medullary Potassium Channel", "Kanal transpor sekresi ion Kalium utama di membran apikal sel prinsipal tubulus distal dan duktus koligentes ginjal.", "Dihambat oleh magnesium intraseluler. Bila magnesium rendah, kanal ROMK terbuka bebas tanpa rem, menyebabkan kalium bocor keluar terus-menerus ke dalam urin.")}. Saat kadar magnesium anjlok, kanal ROMK terbuka lebar tanpa kendali &rarr; kalium terus-menerus disekresikan dan dibuang ke urin.<br><br>
              <b>Keputusan Klinis:</b> Kalium tidak akan pernah bisa naik sebelum <b>Magnesium dikoreksi secara serentak</b>.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_17.jpg')">
            <img src="slides_kul3/slide_17.jpg" class="evidence-thumb" alt="Slide 17" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 17 &amp; 28</span>
              <div class="evidence-title">Mekanisme Kegagalan Koreksi Kalium Akibat Disfungsi Kanal ROMK Ginjal</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

      <!-- BAB 5 -->
      <section class="chapter-section">
        <h2 class="chapter-title">5. Fosfat (P) &amp; Refeeding Syndrome: Krisis Energi ATP Fatal</h2>
        <div class="chapter-body">
          <p>Fosfat anorganik serum adalah komponen pembentuk adenosin trifosfat (ATP), 2,3-difosfogliserat (2,3-DPG eritrosit), dan fosfolipid membran sel. Tanpa fosfat, sel tubuh tidak mampu memproduksi energi kimia.</p>

          <p>Refeeding syndrome merupakan kegawatan medis yang terjadi saat pasien malnutrisi berat, anoreksia nervosa, atau orang yang kelaparan lebih dari 7–10 hari <b>diberikan asupan nutrisi tinggi karbohidrat secara mendadak</b>:</p>

          <div class="table-wrap">
            <table class="reading-table">
              <thead>
                <tr>
                  <th>Fase</th>
                  <th>Perubahan Biokimiawi</th>
                  <th>Dampak Klinis pada Pasien</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>1. Periode Kelaparan</b></td>
                  <td>Tubuh beralih ke pembakaran asam lemak dan keton. Cadangan fosfat intraseluler habis terkuras.</td>
                  <td>Atrofi organ, konsentrasi elektrolit serum tampak normal palsu akibat dehidrasi dan kompensasi ginjal.</td>
                </tr>
                <tr>
                  <td><b>2. Nutrisi Dimulai</b></td>
                  <td>Glukosa memicu pankreas mensekresi hormon <b>Insulin dalam jumlah masif</b>.</td>
                  <td>Insulin mendorong glukosa bersama ion <b>Fosfat (P), Kalium (K), dan Magnesium (Mg)</b> tersedot masuk ke dalam sel.</td>
                </tr>
                <tr>
                  <td><b>3. Hipofosfatemia Akut</b></td>
                  <td>Kadar fosfat plasma anjlok drastis hingga <b>{cl("&lt;1.0 mg/dL")}</b>. Sintesis ATP dan 2,3-DPG berhenti total.</td>
                  <td><b>Gagal napas akut</b> akibat kelumpuhan diafragma, kardiomiopati akut, aritmia fatal, rabdomiolisis, dan kematian mendadak.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="callout-pearl">
            <div class="callout-title">Protokol Pencegahan ASPEN &amp; NICE (Slide 19)</div>
            <div class="callout-body">
              1. Berikan suplemen <b>Tiamin (B1) sebelum makanan atau infus pertama dimulai</b> untuk mencegah ensefalopati Wernicke.<br>
              2. Batasi kalori awal pada tingkat rendah: <b>{cl("10–15 kkal/kg berat badan/hari")}</b>, lalu naikkan perlahan dalam 4–7 hari.<br>
              3. Lakukan pemantauan laboratorium serial terhadap kadar fosfat, kalium, dan magnesium darah setiap 12–24 jam.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_19.jpg')">
            <img src="slides_kul3/slide_19.jpg" class="evidence-thumb" alt="Slide 19" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 19 &amp; 29</span>
              <div class="evidence-title">Bagan Alir Patofisiologi Refeeding Syndrome ASPEN 2020</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

      <!-- BAB 6 -->
      <section class="chapter-section">
        <h2 class="chapter-title">6. Tembaga (Cu) vs Seng, Iodium (I), &amp; Selenium (Se)</h2>
        <div class="chapter-body">
          <p>Interaksi kompetitif penyerapan mineral merupakan sumber kesalahan diagnosis yang sering dijadikan jebakan soal klinik oleh dosen:</p>

          <p><b>Tembaga (Cu) &amp; Pemicu Iatrogenik Suplemen Seng:</b><br>
          Tembaga merupakan komponen enzim <i>ceruloplasmin</i> (ferroksidase yang mengubah Fe2+ menjadi Fe3+ agar bisa diangkut transferrin). Defisiensi tembaga bermanifestasi sebagai trias: <b>{cl("anemia mikrositik + neutropenia berat + mielopati ataksia")}</b> (degenerasi kolumna dorsalis medula spinalis menyerupai defisiensi vitamin B12).<br>
          Pemicu iatrogenik paling umum adalah konsumsi suplemen Seng (Zinc) dosis tinggi (&gt;50 mg/hari). Zinc merangsang sintesis protein {tt("Metallothionein", "Metallothionein", "Protein intraseluler kaya sistein di enterosit usus halus.", "Diinduksi oleh zinc dosis tinggi; memiliki afinitas pengikatan terhadap tembaga yang jauh lebih kuat daripada seng, sehingga tembaga terjebak di dalam sel usus dan ikut terbuang saat sel epitel terkelupas.")} di sel usus, yang mengikat tembaga dan membuangnya keluar tubuh.</p>

          <p><b>Iodium (I):</b><br>
          Bahan baku utama sintesis tiroksin (T4) dan triiodotironin (T3). Defisiensi memicu hipertrofi kelenjar tiroid (struma/gondok endemik) karena umpan balik negatif ke hipofisis menurun dan sekresi TSH melonjak. Bila terjadi pada masa kehamilan, defisiensi iodium mengakibatkan sindrom {tt("Kretinisme", "Kretinisme Endemik", "Sindrom defisiensi neurologis bawaan permanen akibat kekurangan iodium berat selama masa kehamilan.", "Ditandai dengan retardasi mental berat, tuli-bisu saraf sensorineural, spastisitas otot, dan perawakan pendek cebol.")}.</p>

          <p><b>Selenium (Se):</b><br>
          Komponen asam amino selenocysteine dalam enzim antioksidan glutation peroksidase (GPx). Defisiensi berat di wilayah tanah miskin selenium memicu {tt("Penyakit Keshan", "Penyakit Keshan", "Kardiomiopati kongestif endemik yang pertama kali diidentifikasi di wilayah Keshan, Tiongkok.", "Defisiensi selenium memicu mutasi virus Coxsackie B dan stres oksidatif miosit jantung, menyebabkan dilatasi ventrikel dan henti jantung pada anak-anak.")}.</p>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_22.jpg')">
            <img src="slides_kul3/slide_22.jpg" class="evidence-thumb" alt="Slide 22" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 13, 22, 23</span>
              <div class="evidence-title">Mikromineral Unik: Tembaga (Cu), Iodium (I), dan Selenium (Se)</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

      <!-- BAB 7 -->
      <section class="chapter-section">
        <h2 class="chapter-title">7. Bedah 3 Kasus Asli Slide Diskusi dr. Iwal Reza Ahdi, Sp.PD</h2>
        <div class="chapter-body">
          <p>Tiga kasus diskusi berikut adalah materi asli yang dibahas dr. Iwal pada slide 27, 28, dan 29. Dosen FK mengambil 4 soal ujian UAB langsung dari modifikasi kasus ini:</p>

          <div class="callout-pearl">
            <div class="callout-title">Kasus 1: Mikrositosis &amp; Pagophagia (Slide 27)</div>
            <div class="callout-body">
              <b>Pasien:</b> Perempuan 29 tahun dengan menstruasi banyak (menorrhagia), lelah, berdebar, Hb 8.9 g/dL, MCV 68 fL, ferritin 7 ng/mL, suka mengunyah es batu.<br>
              <b>Diagnosis Kerja:</b> Anemia Defisiensi Besi (IDA) stadium 3.<br>
              <b>Rasional Klinis:</b> Nilai ferritin serum &lt;15 ng/mL adalah konfirmasi absolut penipisan cadangan besi. Pagophagia adalah bentuk pica patognomonik.<br>
              <b>Tatalaksana:</b> Berikan suplementasi sulfas ferosus oral 1 kali sehari pagi hari (atau selang-hari) dan rujuk ke dokter spesialis obstetri ginekologi untuk menghentikan menorrhagia.
            </div>
          </div>

          <div class="callout-danger">
            <div class="danger-title">Kasus 2: Hipokalemia Refrakter (Slide 28)</div>
            <div class="danger-body">
              <b>Pasien:</b> Laki-laki 67 tahun, riwayat minum furosemid, lemas, berdebar, EKG ada gelombang U, kalium 2.8 mmol/L tetap rendah meski sudah diberi KCl oral 3 hari, magnesium 1.1 mg/dL.<br>
              <b>Diagnosis Kerja:</b> Hipokalemia refrakter akibat hipomagnesemia tersembunyi.<br>
              <b>Rasional Klinis:</b> Furosemid membuang K dan Mg di ansa Henle. Selama Mg &lt;1.7 mg/dL, kanal ROMK ginjal bocor terus.<br>
              <b>Tatalaksana:</b> Wajib berikan koreksi Magnesium (MgSO4 IV atau magnesium oral) secara bersamaan dengan KCl.
            </div>
          </div>

          <div class="callout-pearl">
            <div class="callout-title">Kasus 3: Sesak Napas Pasca-Nutrisi (Slide 29)</div>
            <div class="callout-body">
              <b>Pasien:</b> Laki-laki 46 tahun, malnutrisi berat tidak makan 12 hari, 48 jam pasca diberi nutrisi karbohidrat timbul sesak napas berat, takipnea, fosfat 0.8 mg/dL, kalium dan magnesium turun.<br>
              <b>Diagnosis Kerja:</b> Refeeding Syndrome dengan komplikasi gagal napas diafragma akut.<br>
              <b>Rasional Klinis:</b> Hipofosfatemia berat (&lt;1.0 mg/dL) akibat insulin memicu deplesi ATP otot pernapasan.<br>
              <b>Tatalaksana:</b> Turunkan laju infus nutrisi, berikan koreksi natrium/kalium fosfat IV, berikan injeksi tiamin, dan rawat di ruang intensif dengan pemantauan serial.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_27.jpg')">
            <img src="slides_kul3/slide_27.jpg" class="evidence-thumb" alt="Slide 27" />
            <div class="evidence-meta">
              <span class="evidence-num">Slide 27, 28, 29</span>
              <div class="evidence-title">Sesi Kasus Diskusi Interaktif dr. Iwal Reza Ahdi, Sp.PD</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah asli ↗</div>
            </div>
          </div>
        </div>
      </section>

    </div>

    <!-- =================================================================== -->
    <!-- VIEW 2: JEMBATAN KLINIS LINTAS BLOK (FITUR 5)                       -->
    <!-- =================================================================== -->
    <div id="view-bridge" class="study-pane">
      <div class="bridge-card">
        <h2 class="chapter-title" style="border:none;margin-bottom:6px;">Jembatan Klinis Lintas Blok: Menghubungkan Semester 1 s.d. 3</h2>
        <p style="color:var(--ink-secondary);font-size:0.95rem;margin-bottom:16px;">Konsep defisiensi mineral saling terkait erat dengan materi patologi, genetika, dan fisiologi dari blok-blok sebelumnya:</p>

        <div class="bridge-tabs">
          <button type="button" class="bridge-tab-btn active" onclick="switchBridge('br-anemia', this)">1. Sindrom Anemia Mikrositik</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridge('br-ginjal', this)">2. Fisiologi Ginjal &amp; Kalium</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridge('br-atp', this)">3. Refeeding &amp; Jalur Glikolisis</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridge('br-tulang', this)">4. Kalsium &amp; Resorpsi Tulang</button>
        </div>

        <!-- Bridge 1: Anemia -->
        <div id="br-anemia" class="bridge-pane active">
          <p style="font-size:0.95rem;color:var(--ink);margin-bottom:12px;"><b>Diagnosis Banding Anemia Mikrositik Hipokromik (MCV &lt; 80 fL):</b> Tiga penyakit dari tiga blok berbeda yang paling sering diadu di lembar ujian UAB:</p>
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-emn">Blok 9 EMN · Nutrisi</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Anemia Defisiensi Besi (IDA)</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                • <b>Ferritin:</b> Anjlok (&lt;15–30 ng/mL)<br>
                • <b>TIBC:</b> Meningkat (&gt;400 &mu;g/dL)<br>
                • <b>RDW:</b> Melebar (anisositosis nyata)<br>
                • <b>Penyebab:</b> Menorrhagia, ulkus peptikum, celiac.
              </p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 2 BMS 1 · Genetika</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Thalassemia Trait (&alpha; / &beta;)</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                • <b>Ferritin:</b> Normal atau bahkan meningkat<br>
                • <b>TIBC:</b> Normal<br>
                • <b>RDW:</b> Normal / homogen<br>
                • <b>Mentzer Index (MCV/RBC):</b> &lt; 13 (sangat mengarah ke thal)<br>
                • <b>Konfirmasi:</b> Elektroforesis Hb (HbA2 naik).
              </p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-hi">Blok 8 HI · Infeksi Imun</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Anemia Penyakit Kronis (ACD)</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                • <b>Ferritin:</b> Normal atau MENINGKAT (reaktan fase akut)<br>
                • <b>Hepcidin:</b> Melonjak akibat stimulasi sitokin IL-6<br>
                • <b>Patofisiologi:</b> Besi terperangkap di dalam makrofag limpa dan hati, tidak bisa disalurkan ke eritroblas.
              </p>
            </div>
          </div>
        </div>

        <!-- Bridge 2: Ginjal -->
        <div id="br-ginjal" class="bridge-pane">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 5 BMS 4 · Faal Ginjal</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Kanal ROMK &amp; Furosemid</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                Furosemid menghambat kotransporter Na-K-2Cl di ansa Henle tebal, meningkatkan muatan natrium dan cairan ke tubulus distal. Di tubulus distal, kanal ROMK membuang kalium. Bila magnesium intrasel kurang, kanal ROMK terbuka permanen, memicu hipokalemia berat.
              </p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-bdt">Blok 7 BDT · Gawat Darurat</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Protokol Koreksi KCl &amp; MgSO4</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                Hipokalemia dengan gelombang U berisiko aritmia Torsades de Pointes. Pemberian infus KCl perifer maksimal 10 mEq/jam. Bila refrakter, wajib berikan MgSO4 20% 1–2 gram IV dalam 15 menit.
              </p>
            </div>
          </div>
        </div>

        <!-- Bridge 3: ATP -->
        <div id="br-atp" class="bridge-pane">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 4 BMS 3 · Biokimia</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Jalur Glikolisis Heksokinase</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                Fosforilasi glukosa oleh enzim heksokinase membutuhkan fosfat anorganik. Saat insulin memicu glikolisis mendadak, fosfat serum tersedot habis ke intrasel sehingga eritrosit kekurangan 2,3-DPG (kurva disosiasi Hb bergeser ke kiri, oksigen sulit dilepas ke jaringan).
              </p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-emn">Blok 9 EMN · Malnutrisi Anak</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Protokol Formula F-75 WHO</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                Pada anak gizi buruk (marasmus/kwashiorkor), pemberian formula awal F-75 sengaja dibatasi rendah protein dan kalori (75 kkal/100 mL) untuk mencegah refeeding syndrome dan gagal jantung kongestif sebelum beralih ke F-100.
              </p>
            </div>
          </div>
        </div>

        <!-- Bridge 4: Tulang -->
        <div id="br-tulang" class="bridge-pane">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 3 BMS 2 · Histologi</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Sistem RANK / RANKL Tulang</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                Saat kalsium serum rendah, hormon paratiroid (PTH) meningkat dan merangsang osteoblas untuk mengekspresikan RANKL. RANKL berikatan dengan RANK pada pre-osteoklas, menginduksi diferensiasi osteoklas aktif untuk meresorpsi matriks tulang hidroksiapatit.
              </p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-emn">Blok 9 EMN · Vitamin D</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Sintesis Calbindin Mukosa</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">
                Kalsitriol (1,25-(OH)2D3) menembus membran enterosit duodenum dan berikatan dengan reseptor nukleus VDR, menginduksi transkripsi protein calbindin-D9k yang mengangkut kalsium dari lumen usus menyeberang ke sirkulasi darah.
              </p>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 3: LATIHAN CBT UWORLD METRICS (FITUR 3)                        -->
    <!-- =================================================================== -->
    <div id="view-cbt" class="study-pane">
      <div class="cbt-container">
        
        <div class="diag-dashboard">
          <div class="diag-card">
            <span class="diag-val" id="diag-mastered" style="color:var(--sage);">0</span>
            <span class="diag-lbl">Tuntas (Benar + Yakin)</span>
          </div>
          <div class="diag-card">
            <span class="diag-val" id="diag-lucky" style="color:var(--ochre);">0</span>
            <span class="diag-lbl">Tebakan Beruntung (Benar + Ragu)</span>
          </div>
          <div class="diag-card">
            <span class="diag-val" id="diag-danger" style="color:var(--coral);">0</span>
            <span class="diag-lbl">Miskonsepsi Berbahaya (Salah + Yakin)</span>
          </div>
          <div class="diag-card">
            <span class="diag-val" id="diag-gap" style="color:var(--navy);">0</span>
            <span class="diag-lbl">Kesenjangan Pemahaman (Salah + Ragu)</span>
          </div>
        </div>

        <div id="cbt-cards-target"></div>

      </div>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 4: MATRIKS CEK CEPAT H-1                                      -->
    <!-- =================================================================== -->
    <div id="view-flash" class="study-pane">
      <div class="table-wrap" style="box-shadow:var(--shadow-sm);margin-top:0;">
        <table class="reading-table">
          <thead>
            <tr>
              <th>Mineral</th>
              <th>Organ Target</th>
              <th>Gejala Klinis Patognomonik</th>
              <th>Biomarker Laboratorium Kunci</th>
              <th>Jebakan Ujian UAB</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Besi (Fe)</b></td>
              <td>Darah &amp; Enzim</td>
              <td>Pagophagia (makan es batu), koilonychia (kuku sendok), lemas cepat lelah.</td>
              <td><b>Ferritin &lt; 15–30 ng/mL</b> (paling dini), TSAT &lt; 20%.</td>
              <td style="color:var(--coral);font-weight:600;">MCV normal tidak menyingkirkan defisiensi besi dini!</td>
            </tr>
            <tr>
              <td><b>Seng (Zn)</b></td>
              <td>Kulit &amp; Imun</td>
              <td>Dermatitis periorifisial/akral, diare kronik, alopesia, luka sulit sembuh.</td>
              <td>Serum Zinc &lt; 70 &mu;g/dL.</td>
              <td style="color:var(--coral);font-weight:600;">Diet tinggi asam fitat serealia menghambat penyerapan seng di usus.</td>
            </tr>
            <tr>
              <td><b>Magnesium (Mg)</b></td>
              <td>Saraf &amp; Ginjal</td>
              <td>Tremor, hiperrefleksia, tetani, aritmia, <b>hipokalemia refrakter</b>.</td>
              <td>Magnesium serum &lt; 1.7 mg/dL.</td>
              <td style="color:var(--coral);font-weight:600;">Kalium tidak bisa naik sebelum kadar Mg dikoreksi serentak!</td>
            </tr>
            <tr>
              <td><b>Fosfat (P)</b></td>
              <td>Energi (ATP)</td>
              <td>Kelemahan napas diafragma akut (takipnea), aritmia, henti napas.</td>
              <td>Fosfat serum &lt; 1.0 mg/dL (hipofosfatemia berat).</td>
              <td style="color:var(--coral);font-weight:600;">Dipicu lonjakan insulin saat refeeding karbohidrat pada malnutrisi.</td>
            </tr>
            <tr>
              <td><b>Tembaga (Cu)</b></td>
              <td>Darah &amp; Saraf</td>
              <td>Anemia mikrositik + neutropenia berat + ataksia sensorik (mirip B12).</td>
              <td>Serum Cu rendah, ceruloplasmin rendah.</td>
              <td style="color:var(--coral);font-weight:600;">Dipicu konsumsi suplemen Zinc dosis tinggi jangka panjang!</td>
            </tr>
            <tr>
              <td><b>Kalsium (Ca)</b></td>
              <td>Saraf &amp; Tulang</td>
              <td>Parestesia perioral, tanda Chvostek (+), Trousseau (+), QT memanjang.</td>
              <td>Ionized Calcium (kalsium ionisasi bebas).</td>
              <td style="color:var(--coral);font-weight:600;">99% kalsium ada di tulang, serum total dipengaruhi albumin.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- Lightbox Image Modal -->
  <div id="lightbox-modal" class="lightbox-modal" onclick="closeLightbox()">
    <img id="lightbox-img" src="" class="lightbox-img" alt="Zoom Slide" onclick="event.stopPropagation()" />
  </div>

  <script>
    // VIEW SWITCHER
    function switchView(viewId, btn) {{
      document.querySelectorAll('.study-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(viewId).classList.add('active');
      btn.classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // BRIDGE TAB SWITCHER
    function switchBridge(paneId, btn) {{
      document.querySelectorAll('.bridge-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.bridge-tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(paneId).classList.add('active');
      btn.classList.add('active');
    }}

    // LIGHTBOX CONTROLLER
    function openLightbox(src) {{
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      img.src = src;
      modal.classList.add('open');
    }}
    function closeLightbox() {{
      document.getElementById('lightbox-modal').classList.remove('open');
    }}
    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') closeLightbox();
    }});

    // FEATURE 2: CLOZE MODE (OSMOSIS ACTIVE RECALL)
    let clozeActive = false;
    function toggleCloze() {{
      clozeActive = !clozeActive;
      document.body.classList.toggle('cloze-active', clozeActive);
      const btn = document.getElementById('cloze-toggle');
      const status = document.getElementById('cloze-status');
      if (clozeActive) {{
        btn.classList.add('active');
        status.textContent = 'ON';
        document.querySelectorAll('.cloze-mask').forEach(el => el.classList.remove('revealed'));
      }} else {{
        btn.classList.remove('active');
        status.textContent = 'OFF';
      }}
    }}
    document.addEventListener('keydown', e => {{
      if (e.key.toLowerCase() === 'm' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {{
        toggleCloze();
      }}
    }});

    // CBT DATA (8 SOAL ADAPTIF DR. IWAL)
    const QUIZ = [
      {{
        stem: 'Seorang perempuan 29 tahun datang ke poliklinik dengan keluhan lemas dan berdebar saat beraktivitas sejak 2 bulan. Pasien memiliki riwayat menstruasi sangat banyak (ganti pembalut 6–7 kali/hari) selama 8 hari setiap siklusnya. Konjungtiva anemis (+). Laboratorium: Hb 8,9 g/dL, MCV 68 fL, MCH 21 pg. Pasien mengaku memiliki kebiasaan mengunyah es batu berulang kali (pagophagia). Pemeriksaan biomarker manakah yang paling sensitif dan paling awal menurun untuk memastikan diagnosis?',
        opts: [
          'Total Iron Binding Capacity (TIBC)',
          'Ferritin serum',
          'Saturasi transferrin (TSAT)',
          'Hemoglobin elektroforesis',
          'Bilirubin indirek serum'
        ],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Ferritin serum)</b><br>Pasien mengalami Anemia Defisiensi Besi sekunder akibat menorrhagia kronik. Gejala <i>pagophagia</i> (pica makan es batu) adalah tanda patognomonik defisiensi besi. Pada perjalanan alami penipisan besi (Slide 10), <b>Ferritin serum adalah biomarker pertama yang anjlok (&lt;15–30 ng/mL)</b> mencerminkan habisnya cadangan besi di retikuloendotelial, sebelum nilai Hb dan MCV turun menjadi anemia mikrositik.',
        slide: 'slides_kul3/slide_10.jpg',
        slideTitle: 'Slide 10 · Perjalanan Defisiensi Besi: Ferritin Turun Lebih Awal'
      }},
      {{
        stem: 'Laki-laki 67 tahun dengan gagal jantung kongestif yang rutin mengonsumsi furosemid mengeluh kelemahan otot tungkai dan berdebar. EKG menunjukkan depresi segmen ST, gelombang T mendatar, dan muncul gelombang U yang menonjol. Hasil laboratorium: Kalium 2,8 mmol/L. Dokter telah memberikan suplementasi KCl oral dosis tinggi selama 3 hari, namun pada evaluasi ulang kadar Kalium pasien tetap rendah (2,9 mmol/L). Gangguan elektrolit penyerta manakah yang mendasari kondisi refrakter tersebut?',
        opts: [
          'Hiponatremia',
          'Hipokalsemia',
          'Hipomagnesemia',
          'Hiperfosfatemia',
          'Hiperkalsiuria'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Hipomagnesemia)</b><br>Furosemid membuang Kalium dan Magnesium sekaligus. Di tubulus ginjal, ion Magnesium intrasel bertindak sebagai inhibitor alami kanal ROMK. Pada kondisi hipomagnesemia (Slide 17 & 28), kanal ROMK terbuka bebas tanpa rem sehingga Kalium terus-menerus bocor ke urin. Akibatnya kalium tidak dapat naik sebelum kadar Magnesium dikoreksi secara serentak.',
        slide: 'slides_kul3/slide_17.jpg',
        slideTitle: 'Slide 17 · Mengapa Kalium Sulit Naik Bila Magnesium Rendah'
      }},
      {{
        stem: 'Anak laki-laki 4 tahun dibawa ibunya dengan keluhan bercak kemerahan bersisik dan berkrusta di area sekitar mulut, perineum, serta sela-sela jari kaki sejak 1 bulan. Pasien juga mengalami diare kronik kambuhan dan rambut rontok hingga tampak botak sebagian. Pasien memiliki riwayat diet monoton tinggi serealia dan bubur gandum tanpa asupan hewani. Defisiensi mikromineral apakah yang mendasari kelainan tersebut?',
        opts: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Seng (Zn)',
          'Selenium (Se)',
          'Mangan (Mn)'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Seng / Zinc)</b><br>Trias patognomonik: <b>dermatitis periorifisial & akral, diare kronik, dan alopesia</b> merupakan tanda khas defisiensi Seng (Slide 12). Serealia dan gandum mengandung asam <b>fitat</b> tinggi yang mengikat seng di lumen usus membentuk senyawa tak larut yang tidak dapat diserap enterosit.',
        slide: 'slides_kul3/slide_12.jpg',
        slideTitle: 'Slide 12 · Seng (Zn): Integritas Kulit & Peran Inhibitor Fitat'
      }},
      {{
        stem: 'Pasien laki-laki 46 tahun dengan riwayat malnutrisi berat dan kelaparan selama 12 hari dirawat di bangsal. Dokter segera memberikan nutrisi parenteral tinggi karbohidrat. Dalam waktu 48 jam, pasien mendadak mengalami takipnea berat, kelemahan otot menyeluruh, dan aritmia. Gangguan elektrolit serum manakah yang menjadi pemicu utama kegagalan napas akut tersebut?',
        opts: [
          'Hiponatremia berat (&lt;120 mEq/L)',
          'Hipokalsemia terionisasi',
          'Hipofosfatemia berat (&lt;1.0 mg/dL)',
          'Asidosis laktat berat',
          'Hiperglikemia hiperosmolar'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Hipofosfatemia berat &lt;1.0 mg/dL)</b><br>Pasien mengalami <i>Refeeding Syndrome</i> (Slide 19 & 29). Karbohidrat mendadak memicu lonjakan insulin yang mendorong glukosa dan Fosfat masuk masif ke dalam sel. Terjadilah hipofosfatemia berat yang menghentikan sintesis ATP seluler, melumpuhkan otot diafragma (gagal napas akut) dan memicu kardiomiopati akut.',
        slide: 'slides_kul3/slide_19.jpg',
        slideTitle: 'Slide 19 · Refeeding Syndrome: Pergeseran Elektrolit Akut'
      }},
      {{
        stem: 'Perempuan 35 tahun pasca-operasi bypass lambung datang dengan keluhan baal dan kesemutan di kedua tungkai serta ataksia sensorik. Laboratorium: Hb 9,0 g/dL, MCV 72 fL (mikrositik), dan neutropenia berat (ANC 750/&mu;L). Pasien mengaku mengonsumsi suplemen Zinc dosis tinggi (80 mg/hari) selama 8 bulan terakhir. Defisiensi mineral apakah yang paling tepat menjelaskan kondisi pasien?',
        opts: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Iodium (I)',
          'Selenium (Se)',
          'Kalsium (Ca)'
        ],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Tembaga / Cu)</b><br>Kombinasi <b>anemia mikrositik + neutropenia + mielopati ataksia</b> adalah tanda khas defisiensi Tembaga (Slide 22). Suplemen Zinc dosis tinggi menginduksi protein <i>metallothionein</i> di enterosit usus yang mengikat tembaga dengan kuat dan menghambat absorpsinya ke sirkulasi darah.',
        slide: 'slides_kul3/slide_22.jpg',
        slideTitle: 'Slide 22 · Tembaga (Cu) & Pemicu Iatrogenik Suplemen Zinc'
      }},
      {{
        stem: 'Berdasarkan Clinical Practice Update American Gastroenterological Association (AGA 2024), bagaimanakah aturan suplementasi besi oral yang paling tepat dan dapat ditoleransi optimal pada pasien anemia defisiensi besi?',
        opts: [
          'Diberikan dosis tinggi 3 kali sehari bersama makanan',
          'Diberikan dosis terbagi setiap 6 jam disertai antasida',
          'Diberikan maksimal 1 kali sehari atau rejimen selang-hari (alternate-day)',
          'Diberikan bersamaan dengan susu sapi segar',
          'Diberikan 4 kali sehari dalam dosis kecil'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Maksimal 1 kali sehari atau selang-hari)</b><br>Pedoman konsensus AGA 2024 (Slide 11) menekankan bahwa setiap dosis besi oral memicu peningkatan hormon <b>Hepcidin</b> yang memblokade absorpsi besi selanjutnya selama 24–48 jam. Pemberian 1x/hari atau selang-hari (alternate day) memaksimalkan penyerapan dan meminimalkan efek samping saluran cerna.',
        slide: 'slides_kul3/slide_11.jpg',
        slideTitle: 'Slide 11 · Terapi Fe Konsensus AGA 2024'
      }},
      {{
        stem: 'Pemeriksaan fisik pada pasien dengan kecurigaan hipokalsemia menunjukkan adanya spasme karpopedal pada tangan ketika manset tensimeter dipompa di atas tekanan sistolik selama 3 menit. Disebut apakah tanda fisik klinis patognomonik tersebut?',
        opts: [
          'Chvostek sign',
          'Trousseau sign',
          'Kernig sign',
          'Brudzinski sign',
          'Babinski sign'
        ],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Trousseau sign)</b><br>Tanda Trousseau (spasme karpopedal tangan saat manset tensimeter dipompa >sistolik selama 3 menit) sangat sensitif dan spesifik untuk hipokalsemia (Slide 15). Tanda Chvostek adalah kedutan sudut bibir saat saraf fasialis diketuk.',
        slide: 'slides_kul3/slide_15.jpg',
        slideTitle: 'Slide 15 · Hipokalsemia: Tanda Klinis Trousseau & Chvostek'
      }},
      {{
        stem: 'Wanita hamil di daerah pegunungan yang jarang mengonsumsi garam beriodium melahirkan bayi dengan keterlambatan perkembangan saraf berat, perawakan pendek, dan tuli-bisu. Mekanisme patofisiologi apakah yang mendasari kondisi kretinisme pada bayi tersebut?',
        opts: [
          'Kekurangan iodium memicu hambatan sintesis T3/T4 yang vital bagi mielinisasi dan perkembangan otak janin',
          'Kelebihan TSH ibu menembus plasenta dan merusak kelenjar tiroid janin',
          'Defisiensi selenium langsung menghambat enzim deiodinase perifer tanpa melibatkan hormon tiroid',
          'Kadar kalsium yang rendah mengganggu pembentukan neurotransmitter otak',
          'Fosfat yang rendah menyebabkan kegagalan pembentukan mielin saraf'
        ],
        ans: 0,
        exp: '<b>Jawaban Benar: A</b><br>Iodium adalah substrat esensial hormon tiroid T3/T4 (Slide 13). Pada kehamilan, hormon tiroid sangat krusial untuk neurogenesis dan mielinisasi otak janin. Defisiensi berat memicu sindrom kretinisme endemik dengan defisit mental permanen.',
        slide: 'slides_kul3/slide_13.jpg',
        slideTitle: 'Slide 13 · Iodium (I): Sintesis Hormon Tiroid & Bahaya Kehamilan'
      }}
    ];

    // FEATURE 3: UWORLD CONFIDENCE & DIAGNOSTICS CONTROLLER
    let userAns = {{}};
    let userConf = {{}};

    function setConfidence(idx, val) {{
      userConf[idx] = val;
      const card = document.getElementById('q-card-' + idx);
      const btns = card.querySelectorAll('.conf-btn');
      btns.forEach(b => b.classList.remove('active-high', 'active-low'));
      if (val === 'high') btns[0].classList.add('active-high');
      else btns[1].classList.add('active-low');
    }}

    function pickAnswer(qIdx, optIdx) {{
      if (userAns[qIdx] !== undefined) return;
      userAns[qIdx] = optIdx;
      if (!userConf[qIdx]) userConf[qIdx] = 'high';

      const q = QUIZ[qIdx];
      const isCorrect = optIdx === q.ans;
      const conf = userConf[qIdx];

      const card = document.getElementById('q-card-' + qIdx);
      const rows = card.querySelectorAll('.opt-choice');
      rows.forEach((r, idx) => {{
        if (idx === q.ans) r.classList.add('is-correct');
        else if (idx === optIdx && !isCorrect) r.classList.add('is-wrong');
      }});

      // Show Explanation & Outcome Pill
      const expBox = document.getElementById('exp-box-' + qIdx);
      const pill = document.getElementById('pill-' + qIdx);
      expBox.classList.add('show');

      if (isCorrect && conf === 'high') {{
        pill.className = 'outcome-pill pill-mastered';
        pill.textContent = '🏆 Tuntas (Benar + Yakin)';
      }} else if (isCorrect && conf === 'low') {{
        pill.className = 'outcome-pill pill-lucky';
        pill.textContent = '⚠️ Tebakan Beruntung (Benar + Ragu) — Review Ulang!';
      }} else if (!isCorrect && conf === 'high') {{
        pill.className = 'outcome-pill pill-danger';
        pill.textContent = '🚨 Miskonsepsi Berbahaya (Salah + Yakin) — Prioritas Evaluasi!';
      }} else {{
        pill.className = 'outcome-pill pill-gap';
        pill.textContent = '📖 Kesenjangan Pemahaman (Salah + Ragu)';
      }}

      updateDiagnostics();
    }}

    function updateDiagnostics() {{
      let mastered = 0, lucky = 0, danger = 0, gap = 0;
      Object.keys(userAns).forEach(k => {{
        const idx = parseInt(k);
        const q = QUIZ[idx];
        const isCorrect = userAns[idx] === q.ans;
        const conf = userConf[idx] || 'high';

        if (isCorrect && conf === 'high') mastered++;
        else if (isCorrect && conf === 'low') lucky++;
        else if (!isCorrect && conf === 'high') danger++;
        else gap++;
      }});

      document.getElementById('diag-mastered').textContent = mastered;
      document.getElementById('diag-lucky').textContent = lucky;
      document.getElementById('diag-danger').textContent = danger;
      document.getElementById('diag-gap').textContent = gap;
    }}

    // RENDER CBT QUESTIONS
    function renderCBT() {{
      const container = document.getElementById('cbt-cards-target');
      if (!container) return;
      container.innerHTML = QUIZ.map((q, idx) => `
        <article class="q-card" id="q-card-${{idx}}">
          <div class="q-header-row">
            <span class="q-number">SOAL #${{idx + 1}}</span>
            <div class="confidence-picker">
              <span>Tingkat Keyakinan:</span>
              <button type="button" class="conf-btn active-high" onclick="setConfidence(${{idx}}, 'high')">🎯 Yakin</button>
              <button type="button" class="conf-btn" onclick="setConfidence(${{idx}}, 'low')">🤔 Ragu-Ragu</button>
            </div>
          </div>
          <div class="q-stem">${{q.stem}}</div>
          <div class="q-options-stack">
            ${{q.opts.map((opt, oIdx) => `
              <button type="button" class="opt-choice" onclick="pickAnswer(${{idx}}, ${{oIdx}})">
                <span class="opt-key-txt">${{String.fromCharCode(65 + oIdx)}}.</span>
                <span>${{opt}}</span>
              </button>
            `).join('')}}
          </div>
          <div class="q-explanation-box" id="exp-box-${{idx}}">
            <span class="outcome-pill" id="pill-${{idx}}"></span>
            <div style="color:#2D2F33;margin-bottom:12px;">${{q.exp}}</div>
            <div class="slide-evidence" onclick="openLightbox('${{q.slide}}')" style="margin:8px 0 0;background:#FFFFFF;">
              <img src="${{q.slide}}" class="evidence-thumb" alt="Slide" />
              <div class="evidence-meta">
                <span class="evidence-num">Bukti Slide Asli</span>
                <div class="evidence-title">${{q.slideTitle}}</div>
                <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
              </div>
            </div>
          </div>
        </article>
      `).join('');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      renderCBT();
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Modul EMN KUL 3 Joyful & Calm Edition berhasil dibuat di {OUT_HTML} (ukuran: {len(HTML_CONTENT)} bytes)")
