#!/usr/bin/env python3
"""Deduplikasi soal per blok, cocokkan ke slide di blok masing-masing,
analisis profil dosen per blok dan lintas blok, lalu simpan laporan lengkap -> all_blocks_summary.json"""
import collections
import json
import os
import re
import sys
import numpy as np
import scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

HERE = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(HERE, "all_bank_questions.json")
SLIDES_FILE = os.path.join(HERE, "all_slides.json")
OUT_JSON = os.path.join(HERE, "all_blocks_summary.json")

STOPS = set("yang dan di ke dari pada untuk dengan adalah atau ini itu dalam akan juga tidak oleh sebagai apa apakah manakah berikut dibawah seorang pasien dokter yg sesuai benar salah tepat paling".split())

def clean(t):
    t = re.sub(r"[^a-z0-9 ]+", " ", t.lower())
    return " ".join(w for w in t.split() if w not in STOPS)

def classify_qtype_rule(stem, opts_text):
    s = stem.lower()
    if re.search(r"\b(seorang|wanita|laki-laki|anak|pria|perempuan|ny\.|tn\.|by\.|umur|th|tahun|datang|mengeluh|pemeriksaan didapatkan|keluhan)\b", s):
        if re.search(r"\b(etika|moral|sikap|hak|pasien menolak|keluarga|rahasia|komunikasi)\b", s):
            return "etika_sikap"
        if re.search(r"\b(hitung|dosis|berapa|cth|ml|mg|tetes|rumus)\b", s):
            return "hitungan"
        return "kasus_klinis"
    if re.search(r"\b(hitung|berapa|dosis|cth|mg/kg|kecepatan tetes|ml/jam)\b", s):
        return "hitungan"
    if re.search(r"\b(bukan|kecuali|tidak termasuk|tidak benar|salah)\b", s):
        return "negasi"
    if re.search(r"\b(perbedaan|membedakan|hubungan|mekanisme|mengapa|kenapa|sebab)\b", s):
        return "perbandingan_mekanisme"
    if re.search(r"\b(tahapan|urutan|langkah|prosedur|fiksasi|teknik|pembuatan)\b", s):
        return "prosedur_urutan"
    if re.search(r"\b(angka|nama|tokoh|tahun|tanggal|berapa persen|nilai normal)\b", s):
        return "fakta_angka_nama"
    return "definisi_istilah"

def deduplicate_questions(q_list):
    if not q_list: return []
    tx = [clean(q["stem"] + " " + " ".join(q["options"].values())) for q in q_list]
    # Filter teks kosong
    valid_indices = [i for i, t in enumerate(tx) if len(t.strip()) > 5]
    if not valid_indices: return []
    
    sub_q = [q_list[i] for i in valid_indices]
    sub_tx = [tx[i] for i in valid_indices]
    
    vec = normalize(TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True).fit_transform(sub_tx))
    sim = (vec @ vec.T).toarray()
    
    parent = list(range(len(sub_q)))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
        
    for i in range(len(sub_q)):
        for j in range(i + 1, len(sub_q)):
            if sim[i, j] >= 0.70:
                parent[find(j)] = find(i)
                
    clusters = collections.defaultdict(list)
    for i in range(len(sub_q)):
        clusters[find(i)].append(i)
        
    unique = []
    for root_idx, idxs in clusters.items():
        base = sub_q[root_idx].copy()
        base["occurrences"] = len(idxs)
        base["sources"] = list({sub_q[k]["source"] for k in idxs})
        base["qtype"] = classify_qtype_rule(base["stem"], " ".join(base["options"].values()))
        unique.append(base)
        
    return unique

