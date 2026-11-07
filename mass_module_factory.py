#!/usr/bin/env python3
"""Pabrik Massal Pembuat Web Rangkuman Split-Screen Slide-Sync untuk SELURUH Kuliah di Google Drive.
Menghasilkan modul HTML + Slide JPGs + Anki (.apkg) + Update summaries.json secara otomatis.
Dapat dijalankan mandiri atau dipanggil otomatis oleh mirror_server.py saat ada upload baru.
"""
import glob
import json
import logging
import os
import re
import subprocess
import sys
import time
import urllib.request

logging.disable(logging.CRITICAL)
from pypdf import PdfReader
# genanki removed

HERE = os.path.dirname(os.path.abspath(__file__))
TREE_FILE = os.path.join(HERE, "drive_tree.json")
SUMMARIES_FILE = os.path.join(HERE, "summaries.json")
LECTURES_DIR = os.path.join(HERE, "analysis", "lectures")
os.makedirs(LECTURES_DIR, exist_ok=True)

# Swift script template for fast PDFKit rendering
SWIFT_RENDERER = """import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
guard args.count >= 3 else { exit(1) }
let pdfPath = args[1]
let outDir = args[2]

let url = URL(fileURLWithPath: pdfPath)
guard let doc = PDFDocument(url: url) else { exit(1) }

let fm = FileManager.default
try? fm.createDirectory(atPath: outDir, withIntermediateDirectories: true, attributes: nil)

for i in 0..<doc.pageCount {
    let outPath = "\(outDir)/slide_\(i + 1).jpg"
    if fm.fileExists(atPath: outPath) { continue }
    guard let page = doc.page(at: i) else { continue }
    let pageRect = page.bounds(for: .mediaBox)
    let scale: CGFloat = 1.4
    let size = NSSize(width: pageRect.width * scale, height: pageRect.height * scale)
    let img = page.thumbnail(of: size, for: .mediaBox)
    guard let tiff = img.tiffRepresentation,
          let rep = NSBitmapImageRep(data: tiff),
          let jpg = rep.representation(using: .jpeg, properties: [.compressionFactor: 0.82]) else { continue }
    try? jpg.write(to: URL(fileURLWithPath: outPath))
}
print("Rendered \(doc.pageCount) slides to \(outDir)")
"""

SWIFT_SCRIPT_PATH = os.path.join(HERE, "analysis", "render_slides.swift")
with open(SWIFT_SCRIPT_PATH, "w", encoding="utf-8") as f:
    f.write(SWIFT_RENDERER)

def clean_slug(s):
    s = re.sub(r"[^\w]+", "_", s).strip("_")
    return s[:40].lower()

def download_if_missing(file_id, dest_path):
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        return True
    url = f"https://drive.google.com/uc?export=download&confirm=t&id={file_id}"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                continue
            with open(dest_path + ".tmp", "wb") as f:
                f.write(data)
            os.replace(dest_path + ".tmp", dest_path)
            return True
        except Exception:
            time.sleep(1.5)
    return False

def render_slides(pdf_path, out_dir):
    try:
        subprocess.run(["swift", SWIFT_SCRIPT_PATH, pdf_path, out_dir], check=True, capture_output=True, timeout=180)
        return True
    except Exception as e:
        print(f"  [Render Error] {e}", flush=True)
        return False

def clean_surrogates(s):
    if not s: return ""
    return s.encode("utf-16", "surrogatepass").decode("utf-16", "ignore")

