#!/usr/bin/env python3
"""
EMN KUL 5 — MALNUTRISI ENERGI PROTEIN (dr. Ditya Arisanti, Sp.A) — 42 slide.

Dibangun dengan design system "Split-Screen Mastery" yang diwarisi dari modul
HI KUL 20 (CSS diekstrak saat build supaya konsisten, bukan disalin manual).

Keluaran:
  EMN_KUL5_Malnutrisi.html          modul 6 bab + tryout
  anki/VERTEX_EMN_KUL5_Malnutrisi.apkg
  slides_emn_kul5/slide_1..42.jpg

Semua fakta diambil dari slide asli dosen. Soal latihan diberi label jujur:
tidak ada arsip UAB EMN, jadi bukan "soal asli UAB".
"""
from __future__ import annotations

import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "/Users/dimaswastu/VERTEX-PREP"
REF = os.path.join(REPO, "HI_KUL20_Autoimunitas.html")

DRIVE_ID = "1nDM2aZ2IdXxCQPBEwbF84RFVycf5-rkG"  # placeholder; diganti saat registrasi

# --------------------------------------------------------------------------- css
def ambil_css(path: str) -> str:
    html = open(path, encoding="utf-8").read()
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    if not m:
        raise SystemExit("CSS tidak ditemukan di " + path)
    return m.group(1)


CSS_TAMBAHAN = """
    /* --- tabel pembanding (khusus modul ini) --- */
    .cmp-wrap { overflow-x: auto; margin-top: 18px; }
    table.cmp {
      width: 100%; border-collapse: collapse; font-size: 0.92rem; line-height: 1.55;
      background: var(--surface-card); border: 1px solid var(--border); border-radius: var(--r-md);
      overflow: hidden;
    }
    table.cmp th, table.cmp td { padding: 10px 14px; border-bottom: 1px solid var(--border); vertical-align: top; text-align: left; }
    table.cmp thead th { background: var(--surface-subtle); font-size: 0.72rem; letter-spacing: .08em; text-transform: uppercase; color: var(--ink-muted); }
    table.cmp tbody th { width: 26%; font-weight: 600; color: var(--ink); font-size: 0.84rem; }
    table.cmp tr:last-child td, table.cmp tr:last-child th { border-bottom: 0; }
    table.cmp td.kwashi { color: var(--coral); }
    table.cmp td.marasm { color: var(--navy); }
    .num-table { font-family: var(--font-mono); font-variant-numeric: tabular-nums; }

    /* --- ponsel: cegah halaman melebar --- */
    @media (max-width: 900px) {
      .topbar-inner { flex-wrap: wrap; height: auto; padding: 10px 14px; gap: 8px 10px; }
      .brand-group { min-width: 0; flex-wrap: wrap; width: 100%; }
      .course-select { width: 100%; max-width: 100%; }
      .tool-group { flex-wrap: wrap; width: 100%; justify-content: flex-start; }
      .page-wrap { padding-left: 14px; padding-right: 14px; }
      .narrative-panel { min-width: 0; padding: 22px 16px; }
      .hook-hero { padding: 26px 18px; }
      .cmp-wrap { max-width: 100%; overflow-x: auto; }
      table.cmp { font-size: 0.82rem; }
      table.cmp th, table.cmp td { padding: 8px 9px; }
      .slide-stage img, .stage-frame img { max-width: 100%; height: auto; }
    }
"""

# --------------------------------------------------------------------------- body
HERO = """
    <section class="hook-hero">
      <div class="hook-meta-row">
        <span class="meta-pill pill-skdi">Blok 9 EMN · 42 Slide Asli dr. Ditya Arisanti, Sp.A</span>
        <span class="meta-pill pill-uab">Tryout = Latihan Berbasis Slide, bukan arsip UAB</span>
        <span class="meta-pill pill-slides">6 Bab · 10 Langkah Tatalaksana</span>
      </div>
      <h1 class="hook-headline">Anak yang Tubuhnya Mulai Memakan Dirinya Sendiri</h1>
      <p class="hook-lead">
        Pada malnutrisi energi protein, tubuh tidak sekadar kurus. Ia membakar otot untuk menjaga
        gula darah, menurunkan laju metabolik, dan pada titik tertentu <b>membanjiri jaringan dengan
        natrium sampai timbul edema</b> — sehingga anak bisa tampak "gemuk" padahal sedang sekarat.
        Tiga kasus di bawah adalah pola yang paling sering muncul di ujian, dan semuanya bisa
        dijawab hanya dari slide dr. Ditya:
      </p>

      <div class="enigma-row">
        <div class="enigma-card">
          <div>
            <div class="enigma-tag">KASUS 1 · EDEMA</div>
            <h3 class="enigma-title">Balita 18 bulan, "kok bengkak?"</h3>
            <p class="enigma-desc">BB 8 kg, kedua punggung kaki pitting edema, rambut merah kecoklatan dan mudah dicabut, wajah moon face. Albumin 1,8 g/dL. Ini marasmus atau kwashiorkor?</p>
          </div>
          <button type="button" class="enigma-btn" onclick="showMystery(1)">Buka Jawabannya ↗</button>
        </div>

        <div class="enigma-card">
          <div>
            <div class="enigma-tag">KASUS 2 · TANPA EDEMA</div>
            <h3 class="enigma-title">Iga gambang, tapi lahap makan</h3>
            <p class="enigma-desc">Balita 24 bulan sangat kurus, perut cekung, iga gambang, lemak subkutan hilang, nafsu makan justru baik, tidak ada edema. Mengapa prognosisnya berbeda?</p>
          </div>
          <button type="button" class="enigma-btn" onclick="showMystery(2)">Buka Jawabannya ↗</button>
        </div>

        <div class="enigma-card">
          <div>
            <div class="enigma-tag">KASUS 3 · JAM 3 PAGI</div>
            <h3 class="enigma-title">Kejang di tengah malam</h3>
            <p class="enigma-desc">Anak gizi buruk dirawat, pukul 03.00 kejang, glukosa darah 40 mg/dL, masih sadar. Apa langkah pertama 10 langkah tatalaksana, dan berapa dosisnya?</p>
          </div>
          <button type="button" class="enigma-btn" onclick="showMystery(3)">Buka Jawabannya ↗</button>
        </div>
      </div>

      <div id="mystery-box" class="enigma-answer"></div>
    </section>
"""