def match_block(q_unique, block_slides):
    if not q_unique or not block_slides:
        return []
    
    # Exclude modul umum jika ada kuliah spesifik
    valid_slides = [s for s in block_slides if s["chars"] >= 15]
    if not valid_slides:
        valid_slides = block_slides
        
    s_texts = [clean(s["lecture"] + " " + s["text"]) for s in valid_slides]
    q_texts = [clean(q["stem"] + " " + " ".join(q["options"].values())) for q in q_unique]
    
    all_texts = s_texts + q_texts
    wv = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=1).fit(all_texts)
    cv = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True, min_df=2).fit(all_texts)
    
    def V(t):
        return normalize(sp.hstack([wv.transform(t), cv.transform(t)]).tocsr())
        
    sim = (V(q_texts) @ V(s_texts).T).toarray()
    
    matches = []
    for qi, q in enumerate(q_unique):
        best_idx = int(np.argmax(sim[qi]))
        score = float(sim[qi, best_idx])
        sl = valid_slides[best_idx]
        
        # Coverage rule
        if score >= 0.28:
            cov = "eksplisit"
        elif score >= 0.14:
            cov = "perlu_penalaran"
        else:
            cov = "tidak_ada"
            
        m = q.copy()
        m["matched_lecture"] = sl["lecture"]
        m["matched_lecturer"] = sl["lecturer"] or "TANPA_INISIAL"
        m["matched_slide"] = sl["slide"]
        m["slide_total"] = sl["n"]
        m["match_score"] = round(score, 4)
        m["coverage"] = cov
        matches.append(m)
        
    return matches

