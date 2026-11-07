# VERTEX-PREP 2.0 — MASTER HANDOFF & STATE FILE
**User:** Mahasiswa Semester 3 FKIK UIN Maulana Malik Ibrahim Malang (Angkatan 2025 — "VERTEX")
**Lokasi Workspace Utama:** `/Users/dimaswastu/VERTEX-PREP`
**Conversation ID Sesi Awal:** `0dd7aa5f-d384-4b0d-8b95-c57759ac16dc`

---

## 1. Tujuan Utama Projek (`Core Goal`)
Membangun **Platform Belajar Kedokteran Visual & Persiapan UAB (`VERTEX-PREP 2.0`)** dengan prinsip utama:
1. **Belajar Tuntas Tanpa Perlu Buka File PPT (`Zero PPT Fatigue`)**: Memadatkan PPT kuliah dosen yang panjang (30–80 slide) menjadi **6–7 Bab Bento Visual Mengalir** (kotak alur bertahap, tabel pembeda konsep kembar, dan radar jebakan ujian).
2. **Bukti Fisik Slide Asli Dosen (`Slide-Verified`)**: Setiap bab dan setiap pembahasan soal wajib menyertakan **gambar tangkapan layar slide asli dosen** (di-*render* via `PyMuPDF` ke folder `slides_.../slide_N.jpg`) di dalam *Slide Dock* pendamping agar user tahu 100% materinya benar-benar berasal dari slide tersebut.
3. **Kejujuran Sumber Soal Mutlak (`Zero Fabrication`)**:
   - Arsip `/Users/dimaswastu/VERTEX-PREP/Bank_Soal_UAB/` berisi **51 file (2.633 soal)** dari **8 Blok Semester 1–2 (`BUAMS`, `BMS 1`, `BMS 2`, `BMS 3`, `BMS 4`, `BMD`, `BDT`, `HI`)**.
   - **Belum ada file soal UAB untuk Blok 9 (EMN)**. Jangan pernah mengklaim soal irisan/prediksi sebagai "Soal Asli UAB EMN". Beri label jujur: `Kasus Asli Slide Dosen`, `Soal Irisan Blok Terdahulu`, atau `Prediksi Berbasis Slide`.
4. **Standar UI/UX & Penulisan**:
   - Gunakan gaya desain **Supahero.io** (*Floating Pill Navbar*, *Split-Screen Hero dengan Live Slide Showcase*, *Bento Split-View Chapters*, tipografi `Newsreader` + `IBM Plex Sans` + `JetBrains Mono`).
   - Wajib lolos audit `/Users/dimaswastu/.agents/skills/impeccable/scripts/impeccable detect` dengan **`0 anti-patterns found`**.
   - Gunakan skill `no-ai-slop` (bahasa Indonesia medis yang tajam, padat, tanpa basa-basi AI).

---

## 2. File & Aset yang Sudah Selesai Dibangun di `/Users/dimaswastu/VERTEX-PREP/`
1. **Modul 1 (Blok 7 BDT · Kuliah 3: Patient Safety — dr. Riskiyah, MMRS [80 Slide])**:
   - File HTML Utama (Supahero Edition): `/Users/dimaswastu/VERTEX-PREP/BDT_KUL3_Patient_Safety.html` & `/Users/dimaswastu/VERTEX-PREP/index.html`
   - PDF Asli: `/Users/dimaswastu/VERTEX-PREP/KUL_3_BDT_Patient_Safety_KI.pdf`
   - 80 Gambar Slide (140 DPI): `/Users/dimaswastu/VERTEX-PREP/slides_bdt_kul3/slide_1.jpg` s.d. `slide_80.jpg`
   - Anki Deck (`.apkg`): `/Users/dimaswastu/VERTEX-PREP/anki/VERTEX_BDT_KUL3_Patient_Safety.apkg`
   - Isi: 7 Bab Visual + 9 Soal Asli UAB & Remidi BDT yang 100% keluar dari 14 slide inti.