BAB1 = """
    <section class="split-chapter" id="bab-1">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 01 · Slide 6–10 &amp; 13</span>
          <span class="meta-pill pill-uab">Definisi &amp; spektrum</span>
        </div>
        <h2 class="ch-title">Malnutrisi Bukan Sekadar Kurus: Dari Gizi Kurang sampai Obesitas</h2>

        <div class="peer-talk">
          <p><b>Slide 6</b> memberi definisi yang lebih luas dari dugaan orang: <span class="med-term" tabindex="0">Malnutrisi<span class="med-tooltip"><span class="tt-kicker">Definisi Slide 6</span><span class="tt-title">Malnutrition</span><span class="tt-desc">Mencakup <i>undernutrition</i> dan <i>overnutrition</i>.</span><span class="tt-pearl">💡 MEP adalah bagian <i>undernutrition</i>: defisiensi energi + protein, umumnya disertai kekurangan zat gizi lain.</span></span></span> mencakup dua kutub sekaligus: <b>undernutrition</b> dan <b>overnutrition</b>. Yang kita pelajari di blok ini adalah <b>Malnutrisi Energi Protein (MEP)</b> — defisiensi energi dan protein yang hampir selalu ditemani defisiensi mikronutrien.</p>
          <p><b>Slide 7</b> menurunkan definisi itu ke bahasa Permenkes No. 29/2019, dan inilah yang dipakai untuk menegakkan diagnosis di puskesmas: <b>gizi kurang</b> bila BB/PB atau BB/TB antara −3 SD sampai −2 SD, dan/atau LILA 11,5–12,5 cm pada anak 6–59 bulan; <b>gizi buruk</b> bila sangat kurus, dengan atau tanpa edema.</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Tiga istilah yang sering tertukar (Slide 9)</h4>
            <ul>
              <li><b>Wasting (kurus)</b> — BB/TB rendah. Tanda malnutrisi <b>akut</b>.</li>
              <li><b>Stunting (pendek)</b> — TB/U rendah. Tanda malnutrisi <b>kronis</b>.</li>
              <li><b>Underweight</b> — BB/U rendah. Bisa akut, kronis, atau keduanya.</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Batas angka yang harus dihafal (Slide 13)</h4>
            <ul>
              <li>Gizi kurang: −3 SD &lt; z &lt; −2 SD · gizi buruk: &lt; −3 SD</li>
              <li><i>Severe wasting</i>: BB/TB &lt; −3 SD</li>
              <li><i>Severe stunting</i>: TB/U &lt; −3 SD</li>
              <li>Edema simetris = tanda gizi buruk, berapa pun BB-nya</li>
            </ul>
          </div>
        </div>

        <div class="callout note-warn">
          <div class="callout-title">Jebakan ujian</div>
          Anak dengan edema bisa punya BB/U yang <b>tidak terlalu rendah</b>. Kalau kamu hanya memakai
          BB/U, kwashiorkor akan lolos dari diagnosis. Edema simetris selalu menempatkan anak di
          kategori gizi buruk.
        </div>

        <div class="inline-quiz" id="iq-1">
          <div class="iq-kicker">Latihan Bab 1 · berbasis slide 7 &amp; 9</div>
          <div class="iq-stem">Balita 30 bulan, BB/TB −3,2 SD, tanpa edema. Istilah yang tepat untuk kondisi ini adalah…</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-1', 0, true, 'BB/TB rendah = wasting, tanda malnutrisi akut (Slide 9).')"><span>A.</span><span>Wasting (malnutrisi akut)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-1', 1, false, 'Stunting dinilai dari TB/U, bukan BB/TB.')"><span>B.</span><span>Stunting (malnutrisi kronis)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-1', 2, false, 'Underweight dinilai dari BB/U; bisa akut maupun kronis.')"><span>C.</span><span>Underweight</span></button>
          </div>
          <div class="iq-fb" id="iq-1-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 01 · Slide Asli (6–10, 13)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch1">
          <button class="slide-pill active" onclick="setStage('ch1', 6, 'Slide 6 · Definisi Malnutrisi &amp; MEP', this)">Slide 6</button>
          <button class="slide-pill" onclick="setStage('ch1', 7, 'Slide 7 · Definisi Permenkes No. 29/2019', this)">Slide 7</button>
          <button class="slide-pill" onclick="setStage('ch1', 9, 'Slide 9 · Wasting, Stunting, Underweight', this)">Slide 9</button>
          <button class="slide-pill" onclick="setStage('ch1', 10, 'Slide 10 · Spektrum Status Nutrisi', this)">Slide 10</button>
          <button class="slide-pill" onclick="setStage('ch1', 13, 'Slide 13 · Ambang z-score WHO', this)">Slide 13</button>
        </div>
        <div class="stage-frame" onclick="openZoom(this.querySelector('img').src)">
          <img id="img-ch1" src="slides_emn_kul5/slide_6.jpg" alt="Slide 6 — definisi malnutrisi energi protein">
        </div>
        <div class="stage-caption" id="cap-ch1">Slide 6 · Definisi Malnutrisi &amp; MEP</div>
      </aside>
    </section>
"""

