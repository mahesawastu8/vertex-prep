# 03 — AUDIT & ROADMAP VERTEX-PREP

**Tanggal:** 7 November 2026
**Lingkup:** isi `~/VERTEX-PREP` (5 modul, 42–80 slide per kuliah, bank soal 2.235 soal)
**Sifat:** audit teknis + rencana kerja. Bukan penilaian konten medis.

---

## 1. Angka dasar (terukur, bukan kesan)

| Hal | Kenyataan |
|---|---|
| Modul selesai | 5 (BDT KUL3, EMN KUL2, EMN KUL3, EMN KUL5, HI KUL20) |
| Kuliah terdeteksi di Drive | 38 berkas kuliah; 25 di antaranya blok HI |
| Skrip build | **18 berkas, 1.175 KB**, untuk 5 kuliah |
| Berkas HTML | 9 — tetapi hanya 5 modul; sisanya duplikat (`index.html` = salinan BDT, PoC vs EMN2) |
| Ukuran repo | **1,1 GB** (847 MB di `analysis/`) |
| Version control | **tidak ada** (`git` belum di-init) |
| Deck Anki | 7, 7, 8, **43**, 7 kartu — tidak seragam |
| Indeks ⌘K | "Defisiensi Mineral" dan "Autoimunitas" **tidak ada** di indeks |
| Navigasi antar modul | tidak konsisten: dropdown BDT 3 opsi, EMN2 6 opsi, EMN3/HI 5 opsi, tidak saling mengenal KUL5 |
| Soal UAB per blok | BMD 490, BMS1 437, BUAMS 344, BDT 261, **HI 231**, BMS4 207, **EMN 0** |

Kesimpulan satu baris: **kontennya kuat, fondasinya belum.** Yang menghambat bukan kualitas materi, melainkan arsitektur yang menyalin-tempel per kuliah.

---

## 2. Lima masalah struktural

### 2.1 Arsitektur salin-tempel (masalah utama)
Setiap modul adalah skrip Python 70–95 KB yang memuat: CSS ~30 KB, topbar, 6 bab, kuis, tryout, dan JS. 18 skrip = 1.175 KB kode yang 80%-nya sama. Akibat nyata:
- Perbaikan bug harus diulang 5 kali (contoh: lebar ponsel — modul lama masih melebar di 390 px).
- Dropdown modul berbeda-beda isinya; modul baru tidak otomatis muncul di modul lama.
- Menambah 1 kuliah = menulis ulang ~1.500 baris, bukan mengisi konten.

### 2.2 Tidak ada pintu masuk
`index.html` bukan hub — ia salinan modul BDT. Lima modul hidup sendiri-sendiri; tidak ada halaman "semua kuliah", tidak ada progres, tidak ada penanda mana yang sudah/belum.

### 2.3 Indeks pencarian tidak mencakup modul
`vendor/uab_search_data.js` (1,6 MB) mengindeks bank soal + slide, tetapi **bukan isi modul**. ⌘K tidak bisa menemukan "Toleransi Perifer" atau "skor McLaren" — padahal itu yang paling sering dicari saat belajar.

### 2.4 Kualitas tidak seragam
- Anki: 7–8 kartu untuk modul 6 bab (terlalu tipis untuk spaced repetition), sementara KUL5 punya 43.
- Staging slide: modul lama 16–21 slide statis, modul baru 6 slide + pill dinamis — pola berbeda.
- Label kejujuran: sudah baik (KUL5 eksplisit "bukan arsip UAB"), tapi belum ada pemeriksa otomatis yang mencegah klaim "soal asli UAB" muncul tanpa bukti.

### 2.5 Tidak ada jaring pengaman
Tidak ada git, tidak ada uji otomatis, tidak ada pemeriksa tautan/gambar. Satu `rm` atau satu skrip yang salah tulis bisa menghapus pekerjaan berhari-hari.

---

## 3. Prioritas (dampak ÷ usaha)

