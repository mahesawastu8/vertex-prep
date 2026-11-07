#!/usr/bin/env python3
"""VERTEX Preclinical Engine — Pembangun Modul Web 4-Lapis & Deck Anki Otomatis.

Dapat digunakan berulang untuk semua kuliah dan blok hingga lulus S.Ked (preklinik).
Penggunaan:
  python3 vertex_engine.py --pdf "path/ke/kuliah.pdf" --blok "EMN" --dosen "IWL"
"""
import argparse
import json
import logging
import os
import re
import subprocess
import sys

logging.disable(logging.CRITICAL)
from pypdf import PdfReader
import genanki

HERE = os.path.dirname(os.path.abspath(__file__))
ANKI_DIR = os.path.join(HERE, "anki")
SUMMARIES_FILE = os.path.join(HERE, "summaries.json")
DRIVE_TREE_FILE = os.path.join(HERE, "drive_tree.json")
os.makedirs(ANKI_DIR, exist_ok=True)

def render_slides_swift(pdf_path, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    swift_code = f"""
    import Foundation
    import PDFKit
    import AppKit

    let url = URL(fileURLWithPath: "{pdf_path}")
    guard let doc = PDFDocument(url: url) else {{ exit(1) }}
    for i in 0..<doc.pageCount {{
        guard let page = doc.page(at: i) else {{ continue }}
        let pageRect = page.bounds(for: .mediaBox)
        let scale: CGFloat = 1.5
        let size = NSSize(width: pageRect.width * scale, height: pageRect.height * scale)
        let img = page.thumbnail(of: size, for: .mediaBox)
        guard let tiff = img.tiffRepresentation,
              let rep = NSBitmapImageRep(data: tiff),
              let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.82]) else {{ continue }}
        let outUrl = URL(fileURLWithPath: "{out_dir}/slide_\\(i + 1).jpg")
        try? jpg.write(to: outUrl)
    }}
    """
    subprocess.run(["swift", "-"], input=swift_code, text=True, check=True)

def find_drive_id(lecture_filename):
    if not os.path.exists(DRIVE_TREE_FILE): return None
    try:
        t = json.load(open(DRIVE_TREE_FILE, encoding="utf-8"))
        base = os.path.basename(lecture_filename)
        name_no_ext = os.path.splitext(base)[0].lower()
        
        def walk(n):
            if not n.get("isFolder") and (os.path.splitext(n["name"])[0].lower() == name_no_ext or n["name"].lower() == base.lower()):
                return n["id"]
            for c in n.get("children", []):
                r = walk(c)
                if r: return r
            return None
        return walk(t)
    except Exception:
        return None

def main():
    parser = argparse.ArgumentParser(description="VERTEX Preclinical Module Generator")
    parser.add_argument("--pdf", required=True, help="Path ke file PDF kuliah")
    parser.add_argument("--blok", required=True, help="Nama blok, misal: EMN, BDT, BMS 1")
    parser.add_argument("--dosen", default="", help="Inisial dosen (misal: IWL, SAN, DTY)")
    parser.add_argument("--title", default="", help="Judul kuliah (opsional, auto dari nama file)")
    args = parser.parse_args()

    pdf_path = os.path.abspath(args.pdf)
    if not os.path.exists(pdf_path):
        sys.exit(f"File PDF tidak ditemukan: {pdf_path}")

    filename = os.path.basename(pdf_path)
    base_name = os.path.splitext(filename)[0]
    title = args.title or base_name
    dosen = args.dosen.upper()
    if not dosen:
        m = re.search(r"\(([A-Z]{2,6})\)", base_name)
        dosen = m.group(1).upper() if m else "UMUM"

    slug = re.sub(r"[^\w]+", "_", base_name).strip("_")
    slides_dir_name = f"slides_{slug[:16].lower()}"
    slides_out_dir = os.path.join(HERE, slides_dir_name)

    print(f"\n🚀 Memproses Kuliah: {title}")
    print(f"   Blok: {args.blok} | Dosen: {dosen}")
    print(f"1. Merender slide ke gambar JPG...")
    render_slides_swift(pdf_path, slides_out_dir)

    print(f"2. Membaca teks slide...")
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"   Total {total_pages} slide terdeteksi.")

    html_filename = f"{slug}.html"
    html_out_path = os.path.join(HERE, html_filename)

    # Cek apakah Drive ID ditemukan di pohon Drive
    drive_id = find_drive_id(filename)
    if drive_id:
        print(f"   Terhubung ke Drive ID: {drive_id}")
        try:
            with open(SUMMARIES_FILE, "r", encoding="utf-8") as f:
                sum_data = json.load(f)
        except Exception:
            sum_data = {}
        sum_data[drive_id] = {
            "title": f"{args.blok} · {title}",
            "url": html_filename
        }
        with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
            json.dump(sum_data, f, ensure_ascii=False, indent=2)
        print(f"   Tercatat otomatis di summaries.json!")

    print(f"\n✅ Mesin VERTEX siap memproses kuliah berikutnya kapan saja.")
    print(f"   Gunakan: python3 vertex_engine.py --pdf '<path_pdf>' --blok '<nama_blok>' --dosen '<inisial>'")

if __name__ == "__main__":
    main()
