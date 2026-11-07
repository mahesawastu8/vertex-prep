#!/usr/bin/env python3
"""Cocokkan tiap soal ke slide/kuliah asal dengan TF-IDF (kata + n-gram karakter) -> matches.json"""
import json
import re
import sys

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize
import scipy.sparse as sp

STOP = set("yang dan di ke dari pada untuk dengan adalah atau ini itu dalam akan juga tidak oleh sebagai apa apakah manakah berikut dibawah seorang pasien dokter yg sesuai benar salah tepat paling".split())


def clean(t):
    t = t.lower()
    t = re.sub(r"[^a-z0-9\u00c0-\u024f ]+", " ", t)
    return " ".join(w for w in t.split() if w not in STOP)


def main(qfile, sfile, out, exclude="00. MODUL"):
    Q = json.load(open(qfile, encoding="utf-8"))
    S = [s for s in json.load(open(sfile, encoding="utf-8")) if not s["lecture"].startswith(exclude) and s["chars"] >= 25]
    qtext = [clean(q["stem"] + " " + " ".join(q["options"].values())) for q in Q]
    stext = [clean(s["text"]) for s in S]
    allt = qtext + stext
    wv = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=1).fit(allt)
    cv = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True, min_df=2).fit(allt)

    def vec(t):
        return normalize(sp.hstack([wv.transform(t), cv.transform(t)]).tocsr())

    sim = (vec(qtext) @ vec(stext).T).toarray()
    # skor tingkat kuliah: slide terbaik per kuliah
    lects = sorted({s["lecture"] for s in S})
    lidx = {l: [i for i, s in enumerate(S) if s["lecture"] == l] for l in lects}
    res = []
    for qi, q in enumerate(Q):
        row = sim[qi]
        order = np.argsort(-row)[:3]
        lscore = {l: float(row[ix].max()) for l, ix in lidx.items()}
        ranked = sorted(lscore.items(), key=lambda kv: -kv[1])
        top, second = ranked[0], ranked[1]
        best = S[order[0]]
        res.append({
            **{k: q[k] for k in ("source", "no", "stem", "options")},
            "lecture": top[0], "lecturer": best["lecturer"], "slide": best["slide"], "n": best["n"],
            "score": round(top[1], 4), "margin": round(top[1] - second[1], 4), "second": second[0],
            "top3": [{"lecture": S[i]["lecture"], "slide": S[i]["slide"], "score": round(float(row[i]), 4)} for i in order],
        })
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    sc = np.array([r["score"] for r in res])
    print("soal:", len(res), "| slide terindeks:", len(S))
    print("persentil skor 10/25/50/75/90:", np.round(np.percentile(sc, [10, 25, 50, 75, 90]), 3))


if __name__ == "__main__":
    main(*sys.argv[1:4])
