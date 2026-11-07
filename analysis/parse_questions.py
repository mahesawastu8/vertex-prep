#!/usr/bin/env python3
"""Parse soal pilihan ganda dari PDF bank soal (hasil ingatan mahasiswa; format berantakan).

Strategi: normalisasi spasi -> cari penanda nomor yang BERURUTAN (1,2,3,...) agar tidak tertipu angka lain
-> pecah opsi A..E secara berurutan. Soal yang tidak punya >=2 opsi dibuang (bukan soal terstruktur).
"""
import json
import logging
import os
import re
import sys

logging.disable(logging.CRITICAL)
from pypdf import PdfReader  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
BANK = os.path.join(HERE, "..", "Bank_Soal_UAB")


def read_text(path):
    r = PdfReader(path)
    return " ".join((p.extract_text() or "") for p in r.pages)


def norm(t):
    t = t.replace("\u00a0", " ")
    t = re.sub(r"[ \t\r\n]+", " ", t)
    return t.strip()


def split_numbered(t, loose=False):
    """Potong teks menjadi blok soal berdasarkan penanda nomor berurutan.

    loose=True: nomor tanpa titik/kurung ("12 Seorang laki-laki ..."), hanya bila diikuti huruf kapital.
    """
    pos = []
    cur = 0
    k = 1
    while True:
        sep = r"\s+(?=[A-Z])" if loose else r"\s?[\.\)]\s+(?=\S)"
        m = re.compile(rf"(?:(?<=\s)|^){k}{sep}").search(t, cur)
        if not m:
            break
        pos.append((k, m.start(), m.end()))
        cur = m.end()
        k += 1
    blocks = []
    for i, (k, s, e) in enumerate(pos):
        end = pos[i + 1][1] if i + 1 < len(pos) else len(t)
        blocks.append((k, t[e:end].strip()))
    if not loose and len(blocks) < 5:
        alt = split_numbered(t, loose=True)
        if len(alt) > len(blocks):
            return alt
    return blocks


OPT_RE = {c: re.compile(rf"(?:(?<=\s)|^)[{c}{c.lower()}]\s?[\.\)]\s+") for c in "ABCDE"}


def split_options(block):
    """Pisahkan stem dan opsi A-E berurutan. Kembalikan (stem, {huruf: teks}) atau None."""
    cur = 0
    marks = []
    for c in "ABCDE":
        m = OPT_RE[c].search(block, cur)
        if not m:
            break
        marks.append((c, m.start(), m.end()))
        cur = m.end()
    if len(marks) < 2:
        return None
    stem = block[: marks[0][1]].strip()
    opts = {}
    for i, (c, s, e) in enumerate(marks):
        end = marks[i + 1][1] if i + 1 < len(marks) else len(block)
        opts[c] = block[e:end].strip()
    return stem, opts


def parse_file(path, source):
    raw = read_text(path)
    blocks = split_numbered(norm(raw))
    if len(blocks) < 5:  # file tak bernomor: pisah per paragraf (baris kosong)
        blocks = [(i + 1, norm(p)) for i, p in enumerate(re.split(r"\n[ \t]*\n", raw)) if p.strip()]
    out = []
    for k, blk in blocks:
        r = split_options(blk)
        if not r or len(r[0]) < 12:
            continue
        stem, opts = r
        stem = re.sub(r"^\d{1,3}\s?[\.\)]\s+", "", stem)  # buang nomor yang tertinggal
        out.append({"source": source, "no": k, "stem": stem, "options": opts})
    return out


if __name__ == "__main__":
    # argumen: output.json lalu nama-file...
    outp, files = sys.argv[1], sys.argv[2:]
    allq = []
    for f in files:
        qs = parse_file(os.path.join(BANK, f), f)
        print(f"{len(qs):>4} soal  {f}", flush=True)
        allq.extend(qs)
    json.dump(allq, open(outp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"total {len(allq)} soal -> {outp}")
