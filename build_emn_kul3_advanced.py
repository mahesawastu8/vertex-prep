#!/usr/bin/env python3
"""Build Supahero Advanced Edition for Blok 9 EMN · KUL 3 Defisiensi Mineral (dr. Iwal Reza Ahdi, Sp.PD).
Menyuntikkan 4 Fitur Standar Dunia:
1. AMBOSS-style Smart Medical Tooltips
2. Osmosis Active Masking / Cloze Mode
3. UWorld Decision & Confidence Metrics (Yakin vs Ragu, Diagnostic Matrix)
4. Cross-Block Knowledge Linking (Peta Jembatan Lintas Blok 1-9)
"""
import os
import json

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

# Baca CSS dan JS dari build_supahero_edition.py
with open(os.path.join(BASE_DIR, "build_supahero_edition.py"), "r", encoding="utf-8") as f:
    code = f.read()

css_start = code.find('SUPAHERO_CSS = """') + len('SUPAHERO_CSS = """')
css_end = code.find('"""\n\nSUPAHERO_JS = """')
BASE_CSS = code[css_start:css_end]

js_start = code.find('SUPAHERO_JS = """') + len('SUPAHERO_JS = """')
js_end = code.find('"""\n\n# ==============================================================================')
BASE_JS = code[js_start:js_end]

ADVANCED_CSS = """
    /* =====================================================================
       1. AMBOSS SMART MEDICAL TOOLTIPS
       ===================================================================== */
    .med-term {
      border-bottom: 2px dotted var(--cobalt);
      color: var(--cobalt);
      font-weight: 600;
      cursor: help;
      position: relative;
      display: inline-block;
      transition: color 0.15s ease;
    }
    .med-term:hover {
      color: #0B6350;
      background: var(--cobalt-soft);
      border-radius: 4px;
    }
    .med-tooltip {
      visibility: hidden;
      opacity: 0;
      position: absolute;
      bottom: 130%;
      left: 50%;
      transform: translateX(-50%) translateY(6px);
      width: 300px;
      background: #0B131A;
      color: #FFFFFF;
      border-radius: 12px;
      padding: 14px 16px;
      font-size: 0.84rem;
      line-height: 1.5;
      box-shadow: 0 18px 42px rgba(11, 19, 26, 0.35);
      z-index: 500;
      pointer-events: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
      text-align: left;
    }
    .med-tooltip::after {
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      margin-left: -7px;
      border-width: 7px;
      border-style: solid;
      border-color: #0B131A transparent transparent transparent;
    }
    .med-term:hover .med-tooltip {
      visibility: visible;
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }
    .tt-kicker { font-size: 0.7rem; font-weight: 700; color: #8FD6C5; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 3px; }
    .tt-title { font-size: 0.95rem; font-weight: 700; color: #FFFFFF; margin-bottom: 5px; }
    .tt-desc { color: #D4DEE7; font-size: 0.84rem; }
    .tt-pearl { margin-top: 8px; padding-top: 8px; border-top: 1px solid #263645; color: #FDF2E2; font-size: 0.8rem; font-style: italic; }

    /* =====================================================================
       2. OSMOSIS ACTIVE MASKING / CLOZE MODE
       ===================================================================== */
    .cloze-toggle-btn {
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 6px 14px;
      font-family: inherit;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--ink-700);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }
    .cloze-toggle-btn:hover {
      border-color: var(--cobalt);
      color: var(--cobalt);
    }
    .cloze-toggle-btn.active {
      background: #0B131A;
      color: #FFFFFF;
      border-color: #0B131A;
      box-shadow: 0 4px 14px rgba(11, 19, 26, 0.2);
    }
    .cloze-badge {
      background: #EAEFF4;
      color: #0B131A;
      padding: 2px 7px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-family: 'JetBrains Mono', monospace;
    }
    .cloze-toggle-btn.active .cloze-badge {
      background: #0B6350;
      color: #FFFFFF;
    }

    /* Cloze Mask Styling */
    body.cloze-active .cloze-mask {
      background: #164F73 !important;
      color: transparent !important;
      border-radius: 6px;
      padding: 1px 7px;
      cursor: pointer;
      user-select: none;
      filter: blur(4px);
      transition: all 0.2s ease;
      display: inline-block;
      text-shadow: none !important;
    }
    body.cloze-active .cloze-mask:hover {
      filter: blur(2px);
      background: #0B6350 !important;
    }
    body.cloze-active .cloze-mask.revealed {
      background: #E1F2EE !important;
      color: #0B6350 !important;
      filter: none !important;
      font-weight: 700;
      border: 1px solid #8FD6C5;
    }

    /* =====================================================================
       3. UWORLD CONFIDENCE METRICS & DIAGNOSTIC MATRIX
       ===================================================================== */
    .confidence-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--bg-subtle);
      border-radius: var(--radius-md);
      padding: 8px 14px;
      margin-bottom: 12px;
      font-size: 0.84rem;
    }
    .conf-btn-group {
      display: flex;
      gap: 6px;
    }
    .conf-btn {
      border: 1px solid var(--border);
      background: #FFFFFF;
      color: var(--ink-700);
      font-family: inherit;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .conf-btn.active-high {
      background: #0B6350;
      color: #FFFFFF;
      border-color: #0B6350;
    }
    .conf-btn.active-low {
      background: #9E5400;
      color: #FFFFFF;
      border-color: #9E5400;
    }
    .outcome-pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 4px 12px;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 8px;
    }
    .outcome-mastered { background: #E1F2EE; color: #0B6350; border: 1px solid #8FD6C5; }
    .outcome-lucky { background: #FDF2E2; color: #9E5400; border: 1px solid #E6C280; }
    .outcome-danger { background: #FCECEB; color: #B82921; border: 1px solid #F1A39D; }
    .outcome-gap { background: #E4F0F7; color: #164F73; border: 1px solid #A8CDE4; }

    /* Diagnostic Analytics Box */
    .diag-dashboard {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 18px 24px;
      margin-bottom: 20px;
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 16px;
      box-shadow: var(--shadow-soft);
    }
    .diag-card {
      border-left: 3px solid var(--border);
      padding-left: 12px;
    }
    .diag-val { font-size: 1.4rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; line-height: 1.2; }
    .diag-lbl { font-size: 0.78rem; color: var(--ink-500); margin-top: 2px; }

    /* =====================================================================
       5. CROSS-BLOCK KNOWLEDGE LINKING (HUBUNGAN LINTAS BLOK)
       ===================================================================== */
    .cross-bridge-card {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      margin-bottom: 20px;
      box-shadow: var(--shadow-soft);
    }
    .bridge-tabs {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 18px;
      border-bottom: 1px solid var(--border);
      padding-bottom: 12px;
    }
    .bridge-tab-btn {
      padding: 7px 14px;
      border-radius: 999px;
      background: var(--bg-subtle);
      border: 1px solid var(--border);
      font-family: inherit;
      font-size: 0.84rem;
      font-weight: 600;
      color: var(--ink-700);
      cursor: pointer;
      transition: all 0.2s ease;
    }
    .bridge-tab-btn.active {
      background: #164F73;
      color: #FFFFFF;
      border-color: #164F73;
    }
    .bridge-pane { display: none; }
    .bridge-pane.active { display: block; animation: fadeIn 0.2s ease; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

    .bridge-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 14px;
      margin-top: 14px;
    }
    .bridge-node {
      background: var(--bg-canvas);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      position: relative;
    }
    .bridge-block-tag {
      font-size: 0.72rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 6px;
      display: inline-block;
      margin-bottom: 6px;
    }
    .tag-emn { background: #E1F2EE; color: #0B6350; }
    .tag-bms { background: #E4F0F7; color: #164F73; }
    .tag-bdt { background: #FDF2E2; color: #9E5400; }
    .tag-hi  { background: #FCECEB; color: #B82921; }
"""

# Tooltip helper function
def tt(term, title, desc, pearl):
    return f"""<span class="med-term">{term}<span class="med-tooltip"><span class="tt-kicker">AMBOSS Clinical Guide</span><div class="tt-title">{title}</div><div class="tt-desc">{desc}</div><div class="tt-pearl">💡 {pearl}</div></span></span>"""

# Cloze mask helper function
def cl(text):
    return f"""<span class="cloze-mask" onclick="this.classList.toggle('revealed')">{text}</span>"""

FINAL_HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VERTEX-PREP · EMN Kuliah 3: Defisiensi Mineral (Supahero World-Class Edition)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
  <style>
{BASE_CSS}
{ADVANCED_CSS}
  </style>