BAB2 = """
    <section class="split-chapter" id="bab-2">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 02 · Slide 8, 21–23</span>
          <span class="meta-pill pill-uab">Marasmus vs Kwashiorkor</span>
        </div>
        <h2 class="ch-title">Tiga Wajah MEP, Satu Tubuh yang Berbeda Cerita</h2>

        <div class="peer-talk">
          <p><b>Slide 8</b> membagi MEP tiga arah sekaligus. Menurut <b>bentuk klinis</b>: marasmus, kwashiorkor, dan marasmik-kwashiorkor. Menurut <b>sebab</b>: primer (makanan tidak tersedia atau kualitasnya kurang) dan sekunder (kebutuhan meningkat atau kehilangan berlebih). Menurut <b>jalannya penyakit</b>: akut dan kronis.</p>
          <p><b>Slide 21</b> adalah tabel yang paling sering diminta di ujian. Bedanya bukan sekadar "ada edema atau tidak" — kwashiorkor juga mengubah rambut, kulit, hati, dan albumin, sementara marasmus hampir murni kehilangan massa.</p>
        </div>

        <div class="cmp-wrap">
          <table class="cmp">
            <thead>
              <tr><th scope="col">Pembeda</th><th scope="col">Marasmus</th><th scope="col">Kwashiorkor</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Perubahan mental</th><td class="marasm">Jarang</td><td class="kwashi">Apatis, lesu</td></tr>
              <tr><th scope="row">Bentuk perut</th><td class="marasm">Cekung, iga gambang</td><td class="kwashi">Edema (pitting)</td></tr>
              <tr><th scope="row">Kulit &amp; rambut</th><td class="marasm">Tidak tampak perubahan</td><td class="kwashi">Dermatosis; rambut merah, belang seperti rambut jagung</td></tr>
              <tr><th scope="row">Lemak subkutan</th><td class="marasm">Tidak tampak</td><td class="kwashi">Masih tampak</td></tr>
              <tr><th scope="row">BB/U</th><td class="marasm">Sangat rendah</td><td class="kwashi">Tidak terlalu rendah</td></tr>
              <tr><th scope="row">Nafsu makan</th><td class="marasm">Masih baik</td><td class="kwashi">Sangat turun, sering diare</td></tr>
              <tr><th scope="row">Hati</th><td class="marasm">Tidak hepatomegali</td><td class="kwashi">Sering hepatomegali</td></tr>
              <tr><th scope="row">Hb &amp; albumin</th><td class="marasm">Hb normal, albumin normal atau sedikit turun</td><td class="kwashi">Hb dan albumin rendah</td></tr>
            </tbody>
          </table>
        </div>

        <div class="callout note-bad">
          <div class="callout-title">Kesalahan fatal</div>
          Memberi diuretik untuk edema pada kwashiorkor. Edema di sini bukan kelebihan cairan yang perlu
          dibuang, melainkan akibat ketidakseimbangan elektrolit dan kebocoran kapiler (Slide 34).
        </div>

        <div class="inline-quiz" id="iq-2">
          <div class="iq-kicker">Latihan Bab 2 · berbasis slide 21</div>
          <div class="iq-stem">Balita dengan edema pitting, rambut merah mudah dicabut, hepatomegali, dan albumin 2,0 g/dL. Diagnosis bentuk klinis yang paling tepat…</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-2', 0, false, 'Marasmus justru tanpa edema dan tanpa hepatomegali.')"><span>A.</span><span>Marasmus</span></button>
            <button class="iq-btn" onclick="ansInline('iq-2', 1, true, 'Edema + dermatosis + hepatomegali + albumin rendah = kwashiorkor (Slide 21).')"><span>B.</span><span>Kwashiorkor</span></button>
            <button class="iq-btn" onclick="ansInline('iq-2', 2, false, 'Marasmik-kwashiorkor menggabungkan tanda keduanya; di sini gambaran kwashiorkor jelas.')"><span>C.</span><span>Marasmik-kwashiorkor</span></button>
          </div>
          <div class="iq-fb" id="iq-2-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 02 · Slide Asli (8, 21–23)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch2">
          <button class="slide-pill active" onclick="setStage('ch2', 8, 'Slide 8 · Klasifikasi MEP', this)">Slide 8</button>
          <button class="slide-pill" onclick="setStage('ch2', 21, 'Slide 21 · Tanda &amp; Gejala: Marasmus vs Kwashiorkor', this)">Slide 21</button>
          <button class="slide-pill" onclick="setStage('ch2', 22, 'Slide 22 · Foto Marasmus', this)">Slide 22</button>
          <button class="slide-pill" onclick="setStage('ch2', 23, 'Slide 23 · Foto Kwashiorkor', this)">Slide 23</button>
        </div>
        <div class="stage-frame" onclick="openZoom(this.querySelector('img').src)">
          <img id="img-ch2" src="slides_emn_kul5/slide_21.jpg" alt="Slide 21 — tabel pembeda marasmus dan kwashiorkor">
        </div>
        <div class="stage-caption" id="cap-ch2">Slide 21 · Tanda &amp; Gejala: Marasmus vs Kwashiorkor</div>
      </aside>
    </section>
"""

BAB3 = """
    <section class="split-chapter" id="bab-3">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 03 · Slide 11–12</span>
          <span class="meta-pill pill-uab">Skor klasifikasi</span>
        </div>
        <h2 class="ch-title">Empat Skor yang Menjawab Pertanyaan Berbeda</h2>

        <div class="peer-talk">
          <p><b>Slide 11</b> membandingkan tiga sistem klasik. <b>Gomez</b> hanya memakai BB/U — cepat, tapi buta terhadap jenis defisit. <b>Wellcome</b> menambahkan edema ke BB/U, sehingga bisa memisahkan kwashiorkor dan marasmik-kwashiorkor. <b>Waterlow</b> memakai TB/U dan BB/TB, dan justru inilah yang bisa membedakan <i>wasting</i> dari <i>stunting</i>.</p>
          <p><b>Slide 12</b> menambahkan skor <b>McLaren</b> yang menggabungkan klinis dan laboratorium. Nilainya dijumlahkan, lalu dipetakan ke bentuk klinis.</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Skor McLaren (Slide 12)</h4>
            <ul>
              <li>Edema <b>3</b> · Dermatosis <b>2</b> · keduanya <b>6</b></li>
              <li>Perubahan rambut <b>1</b> · Hepatomegali <b>1</b></li>
              <li>Albumin: &lt;1 → 7 · 1,0–1,49 → 6 · 1,5–1,99 → 5 · 2,0–2,49 → 4</li>
              <li>2,5–2,99 → 3 · 3,0–3,49 → 2 · 3,5–3,99 → 1 · &gt;4 → 0</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Pemetaan skor (Slide 12)</h4>
            <ul>
              <li><b>0–3</b> → Marasmus</li>
              <li><b>4–8</b> → Kwashiorkor marasmik</li>
              <li><b>9–15</b> → Kwashiorkor</li>
            </ul>
            <p style="margin-top:10px;font-size:0.86rem;color:var(--ink-muted);">Contoh: edema + dermatosis (6) + albumin 2,2 g/dL (4) = <b>10</b> → kwashiorkor.</p>
          </div>
        </div>

        <div class="callout note-warn">
          <div class="callout-title">Jebakan ujian</div>
          Gomez tidak bisa membedakan wasting dan stunting karena hanya memakai BB/U. Kalau soal
          menanyakan kemampuan membedakan keduanya, jawabannya <b>Waterlow</b>.
        </div>

        <div class="inline-quiz" id="iq-3">
          <div class="iq-kicker">Latihan Bab 3 · berbasis slide 11–12</div>
          <div class="iq-stem">Seorang balita: edema (3), dermatosis (2), rambut berubah (1), albumin 1,6 g/dL (5). Berapa skor McLaren dan bentuk klinisnya?</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-3', 0, false, 'Hitung ulang: 3 + 2 + 1 + 5 = 11, bukan 9.')"><span>A.</span><span>9 — marasmik-kwashiorkor</span></button>
            <button class="iq-btn" onclick="ansInline('iq-3', 1, true, '3+2+1+5 = 11 → rentang 9–15 = kwashiorkor (Slide 12).')"><span>B.</span><span>11 — kwashiorkor</span></button>
            <button class="iq-btn" onclick="ansInline('iq-3', 2, false, 'Skor 6 hanya dari edema+dermatosis saja; di sini masih ada rambut dan albumin.')"><span>C.</span><span>6 — marasmus</span></button>
          </div>
          <div class="iq-fb" id="iq-3-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 03 · Slide Asli (11–12)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch3">
          <button class="slide-pill active" onclick="setStage('ch3', 11, 'Slide 11 · Gomez, Wellcome, Waterlow', this)">Slide 11</button>
          <button class="slide-pill" onclick="setStage('ch3', 12, 'Slide 12 · Skor McLaren', this)">Slide 12</button>
        </div>
        <div class="stage-frame" onclick="openZoom(this.querySelector('img').src)">
          <img id="img-ch3" src="slides_emn_kul5/slide_12.jpg" alt="Slide 12 — skor McLaren">
        </div>
        <div class="stage-caption" id="cap-ch3">Slide 12 · Skor McLaren</div>
      </aside>
    </section>
"""

