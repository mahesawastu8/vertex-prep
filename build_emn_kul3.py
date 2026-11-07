#!/usr/bin/env python3
"""Build Supahero 4-Layer Inverted Mastery Module for Blok 9 EMN · KUL 3 Defisiensi Mineral (IWL)
dan export Anki .apkg deck menggunakan genanki."""
import json
import os
import genanki

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
ANKI_DIR = os.path.join(BASE_DIR, "anki")
os.makedirs(ANKI_DIR, exist_ok=True)

# 1. GENERATE ANKI DECK (.apkg)
model = genanki.Model(
    1607392400,
    'VERTEX-PREP Clinical Slide-Verified Model (EMN KUL 3)',
    fields=[{'name': 'Question'}, {'name': 'Answer'}, {'name': 'SlideProof'}],
    templates=[{
        'name': 'Card 1',
        'qfmt': '<div style="font-family:IBM Plex Sans,sans-serif;font-size:16px;color:#0B131A;padding:12px;"><b>{{Question}}</b></div>',
        'afmt': '{{FrontSide}}<hr id="answer"><div style="font-family:IBM Plex Sans,sans-serif;font-size:15px;color:#0B6350;padding:12px;">{{Answer}}</div><div style="font-size:12px;color:#667A8A;padding:6px 12px;">Bukti: {{SlideProof}}</div>',
    }],
    css='.card { background-color: #F3F5F8; text-align: left; }'
)

deck = genanki.Deck(2059400200, 'VERTEX-PREP :: Blok 9 (EMN) :: KUL 3 Defisiensi Mineral (dr. Iwal Reza, Sp.PD)')

cards_data = [
    ("Apa biomarker paling dini dan sensitif yang turun pada defisiensi besi sebelum Hb dan MCV abnormal?",
     "<b>Ferritin serum</b> (cadangan Fe habis lebih dahulu; Hb dan MCV masih normal pada stadium awal).",
     "Slide 10: Perjalanan Defisiensi Besi"),
    ("Mengapa hipokalemia refrakter (sulit naik) bila kadar magnesium juga rendah?",
     "Karena defisiensi <b>Magnesium (Mg)</b> menyebabkan disfungsi kanal ginjal (ROMK) sehingga <b>ekskresi Kalium lewat urin meningkat masif</b>. Koreksi Mg wajib bersamaan.",
     "Slide 17 & 28: Mengapa Kalium Sulit Naik Bila Mg Rendah"),
    ("Trias manifestasi klinis khas apa yang menandakan defisiensi Seng (Zinc)?",
     "<b>Dermatitis periorifisial / akral</b> (Acrodermatitis enteropathica), <b>diare kronik</b>, dan <b>alopesia</b>, disertai gangguan penyembuhan luka.",
     "Slide 12: Seng (Zn) — Pertumbuhan, Kulit, Imunitas"),
    ("Apa patofisiologi utama Refeeding Syndrome pada pasien malnutrisi berat yang baru diberi nutrisi tinggi karbohidrat?",
     "Lonjakan <b>Insulin</b> mendadak memicu perpindahan masif <b>Fosfat, Kalium, dan Magnesium</b> ke intrasel &rarr; <b>Hipofosfatemia berat (&lt;1 mg/dL)</b> &rarr; krisis ATP, aritmia, dan gagal napas.",
     "Slide 19 & 29: Refeeding Syndrome"),
    ("Pasien wanita dengan anemia mikrositik hipokromik yang memiliki kebiasaan makan es batu (pagophagia) mengindikasikan defisiensi apa?",
     "<b>Defisiensi Besi (Fe)</b>. Pagophagia adalah bentuk pica spesifik untuk anemia defisiensi besi.",
     "Slide 3, 9, 27: Kasus Pagophagia & Anemia Besi"),
    ("Pemberian suplemen Seng (Zinc) dosis tinggi berkepanjangan dapat memicu defisiensi mineral apa secara iatrogenik?",
     "<b>Defisiensi Tembaga (Cu)</b> (karena Zn menstimulasi metallothionein di enterosit yang mengikat tembaga dan memblokir absorpsinya).",
     "Slide 22: Tembaga (Cu) — Darah & Saraf"),
    ("Mengapa pedoman AGA 2024 menganjurkan pemberian besi oral maksimal 1x sehari atau selang hari?",
     "Untuk menghindari lonjakan <b>Hepcidin</b> berulang yang memblokade absorpsi dosis besi berikutnya selama 24–48 jam.",
     "Slide 11: Terapi Fe — AGA Clinical Practice Update"),
    ("Temuan EKG khas apa yang terlihat pada hipokalsemia dan hipokalemia berat?",
     "Hipokalsemia: <b>QT interval memanjang</b>. Hipokalemia: <b>Gelombang T mendatar, depresi segmen ST, dan muncul Gelombang U</b>.",
     "Slide 15 & 20: Hipokalsemia & Hipokalemia")
]

for q, a, sp in cards_data:
    deck.add_note(genanki.Note(model=model, fields=[q, a, sp]))

anki_out = os.path.join(ANKI_DIR, "VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg")
genanki.Package(deck).write_to_file(anki_out)
print(f"Anki deck berhasil ditulis ke {anki_out}")

