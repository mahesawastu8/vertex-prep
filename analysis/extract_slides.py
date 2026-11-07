#!/usr/bin/env python3
"""Ekstrak teks per slide dari semua PDF kuliah sebuah blok -> slides.json
[{lecture, lecturer, kul, slide, text, chars}]"""
import glob
import json
import logging
import os
import re
import sys

logging.disable(logging.CRITICAL)
from pypdf import PdfReader  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


def lecturer_of(name):
    m = re.search(r"\(([A-Z]{2,6})\)(?:\.pdf)?$", name.strip())
    return m.group(1) if m else ""


def main(block_dir, out):
    rows = []
    for f in sorted(glob.glob(os.path.join(block_dir, "*.pdf"))):
        name = os.path.basename(f)[:-4]
        try:
            pages = PdfReader(f).pages
        except Exception as e:  # noqa: BLE001
            print("GAGAL", name, e)
            continue
        for i, p in enumerate(pages, 1):
            try:
                t = re.sub(r"\s+", " ", p.extract_text() or "").strip()
            except Exception:  # noqa: BLE001
                t = ""
            rows.append({"lecture": name, "lecturer": lecturer_of(name), "slide": i, "n": len(pages), "text": t, "chars": len(t)})
        print(f"{len(pages):>4} slide  {name}", flush=True)
    json.dump(rows, open(out, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"total {len(rows)} slide -> {out}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