BAB4 = """
    <section class="split-chapter" id="bab-4">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 04 · Slide 15 &amp; 34</span>
          <span class="meta-pill pill-uab">Patofisiologi</span>
        </div>
        <h2 class="ch-title">Yang Terjadi di Dalam Tubuh: Organ demi Organ</h2>

        <div class="peer-talk">
          <p><b>Slide 15</b> mendaftar perubahan yang menjelaskan hampir semua gejala klinis. Berat badan turun, elektrolit kacau (<b>hipernatremia</b> dan <b>hipokalemia</b>), lalu organ demi organ menyesuaikan diri dengan keadaan kelaparan: otak mengecil, jantung menurunkan <i>stroke volume</i> dan <i>cardiac output</i>, hati mengalami degenerasi lemak, mukosa usus atrofi sehingga enzim menurun, ginjal mengalami hialinisasi dan nekrosis tubuler, otot menyusut sampai 30%.</p>
          <p>Sistem endokrin ikut berbalik arah: hormon tiroid, insulin, dan IGF <b>turun</b>; glukokortikoid dan GH <b>naik</b> — tubuh masuk mode katabolik untuk mempertahankan glukosa darah.</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Konsekuensi klinis</h4>
            <ul>
              <li>Cadangan energi terbatas → hipoglikemia dan hipotermia mudah terjadi</li>
              <li>Atrofi mukosa usus → diare dan malabsorpsi makin memberat</li>
              <li>Cardiac output turun → tanda renjatan mudah muncul</li>
              <li>Hipokalemia + hipomagnesemia → hipokalemia refrakter</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Kenapa edema tidak boleh diberi diuretik</h4>
            <p style="font-size:0.92rem;line-height:1.6;">Slide 34 menjelaskan: malnutrisi berat mengalami <b>kelebihan natrium</b>, <b>kekurangan kalium dan magnesium</b>. Edema muncul dari ketidakseimbangan elektrolit, bukan dari volume cairan berlebih yang perlu dibuang. Diuretik akan memperburuk hipokalemia.</p>
          </div>
        </div>

        <div class="inline-quiz" id="iq-4">
          <div class="iq-kicker">Latihan Bab 4 · berbasis slide 15 &amp; 34</div>
          <div class="iq-stem">Mengapa pemberian diuretik pada edema kwashiorkor berbahaya?</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-4', 0, false, 'Edema di sini bukan karena kelebihan cairan sederhana, melainkan ketidakseimbangan elektrolit.')"><span>A.</span><span>Karena edema disebabkan kelebihan cairan berat</span></button>
            <button class="iq-btn" onclick="ansInline('iq-4', 1, true, 'Diuretik memperburuk hipokalemia dan ketidakseimbangan elektrolit yang sudah ada (Slide 34).')"><span>B.</span><span>Karena akan memperburuk hipokalemia dan gangguan elektrolit</span></button>
            <button class="iq-btn" onclick="ansInline('iq-4', 2, false, 'Justru diuresis bukan terapi edema pada kwashiorkor.')"><span>C.</span><span>Karena akan menurunkan albumin lebih cepat</span></button>
          </div>
          <div class="iq-fb" id="iq-4-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 04 · Slide Asli (15, 34)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch4">
          <button class="slide-pill active" onclick="setStage('ch4', 15, 'Slide 15 · Perubahan Tubuh pada Malnutrisi', this)">Slide 15</button>
          <button class="slide-pill" onclick="setStage('ch4', 34, 'Slide 34 · Gangguan Keseimbangan Elektrolit', this)">Slide 34</button>
        </div>
        <div class="stage-frame" onclick="openZoom(this.querySelector('img').src)">
          <img id="img-ch4" src="slides_emn_kul5/slide_15.jpg" alt="Slide 15 — perubahan tubuh pada malnutrisi">
        </div>
        <div class="stage-caption" id="cap-ch4">Slide 15 · Perubahan Tubuh pada Malnutrisi</div>
      </aside>
    </section>
"""

