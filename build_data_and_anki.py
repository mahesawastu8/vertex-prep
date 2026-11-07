import os
import re
import json
import glob
import pymupdf
import docx
import genanki

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
UAB_DIR = os.path.join(BASE_DIR, "Bank_Soal_UAB")
VENDOR_DIR = os.path.join(BASE_DIR, "vendor")
ANKI_DIR = os.path.join(BASE_DIR, "anki")
os.makedirs(VENDOR_DIR, exist_ok=True)
os.makedirs(ANKI_DIR, exist_ok=True)

def infer_block(filename):
    u = filename.upper()
    if "BUAMS" in u: return "BUAMS"
    if "BMS 1" in u or "BMS1" in u or "BMS-1" in u: return "BMS 1"
    if "BMS 2" in u or "BMS2" in u or "BMS-2" in u: return "BMS 2"
    if "BMS 3" in u or "BMS3" in u or "BMS-3" in u: return "BMS 3"
    if "BMS 4" in u or "BMS4" in u or "BMS-4" in u: return "BMS 4"
    if "BMD" in u: return "BMD"
    if "BDT" in u: return "BDT"
    if "HI" in u: return "HI"
    return "LINTAS BLOK"

search_items = []

# 1. Index all 80 slides of BDT KUL 3
doc_bdt = pymupdf.open(os.path.join(BASE_DIR, "KUL_3_BDT_Patient_Safety_KI.pdf"))
for idx, page in enumerate(doc_bdt):
    txt = " ".join(page.get_text().split())
    if not txt:
        txt = f"Slide Visual / Bagan Gambar Patient Safety (Halaman {idx+1})"
    search_items.append({
        "id": f"slide-bdt-{idx+1}",
        "type": "SLIDE DOSEN",
        "block": "BDT (Blok 7)",
        "source": f"KUL 3 Patient Safety (dr. Riskiyah) · Slide {idx+1}",
        "text": txt[:420],
        "img": f"slides_bdt_kul3/slide_{idx+1}.jpg",
        "url": f"BDT_KUL3_Patient_Safety.html#slide-{idx+1}"
    })

# 2. Index all 28 slides of EMN KUL 2
doc_emn = pymupdf.open(os.path.join(BASE_DIR, "KUL_2_Defisiensi_Vitamin_dr_Iwal.pdf"))
for idx, page in enumerate(doc_emn):
    txt = " ".join(page.get_text().split())
    search_items.append({
        "id": f"slide-emn-{idx+1}",
        "type": "SLIDE DOSEN",
        "block": "EMN (Blok 9)",
        "source": f"KUL 2 Defisiensi Vitamin (dr. Iwal) · Slide {idx+1}",
        "text": txt[:420],
        "img": f"slides_kul2/slide_{idx+1}.jpg",
        "url": f"VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html#slide-{idx+1}"
    })

# 3. Parse all 51 files in Bank_Soal_UAB into searchable chunks
uab_files = sorted(os.listdir(UAB_DIR))
q_counter = 0
for fname in uab_files:
    fpath = os.path.join(UAB_DIR, fname)
    if not os.path.isfile(fpath):
        continue
    blk = infer_block(fname)
    full_text = ""
    try:
        if fname.lower().endswith(".pdf"):
            d = pymupdf.open(fpath)
            pages_txt = []
            for p in d:
                pages_txt.append(p.get_text())
            full_text = "\n".join(pages_txt)
        elif fname.lower().endswith(".docx"):
            d = docx.Document(fpath)
            paras = [p.text for p in d.paragraphs if p.text.strip()]
            for t in d.tables:
                for row in t.rows:
                    paras.append(" | ".join(c.text.strip() for c in row.cells if c.text.strip()))
            full_text = "\n".join(paras)
    except Exception as e:
        continue

    clean_text = " ".join(full_text.split())
    if not clean_text:
        continue

    # Split by numbered question pattern or 450-char sliding windows
    parts = re.split(r'(?=(?:^|\s)(?:\d{1,3}[\.\)]\s+[A-Z]))', clean_text)
    if len(parts) < 5:
        # fallback chunking
        step = 380
        parts = [clean_text[i:i+450] for i in range(0, len(clean_text), step)]

    for idx, part in enumerate(parts):
        p_clean = part.strip()
        if len(p_clean) < 35:
            continue
        q_counter += 1
        search_items.append({
            "id": f"uab-{q_counter}",
            "type": "BANK SOAL UAB",
            "block": blk,
            "source": f"{fname} (Bagian #{idx+1})",
            "text": p_clean[:420],
            "img": "",
            "url": ""
        })

