import os
import shutil

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
DOCS_DIR = os.path.join(BASE_DIR, "docs")
os.makedirs(DOCS_DIR, exist_ok=True)

# Symlink or copy slide folders into docs/ so mkdocs bundles them cleanly
for folder in ["slides_bdt_kul3", "slides_kul2", "anki"]:
    src = os.path.join(BASE_DIR, folder)
    dst = os.path.join(DOCS_DIR, folder)
    if os.path.exists(src) and not os.path.exists(dst):
        shutil.copytree(src, dst)

# Create extra CSS & JS for Markmap + clean medical styling
os.makedirs(os.path.join(DOCS_DIR, "stylesheets"), exist_ok=True)
os.makedirs(os.path.join(DOCS_DIR, "javascripts"), exist_ok=True)

with open(os.path.join(DOCS_DIR, "stylesheets", "extra.css"), "w", encoding="utf-8") as f:
    f.write("""
:root {
  --md-primary-fg-color: #0F5C4D;
  --md-primary-fg-color--light: #167A67;
  --md-primary-fg-color--dark: #0A4036;
  --md-accent-fg-color: #0F5C4D;
}
.md-typeset h1 {
  font-weight: 700;
  letter-spacing: -0.02em;
}
.md-typeset h2 {
  font-weight: 700;
  border-bottom: 1px solid rgba(15, 92, 77, 0.15);
  padding-bottom: 0.35rem;
}
.slide-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 16px;
  margin: 12px 0;
}
.slide-card {
  border: 1px solid rgba(0,0,0,0.12);
  border-radius: 8px;
  padding: 10px;
  background: var(--md-code-bg-color);
}
.slide-card img {
  border-radius: 6px;
  width: 100%;
  display: block;
}
.slide-caption {
  font-size: 0.75rem;
  font-weight: 600;
  margin-top: 6px;
  opacity: 0.85;
}
.markmap-box {
  width: 100%;
  height: 380px;
  border: 1px solid rgba(0,0,0,0.12);
  border-radius: 10px;
  background: var(--md-default-bg-color);
  margin: 14px 0;
}
.markmap-box > svg {
  width: 100%;
  height: 100%;
}
""")

with open(os.path.join(DOCS_DIR, "javascripts", "init_diagrams.js"), "w", encoding="utf-8") as f:
    f.write("""
document$.subscribe(function() {
  if (window.mermaid) {
    window.mermaid.initialize({ startOnLoad: true, theme: 'default', securityLevel: 'loose' });
    window.mermaid.run({ querySelector: '.mermaid' });
  }
});
""")

MKDOCS_YML = """site_name: VERTEX-PREP · FKIK UIN Malang (Angkatan 2025)
site_description: Platform Belajar Kedokteran Visual & Terbukti Slide Tanpa Perlu Buka PPT
site_url: http://localhost:8765/

theme:
  name: material
  language: id
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: custom
      accent: teal
      toggle:
        icon: material/weather-night
        name: Beralih ke Mode Malam
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: teal
      toggle:
        icon: material/weather-sunny
        name: Beralih ke Mode Terang
  font:
    text: Plus Jakarta Sans
    code: JetBrains Mono
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - navigation.Instant
    - navigation.tracking
    - toc.follow
    - search.suggest
    - search.highlight
    - content.tabs.link

plugins:
  - search:
      lang: id
  - glightbox:
      touchNavigation: true
      loop: false
      effect: zoom
      slide_effect: slide
      width: 100%
      height: auto
      zoomable: true
      draggable: true
  - quiz:
      enabled: true
      show_correct: true
      auto_number: true

markdown_extensions:
  - admonition
  - attr_list
  - md_in_html
  - tables
  - def_list
  - pymdownx.details
  - pymdownx.mark
  - pymdownx.critic
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format

extra_css:
  - stylesheets/extra.css

extra_javascript:
  - https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js
  - https://cdn.jsdelivr.net/npm/markmap-autoloader@0.18
  - javascripts/init_diagrams.js

nav:
  - Beranda: index.md
  - Blok 7 (BDT) · Patient Safety: bdt-kul3-patient-safety.md
  - Blok 9 (EMN) · Defisiensi Vitamin: emn-kul2-defisiensi-vitamin.md
"""

with open(os.path.join(BASE_DIR, "mkdocs.yml"), "w", encoding="utf-8") as f:
    f.write(MKDOCS_YML)

# ==============================================================================
# 1. DOCS/INDEX.MD
# ==============================================================================
INDEX_MD = """# Portal Belajar Visual VERTEX-PREP

Selamat datang di ruang belajar **Angkatan 2025 (VERTEX) — FKIK UIN Maulana Malik Ibrahim Malang**. Sistem ini dibangun di atas kombinasi *open-source* terbaik yang paling banyak dipakai untuk *Medical Digital Garden* di GitHub:

- **`squidfunk/mkdocs-material`** *(22.000+ GitHub Stars)* — Navigasi 3 kolom bersih, daftar isi otomatis di kanan, pencarian instan (`/`), dan mode Siang/Malam.
- **`mermaid-js/mermaid` & `markmap/markmap`** — Mengubah isi PPT yang panjang menjadi diagram alur vektor & *mindmap* interaktif yang bisa di-*zoom*.
- **`blueswen/mkdocs-glightbox`** — Bukti tangkapan layar slide asli dosen tersimpan rapi di tab pendamping dan bisa diperbesar secara mulus dengan 1 klik.
- **`ewels/mkdocs-quiz`** — Latihan soal pilihan ganda interaktif langsung di bawah materi, lengkap dengan penjelasan per opsi dan bukti slide dosen.

---

## Pilih Modul Kuliah yang Tersedia

<div class="grid cards" markdown>

-   **Blok 7 (BDT) · Kuliah 3: Patient Safety**

    ---

    Memadatkan **80 slide dr. Riskiyah, MMRS** menjadi **7 Bab Diagram Alur Vektor** + **9 Soal Asli UAB & Remidi BDT** yang terbukti 100% keluar dari 14 slide inti.

    [:octicons-arrow-right-24: Mulai Belajar BDT Kuliah 3](bdt-kul3-patient-safety.md)

-   **Blok 9 (EMN) · Kuliah 2: Defisiensi Vitamin**

    ---

    Memadatkan **28 slide dr. Iwal Reza Ahdi, Sp.PD** menjadi **6 Bab Diagram Metabolik & Klinis** + **6 Soal Interaktif** (3 Kasus Diskusi Asli Slide + 3 Prediksi).

    [:octicons-arrow-right-24: Mulai Belajar EMN Kuliah 2](emn-kul2-defisiensi-vitamin.md)

</div>

---

## Peta Besar Ekosistem Kuliah (Interactive Mindmap `Markmap`)

*Geser (drag) dan scroll pada kotak di bawah untuk memperbesar atau melipat cabang materi:*

<div class="markmap-box">
<div class="markmap">
<script type="text/template">
# VERTEX-PREP FKIK UIN Malang
## Blok 7: BDT
- Kuliah 3: Patient Safety (80 Slide)
  - Bab 1: 5 Jenis Insiden (KPC, KNC, KTC, KTD, Sentinel)
  - Bab 2: 7 Standar vs 6 SKP vs 7 Langkah
  - Bab 3: SKP 1 Identifikasi & 4 Gelang Pasien
  - Bab 4: SKP 2 Komunikasi TBaK & SBAR
  - Bab 5: SKP 3 Obat High-Alert & KCl Pekat
  - Bab 6: SKP 4 Operasi Aman & Time-Out
  - Bab 7: SKP 5-6, Lapor 2x24 Jam & RCA
  - 9 Soal Asli UAB & Remidi BDT
## Blok 9: EMN (Semester 3 Aktif)
- Kuliah 2: Defisiensi Vitamin (28 Slide)
  - Bab 1: 4 Jalur Etiologi & Obat (Metformin, INH, Warfarin)
  - Bab 2: Vitamin A (Retinal vs Retinoat & Bercak Bitot)
  - Bab 3: Vitamin D (25-OH-D vs 1,25-OH2-D), E, & K
  - Bab 4: Vitamin B1 (Tiamin/Wernicke), B2, B3 (Pellagra), B6
  - Bab 5: Pembeda B9 (Folat) vs B12 (MMA & Neuropati)
  - Bab 6: Pembeda Skorbut (Vit C) vs Defisiensi Vit K
</script>
</div>
</div>
"""

with open(os.path.join(DOCS_DIR, "index.md"), "w", encoding="utf-8") as f:
    f.write(INDEX_MD)