BAB5 = """
    <section class="split-chapter" id="bab-5">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 05 · Slide 17–20, 24</span>
          <span class="meta-pill pill-uab">Diagnosis MAB</span>
        </div>
        <h2 class="ch-title">Menegakkan Diagnosis dan Memisahkan yang Berkomplikasi</h2>

        <div class="peer-talk">
          <p><b>Slide 17</b> memberi empat kriteria Malnutrisi Akut Berat: terlihat sangat kurus, edema nutrisional, BB/TB &lt; −3 SD, atau LILA &lt; 115 mm. Setelah itu pertanyaannya berubah: <b>ada komplikasi atau tidak?</b></p>
          <p>Komplikasi yang dimaksud bukan hal sepele — anoreksia, muntah profus, dehidrasi berat, letargi, penurunan kesadaran, hipotermia/hipertermia, pneumonia, anemia berat, edema 3+, dan lesi kulit berat. Adanya satu saja sudah menempatkan pasien di jalur rawat inap.</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Anamnesis (Slide 19)</h4>
            <ul>
              <li>Makanan sehari-hari sebelum sakit; asupan beberapa hari terakhir</li>
              <li>ASI/MPASI, muntah &amp; diare (durasi, frekuensi, warna)</li>
              <li>BAK terakhir, berat lahir, tumbuh kembang</li>
              <li>Kontak TB/campak, imunisasi, riwayat penyakit keluarga</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Pemeriksaan fisis (Slide 20)</h4>
            <ul>
              <li>BB, PB/TB; suhu (hipotermi/demam)</li>
              <li>Pucat (anemia gravis), respirasi (pneumonia/gagal jantung)</li>
              <li>Tanda kolaps: akral dingin, nadi lemah, kesadaran menurun</li>
              <li><i>Old man face</i>, edema, <i>baggy pant</i>, atrofi otot, hepatomegali</li>
            </ul>
          </div>
        </div>

        <div class="callout note-warn">
          <div class="callout-title">Jebakan ujian</div>
          Tanda dehidrasi pada MAB sulit dinilai secara klinis. Slide 31 menegaskan diagnosis pasti
          dehidrasi memakai <b>berat jenis urine &gt; 1.030</b> ditambah tanda klinis lain — bukan hanya
          mata cekung atau turgor.
        </div>

        <div class="inline-quiz" id="iq-5">
          <div class="iq-kicker">Latihan Bab 5 · berbasis slide 17</div>
          <div class="iq-stem">Balita dengan BB/TB −3,4 SD, LILA 108 mm, letargi dan muntah berulang. Kategori yang tepat…</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-5', 0, false, 'Tanpa komplikasi berarti tidak ada tanda bahaya; di sini ada letargi dan muntah.')"><span>A.</span><span>MAB tanpa komplikasi</span></button>
            <button class="iq-btn" onclick="ansInline('iq-5', 1, true, 'Kriteria MAB terpenuhi dan ada komplikasi (letargi, muntah) → rawat inap (Slide 17).')"><span>B.</span><span>MAB dengan komplikasi</span></button>
            <button class="iq-btn" onclick="ansInline('iq-5', 2, false, 'Gizi kurang tidak memenuhi kriteria MAB; di sini BB/TB sudah < −3 SD.')"><span>C.</span><span>Gizi kurang tanpa komplikasi</span></button>
          </div>
          <div class="iq-fb" id="iq-5-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 05 · Slide Asli (17, 19, 20, 24)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch5">
          <button class="slide-pill active" onclick="setStage('ch5', 17, 'Slide 17 · Kriteria Diagnosis MAB', this)">Slide 17</button>
          <button class="slide-pill" onclick="setStage('ch5', 19, 'Slide 19 · Anamnesis', this)">Slide 19</button>
          <button class="slide-pill" onclick="setStage('ch5', 20, 'Slide 20 · Gejala Klinis', this)">Slide 20</button>
          <button class="slide-pill" onclick="setStage('ch5', 24, 'Slide 24 · Laboratorium &amp; Antropometri', this)">Slide 24</button>
        </div>
        <div class="stage-frame" onclick="openZoom(this.querySelector('img').src)">
          <img id="img-ch5" src="slides_emn_kul5/slide_17.jpg" alt="Slide 17 — kriteria diagnosis malnutrisi akut berat">
        </div>
        <div class="stage-caption" id="cap-ch5">Slide 17 · Kriteria Diagnosis MAB</div>
      </aside>
    </section>
"""