print(f"Total indexed items: {len(search_items)} (Slides: 108, UAB Chunks: {q_counter})")

with open(os.path.join(VENDOR_DIR, "uab_search_data.js"), "w", encoding="utf-8") as f:
    f.write("window.VERTEX_SEARCH_INDEX = ")
    json.dump(search_items, f, ensure_ascii=False)
    f.write(";\n")

# 4. Build Anki .apkg decks using kerrickstaley/genanki
model = genanki.Model(
    1607392319,
    'VERTEX-PREP Clinical Slide-Verified Model',
    fields=[
        {'name': 'Title'},
        {'name': 'Question'},
        {'name': 'Answer'},
        {'name': 'SlideProof'},
        {'name': 'EpistemicLayers'},
    ],
    templates=[
        {
            'name': 'VERTEX Card',
            'qfmt': '''
                <div style="font-family: sans-serif; padding: 16px; background: #F3F6F8; color: #0F1C24; border-radius: 10px;">
                    <div style="font-size: 12px; font-weight: 700; color: #0F5C4D; text-transform: uppercase; letter-spacing: 0.06em;">{{Title}}</div>
                    <h2 style="font-size: 18px; margin-top: 8px; line-height: 1.45;">{{Question}}</h2>
                </div>
            ''',
            'afmt': '''
                {{FrontSide}}
                <hr id="answer" style="border: none; border-top: 1px solid #CFD9E0; margin: 14px 0;">
                <div style="font-family: sans-serif; padding: 16px; background: #FFFFFF; color: #0F1C24; border-radius: 10px;">
                    <div style="font-size: 16px; font-weight: 700; color: #0F5C4D; margin-bottom: 10px;">{{Answer}}</div>
                    <div style="font-size: 14px; line-height: 1.5; margin-bottom: 12px;">{{EpistemicLayers}}</div>
                    <div style="margin-top: 10px;">{{SlideProof}}</div>
                </div>
            ''',
        },
    ])

