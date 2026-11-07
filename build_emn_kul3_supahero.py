#!/usr/bin/env python3
"""Build Supahero Masterpiece Edition for Blok 9 EMN · KUL 3 Defisiensi Mineral (dr. Iwal Reza Ahdi, Sp.PD).
Menerapkan arsitektur penuh: Hero showcase, 7 Bento Chapters, Slide Docks, 8 Soal CBT, Cek Cepat H-1, Cmd+K."""
import os
import json

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

# Baca CSS dan JS dari build_supahero_edition.py agar 100% konsisten
with open(os.path.join(BASE_DIR, "build_supahero_edition.py"), "r", encoding="utf-8") as f:
    code = f.read()

# Extract SUPAHERO_CSS and SUPAHERO_JS
css_start = code.find('SUPAHERO_CSS = """') + len('SUPAHERO_CSS = """')
css_end = code.find('"""\n\nSUPAHERO_JS = """')
SUPAHERO_CSS = code[css_start:css_end]

js_start = code.find('SUPAHERO_JS = """') + len('SUPAHERO_JS = """')
js_end = code.find('"""\n\n# ==============================================================================')
SUPAHERO_JS = code[js_start:js_end]

EMN_KUL3_HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>VERTEX-PREP · EMN Kuliah 3: Defisiensi Mineral (Supahero Edition)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@600;700&family=Newsreader:opsz,wght@6..72,600;6..72,700&display=swap" rel="stylesheet">
  <style>
{SUPAHERO_CSS}
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
        <button type="button" class="supa-pill-btn" onclick="switchView('soal', this)">8 Soal Adaptif dr. Iwal</button>
        <button type="button" class="supa-pill-btn" onclick="switchView('flash', this)">Cek Cepat H-1 Ujian</button>
      </nav>

      <div class="supa-actions">
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
          <p class="hero-lead">Dari analisis 1.680 soal UAB, <strong>dr. Iwal Reza Ahdi, Sp.PD memiliki karakter 66.7% penalaran klinis & 45.8% kasus vignette</strong> (hanya 4% hafalan kata slide). Seluruh 32 slide mineral (Fe, Ca, Zn, Mg, I, K, Cu, P) telah dipadatkan menjadi <strong>7 Bab Bento Visual</strong> dengan fokus rantai sebab-akibat patofisiologi dan 3 kasus diskusi asli slide dosen.</p>

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
                <div class="tile-title">Ca, P, Mg, Na, K, Cl</div>
                <div class="tile-body">Dibutuhkan dalam gram/hari. Berperan dalam struktur tulang/gigi, transmisi potensial aksi saraf-otot, dan keseimbangan osmotik cairan tubuh.</div>
              </div>
              <div class="step-tile tone-emerald">
                <div class="tile-kicker">Mikromineral (Trace Elements)</div>
                <div class="tile-title">Fe, Zn, I, Se, Cu, Mn</div>
                <div class="tile-body">Dibutuhkan dalam miligram atau mikrogram/hari. Berperan vital sebagai kofaktor enzim metabolisme redoks, sintesis DNA, dan hormon tiroid.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">4 Jalur Mekanisme Defisiensi</div>
                <div class="tile-title">Asupan, Malabsorpsi, Kehilangan, Redistribusi</div>
                <div class="tile-body">
                  1. <b>Asupan Rendah:</b> Diet monoton, kemiskinan, anoreksia.<br>
                  2. <b>Malabsorpsi:</b> Penyakit celiac, bariatrik bypass lambung, IBD.<br>
                  3. <b>Kehilangan Berlebih:</b> Perdarahan haid/GI, diare kronik, diuretik.<br>
                  4. <b>Redistribusi / Regulasi:</b> Refeeding syndrome, lonjakan insulin, alkalosis.
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
                <div class="tile-title">Ferritin Turun (&lt;15–30 ng/mL) · Hb &amp; MCV Normal</div>
                <div class="tile-body">Cadangan besi di hati dan makrofag sumsum tulang habis. Eritropoiesis masih dipertahankan dari besi sirkulasi. <b>Pasien belum anemia</b>, namun sudah bisa mengeluh cepat lelah.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Stadium 2: Eritropoiesis Terbatas (Iron-Deficient Erythropoiesis)</div>
                <div class="tile-title">TSAT Anjlok (&lt;16–20%) · TIBC Meningkat</div>
                <div class="tile-body">Besi transport tidak mencukupi untuk kebutuhan sumsum tulang. Pembentukan eritrosit mulai terhambat. Hb mulai menurun di ambang batas.</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Stadium 3: Anemia Defisiensi Besi Nyata (IDA)</div>
                <div class="tile-title">Hb &lt;12 g/dL · MCV &lt;80 fL (Mikrositik Hipokromik)</div>
                <div class="tile-body">Bentuk lanjut: pucat, konjungtiva anemis, koilonychia (kuku sendok), atrofi papil lidah, dan <b>pagophagia (pica es batu)</b>.</div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">Pembaruan Pedoman AGA 2024 (Slide 11)</div>
              <div class="pearl-title">Mengapa Besi Oral Tidak Boleh Diberikan 3x Sehari?</div>
              <p>Setiap dosis besi oral diserap di duodenum, tubuh merespons dengan memproduksi hormon <b>Hepcidin</b> di hati. Hepcidin mengunci gerbang <i>ferroportin</i> selama 24–48 jam. Jika Anda memberi tablet besi 3x sehari, dosis ke-2 dan ke-3 tidak diserap dan hanya menimbulkan mual, kram, serta konstipasi parah. <b>Rekomendasi AGA 2024: Maksimal 1x/hari pagi saat perut kosong, atau rejimen selang-hari (alternate-day)!</b></p>
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
                <div class="tile-title">Dermatitis Periorifisial + Diare Kronik + Alopesia</div>
                <div class="tile-body">Ruam eritematosa bersisik berkrusta di sekitar lubang tubuh (mulut, hidung, mata, perineum) dan akral (jari tangan/kaki). Mirip penyakit herediter <i>Acrodermatitis enteropathica</i>.</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Gejala Penyerta Lainnya</div>
                <div class="tile-title">Luka Sulit Sembuh · Disgeusia · Retardasi Pertumbuhan</div>
                <div class="tile-body">Gangguan pengecapan (hipogeusia) dan penciuman karena zinc esensial untuk enzim <i>gustin</i> di papil lidah. Pada anak memicu stunting dan penurunan imunitas sel T.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Faktor Risiko Utama: Fitat</div>
                <div class="tile-title">Serealia Tak Beragi Mengikat Seng Secara Permanen</div>
                <div class="tile-body">Asam fitat pada gandum dan biji-bijian membentuk kompleks tak larut dengan seng di lumen usus, mencegah penyerapan. Rawan pada populasi diet tinggi sereal nabati tanpa protein hewani.</div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">UAB Trap Alert</div>
              <div class="pearl-title">Suplementasi Zinc pada Diare Anak</div>
              <p>WHO merekomendasikan Zinc 20 mg/hari selama 10–14 hari pada diare akut anak untuk meregenerasi mikrovili mukosa usus yang rusak dan menurunkan mortalitas diare hingga 23%.</p>
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
                <div class="tile-title">Parestesia · Chvostek (+) · Trousseau (+) · QT Panjang</div>
                <div class="tile-body">Kalsium ionisasi rendah meningkatkan permeabilitas natrium membran saraf, memicu hipereksitabilitas. Spasme karpopedal saat manset tensimeter dipompa (Trousseau) sangat sensitif. EKG: QT memanjang berisiko aritmia.</div>
              </div>
              <div class="step-tile tone-crimson">
                <div class="tile-kicker">Mekanisme Ginjal: Hubungan Mg dan K (Slide 17)</div>
                <div class="tile-title">Disfungsi Kanal ROMK Memicu Kebocoran Kalium Urin</div>
                <div class="tile-body">Di sel tubulus distal ginjal, Magnesium intrasel berfungsi sebagai <b>penghambat alami kanal ROMK</b>. Bila Mg serum anjlok, kanal ROMK terbuka lebar tanpa kontrol &rarr; Kalium terus menerus dibuang ke urin. Diberi Kalium oral/IV sebanyak apa pun, kalium akan langsung lolos terbuang. <b>Wajib koreksi Mg dulu!</b></div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Temuan EKG Hipokalemia (Slide 20)</div>
                <div class="tile-title">Gelombang T Mendatar · ST Depresi · Muncul Gelombang U</div>
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
                <div class="tile-kicker">Fase 3: Hipofosfatemia Berat (&lt;1.0 mg/dL)</div>
                <div class="tile-title">Kegagalan Sintesis ATP &rarr; Gagal Napas &amp; Kematian</div>
                <div class="tile-body">Tanpa fosfat ekstraseluler, sintesis ATP dan 2,3-DPG eritrosit lumpuh total. Otot diafragma gagal berkontraksi (takipnea lalu henti napas), otot jantung mengalami kardiomiopati akut dan aritmia fatal.</div>
              </div>
            </div>

            <div class="clinical-pearl-box">
              <div class="pearl-kicker">Protokol Pencegahan ASPEN / NICE (Slide 19)</div>
              <div class="pearl-title">Aturan Emas Memulai Nutrisi pada Pasien Malnutrisi Berat</div>
              <p>1. Berikan <b>Tiamin (B1) oral/IV sebelum nutrisi dimulai</b> untuk mencegah ensefalopati Wernicke.<br>
              2. Mulai kalori sangat rendah: <b>10–15 kkal/kg/hari</b>, naikkan bertahap dalam 4–7 hari.<br>
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
                <div class="tile-title">Anemia Mikrositik + Neutropenia + Mielopati</div>
                <div class="tile-body">Tembaga adalah komponen <i>ceruloplasmin</i> (ferroksidase untuk transportasi besi). Defisiensi Cu memicu anemia yang tidak membaik dengan besi, disertai neutropenia dan degenerasi kolumna dorsalis medula spinalis (mirip defisiensi B12). Pemicu klasik: <b>suplemen Zinc dosis tinggi atau perekat gigi palsu kaya zinc</b>!</div>
              </div>
              <div class="step-tile tone-amber">
                <div class="tile-kicker">Iodium (I) &amp; Perkembangan Saraf (Slide 13)</div>
                <div class="tile-title">Gondok Endemik pada Dewasa · Kretinisme pada Janin</div>
                <div class="tile-body">Iodium adalah bahan baku T3/T4. Defisiensi &rarr; umpan balik negatif berkurang &rarr; TSH hipofisis melonjak &rarr; hiperplasia folikel tiroid (struma/gondok). Bila terjadi pada ibu hamil, janin mengalami <b>kretinisme neurologis</b> (tuli-bisu, retardasi mental, perawakan pendek).</div>
              </div>
              <div class="step-tile tone-cobalt">
                <div class="tile-kicker">Selenium (Se) &amp; Penyakit Keshan (Slide 23)</div>
                <div class="tile-title">Antioksidan Selenoprotein · Kardiomiopati Endemik</div>
                <div class="tile-body">Selenium merupakan kofaktor enzim <i>Glutathione Peroxidase</i> dan <i>Deiodinase</i>. Defisiensi di daerah tanah miskin selenium (misal provinsi Keshan, Tiongkok) memicu <b>kardiomiopati kongestif fatal</b> terutama pada anak dan wanita muda.</div>
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
    <!-- VIEW 2: CBT SIMULATOR ADAPTIF GAYA DR. IWAL                         -->
    <!-- =================================================================== -->
    <div id="view-soal" class="view-section">
      <div class="cbt-header">
        <div>
          <h2>8 Soal Latihan Adaptif Karakter dr. Iwal Reza Ahdi, Sp.PD</h2>
          <p style="color:var(--ink-500);font-size:0.92rem;margin-top:4px;">Disusun berdasarkan profil 66.7% penalaran klinis &amp; perbandingan konsep mirip. Dilengkapi bukti slide asli.</p>
        </div>
        <div class="cbt-stat-card">
          <span class="cbt-stat-val" id="cbt-score">0 / 8</span>
          <span class="cbt-stat-lbl">Skor CBT Anda</span>
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
    <!-- VIEW 3: CEK CEPAT H-1 UJIAN (FLASH SUMMARY)                         -->
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

  <!-- MODAL ZOOM SLIDE -->
  <div id="zoom-modal" class="zoom-modal" onclick="closeZoom()">
    <div class="zoom-content" onclick="event.stopPropagation()">
      <div class="zoom-head">
        <h4 id="zoom-title" style="margin:0;font-size:1.1rem;color:white;">Bukti Slide Asli Dosen</h4>
        <button type="button" class="zoom-close" onclick="closeZoom()">✕</button>
      </div>
      <img id="zoom-img" src="" alt="Zoom Slide Asli" />
    </div>
  </div>

  <!-- COMMAND PALETTE MODAL (Cmd+K) -->
  <div id="cmdk-backdrop" class="cmdk-backdrop" onclick="closeSearchModal()">
    <div class="cmdk-modal" onclick="event.stopPropagation()">
      <div class="cmdk-input-wrap">
        <input type="text" id="cmdk-input" placeholder="Cari topik kuliah, slide, biomarker, atau kasus..." oninput="handleCmdkSearch(this.value)" />
        <button type="button" class="cmdk-esc" onclick="closeSearchModal()">ESC</button>
      </div>
      <div id="cmdk-results" class="cmdk-results"></div>
    </div>
  </div>

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

    {SUPAHERO_JS}

    function initCBT() {{
      const list = document.getElementById('cbt-list');
      if (!list) return;
      list.innerHTML = window.QUIZ_DATA.map((q, idx) => `
        <article class="q-module" id="qm-${{idx}}" data-cat="${{q.cat}}">
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
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(EMN_KUL3_HTML)

print(f"Masterpiece Supahero Edition berhasil dibangun di: {OUT_HTML} (ukuran: {len(EMN_KUL3_HTML)} bytes)")
