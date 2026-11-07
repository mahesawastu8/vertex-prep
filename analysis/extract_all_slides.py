#!/usr/bin/env python3
"""Ekstrak teks per slide dari SELURUH kuliah di semua blok (BUAMS, BMS 1-4, BMD, BDT, HI, EMN) -> all_slides.json"""
import glob
import json
import logging
import os
import re
import sys

logging.disable(logging.CRITICAL)
from pypdf import PdfReader
try:
    from pptx import Presentation
except ImportError:
    Presentation = None

HERE = os.path.dirname(os.path.abspath(__file__))
LECTURES_DIR = os.path.join(HERE, "lectures")
OUT = os.path.join(HERE, "all_slides.json")
def clean_surrogates(s):
    if not s: return ""
    return s.encode("utf-16", "surrogatepass").decode("utf-16", "ignore")

def lecturer_of(name):
    m = re.search(r"\(([A-Z]{2,6})\)(?:\.pdf|\.pptx)?$", name.strip(), re.I)
    return m.group(1).upper() if m else ""

def extract_pdf(path, block_name):
    name = os.path.basename(path)
    if name.lower().endswith(".pdf"): name = name[:-4]
    lecturer = lecturer_of(name)
    slides = []
    try:
        pages = PdfReader(path).pages
        for i, p in enumerate(pages, 1):
            try:
                t = re.sub(r"\s+", " ", p.extract_text() or "").strip()
                t = clean_surrogates(t)
            except Exception:
                t = ""
            slides.append({
                "block": block_name,
                "lecture": name,
                "lecturer": lecturer,
                "slide": i,
                "n": len(pages),
                "text": t,
                "chars": len(t)
            })
    except Exception as e:
        print(f"  [PDF Err] {name}: {e}", flush=True)
    return slides

def extract_pptx(path, block_name):
    if not Presentation: return []
    name = os.path.basename(path)
    if name.lower().endswith(".pptx"): name = name[:-5]
    lecturer = lecturer_of(name)
    slides = []
    try:
        prs = Presentation(path)
        total = len(prs.slides)
        for i, s in enumerate(prs.slides, 1):
            txts = []
            for shape in s.shapes:
                if shape.has_text_frame:
                    for para in shape.text_frame.paragraphs:
                        t = para.text.strip()
                        if t: txts.append(t)
            joined = clean_surrogates(re.sub(r"\s+", " ", " ".join(txts)).strip())
            slides.append({
                "block": block_name,
                "lecture": name,
                "lecturer": lecturer,
                "slide": i,
                "n": total,
                "text": joined,
                "chars": len(joined)
            })
    except Exception as e:
        print(f"  [PPTX Err] {name}: {e}", flush=True)
    return slides

def main():
    blocks = sorted(os.listdir(LECTURES_DIR))
    all_slides = []
    total_lectures = 0
    
    print("Mengekstrak slide dari seluruh blok...", flush=True)
    for b in blocks:
        bpath = os.path.join(LECTURES_DIR, b)
        if not os.path.isdir(bpath): continue
        files = sorted(os.listdir(bpath))
        b_slides = 0
        b_lecs = 0
        for f in files:
            fpath = os.path.join(bpath, f)
            if f.lower().endswith(".pdf"):
                sl = extract_pdf(fpath, b)
            elif f.lower().endswith(".pptx"):
                sl = extract_pptx(fpath, b)
            else:
                continue
            if sl:
                all_slides.extend(sl)
                b_slides += len(sl)
                b_lecs += 1
                total_lectures += 1
        print(f"  {b:<14} -> {b_lecs:>2} kuliah, {b_slides:>4} slide", flush=True)
        
    print(f"\nTotal: {total_lectures} kuliah, {len(all_slides)} slide terekstrak.")
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(all_slides, f, ensure_ascii=False)
    print(f"Tersimpan di: {OUT}")

if __name__ == "__main__":
    main()