BAB6 = """
    <section class="split-chapter" id="bab-6">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 06 · Slide 25–41</span>
          <span class="meta-pill pill-uab">Tatalaksana</span>
        </div>
        <h2 class="ch-title">10 Langkah Tatalaksana: Urutannya Tidak Boleh Dibalik</h2>

        <div class="peer-talk">
          <p><b>Slide 25</b> adalah peta jalan seluruh terapi. Empat fase: <b>stabilisasi</b> (hari 1–2), <b>transisi</b> (hari 3–7), <b>rehabilitasi</b> (minggu 2–6), dan <b>tindak lanjut</b> (minggu 7–26). Sepuluh langkah dijalankan berurutan; hati-hati pada preparat besi yang sengaja <b>ditunda</b> sampai fase rehabilitasi.</p>
          <p>Prinsip yang menyatukan semuanya: <b>jangan mengejar berat badan lebih dulu</b>. Fase awal adalah menyelamatkan nyawa — gula darah, suhu, cairan, elektrolit, infeksi.</p>
        </div>

        <div class="cmp-wrap">
          <table class="cmp">
            <thead>
              <tr><th scope="col">Fase</th><th scope="col">Waktu</th><th scope="col">Yang dikerjakan</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Stabilisasi</th><td class="num-table">Hari 1–2</td><td>Hipoglikemia, hipotermia, dehidrasi, elektrolit, infeksi, mikronutrien (tanpa Fe), pemberian makan awal</td></tr>
              <tr><th scope="row">Transisi</th><td class="num-table">Hari 3–7</td><td>Lanjut elektrolit &amp; infeksi, mikronutrien tanpa Fe, pemberian makan dinaikkan</td></tr>
              <tr><th scope="row">Rehabilitasi</th><td class="num-table">Minggu 2–6</td><td>Mikronutrien <b>+ Fe</b>, tumbuh kejar, stimulasi sensoris, persiapan tindak lanjut</td></tr>
              <tr><th scope="row">Tindak lanjut</th><td class="num-table">Minggu 7–26</td><td>Tumbuh kejar berlanjut, stimulasi, pemantauan di rumah</td></tr>
            </tbody>
          </table>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Hipoglikemia &lt; 54 mg/dL (Slide 26)</h4>
            <ul>
              <li><b>Sadar</b>: larutan gula pasir/glukosa 10% oral atau NGT <b>50 ml</b></li>
              <li><b>Tidak sadar</b>: glukosa 10% IV <b>5 ml/kgBB</b>, lalu 50 ml oral/NGT</li>
              <li><b>Renjatan</b>: glukosa 10% IV 5 ml/kgBB, lalu RL + glukosa 5% (1:1) <b>15 ml/kgBB/jam</b></li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Hipotermia &lt; 36,5 °C (Slide 27–29)</h4>
            <ul>
              <li>Selalu dianggap bersama hipoglikemia dan infeksi — obati keduanya</li>
              <li>Hangatkan dengan metode <b>kanguru</b>, suhu ruang 25–30 °C</li>
              <li>Monitor suhu tiap <b>30 menit</b>; hentikan pemanasan saat 37 °C</li>
              <li>Jangan menghangatkan dengan air panas dalam botol</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Dehidrasi: ReSoMal (Slide 31)</h4>
            <ul>
              <li>5 ml/kg setiap 30 menit selama 2 jam pertama (oral/NGT)</li>
              <li>Lalu 5–10 ml/kg/jam selama 4–10 jam berikutnya</li>
              <li>Sudah terhidrasi → hentikan ReSoMal, lanjut <b>F75</b> tiap 2 jam</li>
              <li>Masih diare: &lt;2 tahun 50–100 ml, &gt;2 tahun 100–200 ml tiap diare</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Infeksi &amp; mikronutrien (Slide 35–36)</h4>
            <ul>
              <li>Amoksisilin 25 mg/kg/12 jam oral, 5 hari (rawat jalan, tanpa tanda infeksi)</li>
              <li>Dengan komplikasi: ampisilin 50 mg/kg IM/IV tiap 6 jam 2 hari → amoksisilin oral</li>
              <li>Vitamin A: 50.000 IU (0–5 bln), 100.000 IU (6–12 bln), 200.000 IU (&gt;12 bln)</li>
              <li>Zinc 2 mg/kg/hari, copper 0,3 mg/kg/hari, Fe 3 mg/kg/hari <b>di fase rehabilitasi</b></li>
            </ul>
          </div>
        </div>

        <div class="callout note-ok">
          <div class="callout-title">Diet bertingkat (Slide 38)</div>
          <b>Stabilisasi</b> 80–100 kkal/kgBB/hari, protein 1–1,5 g/kgBB/hari, cairan 130 ml/kgBB/hari (100 ml bila edema berat) → <b>F75</b>.
          <b>Transisi</b> 100–150 kkal, protein 2–3 g → <b>F100</b>.
          <b>Rehabilitasi</b> 150–220 kkal, protein 3–4 g → <b>F135</b>.
        </div>

        <div class="callout note-warn">
          <div class="callout-title"> Pemantauan &amp; kriteria pulang (Slide 39–41)</div>
          Timbang setiap pagi sebelum makan. Kenaikan &lt; 50 g/kgBB/minggu → kaji 4 sebab: asupan tidak
          adekuat, defisiensi zat gizi, infeksi/saluran cerna, masalah psikologik. Pulang bila mental
          membaik, suhu 36,5–37,5 °C, tanpa muntah/diare/edema, dan kenaikan BB &gt; 5 g/kgBB/hari
          selama 3 hari berturut-turut.
        </div>

        <div class="inline-quiz" id="iq-6">
          <div class="iq-kicker">Latihan Bab 6 · berbasis slide 26 &amp; 36</div>
          <div class="iq-stem">Anak MAB sadar, glukosa 40 mg/dL. Tindakan pertama yang tepat…</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-6', 0, false, 'Preparat besi justru ditunda sampai fase rehabilitasi.')"><span>A.</span><span>Beri preparat besi 3 mg/kgBB</span></button>
            <button class="iq-btn" onclick="ansInline('iq-6', 1, true, 'Sadar → larutan gula/glukosa 10% oral atau NGT 50 ml (Slide 26).')"><span>B.</span><span>Beri larutan glukosa 10% oral/NGT 50 ml</span></button>
            <button class="iq-btn" onclick="ansInline('iq-6', 2, false, 'Diuretik tidak dipakai; fokusnya koreksi glukosa lebih dulu.')"><span>C.</span><span>Beri diuretik untuk edema</span></button>
          </div>
          <div class="iq-fb" id="iq-6-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 06 · Slide Asli (25–41)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch6">
          <button class="slide-pill active" onclick="setStage('ch6', 25, 'Slide 25 · 10 Langkah Tatalaksana MAB', this)">Slide 25</button>
          <button class="slide-pill" onclick="setStage('ch6', 26, 'Slide 26 · Hipoglikemia', this)">Slide 26</button>
          <button class="slide-pill" onclick="setStage('ch6', 31, 'Slide 31 · Dehidrasi &amp; ReSoMal', this)">Slide 31</button>
          <button class="slide-pill" onclick="setStage('ch6', 36, 'Slide 36 · Koreksi Defisiensi Mikronutrien', this)">Slide 36</button>
          <button class="slide-pill" onclick="setStage('ch6', 38, 'Slide 38 · Kebutuhan Gizi per Fase', this)">Slide 38</button>
          <button class="slide-pill" onclick="setStage('ch6', 40, 'Slide 40 · Kriteria Pemulangan', this)">Slide 40</button>
        </div>
        <div class="stage-frame" onclick="openZoom(this.querySelector('img').src)">
          <img id="img-ch6" src="slides_emn_kul5/slide_25.jpg" alt="Slide 25 — 10 langkah tatalaksana malnutrisi akut berat">
        </div>
        <div class="stage-caption" id="cap-ch6">Slide 25 · 10 Langkah Tatalaksana MAB</div>
      </aside>
    </section>
"""

TRYOUT = """
    <section class="tryout-section" id="tryout-akhir">
      <div class="tryout-head">
        <div>
          <div class="ch-kicker">Tryout · 8 soal</div>
          <h2 style="font-family:var(--font-serif);font-size:2rem;color:var(--ink);margin-top:6px;">Latihan Berbasis Slide — Bukan Arsip UAB EMN</h2>
          <p style="color:var(--ink-secondary);max-width:64ch;margin-top:8px;font-size:0.95rem;">
            Belum ada berkas soal UAB untuk Blok 9 (EMN) di arsip. Semua soal di bawah disusun
            <b>langsung dari isi 42 slide dr. Ditya</b> dan diberi label sumbernya. Jangan menganggapnya
            soal asli UAB.
          </p>
        </div>
        <div class="tryout-score" id="tryout-score">0 / 8</div>
      </div>
      <div id="tryout-list"></div>
    </section>
"""

FOOTER = """
  </main>

  <footer style="max-width:1240px;margin:40px auto 60px;padding:0 28px;color:var(--ink-muted);font-size:0.82rem;line-height:1.7;">
    <div style="border-top:1px solid var(--border);padding-top:18px;display:flex;flex-wrap:wrap;gap:8px 18px;justify-content:space-between;">
      <span>EMN KUL 5 · Malnutrisi Energi Protein — dr. Ditya Arisanti, Sp.A · 42 slide</span>
      <span>Disusun dari slide asli. Bukan pengganti kuliah atau penilaian klinis.</span>
    </div>
  </footer>

  <div class="lightbox" id="lightbox" onclick="if(event.target===this) closeZoom()">
    <img id="lightbox-img" src="" alt="Slide diperbesar">
  </div>
"""

