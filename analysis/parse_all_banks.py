#!/usr/bin/env python3
"""Parse semua file di Bank_Soal_UAB (PDF, DOCX, dan OCR untuk PDF scan)
lalu kelompokkan per blok (BUAMS, BMS 1-4, BMD, BDT, HI) -> all_bank_questions.json"""
import glob
import json
import logging
import os
import re
import sys
import subprocess

logging.disable(logging.CRITICAL)
from pypdf import PdfReader
try:
    import docx
except ImportError:
    docx = None

HERE = os.path.dirname(os.path.abspath(__file__))
BANK_DIR = os.path.join(HERE, "..", "Bank_Soal_UAB")
OUT = os.path.join(HERE, "all_bank_questions.json")

def detect_block(filename, text_sample=""):
    fn = filename.upper()
    ts = text_sample.upper()
    
    if "BUAMS" in fn: return "1 (BUAMS)"
    if "BMS 1" in fn or "BMS1" in fn: return "2 (BMS 1)"
    if "BMS 2" in fn or "BMS2" in fn: return "3 (BMS 2)"
    if "BMS 3" in fn or "BMS3" in fn: return "4 (BMS 3)"
    if "BMS 4" in fn or "BMS4" in fn: return "5 (BMS 4)"
    if "BMD" in fn: return "6 (BMD)"
    if "BDT" in fn or "BASIC DIAGNOSTIC" in fn: return "7 (BDT)"
    if " HI " in fn or "HI." in fn or fn.endswith("HI") or "HIHIHI" in fn or "HI 20" in fn or "HI COSTANION" in fn or "HI AXONATION" in fn:
        return "8 (HI)"
    
    # Deteksi berdasarkan isi untuk file tanpa nama blok
    if "SPICES" in ts or "KEPEMIMPINAN" in ts: return "1 (BUAMS)"
    if "REABSORPSI" in ts and "GLOMERULUS" in ts: return "5 (BMS 4)"
    if "LUKA BABRAS" in ts and "ASAM MEFENAMAT" in ts: return "7 (BDT)"
    
    return "UNKNOWN"

def read_pdf(path):
    try:
        r = PdfReader(path)
        txt = " ".join((p.extract_text() or "") for p in r.pages)
        if len(txt.strip()) > 300:
            return txt
    except Exception as e:
        pass
    
    # Jika PDF hasil scan (teks kosong/sangat sedikit), gunakan Apple Vision OCR via swift
    print(f"  [OCR] Menjalankan Vision OCR untuk PDF scan: {os.path.basename(path)}", flush=True)
    swift_script = f"""
    import Foundation
    import PDFKit
    import Vision
    import AppKit

    let url = URL(fileURLWithPath: "{path}")
    guard let doc = PDFDocument(url: url) else {{ exit(1) }}
    var fullText = ""
    for i in 0..<doc.pageCount {{
        guard let page = doc.page(at: i) else {{ continue }}
        let img = page.thumbnail(of: NSSize(width: 1400, height: 1800), for: .mediaBox)
        guard let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {{ continue }}
        let req = VNRecognizeTextRequest()
        req.recognitionLevel = .accurate
        try? VNImageRequestHandler(cgImage: cg).perform([req])
        let txt = (req.results ?? []).compactMap {{ $0.topCandidates(1).first?.string }}.joined(separator: " ")
        fullText += txt + "\\n\\n"
    }}
    print(fullText)
    """
    try:
        p = subprocess.run(["swift", "-"], input=swift_script, text=True, capture_output=True, timeout=180)
        return p.stdout
    except Exception as e:
        print(f"  [OCR Error] {e}", flush=True)
        return ""

def read_docx(path):
    if not docx: return ""
    try:
        doc = docx.Document(path)
        return "\n\n".join(p.text for p in doc.paragraphs)
    except Exception as e:
        return ""

def clean_surrogates(s):
    if not s: return ""
    return s.encode("utf-16", "surrogatepass").decode("utf-16", "ignore")

def norm(t):
    t = clean_surrogates(t)
    t = t.replace("\u00a0", " ")
    t = re.sub(r"[ \t\r\n]+", " ", t)
    return t.strip()
def split_numbered(t, loose=False):
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

def parse_text_to_questions(raw, filename, block_name):
    blocks = split_numbered(norm(raw))
    if len(blocks) < 5:
        blocks = [(i + 1, norm(p)) for i, p in enumerate(re.split(r"\n[ \t]*\n", raw)) if p.strip()]
    
    questions = []
    for k, blk in blocks:
        r = split_options(blk)
        if not r or len(r[0]) < 12:
            continue
        stem, opts = r
        stem = re.sub(r"^\d{1,3}\s?[\.\)]\s+", "", stem)
        questions.append({
            "block": block_name,
            "source": filename,
            "no": k,
            "stem": stem,
            "options": opts
        })
    return questions

def main():
    files = sorted(os.listdir(BANK_DIR))
    all_qs = []
    by_block_count = {}
    
    print(f"Memproses {len(files)} file di Bank_Soal_UAB...", flush=True)
    for fn in files:
        if fn.startswith("."): continue
        path = os.path.join(BANK_DIR, fn)
        ext = fn.split(".")[-1].lower()
        if ext not in ("pdf", "docx"): continue
        
        if ext == "pdf":
            raw = read_pdf(path)
        else:
            raw = read_docx(path)
            
        if not raw or len(raw.strip()) < 50:
            print(f"  [Kosong/Lewat] {fn}", flush=True)
            continue
            
        block = detect_block(fn, raw[:2000])
        qs = parse_text_to_questions(raw, fn, block)
        print(f"  {len(qs):>3} soal | Blok: {block:<12} | File: {fn}", flush=True)
        by_block_count[block] = by_block_count.get(block, 0) + len(qs)
        all_qs.extend(qs)
        
    print("\nRingkasan Soal per Blok:")
    for b, c in sorted(by_block_count.items()):
        print(f"  {b:<14}: {c:>4} butir soal")
        
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(all_qs, f, ensure_ascii=False, indent=1)
    print(f"\nTotal tersimpan: {len(all_qs)} soal -> {OUT}")

if __name__ == "__main__":
    main()