2. **Modul 2 (Blok 9 EMN · Kuliah 2: Defisiensi Vitamin — dr. Iwal Reza Ahdi, Sp.PD [28 Slide])**:
   - File HTML Utama (Supahero Edition): `/Users/dimaswastu/VERTEX-PREP/VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html`
   - PDF Asli: `/Users/dimaswastu/VERTEX-PREP/KUL_2_Defisiensi_Vitamin_dr_Iwal.pdf`
   - 28 Gambar Slide (140 DPI): `/Users/dimaswastu/VERTEX-PREP/slides_kul2/slide_1.jpg` s.d. `slide_28.jpg`
   - Anki Deck (`.apkg`): `/Users/dimaswastu/VERTEX-PREP/anki/VERTEX_EMN_KUL2_Defisiensi_Vitamin.apkg`
3. **Indeks Pencarian Instan (`⌘K`) 51 File Bank Soal UAB + Slide**:
   - File Indeks JS: `/Users/dimaswastu/VERTEX-PREP/vendor/uab_search_data.js` (`3.424 item` terindeks dari 51 file PDF/DOCX di `Bank_Soal_UAB/` + 108 slide).
   - Script Generator Supahero: `/Users/dimaswastu/VERTEX-PREP/build_supahero_edition.py`

---

## 3. Peta ID Google Drive Angkatan (`VERTEXTERIAL`)
- **Folder Induk `VERTEXTERIAL`**: `1vrUGhIJuAjfV8R9zKDe8Wr-ojAtnLeJt`
- **Folder `BLOK`**: `1SImTvPqhkojagTOq5clNNb7ZF_5vtmPP`
  - `0 (E-BOOK)`: `1tZbMbQMbAJRmojT8IyTzjO2bzQfLy_2M`
  - `1 (BUAMS)`: `1mRMtfuraC0HueVl-4LTzXhSpinj1C6CD`
  - `2 (BMS 1)`: `1GFFIxSHGjGf1B3nq4kSJwQ4QMj_qbRm3`
  - `3 (BMS 2)`: `1tVA1x3gVnyEvYKtcedPJItGZLcJnstJR`
  - `4 (BMS 3)`: `1NeQ2ZvQbr6lJZEujXYIYa8ToQIBuNCp4`
  - `5 (BMS 4)`: `1b1ejwl4M0fMwes32fKVTa5x0z7Fdc_fW`
  - `6 (BMD)`: `1WdqpA4rXB-uFb0z9E4luC0elRniBDQqx`
  - `7 (BDT)`: `1823rKPuQVAl_vE-EQfo7rTq-Eh9KQves`
    - `00. MODUL BDT 2026`: `1rqtwJEEByoQZTxIMn547BtVws44wGPeP`
    - `KUL 2 CLINICAL PROCESS (IWL).pdf`: `1m46sdMnmoY7q1RI__kd5kYtTjJ6w1hqK`
    - `KUL 3 PATIENT SAFETY (KI)`: `150LONb6yrp0lv-hR1tj0ob2w6Ht2mVOB`
  - `8 (HI)`: `1UmiWDG9hqS8MhMFufhhOFp62eobYXUg2`
  - `9 (EMN)` *(Blok Aktif Semester 3)*: `1BDgeySHpYa3PMVSDHtXytPJqA6cMN0d3`
    - `00. MODUL EMN 2026.pdf`: `1GkliSzrTBNggyoIxRkPI4N4TDgwcgz6h`
    - `KUL 2 DEFISIENSI VITAMIN (IWL)`: `1-JrPD7PhKNVTGua72nDXVcVbDcrcSV0W`
    - `KUL 3 DEFISIENSI MINERAL (IWL)`: `1nDM2aZ2IdXxCQPBEwbF84RFVycf5-rkG`

---

## 4. Langkah Selanjutnya Saat Sesi Dilanjutkan
1. Cek apakah ada feedback tambahan pada tampilan `/Users/dimaswastu/VERTEX-PREP/BDT_KUL3_Patient_Safety.html` dan `/Users/dimaswastu/VERTEX-PREP/VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html`.
2. Lanjutkan pembuatan modul kuliah berikutnya (misal **Blok 9 EMN · KUL 3 Defisiensi Mineral** dari Drive ID `1nDM2aZ2IdXxCQPBEwbF84RFVycf5-rkG` atau kuliah lain di Blok BDT/EMN) menggunakan template `/Users/dimaswastu/VERTEX-PREP/build_supahero_edition.py`.
3. Jalankan server lokal di port `8765` (`python3 -m http.server 8765 --directory /Users/dimaswastu/VERTEX-PREP`) bila belum aktif.