TRYOUT_JS = """
    const TRYOUT_Q = [
      {
        stem: '1. Definisi Malnutrisi Energi Protein menurut slide adalah…',
        opts: ['Defisiensi energi dan protein, umumnya disertai kekurangan zat gizi lain',
               'Kelebihan energi yang menyebabkan obesitas',
               'Kekurangan satu jenis vitamin saja',
               'Kegagalan absorbsi karbohidrat di usus halus',
               'Kelebihan protein yang membebani ginjal'],
        ans: 0,
        exp: 'Slide 6: MEP adalah defisiensi/kekurangan energi dan protein, umumnya disertai kekurangan zat gizi lainnya.'
      },
      {
        stem: '2. Menurut Permenkes No. 29/2019, gizi buruk ditandai dengan…',
        opts: ['BB/U antara −2 dan −3 SD',
               'Sangat kurus, disertai atau tidak disertai edema',
               'TB/U antara −2 dan −3 SD',
               'LILA 13–14 cm',
               'BB/U di atas median'],
        ans: 1,
        exp: 'Slide 7: gizi buruk = keadaan sangat kurus, disertai atau tidak edema. Gizi kurang = −3 s.d. −2 SD.'
      },
      {
        stem: '3. Balita dengan edema pitting, rambut merah mudah dicabut, hepatomegali, dan albumin rendah. Gambaran ini khas untuk…',
        opts: ['Marasmus', 'Kwashiorkor', 'Stunting murni', 'Obesitas', 'Defisiensi vitamin A saja'],
        ans: 1,
        exp: 'Slide 21: edema, dermatosis, rambut seperti jagung, hepatomegali, dan albumin rendah adalah tanda kwashiorkor.'
      },
      {
        stem: '4. Skor McLaren seorang anak: edema (3), dermatosis (2), rambut berubah (1), albumin 2,2 g/dL (4). Bentuk klinisnya…',
        opts: ['Marasmus (0–3)', 'Kwashiorkor marasmik (4–8)', 'Kwashiorkor (9–15)', 'Normal', 'Tidak dapat dinilai'],
        ans: 2,
        exp: '3+2+1+4 = 10 → rentang 9–15 = kwashiorkor (Slide 12).'
      },
      {
        stem: '5. Sistem klasifikasi yang dapat membedakan wasting dari stunting adalah…',
        opts: ['Gomez', 'Wellcome', 'Waterlow', 'McLaren', 'Broca'],
        ans: 2,
        exp: 'Slide 11: Waterlow memakai TB/U dan BB/TB sehingga bisa membedakan wasting dan stunting; Gomez hanya BB/U.'
      },
      {
        stem: '6. Anak MAB sadar dengan glukosa darah 40 mg/dL. Tindakan yang tepat adalah…',
        opts: ['Glukosa 10% IV 5 ml/kgBB segera',
               'Larutan gula pasir/glukosa 10% oral atau NGT 50 ml',
               'Preparat besi 3 mg/kgBB',
               'Diuretik IV',
               'Transfusi albumin'],
        ans: 1,
        exp: 'Slide 26: bila sadar (tidak letargis) → larutan gula/glukosa 10% oral/NGT 50 ml. IV 5 ml/kgBB untuk yang tidak sadar.'
      },
      {
        stem: '7. Cairan rehidrasi khusus untuk malnutrisi akut berat adalah…',
        opts: ['Ringer laktat tanpa modifikasi', 'ReSoMal', 'NaCl 0,9%', 'Dextrose 5%', 'Albumin 20%'],
        ans: 1,
        exp: 'Slide 31: ReSoMal (Rehydration Solution for Malnutrition), 5 ml/kg tiap 30 menit selama 2 jam pertama.'
      },
      {
        stem: '8. Kapan preparat besi (Fe) mulai diberikan pada tatalaksana MAB?',
        opts: ['Sejak hari pertama stabilisasi', 'Bersamaan dengan antibiotik', 'Saat memasuki fase rehabilitasi, setelah nafsu makan membaik', 'Setelah pulang', 'Tidak pernah diberikan'],
        ans: 2,
        exp: 'Slide 25 & 36: Fe ditunda; diberikan saat fase rehabilitasi, ketika nafsu makan membaik dan BB mulai bertambah.'
      }
    ];
"""

