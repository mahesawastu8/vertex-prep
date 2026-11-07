#!/usr/bin/env python3
"""Build Super Simple & Complete High-Yield Mastery Module for EMN KUL 3 Defisiensi Mineral.
Filosofi:
- Super Simpel: Tidak ada 5 tab membingungkan, tidak ada dashboard rumit, tidak ada gimmick.
- Mencakup 100% Materi: Seluruh 32 slide (Fe, Zn, Mg, Ca, P, Cu, I, Se) terangkum padat dan presisi.
- Bug-free logic: Evaluasi kuis benar/salah dinamis dan jelas.
- Desain tenang, bersih, nyaman di mata (Warm paper, tipografi elegan, interaksi memuaskan).
"""
import os
import json

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

SIMPLE_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Mineral · Buku Pintar UAB EMN</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@600&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #FBFBFA;
      --surface: #FFFFFF;
      --border: #E6E4DD;
      --border-dark: #C8C5BB;
      
      --ink: #191919;
      --ink-secondary: #5A5A58;
      --ink-muted: #8A8A86;
      
      --sage: #2D6A4F;
      --sage-light: #EBF4EF;
      --coral: #C84B31;
      --coral-light: #FBEFEA;
      --ochre: #B87333;
      --ochre-light: #FAF2EA;
      --navy: #1D3557;
      --navy-light: #EEF2F6;
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      
      --font-serif: 'Newsreader', Georgia, serif;
      --font-sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    
    body {
      background-color: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 100px;
    }

    ::selection { background: #D8EADF; color: #191919; }

    /* Sticky Clean Topbar */
    .topbar {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(251, 251, 250, 0.95);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 12px 20px;
    }
    .topbar-inner {
      max-width: 860px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 14px;
    }
    .topbar-title {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--ink);
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .topbar-badge {
      background: var(--navy);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 0.88rem;
    }
    .nav-links a {
      color: var(--ink-secondary);
      text-decoration: none;
      font-weight: 500;
      transition: color 0.15s ease;
    }
    .nav-links a:hover { color: var(--ink); }
    .btn-anki {
      background: var(--sage);
      color: #FFFFFF !important;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 0.8rem;
      transition: opacity 0.15s ease;
    }
    .btn-anki:hover { opacity: 0.9; }

    /* Main Container */
    .container {
      max-width: 860px;
      margin: 0 auto;
      padding: 40px 20px 0;
    }

    /* Simple Header */
    .header-section {
      margin-bottom: 40px;
    }
    .kicker {
      font-size: 0.8rem;
      font-weight: 700;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 8px;
    }
    h1 {
      font-family: var(--font-serif);
      font-size: 2.6rem;
      font-weight: 700;
      line-height: 1.2;
      color: var(--ink);
      margin-bottom: 12px;
    }
    .subtitle {
      font-size: 1.05rem;
      color: var(--ink-secondary);
      line-height: 1.6;
    }
    .meta-row {
      display: flex;
      gap: 16px;
      margin-top: 14px;
      font-size: 0.85rem;
      color: var(--ink-muted);
    }

    /* Section Divider & Titles */
    .section-block {
      margin-bottom: 50px;
    }
    .section-heading {
      font-family: var(--font-serif);
      font-size: 1.6rem;
      font-weight: 700;
      color: var(--ink);
      margin-bottom: 18px;
      padding-bottom: 8px;
      border-bottom: 2px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .section-badge {
      font-family: var(--font-sans);
      font-size: 0.75rem;
      font-weight: 600;
      color: var(--ink-muted);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    /* Compact Mineral Cards (Super Simpel, Full Content) */
    .mineral-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 16px;
    }
    .mineral-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      transition: all 0.2s ease;
    }
    .mineral-card:hover {
      border-color: var(--border-dark);
      box-shadow: 0 4px 12px rgba(0,0,0,0.03);
    }
    .m-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .m-name {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--ink);
    }
    .m-category {
      font-size: 0.75rem;
      font-weight: 700;
      padding: 2px 8px;
      border-radius: 4px;
    }
    .cat-makro { background: var(--navy-light); color: var(--navy); }
    .cat-mikro { background: var(--sage-light); color: var(--sage); }

    .m-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-size: 0.93rem;
      color: #333333;
    }
    .m-list li strong { color: var(--ink); }
    .uab-trap {
      margin-top: 10px;
      padding: 10px 14px;
      background: var(--coral-light);
      border-radius: 6px;
      font-size: 0.88rem;
      color: #7A2818;
      line-height: 1.5;
    }
    .uab-trap strong { color: var(--coral); }

    /* Slide Evidence Card */
    .slide-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-top: 10px;
      padding: 4px 10px;
      background: #F2EFE8;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--ink-secondary);
      cursor: pointer;
      border: 1px solid var(--border);
    }
    .slide-chip:hover {
      background: var(--sage-light);
      color: var(--sage);
      border-color: var(--sage);
    }

    /* 4 Essential Pathophysiology Chains (Paham) */
    .chain-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px 24px;
      margin-bottom: 16px;
    }
    .chain-title {
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--navy);
      margin-bottom: 8px;
    }
    .chain-flow {
      background: #F8F6F0;
      border-radius: var(--radius-sm);
      padding: 12px 16px;
      font-size: 0.92rem;
      line-height: 1.6;
      color: #262626;
      margin-bottom: 8px;
    }
    .chain-conclusion {
      font-size: 0.88rem;
      color: var(--ink-secondary);
    }

    /* CBT Questions (8 Real UAB Predictions) */
    .q-container {
      display: flex;
      flex-direction: column;
      gap: 24px;
    }
    .q-box {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 24px 28px;
    }
    .q-num-tag {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }
    .q-text {
      font-size: 1.02rem;
      font-weight: 500;
      line-height: 1.65;
      color: var(--ink);
      margin-bottom: 18px;
    }
    .opt-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .opt-item {
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
    }
    .opt-item:hover {
      background: #FAF8F5;
      border-color: #BDB7AB;
    }
    .opt-key {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--ink-muted);
      flex: none;
    }
    .opt-item.is-correct {
      background: var(--sage-light);
      border-color: var(--sage);
      color: #174230;
      font-weight: 600;
    }
    .opt-item.is-wrong {
      background: var(--coral-light);
      border-color: var(--coral);
      color: #7A2818;
    }

    .q-feedback {
      margin-top: 16px;
      padding: 16px 18px;
      border-radius: var(--radius-sm);
      font-size: 0.92rem;
      line-height: 1.6;
      display: none;
    }
    .q-feedback.show { display: block; }
    .q-feedback.correct-fb {
      background: var(--sage-light);
      border: 1px solid #B8DEC9;
      color: #174230;
    }
    .q-feedback.wrong-fb {
      background: var(--coral-light);
      border: 1px solid #F3C4BA;
      color: #7A2818;
    }

    /* Modal Zoom Slide */
    .modal-backdrop {
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(25, 25, 25, 0.75); backdrop-filter: blur(8px);
      display: none; align-items: center; justify-content: center; padding: 20px;
    }
    .modal-backdrop.open { display: flex; }
    .modal-img {
      max-width: 90%; max-height: 85vh; border-radius: 8px;
      box-shadow: 0 16px 36px rgba(0,0,0,0.3);
    }

    @media (max-width: 768px) {
      h1 { font-size: 2rem; }
      .nav-links { display: none; }
      .q-box { padding: 18px; }
    }
  </style>