</head>
<body>

  <!-- SUPAHERO FLOATING PILL NAVBAR -->
  <div class="supa-nav-wrap">
    <header class="supa-navbar">
      <div class="supa-brand">
        <span class="brand-dot">VX</span>
        <select class="course-switcher" aria-label="Pilih Kuliah" onchange="window.location.href=this.value">
          <option value="BDT_KUL3_Patient_Safety.html">Blok 7 BDT · Kuliah 3: Patient Safety (dr. Riskiyah)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html">Blok 9 EMN · Kuliah 2: Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
          <option value="EMN_KUL3_Defisiensi_Mineral.html" selected>Blok 9 EMN · Kuliah 3: Defisiensi Mineral (dr. Iwal, Sp.PD)</option>
        </select>
      </div>

      <nav class="supa-pills" aria-label="Mode Belajar">
        <button type="button" class="supa-pill-btn active" onclick="switchView('materi', this)">7 Bab Bento Visual</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('bridge', this)">🌉 Jembatan Lintas Blok</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('soal', this)">CBT Adaptif dr. Iwal (8)</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('flash', this)">Cek Cepat H-1 Ujian</button>
      </nav>

      <div class="supa-actions">
        <!-- Feature 2: Cloze Toggle -->
        <button type="button" id="cloze-toggle" class="cloze-toggle-btn" onclick="toggleClozeMode()" title="Tekan M untuk aktifkan / matikan mode uji ingatan">
          <span>🧠 Mode Uji Ingatan</span>
          <span class="cloze-badge" id="cloze-status-text">OFF</span>
        </button>
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-primary" style="padding:6px 14px;font-size:0.8rem;text-decoration:none;" download>⬇ Anki (.apkg)</a>
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
          <h1>Kuasai 32 Slide Defisiensi Mineral Tanpa Buka PPT Sekalipun.</h1>
          <div class="hero-meta-line">Blok 9 EMN · Kuliah Pakar 3 · dr. Iwal Reza Ahdi, Sp.PD-FINASIM</div>
          <p class="hero-lead">Dari analisis 1.680 soal UAB, <strong>dr. Iwal Reza Ahdi, Sp.PD memiliki karakter 66.7% penalaran klinis & 45.8% kasus vignette</strong> (hanya 4% hafalan kata slide). Modul ini dilengkapi <strong>Smart Tooltips (Gaya AMBOSS)</strong> untuk istilah medis, <strong>Mode Uji Ingatan Aktif (Osmosis Cloze Blur)</strong>, serta 3 kasus diskusi asli slide dosen.</p>

          <div class="hero-cta-row">
            <a href="#emn3-01" class="btn-primary">Mulai Pelajari 7 Bab Visual ↓</a>
            <button type="button" class="btn-secondary" onclick="jumpToQuiz()">Kerjakan 8 Soal Latihan →</button>
          </div>

          <div class="hero-stats-row">
            <div class="stat-unit">
              <span class="stat-num">32 → 7 Bab</span>
              <span class="stat-lbl">Pemadatan Materi Utuh</span>
            </div>
            <div class="stat-unit">
              <span class="stat-num">66.7% Kasus</span>
              <span class="stat-lbl">Karakteristik Soal dr. Iwal</span>
            </div>
            <div class="stat-unit">
              <span class="stat-num">3 Kasus Asli</span>
              <span class="stat-lbl">Diskusi Slide 27, 28, & 29</span>
            </div>
          </div>
        </div>

        <div class="hero-showcase">
          <div class="window-bar">
            <div class="window-dots">
              <span class="w-dot"></span><span class="w-dot"></span><span class="w-dot"></span>
            </div>
            <span class="window-tag">Bukti Slide #10 · 3 Stadium Defisiensi Besi</span>
          </div>
          <img src="slides_kul3/slide_10.jpg" alt="Bukti Slide 10" class="hero-slide-preview" onclick="openZoom('slides_kul3/slide_10.jpg', 'Slide 10 · Perjalanan Defisiensi Besi: Ferritin Turun Lebih Awal')" />
          <div class="showcase-caption">
            <span>Slide 10 Asli dr. Iwal (Ferritin turun lebih awal sebelum Hb/MCV abnormal)</span>
            <span>Klik untuk Zoom ↗</span>
          </div>
        </div>
      </section>

      <!-- CHAPTER QUICK-JUMP RIBBON -->
      <div class="chapter-ribbon">
        <a href="#emn3-01" class="chapter-chip">01 · Makro vs Mikro & 4 Mekanisme</a>
        <a href="#emn3-02" class="chapter-chip">02 · Besi (Fe), Ferritin, & AGA 2024</a>
        <a href="#emn3-03" class="chapter-chip">03 · Seng (Zn), Kulit, & Fitat</a>
        <a href="#emn3-04" class="chapter-chip">04 · Kalsium, Magnesium, & Hipo-K</a>
        <a href="#emn3-05" class="chapter-chip">05 · Fosfat & Refeeding Syndrome</a>
        <a href="#emn3-06" class="chapter-chip">06 · Tembaga, Iodium, & Selenium</a>
        <a href="#emn3-07" class="chapter-chip">07 · Peta Organ & 3 Kasus Asli dr. Iwal</a>
      </div>

      <!-- ================================================================= -->
      <!-- BAB 01: MAKRO VS MIKRO & 4 MEKANISME                             -->
      <!-- ================================================================= -->
      <article id="emn3-01" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 01 · Merangkum Slide 4, 5, 6</span>
          <span class="badge badge-cobalt">Konsep Dasar Homeostasis</span>
        </div>
        <h2>Klasifikasi Mineral & 4 Jalur Terjadinya Defisiensi</h2>
        <p class="bento-sub">Jumlah kebutuhan harian <strong>tidak sama dengan tingkat kepentingan klinis</strong>. Semua mineral esensial dapat memicu sindrom fatal bila kadarnya anjlok bermakna.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Makromineral (Mayor)</div>
                <div class="tile-title">{cl("Ca, P, Mg, Na, K, Cl")}</div>
                <div class="tile-body">Dibutuhkan dalam gram/hari. Berperan dalam struktur tulang/gigi, transmisi potensial aksi saraf-otot, dan keseimbangan osmotik cairan tubuh.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Mikromineral (Trace Elements)</div>
                <div class="tile-title">{cl("Fe, Zn, I, Se, Cu, Mn")}</div>
                <div class="tile-body">Dibutuhkan dalam miligram atau mikrogram/hari. Berperan vital sebagai kofaktor enzim metabolisme redoks, sintesis DNA, dan hormon tiroid.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">4 Jalur Mekanisme Defisiensi</div>
                <div class="tile-title">Asupan, Malabsorpsi, Kehilangan, Redistribusi</div>
                <div class="tile-body">
                  1. <b>Asupan Rendah:</b> Diet monoton, kemiskinan, anoreksia.<br>
                  2. <b>Malabsorpsi:</b> Penyakit celiac, bariatrik bypass lambung, IBD.<br>
                  3. <b>Kehilangan Berlebih:</b> Perdarahan haid/GI, diare kronik, diuretik.<br>
                  4. <b>Redistribusi / Regulasi:</b> {tt("Refeeding syndrome", "Refeeding Syndrome", "Krisis metabolik akibat pemberian nutrisi cepat pasca kelaparan.", "Insulin melonjak mendorong fosfat, kalium, dan magnesium masuk intrasel -> hipofosfatemia berat.")}, lonjakan insulin, alkalosis.
                </div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">Clinical Pearl dr. Iwal (Slide 5)</div>
              <div class="pearl-title">Kadar Serum Rendah Bukan Berarti Tubuh Kurang Asupan!</div>
              <p>Serum darah hanyalah kompartemen transport. Kadar rendah sering kali disebabkan oleh <i>pergeseran antar-kompartemen</i> (contoh: fosfat masuk ke dalam sel saat refeeding) atau <i>kehilangan renal akibat obat</i> (contoh: kalium keluar karena diuretik), bukan sekadar kurang makan garam/mineral.</p>
            </div>
          </div>

          <div class="slide-dock">
            <div class="dock-nav">
              <button type="button" class="dock-btn active" onclick="swapDockSlide('d1', 'slides_kul3/slide_4.jpg', 'Slide 4 · Klasifikasi Mayor vs Renik', this)">Slide 4</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d1', 'slides_kul3/slide_5.jpg', 'Slide 5 · Homeostasis Usus-Darah-Jaringan-Ginjal', this)">Slide 5</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d1', 'slides_kul3/slide_6.jpg', 'Slide 6 · 4 Mekanisme Defisiensi', this)">Slide 6</button>
            </div>
            <img id="dock-img-d1" src="slides_kul3/slide_4.jpg" alt="Bukti Slide 4" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d1').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d1">Slide 4 · Klasifikasi Mayor vs Renik</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

      <!-- ================================================================= -->
      <!-- BAB 02: BESI (FE), FERRITIN, & PEDOMAN AGA 2024                  -->
      <!-- ================================================================= -->
      <article id="emn3-02" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 02 · Merangkum Slide 9, 10, 11</span>
          <span class="badge badge-crimson">Topik Paling Sering Diuji</span>
        </div>
        <h2>Besi (Fe): 3 Stadium Defisiensi, Gejala Pica, &amp; Pedoman Terapi AGA 2024</h2>
        <p class="bento-sub">Jangan tertipu oleh MCV yang normal. Pahami perjalanan alami penipisan besi dan aturan mutakhir suplementasi oral.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Stadium 1: Cadangan Turun (Iron Depletion)</div>
                <div class="tile-title">{tt("Ferritin", "Ferritin Serum", "Protein pengikat cadangan besi di hati dan makrofag.", "Biomarker paling awal turun (<15–30 ng/mL) sebelum Hb/MCV turun.")} Turun ({cl("&lt;15–30 ng/mL")}) · Hb &amp; MCV Normal</div>
                <div class="tile-body">Cadangan besi di hati dan makrofag sumsum tulang habis. Eritropoiesis masih dipertahankan dari besi sirkulasi. <b>Pasien belum anemia</b>, namun sudah bisa mengeluh cepat lelah.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Stadium 2: Eritropoiesis Terbatas (Iron-Deficient Erythropoiesis)</div>
                <div class="tile-title">TSAT Anjlok ({cl("&lt;16–20%")}) · TIBC Meningkat</div>
                <div class="tile-body">Besi transport tidak mencukupi untuk kebutuhan sumsum tulang. Pembentukan eritrosit mulai terhambat. Hb mulai menurun di ambang batas.</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Stadium 3: Anemia Defisiensi Besi Nyata (IDA)</div>
                <div class="tile-title">Hb &lt;12 g/dL · MCV {cl("&lt;80 fL (Mikrositik Hipokromik)")}</div>
                <div class="tile-body">Bentuk lanjut: pucat, konjungtiva anemis, koilonychia (kuku sendok), atrofi papil lidah, dan {tt("Pagophagia", "Pagophagia", "Pica spesifik mengunyah es batu berulang kali.", "Tanda klinis patognomonik defisiensi besi.")}.</div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">Pembaruan Pedoman AGA 2024 (Slide 11)</div>
              <div class="pearl-title">Mengapa Besi Oral Tidak Boleh Diberikan 3x Sehari?</div>
              <p>Setiap dosis besi oral diserap di duodenum, tubuh merespons dengan memproduksi hormon {tt("Hepcidin", "Hepcidin", "Hormon peptida pengatur utama kadar besi sistemik.", "Mengikat dan menginternalisasi ferroportin -> memblokir absorpsi besi di duodenum selama 24–48 jam.")} di hati. Hepcidin mengunci gerbang <i>ferroportin</i> selama 24–48 jam. Jika Anda memberi tablet besi 3x sehari, dosis ke-2 dan ke-3 tidak diserap dan hanya menimbulkan efek samping mual serta konstipasi. <b>Rekomendasi AGA 2024: {cl("Maksimal 1x/hari pagi hari atau selang-hari (alternate-day)!")}</b></p>
            </div>
          </div>

          <div class="slide-dock">
            <div class="dock-nav">
              <button type="button" class="dock-btn active" onclick="swapDockSlide('d2', 'slides_kul3/slide_10.jpg', 'Slide 10 · 3 Stadium Defisiensi Besi', this)">Slide 10</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d2', 'slides_kul3/slide_11.jpg', 'Slide 11 · Rekomendasi Terapi AGA 2024', this)">Slide 11</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d2', 'slides_kul3/slide_9.jpg', 'Slide 9 · Peran Fisiologis Fe & Hepcidin', this)">Slide 9</button>
            </div>
            <img id="dock-img-d2" src="slides_kul3/slide_10.jpg" alt="Bukti Slide 10" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d2').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d2">Slide 10 · 3 Stadium Defisiensi Besi</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

      <!-- ================================================================= -->
      <!-- BAB 03: SENG (ZN), KULIT, & FITAT                                -->
      <!-- ================================================================= -->
      <article id="emn3-03" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 03 · Merangkum Slide 12</span>
          <span class="badge badge-emerald">Dermatologi &amp; Imunitas</span>
        </div>
        <h2>Seng (Zn): Trias Gejala Khas, Integritas Kulit, &amp; Bahaya Fitat</h2>
        <p class="bento-sub">Seng adalah kofaktor lebih dari 300 enzim metalloproteinase, esensial untuk sintesis protein, transkripsi gen jari-seng (zinc-finger), dan pembelahan sel epitel.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Trias Patognomonik Defisiensi Seng</div>
                <div class="tile-title">{cl("Dermatitis Periorifisial + Diare Kronik + Alopesia")}</div>
                <div class="tile-body">Ruam eritematosa bersisik berkrusta di sekitar lubang tubuh (mulut, hidung, mata, perineum) dan akral (jari tangan/kaki). Menyerupai penyakit herediter {tt("Acrodermatitis enteropathica", "Acrodermatitis Enteropathica", "Kelainan resesif autosomal mutasi transporter seng ZIP4.", "Trias: dermatitis periorifisial & akral, diare kronik, alopesia.")}.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Gejala Penyerta Lainnya</div>
                <div class="tile-title">Luka Sulit Sembuh · Disgeusia · Retardasi Pertumbuhan</div>
                <div class="tile-body">Gangguan pengecapan (hipogeusia) dan penciuman karena zinc esensial untuk enzim <i>gustin</i> di papil lidah. Pada anak memicu stunting dan penurunan imunitas sel T.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Faktor Risiko Utama: Fitat</div>
                <div class="tile-title">{tt("Fitat", "Asam Fitat (Phytic Acid)", "Senyawa penyimpan fosfor pada biji gandum & serealia tak beragi.", "Membentuk kelat tak larut dengan Seng di lumen usus -> mencegah absorpsi.")}</div>
                <div class="tile-body">Asam fitat pada gandum dan biji-bijian membentuk kompleks tak larut dengan seng di lumen usus, mencegah penyerapan. Rawan pada populasi diet tinggi sereal nabati tanpa protein hewani.</div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">UAB Trap Alert</div>
              <div class="pearl-title">Suplementasi Zinc pada Diare Anak</div>
              <p>WHO merekomendasikan Zinc {cl("20 mg/hari")} selama 10–14 hari pada diare akut anak untuk meregenerasi mikrovili mukosa usus yang rusak dan menurunkan mortalitas diare hingga 23%.</p>
            </div>
          </div>

          <div class="slide-dock">
            <img src="slides_kul3/slide_12.jpg" alt="Bukti Slide 12" class="dock-img" onclick="openZoom(this.src, 'Slide 12 · Seng (Zn) — Pertumbuhan, Kulit, Imunitas')" />
            <div class="dock-foot">
              <span>Slide 12 · Seng (Zn) — Pertumbuhan, Kulit, Imunitas</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

      <!-- ================================================================= -->
      <!-- BAB 04: KALSIUM, MAGNESIUM, & HIPO-K                            -->
      <!-- ================================================================= -->
      <article id="emn3-04" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 04 · Merangkum Slide 14, 15, 16, 17, 20, 28</span>
          <span class="badge badge-amber">Kelistrikan Jantung &amp; Neuromuskular</span>
        </div>
        <h2>Kalsium, Magnesium, &amp; Mengapa Kalium Susah Naik Bila Mg Rendah</h2>
        <p class="bento-sub">Keseimbangan mineral ini saling mengunci. Memahami mekanisme kanal ROMK di tubulus ginjal adalah kunci menjawab soal hipokalemia refrakter.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Hipokalsemia &amp; Tanda Tetani</div>
                <div class="tile-title">Parestesia · {tt("Chvostek sign", "Tanda Chvostek", "Kedutan sudut bibir saat saraf fasialis diketuk.", "Tanda hipereksitabilitas neuromuskular akibat hipokalsemia.")} (+) · {tt("Trousseau sign", "Tanda Trousseau", "Spasme karpopedal saat manset tensimeter dipompa >sistolik 3 menit.", "Lebih sensitif dan spesifik dibanding tanda Chvostek.")} (+) · {cl("QT Panjang")}</div>
                <div class="tile-body">Kalsium ionisasi rendah meningkatkan permeabilitas natrium membran saraf, memicu hipereksitabilitas. Spasme karpopedal saat manset tensimeter dipompa (Trousseau) sangat sensitif. EKG: QT memanjang berisiko aritmia.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Mekanisme Ginjal: Hubungan Mg dan K (Slide 17)</div>
                <div class="tile-title">{tt("ROMK", "Renal Outer Medullary Potassium Channel", "Kanal sekresi kalium di sel prinsipal tubulus distal ginjal.", "Dihambat oleh Mg intrasel. Jika Mg rendah, kanal terbuka -> Kalium bocor masif ke urin.")} Memicu Kebocoran Kalium Urin</div>
                <div class="tile-body">Di sel tubulus distal ginjal, Magnesium intrasel berfungsi sebagai penghambat alami kanal ROMK. Bila Mg serum anjlok ({cl("&lt;1.7 mg/dL")}), kanal ROMK terbuka lebar tanpa kontrol &rarr; Kalium terus menerus dibuang ke urin. Diberi Kalium oral/IV sebanyak apa pun, kalium akan langsung lolos terbuang. <b>{cl("Wajib koreksi Mg dulu!")}</b></div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Temuan EKG Hipokalemia (Slide 20)</div>
                <div class="tile-title">Gelombang T Mendatar · ST Depresi · {cl("Muncul Gelombang U")}</div>
                <div class="tile-body">Gejala klinis: lemas otot flaksid, kram betis, konstipasi/ileus paralitik (otot polos usus lumpuh). Hati-hati diuretik loop (furosemid) membuang Mg dan K sekaligus.</div>
              </div>
            </div>
          </div>

          <div class="slide-dock">
            <div class="dock-nav">
              <button type="button" class="dock-btn active" onclick="swapDockSlide('d4', 'slides_kul3/slide_17.jpg', 'Slide 17 · Mengapa K sulit naik bila Mg rendah', this)">Slide 17</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d4', 'slides_kul3/slide_15.jpg', 'Slide 15 · Hipokalsemia', this)">Slide 15</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d4', 'slides_kul3/slide_20.jpg', 'Slide 20 · Hipokalemia', this)">Slide 20</button>
            </div>
            <img id="dock-img-d4" src="slides_kul3/slide_17.jpg" alt="Bukti Slide 17" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d4').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d4">Slide 17 · Mengapa K sulit naik bila Mg rendah</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

      <!-- ================================================================= -->
      <!-- BAB 05: FOSFAT & REFEEDING SYNDROME                              -->
      <!-- ================================================================= -->
      <article id="emn3-05" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 05 · Merangkum Slide 18, 19, 29</span>
          <span class="badge badge-crimson">Kegawatan Nutrisi Fatal</span>
        </div>
        <h2>Fosfat (P) &amp; Refeeding Syndrome: Krisis ATP yang Mengancam Jiwa</h2>
        <p class="bento-sub">Kelemahan diafragma akut dan aritmia fatal pada pasien pasca-kelaparan yang diberi makan terlalu cepat.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Fase 1: Malnutrisi Kronik</div>
                <div class="tile-title">Cadangan Fosfat &amp; Elektrolit Total Tubuh Menyusut</div>
                <div class="tile-body">Pada puasa lama, anoreksia, atau alkoholisme, tubuh membakar lemak &amp; protein. Serum fosfat tampak masih normal semu karena kompensasi ginjal, namun cadangan intrasel sudah kritis.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Fase 2: Nutrisi Karbohidrat Dimulai</div>
                <div class="tile-title">Lonjakan Insulin Mendorong Elektrolit Masuk ke Sel</div>
                <div class="tile-body">Glukosa memicu pankreas memompa Insulin dalam jumlah masif. Insulin merangsang glikolisis dan transpor glukosa bersama <b>Fosfat (P), Kalium (K), dan Magnesium (Mg) ke intrasel</b>.</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Fase 3: Hipofosfatemia Berat ({cl("&lt;1.0 mg/dL")})</div>
                <div class="tile-title">Kegagalan Sintesis ATP &rarr; Gagal Napas &amp; Kematian</div>
                <div class="tile-body">Tanpa fosfat ekstraseluler, sintesis ATP dan 2,3-DPG eritrosit lumpuh total. Otot diafragma gagal berkontraksi ({cl("takipnea lalu henti napas")}), otot jantung mengalami kardiomiopati akut dan aritmia fatal.</div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">Protokol Pencegahan ASPEN / NICE (Slide 19)</div>
              <div class="pearl-title">Aturan Emas Memulai Nutrisi pada Pasien Malnutrisi Berat</div>
              <p>1. Berikan <b>Tiamin (B1) oral/IV sebelum nutrisi dimulai</b> untuk mencegah ensefalopati Wernicke.<br>
              2. Mulai kalori sangat rendah: <b>{cl("10–15 kkal/kg/hari")}</b>, naikkan bertahap dalam 4–7 hari.<br>
              3. Pantau kadar serum <b>Fosfat, Kalium, dan Magnesium serial</b> tiap 24 jam selama 3 hari pertama.</p>
            </div>
          </div>

          <div class="slide-dock">
            <img src="slides_kul3/slide_19.jpg" alt="Bukti Slide 19" class="dock-img" onclick="openZoom(this.src, 'Slide 19 · Refeeding Syndrome')" />
            <div class="dock-foot">
              <span>Slide 19 · Pola Refeeding Syndrome</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

      <!-- ================================================================= -->
      <!-- BAB 06: TEMBAGA, IODIUM, & SELENIUM                              -->
      <!-- ================================================================= -->
      <article id="emn3-06" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 06 · Merangkum Slide 13, 22, 23</span>
          <span class="badge badge-emerald">Mikromineral Unik</span>
        </div>
        <h2>Tembaga (Cu) vs Seng, Iodium (I), &amp; Selenium (Penyakit Keshan)</h2>
        <p class="bento-sub">Interaksi kompetitif antar-mineral yang sering muncul sebagai skenario kasus iatrogenik di ujian UAB.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Tembaga (Cu) &amp; Jebakan Zinc Berlebih (Slide 22)</div>
                <div class="tile-title">{cl("Anemia Mikrositik + Neutropenia + Mielopati")}</div>
                <div class="tile-body">Tembaga adalah komponen <i>ceruloplasmin</i> (ferroksidase untuk transportasi besi). Defisiensi Cu memicu anemia yang tidak membaik dengan besi, disertai neutropenia dan degenerasi kolumna dorsalis medula spinalis (mirip defisiensi B12). Pemicu klasik: <b>suplemen Zinc dosis tinggi atau perekat gigi palsu kaya zinc</b> yang memicu induksi {tt("Metallothionein", "Metallothionein", "Protein pengikat logam di enterosit usus.", "Diinduksi oleh zinc dosis tinggi. Mengikat tembaga dengan afinitas kuat -> Cu terperangkap & terbuang.")}!</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Iodium (I) &amp; Perkembangan Saraf (Slide 13)</div>
                <div class="tile-title">Gondok Endemik pada Dewasa · {tt("Kretinisme", "Kretinisme Endemik", "Sindrom defisit neurologis dan fisik janin akibat kekurangan iodium ibu hamil.", "Gejala: retardasi mental berat, tuli-bisu, cebol, spastisitas.")} pada Janin</div>
                <div class="tile-body">Iodium adalah bahan baku T3/T4. Defisiensi &rarr; umpan balik negatif berkurang &rarr; TSH hipofisis melonjak &rarr; hiperplasia folikel tiroid (struma/gondok). Bila terjadi pada ibu hamil, janin mengalami kretinisme neurologis.</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Selenium (Se) &amp; Penyakit Keshan (Slide 23)</div>
                <div class="tile-title">Antioksidan Selenoprotein · {tt("Penyakit Keshan", "Penyakit Keshan", "Kardiomiopati kongestif endemik akibat defisiensi selenium di tanah miskin Se.", "Terjadi terutama pada anak dan wanita usia subur; dapat fatal.")}</div>
                <div class="tile-body">Selenium merupakan kofaktor enzim <i>Glutathione Peroxidase</i> dan <i>Deiodinase</i>. Defisiensi di daerah tanah miskin selenium memicu kardiomiopati kongestif fatal terutama pada anak dan wanita muda.</div>
              </div>
            </div>
          </div>

          <div class="slide-dock">
            <div class="dock-nav">
              <button type="button" class="dock-btn active" onclick="swapDockSlide('d6', 'slides_kul3/slide_22.jpg', 'Slide 22 · Tembaga (Cu)', this)">Slide 22</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d6', 'slides_kul3/slide_13.jpg', 'Slide 13 · Iodium (I)', this)">Slide 13</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d6', 'slides_kul3/slide_23.jpg', 'Slide 23 · Selenium (Se)', this)">Slide 23</button>
            </div>
            <img id="dock-img-d6" src="slides_kul3/slide_22.jpg" alt="Bukti Slide 22" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d6').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d6">Slide 22 · Tembaga (Cu) — Darah &amp; Saraf</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

      <!-- ================================================================= -->
      <!-- BAB 07: PETA ORGAN & 3 KASUS ASLI DR. IWAL                       -->
      <!-- ================================================================= -->
      <article id="emn3-07" class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Bab 07 · Merangkum Slide 3, 8, 24, 27, 28, 29</span>
          <span class="badge badge-crimson">Bedah Kasus Asli Dosen</span>
        </div>
        <h2>Peta Organ &amp; Pembahasan Tuntas 3 Kasus Asli Diskusi dr. Iwal</h2>
        <p class="bento-sub">Dosen mengambil 4 soal UAB dari pola kasus seperti ini. Pelajari bagaimana menghubungkan data laboratorium dengan diagnosis pasti.</p>

        <div class="bento-split">
          <div>
            <div class="step-grid">
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Kasus 1: Mikrositosis &amp; Pagophagia (Slide 27)</div>
                <div class="tile-title">Perempuan 29 Th · Hb 8.9 · MCV 68 · Ferritin 7 ng/mL</div>
                <div class="tile-body">
                  <b>Diagnosis:</b> Anemia Defisiensi Besi sekunder akibat menorrhagia kronik.<br>
                  <b>Rasional:</b> Ferritin sangat rendah (&lt;15 ng/mL) adalah bukti konfirmasi absolut penipisan cadangan besi. Pagophagia (mengunyah es batu) adalah pica spesifik.<br>
                  <b>Tatalaksana:</b> Berikan preparat besi oral 1x/hari (atau selang hari) + rujuk ginekologi untuk atasi menorrhagia.
                </div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Kasus 2: Hipokalemia Refrakter (Slide 28)</div>
                <div class="tile-title">Laki-laki 67 Th · Diuretik · K 2.8 · Gelombang U · Mg 1.1 mg/dL</div>
                <div class="tile-body">
                  <b>Diagnosis:</b> Hipokalemia refrakter akibat hipomagnesemia tersembunyi.<br>
                  <b>Rasional:</b> Furosemid membuang K dan Mg. Selama Mg &lt;1.7 mg/dL, kanal ROMK ginjal bocor terus.<br>
                  <b>Tatalaksana:</b> Koreksi Magnesium IV/oral wajib dilakukan bersamaan dengan Kalium. Pantau EKG serial untuk gelombang U.
                </div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Kasus 3: Sesak Pasca-Nutrisi (Slide 29)</div>
                <div class="tile-title">Laki-laki 46 Th · Malnutrisi 12 Hari · P 0.8 mg/dL · Takipnea</div>
                <div class="tile-body">
                  <b>Diagnosis:</b> Refeeding Syndrome terkomplikasi gagal napas akut.<br>
                  <b>Rasional:</b> Hipofosfatemia berat (&lt;1.0 mg/dL) melumpuhkan ATP diafragma.<br>
                  <b>Tatalaksana:</b> Hentikan/turunkan laju nutrisi segera, koreksi Fosfat IV terkontrol, suplementasi tiamin, monitor serial elektrolit tiap 12 jam.
                </div>
              </div>
            </div>
          </div>

          <div class="slide-dock">
            <div class="dock-nav">
              <button type="button" class="dock-btn active" onclick="swapDockSlide('d7', 'slides_kul3/slide_27.jpg', 'Slide 27 · Kasus 1 Mikrositosis', this)">Kasus 1</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d7', 'slides_kul3/slide_28.jpg', 'Slide 28 · Kasus 2 Hipo-K Refrakter', this)">Kasus 2</button>
              <button type="button" class="dock-btn" onclick="swapDockSlide('d7', 'slides_kul3/slide_29.jpg', 'Slide 29 · Kasus 3 Refeeding', this)">Kasus 3</button>
            </div>
            <img id="dock-img-d7" src="slides_kul3/slide_27.jpg" alt="Bukti Slide 27" class="dock-img" onclick="openZoom(this.src, document.getElementById('dock-cap-d7').textContent)" />
            <div class="dock-foot">
              <span id="dock-cap-d7">Slide 27 · Kasus 1 Mikrositosis &amp; Pagophagia</span>
              <span>Zoom ↗</span>
            </div>
          </div>
        </div>
      </article>

    </div>

    <!-- =================================================================== -->
    <!-- VIEW 2: CROSS-BLOCK KNOWLEDGE LINKING (FEATURE 5)                   -->
    <!-- =================================================================== -->
    <div id="view-bridge" class="view-section">
      <div class="cross-bridge-card">
        <div class="bento-header">
          <span class="ch-index">Sistem Terintegrasi FK</span>
          <span class="badge badge-cobalt">Peta 8 Blok Preklinik</span>
        </div>
        <h2>Jembatan Klinis Lintas Blok: Menghubungkan Semester 1 s.d. 3</h2>
        <p class="bento-sub">Dosen sering menguji konsep mineral dengan menghubungkannya ke materi patologi, histologi, dan biokimia dari blok-blok sebelumnya.</p>

        <div class="bridge-tabs">
          <button type="button" class="bridge-tab-btn active" onclick="switchBridge('br-anemia', this)">🩸 1. Sindrom Anemia Mikrositik</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridge('br-ginjal', this)">⚡ 2. Regulasi Elektrolit &amp; Ginjal</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridge('br-atp', this)">🔥 3. Refeeding, Glikolisis, &amp; ATP</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridge('br-tulang', this)">🦴 4. Metabolisme Kalsium &amp; Tulang</button>
        </div>

        <!-- PANE 1: ANEMIA -->
        <div id="br-anemia" class="bridge-pane active">
          <p style="font-size:0.92rem;color:var(--ink-700);line-height:1.6;"><b>Diagnosis Banding Anemia Mikrositik Hipokromik (MCV &lt; 80 fL):</b> Tiga penyakit dari tiga blok berbeda yang saling diadu di ujian UAB:</p>
          <div class="bridge-grid">
            <div class="bridge-node">
              <span class="bridge-block-tag tag-emn">Blok 9 (EMN) · Defisiensi Besi</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Anemia Defisiensi Besi (IDA)</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                • <b>Ferritin:</b> Turun drastis (&lt;15–30 ng/mL)<br>
                • <b>TIBC:</b> Meningkat (&gt;400 &mu;g/dL)<br>
                • <b>RDW:</b> Melebar (anisositosis nyata)<br>
                • <b>Penyebab:</b> Menorrhagia, perdarahan saluran cerna.
              </div>
            </div>
            <div class="bridge-node">
              <span class="bridge-block-tag tag-bms">Blok 2 (BMS 1) · Genetika Sel</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Thalassemia Trait (&alpha; / &beta;)</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                • <b>Ferritin:</b> Normal atau justru meningkat!<br>
                • <b>TIBC:</b> Normal<br>
                • <b>RDW:</b> Cenderung normal/homogen<br>
                • <b>Mentzer Index (MCV/RBC):</b> &lt; 13 (sangat mengarah ke thal)<br>
                • <b>Diagnosis Pasti:</b> Hb elektroforesis (HbA2 naik).
              </div>
            </div>
            <div class="bridge-node">
              <span class="bridge-block-tag tag-hi">Blok 8 (HI) · Imunologi &amp; Infeksi</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Anemia Penyakit Kronis (ACD)</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                • <b>Ferritin:</b> Normal atau MENINGKAT (reaktan fase akut)<br>
                • <b>Hepcidin:</b> Melonjak drastis akibat stimulasi sitokin IL-6<br>
                • <b>Mekanisme:</b> Besi terperangkap di dalam makrofag sistem retikuloendotelial, tidak bisa dipakai sumsum tulang.
              </div>
            </div>
          </div>
        </div>

        <!-- PANE 2: GINJAL -->
        <div id="br-ginjal" class="bridge-pane">
          <p style="font-size:0.92rem;color:var(--ink-700);line-height:1.6;"><b>Korelasi Fisiologi Ginjal dan Kelistrikan Jantung:</b></p>
          <div class="bridge-grid">
            <div class="bridge-node">
              <span class="bridge-block-tag tag-bms">Blok 5 (BMS 4) · Faal Ginjal</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Kanal ROMK &amp; Na-K-2Cl</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                Di ansa Henle tebal dan tubulus distal, kanal ROMK meregenerasi kalium ke lumen. Magnesium intrasel bertindak sebagai sumbat alami (voltage-gate block). Bila Mg anjlok, kalium loss tak terkendali.
              </div>
            </div>
            <div class="bridge-node">
              <span class="bridge-block-tag tag-bdt">Blok 7 (BDT) · Gawat Darurat</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Aritmia &amp; Protokol KCl IV</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                Hipokalemia memicu gelombang U dan risiko Torsades de Pointes. Pemberian Kalium IV maksimal 10–20 mEq/jam lewat vena perifer untuk cegah flebitis dan henti jantung asistol.
              </div>
            </div>
          </div>
        </div>

        <!-- PANE 3: ATP -->
        <div id="br-atp" class="bridge-pane">
          <p style="font-size:0.92rem;color:var(--ink-700);line-height:1.6;"><b>Biokimiawi Refeeding Syndrome:</b></p>
          <div class="bridge-grid">
            <div class="bridge-node">
              <span class="bridge-block-tag tag-bms">Blok 4 (BMS 3) · Metabolisme Karbohidrat</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Jalur Glikolisis &amp; Fosforilasi</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                Setiap 1 molekul glukosa yang masuk glikolisis membutuhkan fosfat bebas untuk membentuk Glukosa-6-P dan Fruktosa-1,6-bifosfat. Saat insulin memicu glikolisis massal, fosfat serum tersedot habis &rarr; sintesis ATP anjlok.
              </div>
            </div>
            <div class="bridge-node">
              <span class="bridge-block-tag tag-emn">Blok 9 (EMN) · Gizi Klinis</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Pencegahan Malnutrisi &amp; Stunting</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                Pemberian F-75 (formula rendah protein dan kalori) pada fase stabilisasi malnutrisi berat anak bertujuan mencegah refeeding syndrome sebelum beralih ke F-100 fase transisi.
              </div>
            </div>
          </div>
        </div>

        <!-- PANE 4: TULANG -->
        <div id="br-tulang" class="bridge-pane">
          <p style="font-size:0.92rem;color:var(--ink-700);line-height:1.6;"><b>Regulasi Kalsium dan Resorpsi Tulang:</b></p>
          <div class="bridge-grid">
            <div class="bridge-node">
              <span class="bridge-block-tag tag-bms">Blok 3 (BMS 2) · Histologi Tulang</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Osteoblas vs Osteoklas</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                PTH merangsang ligan RANKL pada osteoblas, yang mengaktifkan reseptor RANK pada osteoklas untuk meresorpsi hidroksiapatit tulang dan melepaskan ion Ca ke darah.
              </div>
            </div>
            <div class="bridge-node">
              <span class="bridge-block-tag tag-emn">Blok 9 (EMN) · Vitamin D</span>
              <div style="font-weight:700;font-size:0.95rem;margin-bottom:4px;">Kalsitriol 1,25-(OH)2D3</div>
              <div style="font-size:0.84rem;color:var(--ink-700);line-height:1.5;">
                Dihidroksilasi di ginjal oleh 1&alpha;-hidroksilase (distimulasi PTH). Kalsitriol menginduksi sintesis <i>calbindin</i> di enterosit untuk menyerap kalsium dan fosfat dari makanan.
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 3: CBT SIMULATOR ADAPTIF DENGAN UWORLD METRICS (FEATURE 3)     -->
    <!-- =================================================================== -->
    <div id="view-soal" class="view-section">
      <div class="cbt-header">
        <div>
          <h2>8 Soal Latihan Adaptif Karakter dr. Iwal Reza Ahdi, Sp.PD</h2>
          <p style="color:var(--ink-500);font-size:0.92rem;margin-top:4px;">Dilengkapi Metrik Keyakinan UWorld (Confidence Tracker) untuk mendeteksi miskonsepsi berbahaya.</p>
        </div>
        <div class="cbt-stat-card">
          <span class="cbt-stat-val" id="cbt-score">0 / 8</span>
          <span class="cbt-stat-lbl">Skor Akurasi</span>
        </div>
      </div>

      <!-- Feature 3: UWorld Diagnostic Dashboard -->
      <div class="diag-dashboard">
        <div class="diag-card" style="border-color:#0B6350;">
          <div class="diag-val" id="diag-mastered" style="color:#0B6350;">0</div>
          <div class="diag-lbl">🏆 Tuntas (Benar + Yakin)</div>
        </div>
        <div class="diag-card" style="border-color:#9E5400;">
          <div class="diag-val" id="diag-lucky" style="color:#9E5400;">0</div>
          <div class="diag-lbl">⚠️ Tebakan Beruntung (Benar + Ragu)</div>
        </div>
        <div class="diag-card" style="border-color:#B82921;">
          <div class="diag-val" id="diag-danger" style="color:#B82921;">0</div>
          <div class="diag-lbl">🚨 Miskonsepsi Berbahaya (Salah + Yakin)</div>
        </div>
        <div class="diag-card" style="border-color:#164F73;">
          <div class="diag-val" id="diag-gap" style="color:#164F73;">0</div>
          <div class="diag-lbl">📖 Kesenjangan Konsep (Salah + Ragu)</div>
        </div>
      </div>

      <div class="cbt-filter-bar">
        <button type="button" class="cbt-filter-btn active" onclick="filterCBT('all', this)">Semua Soal (8)</button>
        <button type="button" class="cbt-filter-btn" onclick="filterCBT('kasus', this)">Kasus Vignette (5)</button>
        <button type="button" class="cbt-filter-btn" onclick="filterCBT('mekanisme', this)">Mekanisme &amp; Terapi (3)</button>
      </div>

      <div id="cbt-list"></div>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 4: CEK CEPAT H-1 UJIAN (FLASH SUMMARY)                         -->
    <!-- =================================================================== -->
    <div id="view-flash" class="view-section">
      <article class="bento-chapter">
        <div class="bento-header">
          <span class="ch-index">Flashcard Matriks</span>
          <span class="badge badge-emerald">Kunci Hafalan Cepat</span>
        </div>
        <h2>Matriks Seluruh Mineral untuk Review Kilat Sebelum Ujian</h2>
        <p class="bento-sub">Fokuskan mata pada kolom Gejala Patognomonik dan Nilai Lab Kunci:</p>

        <table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:0.92rem;">
          <thead>
            <tr style="background:var(--bg-subtle);border-bottom:2px solid var(--border);">
              <th style="padding:12px;text-align:left;">Mineral</th>
              <th style="padding:12px;text-align:left;">Organ Target</th>
              <th style="padding:12px;text-align:left;">Gejala Kunci Patognomonik</th>
              <th style="padding:12px;text-align:left;">Biomarker Laboratorium Kunci</th>
              <th style="padding:12px;text-align:left;">Jebakan Ujian UAB</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px;"><b>Besi (Fe)</b></td>
              <td style="padding:12px;">Darah &amp; Enzim</td>
              <td style="padding:12px;">Pagophagia (makan es batu), koilonychia, lemas.</td>
              <td style="padding:12px;"><b>Ferritin &lt; 15–30 ng/mL</b> (paling dini), TSAT &lt; 20%.</td>
              <td style="padding:12px;color:var(--crimson);">MCV normal tidak menyingkirkan defisiensi besi stadium awal!</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px;"><b>Seng (Zn)</b></td>
              <td style="padding:12px;">Kulit &amp; Imun</td>
              <td style="padding:12px;">Dermatitis periorifisial/akral, diare kronik, alopesia.</td>
              <td style="padding:12px;">Serum Zinc &lt; 70 &mu;g/dL.</td>
              <td style="padding:12px;color:var(--crimson);">Diet tinggi fitat menghambat absorpsi seng secara kuat.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px;"><b>Magnesium (Mg)</b></td>
              <td style="padding:12px;">Saraf &amp; Ginjal</td>
              <td style="padding:12px;">Tremor, tetani, aritmia, <b>hipokalemia refrakter</b>.</td>
              <td style="padding:12px;">Magnesium serum &lt; 1.7 mg/dL.</td>
              <td style="padding:12px;color:var(--crimson);">Kalium tidak bisa naik sebelum kadar Mg dikoreksi bersamaan!</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px;"><b>Fosfat (P)</b></td>
              <td style="padding:12px;">Energi (ATP)</td>
              <td style="padding:12px;">Kelemahan otot napas akut (takipnea), aritmia (Refeeding).</td>
              <td style="padding:12px;">Fosfat serum &lt; 1.0 mg/dL (berat).</td>
              <td style="padding:12px;color:var(--crimson);">Dipicu lonjakan insulin saat refeeding karbohidrat pada malnutrisi.</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px;"><b>Tembaga (Cu)</b></td>
              <td style="padding:12px;">Darah &amp; Saraf</td>
              <td style="padding:12px;">Anemia mikrositik + neutropenia + ataksia sensorik.</td>
              <td style="padding:12px;">Serum Cu rendah, ceruloplasmin rendah.</td>
              <td style="padding:12px;color:var(--crimson);">Dipicu konsumsi suplemen Zinc dosis tinggi berkepanjangan!</td>
            </tr>
            <tr style="border-bottom:1px solid var(--border);">
              <td style="padding:12px;"><b>Kalsium (Ca)</b></td>
              <td style="padding:12px;">Saraf &amp; Tulang</td>
              <td style="padding:12px;">Parestesia, tanda Chvostek/Trousseau (+), QT memanjang.</td>
              <td style="padding:12px;">Ionized Calcium (Ca bebas aktif).</td>
              <td style="padding:12px;color:var(--crimson);">99% Ca di tulang, serum normal belum tentu tulang aman.</td>
            </tr>
          </tbody>
        </table>
      </article>
    </div>

  </main>

  <!-- ZOOM MODAL -->
  <div id="zoom-modal" class="modal-overlay" onclick="closeZoom()">
    <div class="modal-window" onclick="event.stopPropagation()">
      <div class="modal-top">
        <strong id="zoom-title">Bukti Slide Asli Dosen</strong>
        <button type="button" class="cmdk-trigger" onclick="closeZoom()">Tutup (ESC)</button>
      </div>
      <img id="zoom-img" src="slides_kul3/slide_10.jpg" alt="Slide Zoom" />
    </div>
  </div>

  <!-- CMD+K MODAL -->
  <div id="search-modal" class="modal-overlay" onclick="closeSearchModal()">
    <div class="cmdk-box" onclick="event.stopPropagation()">
      <div class="cmdk-bar">
        <input type="text" id="cmdk-inp" class="cmdk-input" placeholder="Ketik kata kunci soal UAB / slide (contoh: Ferritin, Zinc, Refeeding, ROMK, B12)..." oninput="execSearch()" />
        <button type="button" class="cmdk-trigger" onclick="closeSearchModal()">ESC</button>
      </div>
      <div id="cmdk-out" class="cmdk-results"></div>
    </div>
  </div>

  <script src="vendor/uab_search_data.js"></script>

  <script>
    window.MOD_KEY = 'EMN_KUL3_MINERAL';

    window.QUIZ_DATA = [
      {{
        cat: 'kasus',
        stem: '1. Seorang perempuan berusia 29 tahun datang ke poliklinik dengan keluhan badan mudah lelah dan jantung berdebar saat beraktivitas ringan sejak 2 bulan terakhir. Pasien memiliki riwayat menstruasi sangat banyak (ganti pembalut 6-7 kali/hari) selama 8 hari setiap siklusnya. Pemeriksaan fisik menunjukkan konjungtiva pucat tanpa ikterus. Laboratorium: Hb 8,9 g/dL, leukosit 6.200/&mu;L, trombosit 380.000/&mu;L, MCV 68 fL, MCH 21 pg. Pasien mengaku sering sekali mengunyah es batu (pagophagia). Pemeriksaan biomarker manakah yang paling spesifik dan paling dini menurun untuk memastikan diagnosis pasien tersebut?',
        opts: [
          'Total Iron Binding Capacity (TIBC)',
          'Ferritin serum',
          'Saturasi transferrin (TSAT)',
          'Hemoglobin elektroforesis',
          'Bilirubin indirek serum'
        ],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Ferritin serum)</b><br>Kasus klasik Anemia Defisiensi Besi (Hb 8.9, MCV 68 fL mikrositik-hipokromik) akibat menorrhagia. Gejala <i>pagophagia</i> (pica makan es batu) adalah tanda khas defisiensi besi. Pada perjalanan alami defisiensi besi (Slide 10), <b>Ferritin serum adalah biomarker pertama yang anjlok (&lt;15–30 ng/mL)</b> mencerminkan habisnya cadangan besi tubuh, bahkan sebelum Hb dan MCV turun menjadi anemia.',
        slide: 'slides_kul3/slide_10.jpg',
        slideCap: 'Slide 10 · Perjalanan Defisiensi Besi: Ferritin Turun Lebih Awal'
      }},
      {{
        cat: 'kasus',
        stem: '2. Laki-laki 67 tahun dengan gagal jantung kongestif dan riwayat konsumsi furosemid mengeluh kelemahan otot tungkai dan palpitasi. EKG menunjukkan depresi segmen ST, gelombang T mendatar, dan muncul gelombang U yang prominen. Hasil laboratorium menunjukkan Kalium 2,8 mmol/L. Dokter telah memberikan suplementasi KCl oral dosis tinggi selama 3 hari, namun pada evaluasi ulang kadar Kalium pasien tetap rendah (2,9 mmol/L). Gangguan elektrolit penyerta manakah yang paling mendasari kondisi refrakter tersebut?',
        opts: [
          'Hiponatremia',
          'Hipokalsemia',
          'Hipomagnesemia',
          'Hiperfosfatemia',
          'Hiperkalsiuria'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Hipomagnesemia)</b><br>Furosemid membuang Kalium dan Magnesium sekaligus. Magnesium intrasel berfungsi sebagai inhibitor alami kanal ROMK di tubulus ginjal. Jika terjadi hipomagnesemia (Slide 17 & 28), kanal ROMK terbuka lebar tanpa kendali sehingga Kalium terus menerus bocor ke urin. Akibatnya, koreksi kalium menjadi refrakter (gagal naik). Kalium hanya bisa normal jika Magnesium dikoreksi bersamaan.',
        slide: 'slides_kul3/slide_17.jpg',
        slideCap: 'Slide 17 · Mengapa Kalium Sulit Naik Bila Magnesium Rendah?'
      }},
      {{
        cat: 'kasus',
        stem: '3. Anak laki-laki berusia 4 tahun dibawa ibunya dengan keluhan bercak kemerahan bersisik dan berkrusta di area sekitar mulut, anus, serta sela-sela jari kaki sejak 1 bulan. Anak juga mengalami diare berulang dan rambut rontok hingga tampak botak sebagian. Pasien memiliki riwayat diet monoton tinggi serealia dan bubur gandum tanpa asupan hewani. Defisiensi mikromineral apakah yang mendasari kondisi anak tersebut?',
        opts: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Seng (Zn)',
          'Selenium (Se)',
          'Mangan (Mn)'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Seng / Zn)</b><br>Trias patognomonik: <b>dermatitis periorifisial & akral, diare kronik, dan alopesia</b> merupakan tanda khas defisiensi Seng (Zinc) (Slide 12). Diet tinggi serealia/gandum mengandung asam <b>fitat</b> dalam kadar tinggi, yang mengikat seng di usus membentuk senyawa tak larut sehingga menghambat absorpsinya.',
        slide: 'slides_kul3/slide_12.jpg',
        slideCap: 'Slide 12 · Seng (Zn) — Pertumbuhan, Kulit, Imunitas & Peran Fitat'
      }},
      {{
        cat: 'kasus',
        stem: '4. Pasien laki-laki 46 tahun dengan riwayat malnutrisi berat dan puasa selama 12 hari dirawat di bangsal. Dokter segera memberikan nutrisi parenteral tinggi karbohidrat. Dalam waktu 48 jam, pasien mendadak mengalami sesak napas berat (takipnea), kelemahan otot menyeluruh, dan takikardia. Manakah gangguan biokimiawi serum di bawah ini yang menjadi pemicu utama kegagalan napas akut tersebut?',
        opts: [
          'Hiponatremia berat (&lt;120 mEq/L)',
          'Hipokalsemia terionisasi',
          'Hipofosfatemia berat (&lt;1.0 mg/dL)',
          'Asidosis laktat berat',
          'Hiperglikemia hiperosmolar'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Hipofosfatemia berat &lt;1.0 mg/dL)</b><br>Pasien mengalami <i>Refeeding Syndrome</i> (Slide 19 & 29). Pemberian nutrisi memicu lonjakan insulin yang mendorong glukosa bersama Fosfat, Kalium, dan Magnesium masuk masif ke dalam sel. Terjadilah hipofosfatemia berat yang menghentikan sintesis ATP seluler, sehingga otot diafragma lumpuh (kelemahan napas akut), kardiomiopati akut, dan aritmia.',
        slide: 'slides_kul3/slide_19.jpg',
        slideCap: 'Slide 19 · Pola Refeeding Syndrome: Pergeseran Elektrolit Akut'
      }},
      {{
        cat: 'kasus',
        stem: '5. Perempuan 35 tahun pasca-operasi bypass lambung (bariatrik) datang dengan keluhan baal dan kesemutan di kedua kaki serta gangguan berjalan (ataksia). Laboratorium menunjukkan Hb 9,0 g/dL, MCV 72 fL (mikrositik), dan neutropenia berat (ANC 750/&mu;L). Pasien mengaku mengonsumsi suplemen Zinc dosis tinggi (80 mg/hari) selama 8 bulan terakhir untuk menjaga imunitas. Defisiensi mineral apakah yang paling tepat menjelaskan kondisi pasien?',
        opts: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Iodium (I)',
          'Selenium (Se)',
          'Kalsium (Ca)'
        ],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Tembaga / Cu)</b><br><b>Anemia mikrositik + neutropenia + mielopati/gejala neurologis</b> adalah manifestasi klasik defisiensi Tembaga (Cu) (Slide 22). Zinc dosis tinggi menginduksi metallothionein di enterosit yang mengikat tembaga dan memblokir absorpsinya, memicu defisiensi tembaga iatrogenik.',
        slide: 'slides_kul3/slide_22.jpg',
        slideCap: 'Slide 22 · Tembaga (Cu) & Pemicu Iatrogenik Suplemen Zinc'
      }},
      {{
        cat: 'mekanisme',
        stem: '6. Berdasarkan Clinical Practice Update dari American Gastroenterological Association (AGA 2024), bagaimanakah aturan suplementasi besi oral yang paling tepat dan dapat ditoleransi optimal pada pasien anemia defisiensi besi?',
        opts: [
          'Diberikan dosis tinggi 3 kali sehari bersama makanan',
          'Diberikan dosis terbagi setiap 6 jam disertai antasida',
          'Diberikan maksimal 1 kali sehari atau rejimen selang-hari (alternate-day)',
          'Diberikan bersamaan dengan susu sapi untuk mengurangi iritasi lambung',
          'Diberikan 4 kali sehari dalam dosis kecil'
        ],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Maksimal 1 kali sehari atau selang-hari)</b><br>Pedoman AGA 2024 (Slide 11) menekankan bahwa setiap dosis besi memicu lonjakan hormon <b>Hepcidin</b> yang memblokade absorpsi besi selanjutnya selama 24–48 jam. Pemberian maksimal 1x/hari atau selang-hari memberikan penyerapan fraksional lebih tinggi dengan efek samping mual/konstipasi yang jauh lebih minimal.',
        slide: 'slides_kul3/slide_11.jpg',
        slideCap: 'Slide 11 · Terapi Fe: AGA Clinical Practice Update (2024)'
      }},
      {{
        cat: 'mekanisme',
        stem: '7. Pemeriksaan fisik pada pasien dengan kecurigaan hipokalsemia menunjukkan adanya spasme karpopedal pada tangan ketika manset tensimeter dipompa di atas tekanan sistolik selama 3 menit. Disebut apakah tanda fisik klinis patognomonik tersebut?',
        opts: [
          'Chvostek sign',
          'Trousseau sign',
          'Kernig sign',
          'Brudzinski sign',
          'Babinski sign'
        ],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Trousseau sign)</b><br>Trousseau sign (spasme karpopedal akibat iskemia saraf brakialis oleh manset tensimeter) sangat sensitif dan spesifik untuk hipokalsemia simptomatik (Slide 15). Chvostek sign adalah kedutan sudut bibir saat saraf fasialis diketuk di anterior telinga.',
        slide: 'slides_kul3/slide_15.jpg',
        slideCap: 'Slide 15 · Hipokalsemia: Tanda Klinis & Evaluasi Penyebab'
      }},
      {{
        cat: 'mekanisme',
        stem: '8. Seorang wanita hamil di daerah pegunungan pedalaman yang jarang mengonsumsi garam beriodium melahirkan bayi dengan keterlambatan perkembangan saraf berat, perawakan pendek, dan tuli-bisu. Mekanisme patofisiologi apakah yang mendasari kondisi kretinisme pada bayi tersebut?',
        opts: [
          'Kekurangan iodium memicu hambatan sintesis T3/T4 yang vital bagi mielinisasi dan perkembangan otak janin',
          'Kelebihan TSH ibu menembus plasenta dan merusak kelenjar tiroid janin',
          'Defisiensi selenium langsung menghambat enzim deiodinase perifer tanpa melibatkan hormon tiroid',
          'Kadar kalsium yang rendah mengganggu pembentukan neurotransmitter otak',
          'Fosfat yang rendah menyebabkan kegagalan pembentukan mielin saraf'
        ],
        ans: 0,
        exp: '<b>Jawaban Benar: A</b><br>Iodium adalah substrat mutlak sintesis hormon tiroid T3/T4 (Slide 13). Pada kehamilan, hormon tiroid ibu dan janin sangat krusial untuk neurogenesis, migrasi neuron, dan mielinisasi otak janin. Defisiensi berat menyebabkan sindrom kretinisme endemik dengan retardasi mental permanen.',
        slide: 'slides_kul3/slide_13.jpg',
        slideCap: 'Slide 13 · Iodium (I) — Sintesis Hormon Tiroid & Bahaya Kehamilan'
      }}
    ];

    {BASE_JS}

    // =========================================================================
    // FEATURE 2: ACTIVE MASKING / CLOZE MODE CONTROLLER
    // =========================================================================
    let clozeMode = false;
    function toggleClozeMode() {{
      clozeMode = !clozeMode;
      document.body.classList.toggle('cloze-active', clozeMode);
      const btn = document.getElementById('cloze-toggle');
      const badge = document.getElementById('cloze-status-text');
      if (clozeMode) {{
        btn.classList.add('active');
        badge.textContent = 'ON';
        document.querySelectorAll('.cloze-mask').forEach(el => el.classList.remove('revealed'));
      }} else {{
        btn.classList.remove('active');
        badge.textContent = 'OFF';
      }}
    }}

    document.addEventListener('keydown', e => {{
      if (e.key.toLowerCase() === 'm' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {{
        toggleClozeMode();
      }}
    }});

    // =========================================================================
    // FEATURE 3: UWORLD CONFIDENCE & DIAGNOSTIC MATRIX
    // =========================================================================
    let userConfidence = {{}}; // idx -> 'high' | 'low'
    let questionOutcomes = {{}}; // idx -> 'mastered' | 'lucky' | 'danger' | 'gap'

    function setConfidence(qIdx, level) {{
      userConfidence[qIdx] = level;
      const qm = document.getElementById('qm-' + qIdx);
      if (!qm) return;
      const btns = qm.querySelectorAll('.conf-btn');
      btns.forEach(b => b.classList.remove('active-high', 'active-low'));
      if (level === 'high') btns[0].classList.add('active-high');
      else btns[1].classList.add('active-low');
    }}

    function calculateUWorldMetrics() {{
      let mastered = 0, lucky = 0, danger = 0, gap = 0;
      Object.keys(userAns).forEach(idx => {{
        const qIdx = parseInt(idx);
        const q = window.QUIZ_DATA[qIdx];
        const isRight = userAns[qIdx] === q.ans;
        const conf = userConfidence[qIdx] || 'high'; // default high

        if (isRight && conf === 'high') {{
          mastered++;
          questionOutcomes[qIdx] = 'mastered';
        }} else if (isRight && conf === 'low') {{
          lucky++;
          questionOutcomes[qIdx] = 'lucky';
        }} else if (!isRight && conf === 'high') {{
          danger++;
          questionOutcomes[qIdx] = 'danger';
        }} else {{
          gap++;
          questionOutcomes[qIdx] = 'gap';
        }}
      }});

      document.getElementById('diag-mastered').textContent = mastered;
      document.getElementById('diag-lucky').textContent = lucky;
      document.getElementById('diag-danger').textContent = danger;
      document.getElementById('diag-gap').textContent = gap;

      // Update outcome badge in drawer
      Object.keys(questionOutcomes).forEach(idx => {{
        const outBadge = document.getElementById('outcome-badge-' + idx);
        if (!outBadge) return;
        const outcome = questionOutcomes[idx];
        if (outcome === 'mastered') {{
          outBadge.className = 'outcome-pill outcome-mastered';
          outBadge.textContent = '🏆 Tuntas (Mastered)';
        }} else if (outcome === 'lucky') {{
          outBadge.className = 'outcome-pill outcome-lucky';
          outBadge.textContent = '⚠️ Tebakan Beruntung (Review Ulang!)';
        }} else if (outcome === 'danger') {{
          outBadge.className = 'outcome-pill outcome-danger';
          outBadge.textContent = '🚨 Miskonsepsi Berbahaya (Prioritas Merah!)';
        }} else {{
          outBadge.className = 'outcome-pill outcome-gap';
          outBadge.textContent = '📖 Kesenjangan Pemahaman (Baca Materi)';
        }}
      }});
    }}

    // Override pickAnswer to integrate UWorld metrics
    const originalPickAnswer = window.pickAnswer;
    window.pickAnswer = function(qIdx, oIdx) {{
      if (userAns[qIdx] !== undefined) return; // prevent multiple clicks
      userAns[qIdx] = oIdx;
      if (!userConfidence[qIdx]) userConfidence[qIdx] = 'high';
      try {{ localStorage.setItem(QUIZ_KEY, JSON.stringify(userAns)); }} catch (e) {{}}
      syncQuizUI();
      calculateUWorldMetrics();
    }};

    // =========================================================================
    // FEATURE 5: CROSS-BLOCK JEMBATAN CONTROLLER
    // =========================================================================
    function switchBridge(paneId, btn) {{
      document.querySelectorAll('.bridge-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.bridge-tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(paneId).classList.add('active');
      btn.classList.add('active');
    }}

    function initCBT() {{
      const list = document.getElementById('cbt-list');
      if (!list) return;
      list.innerHTML = window.QUIZ_DATA.map((q, idx) => `
        <article class="q-module" id="qm-${{idx}}" data-cat="${{q.cat}}">
          <!-- UWorld Confidence selector bar -->
          <div class="confidence-bar">
            <span><b>Tingkat Keyakinan Sebelum Jawab:</b></span>
            <div class="conf-btn-group">
              <button type="button" class="conf-btn active-high" onclick="setConfidence(${{idx}}, 'high')">🎯 Yakin</button>
              <button type="button" class="conf-btn" onclick="setConfidence(${{idx}}, 'low')">🤔 Ragu-Ragu / Tebak</button>
            </div>
          </div>

          <div class="q-stem">${{q.stem}}</div>
          <div class="q-options">
            ${{q.opts.map((opt, oIdx) => `
              <button type="button" class="opt-row" id="opt-${{idx}}-${{oIdx}}" onclick="pickAnswer(${{idx}}, ${{oIdx}})">
                <span class="opt-key">${{String.fromCharCode(65 + oIdx)}}.</span>
                <span>${{opt}}</span>
              </button>
            `).join('')}}
          </div>
          <div class="q-drawer" id="qd-${{idx}}">
            <div id="outcome-badge-${{idx}}" class="outcome-pill outcome-mastered" style="display:inline-block;margin-bottom:10px;"></div>
            <div style="font-size:0.94rem;color:#263645;line-height:1.6;">${{q.exp}}</div>
            <div class="slide-dock">
              <img src="${{q.slide}}" alt="${{q.slideCap}}" class="dock-img" onclick="openZoom('${{q.slide}}', '${{q.slideCap}}')" />
              <div class="dock-foot"><span>${{q.slideCap}}</span><span>Zoom ↗</span></div>
            </div>
          </div>
        </article>
      `).join('');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      initCBT();
      syncQuizUI();
      calculateUWorldMetrics();
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(FINAL_HTML)

print(f"Modul EMN KUL 3 World-Class Edition berhasil dibuat: {OUT_HTML} (ukuran: {len(FINAL_HTML)} bytes)")