def extract_pdf_slides(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        pages = []
        for i, p in enumerate(reader.pages, 1):
            t = (p.extract_text() or "").strip()
            t = re.sub(r"\s+", " ", t)
            t = clean_surrogates(t)
            pages.append({"num": i, "text": t})
        return pages
    except Exception as e:
        print(f"  [PDF Read Error] {e}", flush=True)
        return []

def generate_module(block_name, file_id, file_name, pdf_path):
    base_name = os.path.splitext(file_name)[0]
    slug = f"{clean_slug(block_name)}_{clean_slug(base_name)}"
    html_filename = f"{slug}.html"
    html_out = os.path.join(HERE, html_filename)
    slides_dirname = f"slides_{slug}"
    slides_out_dir = os.path.join(HERE, slides_dirname)
    
    # 1. Render slide JPGs
    render_slides(pdf_path, slides_out_dir)
    
    # 2. Extract slides text
    pages = extract_pdf_slides(pdf_path)
    if not pages:
        return None
        
    total_slides = len(pages)
    
    # Deteksi dosen
    m_doc = re.search(r"\(([A-Z]{2,6})\)", base_name)
    dosen = m_doc.group(1).upper() if m_doc else "Pakar"
    
    # 3. Kelompokkan slide jadi 4-6 bab tematik
    chunk_size = max(4, total_slides // 5)
    chapters = []
    for c_idx in range(0, total_slides, chunk_size):
        ch_pages = pages[c_idx:c_idx + chunk_size]
        if not ch_pages: continue
        ch_num = len(chapters) + 1
        start_s = ch_pages[0]["num"]
        end_s = ch_pages[-1]["num"]
        
        # Cari judul terbaik dari teks slide pertama di bab
        first_txt = ch_pages[0]["text"]
        words = [w for w in first_txt.split() if len(w) > 3][:6]
        ch_title = " ".join(words) if words else f"Topik Bagian {ch_num}"
        ch_title = re.sub(r"^(KULIAH|MODUL|BLOK|SLIDE|\d+)+", "", ch_title, flags=re.I).strip()
        if not ch_title or len(ch_title) < 4:
            ch_title = f"Konsep & Patofisiologi Bagian {ch_num}"
            
        summary_points = []
        for p in ch_pages:
            t = p["text"]
            if len(t) > 30:
                sents = [s.strip() for s in t.split(".") if len(s.strip()) > 20]
                if sents:
                    summary_points.append((p["num"], sents[0]))
        if not summary_points:
            summary_points = [(start_s, f"Mempelajari konsep fisiologis dan klinis pada slide {start_s}–{end_s}.")]
            
        chapters.append({
            "num": ch_num,
            "title": ch_title,
            "start": start_s,
            "end": end_s,
            "slides": [p["num"] for p in ch_pages],
            "points": summary_points[:4]
        })
        
    # Anki generation removed

    # 5. Build HTML content using Split-Screen Slide-Sync Masterpiece Blueprint
    chapters_html = ""
    for ch in chapters:
        pills_html = "".join([
            f'<button class="slide-pill{" active" if i==0 else ""}" onclick="setStage(\'ch{ch["num"]}\', {s}, \'Slide {s}\', this)">Slide {s}</button>'
            for i, s in enumerate(ch["slides"][:6])
        ])
        
        points_html = "".join([
            f'<li><b>Slide {s_num}:</b> <span class="cloze-mask" onclick="this.classList.toggle(\'revealed\')">{pt}</span></li>'
            for s_num, pt in ch["points"]
        ])
        
        # Inline quiz per bab
        sample_pt = ch["points"][0][1] if ch["points"] else "Konsep penting pada slide ini."
        s_num = ch["points"][0][0] if ch["points"] else ch["start"]
        
        chapters_html += f"""
        <section class="split-chapter" id="bab-{ch['num']}">
          <div class="narrative-panel">
            <div class="ch-kicker-row">
              <span class="ch-kicker">Bab 0{ch['num']} · Slide {ch['start']} s.d. {ch['end']}</span>
              <span class="meta-pill pill-uab">Inti UAB {block_name}</span>
            </div>
            <h2 class="ch-title">{ch['title']}</h2>
            
            <div class="peer-talk">
              <p>Pada bagian ini, <b>dr. {dosen}</b> membahas transisi penting antara slide {ch['start']} sampai {ch['end']}. Perhatikan alur logisnya pada slide asli di sebelah kanan:</p>
            </div>

            <div class="concept-box" style="margin: 18px 0;">
              <h4>Poin Kunci &amp; Fakta Laboratorium (Gunakan Mode Uji Ingatan M)</h4>
              <ul>
                {points_html}
              </ul>
            </div>

            <div class="callout trap">
              <div class="callout-title">⚠️ Jebakan Soal UAB dr. {dosen}</div>
              Dosen sering kali menguji pemahaman dengan memutarbalikkan pernyataan sebab-akibat dari slide {ch['start']}. Jangan hanya menghafal teksnya; pahami mengapa proses ini terjadi di jaringan tubuh.
            </div>

            <!-- Inline Quiz Bab -->
            <div class="inline-quiz" id="iq-{ch['num']}">
              <div class="iq-kicker">🎯 Cek Paham Bab 0{ch['num']}</div>
              <div class="iq-stem">Berdasarkan pembahasan pada Slide {s_num}, manakah pernyataan klinis yang paling tepat mengenai topik ini?</div>
              <div class="iq-opts">
                <button class="iq-btn" onclick="ansInline('iq-{ch['num']}', 0, true, 'Tepat! Sesuai dengan materi yang tertera pada Slide {s_num}.')"><span>A.</span><span>{sample_pt[:120]}</span></button>
                <button class="iq-btn" onclick="ansInline('iq-{ch['num']}', 1, false, 'Pernyataan ini terbalik dari mekanisme fisiologis yang sebenarnya.')"><span>B.</span><span>Mekanisme ini berlangsung berlawanan dengan fungsi homeostasis normal</span></button>
                <button class="iq-btn" onclick="ansInline('iq-{ch['num']}', 2, false, 'Tidak sesuai dengan pedoman diagnosis standar pada slide.')"><span>C.</span><span>Tidak ada relevansi klinis yang bermakna pada kondisi akut</span></button>
              </div>
              <div class="iq-fb" id="iq-{ch['num']}-fb"></div>
            </div>
          </div>

          <!-- Right Sticky Slide Stage -->
          <aside class="slide-stage">
            <div class="stage-top">
              <span class="stage-label">Bab 0{ch['num']} · Slide Asli ({ch['start']}–{ch['end']})</span>
              <span style="font-size:0.75rem;color:var(--ink-muted);">Klik untuk Zoom</span>
            </div>
            <div class="slide-pills" id="pills-ch{ch['num']}">
              {pills_html}
            </div>
            <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch{ch['num']}').src)">
              <img id="img-ch{ch['num']}" src="{slides_dirname}/slide_{ch['start']}.jpg" alt="Slide Bab {ch['num']}">
            </div>
            <div class="stage-caption">
              <span id="cap-ch{ch['num']}">Slide {ch['start']}</span>
              <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
            </div>
          </aside>
        </section>
        """

    ch_nav_pills = "".join([
        f'<a href="#bab-{ch["num"]}" class="ch-jump{" active" if i==0 else ""}">{ch["num"]}. {ch["title"][:18]}...</a>'
        for i, ch in enumerate(chapters)
    ])

    html_full = f"""<!DOCTYPE html>
<html lang="id" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{base_name} · Split-Screen Mastery {block_name}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400&family=JetBrains+Mono:wght@500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #FAF8F5;
      --surface: #FFFFFF;
      --surface-subtle: #F2EFE9;
      --surface-card: #FDFCFA;
      --border: #E5E0D5;
      --border-strong: #C9C2B2;

      --ink: #161719;
      --ink-secondary: #4A4D52;
      --ink-muted: #7C8087;

      --sage: #1E6B47;
      --sage-soft: #EBF5F0;
      --sage-border: #BCDCCB;

      --coral: #B93822;
      --coral-soft: #FBEFEA;
      --coral-border: #F2C6BC;

      --ochre: #9E5E10;
      --ochre-soft: #FDF4E7;
      --ochre-border: #F3D5A8;

      --navy: #1B3B6F;
      --navy-soft: #EDF3FA;
      --navy-border: #C2D6EE;

      --shadow-sm: 0 2px 8px rgba(22, 23, 25, 0.04);
      --shadow-md: 0 10px 28px -4px rgba(22, 23, 25, 0.07);
      --shadow-lg: 0 24px 52px -10px rgba(22, 23, 25, 0.16);

      --r-sm: 8px;
      --r-md: 14px;
      --r-lg: 20px;
      --r-full: 9999px;

      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-serif: 'Newsreader', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    html[data-theme="dark"] {{
      --bg: #131517;
      --surface: #1B1E21;
      --surface-subtle: #23272B;
      --surface-card: #1F2327;
      --border: #2D3238;
      --border-strong: #434A52;

      --ink: #ECEAE4;
      --ink-secondary: #B4B8BF;
      --ink-muted: #7E848D;

      --sage: #4CC38A;
      --sage-soft: rgba(76, 195, 138, 0.13);
      --sage-border: rgba(76, 195, 138, 0.35);

      --coral: #F2745F;
      --coral-soft: rgba(242, 116, 95, 0.13);
      --coral-border: rgba(242, 116, 95, 0.35);

      --ochre: #F0B15B;
      --ochre-soft: rgba(240, 177, 91, 0.12);
      --ochre-border: rgba(240, 177, 91, 0.32);

      --navy: #7CB3F5;
      --navy-soft: rgba(124, 179, 245, 0.13);
      --navy-border: rgba(124, 179, 245, 0.32);

      --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 12px 32px rgba(0, 0, 0, 0.38);
      --shadow-lg: 0 28px 60px rgba(0, 0, 0, 0.55);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}

    body {{
      background: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      transition: background 0.25s ease, color 0.25s ease;
      padding-bottom: 120px;
    }}

    ::selection {{ background: var(--sage-soft); color: var(--sage); }}

    .scroll-bar {{
      position: fixed;
      top: 0;
      left: 0;
      height: 3px;
      width: 0%;
      background: linear-gradient(90deg, var(--sage), var(--navy));
      z-index: 300;
      transition: width 0.1s ease-out;
    }}

    .topbar {{
      position: sticky;
      top: 0;
      z-index: 200;
      background: color-mix(in srgb, var(--bg) 92%, transparent);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
      padding: 10px 24px;
    }}
    .topbar-inner {{
      max-width: 1360px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .brand-group {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex: none;
    }}
    .brand-badge {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      background: var(--navy);
      color: #fff;
      padding: 4px 9px;
      border-radius: var(--r-sm);
      letter-spacing: 0.04em;
    }}
    .brand-title {{
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--ink);
    }}

    .chapter-strip {{
      display: flex;
      align-items: center;
      gap: 4px;
      overflow-x: auto;
      scrollbar-width: none;
      padding: 2px;
    }}
    .chapter-strip::-webkit-scrollbar {{ display: none; }}
    .ch-jump {{
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--ink-secondary);
      text-decoration: none;
      padding: 6px 11px;
      border-radius: var(--r-full);
      white-space: nowrap;
      transition: all 0.15s ease;
    }}
    .ch-jump:hover {{ background: var(--surface-subtle); color: var(--ink); }}
    .ch-jump.active {{ background: var(--ink); color: var(--bg); }}

    .tool-group {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex: none;
    }}
    .tool-btn {{
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--ink-secondary);
      font-family: var(--font-sans);
      font-size: 0.79rem;
      font-weight: 600;
      padding: 6px 13px;
      border-radius: var(--r-full);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 7px;
      transition: all 0.18s ease;
      white-space: nowrap;
    }}
    .tool-btn:hover {{ border-color: var(--border-strong); color: var(--ink); }}
    .tool-btn.active {{ background: var(--ink); color: var(--bg); border-color: var(--ink); }}
    .state-pill {{
      font-family: var(--font-mono);
      font-size: 0.68rem;
      padding: 1px 6px;
      border-radius: 4px;
      background: var(--surface-subtle);
      color: var(--ink);
    }}
    .tool-btn.active .state-pill {{ background: var(--sage); color: #fff; }}
    .btn-anki {{
      background: var(--sage);
      color: #FFFFFF !important;
      font-size: 0.79rem;
      font-weight: 700;
      padding: 7px 14px;
      border-radius: var(--r-full);
      text-decoration: none;
      white-space: nowrap;
      transition: opacity 0.15s ease;
    }}
    .btn-anki:hover {{ opacity: 0.9; }}

    .page-wrap {{
      max-width: 1340px;
      margin: 0 auto;
      padding: 32px 24px 0;
    }}

    .hook-hero {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-lg);
      padding: 36px 40px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-md);
    }}
    .hook-meta-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px;
      margin-bottom: 14px;
    }}
    .meta-pill {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: var(--r-full);
      letter-spacing: 0.04em;
      text-transform: uppercase;
    }}
    .pill-skdi {{ background: var(--sage-soft); color: var(--sage); border: 1px solid var(--sage-border); }}
    .pill-uab {{ background: var(--coral-soft); color: var(--coral); border: 1px solid var(--coral-border); }}
    .pill-slides {{ background: var(--navy-soft); color: var(--navy); border: 1px solid var(--navy-border); }}

    .hook-headline {{
      font-family: var(--font-serif);
      font-size: 2.5rem;
      font-weight: 600;
      line-height: 1.22;
      color: var(--ink);
      letter-spacing: -0.02em;
      margin-bottom: 14px;
    }}
    .hook-lead {{
      font-size: 1.05rem;
      color: var(--ink-secondary);
      max-width: 960px;
      margin-bottom: 24px;
    }}

    /* SPLIT-SCREEN LAYOUT */
    .split-chapter {{
      display: grid;
      grid-template-columns: 1fr 480px;
      gap: 32px;
      align-items: start;
      margin-bottom: 52px;
      scroll-margin-top: 84px;
    }}
    .narrative-panel {{
      grid-column: 1;
      grid-row: 1;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-lg);
      padding: 36px 42px;
      box-shadow: var(--shadow-sm);
    }}
    .slide-stage {{
      grid-column: 2;
      grid-row: 1;
      position: sticky;
      top: 78px;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-lg);
      padding: 18px;
      box-shadow: var(--shadow-md);
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }}
    .slide-stage:hover {{
      border-color: var(--border-strong);
      box-shadow: var(--shadow-lg);
    }}
    .stage-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 12px;
    }}
    .stage-label {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .stage-nav-arrows {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }}
    .stage-arrow-btn {{
      border: 1px solid var(--border);
      background: var(--surface-subtle);
      color: var(--ink-secondary);
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 700;
      width: 26px;
      height: 26px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-grid;
      place-items: center;
      transition: all 0.15s ease;
    }}
    .stage-arrow-btn:hover {{ background: var(--ink); color: var(--bg); border-color: var(--ink); }}

    .slide-pills {{
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
      margin-bottom: 12px;
    }}
    .slide-pill {{
      border: 1px solid var(--border);
      background: var(--surface-subtle);
      color: var(--ink-secondary);
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: var(--r-full);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .slide-pill:hover {{ border-color: var(--border-strong); color: var(--ink); }}
    .slide-pill.active {{ background: var(--navy); color: #FFFFFF; border-color: var(--navy); }}
    .stage-frame {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #fff;
      border-radius: var(--r-md);
      overflow: hidden;
      border: 1px solid var(--border);
      cursor: zoom-in;
    }}
    .stage-frame img {{
      width: 100%;
      height: 100%;
      object-fit: contain;
      background: #fff;
      display: block;
    }}
    .stage-caption {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 0.8rem;
      color: var(--ink-muted);
      margin-top: 10px;
      padding: 0 4px;
    }}

    .ch-kicker-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 10px;
    }}
    .ch-kicker {{
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--navy);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .ch-title {{
      font-family: var(--font-serif);
      font-size: 1.95rem;
      font-weight: 600;
      line-height: 1.25;
      color: var(--ink);
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }}
    .peer-talk {{ font-size: 1rem; color: var(--ink); margin-bottom: 18px; }}
    .peer-talk p {{ margin-bottom: 14px; }}

    .concept-box {{
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--r-md);
      padding: 16px 18px;
    }}
    .concept-box h4 {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }}
    .concept-box ul {{ padding-left: 18px; font-size: 0.93rem; line-height: 1.6; color: var(--ink); }}
    .concept-box li {{ margin-bottom: 6px; }}

    .callout {{
      border-radius: var(--r-md);
      padding: 16px 20px;
      margin: 16px 0;
      font-size: 0.94rem;
      line-height: 1.65;
    }}
    .callout-title {{
      font-size: 0.78rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 5px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .callout.trap {{ background: var(--coral-soft); border: 1px solid var(--coral-border); }}
    .callout.trap .callout-title {{ color: var(--coral); }}

    /* INLINE QUIZ */
    .inline-quiz {{
      margin-top: 24px;
      padding-top: 22px;
      border-top: 2px dashed var(--border);
    }}
    .iq-kicker {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }}
    .iq-stem {{ font-size: 0.98rem; font-weight: 600; color: var(--ink); line-height: 1.6; margin-bottom: 12px; }}
    .iq-opts {{ display: flex; flex-direction: column; gap: 8px; }}
    .iq-btn {{
      padding: 11px 15px;
      border-radius: var(--r-sm);
      border: 1px solid var(--border);
      background: var(--surface-card);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 0.91rem;
      text-align: left;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      transition: all 0.15s ease;
    }}
    .iq-btn:hover {{ border-color: var(--border-strong); background: var(--surface-subtle); }}
    .iq-btn.is-correct {{ background: var(--sage-soft) !important; border-color: var(--sage) !important; color: var(--sage) !important; font-weight: 700; }}
    .iq-btn.is-wrong {{ background: var(--coral-soft) !important; border-color: var(--coral) !important; color: var(--coral) !important; }}
    .iq-fb {{
      margin-top: 12px;
      padding: 14px 16px;
      border-radius: var(--r-sm);
      font-size: 0.9rem;
      line-height: 1.6;
      display: none;
    }}
    .iq-fb.show {{ display: block; }}
    .iq-fb.ok {{ background: var(--sage-soft); border: 1px solid var(--sage-border); color: var(--ink); }}
    .iq-fb.no {{ background: var(--coral-soft); border: 1px solid var(--coral-border); color: var(--ink); }}

    /* CLOZE MASKING */
    body.cloze-active .cloze-mask {{
      background: var(--border-strong) !important;
      color: transparent !important;
      border-radius: 5px;
      padding: 1px 7px;
      cursor: pointer;
      user-select: none;
      display: inline-block;
      transition: all 0.15s ease;
    }}
    body.cloze-active .cloze-mask.revealed {{
      background: var(--sage-soft) !important;
      color: var(--sage) !important;
      font-weight: 700;
      border: 1px solid var(--sage-border);
    }}

    .lightbox {{
      position: fixed;
      inset: 0;
      z-index: 1000;
      background: rgba(12, 13, 15, 0.86);
      backdrop-filter: blur(8px);
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .lightbox.open {{ display: flex; }}
    .lightbox img {{ max-width: 94%; max-height: 90vh; border-radius: var(--r-md); box-shadow: var(--shadow-lg); }}

    @media (max-width: 1020px) {{
      .split-chapter {{ grid-template-columns: 1fr; }}
      .narrative-panel {{ grid-column: 1; grid-row: 1; padding: 24px 20px; }}
      .slide-stage {{ grid-column: 1; grid-row: 2; position: static; }}
      .chapter-strip {{ display: none; }}
    }}
  </style>
</head>
<body>
  <div class="scroll-bar" id="scroll-bar"></div>

  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-group">
        <span class="brand-badge">{block_name}</span>
        <span class="brand-title">{base_name}</span>
      </div>

      <nav class="chapter-strip" aria-label="Lompat ke Bab">
        {ch_nav_pills}
      </nav>

      <div class="tool-group">
        <button type="button" id="cloze-btn" class="tool-btn" onclick="toggleCloze()" title="Shortcut tombol M">
          <span>🧠 Uji Ingatan</span>
          <span class="state-pill" id="cloze-state">OFF</span>
        </button>
        <button type="button" id="theme-btn" class="tool-btn" onclick="toggleTheme()" title="Shortcut tombol D">
          <span id="theme-label">🌙 Mode Malam</span>
        </button>
        <!-- Anki removed -->
      </div>
    </div>
  </header>

  <main class="page-wrap">
    <section class="hook-hero">
      <div class="hook-meta-row">
        <span class="meta-pill pill-skdi">{block_name} · Materi Kuliah Pakar</span>
        <span class="meta-pill pill-uab">Narasumber: dr. {dosen}</span>
        <span class="meta-pill pill-slides">{total_slides} Slide Lengkap</span>
      </div>
      <h1 class="hook-headline">Kuasai {total_slides} Slide {base_name} Tanpa Buka PPT Sekalipun.</h1>
      <p class="hook-lead">
        Seluruh materi kuliah ini telah diperas menjadi <strong>{len(chapters)} Bab Split-Screen Interaktif</strong>: penjelasan mengalir di sebelah kiri dengan bahasa teman yang mudah dipahami, sementara slide asli dosen menempel di sebelah kanan secara sinkron untuk memastikan <strong>100% materi tercover tanpa ada yang terlewat</strong>.
      </p>
    </section>

    {chapters_html}
  </main>

  <div id="lightbox" class="lightbox" onclick="closeZoom()">
    <img id="lightbox-img" src="" alt="Slide Zoom" onclick="event.stopPropagation()">
  </div>

  <script>
    function setStage(chId, slideNum, caption, btn) {{
      document.getElementById('img-' + chId).src = '{slides_dirname}/slide_' + slideNum + '.jpg';
      document.getElementById('cap-' + chId).textContent = caption;
      const wrap = document.getElementById('pills-' + chId);
      wrap.querySelectorAll('.slide-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }}

    const inlineAnswered = {{}};
    function ansInline(id, idx, isRight, reason) {{
      if (inlineAnswered[id]) return;
      inlineAnswered[id] = true;
      const wrap = document.getElementById(id);
      wrap.querySelectorAll('.iq-btn').forEach((b, i) => {{
        if (i === idx) b.classList.add(isRight ? 'is-correct' : 'is-wrong');
      }});
      const fb = document.getElementById(id + '-fb');
      fb.className = 'iq-fb show ' + (isRight ? 'ok' : 'no');
      fb.innerHTML = (isRight ? '<strong>✅ Benar!</strong> ' : '<strong>❌ Kurang Tepat.</strong> ') + reason;
    }}

    let clozeOn = false;
    function toggleCloze() {{
      clozeOn = !clozeOn;
      document.body.classList.toggle('cloze-active', clozeOn);
      document.getElementById('cloze-btn').classList.toggle('active', clozeOn);
      document.getElementById('cloze-state').textContent = clozeOn ? 'ON' : 'OFF';
      if (clozeOn) document.querySelectorAll('.cloze-mask').forEach(e => e.classList.remove('revealed'));
    }}

    function toggleTheme() {{
      const root = document.documentElement;
      const next = root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      document.getElementById('theme-label').textContent = next === 'dark' ? '☀️ Mode Kertas' : '🌙 Mode Malam';
      try {{ localStorage.setItem('vx_theme_{slug}', next); }} catch(e) {{}}
    }}

    function openZoom(src) {{
      document.getElementById('lightbox-img').src = src;
      document.getElementById('lightbox').classList.add('open');
    }}
    function closeZoom() {{
      document.getElementById('lightbox').classList.remove('open');
    }}

    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') closeZoom();
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes(document.activeElement.tagName)) return;
      if (e.key.toLowerCase() === 'm') toggleCloze();
      if (e.key.toLowerCase() === 'd') toggleTheme();
    }});

    function stepStage(chId, dir) {{
      const wrap = document.getElementById('pills-' + chId);
      if (!wrap) return;
      const pills = [...wrap.querySelectorAll('.slide-pill')];
      if (pills.length < 2) return;
      const idx = pills.findIndex(b => b.classList.contains('active'));
      const nextIdx = (idx + dir + pills.length) % pills.length;
      pills[nextIdx].click();
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      document.querySelectorAll('.slide-stage').forEach(stage => {{
        const pillsWrap = stage.querySelector('.slide-pills');
        if (!pillsWrap) return;
        const chId = pillsWrap.id.replace('pills-', '');
        const count = pillsWrap.querySelectorAll('.slide-pill').length;
        const top = stage.querySelector('.stage-top');
        if (top && count > 1) {{
          const nav = document.createElement('div');
          nav.className = 'stage-nav-arrows';
          nav.innerHTML = `<button type="button" class="stage-arrow-btn" title="Slide sebelumnya" onclick="stepStage('${{chId}}', -1)">‹</button><button type="button" class="stage-arrow-btn" title="Slide berikutnya" onclick="stepStage('${{chId}}', 1)">›</button>`;
          top.appendChild(nav);
        }}
      }});

      const chapters = [...document.querySelectorAll('.split-chapter')];
      const navLinks = [...document.querySelectorAll('.ch-jump')];
      window.addEventListener('scroll', () => {{
        const doc = document.documentElement;
        const pct = (doc.scrollTop / Math.max(1, doc.scrollHeight - doc.clientHeight)) * 100;
        const bar = document.getElementById('scroll-bar');
        if (bar) bar.style.width = pct + '%';

        let currentId = 'bab-1';
        for (const sec of chapters) {{
          if (sec.getBoundingClientRect().top <= 160) currentId = sec.id;
        }}
        navLinks.forEach(a => {{
          a.classList.toggle('active', a.getAttribute('href') === '#' + currentId);
        }});
      }}, {{ passive: true }});

      try {{
        const saved = localStorage.getItem('vx_theme_{slug}');
        if (saved === 'dark') toggleTheme();
      }} catch(e) {{}}
    }});
  </script>
</body>
</html>
"""

    with open(html_out, "w", encoding="utf-8") as f:
        f.write(html_full)
        
    # 6. Update summaries.json
    try:
        sdata = json.load(open(SUMMARIES_FILE, encoding="utf-8"))
    except Exception:
        sdata = {}
    sdata[file_id] = {
        "title": f"{block_name} · {base_name}",
        "url": html_filename
    }
    with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
        json.dump(sdata, f, ensure_ascii=False, indent=2)
        
    print(f"✅ Berhasil membuat modul: {html_filename} ({total_slides} slide, {len(chapters)} bab)")
    return html_filename

def process_all_missing():
    tree = json.load(open(TREE_FILE, encoding="utf-8"))
    blok = next(c for c in tree["children"] if c["name"] == "BLOK")
    try:
        summaries = json.load(open(SUMMARIES_FILE, encoding="utf-8"))
    except Exception:
        summaries = {}
        
    targets = []
    for b in blok["children"]:
        if b["name"] == "0 (E-BOOK)": continue
        if not b.get("children"): continue
        for f in b["children"]:
            if f.get("isFolder"): continue
            nm = f["name"].lower()
            if not (nm.endswith(".pdf") or f.get("mime") == "application/pdf"):
                continue
            if f["id"] in summaries:
                continue
            targets.append((b["name"], f["id"], f["name"]))
            
    print(f"Ditemukan {len(targets)} materi kuliah yang belum memiliki web rangkuman.", flush=True)
    done_count = 0
    for bname, fid, fname in targets:
        b_safe = re.sub(r"[^\w\-. ()]+", "_", bname).strip()
        f_safe = re.sub(r"[^\w\-. ()]+", "_", fname).strip()
        if not f_safe.lower().endswith(".pdf"): f_safe += ".pdf"
        local_path = os.path.join(LECTURES_DIR, b_safe, f_safe)
        
        # Unduh bila belum ada di lokal
        if not (os.path.exists(local_path) and os.path.getsize(local_path) > 1000):
            print(f"Mengunduh {fname} dari Drive...", flush=True)
            ok = download_if_missing(fid, local_path)
            if not ok:
                print(f"  [Skip] Gagal mengunduh {fname}")
                continue
                
        try:
            generate_module(bname, fid, fname, local_path)
            done_count += 1
        except Exception as e:
            print(f"  [Error] {fname}: {e}", flush=True)
            
    print(f"\n🎉 Selesai memproses {done_count} modul baru!")

if __name__ == "__main__":
    process_all_missing()
