#!/usr/bin/env python3
"""Untuk tiap soal (dengan llm_lecture dari tahap 1) ambil 8 slide kandidat terbaik di dalam kuliah itu (TF-IDF)."""
import collections
import json
import re
import sys

import numpy as np
import scipy.sparse as sp
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

STOPS = set("yang dan di ke dari pada untuk dengan adalah atau ini itu dalam akan juga tidak oleh sebagai apa apakah manakah berikut dibawah seorang pasien dokter yg sesuai benar salah tepat paling".split())


def clean(t):
    t = re.sub(r"[^a-z0-9 ]+", " ", t.lower())
    return " ".join(w for w in t.split() if w not in STOPS)


def main(qfile, sfile, out, k=8):
    Q = json.load(open(qfile, encoding="utf-8"))
    S = [s for s in json.load(open(sfile, encoding="utf-8")) if not s["lecture"].startswith("00. MODUL")]
    by = collections.defaultdict(list)
    for s in S:
        if s["chars"] >= 25:
            by[s["lecture"]].append(s)
    res = {}
    for lec, sl in by.items():
        qi = [i for i, q in enumerate(Q) if q["llm_lecture"] == lec]
        if not qi:
            continue
        texts = [clean(s["text"]) for s in sl]
        qt = [clean(Q[i]["stem"] + " " + " ".join(Q[i]["options"].values())) for i in qi]
        allt = texts + qt
        wv = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit(allt)
        cv = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), sublinear_tf=True).fit(allt)

        def V(t):
            return normalize(sp.hstack([wv.transform(t), cv.transform(t)]).tocsr())

        sim = (V(qt) @ V(texts).T).toarray()
        for r, i in enumerate(qi):
            order = np.argsort(-sim[r])[:k]
            res[str(i)] = [{"lecture": lec, "slide": sl[j]["slide"], "text": sl[j]["text"][:380], "score": round(float(sim[r][j]), 4)} for j in order]
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print(len(res), "soal punya kandidat")


if __name__ == "__main__":
    main(*sys.argv[1:4])