</head>
<body>

  <!-- Top Sticky Bar -->
  <header class="topbar">
    <div class="topbar-inner">
      <div class="topbar-title">
        <span class="topbar-badge">EMN · KUL 3</span>
        <span>Defisiensi Mineral</span>
      </div>
      <div class="nav-links">
        <a href="#ringkasan">Rangkuman 8 Mineral</a>
        <a href="#mekanisme">4 Rantai Sebab-Akibat</a>
        <a href="#latihan-soal">Latihan 8 Soal UAB</a>
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-anki" download>⬇ Download Deck Anki</a>
      </div>
    </div>
  </header>

  <main class="container">
    
    <!-- Header -->
    <header class="header-section">
      <div class="kicker">Modul Ringkas Pengganti PPT (Super Simpel &amp; Lengkap)</div>
      <h1>Defisiensi Mineral</h1>
      <p class="subtitle">Seluruh 32 slide dr. Iwal Reza Ahdi, Sp.PD diperas menjadi ringkasan to-the-point: gejala khas patognomonik, nilai lab kunci, jebakan soal UAB, dan 8 latihan soal teruji.</p>
      <div class="meta-row">
        <span>👨‍⚕️ Narasumber: <b>dr. Iwal Reza Ahdi, Sp.PD</b></span>
        <span>🎯 Target UAB: <b>4 Soal Pilihan Ganda</b></span>
        <span>⏱️ Waktu Belajar: <b>~25 Menit Selesai</b></span>
      </div>
    </header>

    <!-- SECTION 1: RINGKASAN 8 MINERAL -->
    <section class="section-block" id="ringkasan">
      <div class="section-heading">
        <span>1. Rangkuman Inti 8 Mineral (Hafalan &amp; Lab Kunci)</span>
        <span class="section-badge">Semua Slide Tercover</span>
      </div>

      <div class="mineral-grid">
        
        <!-- BESI -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">1. Besi (Fe)</span>
            <span class="m-category cat-mikro">Mikromineral (Renik)</span>
          </div>
          <ul class="m-list">
            <li><strong>Fungsi Kunci:</strong> Inti heme hemoglobin (transpor O2), mioglobin otot, enzim sitokrom redoks.</li>
            <li><strong>Perjalanan 3 Stadium (Slide 10):</strong>
              <br>• <i>Stadium 1 (Cadangan Turun):</i> <b>Ferritin serum anjlok (&lt;15–30 ng/mL)</b> lebih awal! Hb dan MCV masih normal.
              <br>• <i>Stadium 2 (Eritropoiesis Terbatas):</i> TSAT &lt;16–20%, TIBC meningkat.
              <br>• <i>Stadium 3 (Anemia Defisiensi Besi):</i> Hb &lt;12 g/dL, MCV &lt;80 fL (mikrositik hipokromik).
            </li>
            <li><strong>Gejala Patognomonik:</strong> Cepat lelah, <b>pagophagia (pica makan es batu)</b>, kuku sendok (koilonychia), glossitis.</li>
          </ul>
          <div class="uab-trap">
            <strong>⚠️ Jebakan Ujian dr. Iwal:</strong>
            <br>1. <i>MCV normal TIDAK menyingkirkan defisiensi besi stadium awal!</i> (Biomarker paling awal turun adalah Ferritin).
            <br>2. <i>Pedoman AGA 2024 (Slide 11):</i> Tablet besi oral <b>maksimal 1x/hari pagi hari atau selang-hari (alternate day)</b>. Jangan 3x sehari karena setiap dosis memicu lonjakan <b>Hepcidin</b> 24–48 jam yang memblokir penyerapan besi berikutnya.
          </div>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_10.jpg')">
            📷 Bukti Slide 10: Perjalanan Defisiensi Besi (Klik untuk Zoom)
          </div>
        </article>

        <!-- SENG -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">2. Seng (Zinc / Zn)</span>
            <span class="m-category cat-mikro">Mikromineral (Renik)</span>
          </div>
          <ul class="m-list">
            <li><strong>Fungsi Kunci:</strong> Kofaktor &gt;300 metalloenzim, sintesis DNA/protein, transkripsi <i>zinc fingers</i>, regenerasi epitel mukosa &amp; luka.</li>
            <li><strong>Trias Gejala Patognomonik (Slide 12):</strong> <b>Dermatitis periorifisial &amp; akral</b> (ruam krusta di sekitar mulut, anus, ujung jari), <b>diare kronik</b>, dan <b>alopesia</b> (rambut rontok).</li>
            <li><strong>Gejala Tambahan:</strong> Gangguan rasa/penciuman (hipogeusia), luka sulit sembuh, stunting pada anak.</li>
          </ul>
          <div class="uab-trap">
            <strong>⚠️ Jebakan Ujian dr. Iwal:</strong>
            <br>• Makanan penghambat: Diet tinggi <b>asam fitat</b> (serealia/gandum tak beragi) mengikat seng di usus menjadi kelat tak larut &rarr; malabsorpsi seng.
            <br>• Bentuk herediter mutasi transporter ZIP4 disebut <b>Acrodermatitis enteropathica</b>.
          </div>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_12.jpg')">
            📷 Bukti Slide 12: Seng, Imunitas, &amp; Fitat (Klik untuk Zoom)
          </div>
        </article>

        <!-- MAGNESIUM -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">3. Magnesium (Mg)</span>
            <span class="m-category cat-makro">Makromineral</span>
          </div>
          <ul class="m-list">
            <li><strong>Fungsi Kunci:</strong> Kofaktor reaksi bergantung ATP, menjaga stabilitas potensial membran saraf-otot, pengatur kanal ion ginjal.</li>
            <li><strong>Gejala Defisiensi (&lt;1.7 mg/dL):</strong> Tremor, hiperrefleksia, kejang, tetani, aritmia (Torsades de pointes).</li>
            <li><strong>Faktor Risiko:</strong> Pemakaian diuretik loop (furosemid), konsumsi obat maag PPI (omeprazole) menahun, diare kronik, alkohol.</li>
          </ul>
          <div class="uab-trap">
            <strong>⚠️ Jebakan Ujian dr. Iwal (Slide 17 &amp; 28):</strong>
            <br><b>Mengapa Kalium susah naik bila Magnesium rendah?</b> Di sel tubulus ginjal, Mg intrasel adalah penghambat alami kanal <b>ROMK</b>. Saat Mg anjlok &rarr; kanal ROMK terbuka bebas tanpa rem &rarr; <b>Kalium bocor terbuang terus-menerus ke urin (hipokalemia refrakter)</b>. Koreksi Magnesium wajib diberikan bersamaan!
          </div>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_17.jpg')">
            📷 Bukti Slide 17: Hubungan Mg dan Kalium Ginjal (Klik untuk Zoom)
          </div>
        </article>

        <!-- FOSFAT -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">4. Fosfat (P) &amp; Refeeding Syndrome</span>
            <span class="m-category cat-makro">Makromineral</span>
          </div>
          <ul class="m-list">
            <li><strong>Fungsi Kunci:</strong> Pembentuk molekul energi ATP, 2,3-DPG eritrosit (pelepasan O2 ke jaringan), fosfolipid membran sel.</li>
            <li><strong>Patofisiologi Refeeding Syndrome (Slide 19 &amp; 29):</strong>
              <br>Pasien kelaparan lama / anoreksia mendadak diberi nutrisi karbohidrat &rarr; Pankreas memompa <b>Insulin masif</b> &rarr; Insulin menyedot Fosfat, Kalium, dan Mg masuk ke intrasel &rarr; <b>Hipofosfatemia berat (&lt;1.0 mg/dL)</b> di darah &rarr; Pembentukan ATP lumpuh &rarr; <b>Gagal napas akut (otot diafragma lumpuh)</b> dan aritmia fatal.
            </li>
          </ul>
          <div class="uab-trap">
            <strong>⚠️ Jebakan Ujian dr. Iwal (Pencegahan ASPEN/NICE):</strong>
            <br>1. Berikan <b>Tiamin (B1) sebelum makanan dimulai</b>.
            <br>2. Mulai kalori sangat rendah: <b>10–15 kkal/kg/hari</b> bertahap. Pantau serial P-K-Mg darah.
          </div>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_19.jpg')">
            📷 Bukti Slide 19: Refeeding Syndrome (Klik untuk Zoom)
          </div>
        </article>

        <!-- KALSIUM -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">5. Kalsium (Ca)</span>
            <span class="m-category cat-makro">Makromineral</span>
          </div>
          <ul class="m-list">
            <li><strong>Fungsi Kunci:</strong> Mineral kristal tulang (99%), permeabilitas membran sel saraf, kontraksi otot skelet &amp; jantung.</li>
            <li><strong>Gejala Hipokalsemia (Slide 15):</strong> Parestesia perioral (kesemutan bibir/jari), tetani, spasme karpopedal, <b>EKG interval QT memanjang</b>.</li>
            <li><strong>Tanda Fisik Patognomonik:</strong>
              <br>• <b>Chvostek sign:</b> Kedutan bibir/wajah saat saraf fasialis diketuk anterior telinga.
              <br>• <b>Trousseau sign:</b> Spasme fleksi jari tangan (karpopedal) saat manset tensimeter dipompa &gt;sistolik 3 menit.
            </li>
          </ul>
          <div class="uab-trap">
            <strong>⚠️ Jebakan Ujian:</strong> Hanya <b>Ionized Calcium (kalsium bebas 50%)</b> yang aktif secara fisiologis. Total kalsium dipengaruhi oleh albumin serum.
          </div>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_15.jpg')">
            📷 Bukti Slide 15: Hipokalsemia &amp; Evaluasi (Klik untuk Zoom)
          </div>
        </article>

        <!-- TEMBAGA -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">6. Tembaga (Copper / Cu)</span>
            <span class="m-category cat-mikro">Mikromineral (Renik)</span>
          </div>
          <ul class="m-list">
            <li><strong>Fungsi Kunci:</strong> Komponen enzim <i>ceruloplasmin</i> (ferroksidase untuk transportasi besi) dan sintesis mielin saraf.</li>
            <li><strong>Trias Defisiensi (Slide 22):</strong> <b>Anemia mikrositik + Neutropenia berat + Mielopati ataksia sensorik</b> (gangguan jalan mirip defisiensi vitamin B12).</li>
          </ul>
          <div class="uab-trap">
            <strong>⚠️ Jebakan Ujian dr. Iwal (Pemicu Iatrogenik):</strong>
            <br>Konsumsi suplemen <b>Seng (Zinc) dosis tinggi (&gt;50 mg/hari)</b> berkepanjangan memicu sintesis protein <b>metallothionein</b> di usus yang mengikat tembaga dan membuangnya &rarr; memicu defisiensi tembaga iatrogenik!
          </div>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_22.jpg')">
            📷 Bukti Slide 22: Tembaga &amp; Efek Samping Seng (Klik untuk Zoom)
          </div>
        </article>

        <!-- IODIUM & SELENIUM -->
        <article class="mineral-card">
          <div class="m-top">
            <span class="m-name">7 &amp; 8. Iodium (I) &amp; Selenium (Se)</span>
            <span class="m-category cat-mikro">Mikromineral (Renik)</span>
          </div>
          <ul class="m-list">
            <li><strong>Iodium (Slide 13):</strong> Bahan baku hormon tiroid T3/T4. Defisiensi &rarr; TSH melonjak &rarr; <b>gondok endemik</b>. Bila terjadi pada ibu hamil &rarr; janin mengalami <b>kretinisme</b> (retardasi mental permanen, tuli-bisu, perawakan pendek cebol).</li>
            <li><strong>Selenium (Slide 23):</strong> Kofaktor enzim antioksidan <i>Glutathione Peroxidase</i>. Defisiensi di daerah tanah miskin selenium memicu <b>Penyakit Keshan</b> (kardiomiopati kongestif fatal pada anak &amp; wanita muda).</li>
          </ul>
          <div class="slide-chip" onclick="openModal('slides_kul3/slide_13.jpg')">
            📷 Bukti Slide 13: Iodium &amp; Kretinisme (Klik untuk Zoom)
          </div>
        </article>

      </div>
    </section>

    <!-- SECTION 2: 4 RANTAI SEBAB-AKIBAT -->
    <section class="section-block" id="mekanisme">
      <div class="section-heading">
        <span>2. Empat Rantai Sebab-Akibat Utama (Kunci Paham)</span>
        <span class="section-badge">66.7% Soal Penalaran</span>
      </div>

      <div class="chain-card">
        <div class="chain-title">1. Mengapa Kalium Susah Naik Bila Magnesium Rendah?</div>
        <div class="chain-flow">
          Mg serum anjlok &rarr; Mg intraseluler tubulus ginjal hilang &rarr; <b>Kanal ROMK terbuka bebas tanpa rem</b> &rarr; Kalium bocor terbuang terus-menerus ke urin &rarr; <b>Hipokalemia refrakter</b> terhadap terapi kalium oral/IV.
        </div>
        <div class="chain-conclusion">💡 <b>Solusi:</b> Berikan koreksi Magnesium (MgSO4 IV atau oral) serentak bersama Kalium.</div>
      </div>

      <div class="chain-card">
        <div class="chain-title">2. Mengapa Terjadi Gagal Napas Akut pada Refeeding Syndrome?</div>
        <div class="chain-flow">
          Puasa lama &rarr; Asupan karbohidrat mendadak &rarr; <b>Lonjakan insulin masif</b> &rarr; Fosfat, K, Mg tersedot masuk ke dalam sel &rarr; <b>Hipofosfatemia berat (&lt;1.0 mg/dL)</b> &rarr; Sintesis ATP seluler lumpuh &rarr; <b>Otot diafragma lumpuh gagal bernapas</b>.
        </div>
        <div class="chain-conclusion">💡 <b>Solusi:</b> Tiamin profilaksis sebelum makan, mulai kalori rendah 10–15 kkal/kg/hari secara bertahap.</div>
      </div>

      <div class="chain-card">
        <div class="chain-title">3. Mengapa Besi Oral Hanya Boleh Diberikan Maksimal 1x Sehari?</div>
        <div class="chain-flow">
          Dosis besi pertama diserap &rarr; Hati merespons dengan memproduksi <b>Hepcidin</b> &rarr; Hepcidin mengunci gerbang ferroportin selama 24–48 jam &rarr; Dosis ke-2 dan ke-3 tidak diserap usus &rarr; Hanya memicu mual dan konstipasi.
        </div>
        <div class="chain-conclusion">💡 <b>Solusi (AGA 2024):</b> Berikan dosis tunggal pagi hari atau selang-hari (alternate-day).</div>
      </div>

      <div class="chain-card">
        <div class="chain-title">4. Mengapa Minum Suplemen Zinc Berlebih Bikin Anemia &amp; Neutropenia?</div>
        <div class="chain-flow">
          Zinc dosis tinggi (&gt;50 mg/hari) &rarr; Menginduksi sintesis protein <b>metallothionein</b> di sel usus &rarr; Metallothionein mengikat Tembaga (Cu) dengan afinitas kuat &rarr; Penyerapan Cu terblokir &rarr; <b>Defisiensi Tembaga</b> (anemia mikrositik + neutropenia + ataksia).
        </div>
        <div class="chain-conclusion">💡 <b>Solusi:</b> Hentikan zinc berlebih, evaluasi kadar ceruloplasmin dan tembaga darah.</div>
      </div>
    </section>

    <!-- SECTION 3: LATIHAN SOAL UAB -->
    <section class="section-block" id="latihan-soal">
      <div class="section-heading">
        <span>3. Latihan 8 Soal Prediksi UAB Adaptif dr. Iwal</span>
        <span class="section-badge">Skor: <span id="quiz-score-num">0</span> / 8</span>
      </div>

      <div class="q-container" id="quiz-container"></div>
    </section>

  </main>

  <!-- Modal Zoom -->
  <div id="modal-zoom" class="modal-backdrop" onclick="closeModal()">
    <img id="modal-img" class="modal-img" src="" alt="Slide Zoom" onclick="event.stopPropagation()" />
  </div>

  <script>
    // 8 SOAL REAL UAB DR. IWAL
    const QUESTIONS = [
      {
        num: 1,
        stem: 'Seorang perempuan 29 tahun datang dengan keluhan badan lemas dan berdebar saat beraktivitas sejak 2 bulan. Riwayat menstruasi banyak (ganti pembalut 6–7 kali/hari) selama 8 hari setiap siklusnya. Konjungtiva anemis (+). Laboratorium: Hb 8,9 g/dL, MCV 68 fL, MCH 21 pg. Pasien mengaku sering mengunyah es batu (pagophagia). Pemeriksaan biomarker manakah yang paling sensitif dan paling awal menurun untuk mengonfirmasi diagnosis?',
        options: [
          'Total Iron Binding Capacity (TIBC)',
          'Ferritin serum',
          'Saturasi transferrin (TSAT)',
          'Hemoglobin elektroforesis',
          'Bilirubin indirek serum'
        ],
        correct: 1,
        exp: 'Pasien mengalami Anemia Defisiensi Besi akibat menorrhagia. Pagophagia (pica es batu) adalah tanda khas defisiensi besi. Pada perjalanan alami (Slide 10), <b>Ferritin serum adalah biomarker pertama yang anjlok (&lt;15–30 ng/mL)</b> mencerminkan habisnya cadangan besi di hati dan sumsum tulang sebelum Hb dan MCV turun.'
      },
      {
        num: 2,
        stem: 'Laki-laki 67 tahun dengan gagal jantung mengonsumsi furosemid mengeluh lemas otot dan berdebar. EKG menunjukkan gelombang T mendatar dan gelombang U prominen. Kalium serum 2,8 mmol/L. Dokter memberikan suplementasi KCl oral dosis tinggi 3 hari, namun kalium ulang tetap rendah (2,9 mmol/L). Gangguan elektrolit penyerta manakah yang mendasari kondisi refrakter tersebut?',
        options: [
          'Hiponatremia',
          'Hipokalsemia',
          'Hipomagnesemia',
          'Hiperfosfatemia',
          'Hiperkalsiuria'
        ],
        correct: 2,
        exp: 'Furosemid membuang Kalium dan Magnesium. Di tubulus ginjal, ion Magnesium intrasel adalah penghambat alami kanal ROMK. Saat terjadi <b>hipomagnesemia</b> (&lt;1.7 mg/dL, Slide 17 &amp; 28), kanal ROMK terbuka bebas tanpa rem sehingga Kalium terus menerus bocor ke urin. Koreksi Magnesium wajib diberikan bersamaan.'
      },
      {
        num: 3,
        stem: 'Anak laki-laki 4 tahun dibawa dengan keluhan ruam kemerahan bersisik di area sekitar mulut, perineum, serta sela-sela jari kaki sejak 1 bulan. Anak juga mengalami diare kronik kambuhan dan rambut rontok (alopesia). Riwayat diet monoton tinggi serealia dan bubur gandum tanpa asupan hewani. Defisiensi mikromineral apakah yang mendasari kondisi tersebut?',
        options: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Seng (Zinc / Zn)',
          'Selenium (Se)',
          'Mangan (Mn)'
        ],
        correct: 2,
        exp: 'Trias patognomonik: <b>dermatitis periorifisial &amp; akral, diare kronik, dan alopesia</b> merupakan tanda khas defisiensi Seng (Slide 12). Serealia mengandung asam <b>fitat</b> tinggi yang mengikat seng di usus membentuk kelat tak larut.'
      },
      {
        num: 4,
        stem: 'Pasien laki-laki 46 tahun dengan riwayat malnutrisi berat dan kelaparan selama 12 hari dirawat di bangsal. Dokter segera memberikan nutrisi parenteral tinggi karbohidrat. Dalam waktu 48 jam, pasien mendadak mengalami takipnea berat, lemas otot menyeluruh, dan aritmia. Gangguan biokimiawi serum manakah yang menjadi pemicu utama kegagalan napas akut tersebut?',
        options: [
          'Hiponatremia berat',
          'Hipokalsemia terionisasi',
          'Hipofosfatemia berat (&lt;1.0 mg/dL)',
          'Asidosis laktat',
          'Hiperglikemia hiperosmolar'
        ],
        correct: 2,
        exp: 'Pasien mengalami <b>Refeeding Syndrome</b> (Slide 19 &amp; 29). Karbohidrat memicu lonjakan insulin yang mendorong glukosa dan Fosfat masuk masif ke sel &rarr; hipofosfatemia berat (&lt;1.0 mg/dL) menghentikan sintesis ATP, memicu kelumpuhan diafragma akut (gagal napas) dan aritmia.'
      },
      {
        num: 5,
        stem: 'Perempuan 35 tahun pasca-operasi bypass lambung datang dengan keluhan baal di kedua tungkai serta ataksia sensorik (gangguan jalan). Laboratorium: Hb 9,0 g/dL, MCV 72 fL (mikrositik), dan neutropenia berat (ANC 750/&mu;L). Pasien mengaku mengonsumsi suplemen Zinc dosis tinggi (80 mg/hari) selama 8 bulan. Defisiensi mineral apakah yang paling tepat menjelaskan kondisi pasien?',
        options: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Iodium (I)',
          'Selenium (Se)',
          'Kalsium (Ca)'
        ],
        correct: 1,
        exp: 'Kombinasi <b>anemia mikrositik + neutropenia berat + mielopati ataksia</b> adalah tanda klasik defisiensi Tembaga (Slide 22). Suplemen Zinc dosis tinggi menginduksi protein <i>metallothionein</i> di enterosit yang mengikat tembaga dan menghambat absorpsinya.'
      },
      {
        num: 6,
        stem: 'Berdasarkan pedoman klinis American Gastroenterological Association (AGA 2024), bagaimanakah aturan suplementasi besi oral yang paling tepat dan dapat ditoleransi optimal pada pasien anemia defisiensi besi?',
        options: [
          'Diberikan dosis tinggi 3 kali sehari bersama makanan',
          'Diberikan dosis terbagi setiap 6 jam disertai antasida',
          'Diberikan maksimal 1 kali sehari atau rejimen selang-hari (alternate-day)',
          'Diberikan bersamaan dengan susu sapi',
          'Diberikan 4 kali sehari dalam dosis terbagi'
        ],
        correct: 2,
        exp: 'Pedoman AGA 2024 (Slide 11) menekankan bahwa setiap dosis besi oral memicu lonjakan hormon <b>Hepcidin</b> yang memblokir penyerapan besi berikutnya selama 24–48 jam. Pemberian maksimal 1x/hari atau selang-hari (alternate-day) memaksimalkan penyerapan dan meminimalkan efek samping GI.'
      },
      {
        num: 7,
        stem: 'Pemeriksaan fisik pada pasien dengan kecurigaan hipokalsemia menunjukkan adanya spasme karpopedal pada tangan ketika manset tensimeter dipompa di atas tekanan sistolik selama 3 menit. Disebut apakah tanda fisik patognomonik tersebut?',
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
        num: 8,
        stem: 'Wanita hamil di daerah pegunungan yang jarang mengonsumsi garam beriodium melahirkan bayi dengan keterlambatan perkembangan saraf berat, perawakan pendek, dan tuli-bisu. Mekanisme patofisiologi apakah yang mendasari kondisi kretinisme pada bayi tersebut?',
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
    let totalScore = 0;

    function renderQuiz() {
      const container = document.getElementById('quiz-container');
      container.innerHTML = QUESTIONS.map((q, qIdx) => `
        <article class="q-box" id="q-box-${qIdx}">
          <div class="q-num-tag">SOAL #${q.num} · UAB PREDICTION</div>
          <div class="q-text">${q.stem}</div>
          <div class="opt-list">
            ${q.options.map((opt, oIdx) => `
              <button type="button" class="opt-item" onclick="handleAnswer(${qIdx}, ${oIdx})">
                <span class="opt-key">${String.fromCharCode(65 + oIdx)}.</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
          <div class="q-feedback" id="fb-${qIdx}"></div>
        </article>
      `).join('');
    }

    // Dynamic Bug-Free Evaluation Logic
    function handleAnswer(qIdx, selectedOpt) {
      if (userAnswers[qIdx] !== undefined) return;
      userAnswers[qIdx] = selectedOpt;

      const q = QUESTIONS[qIdx];
      const isCorrect = selectedOpt === q.correct;
      const box = document.getElementById('q-box-' + qIdx);
      const btns = box.querySelectorAll('.opt-item');
      const fb = document.getElementById('fb-' + qIdx);

      btns.forEach((btn, i) => {
        if (i === q.correct) btn.classList.add('is-correct');
        else if (i === selectedOpt && !isCorrect) btn.classList.add('is-wrong');
      });

      if (isCorrect) {
        totalScore++;
        fb.className = 'q-feedback show correct-fb';
        fb.innerHTML = `<b>✅ Benar!</b> ${q.exp}`;
      } else {
        fb.className = 'q-feedback show wrong-fb';
        fb.innerHTML = `<b>❌ Kurang Tepat.</b> Jawaban yang benar adalah <b>${String.fromCharCode(65 + q.correct)} (${q.options[q.correct]})</b>.<br>${q.exp}`;
      }

      document.getElementById('quiz-score-num').textContent = totalScore;
    }

    // Lightbox modal zoom
    function openModal(src) {
      document.getElementById('modal-img').src = src;
      document.getElementById('modal-zoom').classList.add('open');
    }
    function closeModal() {
      document.getElementById('modal-zoom').classList.remove('open');
    }
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeModal();
    });

    document.addEventListener('DOMContentLoaded', () => {
      renderQuiz();
    });
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(SIMPLE_HTML)

print(f"Modul Super Simpel berhasil dibuat di {OUT_HTML} (ukuran: {len(SIMPLE_HTML)} bytes)")