# Deck 1: BDT KUL 3 Patient Safety
deck_bdt = genanki.Deck(2059400110, 'VERTEX-PREP :: Blok 7 (BDT) :: KUL 3 Patient Safety (dr. Riskiyah)')
bdt_cards = [
    ("BDT KUL 3 · Slide 18 (UAB Axonation No. 29 & UAB 22 No. 70)",
     "Seorang pasien disuntik Antalgin untuk nyeri kolik, mengalami syok anafilaktik dan meninggal dunia. Termasuk insiden keselamatan pasien apakah kejadian ini?",
     "Kejadian Sentinel (Suatu KTD yang mengakibatkan kematian atau cedera serius).",
     "slide_18.jpg",
     "<b>[FAKTA SLIDE 18]</b>: Kejadian Sentinel adalah suatu KTD yang mengakibatkan kematian atau cedera yang serius.<br><b>[JEBAKAN UJIAN]</b>: Jangan pilih KTD biasa bila di soal disebutkan pasien meninggal dunia atau cacat permanen."),
    ("BDT KUL 3 · Slide 18 (Soal UAB BDT-1 Hal. 9)",
     "Dokter meresepkan obat dengan dosis salah dan farmasi sudah menyiapkan, tetapi kesalahan diketahui sebelum obat diberikan kepada pasien. Disebut insiden apakah ini?",
     "KNC (Kejadian Nyaris Cedera / Near Miss) — insiden belum sampai terpapar ke pasien.",
     "slide_18.jpg",
     "<b>[FAKTA SLIDE 18]</b>: KNC adalah terjadinya insiden yang belum sampai terpapar ke pasien. Jika sudah diberikan tapi pasien tidak cedera = KTC."),
    ("BDT KUL 3 · Slide 23–24 vs Slide 61 (Rekap UAB BDT No. 32 & 44)",
     "Sebutkan 2 poin dari '7 Standar Keselamatan Pasien' (Slide 23-24) yang paling sering diujikan di UAB BDT untuk mengecoh '7 Langkah Menuju Keselamatan Pasien' (Slide 61)!",
     "1) Hak Pasien (Standar 1) dan 2) Peran Kepemimpinan dalam meningkatkan keselamatan pasien (Standar 5).",
     "slide_24.jpg",
     "<b>[JEBAKAN UJIAN]</b>: Opsi 'Memimpin dan mendukung staf' serta 'Mengembangkan sistem pelaporan' adalah 7 Langkah (Slide 61), bukan 7 Standar!"),
    ("BDT KUL 3 · Slide 32, 34, 35 (Soal UAB BDT-1 Hal. 5)",
     "Pasien laki-laki 58 tahun dirawat dengan pneumonia tetapi belum dipasangkan gelang identitas biru sehingga obat tertukar. Sasaran Keselamatan Pasien (SKP) ke berapa yang dilanggar?",
     "SKP 1: Ketepatan Identifikasi Pasien (Minimal 2 dari 4 identitas: Nama, Tgl Lahir, No RM, NIK; dilarang pakai nomor kamar/tempat tidur).",
     "slide_35.jpg",
     "<b>[FAKTA SLIDE 35]</b>: Gelang Biru = Laki-laki, Pink = Perempuan, Merah = Alergi, Kuning = Risiko Jatuh."),
    ("BDT KUL 3 · Slide 46, 47, 48 (Soal Remidi BDT No. 39)",
     "Cairan Concentrated Potassium Chloride (KCl pekat) disimpan di instalasi farmasi dan wajib diberi label khusus. Apa nama label resminya menurut Slide 48?",
     "HIGH ALERT! MEDICATION (Obat yang Perlu Diwaspadai).",
     "slide_48.jpg",
     "<b>[JEBAKAN SLIDE 48]</b>: Kata 'Distinct Packaging' dan 'Prominent Warning' di kotak kiri Slide 48 adalah sifat kemasannya, sedangkan teks pada botolnya adalah HIGH ALERT!"),
    ("BDT KUL 3 · Slide 51, 52, 54 (Rekap UAB BDT No. 43)",
     "Pasien dijadwalkan operasi thoraks tetapi kaki pasien ikut dioperasi. Berdasarkan Slide 54 (Causes of Surgical Errors), apa penyebab urutan pertama kesalahan tersebut?",
     "Komunikasi yang tidak efektif antara anggota tim bedah (serta kurang melibatkan pasien dalam surgical marking & tidak melakukan Time-Out).",
     "slide_54.jpg",
     "<b>[FAKTA SLIDE 54]</b>: 1. Komunikasi tidak efektif antar tim bedah, 2. Kurangnya kerja sama tim, 3. Kurang melibatkan pasien dalam penandaan lokasi."),
    ("BDT KUL 3 · Slide 69, 71, 73, 75 (UAB 22 No. 85)",
     "Pasien jatuh dari brankar saat ditransfer dari UGD ke kamar operasi. Berapa batas waktu pelaporan internal, dan metode analisis apa yang dipakai tim KPRS bila grading risiko Kuning/Merah?",
     "Pelaporan internal maksimal 2 x 24 jam; analisis menggunakan Root Cause Analysis (RCA) maksimal 45 hari.",
     "slide_69.jpg",
     "<b>[FAKTA SLIDE 69 & 73]</b>: Grading Biru/Hijau = Investigasi Sederhana (1-2 minggu). Grading Kuning/Merah = RCA (Root Cause Analysis)."),
]

bdt_media = []
for title, q, a, img_name, ep in bdt_cards:
    img_path = os.path.join(BASE_DIR, "slides_bdt_kul3", img_name)
    if os.path.exists(img_path):
        bdt_media.append(img_path)
    note = genanki.Note(
        model=model,
        fields=[title, q, a, f'<img src="{img_name}" style="max-width:100%; border-radius:8px;">', ep]
    )
    deck_bdt.add_note(note)

pkg_bdt = genanki.Package(deck_bdt)
pkg_bdt.media_files = list(set(bdt_media))
pkg_bdt.write_to_file(os.path.join(ANKI_DIR, "VERTEX_BDT_KUL3_Patient_Safety.apkg"))