# 2. GENERATE SUPAHERO HTML MODULE
html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Blok 9 EMN · KUL 3 Defisiensi Mineral — VERTEX Inverted Mastery</title>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-canvas: #F3F5F8;
      --bg-surface: #FFFFFF;
      --bg-subtle: #EAEFF4;
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
      --radius-xl: 20px;
      --radius-lg: 14px;
      --radius-md: 10px;
      --shadow-soft: 0 12px 32px -8px rgba(11, 19, 26, 0.06);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }
    body {
      background-color: var(--bg-canvas);
      background-image: radial-gradient(#CBD6E2 1px, transparent 1px);
      background-size: 24px 24px;
      color: var(--ink-900);
      font-family: 'IBM Plex Sans', sans-serif;
      font-size: 15px;
      line-height: 1.6;
      padding-bottom: 60px;
    }
    
    /* Navbar Pill */
    .nav-wrap { position: sticky; top: 16px; z-index: 100; padding: 0 20px; margin-bottom: 24px; }
    .navbar {
      max-width: 1200px; margin: 0 auto; background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px); border: 1px solid var(--border); border-radius: 999px;
      padding: 8px 16px; display: flex; align-items: center; justify-content: space-between;
      box-shadow: var(--shadow-soft);
    }
    .nav-brand { font-weight: 700; font-size: 0.95rem; display: flex; align-items: center; gap: 8px; }
    .nav-brand span.badge { background: var(--cobalt-soft); color: var(--cobalt); font-size: 0.75rem; padding: 2px 8px; border-radius: 6px; }
    .nav-tabs { display: flex; gap: 6px; }
    .nav-tab {
      padding: 7px 14px; border-radius: 999px; font-size: 0.82rem; font-weight: 600;
      color: var(--ink-500); cursor: pointer; border: none; background: transparent; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .nav-tab:hover { background: var(--bg-subtle); color: var(--ink-900); }
    .nav-tab.active { background: var(--cobalt); color: #fff; }
    
    .container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
    
    /* Header Banner */
    .header-box {
      background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius-xl);
      padding: 32px; margin-bottom: 24px; box-shadow: var(--shadow-soft);
    }
    .header-kicker { font-size: 0.8rem; font-weight: 700; color: var(--cobalt); text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
    .header-title { font-size: 1.6rem; font-weight: 700; color: var(--ink-900); margin-bottom: 10px; }
    .header-meta { font-size: 0.88rem; color: var(--ink-500); display: flex; flex-wrap: wrap; gap: 16px; }
    
    /* Sections */
    .view-pane { display: none; }
    .view-pane.active { display: block; }
    
    .card-box {
      background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
      padding: 24px; margin-bottom: 20px; box-shadow: var(--shadow-soft);
    }
    .card-title { font-size: 1.15rem; font-weight: 700; color: var(--ink-900); margin-bottom: 14px; display: flex; align-items: center; justify-content: space-between; }
    
    /* Tables */
    .data-table { width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 0.9rem; }
    .data-table th, .data-table td { padding: 12px 14px; border: 1px solid var(--border); text-align: left; }
    .data-table th { background: var(--bg-subtle); color: var(--ink-700); font-weight: 600; }
    .data-table tr:hover { background: var(--bg-canvas); }
    
    /* Flow Steps */
    .flow-chain { display: flex; flex-direction: column; gap: 12px; margin-top: 14px; }
    .flow-node {
      background: var(--bg-canvas); border: 1px solid var(--border); border-radius: var(--radius-md);
      padding: 14px 18px; display: flex; align-items: flex-start; gap: 14px;
    }
    .flow-num {
      background: var(--cobalt); color: white; width: 28px; height: 28px; border-radius: 50%;
      display: grid; place-items: center; font-size: 0.8rem; font-weight: 700; flex: none;
    }
    
    /* Clinical Gap Box (+21%) */
    .gap-box {
      background: #FFFBF5; border: 1px solid #F5DEB3; border-left: 4px solid var(--amber);
      border-radius: var(--radius-md); padding: 16px 20px; margin-top: 20px;
    }
    .gap-title { font-weight: 700; font-size: 0.92rem; color: var(--amber); margin-bottom: 6px; display: flex; align-items: center; gap: 6px; }
    
    /* CBT Questions */
    .q-item {
      background: var(--bg-surface); border: 1px solid var(--border); border-radius: var(--radius-lg);
      padding: 22px; margin-bottom: 20px; box-shadow: var(--shadow-soft);
    }
    .q-stem { font-size: 1rem; font-weight: 600; color: var(--ink-900); margin-bottom: 16px; line-height: 1.5; }
    .q-options { display: flex; flex-direction: column; gap: 8px; }
    .opt-btn {
      padding: 12px 16px; border: 1px solid var(--border); border-radius: var(--radius-md);
      background: var(--bg-canvas); font: inherit; font-size: 0.92rem; text-align: left; cursor: pointer;
      display: flex; align-items: center; gap: 12px; transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .opt-btn:hover { border-color: var(--cobalt); transform: translateY(-1px); }
    .opt-btn.correct { background: var(--emerald-soft); border-color: var(--emerald); color: var(--emerald); font-weight: 600; }
    .opt-btn.wrong { background: var(--crimson-soft); border-color: var(--crimson); color: var(--crimson); }
    
    .q-explanation {
      margin-top: 16px; padding: 16px; background: var(--bg-subtle); border-radius: var(--radius-md);
      font-size: 0.9rem; line-height: 1.6; display: none;
    }
    .q-explanation.show { display: block; }
    
    /* Slide Dock Thumb */
    .slide-dock {
      margin-top: 12px; padding: 10px; border: 1px solid var(--border); border-radius: var(--radius-md);
      background: #fff; display: flex; align-items: center; gap: 14px; cursor: zoom-in;
    }
    .dock-thumb { width: 90px; height: 58px; object-fit: cover; border-radius: 6px; border: 1px solid var(--border); }
    
    /* Modal Zoom */
    .zoom-modal {
      position: fixed; inset: 0; background: rgba(11, 19, 26, 0.7); backdrop-filter: blur(8px);
      display: none; align-items: center; justify-content: center; z-index: 1000; padding: 20px;
    }
    .zoom-modal.open { display: flex; }
    .zoom-img { max-width: 90%; max-height: 85vh; border-radius: 12px; box-shadow: 0 20px 50px rgba(0,0,0,0.3); }
    
    /* Button styles */
    .btn {
      display: inline-flex; align-items: center; gap: 8px; padding: 9px 16px; border-radius: 999px;
      font-weight: 600; font-size: 0.85rem; text-decoration: none; cursor: pointer; border: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .btn-primary { background: var(--emerald); color: white; }
    .btn-primary:hover { opacity: 0.9; transform: translateY(-1px); }
  </style>
</head>
<body>

  <!-- Floating Nav -->
  <div class="nav-wrap">
    <div class="navbar">
      <div class="nav-brand">
        <span>🩺 VERTEX PREP</span>
        <span class="badge">EMN · KUL 3</span>
      </div>
      <div class="nav-tabs">
        <button class="nav-tab active" onclick="switchTab('tab-peta', this)">1. Peta 1 Halaman (Lapis 0)</button>
        <button class="nav-tab" onclick="switchTab('tab-mekanisme', this)">2. Rantai Mekanisme (Lapis 1)</button>
        <button class="nav-tab" onclick="switchTab('tab-fakta', this)">3. Tabel Mnemonik (Lapis 2)</button>
        <button class="nav-tab" onclick="switchTab('tab-cbt', this)">4. Kuis CBT &amp; Anki (Lapis 3)</button>
      </div>
      <div>
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn btn-primary" download>⬇ Anki (.apkg)</a>
      </div>
    </div>
  </div>

  <div class="container">
    <div class="header-box">
      <div class="header-kicker">Blok 9 (EMN) · Kuliah 3</div>
      <h1 class="header-title">Defisiensi Mineral (Fe, Ca, Zn, Mg, I, K, Cu, P)</h1>
      <div class="header-meta">
        <span>👨‍⚕️ Dosen: <b>dr. Iwal Reza Ahdi, Sp.PD-FINASIM (IWL)</b></span>
        <span>📊 Slide Asli: <b>32 Slide</b></span>
        <span>🎯 Target UAB: <b>4 Soal Pilihan Ganda (Penalaran Klinis 67%)</b></span>
      </div>
    </div>

    <!-- TAB 1: PETA 1 HALAMAN (LAPIS 0) -->
    <div id="tab-peta" class="view-pane active">
      <div class="card-box">
        <div class="card-title">
          <span>🌟 Peta Cepat 1 Halaman: Klasifikasi &amp; Slide Emas</span>
          <span style="font-size:0.8rem;color:var(--cobalt);font-weight:600;">Slide 4, 8, 10, 24</span>
        </div>
        <p style="color:var(--ink-500);margin-bottom:14px;">Hafalkan perbedaan kategori dan target organ kunci sebelum masuk ke patofisiologi:</p>
        <table class="data-table">
          <thead>
            <tr>
              <th>Kategori Mineral</th>
              <th>Daftar Mineral</th>
              <th>Karakteristik &amp; Peran Fisiologis Kunci</th>
              <th>Manifestasi Defisiensi Utama</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Makromineral</b><br><small style="color:var(--ink-500);">Kebutuhan relatif besar</small></td>
              <td><b>Ca, P, Mg, Na, K, Cl</b></td>
              <td>Struktur tulang/gigi, transmisi potensial listrik saraf-otot, homeostasis osmotik &amp; asam-basa.</td>
              <td>Tetani, aritmia, kelemahan otot, osteomalasia/rakitis.</td>
            </tr>
            <tr>
              <td><b>Mikromineral (Trace)</b><br><small style="color:var(--ink-500);">Kebutuhan kecil tapi vital</small></td>
              <td><b>Fe, Zn, I, Se, Cu, Mn</b></td>
              <td>Kofaktor enzim redoks, metabolisme DNA/protein, sintesis hormon tiroid.</td>
              <td>Anemia mikrositik, dermatitis periorifisial, gondok, kretinisme.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="card-box">
        <div class="card-title">
          <span>🎯 Golden Slide: 3 Stadium Defisiensi Besi (Slide 10)</span>
          <span style="font-size:0.8rem;color:var(--crimson);font-weight:600;">⚠️ Sering Keluar di UAB</span>
        </div>
        <p style="color:var(--ink-700);margin-bottom:12px;"><b>Prinsip Ujian:</b> MCV normal <i>tidak menyingkirkan</i> defisiensi besi stadium awal!</p>
        <div class="flow-chain">
          <div class="flow-node">
            <div class="flow-num">1</div>
            <div>
              <b>Stadium 1: Depletion of Iron Stores (Cadangan Turun)</b>
              <div style="color:var(--ink-500);font-size:0.88rem;"><b>Ferritin serum TURUN lebih awal</b> (&lt;15–30 ng/mL). Hb dan MCV masih normal! Pasien belum anemia.</div>
            </div>
          </div>
          <div class="flow-node">
            <div class="flow-num">2</div>
            <div>
              <b>Stadium 2: Iron-Deficient Erythropoiesis (Eritropoiesis Terbatas)</b>
              <div style="color:var(--ink-500);font-size:0.88rem;">Saturasi transferrin (TSAT) anjlok (&lt;16–20%), TIBC meningkat. Produksi eritrosit mulai terhambat.</div>
            </div>
          </div>
          <div class="flow-node">
            <div class="flow-num">3</div>
            <div>
              <b>Stadium 3: Iron Deficiency Anemia (Anemia Defisiensi Besi Nyata)</b>
              <div style="color:var(--ink-500);font-size:0.88rem;">Hb turun, MCV &lt; 80 fL (mikrositik), MCH turun (hipokromik). Gejala klasik lemas, pica (pagophagia: es batu).</div>
            </div>
          </div>
        </div>
        <div class="slide-dock" onclick="openZoom('slides_kul3/slide_10.jpg', 'Slide 10: Perjalanan Defisiensi Besi')">
          <img src="slides_kul3/slide_10.jpg" class="dock-thumb" alt="Slide 10">
          <div><b>Bukti Slide 10:</b> Perjalanan defisiensi besi — ferritin turun lebih awal. <span style="color:var(--cobalt);">Klik untuk zoom ↗</span></div>
        </div>
      </div>
    </div>

    <!-- TAB 2: MEKANISME & SEBAB-AKIBAT (LAPIS 1) -->
    <div id="tab-mekanisme" class="view-pane">
      <div class="card-box">
        <div class="card-title">
          <span>⚡ Mekanisme 1: Mengapa Kalium Susah Naik Bila Magnesium Rendah?</span>
          <span style="font-size:0.8rem;color:var(--cobalt);font-weight:600;">Slide 17 &amp; 28</span>
        </div>
        <div style="line-height:1.7;color:var(--ink-700);">
          <p>Pada pasien hipokalemia refrakter (sudah diberi KCl oral/IV tapi K serum tetap &lt;3.5 mEq/L), <b>penyebab utamanya adalah hipomagnesemia tersembunyi</b>.</p>
          <div style="background:var(--bg-canvas);border:1px solid var(--border);border-radius:var(--radius-md);padding:14px;margin:12px 0;">
            <b>Rantai Sebab-Akibat:</b><br>
            Mg intraseluler rendah &rarr; Kanal ROMK (<i>Renal Outer Medullary Potassium Channel</i>) di tubulus distal kehilangan inhibisi &rarr; Kanal terbuka berlebih &rarr; <b>Kalium bocor terbuang masif ke urin</b> &rarr; Hipokalemia menetap.<br>
            <b>Keputusan Klinis:</b> Koreksi Magnesium (Mg) wajib diberikan bersamaan agar Kalium bisa naik!
          </div>
        </div>
        <div class="slide-dock" onclick="openZoom('slides_kul3/slide_17.jpg', 'Slide 17: Mengapa kalium sulit naik bila magnesium rendah?')">
          <img src="slides_kul3/slide_17.jpg" class="dock-thumb" alt="Slide 17">
          <div><b>Bukti Slide 17 &amp; 28:</b> Hubungan ekskresi K renal dengan kadar Mg. <span style="color:var(--cobalt);">Klik untuk zoom ↗</span></div>
        </div>
      </div>

      <div class="card-box">
        <div class="card-title">
          <span>⚡ Mekanisme 2: Refeeding Syndrome — Bahaya Lonjakan Insulin</span>
          <span style="font-size:0.8rem;color:var(--cobalt);font-weight:600;">Slide 19 &amp; 29</span>
        </div>
        <div style="line-height:1.7;color:var(--ink-700);">
          <p>Terjadi pada pasien malnutrisi berat, anoreksia, atau puasa berkepanjangan (&gt;7–10 hari) yang mendadak diberi nutrisi karbohidrat agresif.</p>
          <div style="background:var(--bg-canvas);border:1px solid var(--border);border-radius:var(--radius-md);padding:14px;margin:12px 0;">
            <b>Rantai Patofisiologi:</b><br>
            Nutrisi karbohidrat masuk &rarr; Pankreas sekresi <b>Insulin masif</b> &rarr; Insulin mendorong glukosa, <b>Fosfat (P), Kalium (K), dan Magnesium (Mg)</b> masuk ke dalam sel &rarr; <b>Hipofosfatemia berat (&lt;1.0 mg/dL)</b> di plasma &rarr; Sel kehabisan ATP &amp; 2,3-DPG &rarr; <b>Gagal napas akut (kelemahan diafragma)</b>, aritmia jantung fatal, dan rabdomiolisis.<br>
            <b>Pencegahan (NICE/ASPEN):</b> Berikan Tiamin (B1) sebelum makan, mulai kalori rendah bertahap (10–15 kkal/kg/hari), pantau serial P-K-Mg.
          </div>
        </div>
        <div class="slide-dock" onclick="openZoom('slides_kul3/slide_19.jpg', 'Slide 19: Refeeding Syndrome')">
          <img src="slides_kul3/slide_19.jpg" class="dock-thumb" alt="Slide 19">
          <div><b>Bukti Slide 19:</b> Pola Refeeding Syndrome yang mengancam nyawa. <span style="color:var(--cobalt);">Klik untuk zoom ↗</span></div>
        </div>
      </div>

      <!-- Pelengkap Klinis 21% -->
      <div class="gap-box">
        <div class="gap-title">🩺 Pelengkap Klinis UAB (+21% Materi Sering Diuji di Luar Teks Slide)</div>
        <ul style="padding-left:20px;color:var(--ink-700);font-size:0.9rem;line-height:1.7;">
          <li><b>Tanda Fisik Hipokalsemia:</b> <i>Chvostek sign</i> (kedutan sudut bibir saat saraf fasialis diketuk) dan <i>Trousseau sign</i> (spasme karpopedal saat manset tensimeter dipompa di atas tekanan sistolik selama 3 menit).</li>
          <li><b>Interaksi Seng vs Tembaga:</b> Suplementasi Zinc &gt;50 mg/hari merangsang sintesis <i>metallothionein</i> di sel usus. Protein ini memiliki afinitas jauh lebih tinggi ke tembaga (Cu) daripada seng, sehingga tembaga terperangkap di enterosit dan terbuang &rarr; <b>Defisiensi Cu iatrogenik</b> (gejala: anemia mikrositik + neutropenia + neuropati mirip defisiensi B12).</li>
          <li><b>Aturan Terapi Besi (AGA 2024):</b> Dosis tunggal oral pagi hari (atau selang hari) lebih baik daripada 3x sehari karena setiap asupan besi memicu sekresi <b>Hepcidin</b> yang memblokir penyerapan besi berikutnya selama 24–48 jam.</li>
        </ul>
      </div>
    </div>

    <!-- TAB 3: TABEL MNEMONIK (LAPIS 2) -->
    <div id="tab-fakta" class="view-pane">
      <div class="card-box">
        <div class="card-title">
          <span>🧠 Tabel Komparasi Cepat Manifestasi &amp; Diagnosis Defisiensi Mineral</span>
          <span style="font-size:0.8rem;color:var(--cobalt);font-weight:600;">Ringkasan Hafalan Ujian</span>
        </div>
        <table class="data-table">
          <thead>
            <tr>
              <th>Mineral</th>
              <th>Gejala Khas Patognomonik</th>
              <th>Biomarker Laboratorium Kunci</th>
              <th>Faktor Risiko / Pemicu Utama</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Besi (Fe)</b></td>
              <td>Kelelahan, koilonychia (kuku sendok), glossitis, <b>pagophagia (pica es batu)</b>.</td>
              <td><b>Ferritin &lt; 15–30 ng/mL</b>, TSAT &lt; 20%, MCV &lt; 80 fL (stadium lanjut).</td>
              <td>Menstruasi berlebih, perdarahan GI okult, malabsorpsi celiac.</td>
            </tr>
            <tr>
              <td><b>Seng (Zn)</b></td>
              <td><b>Dermatitis periorifisial &amp; akral</b>, diare, alopesia, luka lambat sembuh, hipogeusia.</td>
              <td>Zinc serum/plasma rendah (&lt;70 &mu;g/dL).</td>
              <td>Diet tinggi <b>fitat</b> (serealia mentah), malabsorpsi, penyakit celiac.</td>
            </tr>
            <tr>
              <td><b>Kalsium (Ca)</b></td>
              <td>Parestesia perioral, tetani, Chvostek (+), Trousseau (+), <b>QT memanjang</b>.</td>
              <td><b>Ionized Calcium</b> (Ca bebas aktif), albumin (untuk Ca terkoreksi).</td>
              <td>Hipoparatiroid, defisiensi Vitamin D, gagal ginjal kronik.</td>
            </tr>
            <tr>
              <td><b>Magnesium (Mg)</b></td>
              <td>Tremor, hiperrefleksia, kram, aritmia (Torsades de pointes), <b>hipo-K refrakter</b>.</td>
              <td>Magnesium serum &lt; 1.7 mg/dL (&lt;0.7 mmol/L).</td>
              <td>Diare kronik, diuretik loop/tiazid, konsumsi <b>PPI jangka panjang</b>, alkohol.</td>
            </tr>
            <tr>
              <td><b>Iodium (I)</b></td>
              <td><b>Gondok endemik</b>, hipotiroidisme, pada janin: <b>kretinisme</b> &amp; retardasi mental.</td>
              <td>TSH meningkat, FT4 rendah, <i>Urinary Iodine Concentration</i> (surveilans).</td>
              <td>Daerah pegunungan tanah miskin iodium, konsumsi garam non-iodium.</td>
            </tr>
            <tr>
              <td><b>Tembaga (Cu)</b></td>
              <td><b>Anemia mikrositik + neutropenia</b>, mielopati (ataksia sensorik mirip defisiensi B12).</td>
              <td>Serum Cu rendah, <i>ceruloplasmin</i> rendah.</td>
              <td>Operasi bariatrik (bypass lambung), <b>konsumsi suplemen Zinc berlebih</b>.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- TAB 4: KUIS CBT & ANKI (LAPIS 3) -->
    <div id="tab-cbt" class="view-pane">
      <div class="card-box" style="display:flex;justify-content:space-between;align-items:center;">
        <div>
          <h2 style="font-size:1.2rem;margin-bottom:4px;">🎯 Simulator Soal UAB Adaptif Dosen (IWL)</h2>
          <p style="color:var(--ink-500);font-size:0.88rem;">6 Soal Penalaran Klinis &amp; Komparasi Khas Gaya dr. Iwal Reza Ahdi, Sp.PD.</p>
        </div>
        <div style="text-align:right;">
          <div style="font-size:0.8rem;color:var(--ink-500);">Skor Anda:</div>
          <div id="quiz-score" style="font-size:1.4rem;font-weight:700;color:var(--cobalt);">0 / 6</div>
        </div>
      </div>

      <!-- SOAL 1 -->
      <div class="q-item" id="q1">
        <div class="q-stem"><b>1.</b> Seorang perempuan berusia 29 tahun datang dengan keluhan badan lemas dan sering berdebar saat beraktivitas sejak 2 bulan terakhir. Pasien memiliki riwayat menstruasi sangat banyak selama 8 hari setiap siklusnya. Pemeriksaan laboratorium menunjukkan Hb 8,9 g/dL, leukosit 6.200/&mu;L, trombosit 380.000/&mu;L, dan MCV 68 fL. Pasien mengaku memiliki kebiasaan aneh sering mengunyah es batu berulang kali. Pemeriksaan biomarker manakah yang paling spesifik dan paling awal menurun untuk mengonfirmasi diagnosis pasien tersebut?</div>
        <div class="q-options">
          <button class="opt-btn" onclick="checkAnswer(1, 0, false)">A. Total Iron Binding Capacity (TIBC)</button>
          <button class="opt-btn" onclick="checkAnswer(1, 1, true)">B. Ferritin serum</button>
          <button class="opt-btn" onclick="checkAnswer(1, 2, false)">C. Saturasi transferrin (TSAT)</button>
          <button class="opt-btn" onclick="checkAnswer(1, 3, false)">D. Hemoglobin elektroforesis</button>
          <button class="opt-btn" onclick="checkAnswer(1, 4, false)">E. Hemosiderin urin</button>
        </div>
        <div class="q-explanation" id="exp1">
          <b>Jawaban Benar: B (Ferritin serum)</b><br>
          <i>Pembahasan:</i> Pasien mengalami Anemia Defisiensi Besi (Hb rendah, MCV &lt;80 fL / mikrositik) dengan gejala pica spesifik berupa <i>pagophagia</i> (mengunyah es batu) akibat menorrhagia. <b>Ferritin serum</b> adalah cerminan cadangan besi tubuh dan merupakan biomarker yang paling awal turun bahkan sebelum anemia terjadi (Slide 3 &amp; 10).
          <div class="slide-dock" onclick="openZoom('slides_kul3/slide_10.jpg', 'Slide 10: Tahapan Ferritin')">
            <img src="slides_kul3/slide_10.jpg" class="dock-thumb" alt="Slide 10">
            <div><b>Bukti Slide 10:</b> Ferritin turun pada stadium 1 (cadangan turun) sebelum Hb/MCV turun.</div>
          </div>
        </div>
      </div>

      <!-- SOAL 2 -->
      <div class="q-item" id="q2">
        <div class="q-stem"><b>2.</b> Seorang laki-laki 67 tahun dengan gagal jantung mengeluh lemas otot dan berdebar-debar. Pasien rutin mengonsumsi furosemid. Hasil laboratorium menunjukkan Kalium 2,8 mmol/L. Dokter telah memberikan suplementasi kalium oral dosis tinggi selama 3 hari, namun kadar Kalium ulang tetap rendah (2,9 mmol/L) dan EKG menunjukkan gelombang U. Pemeriksaan elektrolit tambahan manakah yang wajib dilakukan untuk mengatasi kondisi refrakter tersebut?</div>
        <div class="q-options">
          <button class="opt-btn" onclick="checkAnswer(2, 0, false)">A. Kalsium total</button>
          <button class="opt-btn" onclick="checkAnswer(2, 1, false)">B. Natrium serum</button>
          <button class="opt-btn" onclick="checkAnswer(2, 2, true)">C. Magnesium serum</button>
          <button class="opt-btn" onclick="checkAnswer(2, 3, false)">D. Klorida serum</button>
          <button class="opt-btn" onclick="checkAnswer(2, 4, false)">E. Fosfat serum</button>
        </div>
        <div class="q-explanation" id="exp2">
          <b>Jawaban Benar: C (Magnesium serum)</b><br>
          <i>Pembahasan:</i> Furosemid memicu kehilangan Kalium dan Magnesium sekaligus. Defisiensi <b>Magnesium (Mg)</b> menyebabkan disinhibisi kanal ROMK di tubulus ginjal sehingga Kalium terus-menerus bocor ke urin, menyebabkan hipokalemia refrakter. Kalium tidak akan bisa naik sebelum kadar magnesium dikoreksi secara bersamaan (Slide 17 &amp; 28).
          <div class="slide-dock" onclick="openZoom('slides_kul3/slide_17.jpg', 'Slide 17: Mengapa K sulit naik bila Mg rendah')">
            <img src="slides_kul3/slide_17.jpg" class="dock-thumb" alt="Slide 17">
            <div><b>Bukti Slide 17:</b> Disfungsi regulasi renal akibat Mg rendah memicu ekskresi K meningkat.</div>
          </div>
        </div>
      </div>

      <!-- SOAL 3 -->
      <div class="q-item" id="q3">
        <div class="q-stem"><b>3.</b> Anak laki-laki berusia 4 tahun dibawa ibunya dengan keluhan ruam kemerahan bersisik di sekitar mulut, anus, dan sela-sela jari kaki sejak 1 bulan lalu. Pasien juga sering mengalami diare cair kambuhan dan rambutnya rontok parah hingga tampak botak sebagian. Pasien memiliki riwayat diet monoton tinggi serealia dan bubur gandum tanpa protein hewani. Defisiensi mineral apakah yang mendasari kelainan pada anak tersebut?</div>
        <div class="q-options">
          <button class="opt-btn" onclick="checkAnswer(3, 0, false)">A. Besi (Fe)</button>
          <button class="opt-btn" onclick="checkAnswer(3, 1, false)">B. Tembaga (Cu)</button>
          <button class="opt-btn" onclick="checkAnswer(3, 2, true)">C. Seng (Zinc)</button>
          <button class="opt-btn" onclick="checkAnswer(3, 3, false)">D. Selenium (Se)</button>
          <button class="opt-btn" onclick="checkAnswer(3, 4, false)">E. Iodium (I)</button>
        </div>
        <div class="q-explanation" id="exp3">
          <b>Jawaban Benar: C (Seng / Zinc)</b><br>
          <i>Pembahasan:</i> Gejala trias berupa <b>dermatitis periorifisial/akral, diare kronik, dan alopesia</b> adalah tanda patognomonik defisiensi Seng (Zinc) (menyerupai sindrom <i>Acrodermatitis enteropathica</i>). Diet tinggi serealia kaya akan <b>fitat</b>, yang merupakan inhibitor kuat penyerapan zinc di usus (Slide 12).
          <div class="slide-dock" onclick="openZoom('slides_kul3/slide_12.jpg', 'Slide 12: Seng')">
            <img src="slides_kul3/slide_12.jpg" class="dock-thumb" alt="Slide 12">
            <div><b>Bukti Slide 12:</b> Dermatitis periorifisial/akral, diare, alopesia, diet tinggi fitat.</div>
          </div>
        </div>
      </div>

      <!-- SOAL 4 -->
      <div class="q-item" id="q4">
        <div class="q-stem"><b>4.</b> Laki-laki 46 tahun dengan riwayat malnutrisi berat dan tidak makan selama 12 hari dirawat di bangsal. Dokter memberikan nutrisi enteral tinggi karbohidrat secara cepat. Dalam 48 jam, pasien mendadak mengalami kelemahan otot menyeluruh, sesak napas berat (takipnea), dan takikardia. Pemeriksaan elektrolit serum manakah yang paling mungkin menunjukkan penurunan sangat drastis (&lt;1.0 mg/dL) sebagai pemicu gagal napas akut pada pasien tersebut?</div>
        <div class="q-options">
          <button class="opt-btn" onclick="checkAnswer(4, 0, false)">A. Natrium serum</button>
          <button class="opt-btn" onclick="checkAnswer(4, 1, false)">B. Kalsium terionisasi</button>
          <button class="opt-btn" onclick="checkAnswer(4, 2, true)">C. Fosfat serum</button>
          <button class="opt-btn" onclick="checkAnswer(4, 3, false)">D. Klorida serum</button>
          <button class="opt-btn" onclick="checkAnswer(4, 4, false)">E. Bikarbonat serum</button>
        </div>
        <div class="q-explanation" id="exp4">
          <b>Jawaban Benar: C (Fosfat serum)</b><br>
          <i>Pembahasan:</i> Pasien mengalami <b>Refeeding Syndrome</b>. Pemberian nutrisi memicu lonjakan insulin yang mendorong glukosa dan <b>Fosfat (P)</b> masuk ke dalam sel. Terjadilah hipofosfatemia berat (&lt;1 mg/dL) yang melumpuhkan pembentukan ATP seluler, menyebabkan kelemahan diafragma akut (gagal napas) dan aritmia (Slide 18, 19, &amp; 29).
          <div class="slide-dock" onclick="openZoom('slides_kul3/slide_19.jpg', 'Slide 19: Refeeding Syndrome')">
            <img src="slides_kul3/slide_19.jpg" class="dock-thumb" alt="Slide 19">
            <div><b>Bukti Slide 19:</b> Refeeding syndrome memicu elektrolit P, K, Mg masuk ke intrasel.</div>
          </div>
        </div>
      </div>

      <!-- SOAL 5 -->
      <div class="q-item" id="q5">
        <div class="q-stem"><b>5.</b> Seorang perempuan 35 tahun pasca operasi bypass lambung (bariatrik) 1 tahun lalu datang dengan keluhan kesemutan dan rasa baal pada kedua tungkai bawah serta gaya berjalan yang tidak stabil (ataksia). Pemeriksaan darah menunjukkan Hb 9.2 g/dL, MCV 74 fL (mikrositik), dan neutropenia berat (leukosit 2.400/&mu;L, ANC 800/&mu;L). Pasien mengaku rutin mengonsumsi multivitamin Zinc dosis tinggi (80 mg/hari) tanpa pengawasan. Defisiensi mikromineral apakah yang paling tepat menjelaskan kondisi pasien?</div>
        <div class="q-options">
          <button class="opt-btn" onclick="checkAnswer(5, 0, false)">A. Besi</button>
          <button class="opt-btn" onclick="checkAnswer(5, 1, true)">B. Tembaga (Cu)</button>
          <button class="opt-btn" onclick="checkAnswer(5, 2, false)">C. Selenium</button>
          <button class="opt-btn" onclick="checkAnswer(5, 3, false)">D. Mangan</button>
          <button class="opt-btn" onclick="checkAnswer(5, 4, false)">E. Kobalt</button>
        </div>
        <div class="q-explanation" id="exp5">
          <b>Jawaban Benar: B (Tembaga / Cu)</b><br>
          <i>Pembahasan:</i> <b>Anemia mikrositik + neutropenia + mielopati/gejala neurologis</b> adalah kombinasi klasik defisiensi Tembaga (Cu). Riwayat konsumsi Zinc tinggi berkepanjangan memicu induksi metallothionein usus yang memblokade absorpsi Cu, memicu defisiensi tembaga iatrogenik (Slide 22).
          <div class="slide-dock" onclick="openZoom('slides_kul3/slide_22.jpg', 'Slide 22: Tembaga')">
            <img src="slides_kul3/slide_22.jpg" class="dock-thumb" alt="Slide 22">
            <div><b>Bukti Slide 22:</b> Zinc tinggi berkepanjangan memicu penyerapan Cu menurun &rarr; anemia + neutropenia.</div>
          </div>
        </div>
      </div>

      <!-- SOAL 6 -->
      <div class="q-item" id="q6">
        <div class="q-stem"><b>6.</b> Berdasarkan pembaruan klinis *American Gastroenterological Association* (AGA 2024), bagaimanakah aturan pemberian preparat besi oral yang paling efektif dan dapat ditoleransi dengan baik pada pasien anemia defisiensi besi?</div>
        <div class="q-options">
          <button class="opt-btn" onclick="checkAnswer(6, 0, false)">A. Diberikan 3 kali sehari bersamaan dengan makanan tinggi serat</button>
          <button class="opt-btn" onclick="checkAnswer(6, 1, false)">B. Diberikan dosis ganda setiap 8 jam disertai antasida</button>
          <button class="opt-btn" onclick="checkAnswer(6, 2, true)">C. Diberikan maksimal 1 kali sehari atau rejimen selang hari</button>
          <button class="opt-btn" onclick="checkAnswer(6, 3, false)">D. Diberikan bersamaan dengan susu sapi segar</button>
          <button class="opt-btn" onclick="checkAnswer(6, 4, false)">E. Diberikan 4 kali sehari dalam dosis terbagi</button>
        </div>
        <div class="q-explanation" id="exp6">
          <b>Jawaban Benar: C (Diberikan maksimal 1 kali sehari atau rejimen selang hari)</b><br>
          <i>Pembahasan:</i> Pedoman AGA 2024 menekankan bahwa konsumsi besi oral dosis tinggi harian memicu peningkatan <b>Hepcidin</b> yang memblokade absorpsi besi selanjutnya. Oleh karena itu, pemberian maksimal 1 kali sehari atau rejimen <b>selang hari (alternate day)</b> memberikan absorpsi fraksional lebih baik dan meminimalkan efek samping GI (Slide 11).
          <div class="slide-dock" onclick="openZoom('slides_kul3/slide_11.jpg', 'Slide 11: Terapi Fe AGA 2024')">
            <img src="slides_kul3/slide_11.jpg" class="dock-thumb" alt="Slide 11">
            <div><b>Bukti Slide 11:</b> Terapi oral maksimal 1x/hari, rejimen selang hari lebih mudah ditoleransi.</div>
          </div>
        </div>
      </div>

    </div>
  </div>

  <!-- Zoom Modal -->
  <div class="zoom-modal" id="zoom-modal" onclick="closeZoom()">
    <img src="" id="zoom-img" class="zoom-img" alt="Zoom Slide">
  </div>

  <script>
    function switchTab(tabId, btn) {
      document.querySelectorAll('.view-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
      document.getElementById(tabId).classList.add('active');
      btn.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    let userScore = 0;
    const answered = {};

    function checkAnswer(qNum, optIdx, isCorrect) {
      if (answered[qNum]) return;
      answered[qNum] = true;
      
      const qBox = document.getElementById('q' + qNum);
      const btns = qBox.querySelectorAll('.opt-btn');
      
      if (isCorrect) {
        btns[optIdx].classList.add('correct');
        userScore++;
      } else {
        btns[optIdx].classList.add('wrong');
        // highlight correct one
        btns.forEach(b => {
          if (b.getAttribute('onclick').includes('true')) b.classList.add('correct');
        });
      }
      
      document.getElementById('exp' + qNum).classList.add('show');
      document.getElementById('quiz-score').textContent = userScore + " / 6";
    }

    function openZoom(src, title) {
      const modal = document.getElementById('zoom-modal');
      const img = document.getElementById('zoom-img');
      img.src = src;
      modal.classList.add('open');
    }

    function closeZoom() {
      document.getElementById('zoom-modal').classList.remove('open');
    }

    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeZoom();
    });
  </script>
</body>
</html>
"""

html_out = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")
with open(html_out, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Modul HTML berhasil dibuat di {html_out}")

# 3. UPDATE SUMMARIES.JSON
sum_path = os.path.join(BASE_DIR, "summaries.json")
try:
    with open(sum_path, "r", encoding="utf-8") as f:
        sum_data = json.load(f)
except Exception:
    sum_data = {}

# Map KUL 3 Mineral Drive ID
sum_data["1nDM2aZ2IdXxCQPBEwbF84RFVycf5-rkG"] = {
    "title": "EMN KUL 3 — Defisiensi Mineral",
    "url": "EMN_KUL3_Defisiensi_Mineral.html"
}

with open(sum_path, "w", encoding="utf-8") as f:
    json.dump(sum_data, f, ensure_ascii=False, indent=2)
print("summaries.json berhasil diperbarui dengan entri KUL 3 Mineral!")
