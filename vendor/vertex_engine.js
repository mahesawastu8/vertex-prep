/**
 * VERTEX-PREP 2.0 Unified Open-Source Integration Engine
 * Integrates:
 * 1. @svgdotjs/svg.js + krmanik/image-occlusion-in-browser (Bounding-Box Highlight & Image Occlusion)
 * 2. PyMuPDF / Docling Exact Slide Coordinate Mapping (0-100% normalized PDF coordinates)
 * 3. open-spaced-repetition/ts-fsrs (FSRS v6 Memory Scheduler: Stability, Difficulty, Retrievability)
 * 4. dexie/Dexie.js (IndexedDB Persistent Study State & Error Code E1-E6 Telemetry)
 * 5. cytoscape/cytoscape.js (Interactive Cause-Effect & Pathophysiology Node Graph)
 * 6. Pagefind / Instant Cross-Block Search Engine (2,633 UAB Questions + 108 Lecture Slides via Cmd+K)
 * 7. kerrickstaley/genanki (.apkg Anki Deck Direct Export)
 */

(function () {
  "use strict";

  // =========================================================================
  // 1. EXACT PYMUPDF / DOCLING SLIDE BOUNDING-BOX COORDINATES (x%, y%, w%, h%)
  // =========================================================================
  const SLIDE_BOXES = {
    "BDT_KUL3": {
      18: [
        { x: 5.5, y: 35.2, w: 88.0, h: 10.8, label: "KTD: Insiden mengakibatkan cedera pada pasien", color: "#B8332A" },
        { x: 5.5, y: 46.2, w: 84.0, h: 10.8, label: "KNC: Belum sampai terpapar ke pasien (UAB BDT-1)", color: "#0F5C4D" },
        { x: 5.5, y: 57.0, w: 84.0, h: 10.8, label: "KTC: Sudah terpapar ke pasien, TIDAK timbul cedera", color: "#1B5E7A" },
        { x: 5.5, y: 67.8, w: 84.0, h: 10.8, label: "KPC: Kondisi sangat berpotensi cedera, belum insiden", color: "#B26200" },
        { x: 5.5, y: 78.6, w: 85.0, h: 11.5, label: "SENTINEL: KTD → Kematian / Cedera Serius (UAB No.29 & 70)", color: "#B8332A" }
      ],
      19: [
        { x: 20.1, y: 17.0, w: 61.0, h: 16.0, label: "Prinsip Utama: What Do We Mean By SAFE?", color: "#0F5C4D" },
        { x: 25.0, y: 41.0, w: 56.0, h: 43.0, label: "DO NO HARM (Prinsip Non-Maleficence Patient Safety)", color: "#B8332A" }
      ],
      23: [
        { x: 27.0, y: 6.5, w: 54.5, h: 7.0, label: "Judul Kerangka 1: 7 Standar Keselamatan Pasien", color: "#0F5C4D" },
        { x: 44.0, y: 20.8, w: 17.0, h: 5.8, label: "Standar 1: HAK PASIEN (Keluar di UAB Axonation No.44)", color: "#B8332A" },
        { x: 32.5, y: 41.0, w: 40.0, h: 5.8, label: "Standar 2: Pendidikan bagi Pasien & Keluarga", color: "#0F5C4D" },
        { x: 36.5, y: 59.8, w: 32.0, h: 8.8, label: "Standar 3: Kesinambungan Pelayanan", color: "#1B5E7A" }
      ],
      24: [
        { x: 33.0, y: 21.5, w: 41.5, h: 9.5, label: "Standar 5: PERAN KEPEMIMPINAN (Keluar di UAB No.32)", color: "#B8332A" },
        { x: 36.5, y: 49.5, w: 34.5, h: 9.5, label: "Standar 6: Pendidikan Staf tentang Keselamatan Pasien", color: "#0F5C4D" },
        { x: 33.5, y: 74.8, w: 41.5, h: 13.5, label: "Standar 7: Komunikasi merupakan Kunci bagi Staf", color: "#1B5E7A" }
      ],
      32: [
        { x: 15.5, y: 5.0, w: 71.5, h: 8.5, label: "Kerangka 2: 6 Sasaran Keselamatan Pasien (SKP)", color: "#0F5C4D" },
        { x: 10.0, y: 26.5, w: 70.0, h: 12.0, label: "SKP 1: Ketepatan Identifikasi Pasien (UAB BDT-1 Hal.5)", color: "#B8332A" },
        { x: 10.0, y: 45.8, w: 72.0, h: 14.5, label: "SKP 2: Peningkatan Komunikasi yang Efektif (TBaK / SBAR)", color: "#0F5C4D" },
        { x: 10.0, y: 68.0, w: 70.0, h: 14.5, label: "SKP 3: Keamanan Obat yang Perlu Diwaspadai (High-Alert)", color: "#B26200" }
      ],
      33: [
        { x: 10.0, y: 23.0, w: 73.0, h: 14.8, label: "SKP 4: Tepat-Lokasi, Tepat-Prosedur, Tepat-Pasien Operasi", color: "#B8332A" },
        { x: 10.0, y: 45.8, w: 68.5, h: 14.8, label: "SKP 5: Pengurangan Risiko Infeksi (Hand Hygiene 5 Moments)", color: "#0F5C4D" },
        { x: 10.0, y: 68.0, w: 65.5, h: 14.8, label: "SKP 6: Pengurangan Risiko Cedera Pasien Akibat Terjatuh", color: "#B26200" }
      ],
      34: [
        { x: 25.5, y: 24.0, w: 59.0, h: 14.5, label: "Wajib Minimal 2 Identitas (Nama, Tgl Lahir, No RM, NIK)", color: "#0F5C4D" },
        { x: 40.5, y: 66.0, w: 30.0, h: 9.5, label: "BENAR: Pertanyaan Terbuka 'Siapa nama Bapak?'", color: "#0F5C4D" },
        { x: 40.5, y: 75.5, w: 30.0, h: 9.5, label: "SALAH: Pertanyaan Tertutup 'Apakah Bapak Tn. Budi?'", color: "#B8332A" }
      ],
      35: [
        { x: 6.5, y: 39.0, w: 28.0, h: 29.0, label: "Gelang MERAH = Alergi Obat / Makanan Tinggi", color: "#B8332A" },
        { x: 37.5, y: 38.0, w: 24.5, h: 28.0, label: "Gelang KUNING = Risiko Jatuh Tinggi (Morse/Humpty Dumpty)", color: "#B26200" },
        { x: 61.5, y: 37.0, w: 26.5, h: 31.0, label: "Gelang BIRU = Identitas Pasien Laki-Laki (Pink = Perempuan)", color: "#1B5E7A" }
      ],
      41: [
        { x: 47.0, y: 55.0, w: 50.0, h: 11.5, label: "STEMPEL NOTASI VERIFIKASI: Tgl, Jam, Paraf Petugas & DPJP", color: "#0F5C4D" }
      ],
      42: [
        { x: 14.0, y: 33.8, w: 67.0, h: 9.0, label: "Komponen Resep Lengkap: Nama Pasien, Tgl/Jam, Nama Obat", color: "#0F5C4D" },
        { x: 13.5, y: 56.5, w: 70.0, h: 14.0, label: "Frekuensi, Durasi, Dosis & Unit (mg/unit), Rute Pemberian", color: "#1B5E7A" }
      ],
      43: [
        { x: 20.0, y: 8.5, w: 60.0, h: 9.0, label: "SKP 3: High-Alert Medications", color: "#B8332A" },
        { x: 34.5, y: 38.5, w: 47.5, h: 46.0, label: "3 Kelompok: Look-Alike Sound-Alike (LASA) & Elektrolit Konsentrat", color: "#B26200" }
      ],
      46: [
        { x: 22.0, y: 35.8, w: 18.0, h: 13.5, label: "1. Concentrated Potassium Chloride (KCl ≥ 2 mEq/mL)", color: "#B8332A" },
        { x: 22.0, y: 62.8, w: 18.0, h: 10.0, label: "2. Concentrated Heparin / Antikoagulan", color: "#B26200" },
        { x: 66.0, y: 39.5, w: 19.0, h: 31.0, label: "3. Dextrose Hipertonik (≥20%) & NaCl Hipertonik (>0,9%)", color: "#0F5C4D" }
      ],
      47: [
        { x: 10.5, y: 21.5, w: 48.0, h: 5.5, label: "1. Beri label High-Risk / High-Alert yang jelas", color: "#B8332A" },
        { x: 10.5, y: 28.0, w: 65.0, h: 5.5, label: "2. Pisahkan obat LASA (Tall Man Lettering)", color: "#0F5C4D" },
        { x: 10.5, y: 40.8, w: 68.0, h: 11.0, label: "4. TARIK Elektrolit Pekat (KCl) dari Ruang Rawat Biasa!", color: "#B8332A" }
      ],
      48: [
        { x: 3.0, y: 21.5, w: 30.0, h: 15.0, label: "Pengecoh Opsi A: Distinct Packaging (Kemasan Berbeda)", color: "#B26200" },
        { x: 3.8, y: 55.0, w: 30.0, h: 15.0, label: "Pengecoh Opsi E: Prominent Warning (Peringatan Mencolok)", color: "#B26200" },
        { x: 40.0, y: 53.5, w: 21.5, h: 17.5, label: "KUNCI REMIDI BDT No.39: Label 'HIGH ALERT! MEDICATION'", color: "#B8332A" }
      ],
      51: [
        { x: 29.0, y: 28.0, w: 56.0, h: 43.0, label: "6 Ceklis Pra-Insisi: Identitas, Sisi/Lokasi, Prosedur, Posisi, Implan", color: "#0F5C4D" },
        { x: 30.0, y: 84.0, w: 46.0, h: 9.5, label: "WAJIB TIME-OUT Tepat Sebelum Insisi Kulit Dimulai!", color: "#B8332A" }
      ],
      54: [
        { x: 5.5, y: 24.5, w: 88.0, h: 14.5, label: "#1 KUNCI UAB No.43: Komunikasi tidak efektif antar tim bedah", color: "#B8332A" },
        { x: 5.5, y: 48.8, w: 73.0, h: 14.5, label: "#3: Kurang melibatkan pasien dalam menandai lokasi (Marking)", color: "#0F5C4D" },
        { x: 5.5, y: 64.5, w: 70.0, h: 14.5, label: "#4: Kurangnya standar prosedur verifikasi lokasi operasi", color: "#1B5E7A" }
      ],
      61: [
        { x: 15.0, y: 6.0, w: 69.5, h: 8.0, label: "Kerangka 3: 7 LANGKAH Menuju Keselamatan Pasien", color: "#B26200" },
        { x: 32.0, y: 31.5, w: 40.0, h: 4.8, label: "Step 2: Memimpin dan mendukung staf (Pengecoh Soal Standar!)", color: "#B8332A" },
        { x: 31.0, y: 54.8, w: 42.0, h: 4.8, label: "Step 4: Mengembangkan sistem pelaporan (Pengecoh Soal Standar!)", color: "#B8332A" }
      ],
      69: [
        { x: 8.0, y: 52.0, w: 24.0, h: 22.0, label: "Batas Pelaporan Internal: MAKSIMAL 2 x 24 JAM", color: "#B8332A" },
        { x: 39.0, y: 42.0, w: 24.5, h: 22.0, label: "Tentukan Derajat Insiden (Grading) & Lakukan RCA (UAB 22 No.85)", color: "#0F5C4D" },
        { x: 70.0, y: 31.8, w: 24.5, h: 7.0, label: "Sifat Laporan: Rahasia & Non-Punitive (Tidak Menyalahkan)", color: "#1B5E7A" }
      ],
      71: [
        { x: 13.8, y: 28.0, w: 76.2, h: 3.8, label: "Aturan Formulir: RAHASIA, TIDAK BOLEH DIFOTOCOPY, MAKS 2x24 JAM", color: "#B8332A" },
        { x: 17.0, y: 88.0, w: 69.0, h: 8.5, label: "Jenis Insiden yang Dilaporkan: KNC (Near Miss), KTD, & Sentinel", color: "#0F5C4D" }
      ],
      73: [
        { x: 10.0, y: 84.8, w: 54.0, h: 5.5, label: "Grading Risiko: BIRU / HIJAU (Sederhana) vs KUNING / MERAH (RCA)", color: "#B8332A" }
      ],
      75: [
        { x: 39.5, y: 18.0, w: 52.0, h: 27.5, label: "KUNCI UAB 22 No.85: Analisis Akar Penyebab Masalah (RCA)", color: "#0F5C4D" },
        { x: 39.5, y: 46.0, w: 52.0, h: 27.5, label: "Fokus: BUKAN menyalahkan individu, tapi BAGAIMANA & MENGAPA", color: "#B8332A" }
      ]
    },
    "EMN_KUL2": {
      3: [
        { x: 7.0, y: 35.5, w: 40.0, h: 39.5, label: "Kasus Pemicu: Pria 62 thn, Metformin lama, Kesemutan, MCV 112 fL", color: "#B8332A" },
        { x: 66.0, y: 28.0, w: 25.0, h: 31.0, label: "Target Diagnosis: Defisiensi Vitamin B12 (Kobalamin)", color: "#0F5C4D" }
      ],
      5: [
        { x: 7.5, y: 26.5, w: 31.0, h: 14.0, label: "Jalur 1: Asupan Kurang (Diet restriktif, alkohol)", color: "#0F5C4D" },
        { x: 53.5, y: 26.5, w: 36.0, h: 14.0, label: "Jalur 2: Gangguan Absorpsi (Ileum, bariatrik, kolestasis)", color: "#1B5E7A" },
        { x: 53.5, y: 50.0, w: 41.0, h: 15.5, label: "Jalur 4 Interaksi Obat: Metformin→B12, Isoniazid→B6, Warfarin→Vit K", color: "#B8332A" }
      ],
      8: [
        { x: 22.0, y: 26.5, w: 30.5, h: 29.5, label: "Fisiologi Vit A: Retinal (Rodopsin) vs Retinoat (Epitel)", color: "#0F5C4D" },
        { x: 58.0, y: 26.5, w: 26.5, h: 29.5, label: "Spektrum Klinis: Nyctalopia → Xerophthalmia/Bitot → Keratomalasia", color: "#B8332A" }
      ],
      9: [
        { x: 8.5, y: 28.5, w: 86.5, h: 13.0, label: "Jalur Aktivasi: Kulit (D3) → Hati (25-OH-D) → Ginjal (1,25-(OH)2-D)", color: "#0F5C4D" },
        { x: 7.5, y: 54.0, w: 81.5, h: 11.5, label: "Anak (Lempeng Epifisis Terbuka) = Rakitis vs Dewasa = Osteomalasia", color: "#B8332A" },
        { x: 12.0, y: 81.8, w: 77.0, h: 5.5, label: "Baku Emas Lab Status Vitamin D = 25(OH)D (Kalsidiol)", color: "#B26200" }
      ],
      11: [
        { x: 9.5, y: 32.5, w: 34.0, h: 37.5, label: "Kofaktor TPP: Piruvat DH, α-Ketoglutarat DH, Transketolase", color: "#0F5C4D" },
        { x: 50.5, y: 27.0, w: 40.0, h: 32.0, label: "3 Sindrom B1: Beriberi Kering, Beriberi Basah, Ensefalopati Wernicke", color: "#B8332A" }
      ],
      17: [
        { x: 6.5, y: 36.8, w: 83.0, h: 14.5, label: "Persamaan B9 & B12: MCV > 100 fL, tapi Neuropati KHAS pada B12!", color: "#B8332A" },
        { x: 6.5, y: 64.8, w: 80.0, h: 5.2, label: "Pembeda Lab Spesifik: Methylmalonic Acid (MMA) NAIK hanya pada B12", color: "#0F5C4D" },
        { x: 13.5, y: 85.8, w: 73.0, h: 5.0, label: "Jebakan Terapi: Beri Folat saja pada defisiensi B12 memperparah saraf!", color: "#B8332A" }
      ],
      24: [
        { x: 8.5, y: 29.0, w: 42.5, h: 35.5, label: "Kasus 1: Metformin + Kesemutan + Gangguan Vibrasi + MCV 112 fL", color: "#B8332A" },
        { x: 66.5, y: 41.0, w: 21.5, h: 34.5, label: "Kunci Slide 24: Defisiensi B12 → Cek B12 Serum, CBC/Smear, & MMA", color: "#0F5C4D" }
      ],
      26: [
        { x: 8.0, y: 30.8, w: 48.5, h: 36.5, label: "Kasus 3: Gusi berdarah + Petechiae perifolikular + PT/INR NORMAL", color: "#B8332A" },
        { x: 65.0, y: 26.5, w: 23.5, h: 46.0, label: "Kunci Slide 26: Skorbut (Defisiensi Vit C) — Defek Kolagen Kapiler", color: "#0F5C4D" }
      ]
    }
  };

  // =========================================================================
  // 2. CYTOSCAPE.JS INTERACTIVE PATHWAY GRAPH DEFINITIONS
  // =========================================================================
  const PATHWAY_GRAPHS = {
    "BDT_KUL3": {
      nodes: [
        { data: { id: "skp1", label: "SKP 1: Identifikasi\n(Min. 2 Identitas & Gelang)", category: "defense", slide: 35, group: "skp" } },
        { data: { id: "skp2", label: "SKP 2: Komunikasi\n(TBaK 1x24J & SBAR)", category: "defense", slide: 41, group: "skp" } },
        { data: { id: "skp3", label: "SKP 3: High-Alert\n(KCl Pekat & LASA)", category: "defense", slide: 48, group: "highalert" } },
        { data: { id: "skp4", label: "SKP 4: Operasi Aman\n(Marking & Time-Out)", category: "defense", slide: 54, group: "surgery" } },
        { data: { id: "skp5", label: "SKP 5: Hand Hygiene\n(5 Moments WHO)", category: "defense", slide: 33, group: "skp" } },
        { data: { id: "skp6", label: "SKP 6: Risiko Jatuh\n(Gelang Kuning)", category: "defense", slide: 35, group: "rca" } },
        { data: { id: "kpc", label: "KPC (Potensial Cedera)\nAlat rusak / stok menumpuk", category: "incident", slide: 18, group: "insiden" } },
        { data: { id: "knc", label: "KNC (Near Miss)\nSalah siapkan obat, belum diberi", category: "incident", slide: 18, group: "insiden" } },
        { data: { id: "ktc", label: "KTC (Tanpa Cedera)\nSudah terpapar, pasien aman", category: "incident", slide: 18, group: "insiden" } },
        { data: { id: "ktd", label: "KTD (Adverse Event)\nPasien mengalami cedera", category: "danger", slide: 18, group: "insiden" } },
        { data: { id: "sentinel", label: "SENTINEL EVENT\nKematian / Salah Sisi Operasi", category: "danger", slide: 18, group: "insiden" } },
        { data: { id: "lapor", label: "Laporan Insiden Internal\nMaksimal 2 x 24 Jam", category: "action", slide: 69, group: "rca" } },
        { data: { id: "biruhijau", label: "Grading BIRU / HIJAU\nInvestigasi Sederhana (1-2 mgg)", category: "action", slide: 73, group: "rca" } },
        { data: { id: "kuningmerah", label: "Grading KUNING / MERAH\nRoot Cause Analysis (RCA ≤45 hr)", category: "danger", slide: 75, group: "rca" } }
      ],
      edges: [
        { data: { source: "skp1", target: "knc", label: "Cegah salah pasien" } },
        { data: { source: "skp2", target: "knc", label: "Baca ulang (Read Back)" } },
        { data: { source: "skp3", target: "sentinel", label: "Jika KCl salah suntik" } },
        { data: { source: "skp4", target: "sentinel", label: "Jika tanpa Time-Out" } },
        { data: { source: "skp6", target: "ktd", label: "Pasien jatuh saat transfer" } },
        { data: { source: "kpc", target: "knc", label: "Bila terjadi error" } },
        { data: { source: "knc", target: "ktc", label: "Lolos ke pasien (tanpa cedera)" } },
        { data: { source: "ktc", target: "ktd", label: "Timbul cedera klinis" } },
        { data: { source: "ktd", target: "sentinel", label: "Kematian / Cacat berat" } },
        { data: { source: "knc", target: "lapor", label: "Wajib lapor 2x24J" } },
        { data: { source: "ktd", target: "lapor", label: "Wajib lapor 2x24J" } },
        { data: { source: "sentinel", target: "lapor", label: "Wajib lapor segera" } },
        { data: { source: "lapor", target: "biruhijau", label: "Skor Risiko Rendah/Moderat" } },
        { data: { source: "lapor", target: "kuningmerah", label: "Skor Risiko Tinggi/Ekstrem" } }
      ]
    },
    "EMN_KUL2": {
      nodes: [
        { data: { id: "metformin", label: "Metformin Lama / Vegan /\nReseksi Ileum / Autoimun", category: "incident", slide: 5, group: "b12" } },
        { data: { id: "b12", label: "Defisiensi Vitamin B12\n(Kobalamin)", category: "danger", slide: 17, group: "b12" } },
        { data: { id: "b9", label: "Defisiensi Vitamin B9\n(Asam Folat)", category: "incident", slide: 17, group: "b12" } },
        { data: { id: "megalo", label: "Anemia Megaloblastik\n(MCV > 100 fL & Homosistein ↑)", category: "action", slide: 17, group: "b12" } },
        { data: { id: "mma", label: "Asam Metilmalonat (MMA) ↑\n& Demyelinisasi Saraf Tepi/Spinal", category: "danger", slide: 24, group: "b12" } },
        { data: { id: "alkohol", label: "Alkoholik Kronik / Hiperemesis\n+ Infus Glukosa Tanpa B1", category: "incident", slide: 11, group: "b1" } },
        { data: { id: "b1", label: "Defisiensi Tiamin (B1)\n(Kofaktor TPP Turun)", category: "danger", slide: 11, group: "b1" } },
        { data: { id: "wernicke", label: "Ensefalopati Wernicke &\nBeriberi Basah/Kering", category: "danger", slide: 11, group: "b1" } },
        { data: { id: "vitd", label: "Kulit (D3) → Hati (25-OH-D)\n→ Ginjal (1,25-(OH)2-D)", category: "defense", slide: 9, group: "vitd" } },
        { data: { id: "rakitis", label: "Anak: Rakitis\nDewasa: Osteomalasia", category: "action", slide: 9, group: "vitd" } },
        { data: { id: "vitc", label: "Defisiensi Vit C (Skorbut)\nGagal Hidroksilasi Kolagen", category: "danger", slide: 26, group: "bleed" } },
        { data: { id: "vitk", label: "Defisiensi Vit K\nFaktor II, VII, IX, X Turun", category: "danger", slide: 19, group: "bleed" } },
        { data: { id: "ptnorm", label: "Gusi Berdarah + Petechiae\nTETAPI PT/INR NORMAL", category: "action", slide: 26, group: "bleed" } },
        { data: { id: "ptlong", label: "Perdarahan Aktif +\nPT/INR MEMANJANG", category: "danger", slide: 19, group: "bleed" } }
      ],
      edges: [
        { data: { source: "metformin", target: "b12", label: "Ganggu absorpsi ileum" } },
        { data: { source: "b12", target: "megalo", label: "Hambat sintesis DNA" } },
        { data: { source: "b9", target: "megalo", label: "Hambat sintesis timidilat" } },
        { data: { source: "b12", target: "mma", label: "Spesifik B12 (B9 normal!)" } },
        { data: { source: "alkohol", target: "b1", label: "Kuras cadangan TPP" } },
        { data: { source: "b1", target: "wernicke", label: "Gagal PDH & Transketolase" } },
        { data: { source: "vitd", target: "rakitis", label: "Bila 25(OH)D rendah" } },
        { data: { source: "vitc", target: "ptnorm", label: "Kapiler rapuh, koagulasi utuh" } },
        { data: { source: "vitk", target: "ptlong", label: "Gagal karboksilasi glutamat" } }
      ]
    }
  };

  // =========================================================================
  // 3. DETECT CURRENT MODULE KEY
  // =========================================================================
  function getModuleKey() {
    const path = window.location.pathname;
    if (path.includes("KUL2") || document.title.includes("Defisiensi Vitamin")) {
      return "EMN_KUL2";
    }
    return "BDT_KUL3";
  }

  // =========================================================================
  // 4. INITIALIZE DEXIE.JS (INDEXEDDB) + TS-FSRS SCHEDULER
  // =========================================================================
  let db = null;
  let fsrsScheduler = null;

  function initFSRSAndDB() {
    if (window.FSRS && typeof window.FSRS.fsrs === "function") {
      fsrsScheduler = window.FSRS.fsrs({
        request_retention: 0.9,
        maximum_interval: 365,
        enable_fuzz: false
      });
    }
    if (window.Dexie) {
      db = new window.Dexie("VertexPrepStudyDB");
      db.version(1).stores({
        cards: "id, moduleKey, itemType, slideNo, due, stability, difficulty, reps, lapses, lastError"
      });
    }
  }

  async function getCardRecord(id, moduleKey, itemType, slideNo, title) {
    const fallbackKey = "vertex_fsrs_" + id;
    if (db) {
      try {
        const existing = await db.cards.get(id);
        if (existing) return existing;
      } catch (e) {}
    }
    const raw = localStorage.getItem(fallbackKey);
    if (raw) {
      try { return JSON.parse(raw); } catch (e) {}
    }
    const emptyCard = (window.FSRS && window.FSRS.createEmptyCard)
      ? window.FSRS.createEmptyCard(new Date())
      : { due: new Date().toISOString(), stability: 0, difficulty: 0, reps: 0, lapses: 0, state: 0 };

    return {
      id,
      moduleKey,
      itemType,
      slideNo,
      title,
      card: emptyCard,
      due: new Date(emptyCard.due).getTime(),
      stability: 0,
      difficulty: 0,
      reps: 0,
      lapses: 0,
      lastError: ""
    };
  }

  async function saveCardRecord(rec) {
    const fallbackKey = "vertex_fsrs_" + rec.id;
    localStorage.setItem(fallbackKey, JSON.stringify(rec));
    if (db) {
      try {
        await db.cards.put(rec);
      } catch (e) {}
    }
    updateFSRSDashboard();
  }

  async function rateStudyItem(id, ratingNum, title, slideNo, errorCode) {
    const moduleKey = getModuleKey();
    const rec = await getCardRecord(id, moduleKey, "slide_core", slideNo, title);
    const now = new Date();
    if (fsrsScheduler && window.FSRS) {
      const res = fsrsScheduler.next(rec.card, now, ratingNum);
      rec.card = res.card;
      rec.due = new Date(res.card.due).getTime();
      rec.stability = Number((res.card.stability || 0).toFixed(2));
      rec.difficulty = Number((res.card.difficulty || 0).toFixed(2));
      rec.reps = res.card.reps || 0;
      rec.lapses = res.card.lapses || 0;
    } else {
      rec.reps += 1;
      rec.stability = ratingNum === 1 ? 0.5 : ratingNum * 2.5;
      rec.difficulty = ratingNum === 1 ? 8.2 : 4.5;
      rec.due = Date.now() + rec.stability * 86400000;
    }
    if (errorCode) {
      rec.lastError = errorCode;
    } else if (ratingNum >= 3) {
      rec.lastError = "";
    }
    await saveCardRecord(rec);
    return rec;
  }

  function formatIntervalDays(dueDate) {
    const diffMs = new Date(dueDate).getTime() - Date.now();
    const mins = Math.max(1, Math.round(diffMs / 60000));
    if (mins < 60) return mins + " mnt";
    const hrs = Math.round(mins / 60);
    if (hrs < 24) return hrs + " jam";
    const days = Math.round(hrs / 24);
    return days + " hari";
  }

  // =========================================================================
  // 5. ENHANCE SLIDE FRAMES WITH SVG.JS BOUNDING-BOX HIGHLIGHT & OCCLUSION
  // =========================================================================
  function enhanceSlideFrames() {
    const moduleKey = getModuleKey();
    const moduleBoxes = SLIDE_BOXES[moduleKey] || {};
    const frames = document.querySelectorAll(".slide-frame");

    frames.forEach((frame, frameIdx) => {
      if (frame.dataset.svgEnhanced === "1") return;
      frame.dataset.svgEnhanced = "1";

      const img = frame.querySelector("img");
      if (!img) return;
      const src = img.getAttribute("src") || "";
      const match = src.match(/slide_(\d+)\.jpg/);
      if (!match) return;
      const slideNo = parseInt(match[1], 10);
      const boxes = moduleBoxes[slideNo] || [
        { x: 10, y: 22, w: 80, h: 24, label: "Area Konsep Utama Slide " + slideNo, color: "#0F5C4D" },
        { x: 10, y: 54, w: 80, h: 24, label: "Detail Klinis & Poin Ujian Slide " + slideNo, color: "#B8332A" }
      ];

      // Build Mode Control Bar inside .slide-frame-bar
      const bar = frame.querySelector(".slide-frame-bar");
      if (bar) {
        const modeGroup = document.createElement("div");
        modeGroup.className = "svg-mode-group";
        modeGroup.innerHTML = `
          <button type="button" class="svg-mode-btn active" data-mode="highlight" title="Sorot koordinat bukti kalimat pada slide (PyMuPDF/Docling)">Sorot Bukti</button>
          <button type="button" class="svg-mode-btn" data-mode="occlusion" title="Tutup bagian penting slide untuk latihan tebak aktif (Image Occlusion)">Uji Gambar (${boxes.length})</button>
          <button type="button" class="svg-mode-btn" data-mode="clean" title="Tampilkan slide asli tanpa kotak sorotan">Polos</button>
        `;
        bar.appendChild(modeGroup);
      }

      // Wrap image in relative container for SVG overlay
      const wrap = document.createElement("div");
      wrap.className = "slide-svg-stage";
      img.parentNode.insertBefore(wrap, img);
      wrap.appendChild(img);

      const overlay = document.createElement("div");
      overlay.className = "slide-svg-overlay";
      wrap.appendChild(overlay);

      // Render SVG via @svgdotjs/svg.js if available, or native SVG
      let currentMode = "highlight";
      let occludedState = boxes.map(() => true);

      function renderOverlay() {
        overlay.innerHTML = "";
        if (currentMode === "clean") {
          overlay.style.pointerEvents = "none";
          return;
        }

        const svgNS = "http://www.w3.org/2000/svg";
        const svgEl = document.createElementNS(svgNS, "svg");
        svgEl.setAttribute("viewBox", "0 0 1000 750");
        svgEl.setAttribute("preserveAspectRatio", "none");
        svgEl.style.width = "100%";
        svgEl.style.height = "100%";
        svgEl.style.display = "block";

        boxes.forEach((b, i) => {
          const rx = (b.x / 100) * 1000;
          const ry = (b.y / 100) * 750;
          const rw = (b.w / 100) * 1000;
          const rh = (b.h / 100) * 750;

          const g = document.createElementNS(svgNS, "g");

          if (currentMode === "highlight") {
            const rect = document.createElementNS(svgNS, "rect");
            rect.setAttribute("x", rx);
            rect.setAttribute("y", ry);
            rect.setAttribute("width", rw);
            rect.setAttribute("height", rh);
            rect.setAttribute("rx", "10");
            rect.setAttribute("fill", b.color === "#B8332A" ? "rgba(184, 51, 42, 0.14)" : "rgba(15, 92, 77, 0.14)");
            rect.setAttribute("stroke", b.color || "#0F5C4D");
            rect.setAttribute("stroke-width", "4");
            rect.setAttribute("stroke-dasharray", "10,5");
            g.appendChild(rect);

            // Corner number tag
            const tagBg = document.createElementNS(svgNS, "rect");
            tagBg.setAttribute("x", rx);
            tagBg.setAttribute("y", Math.max(4, ry - 28));
            tagBg.setAttribute("width", Math.min(920 - rx, Math.max(180, b.label.length * 10.5)));
            tagBg.setAttribute("height", "28");
            tagBg.setAttribute("rx", "6");
            tagBg.setAttribute("fill", b.color || "#0F5C4D");
            g.appendChild(tagBg);

            const txt = document.createElementNS(svgNS, "text");
            txt.setAttribute("x", rx + 10);
            txt.setAttribute("y", Math.max(23, ry - 9));
            txt.setAttribute("fill", "#FFFFFF");
            txt.setAttribute("font-size", "16");
            txt.setAttribute("font-weight", "700");
            txt.setAttribute("font-family", "Plus Jakarta Sans, sans-serif");
            txt.textContent = `#${i + 1} ${b.label.slice(0, 48)}`;
            g.appendChild(txt);
          } else if (currentMode === "occlusion") {
            const isMasked = occludedState[i];
            const rect = document.createElementNS(svgNS, "rect");
            rect.setAttribute("x", rx);
            rect.setAttribute("y", ry);
            rect.setAttribute("width", rw);
            rect.setAttribute("height", rh);
            rect.setAttribute("rx", "10");
            rect.setAttribute("fill", isMasked ? "#0F1C24" : "rgba(15, 92, 77, 0.12)");
            rect.setAttribute("stroke", isMasked ? "#0F5C4D" : "#0F5C4D");
            rect.setAttribute("stroke-width", "4");
            rect.style.cursor = "pointer";
            g.appendChild(rect);

            const txt = document.createElementNS(svgNS, "text");
            txt.setAttribute("x", rx + rw / 2);
            txt.setAttribute("y", ry + rh / 2 + 6);
            txt.setAttribute("text-anchor", "middle");
            txt.setAttribute("fill", isMasked ? "#FFFFFF" : "#0F5C4D");
            txt.setAttribute("font-size", "19");
            txt.setAttribute("font-weight", "700");
            txt.setAttribute("font-family", "Plus Jakarta Sans, sans-serif");
            txt.style.pointerEvents = "none";
            txt.textContent = isMasked
              ? `[Tutup #${i + 1}] Klik untuk Tebak & Buka`
              : `✓ ${b.label.slice(0, 42)}`;
            g.appendChild(txt);

            g.addEventListener("click", (ev) => {
              ev.stopPropagation();
              occludedState[i] = !occludedState[i];
              renderOverlay();
            });
          }

          svgEl.appendChild(g);
        });

        overlay.style.pointerEvents = currentMode === "occlusion" ? "auto" : "none";
        overlay.appendChild(svgEl);
      }

      renderOverlay();

      if (bar) {
        bar.querySelectorAll(".svg-mode-btn").forEach((btn) => {
          btn.addEventListener("click", (ev) => {
            ev.stopPropagation();
            bar.querySelectorAll(".svg-mode-btn").forEach((b) => b.classList.remove("active"));
            btn.classList.add("active");
            currentMode = btn.dataset.mode;
            if (currentMode === "occlusion") {
              occludedState = boxes.map(() => true);
            }
            renderOverlay();
          });
        });
      }

      // Add FSRS Rating Bar at the bottom of the slide frame
      const cardId = `${moduleKey}_slide_${slideNo}_f${frameIdx}`;
      const fsrsBar = document.createElement("div");
      fsrsBar.className = "fsrs-slide-bar";
      fsrsBar.innerHTML = `
        <div class="fsrs-bar-top">
          <span class="fsrs-status-label" id="fsrs-lbl-${cardId}">FSRS Memory: Belum Direview</span>
          <div class="fsrs-btn-row">
            <button type="button" class="fsrs-rate-btn rate-again" data-rate="1">Ulangi</button>
            <button type="button" class="fsrs-rate-btn rate-hard" data-rate="2">Sulit</button>
            <button type="button" class="fsrs-rate-btn rate-good" data-rate="3">Paham</button>
            <button type="button" class="fsrs-rate-btn rate-easy" data-rate="4">Mudah</button>
          </div>
        </div>
      `;
      frame.appendChild(fsrsBar);

      // Load initial saved state
      getCardRecord(cardId, moduleKey, "slide_core", slideNo, `Slide ${slideNo}`).then((rec) => {
        const lbl = document.getElementById(`fsrs-lbl-${cardId}`);
        if (lbl && rec.reps > 0) {
          lbl.textContent = `FSRS: S=${rec.stability}h · D=${rec.difficulty} · Review: ${formatIntervalDays(rec.due)}`;
        }
      });

      fsrsBar.querySelectorAll(".fsrs-rate-btn").forEach((btn) => {
        btn.addEventListener("click", async (ev) => {
          ev.stopPropagation();
          const r = parseInt(btn.dataset.rate, 10);
          const updated = await rateStudyItem(cardId, r, `Slide ${slideNo}`, slideNo, "");
          const lbl = document.getElementById(`fsrs-lbl-${cardId}`);
          if (lbl) {
            lbl.textContent = `FSRS Tersimpan: S=${updated.stability}h · D=${updated.difficulty} · Berikutnya: ${formatIntervalDays(updated.due)}`;
          }
        });
      });
    });
  }

  // =========================================================================
  // 6. INJECT TOP ECOSYSTEM COMMAND BAR + CMD+K MODAL + FSRS & CYTOSCAPE HUB
  // =========================================================================
  function injectEcosystemHub() {
    const moduleKey = getModuleKey();
    const isEMN = moduleKey === "EMN_KUL2";
    const ankiFile = isEMN
      ? "anki/VERTEX_EMN_KUL2_Defisiensi_Vitamin.apkg"
      : "anki/VERTEX_BDT_KUL3_Patient_Safety.apkg";

    // 1. Top Command Bar right above .topbar
    const topCommand = document.createElement("div");
    topCommand.className = "vertex-cmd-strip";
    topCommand.innerHTML = `
      <div class="vertex-cmd-inner">
        <div class="vertex-module-switcher">
          <span class="cmd-brand-pill">VERTEX-PREP 2.0</span>
          <a href="BDT_KUL3_Patient_Safety.html" class="mod-link ${!isEMN ? "active" : ""}">Blok 7 BDT · KUL 3 Patient Safety (80 Slide + 9 Soal UAB)</a>
          <a href="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html" class="mod-link ${isEMN ? "active" : ""}">Blok 9 EMN · KUL 2 Defisiensi Vitamin (28 Slide)</a>
        </div>
        <div class="vertex-cmd-actions">
          <button type="button" class="cmd-search-trigger" id="open-cmdk-btn">
            <span>Cari 2.633 Soal UAB & Slide Dosen</span>
            <kbd>⌘K</kbd>
          </button>
          <a href="${ankiFile}" download class="cmd-anki-btn" title="Generated via kerrickstaley/genanki">
            Download Anki (.apkg)
          </a>
        </div>
      </div>
    `;
    document.body.insertBefore(topCommand, document.body.firstChild);

    // 2. Inject Interactive Cytoscape.js Pathway Graph + FSRS Memory Hub right after .hero
    const hero = document.querySelector(".hero");
    if (hero && hero.parentNode) {
      const hubSection = document.createElement("section");
      hubSection.className = "vertex-interactive-hub";
      hubSection.innerHTML = `
        <div class="hub-header-row">
          <div>
            <div class="eyebrow">Integrasi 7 Repo Open-Source · Cytoscape.js + ts-fsrs + Dexie.js + PyMuPDF + SVG.js</div>
            <h2>Peta Jaringan Sebab-Akibat Interaktif & Jadwal Memori FSRS</h2>
            <p class="lead">Klik titik (node) pada grafik di bawah untuk menyalakan jalur kompensasi/eskalasi klinis dan langsung menampilkan bukti slide dosen di sebelah kanan.</p>
          </div>
          <div class="pathway-filter-bar" id="cy-filter-bar">
            <button type="button" class="cy-filter-btn active" data-group="all">Semua Jalur</button>
            ${!isEMN ? `
              <button type="button" class="cy-filter-btn" data-group="insiden">Tangga 5 Insiden (Slide 18)</button>
              <button type="button" class="cy-filter-btn" data-group="highalert">Obat High-Alert KCl (Slide 48)</button>
              <button type="button" class="cy-filter-btn" data-group="surgery">Time-Out Bedah (Slide 54)</button>
              <button type="button" class="cy-filter-btn" data-group="rca">Lapor 2x24J & RCA (Slide 69-75)</button>
            ` : `
              <button type="button" class="cy-filter-btn" data-group="b12">Jalur B12 vs B9 & MMA (Slide 17)</button>
              <button type="button" class="cy-filter-btn" data-group="b1">Jalur Tiamin B1 & Wernicke (Slide 11)</button>
              <button type="button" class="cy-filter-btn" data-group="vitd">Aktivasi Vit D & Tulang (Slide 9)</button>
              <button type="button" class="cy-filter-btn" data-group="bleed">Perdarahan Vit C vs Vit K (Slide 26)</button>
            `}
          </div>
        </div>

        <div class="cy-workspace-grid">
          <div class="cy-canvas-wrap">
            <div id="cy-pathway" class="cy-canvas"></div>
            <div class="cy-canvas-footer">
              <span>Engine: <code>cytoscape/cytoscape.js</code> · Scroll/Pinch untuk Zoom · Klik Node untuk Sorot Jalur & Slide</span>
              <button type="button" class="cy-reset-btn" id="cy-fit-btn">Reset Posisi Grafik</button>
            </div>
          </div>
          <div class="cy-inspector-panel" id="cy-inspector">
            <div class="eyebrow" id="cy-insp-badge">Bukti Slide Terhubung</div>
            <h3 id="cy-insp-title">${!isEMN ? "Slide 18 · Tangga 5 Insiden Keselamatan Pasien" : "Slide 17 · Pembeda Defisiensi B12 vs Folat (B9)"}</h3>
            <p id="cy-insp-desc">${!isEMN ? "Klik salah satu kotak pada peta jaringan di kiri untuk melihat hubungan antar-SKP, derajat insiden, hingga investigasi RCA beserta bukti slide aslinya." : "Klik salah satu kotak pada peta metabolik di kiri untuk menelusuri mengapa defisiensi vitamin memicu gejala organ dan perubahan laboratorium spesifik."}</p>
            <img id="cy-insp-img" src="${!isEMN ? "slides_bdt_kul3/slide_18.jpg" : "slides_kul2/slide_17.jpg"}" alt="Slide Inspector Proof" class="cy-insp-slide-img" onclick="if(window.openModal) window.openModal(this.src, document.getElementById('cy-insp-title').textContent)" />
          </div>
        </div>

        <div class="fsrs-dashboard-strip" id="fsrs-dashboard">
          <div class="fsrs-metric-box">
            <div class="fsrs-metric-lbl">Engine Jadwal Memori</div>
            <div class="fsrs-metric-val">FSRS v6 + Dexie.js</div>
            <div class="fsrs-metric-sub">open-spaced-repetition/ts-fsrs</div>
          </div>
          <div class="fsrs-metric-box">
            <div class="fsrs-metric-lbl">Kartu & Soal Tercatat</div>
            <div class="fsrs-metric-val" id="fsrs-stat-count">0 Item</div>
            <div class="fsrs-metric-sub" id="fsrs-stat-reps">0 total pengulangan aktif</div>
          </div>
          <div class="fsrs-metric-box">
            <div class="fsrs-metric-lbl">Rata-rata Stabilitas (S)</div>
            <div class="fsrs-metric-val" id="fsrs-stat-stab">0.0 Hari</div>
            <div class="fsrs-metric-sub">Target retensi memori 90%</div>
          </div>
          <div class="fsrs-metric-box">
            <div class="fsrs-metric-lbl">Antrean Wajib Review & Error</div>
            <div class="fsrs-metric-val" id="fsrs-stat-due">0 Item</div>
            <div class="fsrs-metric-sub" id="fsrs-stat-errors">Belum ada error E1–E6 tercatat</div>
          </div>
        </div>
      `;
      hero.parentNode.insertBefore(hubSection, hero.nextSibling);
    }

    // 3. Inject Cmd+K Search Modal
    const modal = document.createElement("div");
    modal.className = "cmdk-backdrop";
    modal.id = "cmdk-modal";
    modal.innerHTML = `
      <div class="cmdk-dialog" onclick="event.stopPropagation()">
        <div class="cmdk-input-row">
          <span class="cmdk-icon">⌕</span>
          <input type="text" id="cmdk-input" class="cmdk-input" placeholder="Ketik kata kunci soal UAB / slide (contoh: Sentinel, KCl, Gelang, B12, Metformin, Skorbut, Anemia)..." autocomplete="off" />
          <button type="button" class="cmdk-close-btn" id="close-cmdk-btn">ESC</button>
        </div>
        <div class="cmdk-filter-row" id="cmdk-filters">
          <button type="button" class="cmdk-pill active" data-filter="ALL">Semua Sumber</button>
          <button type="button" class="cmdk-pill" data-filter="SLIDE DOSEN">Slide Dosen (108)</button>
          <button type="button" class="cmdk-pill" data-filter="BDT">UAB BDT</button>
          <button type="button" class="cmdk-pill" data-filter="BMD">UAB BMD</button>
          <button type="button" class="cmdk-pill" data-filter="BMS 1">UAB BMS 1</button>
          <button type="button" class="cmdk-pill" data-filter="BMS 2">UAB BMS 2</button>
          <button type="button" class="cmdk-pill" data-filter="BMS 3">UAB BMS 3</button>
          <button type="button" class="cmdk-pill" data-filter="BMS 4">UAB BMS 4</button>
          <button type="button" class="cmdk-pill" data-filter="HI">UAB HI</button>
          <button type="button" class="cmdk-pill" data-filter="BUAMS">UAB BUAMS</button>
        </div>
        <div class="cmdk-meta-bar" id="cmdk-meta">Menampilkan indeks 51 file Bank Soal UAB & 108 Slide Kuliah</div>
        <div class="cmdk-results" id="cmdk-results"></div>
      </div>
    `;
    document.body.appendChild(modal);

    setupCmdKSearch();
    initCytoscapeGraph();
    hookQuizButtonsToFSRS();
    updateFSRSDashboard();
  }

  // =========================================================================
  // 7. CYTOSCAPE.JS INITIALIZATION
  // =========================================================================
  function initCytoscapeGraph() {
    const container = document.getElementById("cy-pathway");
    if (!container || !window.cytoscape) return;

    const moduleKey = getModuleKey();
    const isEMN = moduleKey === "EMN_KUL2";
    const graphData = PATHWAY_GRAPHS[moduleKey] || PATHWAY_GRAPHS["BDT_KUL3"];

    const cy = window.cytoscape({
      container,
      elements: [...graphData.nodes, ...graphData.edges],
      style: [
        {
          selector: "node",
          style: {
            "label": "data(label)",
            "text-wrap": "wrap",
            "text-max-width": "150px",
            "font-family": "Plus Jakarta Sans, sans-serif",
            "font-size": "11px",
            "font-weight": "700",
            "color": "#0F1C24",
            "text-valign": "center",
            "text-halign": "center",
            "background-color": "#FFFFFF",
            "border-width": 2.5,
            "border-color": "#0F5C4D",
            "shape": "round-rectangle",
            "width": "158px",
            "height": "54px",
            "padding": "8px"
          }
        },
        {
          selector: 'node[category = "danger"]',
          style: {
            "border-color": "#B8332A",
            "background-color": "#FDF3F2",
            "color": "#7A1C16"
          }
        },
        {
          selector: 'node[category = "incident"]',
          style: {
            "border-color": "#B26200",
            "background-color": "#FEF8EC",
            "color": "#6E3B00"
          }
        },
        {
          selector: 'node[category = "action"]',
          style: {
            "border-color": "#1B5E7A",
            "background-color": "#F0F7FA",
            "color": "#0F3D52"
          }
        },
        {
          selector: "edge",
          style: {
            "width": 2.2,
            "line-color": "#94A7B5",
            "target-arrow-color": "#94A7B5",
            "target-arrow-shape": "triangle",
            "curve-style": "bezier",
            "label": "data(label)",
            "font-family": "Plus Jakarta Sans, sans-serif",
            "font-size": "9.5px",
            "font-weight": "600",
            "color": "#455866",
            "text-background-opacity": 1,
            "text-background-color": "#F3F6F8",
            "text-background-padding": "3px",
            "text-background-shape": "roundrectangle"
          }
        },
        {
          selector: ".highlighted",
          style: {
            "border-width": 4,
            "border-color": "#0F5C4D",
            "line-color": "#0F5C4D",
            "target-arrow-color": "#0F5C4D"
          }
        },
        {
          selector: ".dimmed",
          style: {
            "opacity": 0.25
          }
        }
      ],
      layout: {
        name: "breadthfirst",
        directed: true,
        padding: 24,
        spacingFactor: 1.12
      },
      userZoomingEnabled: true,
      userPanningEnabled: true,
      boxSelectionEnabled: false
    });

    cy.on("tap", "node", function (evt) {
      const node = evt.target;
      const slideNo = node.data("slide");
      const label = (node.data("label") || "").replace(/\n/g, " — ");

      cy.elements().removeClass("highlighted dimmed");
      const connected = node.closedNeighborhood();
      cy.elements().not(connected).addClass("dimmed");
      connected.addClass("highlighted");

      const titleEl = document.getElementById("cy-insp-title");
      const descEl = document.getElementById("cy-insp-desc");
      const imgEl = document.getElementById("cy-insp-img");
      const badgeEl = document.getElementById("cy-insp-badge");

      if (titleEl) titleEl.textContent = `Slide ${slideNo} · ${label}`;
      if (badgeEl) badgeEl.textContent = `Terhubung ke Slide ${slideNo} (Klik gambar untuk Zoom)`;
      if (imgEl) {
        imgEl.src = isEMN ? `slides_kul2/slide_${slideNo}.jpg` : `slides_bdt_kul3/slide_${slideNo}.jpg`;
      }
      if (descEl) {
        const boxes = (SLIDE_BOXES[moduleKey] && SLIDE_BOXES[moduleKey][slideNo]) || [];
        descEl.textContent = boxes.length
          ? "Bukti koordinat pada Slide " + slideNo + ": " + boxes.map((b) => b.label).join(" | ")
          : "Lihat detail visual langsung pada tangkapan layar Slide " + slideNo + " di bawah ini.";
      }
    });

    const fitBtn = document.getElementById("cy-fit-btn");
    if (fitBtn) {
      fitBtn.addEventListener("click", () => {
        cy.elements().removeClass("highlighted dimmed");
        cy.fit(undefined, 24);
      });
    }

    const filterBar = document.getElementById("cy-filter-bar");
    if (filterBar) {
      filterBar.querySelectorAll(".cy-filter-btn").forEach((btn) => {
        btn.addEventListener("click", () => {
          filterBar.querySelectorAll(".cy-filter-btn").forEach((b) => b.classList.remove("active"));
          btn.classList.add("active");
          const grp = btn.dataset.group;
          cy.elements().removeClass("highlighted dimmed");
          if (grp === "all") {
            cy.fit(undefined, 24);
            return;
          }
          const matchedNodes = cy.nodes().filter((n) => n.data("group") === grp);
          const hood = matchedNodes.closedNeighborhood();
          cy.elements().not(hood).addClass("dimmed");
          hood.addClass("highlighted");
        });
      });
    }
  }

  // =========================================================================
  // 8. HOOK CBT QUIZ ANSWERS TO TS-FSRS & DEXIE.JS
  // =========================================================================
  function hookQuizButtonsToFSRS() {
    const moduleKey = getModuleKey();
    document.addEventListener("click", async (ev) => {
      const btn = ev.target.closest(".opt-btn");
      if (!btn) return;
      const card = btn.closest(".q-card");
      if (!card) return;
      const qId = card.id || "q-unknown";
      // Check if answered right or wrong after the page's checkAnswer handler runs
      setTimeout(async () => {
        const isCorrect = btn.classList.contains("correct-choice");
        const isWrong = btn.classList.contains("wrong-choice");
        if (!isCorrect && !isWrong) return;
        const rating = isCorrect ? 3 : 1; // Good (3) vs Again (1)
        const errTag = card.querySelector(".err-tag");
        const errText = (!isCorrect && errTag) ? errTag.textContent.slice(0, 45) : "";
        await rateStudyItem(`${moduleKey}_${qId}`, rating, `Soal CBT ${qId.toUpperCase()}`, 0, errText);
      }, 60);
    });
  }

  async function updateFSRSDashboard() {
    let records = [];
    if (db) {
      try {
        records = await db.cards.toArray();
      } catch (e) {}
    }
    if (!records.length) {
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith("vertex_fsrs_")) {
          try { records.push(JSON.parse(localStorage.getItem(k))); } catch (e) {}
        }
      }
    }

    const active = records.filter((r) => r && r.reps > 0);
    const countEl = document.getElementById("fsrs-stat-count");
    const repsEl = document.getElementById("fsrs-stat-reps");
    const stabEl = document.getElementById("fsrs-stat-stab");
    const dueEl = document.getElementById("fsrs-stat-due");
    const errEl = document.getElementById("fsrs-stat-errors");

    if (!countEl) return;
    countEl.textContent = `${active.length} Item Aktif`;
    const totalReps = active.reduce((acc, r) => acc + (r.reps || 0), 0);
    if (repsEl) repsEl.textContent = `${totalReps} total review tersimpan di IndexedDB`;

    const avgStab = active.length
      ? (active.reduce((acc, r) => acc + (r.stability || 0), 0) / active.length).toFixed(1)
      : "0.0";
    if (stabEl) stabEl.textContent = `${avgStab} Hari`;

    const now = Date.now();
    const dueItems = active.filter((r) => (r.due || 0) <= now + 3600000 || r.lastError);
    if (dueEl) dueEl.textContent = `${dueItems.length} Perlu Review`;

    const errors = active.filter((r) => r.lastError).map((r) => r.lastError);
    if (errEl) {
      errEl.textContent = errors.length
        ? `Terdeteksi: ${errors.slice(0, 2).join(" · ")}`
        : "0 kesalahan aktif (Semua Paham)";
    }
  }

  // =========================================================================
  // 9. CMD + K INSTANT SEARCH ENGINE (2,633 UAB QUESTIONS + 108 SLIDES)
  // =========================================================================
  function setupCmdKSearch() {
    const modal = document.getElementById("cmdk-modal");
    const input = document.getElementById("cmdk-input");
    const resultsBox = document.getElementById("cmdk-results");
    const metaBar = document.getElementById("cmdk-meta");
    const openBtn = document.getElementById("open-cmdk-btn");
    const closeBtn = document.getElementById("close-cmdk-btn");
    const filterContainer = document.getElementById("cmdk-filters");

    let activeFilter = "ALL";

    function openSearch() {
      modal.classList.add("open");
      input.focus();
      runSearch();
    }

    function closeSearch() {
      modal.classList.remove("open");
    }

    if (openBtn) openBtn.addEventListener("click", openSearch);
    if (closeBtn) closeBtn.addEventListener("click", closeSearch);
    if (modal) modal.addEventListener("click", closeSearch);

    document.addEventListener("keydown", (e) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") {
        e.preventDefault();
        if (modal.classList.contains("open")) closeSearch();
        else openSearch();
      } else if (e.key === "Escape" && modal.classList.contains("open")) {
        closeSearch();
      }
    });

    if (filterContainer) {
      filterContainer.querySelectorAll(".cmdk-pill").forEach((pill) => {
        pill.addEventListener("click", () => {
          filterContainer.querySelectorAll(".cmdk-pill").forEach((p) => p.classList.remove("active"));
          pill.classList.add("active");
          activeFilter = pill.dataset.filter;
          runSearch();
        });
      });
    }

    if (input) {
      input.addEventListener("input", runSearch);
    }

    function escapeRegExp(str) {
      return str.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    }

    function highlightText(text, query) {
      if (!query) return text;
      const tokens = query.trim().split(/\s+/).filter((t) => t.length >= 2);
      if (!tokens.length) return text;
      const pattern = new RegExp(`(${tokens.map(escapeRegExp).join("|")})`, "gi");
      return text.replace(pattern, "<mark>$1</mark>");
    }

    function runSearch() {
      const index = window.VERTEX_SEARCH_INDEX || [];
      const q = (input ? input.value : "").trim().toLowerCase();
      const tokens = q.split(/\s+/).filter(Boolean);

      const t0 = performance.now();
      const matched = [];

      for (let i = 0; i < index.length; i++) {
        const item = index[i];
        if (activeFilter !== "ALL") {
          if (activeFilter === "SLIDE DOSEN" && item.type !== "SLIDE DOSEN") continue;
          if (activeFilter !== "SLIDE DOSEN" && item.block !== activeFilter) continue;
        }
        if (tokens.length > 0) {
          const hay = (item.source + " " + item.block + " " + item.text).toLowerCase();
          let ok = true;
          for (let t = 0; t < tokens.length; t++) {
            if (!hay.includes(tokens[t])) {
              ok = false;
              break;
            }
          }
          if (!ok) continue;
        }
        matched.push(item);
        if (matched.length >= 45) break;
      }

      const elapsed = (performance.now() - t0).toFixed(1);
      if (metaBar) {
        metaBar.textContent = `Ditemukan ${matched.length}${matched.length >= 45 ? "+" : ""} hasil dari ${index.length} item terindeks (${elapsed} ms) — Jujur Sumber: 51 File UAB Blok 1–8 & 108 Slide Dosen`;
      }

      if (!resultsBox) return;
      if (!matched.length) {
        resultsBox.innerHTML = `<div class="cmdk-empty">Tidak ditemukan kata kunci tersebut pada filter ini. Coba kata kunci lain (misal: <code>Sentinel</code>, <code>KCl</code>, <code>Anemia</code>, <code>B12</code>, <code>Gelang</code>).</div>`;
        return;
      }

      resultsBox.innerHTML = matched
        .map((item) => {
          const isSlide = item.type === "SLIDE DOSEN";
          const thumbHtml = isSlide && item.img
            ? `<img src="${item.img}" alt="${item.source}" class="cmdk-thumb" />`
            : "";
          return `
            <div class="cmdk-item" onclick="${item.url ? `window.location.href='${item.url}'` : ""}">
              ${thumbHtml}
              <div class="cmdk-item-body">
                <div class="cmdk-item-top">
                  <span class="cmdk-badge ${isSlide ? "badge-slide" : "badge-uab"}">${item.type} · ${item.block}</span>
                  <span class="cmdk-source">${highlightText(item.source, q)}</span>
                </div>
                <div class="cmdk-snippet">${highlightText(item.text, q)}</div>
              </div>
            </div>
          `;
        })
        .join("");
    }
  }

  // =========================================================================
  // BOOTSTRAP ON DOM READY
  // =========================================================================
  document.addEventListener("DOMContentLoaded", () => {
    initFSRSAndDB();
    enhanceSlideFrames();
    injectEcosystemHub();
  });
})();
