#!/usr/bin/env python3
"""Build Split-Screen Slide-Sync Masterpiece for Blok 9 (EMN) · KUL 2 Defisiensi Vitamin (dr. Iwal Reza Ahdi, Sp.PD / IWL).
Generates:
1. EMN_KUL2_Defisiensi_Vitamin.html (Split-Screen Slide-Sync Masterpiece with right-sticky slide stage, peer narrative, AMBOSS tooltips, cloze masking, Folate vs B12 simulator, inline quizzes, and 8 Tryout UAB questions).
2. Anki Deck: anki/VERTEX_EMN_KUL2_Defisiensi_Vitamin.apkg
3. Registers Drive ID in summaries.json.
"""
import os
import json
import genanki

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL2_Defisiensi_Vitamin.html")
ANKI_DIR = os.path.join(BASE_DIR, "anki")
SUMMARIES_FILE = os.path.join(BASE_DIR, "summaries.json")
os.makedirs(ANKI_DIR, exist_ok=True)

def tt(term, title, desc, pearl):
    return (
        f'<span class="med-term" tabindex="0">{term}'
        f'<span class="med-tooltip">'
        f'<span class="tt-kicker">Kamus Vitamin & Hematologi</span>'
        f'<span class="tt-title">{title}</span>'
        f'<span class="tt-desc">{desc}</span>'
        f'<span class="tt-pearl">💡 {pearl}</span>'
        f'</span></span>'
    )

def cl(text):
    return f'<span class="cloze-mask" onclick="this.classList.toggle(\'revealed\')" title="Klik untuk membuka">{text}</span>'

# 1. ANKI DECK GENERATION
model = genanki.Model(
    1607392502,
    "VERTEX-PREP EMN KUL 2 Vitamin Model",
    fields=[{"name": "Question"}, {"name": "Answer"}, {"name": "SlideProof"}],
    templates=[{
        "name": "Card 1",
        "qfmt": '<div style="font-family:Plus Jakarta Sans,sans-serif;font-size:16px;color:#161719;padding:12px;"><b>{{Question}}</b></div>',
        "afmt": '{{FrontSide}}<hr id="answer"><div style="font-family:Plus Jakarta Sans,sans-serif;font-size:15px;color:#1E6B47;padding:12px;">{{Answer}}</div><div style="font-size:12px;color:#7C8087;padding:6px 12px;">Bukti: {{SlideProof}}</div>',
    }],
)

deck = genanki.Deck(2059400502, "VERTEX-PREP :: Blok 9 (EMN) :: KUL 2 Defisiensi Vitamin (dr. Iwal, Sp.PD)")
for q, a, sp in [
    ("Biomarker laboratorium apa yang NAIK SPESIFIK pada defisiensi Vitamin B12 (Kobalamin) tetapi NORMAL pada defisiensi Folat (B9)?",
     "<b>Asam Metilmalonat (MMA / Methylmalonic Acid)</b>. Homosistein meningkat pada KEDUANYA, tetapi MMA hanya naik spesifik pada defisiensi B12 karena kobalamin adalah kofaktor enzim metilmalonil-CoA mutase.",
     "Slide 17: Tabel Pembeda Folat vs B12"),
    ("Mengapa memberikan suplementasi Asam Folat (B9) dosis tinggi pada pasien yang sebenarnya mengalami defisiensi B12 sangat berbahaya (The Folate Trap)?",
     "Karena asam folat akan mengoreksi kelainan darah anemia megaloblastiknya, namun <b>kegagalan mielinisasi saraf akan terus berjalan tanpa disadari</b> hingga memicu <b>kerusakan saraf permanen yang ireversibel</b> (<i>Subacute Combined Degeneration of the Spinal Cord</i>)!",
     "Slide 17: Catatan Klinis Mielopati"),
    ("Trias / Tetrad gejala klinis khas apa yang menandakan penyakit Pellagra akibat defisiensi Vitamin B3 (Niasin)?",
     "<b>Tetrad 4D:</b><br>1. <b>Dermatitis:</b> Ruam hiperpigmentasi fotosensitif simetris pada area terbuka sinar matahari (seperti kalung <i>Casal's necklace</i>).<br>2. <b>Diarrhea:</b> Diare cair kronik akibat kerusakan mukosa usus.<br>3. <b>Dementia:</b> Gangguan memori, halusinasi, dan depresi.<br>4. <b>Death:</b> Kematian bila tidak diterapi.",
     "Slide 20: Vitamin B3 (Niasin)"),
    ("Apa perbedaan manifestasi klinis utama antara Beriberi Basah vs Beriberi Kering akibat defisiensi Vitamin B1 (Tiamin)?",
     "• <b>Beriberi Basah (Wet Beriberi):</b> Keterlibatan kardiovaskular berupa <i>high-output heart failure</i>, dilatasi jantung, edema tungkai, dan sesak napas.<br>• <b>Beriberi Kering (Dry Beriberi):</b> Keterlibatan neurologis murni berupa neuropati perifer simetris (kelemahan otot tungkai dan gangguan sensorik 'kaus kaki & sarung tangan').",
     "Slide 18 & 19: Vitamin B1"),
    ("Obat anti-tuberkulosis (OAT) lini pertama manakah yang secara spesifik memicu defisiensi Vitamin B6 (Piridoksin) dan bagaimana cara mencegahnya?",
     "Obat <b>Isoniazid (INH)</b>. INH berikatan dengan piridoksal fosfat dan menghambat enzim piridoksin kinase sehingga memicu neuropati perifer. Pencegahannya: <b>wajib berikan suplementasi Vitamin B6 (10–25 mg/hari) bersamaan dengan terapi INH</b>.",
     "Slide 20: Vitamin B6 & Sinergi Obat"),
    ("Tahapan klinis defisiensi Vitamin A pada mata menurut klasifikasi WHO (dari paling awal hingga kebutaan permanen)?",
     "1. <b>XN:</b> Buta senja (<i>nyctalopia</i>) &rarr; paling dini!<br>2. <b>X1A / X1B:</b> Xerosis konjungtiva dan <b>Bercak Bitot (Bitot's spots)</b> (bercak busa keputihan di konjungtiva bulbi temporal).<br>3. <b>X2:</b> Xerosis kornea (kornea kering kusam).<br>4. <b>X3A / X3B:</b> Ulkus kornea dan <b>Keratomalasia</b> (kornea melunak hancur &rarr; kebutaan permanen).",
     "Slide 8, 9, 10: Vitamin A & Xerophthalmia"),
    ("Apa kelainan patofisiologis utama pada penyakit Scurvy akibat defisiensi Vitamin C (Asam Askorbat)?",
     "Vitamin C adalah kofaktor enzim <i>prolyl &amp; lysyl hydroxylase</i> untuk <b>hidroksilasi kolagen</b>. Defisiensi menyebabkan kerapuhan dinding kapiler pembuluh darah &rarr; perdarahan gusi, petekie perifolikular, rambut melingkar seperti pembuka tutup botol (<i>corkscrew hairs</i>), dan luka gagal sembuh.",
     "Slide 21: Vitamin C"),
]:
    deck.add_note(genanki.Note(model=model, fields=[q, a, sp]))

anki_path = os.path.join(ANKI_DIR, "VERTEX_EMN_KUL2_Defisiensi_Vitamin.apkg")
genanki.Package(deck).write_to_file(anki_path)
print("Anki deck written:", anki_path)