# ==============================================================================
# 2. DOCS/BDT-KUL3-PATIENT-SAFETY.MD
# ==============================================================================
BDT_MD = """# Blok 7 (BDT) · Kuliah 3: Patient Safety (Keselamatan Pasien)

**Dosen Pengampu:** dr. Riskiyah, MMRS · **Sumber Asli:** 80 Slide PPT · **Rekam Jejak Ujian:** 9 Soal Asli UAB & Remidi BDT

!!! success "Belajar Tuntas Tanpa Perlu Buka File PPT"
    Seluruh isi **80 slide** telah dirangkum menjadi **Mindmap Interaktif + 7 Bab Diagram Vektor (`Mermaid.js`)** di bawah ini. Jika Anda ingin memverifikasi gambar slide aslinya, cukup klik tab **"Bukti Slide Asli Dosen"** di setiap bab (klik gambar untuk *zoom* layar penuh).

---

## Peta Konsep Utuh 1 Kuliah (Interactive `Markmap`)

*Klik titik lingkaran pada cabang untuk melipat/membuka topik, atau scroll untuk memperbesar:*

<div class="markmap-box">
<div class="markmap">
<script type="text/template">
# Patient Safety (dr. Riskiyah)
## 1. Lima Jenis Insiden (Slide 18)
- KPC: Kondisi potensial (alat rusak/lantai licin), belum insiden
- KNC (Near Miss): Salah tindakan, BELUM kena pasien (UAB BDT-1)
- KTC: SUDAH kena pasien, TIDAK timbul cedera
- KTD: SUDAH kena pasien, TIMBUL cedera
- Sentinel: Kematian / Cacat berat / Salah sisi operasi (UAB No.29 & 70)
## 2. Tiga Kerangka Utama
- 7 Standar (Slide 23-24): Kata Benda (Hak Pasien, Peran Kepemimpinan)
- 6 SKP (Slide 32-33): 6 Sasaran Klinis (Identifikasi s.d. Risiko Jatuh)
- 7 Langkah (Slide 61): Kata Kerja Aktif (Membangun, Memimpin, Mengembangkan)
## 3. Enam Sasaran Keselamatan Pasien (SKP 1-6)
- SKP 1: Min. 2 dari 4 Identitas + 4 Warna Gelang (Biru, Pink, Merah, Kuning)
- SKP 2: Komunikasi Telepon TBaK (konfirmasi 1x24 jam) & SBAR
- SKP 3: Obat High-Alert (KCl Pekat, LASA) -> Label HIGH ALERT!
- SKP 4: Surgical Marking (pasien sadar) + Time-Out sebelum insisi
- SKP 5: 5 Moments Hand Hygiene WHO & Injeksi Aman
- SKP 6: Skrining Jatuh (Morse/Humpty Dumpty) & Gelang Kuning
## 4. Pelaporan & Investigasi (Slide 69-75)
- Laporan Internal: Maksimal 2 x 24 Jam (Rahasia & Non-Punitive)
- Grading Biru / Hijau: Investigasi Sederhana (1-2 minggu)
- Grading Kuning / Merah: Root Cause Analysis / RCA (Maks 45 hari)
</script>
</div>
</div>

---

## Bab 1 · Tangga 5 Insiden Keselamatan Pasien (Slide 1–22)

=== "Intisari & Diagram Alur Visual"

    Untuk menjawab soal kasus insiden di UAB tanpa pernah salah, ikuti diagram pohon keputusan 2 langkah dari **Slide 18** berikut:

    ```mermaid
    flowchart LR
        A["Kondisi / Kesalahan Medis"] --> B{"Sudah ada tindakan salah?"}
        B -- "Belum (Baru kondisi bahaya,\nmisal alat rusak / lantai licin)" --> KPC["1. KPC\n(Kejadian Potensial Cedera)"]
        B -- "Sudah terjadi kesalahan" --> C{"Sudah terpapar ke tubuh pasien?"}
        C -- "BELUM (Ketahuan sebelum\ndiberikan ke pasien)" --> KNC["2. KNC / Near Miss\n(Kejadian Nyaris Cedera)\n★ Soal UAB BDT-1"]
        C -- "SUDAH mengenai pasien" --> D{"Timbul cedera pada pasien?"}
        D -- "TIDAK ada cedera" --> KTC["3. KTC\n(Kejadian Tidak Cedera)"]
        D -- "ADA cedera klinis" --> E{"Meninggal / Cacat Permanen?"}
        E -- "Cedera ringan-sedang\n(Reversibel)" --> KTD["4. KTD / Adverse Event\n(Kejadian Tidak Diharapkan)"]
        E -- "MENINGGAL / Cacat Berat /\nSalah Sisi Operasi" --> SENT["5. KEJADIAN SENTINEL\n★ Soal UAB No. 29 & No. 70"]
    ```

    * **Prinsip Dasar (`Slide 19–20`)**: *Being Safe Means Do No Harm*. Empat tujuan utamanya adalah membangun budaya keselamatan, meningkatkan akuntabilitas RS, menurunkan angka KTD, dan melaksanakan program pencegahan sehingga tidak terjadi pengulangan.
    * **3 Kasus Latihan di Slide Dosen (`Slide 18–19`)**:
        1. *Bayi tertukar saat diserahkan ke ibu pasca-persalinan* $\rightarrow$ **Kejadian Sentinel**.
        2. *Salah dosis obat KCl IV sehingga pasien meninggal* $\rightarrow$ **Kejadian Sentinel**.
        3. *Dokter salah tulis dosis obat, farmasi sudah siapkan, tapi ketahuan perawat sebelum disuntikkan ke pasien* $\rightarrow$ **KNC (Kejadian Nyaris Cedera)**.

    !!! danger "Jebakan Soal Asli UAB BDT (No. 29 & UAB 22 No. 70)"
        Jika di soal diceritakan pasien mendapat suntikan obat (misal Antalgin) lalu mengalami **syok anafilaktik hingga meninggal dunia**, jangan pilih KTD biasa! Karena berujung **kematian**, sesuai definisi baris terakhir Slide 18 jawabannya mutlak **Kejadian Sentinel**.

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_18.jpg" class="glightbox" data-gallery="bdt-b1" data-title="Slide 18 · Definisi Resmi 5 Insiden (KTD, KNC, KTC, KPC, Sentinel)">
          <img src="slides_bdt_kul3/slide_18.jpg" alt="Slide 18" />
        </a>
        <div class="slide-caption">Slide 18 · Definisi 5 Insiden (Sumber 3 Soal UAB)</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_19.jpg" class="glightbox" data-gallery="bdt-b1" data-title="Slide 19 · Prinsip Utama: Do No Harm">
          <img src="slides_bdt_kul3/slide_19.jpg" alt="Slide 19" />
        </a>
        <div class="slide-caption">Slide 19 · Prinsip Utama: Do No Harm</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_20.jpg" class="glightbox" data-gallery="bdt-b1" data-title="Slide 20 · 4 Tujuan Patient Safety di Rumah Sakit">
          <img src="slides_bdt_kul3/slide_20.jpg" alt="Slide 20" />
        </a>
        <div class="slide-caption">Slide 20 · 4 Tujuan Patient Safety</div>
      </div>
    </div>

---

## Bab 2 · Pembeda 7 Standar vs 6 SKP vs 7 Langkah (Slide 23–33 & 61)

=== "Tabel Pembeda & Cara Hafal 5 Detik"

    Di UAB BDT, dosen mengeluarkan **2 soal berbeda (`Axonation No. 32` & `No. 44`)** yang menanyakan isi **7 Standar Keselamatan Pasien**, lalu mengambil opsi pengecohnya dari **7 Langkah Menuju Keselamatan Pasien (`Slide 61`)**.

    | Urutan | 7 Standar Keselamatan Pasien (`Slide 23–24`)<br>*Ciri: Diawali KATA BENDA* | 6 Sasaran Keselamatan Pasien / SKP (`Slide 32–33`)<br>*Ciri: 6 Prosedur Klinis* | 7 Langkah Menuju Keselamatan Pasien (`Slide 61`)<br>*Ciri: Diawali KATA KERJA AKTIF* |
    | :--- | :--- | :--- | :--- |
    | **1** | ==**Hak pasien**== *(Keluar di UAB No. 44)* | Ketepatan identifikasi pasien | **Membangun** kesadaran akan nilai keselamatan |
    | **2** | **Pendidikan** bagi pasien dan keluarga | Peningkatan komunikasi yang efektif | **Memimpin** dan mendukung staf *(Pengecoh UAB!)* |
    | **3** | **Keselamatan pasien** dalam kesinambungan pelayanan | Peningkatan keamanan obat yang perlu diwaspadai | **Mengintegrasikan** aktivitas pengelolaan risiko |
    | **4** | **Penggunaan metode** peningkatan kinerja untuk evaluasi | Kepastian tepat-lokasi, tepat-prosedur, tepat-pasien operasi | **Mengembangkan** sistem pelaporan *(Pengecoh UAB!)* |
    | **5** | ==**Peran kepemimpinan**== dalam meningkatkan keselamatan *(UAB No. 32)* | Pengurangan risiko infeksi terkait pelayanan kesehatan | **Melibatkan** dan berkomunikasi dengan pasien |
    | **6** | **Pendidikan** bagi staf tentang keselamatan pasien | Pengurangan risiko cedera pasien akibat terjatuh | **Belajar** dan berbagi pengalaman (RCA) |
    | **7** | **Komunikasi** merupakan kunci bagi staf | *— (Hanya 6 Sasaran)* | **Mencegah** cedera melalui implementasi sistem |

    !!! tip "Rumus Cepat Membedakan di Ruang Ujian"
        - Bila soal menanyakan **7 Standar** $\rightarrow$ cari opsi yang bunyinya **Kata Benda**: **"Hak pasien"** atau **"Peran kepemimpinan dalam meningkatkan keselamatan pasien"**.
        - Bila opsi diawali akhiran kerja ***Me-*** (*Membangun, Memimpin, Mengintegrasikan, Mengembangkan, Melibatkan, Mencegah*) $\rightarrow$ itu pasti **7 Langkah (`Slide 61`)**, bukan 7 Standar!

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_23.jpg" class="glightbox" data-gallery="bdt-b2" data-title="Slide 23 · 7 Standar Keselamatan Pasien (Standar 1–4)">
          <img src="slides_bdt_kul3/slide_23.jpg" alt="Slide 23" />
        </a>
        <div class="slide-caption">Slide 23 · 7 Standar (Nomor 1: Hak Pasien)</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_24.jpg" class="glightbox" data-gallery="bdt-b2" data-title="Slide 24 · 7 Standar Keselamatan Pasien (Standar 5–7)">
          <img src="slides_bdt_kul3/slide_24.jpg" alt="Slide 24" />
        </a>
        <div class="slide-caption">Slide 24 · 7 Standar (Nomor 5: Peran Kepemimpinan)</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_61.jpg" class="glightbox" data-gallery="bdt-b2" data-title="Slide 61 · 7 Langkah Keselamatan Pasien (Sumber Pengecoh Opsi UAB)">
          <img src="slides_bdt_kul3/slide_61.jpg" alt="Slide 61" />
        </a>
        <div class="slide-caption">Slide 61 · 7 Langkah (Pengecoh Soal Standar)</div>
      </div>
    </div>

---

## Bab 3 · SKP 1: Ketepatan Identifikasi & 4 Warna Gelang (Slide 32, 34–38)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart TD
        ID["SKP 1: Ketepatan Identifikasi Pasien\n(Wajib Minimal 2 dari 4 Identitas Resmi)"] --> P1["1. Nama Lengkap Pasien"]
        ID --> P2["2. Tanggal Lahir"]
        ID --> P3["3. Nomor Rekam Medis (No. RM)"]
        ID --> P4["4. Nomor Induk Kependudukan (NIK)"]
        ID -. "DILARANG KERAS!" .-> NO["❌ Nomor Kamar / Nomor Tempat Tidur"]

        GEL["4 Warna Gelang Pasien (Slide 35)"] --> GB["🔵 Gelang Biru:\nIdentitas Laki-Laki"]
        GEL --> GP["🩷 Gelang Pink:\nIdentitas Perempuan"]
        GEL --> GM["🔴 Gelang Merah:\nRiwayat Alergi Tinggi"]
        GEL --> GK["🟡 Gelang Kuning:\nRisiko Jatuh Tinggi"]
    ```

    * **Cara Bertanya yang Benar (`Slide 34`)**: Wajib menggunakan **pertanyaan terbuka (verbal aktif)**: *"Siapa nama Bapak?"* dan *"Kapan tanggal lahir Bapak?"*. Dilarang bertanya tertutup (*"Apakah Bapak Tn. Budi?"*) karena pasien yang mengantuk atau gangguan pendengaran bisa mengangguk meski salah orang.
    * **4 Saat Wajib Verifikasi Identitas (`Slide 37`)**:
        1. Sebelum pemberian obat (oral maupun injeksi).
        2. Sebelum transfusi darah / produk darah.
        3. Sebelum pengambilan darah / spesimen pemeriksaan klinis.
        4. Sebelum melakukan tindakan medis / prosedur operasi.

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_35.jpg" class="glightbox" data-gallery="bdt-b3" data-title="Slide 35 · Foto Gelang Merah (Alergi), Kuning (Risiko Jatuh), Biru (Laki-laki)">
          <img src="slides_bdt_kul3/slide_35.jpg" alt="Slide 35" />
        </a>
        <div class="slide-caption">Slide 35 · Foto Gelang Merah, Kuning, Biru</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_34.jpg" class="glightbox" data-gallery="bdt-b3" data-title="Slide 34 · Aturan Minimal 2 Identitas & Pertanyaan Terbuka">
          <img src="slides_bdt_kul3/slide_34.jpg" alt="Slide 34" />
        </a>
        <div class="slide-caption">Slide 34 · Aturan 2 Identitas & Cara Bertanya</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_37.jpg" class="glightbox" data-gallery="bdt-b3" data-title="Slide 37 · 4 Momen Wajib Identifikasi Pasien">
          <img src="slides_bdt_kul3/slide_37.jpg" alt="Slide 37" />
        </a>
        <div class="slide-caption">Slide 37 · 4 Momen Wajib Identifikasi</div>
      </div>
    </div>

---

## Bab 4 · SKP 2: Komunikasi Efektif TBaK & SBAR (Slide 39–42)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart LR
        S1["1. TULIS LENGKAP\n(Write Down)\nCatat nama obat, dosis,\nrute, & frekuensi di RM"] --> S2["2. BACA ULANG\n(Read Back)\nPerawat membacakan ulang;\nobat LASA wajib DIEJA"]
        S2 --> S3["3. KONFIRMASI 1x24 JAM\n(Confirmation)\nDPJP wajib tanda tangan pada\nstempel NOTASI maks 1x24 jam"]
    ```

    * **Pelaporan Kondisi Pasien dengan Metode SBAR (`Slide 41`)**:
        * **S (*Situation*)**: Identitas pasien dan masalah klinis utama yang sedang terjadi saat ini.
        * **B (*Background*)**: Riwayat penyakit, alasan masuk RS, terapi yang sudah diberikan.
        * **A (*Assessment*)**: Hasil pemeriksaan fisik terbaru, tanda vital, dan nilai laboratorium kritis.
        * **R (*Recommendation*)**: Saran atau permintaan instruksi tindakan lebih lanjut kepada DPJP.
    * **Syarat *Medication Order* Lengkap (`Slide 42`)**: Wajib memuat (1) Nama pasien, (2) Tanggal & jam resep, (3) Nama obat, (4) Dosis & satuan (`mg`, `unit`), (5) Rute pemberian, serta (6) Frekuensi & durasi pemberian.

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_41.jpg" class="glightbox" data-gallery="bdt-b4" data-title="Slide 41 · Contoh Rekam Medis SBAR & Stempel Notasi Paraf DPJP">
          <img src="slides_bdt_kul3/slide_41.jpg" alt="Slide 41" />
        </a>
        <div class="slide-caption">Slide 41 · Catatan SBAR & Stempel Notasi</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_42.jpg" class="glightbox" data-gallery="bdt-b4" data-title="Slide 42 · Komponen Resep Lengkap (Medication Order)">
          <img src="slides_bdt_kul3/slide_42.jpg" alt="Slide 42" />
        </a>
        <div class="slide-caption">Slide 42 · Komponen Medication Order</div>
      </div>
    </div>

---

## Bab 5 · SKP 3: Keamanan Obat High-Alert & Elektrolit Pekat (Slide 43–50)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart TD
        HA["SKP 3: Obat yang Perlu Diwaspadai\n(High-Alert Medications — Slide 43)"] --> G1["1. Elektrolit Konsentrat Pekat\n• KCl pekat ≥ 2 mEq/mL\n• NaCl hipertonik > 0,9%\n• MgSO4 ≥ 20% & Dextrose ≥ 20%"]
        HA --> G2["2. Obat LASA / NORUM\n(Look-Alike Sound-Alike)\nKemasan mirip atau nama terdengar mirip\n→ Gunakan Tall Man Lettering"]
        HA --> G3["3. Obat Risiko Tinggi Lain\n• Concentrated Heparin\n• Insulin, Kemoterapi, Narkotika"]
        G1 --> RULE["Aturan Ketat Slide 47 & 48:\n1. Pasang stiker 'HIGH ALERT! MEDICATION'\n2. TARIK KCl pekat dari ruang rawat biasa!\n3. Simpan terkunci & lakukan Double-Check"]
    ```

    !!! danger "Bedah Soal Asli Remidi BDT No. 39 (Diambil Persis dari Gambar Slide 48!)"
        Soal menanyakan: *"Label apakah yang wajib dipasang pada cairan Concentrated Potassium Chloride (KCl)?"*
        Lihat gambar botol di **Slide 48** (tab sebelah): tulisan besar di badan botol adalah **`HIGH ALERT! MEDICATION`**. Dosen membuat opsi pengecoh `Distinct`, `Warning`, dan `Harmful` dari teks kotak biru di samping botol pada Slide 48!

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_48.jpg" class="glightbox" data-gallery="bdt-b5" data-title="Slide 48 · Gambar Botol HIGH ALERT! MEDICATION (Sumber Soal Remidi No. 39)">
          <img src="slides_bdt_kul3/slide_48.jpg" alt="Slide 48" />
        </a>
        <div class="slide-caption">Slide 48 · Botol HIGH ALERT! (Soal Remidi No.39)</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_46.jpg" class="glightbox" data-gallery="bdt-b5" data-title="Slide 46 · Daftar Cairan High Concentration (KCl, Heparin, Glukosa, NaCl)">
          <img src="slides_bdt_kul3/slide_46.jpg" alt="Slide 46" />
        </a>
        <div class="slide-caption">Slide 46 · Contoh Cairan High Concentration</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_47.jpg" class="glightbox" data-gallery="bdt-b5" data-title="Slide 47 · 5 Langkah Mengurangi Risiko Obat High-Alert">
          <img src="slides_bdt_kul3/slide_47.jpg" alt="Slide 47" />
        </a>
        <div class="slide-caption">Slide 47 · Tarik KCl Pekat dari Bangsal</div>
      </div>
    </div>

---

## Bab 6 · SKP 4: Tepat Lokasi, Prosedur, & Pasien Operasi (Slide 51–54)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart LR
        M1["1. SURGICAL MARKING\n(Di Ruang Rawat)\nDokter operator memberi tanda\nlokasi operasi melibatkan pasien\nsaat pasien masih SADAR"] --> M2["2. VERIFIKASI PRA-INSISI\n(6 Ceklis Slide 51)\nIdentitas, Sisi/Lokasi, Prosedur,\nPosisi pasien, Implan, & Alat khusus"]
        M2 --> M3["3. SURGICAL TIME-OUT\n(Di Kamar Operasi)\nJeda komunikasi aktif seluruh tim\nTEPAT SEBELUM INSISI KULIT"]
    ```

    * **4 Penyebab Utama Kesalahan Operasi (`Slide 54 — Causes of Surgical Errors`)**:
        1. ==**Komunikasi yang tidak efektif antara anggota tim bedah**== *(Keluar persis di UAB BDT Axonation No. 43!)*.
        2. Kurangnya kerja sama tim (*teamwork*).
        3. Kurangnya melibatkan pasien dalam menandai lokasi operasi (*surgical marking*).
        4. Kurangnya standar prosedur untuk memeriksa lokasi operasi sebelum tindakan.

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_54.jpg" class="glightbox" data-gallery="bdt-b6" data-title="Slide 54 · Causes of Surgical Errors (Sumber Soal UAB No. 43)">
          <img src="slides_bdt_kul3/slide_54.jpg" alt="Slide 54" />
        </a>
        <div class="slide-caption">Slide 54 · Penyebab #1: Komunikasi Tim Bedah</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_51.jpg" class="glightbox" data-gallery="bdt-b6" data-title="Slide 51 · 6 Ceklis Verifikasi & Time-Out Sebelum Operasi">
          <img src="slides_bdt_kul3/slide_51.jpg" alt="Slide 51" />
        </a>
        <div class="slide-caption">Slide 51 · 6 Ceklis Time-Out Sebelum Insisi</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_52.jpg" class="glightbox" data-gallery="bdt-b6" data-title="Slide 52 · Komponen Surgical Timeout">
          <img src="slides_bdt_kul3/slide_52.jpg" alt="Slide 52" />
        </a>
        <div class="slide-caption">Slide 52 · Prosedur Surgical Timeout</div>
      </div>
    </div>

---

## Bab 7 · SKP 5–6, Pelaporan 2x24 Jam, Grading Risiko & RCA (Slide 55–80)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart TD
        INS["Terjadi Insiden (KNC / KTD / Sentinel)"] --> LAP["Wajib Lapor Internal ke Tim KPRS\nMAKSIMAL 2 x 24 JAM\n(Rahasia, Tidak Boleh Difotokopi, Non-Blaming)"]
        LAP --> GRD{"Grading Matriks Risiko\n(Dampak x Probabilitas — Slide 71 & 73)"}
        GRD -- "Pita BIRU (Rendah) /\nPita HIJAU (Moderat)" --> INV["Investigasi Sederhana\nOleh Atasan Langsung Unit Kerja\n(Biru maks 1 mgg · Hijau maks 2 mgg)"]
        GRD -- "Pita KUNING (Tinggi) /\nPita MERAH (Ekstrem / Sentinel)" --> RCA["ROOT CAUSE ANALYSIS (RCA)\nInvestigasi Komprehensif oleh Tim KPRS\nMaksimal 45 Hari ★ Soal UAB 22 No. 85"]
    ```

    * **SKP 5 — Pengurangan Risiko Infeksi (`Slide 55–57`)**:
        * **5 Momen Cuci Tangan WHO (*5 Moments for Hand Hygiene*)**: **2 Sebelum** (sebelum kontak pasien & sebelum tindakan aseptik) dan **3 Sesudah** (setelah terpapar cairan tubuh, setelah kontak pasien, & setelah kontak lingkungan sekitar pasien).
        * **Praktik Injeksi Aman**: Jarum & spuit wajib *single-use* (sekali pakai) untuk mencegah transmisi infeksi nosokomial (*HAIs*).
    * **SKP 6 — Pengurangan Risiko Pasien Jatuh (`Slide 58–59`)**:
        * Skrining menggunakan **Skala Morse** (dewasa), **Humpty Dumpty** (anak), atau **Edmonson** (psikiatri), pemasangan **Gelang Kuning**, serta pengamanan pagar tempat tidur (*side rail*).

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_69.jpg" class="glightbox" data-gallery="bdt-b7" data-title="Slide 69 · Alur Pelaporan Insiden 2x24 Jam, Grading, dan RCA">
          <img src="slides_bdt_kul3/slide_69.jpg" alt="Slide 69" />
        </a>
        <div class="slide-caption">Slide 69 · Waktu 2x24 Jam, Grading & RCA</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_71.jpg" class="glightbox" data-gallery="bdt-b7" data-title="Slide 71 · Formulir Laporan Insiden Internal (Rahasia & Maks 2x24 Jam)">
          <img src="slides_bdt_kul3/slide_71.jpg" alt="Slide 71" />
        </a>
        <div class="slide-caption">Slide 71 · Formulir Laporan Insiden 2x24 Jam</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_73.jpg" class="glightbox" data-gallery="bdt-b7" data-title="Slide 73 · Grading Risiko Kejadian: Biru, Hijau, Kuning, Merah">
          <img src="slides_bdt_kul3/slide_73.jpg" alt="Slide 73" />
        </a>
        <div class="slide-caption">Slide 73 · Grading Biru, Hijau, Kuning, Merah</div>
      </div>
      <div class="slide-card">
        <a href="slides_bdt_kul3/slide_75.jpg" class="glightbox" data-gallery="bdt-b7" data-title="Slide 75 · Prinsip Analisis Akar Penyebab Masalah (RCA)">
          <img src="slides_bdt_kul3/slide_75.jpg" alt="Slide 75" />
        </a>
        <div class="slide-caption">Slide 75 · Analisis Akar Masalah (RCA)</div>
      </div>
    </div>

---

## Simulator Soal Asli UAB & Remidi BDT (`mkdocs-quiz`)

*Pilih jawaban Anda lalu klik tombol **Submit** di setiap nomor untuk melihat umpan balik dan gambar slide buktinya:*

<quiz>
**[Soal Asli UAB BDT · Rekap Axonation No. 29]** Seorang perempuan berusia 35 tahun datang ke klinik pratama dengan keluhan nyeri perut. Dokter memberikan suntikan Antalgin untuk mengatasi rasa sakitnya. Beberapa menit kemudian pasien mengalami syok anafilaktik dan meninggal dunia. Termasuk insiden keselamatan pasien manakah kejadian tersebut?
- [ ] Kejadian Potensial Cedera (KPC)
  > Salah. KPC adalah kondisi berpotensi cedera ketika belum terjadi tindakan/insiden sama sekali.
- [ ] Kejadian Nyaris Cedera (KNC)
  > Salah. Pada KNC, kesalahan belum sampai terpapar ke tubuh pasien.
- [ ] Kejadian Tidak Cedera (KTC)
  > Salah. Pada KTC, pasien sudah terpapar namun tidak mengalami cedera.
- [ ] Kejadian Tidak Diharapkan (KTD)
  > Kurang tepat. Karena berujung pada kematian pasien, insiden ini masuk ke kategori paling berat yaitu Kejadian Sentinel.
- [x] Kejadian Sentinel
  > Benar! Sesuai Slide 18 baris terakhir, Kejadian Sentinel adalah suatu KTD yang mengakibatkan kematian atau cedera yang serius.

**Bukti Slide 18:**
![Slide 18](slides_bdt_kul3/slide_18.jpg){ width="380" }
</quiz>

<quiz>
**[Soal Asli UAB BDT · UAB 22 No. 70]** Pasien datang ke IGD karena nyeri kolik abdomen akut. Setelah diberikan injeksi analgetik, pasien mengalami henti jantung akibat reaksi anafilaksis berat dan dinyatakan meninggal. Kategori insiden keselamatan pasien pada kasus ini adalah...
- [ ] Kejadian Tidak Diharapkan (KTD)
  > Kurang tepat. KTD yang menyebabkan kematian atau cacat permanen diklasifikasikan khusus sebagai Kejadian Sentinel.
- [x] Kejadian Sentinel
  > Benar! Setiap KTD yang berujung kematian mendadak di luar perjalanan alamiah penyakit adalah Kejadian Sentinel (Slide 18).
- [ ] Kejadian Nyaris Cedera (KNC)
  > Salah. Obat sudah disuntikkan ke tubuh pasien.
- [ ] Kejadian Potensial Cedera (KPC)
  > Salah. KPC baru berupa kondisi potensial sebelum insiden terjadi.
- [ ] Kejadian Tidak Cedera (KTC)
  > Salah. Pasien mengalami cedera fatal hingga meninggal dunia.
</quiz>

<quiz>
**[Soal Asli UAB BDT-1 · Hal. 9–10]** Dokter meresepkan obat dengan dosis yang salah akibat kelelahan. Petugas farmasi telah menyiapkan obat tersebut, namun perawat ruangan menyadari ketidaksesuaian dosis saat melakukan pengecekan ulang sehingga obat batal diberikan kepada pasien. Disebut apakah insiden ini?
- [ ] Kejadian Potensial Cedera (KPC)
  > Salah. Di sini kesalahan penulisan dan penyiapan obat sudah terjadi, bukan sekadar kondisi potensial.
- [x] Kejadian Nyaris Cedera (KNC)
  > Benar! Sesuai Slide 18, KNC (Near Miss) adalah terjadinya insiden yang belum sampai terpapar ke pasien.
- [ ] Kejadian Tidak Cedera (KTC)
  > Salah. Disebut KTC apabila obat salah tersebut sudah telanjur diminum/disuntikkan ke pasien tetapi pasien tidak mengalami cedera.
- [ ] Kejadian Tidak Diharapkan (KTD)
  > Salah. Obat belum mengenai pasien dan pasien tidak cedera.
- [ ] Kejadian Sentinel
  > Salah. Tidak ada kematian atau cedera serius.
</quiz>

<quiz>
**[Soal Asli UAB BDT · Rekap Axonation No. 32]** Manakah di bawah ini yang termasuk dalam 7 Standar Keselamatan Pasien Rumah Sakit?
- [ ] Membangun kesadaran akan nilai keselamatan pasien
  > Jebakan! Ini adalah Step 1 dari "7 Langkah Menuju Keselamatan Pasien" (Slide 61), bukan 7 Standar.
- [ ] Memimpin dan mendukung staf dalam keselamatan pasien
  > Jebakan! Ini adalah Step 2 dari "7 Langkah Menuju Keselamatan Pasien" (Slide 61).
- [x] Peran kepemimpinan dalam meningkatkan keselamatan pasien
  > Benar! Tertulis persis di Slide 24 baris pertama sebagai Standar ke-5 dari "7 Standar Keselamatan Pasien".
- [ ] Mengembangkan sistem pelaporan insiden keselamatan pasien
  > Jebakan! Ini adalah Step 4 dari "7 Langkah Menuju Keselamatan Pasien" (Slide 61).
- [ ] Mengintegrasikan aktivitas pengelolaan risiko
  > Jebakan! Ini adalah Step 3 dari "7 Langkah Menuju Keselamatan Pasien" (Slide 61).

**Bukti Slide 24:**
![Slide 24](slides_bdt_kul3/slide_24.jpg){ width="380" }
</quiz>

<quiz>
**[Soal Asli UAB BDT · Rekap Axonation No. 44]** Standar keselamatan pasien rumah sakit merupakan acuan bagi fasyankes untuk melaksanakan pelayanannya. Yang termasuk dalam 7 Standar Keselamatan Pasien adalah...
- [x] Hak pasien
  > Benar! Sesuai Slide 23 poin pertama, "Hak Pasien" adalah Standar ke-1 dari 7 Standar Keselamatan Pasien.
- [ ] Ketepatan identifikasi pasien
  > Salah. Ini adalah SKP 1 (6 Sasaran Keselamatan Pasien — Slide 32).
- [ ] Peningkatan keamanan obat yang perlu diwaspadai
  > Salah. Ini adalah SKP 3 (6 Sasaran Keselamatan Pasien — Slide 32).
- [ ] Pengurangan risiko infeksi terkait pelayanan kesehatan
  > Salah. Ini adalah SKP 5 (6 Sasaran Keselamatan Pasien — Slide 33).
- [ ] Membangun kesadaran akan nilai keselamatan pasien
  > Salah. Ini adalah Step 1 dari 7 Langkah Keselamatan Pasien (Slide 61).

**Bukti Slide 23:**
![Slide 23](slides_bdt_kul3/slide_23.jpg){ width="380" }
</quiz>

<quiz>
**[Soal Asli UAB BDT-1 · Hal. 5 & 14]** Seorang pasien laki-laki berusia 58 tahun dirawat di bangsal paru dengan diagnosis pneumonia. Karena petugas admisi sibuk, pasien belum dipasangkan gelang identitas berwarna biru sehingga saat pemberian antibiotik injeksi, obat pasien tertukar dengan pasien di sebelah tempat tidurnya. Sasaran Keselamatan Pasien (SKP) manakah yang dilanggar?
- [x] Ketepatan identifikasi pasien
  > Benar! Pemasangan gelang identitas (biru untuk laki-laki sesuai Slide 35) dan verifikasi minimal 2 identitas sebelum pemberian obat adalah bagian dari SKP 1 (Slide 32).
- [ ] Peningkatan komunikasi yang efektif
  > Salah. SKP 2 mengatur komunikasi verbal/telepon (TBaK) dan SBAR antar-tenaga kesehatan.
- [ ] Peningkatan keamanan obat yang perlu diwaspadai
  > Salah. Akar masalah tertukarnya obat pada kasus ini adalah ketiadaan gelang identitas pasien.
- [ ] Kepastian tepat-lokasi, tepat-prosedur, tepat-pasien operasi
  > Salah. SKP 4 khusus untuk prosedur bedah/invasif di kamar operasi.
- [ ] Pengurangan risiko infeksi terkait pelayanan kesehatan
  > Salah. SKP 5 mengatur cuci tangan (Hand Hygiene).

**Bukti Slide 35:**
![Slide 35](slides_bdt_kul3/slide_35.jpg){ width="380" }
</quiz>

<quiz>
**[Soal Asli Remidi BDT · No. 39]** Cairan elektrolit pekat seperti Concentrated Potassium Chloride (KCl) dapat menyebabkan kejadian fatal bila diberikan tanpa pengenceran. Berdasarkan standar keselamatan pasien, label apakah yang wajib dipasang pada obat tersebut?
- [ ] Distinct
  > Jebakan visual! Kata "Distinct Packaging" tertulis di kotak biru kiri atas Slide 48 sebagai penjelasan kemasan, bukan nama labelnya.
- [x] High Alert
  > Benar! Lihat langsung botol di Slide 48: pada badan botol tertulis besar "HIGH ALERT! MEDICATION".
- [ ] Warning
  > Jebakan visual! Kata "Prominent Warning" adalah teks kotak biru kiri bawah di Slide 48.
- [ ] Harmful
  > Jebakan visual! Kata "Harmful Effects" adalah teks kotak biru kanan atas di Slide 48.
- [ ] Caution
  > Salah. Istilah resminya adalah High Alert.

**Bukti Slide 48:**
![Slide 48](slides_bdt_kul3/slide_48.jpg){ width="380" }
</quiz>

<quiz>
**[Soal Asli UAB BDT · Rekap Axonation No. 43]** Seorang pasien dijadwalkan menjalani operasi di daerah thoraks, namun saat selesai operasi ternyata bagian tungkai kaki pasien juga ikut dioperasi akibat kesalahpahaman instruksi di meja operasi. Berdasarkan materi Patient Safety, apakah penyebab utama terjadinya kesalahan bedah tersebut?
- [x] Komunikasi tidak efektif antar tim medis / bedah
  > Benar! Tertulis persis pada urutan nomor 1 di Slide 54 (Causes of Surgical Errors): "1. Komunikasi yang tidak efektif antara anggota tim bedah".
- [ ] Kurangnya fasilitas kamar operasi
  > Salah. Tidak termasuk dalam 4 penyebab utama di Slide 54.
- [ ] Efek samping obat anestesi
  > Salah. Bukan penyebab salah lokasi operasi (wrong-site surgery).
- [ ] Keluarga pasien terlambat menandatangani informed consent
  > Salah. Penandaan lokasi dan Time-Out adalah tanggung jawab tim bedah bersama pasien.
- [ ] Tidak tersedianya antibiotik profilaksis
  > Salah. Antibiotik profilaksis terkait pencegahan infeksi luka operasi, bukan salah lokasi insisi.

**Bukti Slide 54:**
![Slide 54](slides_bdt_kul3/slide_54.jpg){ width="380" }
</quiz>

<quiz>
**[Soal Asli UAB BDT · UAB 22 No. 85]** Seorang pasien terjatuh dari brankar saat proses transfer dari UGD menuju kamar operasi sehingga mengalami cedera kepala. Tim keselamatan pasien rumah sakit segera melakukan investigasi terstruktur untuk mencari akar penyebab sistemik agar kejadian serupa tidak terulang. Metode apakah yang digunakan tim tersebut?
- [x] Root Cause Analysis (RCA)
  > Benar! Sesuai Slide 69 dan Slide 75, setiap insiden keselamatan pasien dengan derajat risiko Kuning/Merah dianalisis akar masalahnya menggunakan Root Cause Analysis (RCA).
- [ ] Failure Mode and Effects Analysis (FMEA)
  > Salah. FMEA bersifat proaktif (sebelum insiden terjadi), sedangkan analisis sesudah insiden jatuh terjadi menggunakan RCA.
- [ ] Audit Medis Internal
  > Salah. Investigasi insiden keselamatan pasien oleh Tim KPRS menggunakan RCA.
- [ ] Visum et Repertum
  > Salah. Visum adalah keterangan medis untuk kepentingan peradilan pidana.
- [ ] Informed Consent
  > Salah. Informed consent adalah persetujuan tindakan kedokteran.

**Bukti Slide 75:**
![Slide 75](slides_bdt_kul3/slide_75.jpg){ width="380" }
</quiz>
"""