# --------------------------------------------------------------------------- assembly
def build(outdir: str) -> str:
    css = ambil_css(REF) + CSS_TAMBAHAN
    html = f"""<!DOCTYPE html>
<html lang="id" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Malnutrisi Energi Protein · Split-Screen Mastery EMN KUL 5</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">
  <style>
{css}
  </style>
</head>
<body>
  <div class="scroll-bar" id="scroll-bar"></div>

  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-group">
        <span class="brand-badge">EMN · KUL 5</span>
        <select class="course-select" onchange="window.location.href=this.value">
          <option value="EMN_KUL5_Malnutrisi.html" selected>Blok 9 EMN · KUL 5: Malnutrisi (dr. DTY)</option>
          <option value="EMN_KUL3_Defisiensi_Mineral.html">Blok 9 EMN · KUL 3: Defisiensi Mineral (dr. IWL)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html">Blok 9 EMN · KUL 2: Defisiensi Vitamin (dr. IWL)</option>
          <option value="HI_KUL20_Autoimunitas.html">Blok 8 HI · KUL 20: Autoimunitas (dr. LIA)</option>
          <option value="BDT_KUL3_Patient_Safety.html">Blok 7 BDT · KUL 3: Patient Safety (dr. KI)</option>
        </select>
      </div>

      <nav class="chapter-strip" aria-label="Lompat ke Bab">
        <a href="#bab-1" class="ch-jump active">1. Definisi</a>
        <a href="#bab-2" class="ch-jump">2. Marasmus/Kwashiorkor</a>
        <a href="#bab-3" class="ch-jump">3. Skor</a>
        <a href="#bab-4" class="ch-jump">4. Patofisiologi</a>
        <a href="#bab-5" class="ch-jump">5. Diagnosis</a>
        <a href="#bab-6" class="ch-jump">6. 10 Langkah</a>
        <a href="#tryout-akhir" class="ch-jump">🎯 8 Soal Latihan</a>
      </nav>

      <div class="tool-group">
        <button type="button" id="cloze-btn" class="tool-btn" onclick="toggleCloze()" title="Shortcut M">
          <span>🧠 Uji Ingatan</span>
          <span class="state-pill" id="cloze-state">OFF</span>
        </button>
        <button type="button" id="theme-btn" class="tool-btn" onclick="toggleTheme()" title="Shortcut D">
          <span id="theme-label">🌙 Mode Malam</span>
        </button>
        <a href="anki/VERTEX_EMN_KUL5_Malnutrisi.apkg" class="btn-anki" download>⬇ Anki</a>
      </div>
    </div>
  </header>

  <main class="page-wrap">
{HERO}
{BAB1}
{BAB2}
{BAB3}
{BAB4}
{BAB5}
{BAB6}
{TRYOUT}
{FOOTER}

  <script>
    const MISTERY = {{
      1: '<b>Kwashiorkor.</b> Edema pitting, rambut merah mudah dicabut, moon face, dan albumin 1,8 g/dL adalah gambaran khas (Slide 21). Kuncinya: BB/U bisa tampak "cukup" karena edema — jangan pakai BB/U saja.',
      2: '<b>Marasmus.</b> Kehilangan massa otot dan lemak subkutan tanpa edema. Prognosisnya relatif lebih baik karena anak masih mau makan (Slide 21).',
      3: '<b>Hipoglikemia, langkah 1.</b> Glukosa &lt;54 mg/dL. Anak sadar → larutan gula pasir/glukosa 10% oral atau NGT 50 ml. Bila tidak sadar → glukosa 10% IV 5 ml/kgBB (Slide 26).'
    }};

    function showMystery(n) {{
      const box = document.getElementById('mystery-box');
      box.innerHTML = MISTERY[n];
      box.classList.add('show');
    }}

    function setStage(ch, n, label, btn) {{
      const img = document.getElementById('img-' + ch);
      img.src = 'slides_emn_kul5/slide_' + n + '.jpg';
      img.alt = label;
      document.getElementById('cap-' + ch).innerHTML = label;
      const pills = btn.parentElement.querySelectorAll('.slide-pill');
      pills.forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
    }}

    function ansInline(id, idx, isRight, reason) {{
      const wrap = document.getElementById(id);
      wrap.querySelectorAll('.iq-btn').forEach((b, i) => {{
        b.classList.remove('is-correct', 'is-wrong');
        if (i === idx) b.classList.add(isRight ? 'is-correct' : 'is-wrong');
        else if (b.dataset.right === '1') b.classList.add('is-correct');
      }});
      const fb = document.getElementById(id + '-fb');
      fb.className = 'iq-fb show ' + (isRight ? 'ok' : 'no');
      fb.innerHTML = (isRight ? '<strong>✅ Benar!</strong> ' : '<strong>❌ Kurang tepat.</strong> ') + reason;
    }}

    let clozeOn = false;
    function toggleCloze() {{
      clozeOn = !clozeOn;
      document.body.classList.toggle('cloze-active', clozeOn);
      document.getElementById('cloze-btn').classList.toggle('active', clozeOn);
      document.getElementById('cloze-state').textContent = clozeOn ? 'ON' : 'OFF';
      if (clozeOn) document.querySelectorAll('.cloze-mask').forEach(e => e.classList.remove('revealed'));
    }}

    function toggleTheme() {{
      const root = document.documentElement;
      const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      document.getElementById('theme-label').textContent = next === 'dark' ? '☀️ Mode Kertas' : '🌙 Mode Malam';
      try {{ localStorage.setItem('vx_emn_theme', next); }} catch (e) {{}}
    }}

    function openZoom(src) {{
      document.getElementById('lightbox-img').src = src;
      document.getElementById('lightbox').classList.add('open');
    }}
    function closeZoom() {{
      document.getElementById('lightbox').classList.remove('open');
    }}

    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') closeZoom();
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;
      if (e.key.toLowerCase() === 'm') toggleCloze();
      if (e.key.toLowerCase() === 'd') toggleTheme();
    }});

    {TRYOUT_JS}

    let tryoutAns = {{}};
    let tryoutScore = 0;

    function initTryout() {{
      document.getElementById('tryout-list').innerHTML = TRYOUT_Q.map((q, qi) => `
        <div class="inline-quiz" id="tq-${{qi}}" style="border-top:1px solid var(--border);margin-top:18px;padding-top:18px;">
          <div class="iq-stem">${{q.stem}}</div>
          <div class="iq-opts">
            ${{q.opts.map((o, oi) => `
              <button type="button" class="iq-btn" onclick="ansTryout(${{qi}}, ${{oi}})">
                <span>${{String.fromCharCode(65 + oi)}}.</span><span>${{o}}</span>
              </button>`).join('')}}
          </div>
          <div class="iq-fb" id="tq-fb-${{qi}}"></div>
        </div>`).join('');
    }}

    function ansTryout(qi, oi) {{
      if (tryoutAns[qi] !== undefined) return;
      tryoutAns[qi] = oi;
      const q = TRYOUT_Q[qi];
      const ok = (oi === q.ans);
      if (ok) tryoutScore++;
      document.getElementById('tryout-score').textContent = tryoutScore + ' / ' + TRYOUT_Q.length;
      const wrap = document.getElementById('tq-' + qi);
      wrap.querySelectorAll('.iq-btn').forEach((b, i) => {{
        if (i === q.ans) b.classList.add('is-correct');
        else if (i === oi && !ok) b.classList.add('is-wrong');
      }});
      const fb = document.getElementById('tq-fb-' + qi);
      fb.className = 'iq-fb show ' + (ok ? 'ok' : 'no');
      fb.innerHTML = (ok ? '<strong>✅ Benar!</strong> ' : '<strong>❌ Belum tepat.</strong> ') + q.exp;
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      initTryout();
      const chapters = [...document.querySelectorAll('.split-chapter')];
      const navLinks = [...document.querySelectorAll('.ch-jump')];
      window.addEventListener('scroll', () => {{
        const doc = document.documentElement;
        const pct = (doc.scrollTop / Math.max(1, doc.scrollHeight - doc.clientHeight)) * 100;
        document.getElementById('scroll-bar').style.width = pct + '%';
        let currentId = 'bab-1';
        for (const sec of chapters) if (sec.getBoundingClientRect().top <= 160) currentId = sec.id;
        navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + currentId));
      }}, {{ passive: true }});
      try {{ if (localStorage.getItem('vx_emn_theme') === 'dark') toggleTheme(); }} catch (e) {{}}
    }});
  </script>
</body>
</html>
"""
    out = os.path.join(outdir, "EMN_KUL5_Malnutrisi.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    return out


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else HERE
    p = build(target)
    print("html:", p, os.path.getsize(p) // 1024, "KB")