# 2. GENERATE SPLIT-SCREEN HTML
HTML = f"""<!DOCTYPE html>
<html lang="id" data-theme="light">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Vitamin · Split-Screen Mastery EMN KUL 2</title>
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
    .course-select {{
      font-family: var(--font-sans);
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--ink);
      background: transparent;
      border: none;
      cursor: pointer;
      outline: none;
    }}
    .course-select option {{ background: var(--surface); color: var(--ink); }}

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

    /* OPENING HOOK */
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
      font-size: 2.55rem;
      font-weight: 600;
      line-height: 1.22;
      color: var(--ink);
      letter-spacing: -0.02em;
      margin-bottom: 14px;
    }}
    .hook-lead {{
      font-size: 1.06rem;
      color: var(--ink-secondary);
      max-width: 960px;
      margin-bottom: 26px;
    }}

    .enigma-row {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }}
    .enigma-card {{
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--r-md);
      padding: 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .enigma-card:hover {{
      border-color: var(--border-strong);
      transform: translateY(-2px);
      box-shadow: var(--shadow-sm);
    }}
    .enigma-tag {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--coral);
      letter-spacing: 0.05em;
      margin-bottom: 6px;
    }}
    .enigma-title {{
      font-family: var(--font-serif);
      font-size: 1.22rem;
      font-weight: 600;
      color: var(--ink);
      margin-bottom: 8px;
      line-height: 1.3;
    }}
    .enigma-desc {{
      font-size: 0.9rem;
      color: var(--ink-secondary);
      line-height: 1.55;
      margin-bottom: 14px;
    }}
    .enigma-btn {{
      align-self: flex-start;
      border: 1px solid var(--border-strong);
      background: var(--surface);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 0.79rem;
      font-weight: 700;
      padding: 6px 13px;
      border-radius: var(--r-full);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .enigma-btn:hover {{ background: var(--ink); color: var(--bg); }}
    .enigma-answer {{
      margin-top: 18px;
      padding: 18px 22px;
      background: var(--ochre-soft);
      border: 1px solid var(--ochre-border);
      border-radius: var(--r-md);
      font-size: 0.94rem;
      color: var(--ink);
      display: none;
    }}
    .enigma-answer.open {{ display: block; }}

    /* SPLIT-SCREEN: LEFT NARRATIVE + RIGHT STICKY SLIDE */
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
      font-size: 2rem;
      font-weight: 600;
      line-height: 1.24;
      color: var(--ink);
      margin-bottom: 16px;
      padding-bottom: 14px;
      border-bottom: 1px solid var(--border);
    }}
    .peer-talk {{ font-size: 1rem; color: var(--ink); margin-bottom: 18px; }}
    .peer-talk p {{ margin-bottom: 14px; }}

    .concept-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 14px;
      margin: 18px 0;
    }}
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
    .concept-box li {{ margin-bottom: 5px; }}

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
    .callout.pharma {{ background: var(--navy-soft); border: 1px solid var(--navy-border); }}
    .callout.pharma .callout-title {{ color: var(--navy); }}
    .callout.modul {{ background: var(--ochre-soft); border: 1px solid var(--ochre-border); }}
    .callout.modul .callout-title {{ color: var(--ochre); }}

    /* INLINE SIMULATOR */
    .inline-sim {{
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      border-radius: var(--r-md);
      padding: 20px 22px;
      margin: 20px 0;
    }}
    .sim-bar-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--ink);
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .sim-tabs {{
      display: flex;
      background: var(--surface);
      padding: 4px;
      border-radius: var(--r-full);
      border: 1px solid var(--border);
      gap: 4px;
      margin-bottom: 14px;
    }}
    .sim-tab {{
      flex: 1;
      border: none;
      background: transparent;
      color: var(--ink-secondary);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 8px 10px;
      border-radius: var(--r-full);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .sim-tab.active {{ background: var(--ink); color: var(--bg); }}
    .vials-3 {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
      margin-bottom: 12px;
    }}
    .vial {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-sm);
      padding: 12px 14px;
    }}
    .vial.alert {{ border-color: var(--coral); box-shadow: 0 0 0 2px var(--coral-soft); }}
    .vial-kicker {{ font-size: 0.68rem; font-weight: 700; text-transform: uppercase; color: var(--ink-muted); }}
    .vial-num {{ font-family: var(--font-mono); font-size: 1.05rem; font-weight: 700; color: var(--ink); margin: 3px 0 4px; }}
    .vial-note {{ font-size: 0.78rem; font-weight: 600; }}
    .note-bad {{ color: var(--coral); }}
    .note-ok {{ color: var(--sage); }}
    .note-warn {{ color: var(--ochre); }}

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

    /* TOOLTIPS & CLOZE */
    .med-term {{
      border-bottom: 2px dotted var(--navy);
      color: var(--navy);
      font-weight: 600;
      cursor: help;
      position: relative;
      display: inline-block;
    }}
    .med-term:hover {{ background: var(--navy-soft); border-radius: 4px; }}
    .med-tooltip {{
      visibility: hidden;
      opacity: 0;
      position: absolute;
      bottom: 130%;
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      width: 290px;
      background: #141619;
      color: #FFFFFF;
      border-radius: var(--r-md);
      padding: 13px 15px;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 400;
      line-height: 1.5;
      box-shadow: var(--shadow-lg);
      z-index: 400;
      pointer-events: none;
      transition: all 0.18s ease;
      text-align: left;
    }}
    .med-tooltip::after {{
      content: '';
      position: absolute;
      top: 100%;
      left: 50%;
      margin-left: -6px;
      border-width: 6px;
      border-style: solid;
      border-color: #141619 transparent transparent transparent;
    }}
    .med-term:hover .med-tooltip, .med-term:focus .med-tooltip {{
      visibility: visible;
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}
    .tt-kicker {{ font-size: 0.66rem; font-weight: 700; color: #7FD8B2; text-transform: uppercase; letter-spacing: 0.05em; display: block; margin-bottom: 2px; }}
    .tt-title {{ font-size: 0.9rem; font-weight: 700; color: #FFFFFF; display: block; margin-bottom: 4px; }}
    .tt-desc {{ color: #D5D8DC; display: block; }}
    .tt-pearl {{ margin-top: 7px; padding-top: 7px; border-top: 1px solid #2D3137; color: #FAD99B; font-size: 0.78rem; display: block; }}

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

    .tryout-section {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r-lg);
      padding: 36px 40px;
      margin-top: 56px;
      box-shadow: var(--shadow-md);
      scroll-margin-top: 80px;
    }}
    .tryout-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      padding-bottom: 18px;
      margin-bottom: 24px;
      border-bottom: 1px solid var(--border);
    }}
    .tryout-score {{ font-family: var(--font-mono); font-size: 1.7rem; font-weight: 700; color: var(--sage); }}

    /* Lightbox */
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
      .enigma-row {{ grid-template-columns: 1fr; }}
      .concept-grid {{ grid-template-columns: 1fr; }}
      .vials-3 {{ grid-template-columns: 1fr; }}
      .chapter-strip {{ display: none; }}
    }}
  </style>
</head>
<body>
  <div class="scroll-bar" id="scroll-bar"></div>

  <!-- TOP STICKY NAVIGATION -->
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-group">
        <span class="brand-badge">EMN · KUL 2</span>
        <select class="course-select" onchange="window.location.href=this.value">
          <option value="EMN_KUL2_Defisiensi_Vitamin.html" selected>Blok 9 EMN · KUL 2: Defisiensi Vitamin (dr. IWL)</option>
          <option value="EMN_KUL3_Defisiensi_Mineral.html">Blok 9 EMN · KUL 3: Defisiensi Mineral (dr. IWL)</option>
          <option value="EMN_KUL5_Malnutrisi.html">Blok 9 EMN · KUL 5: Malnutrisi Energi Protein (dr. DTY)</option>
          <option value="HI_KUL20_Autoimunitas.html">Blok 8 HI · KUL 20: Autoimunitas (dr. LIA)</option>
          <option value="BDT_KUL3_Patient_Safety.html">Blok 7 BDT · KUL 3: Patient Safety (dr. KI)</option>
          <option value="drive_mirror.html#/1BDgeySHpYa3PMVSDHtXytPJqA6cMN0d3">← Kembali ke Drive Mirror (Blok EMN)</option>
        </select>
      </div>

      <nav class="chapter-strip" aria-label="Lompat ke Bab">
        <a href="#bab-1" class="ch-jump active">1. Larut Lemak vs Air</a>
        <a href="#bab-2" class="ch-jump">2. Vitamin A &amp; Xerophthalmia</a>
        <a href="#bab-3" class="ch-jump">3. Vitamin D, E &amp; K</a>
        <a href="#bab-4" class="ch-jump">4. Folat (B9) vs B12 (MMA)</a>
        <a href="#bab-5" class="ch-jump">5. B1 (Beriberi), B3 (Pellagra), B6 &amp; C</a>
        <a href="#bab-6" class="ch-jump">6. Kasus Diskusi dr. Iwal</a>
        <a href="#tryout-akhir" class="ch-jump">🎯 Tryout UAB (8)</a>
      </nav>

      <div class="tool-group">
        <button type="button" id="cloze-btn" class="tool-btn" onclick="toggleCloze()" title="Shortcut tombol M">
          <span>🧠 Uji Ingatan</span>
          <span class="state-pill" id="cloze-state">OFF</span>
        </button>
        <button type="button" id="theme-btn" class="tool-btn" onclick="toggleTheme()" title="Shortcut tombol D">
          <span id="theme-label">🌙 Mode Malam</span>
        </button>
        <a href="anki/VERTEX_EMN_KUL2_Defisiensi_Vitamin.apkg" class="btn-anki" download>⬇ Anki</a>
      </div>
    </div>
  </header>

  <main class="page-wrap">

    <!-- =================================================================== -->
    <!-- PEMBUKA ("WHY"): 3 MISTERI DEFISIENSI VITAMIN                        -->
    <!-- =================================================================== -->
    <section class="hook-hero">
      <div class="hook-meta-row">
        <span class="meta-pill pill-skdi">SKDI Level 4A · Tuntas Mandiri</span>
        <span class="meta-pill pill-uab">Target 4 Soal UAB · dr. Iwal Reza Ahdi, Sp.PD</span>
        <span class="meta-pill pill-slides">28 Slide Asli + Sinergi Farmakologi dr. SAN</span>
      </div>
      <h1 class="hook-headline">Kenapa Salah Kasih Vitamin Malah Bikin Saraf Pasien Rusak Permanen?</h1>
      <p class="hook-lead">
        Banyak mahasiswa mengira vitamin itu suplemen remeh yang bebas diminum sembarangan. Di klinik penyakit dalam, salah diagnosis antara dua vitamin yang tampak mirip (Folat vs B12) bisa melumpuhkan sumsum tulang belakang pasien selamanya. Begitu juga anak dengan mata kering atau pecandu alkohol yang linglung. Coba pecahkan 3 misteri nyata ini sebelum masuk bab:
      </p>

      <div class="enigma-row">
        <div class="enigma-card">
          <div>
            <div class="enigma-tag">MISTERI KLINIS 01</div>
            <h3 class="enigma-title">Jebakan Maut Asam Folat</h3>
            <p class="enigma-desc">Pasien anemia makrositik kamu beri asam folat dosis tinggi. Darahnya membaik, tapi 2 minggu kemudian kakinya lumpuh total tak bisa jalan. Kenapa?</p>
          </div>
          <button type="button" class="enigma-btn" onclick="showMystery(1)">Buka Jawabannya ↗</button>
        </div>

        <div class="enigma-card">
          <div>
            <div class="enigma-tag">MISTERI KLINIS 02</div>
            <h3 class="enigma-title">Kutukan Bintik Busa Bitot</h3>
            <p class="enigma-desc">Balita sering menabrak pintu saat senja dan ada bercak putih mirip busa sabun di putih matanya. Bila terlambat 1 minggu, bola matanya meleleh hancur.</p>
          </div>
          <button type="button" class="enigma-btn" onclick="showMystery(2)">Buka Jawabannya ↗</button>
        </div>

        <div class="enigma-card">
          <div>
            <div class="enigma-tag">MISTERI KLINIS 03</div>
            <h3 class="enigma-title">Kalung Merah Casal</h3>
            <p class="enigma-desc">Pasien demensia dengan diare menahun memiliki ruam merah gelap melingkar di leher seperti memakai kalung tebal. Makanan apa yang menjadi pemicunya?</p>
          </div>
          <button type="button" class="enigma-btn" onclick="showMystery(3)">Buka Jawabannya ↗</button>
        </div>
      </div>

      <div id="mystery-box" class="enigma-answer"></div>
    </section>

    <!-- =================================================================== -->
    <!-- BAB 1: KLASIFIKASI LEMAK VS AIR & HOMEOSTASIS (SLIDE 1 - 7)         -->
    <!-- =================================================================== -->
    <section class="split-chapter" id="bab-1">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 01 · Slide 1 s.d. 7</span>
          <span class="meta-pill pill-skdi">Sifat Kelarutan &amp; Ekskresi</span>
        </div>
        <h2 class="ch-title">Larut Lemak (A, D, E, K) vs Larut Air (B Kompleks, C)</h2>

        <div class="peer-talk">
          <p>Di <b>Slide 4–6</b> (lihat slide asli dr. Iwal di kanan), sifat kelarutan menentukan segalanya: bagaimana vitamin diserap usus, di mana disimpan, dan seberapa cepat gejalanya muncul saat tubuh kehabisan stok:</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>1. Vitamin Larut Lemak (A, D, E, K)</h4>
            <ul>
              <li>Penyerapannya <b>wajib butuh garam empedu hati &amp; enzim lipase pankreas</b> dalam misel lemak.</li>
              <li>Disimpan lama di hati dan jaringan adiposa. Gejala defisiensi butuh waktu <b>berbulan-bulan/tahunan</b> untuk muncul.</li>
              <li>Dapat terjadi <b>{tt("Toksisitas", "Hipervitaminosis", "Keracunan vitamin akibat akumulasi berlebih di jaringan tubuh.", "Hanya terjadi pada vitamin larut lemak (terutama A dan D) karena sulit diekskresi urin.")}</b> bila konsumsi suplemen berlebih.</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>2. Vitamin Larut Air (B1–B12 &amp; C)</h4>
            <ul>
              <li>Diserap langsung lewat difusi terfasilitasi / transpor aktif usus.</li>
              <li><b>Tidak disimpan lama</b> (kelebihan langsung dibuang lewat ginjal/urin) &rarr; kecuali <b>Vitamin B12 yang disimpan di hati hingga 3–5 tahun</b>!</li>
              <li>Defisiensi muncul cepat dalam hitungan minggu saat asupan terhenti.</li>
            </ul>
          </div>
        </div>

        <div class="callout trap">
          <div class="callout-title">⚠️ Pasien Paling Rawan Defisiensi Larut Lemak (Slide 5)</div>
          Setiap penyakit yang mengganggu aliran empedu atau pencernaan lemak ({tt("Kolestasis", "Kolestasis", "Hambatan aliran empedu dari hati ke duodenum.", "Menyebabkan feses dempul pucat dan malabsorpsi vitamin A, D, E, K.")}, sirosis hepatis, kista fibrosis pankreas, atau reseksi ileum terminal) otomatis memicu <b>malabsorpsi Vitamin A, D, E, dan K sekaligus</b>!
        </div>

        <!-- Inline Quiz Bab 1 -->
        <div class="inline-quiz" id="iq-1">
          <div class="iq-kicker">🎯 Cek Paham Bab 01</div>
          <div class="iq-stem">Seorang pasien pasca-operasi reseksi ileum terminalis akibat penyakit Crohn mengeluh diare berlemak (steatorea). Di antara vitamin berikut, manakah vitamin larut air yang secara spesifik penyerapannya terganggu karena lokasi reseptor serapnya berada di ileum terminal?</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-1', 0, false, 'Tiamin (B1) diserap di jejunum proksimal.')"><span>A.</span><span>Vitamin B1 (Tiamin)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-1', 1, true, 'Tepat! Vitamin B12 berikatan dengan Faktor Intrinsik dan diserap secara spesifik di ileum terminalis (Slide 5 & 17).')"><span>B.</span><span>Vitamin B12 (Kobalamin)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-1', 2, false, 'Vitamin C diserap di usus halus bagian atas (duodenum/jejunum).')"><span>C.</span><span>Vitamin C (Asam askorbat)</span></button>
          </div>
          <div class="iq-fb" id="iq-1-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 01 · Slide Asli (1–7)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch1">
          <button class="slide-pill active" onclick="setStage('ch1', 4, 'Slide 4 · Klasifikasi Vitamin: Larut Lemak vs Larut Air', this)">Slide 4</button>
          <button class="slide-pill" onclick="setStage('ch1', 5, 'Slide 5 · Homeostasis & Penyerapan Usus', this)">Slide 5</button>
          <button class="slide-pill" onclick="setStage('ch1', 6, 'Slide 6 · 4 Mekanisme Defisiensi Vitamin', this)">Slide 6</button>
          <button class="slide-pill" onclick="setStage('ch1', 7, 'Slide 7 · Peta Organ & Vitamin Terkait', this)">Slide 7</button>
        </div>
        <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch1').src)">
          <img id="img-ch1" src="slides_kul2/slide_4.jpg" alt="Slide Bab 1">
        </div>
        <div class="stage-caption">
          <span id="cap-ch1">Slide 4 · Klasifikasi Vitamin: Larut Lemak vs Larut Air</span>
          <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
        </div>
      </aside>
    </section>

    <!-- =================================================================== -->
    <!-- BAB 2: VITAMIN A & XEROPHTHALMIA (SLIDE 8 - 11)                    -->
    <!-- =================================================================== -->
    <section class="split-chapter" id="bab-2">
      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 02 · Slide Asli (8–11)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch2">
          <button class="slide-pill active" onclick="setStage('ch2', 8, 'Slide 8 · Vitamin A: Retinol, Mata, & Epitel', this)">Slide 8</button>
          <button class="slide-pill" onclick="setStage('ch2', 9, 'Slide 9 · Tahapan Xerophthalmia Klasifikasi WHO', this)">Slide 9</button>
          <button class="slide-pill" onclick="setStage('ch2', 10, 'Slide 10 · Foto Klinis Bercak Bitot & Keratomalasia', this)">Slide 10</button>
        </div>
        <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch2').src)">
          <img id="img-ch2" src="slides_kul2/slide_8.jpg" alt="Slide Bab 2">
        </div>
        <div class="stage-caption">
          <span id="cap-ch2">Slide 8 · Vitamin A: Retinol, Mata, &amp; Epitel</span>
          <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
        </div>
      </aside>

      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 02 · Slide 8 s.d. 11</span>
          <span class="meta-pill pill-uab">Klasifikasi WHO Wajib UAB</span>
        </div>
        <h2 class="ch-title">Vitamin A: Dari Buta Senja (Nyctalopia) ke Keratomalasia</h2>

        <div class="peer-talk">
          <p>Vitamin A (Retinol/Retinal/Asam Retinoat) punya dua tugas mahapenting: membentuk pigmen fotosensitif penglihatan gelap {tt("Rhodopsin", "Rhodopsin", "Pigmen fotoreseptor di sel batang (rod cells) retina mata yang peka cahaya redup.", "Membutuhkan 11-cis-retinal; ketiadaan vitamin A memicu buta senja (nyctalopia).")} di retina dan mempertahankan diferensiasi sel epitel mukosa (mencegah metaplasia skuamosa berkeratin).</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Tahapan Xerophthalmia WHO (Slide 9–10)</h4>
            <ul>
              <li><b>1. XN (Buta Senja / {tt("Nyctalopia", "Nyctalopia (Hemeralopia / Buta Senja)", "Ketidakmampuan mata beradaptasi melihat dalam pencahayaan redup/senja hari.", "Gejala klinis paling dini defisiensi vitamin A; anak sering menabrak saat sore/malam hari.")}):</b> Gejala paling awal! Anak sering nabrak saat senja.</li>
              <li><b>2. X1A &amp; X1B:</b> Konjungtiva kering (xerosis) dan <b>{cl("Bercak Bitot (Bitot's spots)")}</b>: bercak putih keabuan berbusa di konjungtiva bulbi temporal.</li>
              <li><b>3. X2:</b> Xerosis kornea (kornea keruh kusam tak mengkilap).</li>
              <li><b>4. X3A &amp; X3B ({tt("Keratomalasia", "Keratomalasia", "Pencairan dan nekrosis stroma kornea mata akibat defisiensi vitamin A stadium terminal.", "Kornea melunak, perforasi, prolaps iris, dan memicu kebutaan permanen yang tidak bisa pulih.")}):</b> Kornea melunak mencair &rarr; kebutaan permanen!</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>Program Suplementasi Nasional (dr. SAN)</h4>
            <ul>
              <li>Kapsul Vitamin A dosis tinggi bulan Februari &amp; Agustus:</li>
              <li>• <b>Kapsul Biru (100.000 IU):</b> Bayi usia {cl("6–11 bulan")}.</li>
              <li>• <b>Kapsul Merah (200.000 IU):</b> Anak balita usia {cl("12–59 bulan")} dan ibu nifas.</li>
            </ul>
          </div>
        </div>

        <!-- Inline Quiz Bab 2 -->
        <div class="inline-quiz" id="iq-2">
          <div class="iq-kicker">🎯 Cek Paham Bab 02</div>
          <div class="iq-stem">Balita 3 tahun dibawa ibunya karena sering menabrak perabot rumah saat sore hari menjelang maghrib. Pada pemeriksaan mata didapatkan bercak segitiga putih keabuan menyerupai busa sabun pada konjungtiva bulbi temporal kedua mata. Stadium xerophthalmia menurut klasifikasi WHO pada anak ini adalah...</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-2', 0, false, 'XN adalah buta senja murni tanpa kelainan morfologi konjungtiva.')"><span>A.</span><span>XN (Night blindness)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-2', 1, true, 'Benar! Bercak Bitot (Bitot spots) yang khas berupa bercak busa putih keabuan di konjungtiva bulbi diklasifikasikan sebagai stadium X1B (Slide 9 & 10).')"><span>B.</span><span>X1B (Bitot spots)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-2', 2, false, 'X3 adalah keratomalasia / ulkus kornea berat.')"><span>C.</span><span>X3A (Keratomalacia)</span></button>
          </div>
          <div class="iq-fb" id="iq-2-fb"></div>
        </div>
      </div>
    </section>

    <!-- =================================================================== -->
    <!-- BAB 3: VITAMIN D, E, & K (SLIDE 12 - 16)                            -->
    <!-- =================================================================== -->
    <section class="split-chapter" id="bab-3">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 03 · Slide 12 s.d. 16</span>
          <span class="meta-pill pill-skdi">Tulang, Saraf, &amp; Pembekuan Darah</span>
        </div>
        <h2 class="ch-title">Vitamin D (Tulang), Vitamin E (Antioksidan), &amp; Vitamin K (Faktor II, VII, IX, X)</h2>

        <div class="peer-talk">
          <p>Tiga vitamin larut lemak berikutnya memegang peran spesifik di tulang, selubung saraf, dan pembekuan darah:</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>1. Vitamin D &amp; Tulang (Slide 12–14)</h4>
            <ul>
              <li>Bentuk aktif: <b>{tt("Kalsitriol", "1,25-dihidroksikolekalsiferol (Kalsitriol)", "Bentuk hormon aktif vitamin D yang dihidroksilasi di tubulus ginjal oleh enzim 1-alfa-hidroksilase.", "Merangsang calbindin di usus untuk menyerap kalsium dan fosfat darah.")} (1,25-(OH)2D3)</b> hasil hidroksilasi ginjal.</li>
              <li>Anak: <b>{cl("Rakitis")}</b> (lempeng pertumbuhan tulang gagal mineralisasi &rarr; kaki O/X, <i>rachitic rosary</i> di iga, <i>craniotabes</i>).</li>
              <li>Dewasa: <b>{cl("Osteomalasia")}</b> (tulang lunak, nyeri tulang difus, rawan fraktur patologis).</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>2. Vitamin E &amp; K (Slide 15–16)</h4>
            <ul>
              <li><b>Vitamin E (Tokoferol):</b> Antioksidan membran eritrosit. Kurang Vit E &rarr; {cl("anemia hemolitik")} pada bayi prematur &amp; degenerasi kolumna posterior medula spinalis (ataksia).</li>
              <li><b>Vitamin K (Filokuinon):</b> Kofaktor karboksilasi glutamat pada faktor koagulasi <b>{cl("Faktor II, VII, IX, X")}</b> serta Protein C dan S!</li>
              <li>Kurang Vit K &rarr; perdarahan tali pusat / perdarahan intrakranial pada bayi baru lahir (<b>HDN / APBD</b>). Injeksi <b>Vitamin K1 fitomenadion 1 mg IM</b> wajib pada semua bayi baru lahir!</li>
            </ul>
          </div>
        </div>

        <!-- Inline Quiz Bab 3 -->
        <div class="inline-quiz" id="iq-3">
          <div class="iq-kicker">🎯 Cek Paham Bab 03</div>
          <div class="iq-stem">Bayi usia 3 hari dibawa ke IGD dengan perdarahan masif dari tali pusat dan memar multipel di kulit. Bayi lahir di dukun beranak dan tidak mendapatkan suntikan profilaksis setelah lahir. Pemeriksaan koagulasi menunjukkan pemanjangan masa protrombin (PT). Defisiensi vitamin apakah yang mendasari kondisi ini?</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-3', 0, false, 'Defisiensi vitamin C memicu perdarahan kapiler perifolikular pada orang dewasa, bukan kelainan masa protrombin bayi baru lahir.')"><span>A.</span><span>Vitamin C</span></button>
            <button class="iq-btn" onclick="ansInline('iq-3', 1, true, 'Benar! Vitamin K mutlak diperlukan untuk sintesis faktor pembekuan II, VII, IX, dan X di hati. Tanpa profilaksis Vit K1, bayi rentan mengalami Hemorrhagic Disease of the Newborn (Slide 16).')"><span>B.</span><span>Vitamin K</span></button>
            <button class="iq-btn" onclick="ansInline('iq-3', 2, false, 'Defisiensi vitamin E menyebabkan anemia hemolitik, bukan pemanjangan PT.')"><span>C.</span><span>Vitamin E</span></button>
          </div>
          <div class="iq-fb" id="iq-3-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 03 · Slide Asli (12–16)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch3">
          <button class="slide-pill active" onclick="setStage('ch3', 12, 'Slide 12 · Vitamin D: Metabolisme & Mineralisasi Tulang', this)">Slide 12</button>
          <button class="slide-pill" onclick="setStage('ch3', 15, 'Slide 15 · Vitamin E: Antioksidan & Anemia Hemolitik', this)">Slide 15</button>
          <button class="slide-pill" onclick="setStage('ch3', 16, 'Slide 16 · Vitamin K: Koagulasi II, VII, IX, X & HDN', this)">Slide 16</button>
        </div>
        <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch3').src)">
          <img id="img-ch3" src="slides_kul2/slide_12.jpg" alt="Slide Bab 3">
        </div>
        <div class="stage-caption">
          <span id="cap-ch3">Slide 12 · Vitamin D: Metabolisme &amp; Mineralisasi Tulang</span>
          <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
        </div>
      </aside>
    </section>

    <!-- =================================================================== -->
    <!-- BAB 4: FOLAT (B9) VS B12 (MMA & BAHAYA FOLATE TRAP) (SLIDE 17)      -->
    <!-- =================================================================== -->
    <section class="split-chapter" id="bab-4">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 04 · Slide 17</span>
          <span class="meta-pill pill-uab">Slide Emas UAB dr. Iwal</span>
        </div>
        <h2 class="ch-title">Folat (B9) vs Kobalamin (B12): Pembeda MMA &amp; Bahaya Folate Trap</h2>

        <div class="peer-talk">
          <p>Ini adalah <b>Slide paling penting di seluruh kuliah Vitamin</b> (lihat <b>Slide 17</b> di kanan). Pasien defisiensi Folat dan B12 sama-sama datang dengan <b>Anemia Megaloblastik</b> (eritrosit bengkak besar MCV &gt;100 fL dan neutropenia dengan hipersegmentasi &ge;5 lobus). Kalau kamu salah membedakan keduanya, akibatnya fatal!</p>
        </div>

        <!-- Embedded Interactive Simulator: MMA & Homocysteine Vials -->
        <div class="inline-sim">
          <div class="sim-bar-title">
            <span>⚡ Simulator Pembeda Laboratorium Folat (B9) vs B12 (Slide 17)</span>
          </div>
          <div class="sim-tabs">
            <button type="button" class="sim-tab active" onclick="simB12(false, this)">Defisiensi Folat (B9)</button>
            <button type="button" class="sim-tab" onclick="simB12(true, this)">Defisiensi Kobalamin (B12)</button>
          </div>
          <div class="vials-3">
            <div class="vial" id="vb-homo">
              <div class="vial-kicker">Homosistein Darah</div>
              <div class="vial-num" id="vn-homo" style="color:var(--coral);">MENINGKAT</div>
              <div class="vial-note note-bad" id="vt-homo">Naik pada B9 &amp; B12!</div>
            </div>
            <div class="vial" id="vb-mma">
              <div class="vial-kicker">Asam Metilmalonat (MMA)</div>
              <div class="vial-num" id="vn-mma" style="color:var(--sage);">NORMAL</div>
              <div class="vial-note note-ok" id="vt-mma">Hanya Folat yang Normal!</div>
            </div>
            <div class="vial" id="vb-neuro">
              <div class="vial-kicker">Kerusakan Saraf (Mielopati)</div>
              <div class="vial-num" id="vn-neuro" style="color:var(--sage);">TIDAK ADA</div>
              <div class="vial-note note-ok" id="vt-neuro">Hanya Anemia Murni</div>
            </div>
          </div>
          <div id="sim-b12-note" style="font-size:0.88rem;color:var(--ink-secondary);">
            💡 <b>Rasional Biokimia:</b> Vitamin B12 adalah kofaktor enzim <i>metilmalonil-CoA mutase</i>. Tanpa B12, asam metilmalonat tidak bisa diubah dan menumpuk di darah/urin (<b>MMA meningkat spesifik</b>), merusak selubung mielin saraf! Pada defisiensi Folat murni, MMA tetap <b>NORMAL</b> dan tidak ada gejala saraf.
          </div>
        </div>

        <div class="callout trap">
          <div class="callout-title">⚠️ Bahaya Maut: The Folate Trap (Slide 17)</div>
          Kalau pasien defisiensi B12 kamu kasih suplemen <b>Asam Folat dosis tinggi</b>, anemia di darahnya memang membaik (seolah sembuh semu). Tapi <b>kerusakan sumsum tulang belakangnya (Subacute Combined Degeneration) akan terus menggerogoti saraf</b> tanpa terdeteksi sampai pasien lumpuh permanen! <b>Wajib cek kadar B12 sebelum memberi terapi asam folat!</b>
        </div>

        <!-- Inline Quiz Bab 4 -->
        <div class="iq-quiz" id="iq-4">
          <div class="iq-kicker">🎯 Cek Paham Bab 04 (Slide 17)</div>
          <div class="iq-stem">Laki-laki 55 tahun pasca-gastrektomi total mengeluh kesemutan pada kedua kaki dan tangan serta cara berjalan goyah (ataksia). Darah rutin menunjukkan Hb 8,5 g/dL dan MCV 108 fL. Pemeriksaan laboratorium manakah yang paling spesifik meningkat untuk memastikan bahwa anemia megaloblastik pasien ini disebabkan oleh defisiensi B12 dan bukan defisiensi folat?</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-4', 0, false, 'Homosistein meningkat pada KEDUANYA (defisiensi folat maupun defisiensi B12).')"><span>A.</span><span>Kadar Homosistein plasma</span></button>
            <button class="iq-btn" onclick="ansInline('iq-4', 1, true, 'Tepat! Asam Metilmalonat (MMA) hanya meningkat spesifik pada defisiensi vitamin B12 karena konversi methylmalonyl-CoA mutase membutuhkan B12 (Slide 17).')"><span>B.</span><span>Kadar Asam Metilmalonat (MMA) serum/urin</span></button>
            <button class="iq-btn" onclick="ansInline('iq-4', 2, false, 'Ferritin adalah penanda cadangan besi pada anemia mikrositik, bukan pembeda megaloblastik.')"><span>C.</span><span>Ferritin serum</span></button>
          </div>
          <div class="iq-fb" id="iq-4-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 04 · Slide Asli (17)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch4">
          <button class="slide-pill active" onclick="setStage('ch4', 17, 'Slide 17 · Tabel Pembeda Defisiensi Folat (B9) vs B12 (dr. Iwal)', this)">Slide 17</button>
        </div>
        <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch4').src)">
          <img id="img-ch4" src="slides_kul2/slide_17.jpg" alt="Slide Bab 4">
        </div>
        <div class="stage-caption">
          <span id="cap-ch4">Slide 17 · Tabel Pembeda Defisiensi Folat (B9) vs B12 (dr. Iwal)</span>
          <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
        </div>
      </aside>
    </section>

    <!-- =================================================================== -->
    <!-- BAB 5: B1 (BERIBERI), B3 (PELLAGRA), B6, & C (SLIDE 18 - 21)        -->
    <!-- =================================================================== -->
    <section class="split-chapter" id="bab-5">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 05 · Slide 18 s.d. 21</span>
          <span class="meta-pill pill-uab">Sindrom Khas Defisiensi B1–B6 &amp; C</span>
        </div>
        <h2 class="ch-title">B1 (Beriberi), B3 (Pellagra 4D), B6 (Efek Samping INH), &amp; Vitamin C (Scurvy)</h2>

        <div class="peer-talk">
          <p>Empat vitamin larut air ini punya sindrom klinis klasik yang gamblang banget di lembar soal UAB:</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>1. B1 (Tiamin) &amp; B3 (Niasin) (Slide 18–20)</h4>
            <ul>
              <li><b>Vitamin B1:</b> Kofaktor dehidrogenase piruvat.
                <br>• <i>Beriberi Basah:</i> Gagal jantung dilatasi berdebar + edema tungkai masif.
                <br>• <i>Beriberi Kering:</i> Neuropati perifer murni.
                <br>• <i>Wernicke-Korsakoff:</i> Trias ataksia, oftalmoplegia (mata juling/nistagmus), dan konfabulasi ingatan pada peminum alkohol.
              </li>
              <li><b>Vitamin B3 (Pellagra):</b> Tetrad <b>{cl("4D: Dermatitis fotosensitif simetris (Casal necklace) + Diare + Demensia + Death")}</b>. Sering pada diet monoton jagung miskin triptofan!</li>
            </ul>
          </div>
          <div class="concept-box">
            <h4>2. B6 (Piridoksin) &amp; Vitamin C (Slide 20–21)</h4>
            <ul>
              <li><b>Vitamin B6 &amp; Obat TB (INH):</b> Obat anti-TB <b>Isoniazid (INH)</b> mematikan fungsi B6 &rarr; memicu kesemutan neuropati perifer. <b>{cl("Wajib resepkan Vitamin B6 10–25 mg/hari")}</b> bersamaan dengan terapi OAT TB!</li>
              <li><b>Vitamin C (Scurvy):</b> Kofaktor hidroksilasi kolagen. Defisiensi &rarr; pembuluh kapiler rapuh &rarr; <b>gusi berdarah bengkak</b>, perdarahan perifolikular, dan rambut melingkar <b>{cl("corkscrew hair")}</b>.</li>
            </ul>
          </div>
        </div>

        <!-- Inline Quiz Bab 5 -->
        <div class="inline-quiz" id="iq-5">
          <div class="iq-kicker">🎯 Cek Paham Bab 05</div>
          <div class="iq-stem">Pasien laki-laki 42 tahun penderita tuberkulosis paru yang sedang menjalani terapi obat anti-tuberkulosis (OAT) kategori 1 mengeluh rasa kesemutan dan baal seperti terbakar pada kedua telapak kakinya sejak 3 minggu. Obat OAT manakah yang memicu efek samping ini dan suplementasi vitamin apa yang wajib diberikan?</div>
          <div class="iq-opts">
            <button class="iq-btn" onclick="ansInline('iq-5', 0, false, 'Rifampisin menyebabkan urin berwarna kemerahan, bukan neuropati perifer.')"><span>A.</span><span>Rifampisin; suplementasi Vitamin B1</span></button>
            <button class="iq-btn" onclick="ansInline('iq-5', 1, true, 'Benar! Isoniazid (INH) memicu defisiensi piridoksal fosfat (Vitamin B6) sehingga menyebabkan neuropati perifer; wajib dicegah dengan suplementasi Vitamin B6 (Slide 20).')"><span>B.</span><span>Isoniazid (INH); suplementasi Vitamin B6 (Piridoksin)</span></button>
            <button class="iq-btn" onclick="ansInline('iq-5', 2, false, 'Etambutol memicu neuritis retrobulbar gangguan penglihatan warna.')"><span>C.</span><span>Etambutol; suplementasi Vitamin A</span></button>
          </div>
          <div class="iq-fb" id="iq-5-fb"></div>
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 05 · Slide Asli (18–21)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch5">
          <button class="slide-pill active" onclick="setStage('ch5', 18, 'Slide 18 · Vitamin B1: Beriberi Basah vs Kering', this)">Slide 18</button>
          <button class="slide-pill" onclick="setStage('ch5', 20, 'Slide 20 · Vitamin B3 (Pellagra 4D) & B6 (INH)', this)">Slide 20</button>
          <button class="slide-pill" onclick="setStage('ch5', 21, 'Slide 21 · Vitamin C: Kolagen & Gejala Scurvy', this)">Slide 21</button>
        </div>
        <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch5').src)">
          <img id="img-ch5" src="slides_kul2/slide_18.jpg" alt="Slide Bab 5">
        </div>
        <div class="stage-caption">
          <span id="cap-ch5">Slide 18 · Vitamin B1: Beriberi Basah vs Kering</span>
          <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
        </div>
      </aside>
    </section>

    <!-- =================================================================== -->
    <!-- BAB 6: BEDAH 3 KASUS DISKUSI ASLI DR. IWAL (SLIDE 22 - 28)          -->
    <!-- =================================================================== -->
    <section class="split-chapter" id="bab-6">
      <div class="narrative-panel">
        <div class="ch-kicker-row">
          <span class="ch-kicker">Bab 06 · Slide 22 s.d. 28</span>
          <span class="meta-pill pill-uab">Bedah Kasus Diskusi dr. Iwal</span>
        </div>
        <h2 class="ch-title">Bedah Tuntas 3 Kasus Asli Slide Diskusi dr. Iwal</h2>

        <div class="peer-talk">
          <p>Tiga kasus klinis di <b>Slide 24, 25, dan 26</b> adalah kasus diskusi resmi yang dibuat dr. Iwal. Pahami rasional pemecahannya karena soal UAB adalah modifikasi langsung dari kasus ini:</p>
        </div>

        <div class="concept-grid">
          <div class="concept-box">
            <h4>Kasus 1: Anemia Megaloblastik &amp; Neuropati (Slide 24)</h4>
            <p>Pasien lansia vegetarian ketat dengan lemas, Hb 7,8 g/dL, MCV 112 fL, dan kesemutan kedua tungkai. <b>Diagnosis:</b> Defisiensi B12. MMA meningkat spesifik. Terapi dengan injeksi sianokobalamin/hidroksokobalamin IM.</p>
          </div>
          <div class="concept-box">
            <h4>Kasus 2: Ruam Melingkar Leher &amp; Diare (Slide 25)</h4>
            <p>Pasien alkoholisme kronis dengan ruam merah bersisik di leher (<i>Casal necklace</i>), diare berulang, dan mudah lupa. <b>Diagnosis:</b> Pellagra akibat defisiensi Niasin (B3). Diberi suplementasi nikotinamid oral.</p>
          </div>
        </div>

        <div class="callout modul">
          <div class="callout-title">Kasus 3: Sesak Napas &amp; Jantung Berdebar pada Peminum Alkohol (Slide 26)</div>
          Laki-laki 38 tahun pecandu alkohol mengeluh sesak napas saat berbaring, bengkak kedua tungkai, kardiomegali pada rontgen dada, dan murmur fungsional. <b>Diagnosis:</b> Wet Beriberi (gagal jantung output tinggi) akibat defisiensi Vitamin B1 (Tiamin). Terapi segera: injeksi Tiamin IV lambat!
        </div>
      </div>

      <aside class="slide-stage">
        <div class="stage-top">
          <span class="stage-label">Bab 06 · Slide Asli (22–28)</span>
          <span style="font-size:0.75rem;color:var(--ink-muted);">Klik gambar untuk Zoom</span>
        </div>
        <div class="slide-pills" id="pills-ch6">
          <button class="slide-pill active" onclick="setStage('ch6', 24, 'Slide 24 · Kasus Diskusi 1 Megaloblastik', this)">Kasus 1</button>
          <button class="slide-pill" onclick="setStage('ch6', 25, 'Slide 25 · Kasus Diskusi 2 Pellagra', this)">Kasus 2</button>
          <button class="slide-pill" onclick="setStage('ch6', 26, 'Slide 26 · Kasus Diskusi 3 Beriberi', this)">Kasus 3</button>
          <button class="slide-pill" onclick="setStage('ch6', 28, 'Slide 28 · Rangkuman & Take Home Message', this)">Slide 28</button>
        </div>
        <div class="stage-frame" onclick="openZoom(document.getElementById('img-ch6').src)">
          <img id="img-ch6" src="slides_kul2/slide_24.jpg" alt="Slide Bab 6">
        </div>
        <div class="stage-caption">
          <span id="cap-ch6">Slide 24 · Kasus Diskusi 1 Megaloblastik</span>
          <span style="color:var(--navy);font-weight:700;">Perbesar ↗</span>
        </div>
      </aside>
    </section>

    <!-- =================================================================== -->
    <!-- TRYOUT AKHIR: 8 SOAL PREDIKSI UAB DEFISIENSI VITAMIN                -->
    <!-- =================================================================== -->
    <section class="tryout-section" id="tryout-akhir">
      <div class="tryout-head">
        <div>
          <span class="ch-kicker">Evaluasi Akhir · UAB Prediction</span>
          <h2 style="font-family:var(--font-serif);font-size:2.1rem;color:var(--ink);margin-top:4px;">Tryout 8 Soal UAB Defisiensi Vitamin (dr. Iwal)</h2>
          <p style="font-size:0.94rem;color:var(--ink-secondary);">Seluruh soal disusun mengikuti karakter penalaran klinis dr. Iwal dan arsip ujian EMN.</p>
        </div>
        <div style="text-align:right;">
          <span style="font-size:0.76rem;font-weight:700;color:var(--ink-muted);text-transform:uppercase;">Skor UAB Anda:</span>
          <div class="tryout-score"><span id="tryout-score-val">0</span> / 8</div>
        </div>
      </div>

      <div id="tryout-list"></div>
    </section>

  </main>

  <!-- LIGHTBOX MODAL ZOOM -->
  <div id="lightbox" class="lightbox" onclick="closeZoom()">
    <img id="lightbox-img" src="" alt="Slide Zoom" onclick="event.stopPropagation()">
  </div>

  <script>
    const MYSTERIES = {{
      1: "<b>Jawabannya: The Folate Trap (Slide 17).</b> Memberi asam folat pada pasien yang sebenarnya kekurangan B12 akan menutupi anemia megaloblastiknya (seolah-olah sembuh semu). Namun kerusakan selubung saraf mielin di sumsum tulang belakang (<i>Subacute Combined Degeneration</i>) akan terus berjalan tanpa hambatan sampai pasien lumpuh permanen!",
      2: "<b>Jawabannya: Xerophthalmia & Keratomalasia (Slide 8–10).</b> Bintik busa itu adalah <b>Bercak Bitot (Bitot\\'s spots)</b> pada defisiensi Vitamin A stadium X1B. Bila tidak segera diberi kapsul vitamin A dosis tinggi, kornea akan melunak dan mencair (Keratomalasia X3B) yang memicu kebutaan permanen seumur hidup.",
      3: "<b>Jawabannya: Pellagra akibat Defisiensi Niasin / Vitamin B3 (Slide 20).</b> Ruam merah gelap melingkar di leher disebut <b>Casal necklace</b> (Dermatitis fotosensitif). Penyakit ini bermanifestasi sebagai tetrad 4D (Dermatitis, Diare, Demensia, Death) akibat diet monoton jagung yang rendah triptofan."
    }};
    function showMystery(n) {{
      const box = document.getElementById('mystery-box');
      box.innerHTML = MYSTERIES[n];
      box.classList.add('open');
    }}

    function setStage(chId, slideNum, caption, btn) {{
      document.getElementById('img-' + chId).src = 'slides_kul2/slide_' + slideNum + '.jpg';
      document.getElementById('cap-' + chId).textContent = caption;
      const wrap = document.getElementById('pills-' + chId);
      wrap.querySelectorAll('.slide-pill').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    }}

    function simB12(isB12, btn) {{
      btn.parentElement.querySelectorAll('.sim-tab').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const vM = document.getElementById('vn-mma');
      const tM = document.getElementById('vt-mma');
      const vN = document.getElementById('vn-neuro');
      const tN = document.getElementById('vt-neuro');
      const note = document.getElementById('sim-b12-note');
      if (isB12) {{
        vM.textContent = 'MENINGKAT TAJAM';
        vM.style.color = 'var(--coral)';
        tM.textContent = 'Spesifik B12!';
        tM.className = 'vial-note note-bad';
        vN.textContent = 'ADA (Mielopati)';
        vN.style.color = 'var(--coral)';
        tN.textContent = 'Kaki baal & jalan goyah';
        tN.className = 'vial-note note-bad';
        note.innerHTML = '💡 <b>Defisiensi Vitamin B12:</b> MMA naik spesifik dan ada gangguan saraf mielopati (karena konversi methylmalonyl-CoA butuh B12). Homosistein juga ikut naik.';
      }} else {{
        vM.textContent = 'NORMAL';
        vM.style.color = 'var(--sage)';
        tM.textContent = 'Hanya Folat yang Normal';
        tM.className = 'vial-note note-ok';
        vN.textContent = 'TIDAK ADA';
        vN.style.color = 'var(--sage)';
        tN.textContent = 'Hanya Anemia Murni';
        tN.className = 'vial-note note-ok';
        note.innerHTML = '💡 <b>Defisiensi Asam Folat (B9):</b> MMA tetap NORMAL dan TIDAK ADA gejala neurologis. Homosistein tetap meningkat.';
      }}
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
      try {{ localStorage.setItem('vx_emn_theme', next); }} catch(e) {{}}
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

    const TRYOUT_Q = [
      {{
        stem: '1. Seorang perempuan 48 tahun datang dengan keluhan badan lemas dan lidah terasa perih kemerahan (glossitis). Pemeriksaan darah menunjukkan Hb 8,2 g/dL, MCV 114 fL (makrositik), dan pada apusan darah tepi ditemukan neutrofil hipersegmentasi (>5 lobus). Pasien tidak memiliki keluhan kesemutan maupun gangguan keseimbangan berjalan. Pemeriksaan laboratorium manakah yang paling akurat untuk mengonfirmasi bahwa pasien menderita defisiensi Folat murni dan bukan defisiensi B12?',
        opts: ['Kadar Homosistein plasma meningkat', 'Kadar Asam Metilmalonat (MMA) serum normal', 'Kadar Ferritin serum menurun', 'Peningkatan saturasi transferrin', 'Kadar asam retinoat serum meningkat'],
        ans: 1,
        exp: 'Pada defisiensi folat murni, kadar <b>Asam Metilmalonat (MMA) tetap NORMAL</b>, sedangkan pada defisiensi B12 MMA akan meningkat tajam (Slide 17).'
      }},
      {{
        stem: '2. Mengapa pemberian terapi Asam Folat dosis tinggi tanpa suplementasi Vitamin B12 dilarang keras (The Folate Trap) pada pasien dengan anemia pernisiosa menurut Slide 17?',
        opts: ['Asam folat memicu krisis hemolitik intravaskular akut', 'Asam folat memperbaiki gambaran anemia darah namun membiarkan degenerasi mielin saraf medula spinalis memburuk secara ireversibel', 'Asam folat memblokir sintesis DNA di sumsum tulang', 'Asam folat mengendap di glomerulus ginjal', 'Asam folat memicu hiperkalsiuria berat'],
        ans: 1,
        exp: 'Folate trap mengoreksi hematologi anemia tetapi <b>membiarkan kerusakan saraf (Subacute Combined Degeneration) memburuk hingga lumpuh permanen</b> (Slide 17).'
      }},
      {{
        stem: '3. Anak balita 2 tahun dibawa ke puskesmas dengan riwayat sering menabrak benda saat sore hari. Pada pemeriksaan mata tampak bercak busa putih keabuan berbentuk segitiga pada konjungtiva bulbi temporal. Kapsul vitamin A dosis tinggi apakah yang wajib diberikan sebagai dosis tatalaksana pada anak usia ini?',
        opts: ['Kapsul Biru (100.000 IU)', 'Kapsul Merah (200.000 IU)', 'Kapsul Kuning (50.000 IU)', 'Kapsul Hijau (20.000 IU)', 'Kapsul Putih (10.000 IU)'],
        ans: 1,
        exp: 'Untuk balita usia 12–59 bulan, kapsul vitamin A dosis tinggi yang diberikan adalah <b>Kapsul Merah (200.000 IU)</b> (Slide 10).'
      }},
      {{
        stem: '4. Pasien alkoholik kronis datang dengan kelemahan ekstremitas bawah, kardiomegali, edema kedua tungkai, dan sesak napas saat berbaring (high-output heart failure). Diagnosis klinis yang paling tepat menurut Slide 18 adalah...',
        opts: ['Dry Beriberi (defisiensi Vitamin B1)', 'Wet Beriberi (defisiensi Vitamin B1)', 'Pellagra (defisiensi Vitamin B3)', 'Scurvy (defisiensi Vitamin C)', 'Rakitis (defisiensi Vitamin D)'],
        ans: 1,
        exp: 'Keterlibatan kardiovaskular berupa gagal jantung dan edema tungkai akibat defisiensi vitamin B1 disebut <b>Wet Beriberi</b> (Slide 18).'
      }},
      {{
        stem: '5. Pasien dengan riwayat konsumsi jagung sebagai makanan pokok tunggal datang dengan ruam kulit eritematosa bersisik kehitaman yang simetris di leher menyerupai kalung (Casal necklace), disertai diare kronik dan gangguan daya ingat (demensia). Defisiensi vitamin apakah yang mendasari tetrad gejala Pellagra ini?',
        opts: ['Vitamin B1 (Tiamin)', 'Vitamin B2 (Riboflavin)', 'Vitamin B3 (Niasin)', 'Vitamin B6 (Piridoksin)', 'Vitamin B12 (Kobalamin)'],
        ans: 2,
        exp: 'Pellagra dengan tetrad 4D (Dermatitis, Diare, Demensia, Death) disebabkan oleh <b>defisiensi Vitamin B3 (Niasin)</b> (Slide 20).'
      }},
      {{
        stem: '6. Pasien TB paru yang menjalani terapi Isoniazid (INH) mengeluh kesemutan dan rasa baal pada kedua telapak kaki. Mekanisme farmakologis INH yang memicu neuropati perifer ini adalah inhibisi terhadap metabolisme vitamin...',
        opts: ['Vitamin B1 (Tiamin)', 'Vitamin B6 (Piridoksin)', 'Vitamin B12 (Kobalamin)', 'Vitamin C (Asam askorbat)', 'Vitamin E (Tokoferol)'],
        ans: 1,
        exp: 'INH menghambat piridoksin kinase dan membentuk kompleks inaktif dengan <b>Vitamin B6 (Piridoksin)</b>; wajib dicegah dengan suplementasi Vitamin B6 10–25 mg/hari (Slide 20).'
      }},
      {{
        stem: '7. Pelaut yang tidak mengonsumsi buah segar selama 4 bulan mengalami perdarahan gusi masif, pembengkakan sendi, bintik perdarahan perifolikular di kulit, dan luka sayatan yang tidak kunjung menutup. Mekanisme biokimiawi apakah yang terganggu pada penyakit Scurvy ini? (Slide 21)',
        opts: ['Kegagalan sintesis faktor koagulasi di hati', 'Gangguan hidroksilasi prolin dan lisin pada rantai tripel heliks kolagen', 'Penurunan pembentukan trombosit di sumsum tulang', 'Kegagalan mineralisasi kalsium pada matriks osteoid', 'Penghambatan enzim deiodinase perifer'],
        ans: 1,
        exp: 'Vitamin C adalah kofaktor enzim prolyl & lysyl hydroxylase; defisiensinya melumpuhkan <b>hidroksilasi kolagen</b> sehingga dinding kapiler menjadi sangat rapuh (Slide 21).'
      }},
      {{
        stem: '8. Bayi baru lahir dari ibu yang melahirkan di rumah tanpa bantuan tenaga medis mengalami perdarahan tali pusat dan hematoma subgaleal di kepala pada hari ke-3 kehidupan. Defisiensi vitamin manakah yang memicu gangguan pembentukan faktor koagulasi II, VII, IX, dan X pada bayi ini?',
        opts: ['Vitamin A', 'Vitamin D', 'Vitamin E', 'Vitamin K', 'Vitamin C'],
        ans: 3,
        exp: 'Hemorrhagic Disease of the Newborn (HDN) terjadi akibat <b>defisiensi Vitamin K</b> yang esensial untuk sintesis faktor koagulasi II, VII, IX, dan X di hati (Slide 16).'
      }}
    ];

    let tryoutAns = {{}};
    let tryoutScore = 0;

    function initTryout() {{
      const host = document.getElementById('tryout-list');
      host.innerHTML = TRYOUT_Q.map((q, qi) => `
        <div class="inline-quiz" id="tq-${{qi}}" style="border-top:1px solid var(--border);margin-top:18px;padding-top:18px;">
          <div class="iq-stem">${{q.stem}}</div>
          <div class="iq-opts">
            ${{q.opts.map((o, oi) => `
              <button type="button" class="iq-btn" onclick="ansTryout(${{qi}}, ${{oi}})">
                <span>${{String.fromCharCode(65 + oi)}}.</span>
                <span>${{o}}</span>
              </button>
            `).join('')}}
          </div>
          <div class="iq-fb" id="tq-fb-${{qi}}"></div>
        </div>
      `).join('');
    }}

    function ansTryout(qi, oi) {{
      if (tryoutAns[qi] !== undefined) return;
      tryoutAns[qi] = oi;
      const q = TRYOUT_Q[qi];
      const ok = (oi === q.ans);
      const wrap = document.getElementById('tq-' + qi);
      wrap.querySelectorAll('.iq-btn').forEach((b, i) => {{
        if (i === q.ans) b.classList.add('is-correct');
        else if (i === oi && !ok) b.classList.add('is-wrong');
      }});
      const fb = document.getElementById('tq-fb-' + qi);
      if (ok) {{
        tryoutScore++;
        fb.className = 'iq-fb show ok';
        fb.innerHTML = `<strong>✅ Benar!</strong> ${{q.exp}}`;
      }} else {{
        fb.className = 'iq-fb show no';
        fb.innerHTML = `<strong>❌ Kurang Tepat.</strong> Jawaban benar: <strong>${{String.fromCharCode(65 + q.ans)}} (${{q.opts[q.ans]}})</strong>.<br>${{q.exp}}`;
      }}
      document.getElementById('tryout-score-val').textContent = tryoutScore;
    }}

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
      initTryout();
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

      const chapters = [...document.querySelectorAll('.split-chapter, #tryout-akhir')];
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
        const saved = localStorage.getItem('vx_emn_theme');
        if (saved === 'dark') toggleTheme();
      }} catch(e) {{}}
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(HTML)
print(f"EMN KUL 2 Defisiensi Vitamin berhasil dibuat di {OUT_HTML} ({len(HTML)} bytes)")

# 3. REGISTER IN SUMMARIES.JSON
try:
    sdata = json.load(open(SUMMARIES_FILE, encoding="utf-8"))
except Exception:
    sdata = {}
sdata["1-JrPD7PhKNVTGua72nDXVcVbDcrcSV0W"] = {
    "title": "EMN KUL 2 — Defisiensi Vitamin",
    "url": "EMN_KUL2_Defisiensi_Vitamin.html",
}
with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
    json.dump(sdata, f, ensure_ascii=False, indent=2)
print("Registered 1-JrPD7PhKNVTGua72nDXVcVbDcrcSV0W in summaries.json!")