# Deck 2: EMN KUL 2 Defisiensi Vitamin
deck_emn = genanki.Deck(2059400111, 'VERTEX-PREP :: Blok 9 (EMN) :: KUL 2 Defisiensi Vitamin (dr. Iwal, Sp.PD)')
emn_cards = [
    ("EMN KUL 2 · Slide 3, 16, 17, 24",
     "Laki-laki 62 tahun, DM tipe 2 konsumsi Metformin jangka panjang, kesemutan kedua kaki, glossitis, Hb 9,8 g/dL, MCV 112 fL. Defisiensi vitamin apa dan pemeriksaan metabolit apa yang meningkat spesifik?",
     "Defisiensi Vitamin B12 (Kobalamin) — terjadi peningkatan asam metilmalonat (MMA) dan homosistein.",
     "slide_17.jpg",
     "<b>[FAKTA SLIDE 17]</b>: B9 (Folat) dan B12 sama-sama menyebabkan anemia megaloblastik (MCV > 100 fL) dan homosistein naik, tetapi MMA hanya naik pada defisiensi B12!"),
    ("EMN KUL 2 · Slide 8 & 19",
     "Sebutkan urutan progresivitas klinis defisiensi Vitamin A pada mata dan peran asam retinoat pada jaringan!",
     "Nyctalopia (rabun senja, paling dini) → Xerosis konjungtiva → Bercak Bitot → Keratomalasia (ulserasi/pencairan kornea → buta). Retinoat mengatur diferensiasi epitel.",
     "slide_8.jpg",
     "<b>[FAKTA SLIDE 8]</b>: Retinal berperan pada rodopsin (siklus visual), sedangkan Retinoat berperan pada diferensiasi epitel mukosa."),
    ("EMN KUL 2 · Slide 9",
     "Urutkan jalur aktivasi metabolik Vitamin D dari kulit hingga ginjal, dan apa metabolit terbaik untuk menilai status Vitamin D di darah?",
     "Kulit (Kolekalsiferol/D3) → Hati (25-OH-D / Kalsidiol) → Ginjal oleh 1α-hidroksilase (1,25-(OH)2-D / Kalsitriol aktif). Parameter lab status Vitamin D adalah 25(OH)D.",
     "slide_9.jpg",
     "<b>[JEBAKAN SLIDE 9]</b>: Bentuk biologis paling aktif adalah 1,25-(OH)2-D, tetapi yang diukur di lab untuk status defisiensi adalah 25(OH)D!"),
    ("EMN KUL 2 · Slide 11 & 25",
     "Pasien alkoholik kronik / hiperemesis gravidarum diberi infus glukosa tanpa tiamin, lalu muncul kebingungan akut, ataksia, dan oftalmoplegia/nistagmus. Apa diagnosis dan kofaktor enzim yang terganggu?",
     "Ensefalopati Wernicke akibat defisiensi Vitamin B1 (Tiamin Pirofosfat / TPP). Enzim: Piruvat dehidrogenase, α-ketoglutarat dehidrogenase, Transketolase.",
     "slide_11.jpg",
     "<b>[JEBAKAN KLINIS]</b>: Wajib berikan Tiamin (B1) SEBELUM atau bersama infus glukosa agar tidak memicu krisis asam laktat & Wernicke!"),
    ("EMN KUL 2 · Slide 14, 15, 26",
     "Pria 41 tahun dengan diet sangat terbatas mengalami perdarahan gusi, petechiae perifolikular, luka lama sembuh, tetapi hasil PT dan INR normal. Defisiensi vitamin apa?",
     "Defisiensi Vitamin C (Skorbut / Scurvy) — gangguan hidroksilasi prolin & lisin pada sintesis kolagen dinding pembuluh darah.",
     "slide_26.jpg",
     "<b>[PEMBEDA SLIDE 26]</b>: Skorbut (Vit C) memiliki PT/INR NORMAL karena defeknya di kolagen kapiler. Defisiensi Vit K memiliki PT/INR MEMANJANG (Faktor II, VII, IX, X)."),
]

emn_media = []
for title, q, a, img_name, ep in emn_cards:
    img_path = os.path.join(BASE_DIR, "slides_kul2", img_name)
    if os.path.exists(img_path):
        emn_media.append(img_path)
    note = genanki.Note(
        model=model,
        fields=[title, q, a, f'<img src="{img_name}" style="max-width:100%; border-radius:8px;">', ep]
    )
    deck_emn.add_note(note)

pkg_emn = genanki.Package(deck_emn)
pkg_emn.media_files = list(set(emn_media))
pkg_emn.write_to_file(os.path.join(ANKI_DIR, "VERTEX_EMN_KUL2_Defisiensi_Vitamin.apkg"))
print("Anki decks successfully written to /Users/dimaswastu/VERTEX-PREP/anki/")