### P1 — Satu mesin, banyak kuliah `[dampak: sangat tinggi]`
Pisahkan **template** dari **konten**:
```
engine/
  template.html        (CSS + shell + komponen: diperbaiki sekali untuk semua)
  render.py            (spec → HTML + Anki + entri summaries.json)
lectures/
  emn-kul5.json        (6 bab: judul, teks, kuis, slide, trap)
```
Target: kuliah baru = 1 berkas spec ±300–500 baris. Migrasi 5 modul lama ke spec **tanpa mengubah tampilan**.

### P2 — Hub + peta cakupan `[tinggi]`
Halaman `index.html` yang dihasilkan dari `summaries.json` + `drive_tree.json`:
- daftar semua kuliah per blok, status: `modul · slide · anki · belum`
- pencarian ⌘K yang mengindeks **isi modul** (bab, istilah, soal, slide)
- progres per bab (localStorage), penanda "terakhir dibaca"

### P3 — Prioritas berbasis soal `[tinggi]`
Jangan bangun berurutan. 231 soal HI, topik terbanyak **Hipersensitivitas (19 soal)** → HI KUL 21 sebelum yang lain. BDT: Patient Safety hanya 4 soal → bukan prioritas berikutnya. EMN: 0 soal UAB → wajib label "latihan berbasis slide" (sudah dilakukan di KUL5).

### P4 — Seragamkan kualitas `[sedang]`
- Anki minimum **25 kartu/modul**, tiap kartu menyebut nomor slide.
- Tiap bab minimal 1 kuis inline + 1 "jebakan ujian".
- Slide staging wajib (bukan opsional) dengan minimal 3 slide per bab.

### P5 — `verify.py` `[sedang, murah]`
Satu skrip yang menggagalkan build bila:
1. ada referensi `slides_*/slide_N.jpg` yang tidak ada,
2. ada placeholder (`TODO`, `Lorem`, `__`),
3. ada modul dengan < 25 kartu Anki atau < 5 bab,
4. render 390 px menghasilkan `scrollWidth > 390`,
5. ada label "UAB" pada soal yang tidak ditemukan di `all_bank_questions.json`.

### P6 — Kebersihan `[murah, mendesak]`
`git init` + `.gitignore` (`node_modules/`, `__pycache__/`, `analysis/`, `*.log`), arsipkan 13 varian build yang mati ke `_arsip/`, hapus duplikat `index.html`/PoC.

### P7 — Fitur belajar yang belum ada `[sedang]`
Mode ujian timer, "ulangi yang salah", ekspor Anki hanya bab yang lemah, dan riwayat skor tryout.

---

## 4. Rencana 14 hari

| Hari | Kerja |
|---|---|
| 1 | `git init`, `.gitignore`, arsip varian mati, hub sederhana dari `summaries.json` |
| 2–4 | `engine/template.html` + `render.py`; migrasi 5 modul ke spec (tampilan tetap) |
| 5 | `verify.py` + jalankan; perbaiki temuan (ponsel, deck tipis, label) |
| 6–7 | Indeks ⌘K memuat isi modul; progres per bab |
| 8–11 | HI KUL 21 Hipersensitivitas (231 soal → topik teratas) |
| 12–14 | HI KUL 11 Transfusi / HI KUL 10 Keganasan, sesuai hitungan soal |

## 5. Ukuran keberhasilan

- Kuliah baru selesai dalam **< 1 hari**, bukan 3–4 hari.
- Nol referensi gambar hilang; nol halaman melebar di 390 px.
- Setiap modul ≥ 25 kartu Anki dan ≥ 5 bab.
- ⌘K mengembalikan hasil dari isi modul dalam < 200 ms.
- `git log` menunjukkan satu commit per modul selesai.

---

## 6. Yang sebaiknya dihindari

1. Menambah modul baru sebelum P1 selesai — biaya per kuliah akan tetap 1.500 baris.
2. Membuat varian desain baru (sudah 18 skrip untuk 5 kuliah; desain ke-19 tidak menambah nilai).
3. Menandai soal sebagai "asli UAB" tanpa entri di `all_bank_questions.json`.
4. Menyimpan 847 MB data analisis di dalam repo tanpa `gitignore`/LFS.