def main():
    print("Memuat data bank soal dan slide...", flush=True)
    all_q = json.load(open(QUESTIONS_FILE, encoding="utf-8"))
    all_s = json.load(open(SLIDES_FILE, encoding="utf-8"))
    
    # Normalisasi nama blok untuk UNKNOWN (UAB 22 -> BDT)
    for q in all_q:
        if q["block"] == "UNKNOWN":
            q["block"] = "7 (BDT)"
            
    blocks = sorted(list({q["block"] for q in all_q}))
    print(f"Daftar blok yang dianalisis: {blocks}\n", flush=True)
    
    block_results = {}
    total_raw_q = 0
    total_uniq_q = 0
    total_matched_explicit = 0
    total_matched_reasoning = 0
    total_matched_missing = 0
    
    lecturer_stats = collections.defaultdict(lambda: {
        "soal": 0, "eksplisit": 0, "penalaran": 0, "tidak_ada": 0,
        "kasus": 0, "hafalan": 0, "hitung": 0, "etika": 0, "mekanisme": 0,
        "blocks": set(), "lectures": set()
    })
    
    for b in blocks:
        bq = [q for q in all_q if q["block"] == b]
        bs = [s for s in all_s if s["block"] == b]
        
        raw_count = len(bq)
        uniq_q = deduplicate_questions(bq)
        uniq_count = len(uniq_q)
        repeats = sum(u["occurrences"] > 1 for u in uniq_q)
        
        matched = match_block(uniq_q, bs)
        
        cov_counts = collections.Counter(m["coverage"] for m in matched)
        qtype_counts = collections.Counter(m["qtype"] for m in matched)
        
        # Slide emas (slide keluar >= 2 kali)
        slide_freq = collections.Counter((m["matched_lecture"], m["matched_slide"]) for m in matched if m["coverage"] != "tidak_ada")
        hot_slides = [(lec, sl, cnt) for (lec, sl), cnt in slide_freq.most_common(5) if cnt >= 2]
        
        # Posisi slide
        pos_list = [(m["matched_slide"] - 1) / max(1, m["slide_total"] - 1) for m in matched if m["coverage"] != "tidak_ada"]
        b_early = sum(p < 1/3 for p in pos_list)
        b_mid = sum(1/3 <= p < 2/3 for p in pos_list)
        b_late = sum(p >= 2/3 for p in pos_list)
        total_pos = max(1, len(pos_list))
        
        # Update agregat
        total_raw_q += raw_count
        total_uniq_q += uniq_count
        total_matched_explicit += cov_counts["eksplisit"]
        total_matched_reasoning += cov_counts["perlu_penalaran"]
        total_matched_missing += cov_counts["tidak_ada"]
        
        # Update profil dosen
        for m in matched:
            d = m["matched_lecturer"]
            ls = lecturer_stats[d]
            ls["soal"] += 1
            if m["coverage"] == "eksplisit": ls["eksplisit"] += 1
            elif m["coverage"] == "perlu_penalaran": ls["penalaran"] += 1
            else: ls["tidak_ada"] += 1
            
            qt = m["qtype"]
            if qt == "kasus_klinis": ls["kasus"] += 1
            elif qt in ("definisi_istilah", "fakta_angka_nama"): ls["hafalan"] += 1
            elif qt == "hitungan": ls["hitung"] += 1
            elif qt == "etika_sikap": ls["etika"] += 1
            elif qt == "perbandingan_mekanisme": ls["mekanisme"] += 1
            
            ls["blocks"].add(b)
            ls["lectures"].add(m["matched_lecture"])
            
        covered_percent = round(100 * (cov_counts["eksplisit"] + cov_counts["perlu_penalaran"]) / max(1, uniq_count), 1)
        
        block_results[b] = {
            "raw_questions": raw_count,
            "unique_questions": uniq_count,
            "repeated_questions": repeats,
            "repeat_rate_percent": round(100 * repeats / max(1, uniq_count), 1),
            "coverage": {
                "eksplisit": cov_counts["eksplisit"],
                "perlu_penalaran": cov_counts["perlu_penalaran"],
                "tidak_ada": cov_counts["tidak_ada"],
                "total_tercakup_percent": covered_percent
            },
            "qtypes": dict(qtype_counts),
            "position": {
                "awal_percent": round(100 * b_early / total_pos, 1),
                "tengah_percent": round(100 * b_mid / total_pos, 1),
                "akhir_percent": round(100 * b_late / total_pos, 1)
            },
            "hot_slides": hot_slides
        }
        
        print(f"[{b}] {raw_count} soal mentah -> {uniq_count} soal unik (ulang {repeats}x / {round(100*repeats/max(1,uniq_count))}%)")
        print(f"  Ketercakupan slide: {covered_percent}% (eksplisit: {cov_counts['eksplisit']}, penalaran: {cov_counts['perlu_penalaran']}, luar: {cov_counts['tidak_ada']})")
        print(f"  Jenis soal teratas: {qtype_counts.most_common(3)}")
        print(f"  Posisi slide: awal {round(100*b_early/total_pos)}% | tengah {round(100*b_mid/total_pos)}% | akhir {round(100*b_late/total_pos)}%\n")

    # Format profil dosen untuk disimpan
    lecturer_report = {}
    for d, st in sorted(lecturer_stats.items(), key=lambda kv: -kv[1]["soal"]):
        n = st["soal"]
        if n == 0: continue
        lecturer_report[d] = {
            "total_soal": n,
            "eksplisit_percent": round(100 * st["eksplisit"] / n, 1),
            "penalaran_percent": round(100 * st["penalaran"] / n, 1),
            "luar_slide_percent": round(100 * st["tidak_ada"] / n, 1),
            "hafalan_percent": round(100 * st["hafalan"] / n, 1),
            "kasus_percent": round(100 * st["kasus"] / n, 1),
            "hitungan_percent": round(100 * st["hitung"] / n, 1),
            "etika_percent": round(100 * st["etika"] / n, 1),
            "mekanisme_percent": round(100 * st["mekanisme"] / n, 1),
            "blocks": sorted(list(st["blocks"])),
            "lecture_count": len(st["lectures"])
        }

    summary = {
        "overall": {
            "total_blocks": len(blocks),
            "total_raw_questions": total_raw_q,
            "total_unique_questions": total_uniq_q,
            "total_covered_percent": round(100 * (total_matched_explicit + total_matched_reasoning) / max(1, total_uniq_q), 1),
            "total_explicit_percent": round(100 * total_matched_explicit / max(1, total_uniq_q), 1),
            "total_reasoning_percent": round(100 * total_matched_reasoning / max(1, total_uniq_q), 1),
            "total_outside_percent": round(100 * total_matched_missing / max(1, total_uniq_q), 1)
        },
        "blocks": block_results,
        "lecturers": lecturer_report
    }

    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f"Laporan lengkap 8 blok berhasil disimpan ke: {OUT_JSON}")

if __name__ == "__main__":
    main()