with open(os.path.join(DOCS_DIR, "bdt-kul3-patient-safety.md"), "w", encoding="utf-8") as f:
    f.write(BDT_MD)

# ==============================================================================
# 3. DOCS/EMN-KUL2-DEFISIENSI-VITAMIN.MD
# ==============================================================================
EMN_MD = """# Blok 9 (EMN) · Kuliah 2: Defisiensi Vitamin

**Dosen Pengampu:** dr. Iwal Reza Ahdi, Sp.PD · **Sumber Asli:** 28 Slide PPT · **Status Bank Soal:** 3 Kasus Asli Slide Dosen + 3 Prediksi Berbasis Slide *(0 Klaim Palsu Soal UAB EMN)*

!!! success "Belajar Tuntas Tanpa Perlu Buka File PPT"
    Seluruh **28 slide dr. Iwal Reza Ahdi, Sp.PD** telah dipadatkan menjadi **Mindmap Interaktif + 6 Bab Diagram Metabolik & Klinis** di bawah ini. Bukti tangkapan layar slide asli tersedia di tab pendamping setiap bab.

---

## Peta Konsep Utuh Defisiensi Vitamin (`Markmap`)

<div class="markmap-box">
<div class="markmap">
<script type="text/template">
# Defisiensi Vitamin (dr. Iwal, Sp.PD)
## 1. Empat Jalur Etiologi (Slide 5)
- Asupan Kurang: Diet restriktif, vegan (B12), alkoholik (B1)
- Gangguan Absorpsi: Celiac, reseksi ileum (B12), bariatrik, kolestasis (A,D,E,K)
- Peningkatan Kebutuhan: Kehamilan & laktasi (Folat/B9), tumbuh kembang
- Obat Spesifik: Metformin (B12), Isoniazid/INH (B6), Warfarin (Vit K)
## 2. Vitamin Larut Lemak (A, D, E, K)
- Vitamin A (Slide 8): Retinal (Rodopsin/Nyctalopia) vs Retinoat (Epitel/Bitot/Keratomalasia)
- Vitamin D (Slide 9): Kulit (D3) -> Hati (25-OH-D = Lab!) -> Ginjal (1,25-OH2-D = Aktif!)
- Vitamin E (Slide 10): Antioksidan membran -> Defisiensi: Ataksia & neuropati
- Vitamin K (Slide 10 & 19): Faktor II, VII, IX, X -> Defisiensi: PT/INR Memanjang!
## 3. Vitamin Larut Air (B Kompleks & C)
- B1 / Tiamin (Slide 11): Kofaktor TPP -> Beriberi Kering, Basah, & Ensefalopati Wernicke
- B2 / Riboflavin (Slide 13): FMN/FAD -> Angular cheilitis, glositis
- B3 / Niasin (Slide 13): NAD+/NADP+ -> Pellagra 3D (Dermatitis Casal necklace, Diare, Demensia)
- B6 / Piridoksin (Slide 13): Kofaktor PLP -> Neuropati akibat Isoniazid (INH)
- B9 vs B12 (Slide 16-17): Sama-sama MCV > 100 fL; bedanya B12 ada Neuropati & MMA Naik!
- Vitamin C / Skorbut (Slide 14 & 26): Hidroksilasi kolagen -> Gusi berdarah & PT/INR Normal!
</script>
</div>
</div>

---

## Bab 1 · 4 Jalur Penyebab Defisiensi & Interaksi Obat (Slide 1–7)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart TD
        ET["4 Jalur Menuju Defisiensi Vitamin (Slide 5)"] --> J1["01. ASUPAN KURANG\n• Diet sangat restriktif\n• Vegan murni tanpa suplemen (B12)\n• Alkoholisme kronik (B1, Folat)"]
        ET --> J2["02. GANGGUAN ABSORPSI\n• Reseksi ileum terminal / Crohn (B12)\n• Operasi bariatrik / gastritis autoimun\n• Kolestasis hepatobilier (Vit A, D, E, K)"]
        ET --> J3["03. PENINGKATAN KEBUTUHAN\n• Kehamilan & laktasi (Folat/B9)\n• Masa pertumbuhan cepat\n• Penyakit kritis / infeksi berat"]
        ET --> J4["04. INTERAKSI OBAT KHAS ★\n• Metformin jangka panjang → Def. B12\n• Isoniazid (INH) obat TB → Def. B6\n• Warfarin → Antagonis Vitamin K"]
    ```

    * **Algoritma Pendekatan Klinis 4 Langkah (`Slide 6`)**:
        1. **Identifikasi Pola Klinis**: Apakah pasien datang dengan pola *anemia makrositik*, *neuropati perifer*, *dermatitis mukokutan*, *nyeri/deformitas tulang*, atau *perdarahan*?
        2. **Nilai Faktor Risiko**: Telusuri riwayat diet, malabsorpsi GI/hepatobilier, konsumsi alkohol, obat rutin (*Metformin, INH, PPI*), usia, dan kehamilan.
        3. **Pilih Uji Lab Terarah**: `CBC + apusan darah tepi`, `B12 serum / MMA`, `25(OH)D`, atau `PT/INR` sesuai indikasi klinis.
        4. **Tangani & Koreksi Penyebab Dasar**: Berikan suplementasi spesifik sekaligus atasi penyakit yang mendasarinya.

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_kul2/slide_5.jpg" class="glightbox" data-gallery="emn-b1" data-title="Slide 5 · Empat Jalur Menuju Defisiensi & Interaksi Obat">
          <img src="slides_kul2/slide_5.jpg" alt="Slide 5" />
        </a>
        <div class="slide-caption">Slide 5 · 4 Jalur Etiologi & Obat</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_6.jpg" class="glightbox" data-gallery="emn-b1" data-title="Slide 6 · Pendekatan Klinis: Curiga → Uji → Tangani">
          <img src="slides_kul2/slide_6.jpg" alt="Slide 6" />
        </a>
        <div class="slide-caption">Slide 6 · Algoritma Curiga → Uji → Tangani</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_3.jpg" class="glightbox" data-gallery="emn-b1" data-title="Slide 3 · Kasus Pemicu Awal: Laki-laki 62 Tahun, Metformin Lama, MCV 112 fL">
          <img src="slides_kul2/slide_3.jpg" alt="Slide 3" />
        </a>
        <div class="slide-caption">Slide 3 · Kasus Pembuka (Metformin & B12)</div>
      </div>
    </div>

---

## Bab 2 · Vitamin Larut Lemak: A, D, E, & K (Slide 8–10, 19)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart LR
        subgraph VITA ["1. Vitamin A (Slide 8)"]
            A1["Retinal → Rodopsin"] --> A2["Defisiensi Dini:\nRabun Senja (Nyctalopia)"]
            A3["Asam Retinoat → Diferensiasi Epitel"] --> A4["Xerophthalmia & Bercak Bitot\n→ Keratomalasia (Buta)"]
        end
        subgraph VITD ["2. Jalur Aktivasi Vitamin D (Slide 9)"]
            D1["Kulit (UVB) / Diet\nVitamin D3 / D2"] --> D2["HATI (25-Hidroksilase)\n25(OH)D / Kalsidiol\n★ Parameter Lab Status Vit D!"]
            D2 --> D3["GINJAL (1α-Hidroksilase)\n1,25-(OH)2-D / Kalsitriol\n★ Bentuk Biologis Aktif!"]
            D3 --> D4["Anak: Rakitis\nDewasa: Osteomalasia"]
        end
    ```

    * **Ringkasan 4 Vitamin Larut Lemak (`Slide 19`)**:
        * **Vitamin A**: Siklus visual (*retinal*) & integritas epitel mukosa (*retinoat*). Defisiensi: *nyctalopia* $\rightarrow$ *xerophthalmia* + **Bercak Bitot** $\rightarrow$ *keratomalasia*.
        * **Vitamin D**: Absorpsi kalsium & fosfat di usus serta mineralisasi tulang. **Ingat catatan Slide 9**: Bentuk yang diukur di laboratorium untuk menilai status Vitamin D adalah **`25(OH)D`**, bukan `1,25-(OH)2-D`!
        * **Vitamin E**: Antioksidan pelindung membran lipid neuron & eritrosit. Defisiensi (pada malabsorpsi lemak kronik): **ataksia spinoserebelar, neuropati perifer, dan hemolisis**.
        * **Vitamin K**: Kofaktor $\gamma$-karboksilasi **Faktor Koagulasi II, VII, IX, X** (serta Protein C & S) di hati. Defisiensi (pada neonatus tanpa profilaksis injeksi Vit K1, kolestasis, atau terapi warfarin): **perdarahan aktif dengan pemanjangan PT/INR**.

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_kul2/slide_8.jpg" class="glightbox" data-gallery="emn-b2" data-title="Slide 8 · Vitamin A: Penglihatan, Epitel, & Foto Klinis Bercak Bitot">
          <img src="slides_kul2/slide_8.jpg" alt="Slide 8" />
        </a>
        <div class="slide-caption">Slide 8 · Vitamin A & Foto Bercak Bitot</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_9.jpg" class="glightbox" data-gallery="emn-b2" data-title="Slide 9 · Vitamin D: Jalur Kulit-Hati-Ginjal & Rakitis vs Osteomalasia">
          <img src="slides_kul2/slide_9.jpg" alt="Slide 9" />
        </a>
        <div class="slide-caption">Slide 9 · Vitamin D & Parameter 25(OH)D</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_10.jpg" class="glightbox" data-gallery="emn-b2" data-title="Slide 10 · Vitamin E (Antioksidan) & Vitamin K (Koagulasi)">
          <img src="slides_kul2/slide_10.jpg" alt="Slide 10" />
        </a>
        <div class="slide-caption">Slide 10 · Vitamin E & Vitamin K</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_19.jpg" class="glightbox" data-gallery="emn-b2" data-title="Slide 19 · Tabel Ringkasan Vitamin Larut Lemak (A, D, E, K)">
          <img src="slides_kul2/slide_19.jpg" alt="Slide 19" />
        </a>
        <div class="slide-caption">Slide 19 · Ringkasan Vitamin Larut Lemak</div>
      </div>
    </div>

---

## Bab 3 · Vitamin B1 (Tiamin), B2, B3 (Pellagra), & B6 (Slide 11–13, 25)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart TD
        B1["Defisiensi Vitamin B1 (Tiamin)\nKofaktor Aktif: Tiamin Pirofosfat (TPP) — Slide 11"] --> E1["3 Enzim yang Lumpuh:\n1. Piruvat dehidrogenase\n2. α-Ketoglutarat dehidrogenase\n3. Transketolase (Jalur HMP)"]
        E1 --> S1["1. Beriberi Kering\nNeuropati perifer simetris\n(kelemahan & kesemutan distal)"]
        E1 --> S2["2. Beriberi Basah\nVasodilatasi perifer → Gagal jantung\ncurah tinggi (High-Output) & edema"]
        E1 --> S3["3. Ensefalopati Wernicke ★\nTrias Akut: Konfusi + Ataksia +\nOftalmoplegia / Nistagmus (Slide 25)"]
    ```

    * **Vitamin B2 (`Riboflavin` — `Slide 13`)**: Kofaktor **FMN & FAD** (reaksi redoks). Tanda defisiensi: **Angular cheilitis** (luka/fisura di sudut bibir), glositis (lidah licin kemerahan/magenta), dan dermatitis seboroik nasolabial.
    * **Vitamin B3 (`Niasin` — `Slide 13`)**: Prekursor **NAD+ & NADP+**. Defisiensi berat (diet jagung monoton / malnutrisi) menyebabkan **Pellagra (Trias 3D)**:
        1. **D**ermatitis fotosensitif simetris di area leher yang terkena matahari (**Casal necklace**).
        2. **D**iare kronik (atrofi vili mukosa usus).
        3. **D**emensia / gangguan neuropsikiatri.
    * **Vitamin B6 (`Piridoksin` — `Slide 13`)**: Kofaktor **PLP** (transaminasi asam amino, sintesis neurotransmiter GABA, dan sintesis heme). Risiko khas: pasien TB yang mendapat terapi **Isoniazid (INH)** tanpa suplementasi B6 $\rightarrow$ **neuropati perifer, kejang, dan anemia sideroblastik**.

    !!! danger "Jebakan Klinis IGD pada Kasus Diskusi 2 (Slide 11 & Slide 25)"
        Pada pasien alkoholik kronik, malnutrisi berat, atau hiperemesis gravidarum yang datang ke IGD, **pemberian infus glukosa/dekstrosa TANPA pemberian Tiamin (B1) terlebih dahulu** akan menguras habis sisa TPP dan langsung memicu **Ensefalopati Wernicke akut**!

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_kul2/slide_11.jpg" class="glightbox" data-gallery="emn-b3" data-title="Slide 11 · Vitamin B1 (Tiamin): 3 Enzim TPP, Beriberi, & Wernicke">
          <img src="slides_kul2/slide_11.jpg" alt="Slide 11" />
        </a>
        <div class="slide-caption">Slide 11 · Vitamin B1 (TPP, Beriberi, Wernicke)</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_13.jpg" class="glightbox" data-gallery="emn-b3" data-title="Slide 13 · Vitamin B2, B3 (Pellagra & Casal Necklace), dan B6">
          <img src="slides_kul2/slide_13.jpg" alt="Slide 13" />
        </a>
        <div class="slide-caption">Slide 13 · B2, B3 (Pellagra), & B6 (INH)</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_25.jpg" class="glightbox" data-gallery="emn-b3" data-title="Slide 25 · Diskusi Kasus 2: Kebingungan Akut, Ataksia, Nistagmus (Wernicke)">
          <img src="slides_kul2/slide_25.jpg" alt="Slide 25" />
        </a>
        <div class="slide-caption">Slide 25 · Diskusi Kasus 2 (Wernicke)</div>
      </div>
    </div>

---

## Bab 4 · Pembeda Utama: Folat (B9) vs Kobalamin (B12) (Slide 16, 17, 24)

=== "Tabel Pembeda & Diagram Metabolik"

    ```mermaid
    flowchart LR
        subgraph B9B12 ["Persamaan B9 & B12"]
            M1["Gangguan Sintesis DNA"] --> M2["Anemia Megaloblastik\n(MCV > 100 fL & Neutrofil Hipersegmentasi)\n+ Homosistein Serum MENINGKAT"]
        end
        subgraph ONLYB12 ["Spesifik Hanya pada Defisiensi B12 (Slide 17)"]
            N1["Gagal Enzim Metilmalonil-KoA Mutase"] --> N2["Asam Metilmalonat (MMA) MENINGKAT ★\n+ Demyelinisasi Kolumna Dorsalis & Saraf Tepi\n(Kesemutan, Hilang Vibrasi, Ataksia)"]
        end
    ```

    | Parameter Pembeda (`Slide 17`) | Defisiensi Vitamin B9 (Folat) | Defisiensi Vitamin B12 (Kobalamin) |
    | :--- | :--- | :--- |
    | **MCV / Gambaran Darah** | Makrositik, megaloblastik (`MCV > 100 fL`) | Makrositik, megaloblastik (`MCV > 100 fL`) |
    | **Neuropati / Ataksia / Vibrasi** | **Tidak khas / Tidak ada** | ==**Khas!**== *(Dapat muncul walau Hb & MCV belum abnormal)* |
    | **Kadar Homosistein** | Sering meningkat | Sering meningkat |
    | **Asam Metilmalonat (`MMA`)** | **Normal** | ==**Meningkat Spesifik!**== |
    | **Faktor Risiko Utama** | Kehamilan, kurang sayur hijau, alkohol, fenitoin/MTX | **Metformin jangka panjang**, diet vegan, gastritis autoimun (anemia pernisiosa), reseksi ileum terminal |

    !!! danger "Peringatan Klinis di Bagian Bawah Slide 17"
        Memberikan terapi **asam folat saja** pada pasien defisiensi Vitamin B12 akan memperbaiki gambaran anemia megaloblastiknya secara semu, tetapi **kerusakan neurologis (demyelinisasi medula spinalis) akan terus memburuk secara ireversibel**!

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_kul2/slide_17.jpg" class="glightbox" data-gallery="emn-b4" data-title="Slide 17 · Tabel Perbandingan Folat (B9) vs B12 (Kobalamin)">
          <img src="slides_kul2/slide_17.jpg" alt="Slide 17" />
        </a>
        <div class="slide-caption">Slide 17 · Tabel B9 vs B12 (MMA & Neuropati)</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_16.jpg" class="glightbox" data-gallery="emn-b4" data-title="Slide 16 · Jalur Absorpsi B12 (Lambung IF → Ileum Terminal)">
          <img src="slides_kul2/slide_16.jpg" alt="Slide 16" />
        </a>
        <div class="slide-caption">Slide 16 · Absorpsi B12 & Faktor Risiko</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_24.jpg" class="glightbox" data-gallery="emn-b4" data-title="Slide 24 · Diskusi Kasus 1: Metformin, Kesemutan, MCV 112 fL">
          <img src="slides_kul2/slide_24.jpg" alt="Slide 24" />
        </a>
        <div class="slide-caption">Slide 24 · Diskusi Kasus 1 (Defisiensi B12)</div>
      </div>
    </div>

---

## Bab 5 · Pembeda Perdarahan: Skorbut (Vit C) vs Defisiensi Vit K (Slide 14, 21, 26)

=== "Intisari & Diagram Alur Visual"

    ```mermaid
    flowchart TD
        BL["Pasien Datang dengan Perdarahan Gusi / Mudah Memar (Slide 26)"] --> LAB{"Cek Hasil Laboratorium\nPT / INR & aPTT"}
        LAB -- "PT / INR NORMAL\n+ Petechiae Perifolikular\n+ Corkscrew Hair & Luka Lama Sembuh" --> VITC["DEFISIENSI VITAMIN C (SKORBUT)\nDefek hidroksilasi prolin & lisin\n→ Kolagen dinding kapiler rapuh"]
        LAB -- "PT / INR MEMANJANG\n+ Riwayat Kolestasis / Warfarin /\nNeonatus Tanpa Profilaksis" --> VITK["DEFISIENSI VITAMIN K\nDefek γ-karboksilasi Faktor II, VII, IX, X\n→ Gangguan kaskade koagulasi"]
    ```

=== "Bukti Slide Asli Dosen (Klik untuk Perbesar)"

    <div class="slide-grid">
      <div class="slide-card">
        <a href="slides_kul2/slide_26.jpg" class="glightbox" data-gallery="emn-b5" data-title="Slide 26 · Diskusi Kasus 3: Perdarahan Gingiva & PT/INR Normal (Skorbut)">
          <img src="slides_kul2/slide_26.jpg" alt="Slide 26" />
        </a>
        <div class="slide-caption">Slide 26 · Diskusi Kasus 3 (Vit C vs Vit K)</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_14.jpg" class="glightbox" data-gallery="emn-b5" data-title="Slide 14 · Vitamin C: Sintesis Kolagen & Gambaran Klinis Skorbut">
          <img src="slides_kul2/slide_14.jpg" alt="Slide 14" />
        </a>
        <div class="slide-caption">Slide 14 · Vitamin C & Skorbut</div>
      </div>
      <div class="slide-card">
        <a href="slides_kul2/slide_21.jpg" class="glightbox" data-gallery="emn-b5" data-title="Slide 21 · Pemilihan Pemeriksaan Lab Sesuai Pertanyaan Klinis">
          <img src="slides_kul2/slide_21.jpg" alt="Slide 21" />
        </a>
        <div class="slide-caption">Slide 21 · Panduan Pemeriksaan Lab Terarah</div>
      </div>
    </div>

---

## Simulator Latihan Kasus Slide & Prediksi (`mkdocs-quiz`)

<quiz>
**[Kasus Asli Slide Dosen · Slide 3 & Slide 24]** Seorang laki-laki berusia 62 tahun dengan riwayat DM tipe 2 dan konsumsi metformin jangka panjang datang dengan keluhan kesemutan pada kedua kaki selama 6 bulan, mudah lelah, dan lidah terasa nyeri (glossitis). Pemeriksaan fisik menunjukkan gangguan sensasi vibrasi. Laboratorium: Hb 9,8 g/dL dan MCV 112 fL. Defisiensi vitamin manakah yang paling mungkin beserta pemeriksaan metabolit konfirmasinya?
- [ ] Vitamin B9 (Folat) — kadar homosistein normal
  > Salah. Pada defisiensi B9 maupun B12 kadar homosistein meningkat, dan B9 tidak menyebabkan gangguan vibrasi/neuropati perifer.
- [x] Vitamin B12 (Kobalamin) — peningkatan asam metilmalonat (MMA)
  > Benar! Konsumsi metformin jangka panjang menghambat absorpsi B12 di ileum terminal, memicu anemia megaloblastik (MCV 112 fL) + neuropati sensorik, dengan peningkatan spesifik asam metilmalonat (MMA) sesuai Slide 17 & 24.
- [ ] Vitamin B1 (Tiamin) — penurunan aktivitas transketolase
  > Salah. Defisiensi B1 tidak menyebabkan anemia makrositik (MCV 112 fL).
- [ ] Vitamin B6 (Piridoksin) — peningkatan feritin serum
  > Salah. Defisiensi B6 menyebabkan anemia mikrositik/sideroblastik, bukan MCV 112 fL.
- [ ] Vitamin E (Tokoferol) — pemanjangan PT/INR
  > Salah. Pemanjangan PT/INR adalah tanda defisiensi Vitamin K.

**Bukti Slide 24:**
![Slide 24](slides_kul2/slide_24.jpg){ width="380" }
</quiz>

<quiz>
**[Kasus Asli Slide Dosen · Slide 25]** Seorang pasien dengan riwayat malnutrisi berat dan muntah berkepanjangan dibawa ke IGD dalam kondisi kebingungan akut (konfusi), langkah jalan sempoyongan (ataksia), serta gangguan gerak bola mata (nistagmus/oftalmoplegia) setelah sebelumnya mendapat cairan infus dekstrosa. Defisiensi vitamin apakah yang mendasari kegawatan neurologis ini?
- [x] Vitamin B1 (Tiamin)
  > Benar! Trias konfusi akut, ataksia, dan nistagmus/oftalmoplegia pasca-pemberian glukosa adalah tanda klasik Ensefalopati Wernicke akibat defisiensi Tiamin Pirofosfat (Slide 11 & 25).
- [ ] Vitamin B2 (Riboflavin)
  > Salah. Defisiensi B2 bermanifestasi sebagai angular cheilitis dan glositis.
- [ ] Vitamin B3 (Niasin)
  > Salah. Defisiensi B3 menyebabkan Pellagra (Dermatitis, Diare, Demensia).
- [ ] Vitamin B12 (Kobalamin)
  > Salah. Defisiensi B12 menyebabkan degenerasi subakut medula spinalis, bukan trias akut Wernicke pasca-infus dekstrosa.
- [ ] Vitamin C (Asam Askorbat)
  > Salah. Defisiensi Vitamin C menyebabkan skorbut (perdarahan gusi & kapiler).

**Bukti Slide 25:**
![Slide 25](slides_kul2/slide_25.jpg){ width="380" }
</quiz>

<quiz>
**[Kasus Asli Slide Dosen · Slide 26]** Seorang pria berusia 41 tahun dengan diet sangat terbatas datang dengan keluhan gusi sering berdarah, mudah memar, bintik perdarahan perifolikular di kedua tungkai, dan luka yang lama sembuh. Hasil pemeriksaan darah menunjukkan jumlah trombosit normal serta nilai PT dan INR normal. Diagnosis yang paling tepat adalah...
- [ ] Defisiensi Vitamin K
  > Salah! Pada defisiensi Vitamin K, nilai PT dan INR pasti memanjang.
- [x] Defisiensi Vitamin C (Skorbut)
  > Benar! Sesuai Slide 26, perdarahan gingiva + petechiae perifolikular + luka lama sembuh dengan PT/INR yang NORMAL adalah ciri khas Skorbut akibat defek kolagen kapiler.
- [ ] Defisiensi Vitamin D (Osteomalasia)
  > Salah. Defisiensi Vitamin D menyebabkan gangguan mineralisasi tulang.
- [ ] Defisiensi Vitamin B3 (Pellagra)
  > Salah. Pellagra ditandai dermatitis fotosensitif, diare, dan demensia.
- [ ] Defisiensi Vitamin A (Xerophthalmia)
  > Salah. Defisiensi Vitamin A menyerang penglihatan senja dan epitel kornea/konjungtiva.

**Bukti Slide 26:**
![Slide 26](slides_kul2/slide_26.jpg){ width="380" }
</quiz>

<quiz>
**[Prediksi Berbasis Slide · Slide 8]** Seorang anak berusia 4 tahun dibawa ibunya karena sering menabrak benda saat senja hari. Pada pemeriksaan konjungtiva tampak bercak putih keperakan berbusa di sisi temporal (Bercak Bitot). Bentuk aktif vitamin manakah yang berperan menjaga diferensiasi epitel konjungtiva agar tidak mengalami metaplasia keratin tersebut?
- [x] Asam retinoat
  > Benar! Sesuai Slide 8: "Retinal → siklus visual (rodopsin)", sedangkan "Retinoat → diferensiasi epitel".
- [ ] 11-cis-retinal
  > Kurang tepat. Retinal berperan pada rodopsin di retina untuk penglihatan gelap, sedangkan diferensiasi epitel konjungtiva diatur oleh asam retinoat.
- [ ] Kalsitriol
  > Salah. Kalsitriol adalah bentuk aktif Vitamin D.
- [ ] Alfa-tokoferol
  > Salah. Alfa-tokoferol adalah bentuk aktif Vitamin E.
- [ ] Menakuinon
  > Salah. Menakuinon adalah Vitamin K2.

**Bukti Slide 8:**
![Slide 8](slides_kul2/slide_8.jpg){ width="380" }
</quiz>

<quiz>
**[Prediksi Berbasis Slide · Slide 9]** Seorang perempuan berusia 50 tahun mengeluhkan nyeri tulang difus dan kelemahan otot proksimal. Dokter mencurigai adanya osteomalasia akibat defisiensi Vitamin D. Pemeriksaan laboratorium manakah yang paling tepat dipilih untuk mencerminkan status cadangan Vitamin D tubuh pasien?
- [ ] 1,25-dihidroksivitamin D [1,25(OH)2D]
  > Jebakan! Walaupun 1,25(OH)2D adalah bentuk biologis paling aktif, waktu paruhnya sangat pendek sehingga tidak digunakan sebagai penanda status cadangan Vitamin D.
- [x] 25-hidroksivitamin D [25(OH)D]
  > Benar! Sesuai catatan kaki di Slide 9: "25(OH)D mencerminkan status vitamin D".
- [ ] 7-dehidrokolesterol
  > Salah. Ini adalah prekursor di kulit sebelum terpapar UVB.
- [ ] Kalsitonin serum
  > Salah. Kalsitonin adalah hormon sel parafolikular tiroid.
- [ ] Alkaline phosphatase urin
  > Salah. Bukan parameter baku status Vitamin D.

**Bukti Slide 9:**
![Slide 9](slides_kul2/slide_9.jpg){ width="380" }
</quiz>

<quiz>
**[Prediksi Berbasis Slide · Slide 13]** Seorang petani yang hanya mengonsumsi jagung tanpa variasi protein hewani datang dengan keluhan ruam kulit hiperpigmentasi simetris di area leher yang terpapar matahari (Casal necklace), disertai diare kronik dan penurunan daya ingat. Defisiensi kofaktor vitamin apakah yang dialami pasien?
- [ ] Vitamin B1 (Tiamin)
  > Salah. Defisiensi B1 menyebabkan beriberi dan ensefalopati Wernicke.
- [ ] Vitamin B2 (Riboflavin)
  > Salah. Defisiensi B2 menyebabkan stomatitis angularis dan glositis.
- [x] Vitamin B3 (Niasin / NAD+ & NADP+)
  > Benar! Sesuai Slide 13, trias Dermatitis fotosensitif (Casal necklace), Diare, dan Demensia adalah sindrom Pellagra akibat defisiensi Vitamin B3 (Niasin).
- [ ] Vitamin B6 (Piridoksin)
  > Salah. Defisiensi B6 terkait neuropati perifer akibat obat Isoniazid.
- [ ] Vitamin B7 (Biotin)
  > Salah. Defisiensi biotin menyebabkan alopesia dan dermatitis periorifisial.

**Bukti Slide 13:**
![Slide 13](slides_kul2/slide_13.jpg){ width="380" }
</quiz>
"""

with open(os.path.join(DOCS_DIR, "emn-kul2-defisiensi-vitamin.md"), "w", encoding="utf-8") as f:
    f.write(EMN_MD)

print("MkDocs files generated successfully!")
