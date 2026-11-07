#!/usr/bin/env python3
"""Build Peer-Taught, Casual, High-Yield Preclinical Guide for EMN KUL 3 Defisiensi Mineral.
Key Features:
1. Casual, smart peer-to-peer Indonesian medical tone ("bayangin kamu lagi jaga IGD...", "nah triknya gini...", "dosen sering ngejebak di sini...").
2. AMBOSS-style Smart Medical Tooltips on ALL medical jargon (distinct dotted underline + hover popover definition).
3. Active Cloze Masking (Restored! Button '🧠 Uji Ingatan' / Hotkey M hides numbers & terms with clickable unblur).
4. The 3 Mystery Enigmas, 60-Second Simulators, 8-Mineral Explorer, and Bug-Free UAB CBT Suite.
"""
import os

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

# Helper for Smart Medical Tooltip
def tt(term, title, desc, pearl):
    return f"""<span class="med-term" tabindex="0">{term}<span class="med-tooltip"><span class="tt-kicker">Kamus Klinis</span><span class="tt-title">{title}</span><span class="tt-desc">{desc}</span><span class="tt-pearl">💡 {pearl}</span></span></span>"""

# Helper for Cloze Masking
def cl(text):
    return f"""<span class="cloze-mask" onclick="this.classList.toggle('revealed')" title="Klik untuk membuka rahasia">{text}</span>"""

PEER_HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Mineral · Teman Belajar UAB EMN</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #FAF9F6;
      --surface: #FFFFFF;
      --surface-subtle: #F3F0EA;
      --surface-active: #EAE6DF;
      
      --border: #E6E2D8;
      --border-dark: #C9C4B7;
      
      --ink: #141517;
      --ink-secondary: #4A4D53;
      --ink-muted: #7E8189;
      
      --sage: #1E6B47;
      --sage-light: #EBF5F0;
      --sage-border: #BCDCCB;
      
      --terracotta: #B93822;
      --terracotta-light: #FBEFEA;
      --terracotta-border: #F3C9BF;
      
      --ochre: #B06914;
      --ochre-light: #FDF4E7;
      --ochre-border: #F6DAB3;
      
      --navy: #1B3B6F;
      --navy-light: #EDF3FA;
      
      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;
      
      --font-sans: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-serif: 'Newsreader', Georgia, serif;
      --font-mono: 'JetBrains Mono', monospace;
      
      --shadow-ambient: 0 4px 20px -2px rgba(20, 21, 23, 0.05);
      --shadow-float: 0 20px 48px -8px rgba(20, 21, 23, 0.12);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}

    body {{
      background-color: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 120px;
    }}

    ::selection {{ background: #D2E8DB; color: #141517; }}

    /* Sticky Clean Topbar */
    .app-header {{
      position: sticky;
      top: 0;
      z-index: 200;
      background: rgba(250, 249, 246, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
      transition: all 0.2s ease;
    }}
    .header-content {{
      max-width: 1100px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .brand-mark {{
      display: flex;
      align-items: center;
      gap: 12px;
      flex: none;
    }}
    .brand-tag {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      color: #FFFFFF;
      background: var(--navy);
      padding: 3px 8px;
      border-radius: var(--radius-sm);
      white-space: nowrap;
    }}
    .brand-context {{
      display: flex;
      flex-direction: column;
      white-space: nowrap;
    }}
    .brand-context-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink);
      line-height: 1.2;
    }}
    .brand-context-sub {{
      font-size: 0.78rem;
      color: var(--ink-muted);
    }}

    .view-pills {{
      display: flex;
      background: var(--surface-subtle);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 2px;
    }}
    .view-pill {{
      border: none;
      background: transparent;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--ink-secondary);
      padding: 7px 15px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
      white-space: nowrap;
    }}
    .view-pill:hover {{ color: var(--ink); }}
    .view-pill.active {{
      background: var(--surface);
      color: var(--ink);
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    /* Active Cloze Mode Toggle Button */
    .btn-cloze-toggle {{
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--ink-secondary);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
    }}
    .btn-cloze-toggle:hover {{
      border-color: var(--sage);
      color: var(--ink);
    }}
    .btn-cloze-toggle.active {{
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
      box-shadow: 0 4px 12px rgba(20, 21, 23, 0.2);
    }}
    .cloze-badge-pill {{
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 1px 6px;
      border-radius: 4px;
      background: var(--bg);
      color: var(--ink);
    }}
    .btn-cloze-toggle.active .cloze-badge-pill {{
      background: var(--sage);
      color: #FFFFFF;
    }}

    .btn-anki {{
      background: var(--sage);
      color: #FFFFFF !important;
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 7px 16px;
      border-radius: var(--radius-full);
      text-decoration: none;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-anki:hover {{
      background: #154D33;
      transform: translateY(-1px);
    }}

    /* Main Container */
    .main-shell {{
      max-width: 980px;
      margin: 0 auto;
      padding: 36px 24px 0;
    }}

    .view-section {{ display: none; }}
    .view-section.active {{ display: block; animation: viewIn 0.25s ease-out; }}
    @keyframes viewIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    /* =========================================================================
       AMBOSS-STYLE SMART MEDICAL TOOLTIPS
       ========================================================================= */
    .med-term {{
      border-bottom: 2px dotted #1D3557;
      color: #1D3557;
      font-weight: 600;
      cursor: help;
      position: relative;
      display: inline-block;
      transition: all 0.15s ease;
    }}
    .med-term:hover {{
      background: #EDF3FA;
      border-radius: 4px;
      color: #0E274D;
    }}
    .med-tooltip {{
      visibility: hidden;
      opacity: 0;
      position: absolute;
      bottom: 135%;
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      width: 295px;
      background: #18191B;
      color: #FFFFFF;
      border-radius: var(--radius-md);
      padding: 14px 16px;
      font-family: var(--font-sans);
      font-size: 0.84rem;
      font-weight: 400;
      line-height: 1.5;
      box-shadow: var(--shadow-float);
      z-index: 500;
      pointer-events: none;
      transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
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
      border-color: #18191B transparent transparent transparent;
    }}
    .med-term:hover .med-tooltip,
    .med-term:focus .med-tooltip {{
      visibility: visible;
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}
    .tt-kicker {{
      font-size: 0.68rem;
      font-weight: 700;
      color: #A3D9C9;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      display: block;
      margin-bottom: 2px;
    }}
    .tt-title {{
      font-size: 0.94rem;
      font-weight: 700;
      color: #FFFFFF;
      margin-bottom: 4px;
      display: block;
    }}
    .tt-desc {{
      color: #D6D6D6;
      display: block;
    }}
    .tt-pearl {{
      margin-top: 8px;
      padding-top: 8px;
      border-top: 1px solid #2F3136;
      color: #F8E7C9;
      font-size: 0.8rem;
      display: block;
    }}

    /* =========================================================================
       OSMOSIS ACTIVE CLOZE MASKING (UJI INGATAN ON/OFF)
       ========================================================================= */
    body.cloze-active .cloze-mask {{
      background: #E5E1D8 !important;
      color: transparent !important;
      border-radius: 6px;
      padding: 1px 7px;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
      display: inline-block;
      text-shadow: none !important;
    }}
    body.cloze-active .cloze-mask:hover {{
      background: #D4CEBF !important;
    }}
    body.cloze-active .cloze-mask.revealed {{
      background: var(--sage-light) !important;
      color: var(--sage) !important;
      font-weight: 700;
      padding: 1px 7px;
      border-radius: 6px;
      border: 1px solid var(--sage-border);
    }}

    /* =========================================================================
       THE "WHY" HERO: PEER STORYTELLING (DIAJARIN TEMEN SENDIRI)
       ========================================================================= */
    .why-section {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 38px 42px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-ambient);
    }}
    .why-kicker {{
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--sage);
      margin-bottom: 12px;
      display: block;
    }}
    .why-headline {{
      font-family: var(--font-serif);
      font-size: 2.7rem;
      font-weight: 600;
      line-height: 1.25;
      color: var(--ink);
      letter-spacing: -0.02em;
      margin-bottom: 18px;
    }}
    .why-lead {{
      font-size: 1.1rem;
      line-height: 1.75;
      color: var(--ink-secondary);
      margin-bottom: 26px;
    }}

    /* 3 Enigma Cards */
    .enigma-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 28px;
    }}
    .enigma-card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }}
    .enigma-card:hover {{
      background: #FFFFFF;
      border-color: var(--ink);
      transform: translateY(-2px);
      box-shadow: var(--shadow-ambient);
    }}
    .enigma-num {{
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--ink-muted);
      letter-spacing: 0.06em;
      margin-bottom: 6px;
    }}
    .enigma-title {{
      font-family: var(--font-serif);
      font-size: 1.2rem;
      font-weight: 600;
      color: var(--ink);
      line-height: 1.35;
      margin-bottom: 10px;
    }}
    .enigma-preview {{
      font-size: 0.88rem;
      color: var(--ink-secondary);
      line-height: 1.55;
      margin-bottom: 16px;
    }}
    .enigma-trigger {{
      align-self: flex-start;
      border: 1px solid var(--border-dark);
      background: var(--surface);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 5px 12px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .enigma-trigger:hover {{
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
    }}

    /* Enigma Reveal Box */
    .enigma-reveal {{
      margin-top: 24px;
      padding: 24px 28px;
      background: #FAF6ED;
      border-radius: var(--radius-md);
      border: 1px solid #EADBBE;
      display: none;
      animation: revealIn 0.25s ease-out;
    }}
    .enigma-reveal.open {{ display: block; }}
    @keyframes revealIn {{ from {{ opacity: 0; transform: translateY(-4px); }} to {{ opacity: 1; transform: translateY(0); }} }}
    .reveal-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }}
    .reveal-title {{
      font-size: 1.1rem;
      font-weight: 700;
      color: #38240D;
    }}
    .reveal-close {{
      border: none;
      background: transparent;
      font-size: 1.1rem;
      color: var(--ink-muted);
      cursor: pointer;
    }}
    .reveal-body {{
      font-size: 0.95rem;
      line-height: 1.68;
      color: #2F2110;
    }}

    .why-bridge-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 16px 22px;
      font-size: 0.94rem;
      color: var(--ink);
    }}
    .btn-start-mastery {{
      border: none;
      background: var(--ink);
      color: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 0.88rem;
      font-weight: 600;
      padding: 9px 20px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .btn-start-mastery:hover {{
      background: var(--sage);
      transform: translateY(-1px);
    }}

    /* =========================================================================
       SECTION: VISUAL SIMULATORS ("LANGSUNG PAHAM" 60 DETIK)
       ========================================================================= */
    .sim-block {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 30px 34px;
      margin-bottom: 32px;
      box-shadow: var(--shadow-ambient);
    }}
    .sim-head {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
    }}
    .sim-title-wrap h3 {{
      font-family: var(--font-serif);
      font-size: 1.45rem;
      font-weight: 600;
      color: var(--ink);
    }}
    .sim-title-wrap p {{
      font-size: 0.9rem;
      color: var(--ink-secondary);
      margin-top: 2px;
    }}
    .btn-intip-slide {{
      border: 1px solid var(--border);
      background: var(--bg);
      color: var(--ink-secondary);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .btn-intip-slide:hover {{
      border-color: var(--ink);
      color: var(--ink);
    }}

    /* Iron Stepper */
    .stager-tabs {{
      display: flex;
      background: var(--surface-subtle);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 4px;
      margin-bottom: 20px;
    }}
    .stager-btn {{
      flex: 1;
      border: none;
      background: transparent;
      padding: 10px 14px;
      font-family: var(--font-sans);
      font-size: 0.86rem;
      font-weight: 600;
      color: var(--ink-secondary);
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.18s ease;
      text-align: center;
    }}
    .stager-btn.active {{
      background: #FFFFFF;
      color: var(--ink);
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }}
    .vial-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 16px;
    }}
    .vial-card {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      transition: all 0.2s ease;
    }}
    .vial-card.active-vial {{
      background: #FFFFFF;
      border-color: var(--terracotta);
      box-shadow: 0 0 0 2px var(--terracotta-light);
    }}
    .vial-lbl {{
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--ink-muted);
    }}
    .vial-val {{
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--ink);
      margin: 4px 0 6px;
    }}
    .vial-tag {{
      font-size: 0.82rem;
      font-weight: 600;
    }}
    .tag-danger {{ color: var(--terracotta); }}
    .tag-safe {{ color: var(--sage); }}
    .tag-warn {{ color: var(--ochre); }}
    .stager-explainer {{
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      font-size: 0.94rem;
      line-height: 1.65;
      color: var(--ink);
    }}

    /* ROMK Simulator */
    .romk-box {{
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 24px;
      align-items: center;
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 24px 28px;
    }}
    .romk-render {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px;
      text-align: center;
    }}
    .romk-door {{
      height: 80px;
      border: 3px dashed var(--navy);
      border-radius: var(--radius-sm);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 14px 0;
      font-weight: 700;
      font-size: 0.95rem;
      transition: all 0.25s ease;
    }}
    .romk-door.plugged {{
      background: var(--sage-light);
      border-color: var(--sage);
      color: var(--sage);
    }}
    .romk-door.leaking {{
      background: var(--terracotta-light);
      border-color: var(--terracotta);
      color: var(--terracotta);
    }}
    .romk-switches {{
      display: flex;
      flex-direction: column;
      gap: 12px;
    }}
    .switch-btn {{
      padding: 12px 18px;
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
      background: #FFFFFF;
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      text-align: left;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .switch-btn:hover {{ border-color: var(--ink); }}
    .switch-btn.active {{
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
    }}

    /* =========================================================================
       SECTION: MASTER-DETAIL 8 MINERAL DECK (KENYAMANAN TANPA LELAH)
       ========================================================================= */
    .browser-deck {{
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 24px;
      margin-bottom: 48px;
    }}
    .deck-nav-col {{
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}
    .deck-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 16px;
      border-radius: var(--radius-md);
      background: #FFFFFF;
      border: 1px solid var(--border);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s ease;
      text-align: left;
    }}
    .deck-item:hover {{
      background: var(--surface-subtle);
      border-color: var(--border-dark);
      transform: translateX(2px);
    }}
    .deck-item.active {{
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
      box-shadow: var(--shadow-ambient);
    }}
    .deck-badge {{
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--surface-subtle);
      color: var(--ink-secondary);
    }}
    .deck-item.active .deck-badge {{
      background: rgba(255, 255, 255, 0.2);
      color: #FFFFFF;
    }}

    .sheet-card {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 30px 34px;
      box-shadow: var(--shadow-ambient);
      display: none;
      animation: sheetFade 0.2s ease-out;
    }}
    .sheet-card.active {{ display: block; }}
    @keyframes sheetFade {{ from {{ opacity: 0; transform: translateY(4px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    .sheet-title-row {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 22px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }}
    .sheet-title-row h2 {{
      font-family: var(--font-serif);
      font-size: 2.1rem;
      font-weight: 600;
      color: var(--ink);
      line-height: 1.15;
    }}
    .sheet-title-row span {{
      font-size: 0.86rem;
      color: var(--ink-muted);
      margin-top: 4px;
      display: block;
    }}

    .sheet-columns {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 18px;
      margin-bottom: 22px;
    }}
    .sheet-pane {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
    }}
    .sheet-pane h4 {{
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }}
    .sheet-pane ul {{
      padding-left: 18px;
      font-size: 0.94rem;
      line-height: 1.6;
      color: #2D2F33;
    }}

    .uab-trap-box {{
      background: var(--ochre-light);
      border: 1px solid var(--ochre-border);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 22px;
    }}
    .uab-trap-box h4 {{
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ochre);
      margin-bottom: 4px;
    }}
    .uab-trap-box p {{
      font-size: 0.94rem;
      line-height: 1.6;
      color: #38240D;
    }}

    .slide-inspector-bar {{
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .slide-inspector-bar:hover {{
      background: #EAE6DF;
      border-color: var(--ink);
    }}
    .inspector-meta-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .inspector-pic {{
      width: 72px;
      height: 48px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }}
    .inspector-labels strong {{
      font-size: 0.9rem;
      color: var(--ink);
      display: block;
    }}
    .inspector-labels span {{
      font-size: 0.78rem;
      color: var(--ink-muted);
    }}

    /* =========================================================================
       SECTION: CBT PRACTICE (100% BUG FREE & SATISFYING)
       ========================================================================= */
    .cbt-anchor {{
      margin-top: 36px;
    }}
    .cbt-score-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }}
    .score-number {{
      font-family: var(--font-mono);
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--sage);
    }}

    .q-card-box {{
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px 32px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-ambient);
    }}
    .q-tag-line {{
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--ink-muted);
      margin-bottom: 8px;
      display: block;
    }}
    .q-stem-body {{
      font-size: 1.05rem;
      font-weight: 500;
      line-height: 1.68;
      color: var(--ink);
      margin-bottom: 20px;
    }}

    .q-options-col {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}
    .opt-choice-btn {{
      padding: 14px 18px;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      background: #FFFFFF;
      text-align: left;
      font-family: var(--font-sans);
      font-size: 0.95rem;
      color: var(--ink);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 14px;
      transition: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    .opt-choice-btn:hover {{
      background: var(--bg);
      border-color: var(--border-dark);
      transform: translateX(2px);
    }}
    .opt-key-badge {{
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--ink-muted);
      flex: none;
    }}

    .opt-choice-btn.is-correct {{
      background: var(--sage-light) !important;
      border-color: var(--sage) !important;
      color: var(--sage) !important;
      font-weight: 600;
      box-shadow: 0 0 0 1px var(--sage);
    }}
    .opt-choice-btn.is-wrong {{
      background: var(--terracotta-light) !important;
      border-color: var(--terracotta) !important;
      color: var(--terracotta) !important;
    }}

    .feedback-sheet {{
      margin-top: 20px;
      padding: 20px 24px;
      border-radius: var(--radius-md);
      font-size: 0.94rem;
      line-height: 1.65;
      display: none;
      animation: fbIn 0.2s ease-out;
    }}
    .feedback-sheet.show {{ display: block; }}
    @keyframes fbIn {{ from {{ opacity: 0; transform: translateY(-4px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    .feedback-sheet.tone-correct {{
      background: var(--sage-light);
      border: 1px solid var(--sage-border);
      color: #124029;
    }}
    .feedback-sheet.tone-wrong {{
      background: var(--terracotta-light);
      border: 1px solid var(--terracotta-border);
      color: #61180C;
    }}

    /* Lightbox Modal */
    .lightbox-backdrop {{
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(20, 21, 23, 0.85); backdrop-filter: blur(10px);
      display: none; align-items: center; justify-content: center; padding: 24px;
    }}
    .lightbox-backdrop.open {{ display: flex; }}
    .lightbox-frame {{
      max-width: 92%; max-height: 88vh; border-radius: var(--radius-md);
      box-shadow: var(--shadow-float);
    }}

    @media (max-width: 860px) {{
      .why-section {{ padding: 26px 18px; }}
      .why-headline {{ font-size: 2.1rem; }}
      .enigma-grid {{ grid-template-columns: 1fr; }}
      .browser-deck {{ grid-template-columns: 1fr; }}
      .vial-grid {{ grid-template-columns: 1fr; }}
      .romk-box {{ grid-template-columns: 1fr; }}
      .sheet-columns {{ grid-template-columns: 1fr; }}
      .view-pills {{ display: none; }}
    }}
  </style>
</head>
<body>

  <!-- Minimalist Sticky Header -->
  <header class="app-header">
    <div class="header-content">
      <div class="brand-mark">
        <span class="brand-tag">EMN 3</span>
        <div class="brand-context">
          <span class="brand-context-title">Defisiensi Mineral</span>
          <span class="brand-context-sub">dr. Iwal Reza Ahdi, Sp.PD-FINASIM</span>
        </div>
      </div>

      <nav class="view-pills">
        <button type="button" class="view-pill active" onclick="switchNav('view-story', this)">1. Kenapa Harus Peduli?</button>
        <button type="button" class="view-pill" onclick="switchNav('view-sim', this)">2. Konsep 60 Detik</button>
        <button type="button" class="view-pill" onclick="switchNav('view-deck', this)">3. Buku 8 Mineral</button>
        <button type="button" class="view-pill" onclick="switchNav('view-modul', this)">4. Kurikulum &amp; SKDI 4A</button>
        <button type="button" class="view-pill" onclick="switchNav('view-cbt', this)">5. Latihan UAB (8)</button>
      </nav>

      <div class="header-actions">
        <!-- Feature 2: Active Masking / Cloze Mode Toggle Button -->
        <button type="button" id="cloze-toggle" class="btn-cloze-toggle" onclick="toggleCloze()" title="Tekan M di keyboard untuk sembunyikan kata/angka kunci">
          <span>🧠 Uji Ingatan</span>
          <span class="cloze-badge-pill" id="cloze-status-tag">OFF</span>
        </button>
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-anki" download>Deck Anki</a>
      </div>
    </div>
  </header>

  <main class="main-shell">

    <!-- =================================================================== -->
    <!-- VIEW 1: THE "WHY" HOOK (PEER-TO-PEER STORYTELLING KASUAL)           -->
    <!-- =================================================================== -->
    <div id="view-story" class="view-section active">
      <article class="why-section">
        <span class="why-kicker">Obrolan Santai Sebelum Buka Materi · Baca Ini 2 Menit</span>
        <h1 class="why-headline">Tiga Atom Penentu Hidup-Mati yang Sering Bikin Dokter Panik di IGD</h1>
        <p class="why-lead">
          Jujur aja, materi mineral sering disepelein: <i>"Ah, cuma hafalan tabel periodik, mending scroll TikTok."</i> Tapi bayangin kamu lagi jaga malam di IGD, dan ada pasien sekarat cuma gara-gara salah ngasih semangkuk bubur atau salah ngitung tetesan infus. Di dalam 60 triliun sel tubuh manusia, atom-atom renik seperti <strong>Besi, Magnesium, Fosfat, dan Seng</strong> ini adalah sakelar listrik kehidupan. Salah paham sedikit, akibatnya fatal.
        </p>

        <!-- 3 High-Stakes Clinical Enigmas -->
        <div class="enigma-grid">
          
          <!-- Enigma 1 -->
          <div class="enigma-card">
            <div>
              <span class="enigma-num">MISTERI 01</span>
              <h3 class="enigma-title">Niat Baik yang Membunuh</h3>
              <p class="enigma-preview">Pasien kelaparan 12 hari kamu kasih makan dengan niat mulia. Dalam 48 jam, napasnya berhenti dan jantungnya kolaps. Kenapa?</p>
            </div>
            <button type="button" class="enigma-trigger" onclick="openEnigma(1)">Buka Misteri ↗</button>
          </div>

          <!-- Enigma 2 -->
          <div class="enigma-card">
            <div>
              <span class="enigma-num">MISTERI 02</span>
              <h3 class="enigma-title">Otak yang Ngidam Es Batu</h3>
              <p class="enigma-preview">Cewek muda ngunyah es batu berember-ember tiap hari. Dia gak gila, otaknya lagi kelaparan satu atom, padahal Hb-nya masih normal!</p>
            </div>
            <button type="button" class="enigma-trigger" onclick="openEnigma(2)">Buka Misteri ↗</button>
          </div>

          <!-- Enigma 3 -->
          <div class="enigma-card">
            <div>
              <span class="enigma-num">MISTERI 03</span>
              <h3 class="enigma-title">Infus yang Ditelan Ginjal</h3>
              <p class="enigma-preview">Infus kalium udah habis 3 botol, tapi kalium darah pasien tetep anjlok parah. Kenapa ginjalnya malah ngebuang kalium itu?</p>
            </div>
            <button type="button" class="enigma-trigger" onclick="openEnigma(3)">Buka Misteri ↗</button>
          </div>

        </div>

        <!-- Dynamic Revelation Box -->
        <div class="enigma-reveal" id="enigma-reveal-box">
          <div class="reveal-head">
            <span class="reveal-title" id="reveal-title">Misteri Terbuka</span>
            <button type="button" class="reveal-close" onclick="closeEnigma()">✕</button>
          </div>
          <div class="reveal-body" id="reveal-text"></div>
        </div>

        <div class="why-bridge-bar">
          <span>Gimana, seru kan rahasia di balik atom-atom ini? Yuk kita bedah mekanismenya pelan-pelan:</span>
          <button type="button" class="btn-start-mastery" onclick="switchNav('view-sim', document.querySelectorAll('.view-pill')[1])">
            Mulai Konsep 60 Detik →
          </button>
        </div>
      </article>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 2: VISUAL SIMULATORS ("LANGSUNG PAHAM" DALAM 60 DETIK)        -->
    <!-- =================================================================== -->
    <div id="view-sim" class="view-section">

      <!-- SIMULATOR 1 -->
      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>1. Kenapa Nilai MCV Normal Bisa Menipu? (3 Stadium Besi)</h3>
            <p>Klik tombol stadium di bawah ini. Perhatikan tabung mana yang anjlok duluan:</p>
          </div>
          <button type="button" class="btn-intip-slide" onclick="openLightbox('slides_kul3/slide_10.jpg')">Intip Slide 10 ↗</button>
        </div>

        <div class="stager-tabs">
          <button type="button" class="stager-btn active" onclick="setIron(1)">Stadium 1: Cadangan Turun</button>
          <button type="button" class="stager-btn" onclick="setIron(2)">Stadium 2: Produksi Terbatas</button>
          <button type="button" class="stager-btn" onclick="setIron(3)">Stadium 3: Anemia Nyata (IDA)</button>
        </div>

        <div class="vial-grid">
          <div class="vial-card active-vial" id="vc-ferr">
            <span class="vial-lbl">{tt("Ferritin", "Ferritin Serum", "Protein pengikat cadangan besi intraseluler di hati dan sumsum tulang.", "Nilai normal 20–250 ng/mL. Anjlok <15–30 ng/mL saat cadangan habis.")} (Gudang Besi)</span>
            <div class="vial-val" id="val-ferr">{cl("&lt; 15 ng/mL")}</div>
            <span class="vial-tag tag-danger" id="tag-ferr">ANJLOK DULUAN (Kritis)</span>
          </div>
          <div class="vial-card" id="vc-tsat">
            <span class="vial-lbl">{tt("TSAT", "Saturasi Transferrin (TSAT)", "Persentase protein transferrin yang mengikat besi di darah.", "Normal 20–50%. Anjlok <16–20% menandakan besi transpor berkurang.")} (Truk Pengangkut)</span>
            <div class="vial-val" id="val-tsat">{cl("28% (Normal)")}</div>
            <span class="vial-tag tag-safe" id="tag-tsat">Transpor Masih Cukup</span>
          </div>
          <div class="vial-card" id="vc-hb">
            <span class="vial-lbl">Hemoglobin &amp; {tt("MCV", "Mean Corpuscular Volume", "Ukuran rata-rata volume satu butir eritrosit.", "Normal 80–100 fL. Jika <80 fL disebut mikrositik.")}</span>
            <div class="vial-val" id="val-hb">{cl("Hb 13.5 · MCV 88")}</div>
            <span class="vial-tag tag-safe" id="tag-hb">Tampak Normal (Belum Anemia)</span>
          </div>
        </div>

        <div class="stager-explainer" id="explainer-iron">
          💡 <b>Trik Ujian dr. Iwal:</b> Bayangin gudang di rumahmu udah kosong melompong (Ferritin anjlok), tapi stok makanan di meja makan masih ada (Hb normal). Pasien di Stadium 1 <i>belum anemia</i>! Makanya kalau dokter cuma ngecek Hb dan MCV, dia bakal ketipu ngira pasien sehat. <b>Ferritin adalah saksi kunci pertama yang menjerit!</b>
        </div>
      </article>

      <!-- SIMULATOR 2 -->
      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>2. Kenapa Kalium Malah Bocor ke Urin Kalau Magnesium Rendah?</h3>
            <p>Coba klik tombol di bawah untuk melihat gerbang kanal ginjal yang bikin dokter jaga bingung:</p>
          </div>
          <button type="button" class="btn-intip-slide" onclick="openLightbox('slides_kul3/slide_17.jpg')">Intip Slide 17 ↗</button>
        </div>

        <div class="romk-box">
          <div class="romk-render">
            <span style="font-size:0.78rem;font-weight:700;color:var(--ink-muted);text-transform:uppercase;">Membran Tubulus Ginjal</span>
            <div class="romk-door plugged" id="romk-door">
              <span id="romk-txt">🔒 KANAL ROMK TERSUMBAT (Mg Cukup)</span>
            </div>
            <span id="romk-urine" style="font-size:0.84rem;color:var(--sage);font-weight:600;">Kalium aman di darah, gak lolos ke kencing</span>
          </div>

          <div class="romk-switches">
            <button type="button" class="switch-btn active" id="sw-mg-norm" onclick="setROMK(true)">
              <span>Magnesium Normal ({cl("&gt;1.7 mg/dL")})</span>
              <span>🔒 Tertutup</span>
            </button>
            <button type="button" class="switch-btn" id="sw-mg-low" onclick="setROMK(false)">
              <span>Magnesium Rendah (Efek Furosemid/PPI)</span>
              <span>⚠️ Bocor</span>
            </button>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">
              Ion Magnesium intraseluler itu ibarat <b>tutup botol alami kanal {tt("ROMK", "Renal Outer Medullary Potassium Channel", "Pintu keluar ion kalium di membran tubulus ginjal.", "Dihambat oleh ion Mg intrasel. Jika Mg rendah, pintu ini terbuka permanen sehingga kalium bocor terbuang ke urin.")}</b> di ginjal. Kalau Mg hilang, pintunya ngebuka lebar tanpa henti &rarr; Kalium infus yang kamu suntikkan bakal langsung terbuang ke urin. Makanya: <b>Wajib kasih Magnesium barengan sama Kalium!</b>
            </p>
          </div>
        </div>
      </article>

      <!-- SIMULATOR 3 -->
      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>3. Kaskade Refeeding: Kenapa Makanan Bikin Diafragma Lumpuh?</h3>
            <p>Alur detik demi detik bagaimana insulin menyedot fosfat dari darah sampai sel kehabisan bensin.</p>
          </div>
          <button type="button" class="btn-intip-slide" onclick="openLightbox('slides_kul3/slide_19.jpg')">Intip Slide 19 ↗</button>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:12px;">
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ink-muted);">01. KELAPARAN</span>
            <div style="font-weight:700;margin:4px 0 6px;">Puasa Lama &gt;10 Hari</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Cadangan fosfat di dalam sel udah habis kering kerontang.</p>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ochre);">02. MAKANAN MASUK</span>
            <div style="font-weight:700;color:var(--ochre);margin:4px 0 6px;">Karbohidrat Tiba-Tiba</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Pankreas syok lalu memompa lonjakan hormon <b>Insulin super gede</b>.</p>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--terracotta);">03. PENYEDOTAN</span>
            <div style="font-weight:700;color:var(--terracotta);margin:4px 0 6px;">Fosfat Masuk Sel</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Insulin nyedot semua <b>Fosfat (P), K, dan Mg</b> dari darah masuk ke dalam sel.</p>
          </div>
          <div style="background:var(--terracotta-light);border:1px solid var(--terracotta-border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--terracotta);font-weight:700;">04. GAGAL NAPAS</span>
            <div style="font-weight:700;color:var(--terracotta);margin:4px 0 6px;">Fosfat Darah {cl("&lt;1.0 mg/dL")}</div>
            <p style="font-size:0.84rem;color:#5D150B;line-height:1.5;">Pabrik ATP mati total &rarr; <b>otot diafragma lemes gak bisa narik napas</b>.</p>
          </div>
        </div>
      </article>

    </div>

    <!-- =================================================================== -->
    <!-- VIEW 3: BUKU EKSPLORASI 8 MINERAL (KENYAMANAN TANPA LELAH)          -->
    <!-- =================================================================== -->
    <div id="view-deck" class="view-section">
      <div class="browser-deck">
        
        <nav class="deck-nav-col" aria-label="Daftar Mineral">
          <button type="button" class="deck-item active" onclick="pickDeck('fe', this)">
            <span>1. Besi (Fe)</span>
            <span class="deck-badge">Renik</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('zn', this)">
            <span>2. Seng (Zn)</span>
            <span class="deck-badge">Renik</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('mg', this)">
            <span>3. Magnesium (Mg)</span>
            <span class="deck-badge">Makro</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('ca', this)">
            <span>4. Kalsium (Ca)</span>
            <span class="deck-badge">Makro</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('p', this)">
            <span>5. Fosfat (P)</span>
            <span class="deck-badge">Makro</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('cu', this)">
            <span>6. Tembaga (Cu)</span>
            <span class="deck-badge">Renik</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('i', this)">
            <span>7. Iodium (I)</span>
            <span class="deck-badge">Renik</span>
          </button>
          <button type="button" class="deck-item" onclick="pickDeck('se', this)">
            <span>8. Selenium (Se)</span>
            <span class="deck-badge">Renik</span>
          </button>
        </nav>

        <div>
          <!-- BESI -->
          <article class="sheet-card active" id="deck-fe">
            <div class="sheet-title-row">
              <div>
                <h2>Besi (Fe)</h2>
                <span>Bahan Inti Pengangkut Oksigen Hemoglobin &amp; Mioglobin</span>
              </div>
              <span class="brand-tag" style="background:var(--terracotta);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Gejala Khas Pasien</h4>
                <ul>
                  <li>Badan lemes gampang capek, jantung berdebar-debar.</li>
                  <li>{tt("Pagophagia", "Pagophagia", "Bentuk pica spesifik berupa dorongan kompulsif untuk mengunyah es batu berulang kali.", "Patognomonik untuk anemia defisiensi besi.")}: Ngidam ngunyah es batu terus-menerus.</li>
                  <li>Kuku cekung mirip sendok ({tt("Koilonychia", "Koilonychia", "Kelainan bentuk lempeng kuku yang menipis dan melengkung ke dalam menyerupai sendok.", "Tanda fisik klasik anemia defisiensi besi kronis berat.")}) dan lidah licin merah ({tt("Glossitis", "Atrophic Glossitis", "Atrofi papil-papil lidah sehingga permukaan lidah tampak licin, merah mengkilap, dan perih.", "Sering menyertai defisiensi besi, folat, atau kobalamin B12.")}).</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Kunci Lab Ujian UAB</h4>
                <ul>
                  <li><b>{tt("Ferritin", "Ferritin Serum", "Protein utama penyimpan cadangan besi tubuh di retikuloendotelial hati dan sumsum tulang.", "Nilai normal 20–250 ng/mL. Jika <15–30 ng/mL, pasti defisiensi besi!")} {cl("&lt; 15–30 ng/mL")}</b>: Kunci paling awal yang anjlok!</li>
                  <li>{tt("TSAT", "Saturasi Transferrin", "Persentase kapasitas transferrin yang terisi besi sirkulasi.", "Normal 20–50%. Anjlok <16–20% menandakan eritropoiesis terbatas.")} {cl("&lt; 16–20%")}, {tt("TIBC", "Total Iron Binding Capacity", "Kapasitas maksimal protein transferrin darah untuk mengikat zat besi.", "Meningkat >400 ug/dL saat tubuh kekurangan besi.")} meningkat.</li>
                  <li>{tt("MCV", "Mean Corpuscular Volume", "Volume rata-rata satu butir eritrosit.", "Normal 80–100 fL. Jika <80 fL disebut mikrositik.")} {cl("&lt; 80 fL (Mikrositik Hipokromik)")} baru muncul di stadium lanjut.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Jebakan Ujian dr. Iwal (Aturan Resep AGA 2024)</h4>
              <p><b>Jangan tulis resep tablet besi 3x sehari!</b> Setiap asupan besi bikin hati memproduksi hormon {tt("Hepcidin", "Hepcidin", "Hormon peptida pengatur utama kadar besi sistemik buatan hati.", "Mengunci dan mendegradasi ferroportin usus selama 24–48 jam sehingga penyerapan besi berikutnya terhenti total.")}. Hepcidin ini ngunci pintu usus selama 24–48 jam. Dosis kedua dan ketiga gak bakal diserap, cuma bikin pasien mual dan sembelit. Rekomendasi benar: <b>{cl("Maksimal 1x sehari pagi hari atau selang-hari (alternate-day)!")}</b></p>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_10.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_10.jpg" class="inspector-pic" alt="Slide 10">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 10: Perjalanan Defisiensi Besi</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- SENG -->
          <article class="sheet-card" id="deck-zn">
            <div class="sheet-title-row">
              <div>
                <h2>Seng (Zinc / Zn)</h2>
                <span>Kofaktor &gt;300 Enzim, Pertumbuhan Anak, dan Kulit Mulus</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Trias Patognomonik (Hafalkan Ini!)</h4>
                <ul>
                  <li><b>{cl("Dermatitis periorifisial &amp; akral")}:</b> Korengan merah bersisik di sekitar mulut, anus, ujung jari.</li>
                  <li><b>Diare kronik:</b> Karena sel usus gak bisa regenerasi tanpa seng.</li>
                  <li><b>Alopesia:</b> Rambut rontok parah sampai botak.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Kelainan Khusus &amp; Gejala Lain</h4>
                <ul>
                  <li>Luka gak sembuh-sembuh, anak jadi stunting/cebol.</li>
                  <li>Lidah gak bisa ngerasain makanan (hipogeusia).</li>
                  <li>Bentuk bawaan genetik: {tt("Acrodermatitis enteropathica", "Acrodermatitis Enteropathica", "Penyakit genetik resesif mutasi gen transporter seng ZIP4 di usus halus.", "Trias: dermatitis periorifisial & akral, diare kronik, alopesia.")}.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Jebakan Makanan: Bahaya Asam Fitat</h4>
              <p>Anak yang cuma dikasih makan bubur gandum/serealia mentah tanpa protein hewani bakal kena defisiensi seng parah. Kenapa? Karena gandum mengandung {tt("Asam Fitat", "Phytic Acid / Fitat", "Senyawa organik pengikat mineral yang melimpah pada kulit ari biji-bijian dan serealia tak beragi.", "Mengikat kation divalen (Zn2+, Fe2+, Ca2+) di usus membentuk kelat tak larut yang gak bisa diserap tubuh.")} yang mengikat seng di usus kayak lem.</p>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_12.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_12.jpg" class="inspector-pic" alt="Slide 12">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 12: Seng, Imunitas, &amp; Fitat</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- MAGNESIUM -->
          <article class="sheet-card" id="deck-mg">
            <div class="sheet-title-row">
              <div>
                <h2>Magnesium (Mg)</h2>
                <span>Penenang Saraf, Kofaktor ATP, dan Pengunci Kalium Ginjal</span>
              </div>
              <span class="brand-tag" style="background:var(--navy);">Makromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Gejala Hipomagnesemia ({cl("&lt;1.7 mg/dL")})</h4>
                <ul>
                  <li>Tremor gemetaran, kram betis, refleks tendon hiperaktif.</li>
                  <li>Aritmia jantung mematikan (Torsades de pointes).</li>
                  <li>Sering bikin kalsium dan kalium ikut anjlok.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Siapa yang Paling Sering Kena?</h4>
                <ul>
                  <li>Orang minum obat kencing <b>furosemid</b> menahun.</li>
                  <li>Orang sakit maag minum obat <b>PPI (omeprazole) bertahun-tahun</b>.</li>
                  <li>Pasien diare kronik dan pecandu alkohol.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Kenapa Kalium Gagal Naik Kalau Mg Masih Rendah?</h4>
              <p>Di ginjal, ion Magnesium bertindak sebagai sumbat gerbang kanal {tt("ROMK", "Renal Outer Medullary Potassium Channel", "Pintu gerbang ekskresi kalium di tubulus distal ginjal.", "Saat magnesium darah anjlok, pintu ini terbuka permanen sehingga kalium darah bocor terbuang ke urin.")}. Kalau Mg rendah, pintu ROMK terbuka permanen &rarr; kalium infus yang kamu suntikkan bakal langsung terbuang ke pispot urin. <b>Koreksi Magnesium dulu bareng Kalium!</b></p>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_17.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_17.jpg" class="inspector-pic" alt="Slide 17">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 17: Regulasi Ginjal ROMK</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- KALSIUM -->
          <article class="sheet-card" id="deck-ca">
            <div class="sheet-title-row">
              <div>
                <h2>Kalsium (Ca)</h2>
                <span>Batu Bata Tulang (99%) &amp; Penjaga Arus Listrik Otot</span>
              </div>
              <span class="brand-tag" style="background:var(--navy);">Makromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Gejala Kalsium Rendah Akut</h4>
                <ul>
                  <li>Bibir dan ujung jari kesemutan tebel (parestesia perioral).</li>
                  <li>Kejang kram kaku tangan (tetani/spasme karpopedal).</li>
                  <li><b>EKG:</b> {cl("Interval QT memanjang")}, rawan aritmia.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Dua Tes Fisik Langsung Tahu</h4>
                <ul>
                  <li><b>{tt("Chvostek sign", "Tanda Chvostek", "Ketuk ringan saraf fasialis di depan telinga -> sudut bibir pasien berkedut sendiri.", "Tanda hipereksitabilitas membran saraf akibat hipokalsemia.")}:</b> Ketuk pipi depan telinga, bibir kedutan.</li>
                  <li><b>{tt("Trousseau sign", "Tanda Trousseau", "Pompa manset tensimeter di atas tekanan sistolik selama 3 menit -> pergelangan tangan menekuk kaku (carpopedal spasm).", "Tanda klinis paling akurat dan sensitif untuk hipokalsemia.")}:</b> Pompa tensi di atas sistolik 3 menit, jari tangan menekuk kram.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Jebakan Nilai Albumin Lab</h4>
              <p>Hanya <b>Ionized Calcium (kalsium ion bebas 50%)</b> yang aktif di pembuluh darah. Kalsium total di lembar lab sering menipu kalau pasien kurang gizi (karena terikat albumin; albumin turun 1, kalsium total tampak turun 0.8 padahal kalsium ionnya bisa normal).</p>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_15.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_15.jpg" class="inspector-pic" alt="Slide 15">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 15: Hipokalsemia &amp; Evaluasi</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- FOSFAT -->
          <article class="sheet-card" id="deck-p">
            <div class="sheet-title-row">
              <div>
                <h2>Fosfat (P)</h2>
                <span>Bensin Energi Seluler (ATP) &amp; Bahaya Refeeding</span>
              </div>
              <span class="brand-tag" style="background:var(--navy);">Makromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Kaskade Refeeding Mematikan</h4>
                <ul>
                  <li>Puasa lama bikin sel kelaparan &amp; cadangan fosfat ludes.</li>
                  <li>Diberi makan karbohidrat mendadak &rarr; insulin melonjak gila-gilaan.</li>
                  <li>Fosfat plasma anjlok <b>{cl("&lt; 1.0 mg/dL")}</b> karena kesedot ke sel.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Akibatnya Kalau Fosfat Darah Habis</h4>
                <ul>
                  <li>Pabrik bensin ATP seluler mati mendadak.</li>
                  <li><b>Otot diafragma lumpuh:</b> Pasien gak bisa narik napas &rarr; gagal napas.</li>
                  <li>Jantung melemah, aritmia fatal, otot rontok (rabdomiolisis).</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Cara Benar Kasih Makan Orang Kelaparan (ASPEN/NICE)</h4>
              <p>1. Suntik vitamin <b>Tiamin (B1) sebelum makanan pertama masuk</b>.<br>
              2. Kasih kalori sangat rendah bertahap: <b>{cl("10–15 kkal/kg/hari")}</b>.<br>
              3. Cek lab fosfat, kalium, dan magnesium darah tiap 24 jam.</p>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_19.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_19.jpg" class="inspector-pic" alt="Slide 19">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 19: Pola Refeeding Syndrome</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- TEMBAGA -->
          <article class="sheet-card" id="deck-cu">
            <div class="sheet-title-row">
              <div>
                <h2>Tembaga (Copper / Cu)</h2>
                <span>Partner Besi di Ceruloplasmin &amp; Pembungkus Kabel Saraf</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Trias Defisiensi Tembaga</h4>
                <ul>
                  <li><b>Anemia mikrositik:</b> Gak mempan dikasih obat besi.</li>
                  <li><b>Neutropenia berat:</b> Sel darah putih leukosit anjlok.</li>
                  <li><b>Mielopati:</b> Kaki baal dan jalan sempoyongan ({tt("Ataksia", "Ataksia Sensorik", "Gangguan koordinasi gaya berjalan akibat degenerasi kolumna dorsalis medula spinalis.", "Menyerupai defisiensi vitamin B12 (subacute combined degeneration).")}).</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Siapa Korbannya?</h4>
                <ul>
                  <li>Orang rajin minum <b>suplemen Zinc dosis tinggi (&gt;50 mg/hari)</b>.</li>
                  <li>Pasien habis operasi potong lambung (bariatrik bypass).</li>
                  <li>Pemakai lem gigi palsu kaya kandungan zinc.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Kenapa Zinc Berlebih Malah Bikin Kurang Tembaga?</h4>
              <p>Seng berlebih bikin sel usus memproduksi protein {tt("Metallothionein", "Metallothionein", "Protein sel usus yang bertindak sebagai penjara pengikat tembaga.", "Diinduksi oleh zinc dosis tinggi; mengikat tembaga sangat kuat sehingga Cu terbuang saat sel usus terkelupas.")}. Protein ini lebih suka nempel sama tembaga daripada seng &rarr; tembaga terperangkap di sel usus dan kebuang pas BAB.</p>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_22.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_22.jpg" class="inspector-pic" alt="Slide 22">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 22: Tembaga &amp; Efek Samping Seng</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- IODIUM -->
          <article class="sheet-card" id="deck-i">
            <div class="sheet-title-row">
              <div>
                <h2>Iodium (I)</h2>
                <span>Bahan Bakar Utama Hormon Tiroid T3 &amp; T4</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Kalau Kena di Orang Dewasa</h4>
                <p>Iodium kurang &rarr; pabrik tiroid macet &rarr; otak ngirim sinyal TSH tinggi buat maksa kerja &rarr; kelenjar tiroid bengkak jadi <b>gondok / struma endemik</b>.</p>
              </div>
              <div class="sheet-pane">
                <h4>Kalau Kena di Ibu Hamil (Fatal!)</h4>
                <p>Janin kekurangan hormon tiroid saat otak lagi dibentuk &rarr; lahir dengan sindrom {tt("Kretinisme", "Kretinisme Endemik", "Kerusakan otak bawaan permanen akibat kekurangan iodium berat selama dalam kandungan.", "Gejala: keterbelakangan mental berat, tuli-bisu saraf, dan badan kerdil cebol.")}: idiot, tuli-bisu, dan badan cebol permanen.</p>
              </div>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_13.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_13.jpg" class="inspector-pic" alt="Slide 13">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 13: Iodium &amp; Kretinisme Janin</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

          <!-- SELENIUM -->
          <article class="sheet-card" id="deck-se">
            <div class="sheet-title-row">
              <div>
                <h2>Selenium (Se)</h2>
                <span>Penjaga Enzim Antioksidan Jantung (GPx)</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Penyakit Keshan (Kardiomiopati)</h4>
                <p>Di daerah yang tanahnya miskin selenium, anak-anak dan cewek muda kena {tt("Penyakit Keshan", "Penyakit Keshan", "Penyakit gagal jantung kardiomiopati kongestif endemik akibat tanah tandus miskin selenium.", "Enzim glutation peroksidase tidak terbentuk -> sel otot jantung hancur oleh radikal bebas.")}: otot jantungnya melar dan gagal mompa darah sampai meninggal.</p>
              </div>
              <div class="sheet-pane">
                <h4>Peran di Tubuh</h4>
                <p>Menjadi bagian dari enzim <i>Glutathione Peroxidase</i> untuk membunuh racun radikal bebas, serta membantu hormon tiroid T4 berubah jadi T3 aktif.</p>
              </div>
            </div>
            <div class="slide-inspector-bar" onclick="openLightbox('slides_kul3/slide_23.jpg')">
              <div class="inspector-meta-group">
                <img src="slides_kul3/slide_23.jpg" class="inspector-pic" alt="Slide 23">
                <div class="inspector-labels">
                  <strong>Bukti Slide Asli 23: Selenium &amp; Penyakit Keshan</strong>
                  <span>Tangkapan layar slide kuliah dr. Iwal Reza Ahdi, Sp.PD</span>
                </div>
              </div>
              <span style="font-weight:700;color:var(--sage);font-size:0.85rem;">Buka Slide ↗</span>
            </div>
          </article>

        </div>
      </div>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 4: KURIKULUM MODUL BLOK EMN & SKDI 4A (HARRISON + SAN + ULUL ALBAB) -->
    <!-- =================================================================== -->
    <div id="view-modul" class="view-section">
      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>1. Standar Kompetensi Dokter Indonesia (SKDI Level 4A — Tuntas Mandiri)</h3>
            <p>Sesuai <b>00. MODUL EMN 2026</b> (Hal. 22 &amp; 43): Sebagai dokter layanan primer, kamu wajib bisa mendiagnosis dan menuntaskan kasus defisiensi mineral secara mandiri dari anamnesis sampai terapi.</p>
          </div>
          <span class="brand-tag" style="background:var(--sage);">SKDI LEVEL 4A</span>
        </div>

        <div class="sheet-columns">
          <div class="sheet-pane">
            <h4>Keterampilan Klinis Wajib (OSCE &amp; Klinik)</h4>
            <ul>
              <li><b>Dietary History &amp; 24-Hour Recall (Level 4A):</b> Menggali pola makan harian pasien (kurang daging merah, diet tinggi fitat serealia, minum teh sehabis makan, konsumsi garam non-iodium).</li>
              <li><b>Pemeriksaan Fisik Nutrisi &amp; Tiroid:</b> Inspeksi konjungtiva anemis, {tt("Koilonychia", "Koilonychia", "Kuku cekung seperti sendok.", "Khas pada anemia defisiensi besi kronis.")}, ruam periorifisial, ketukan {tt("Chvostek sign", "Tanda Chvostek", "Ketuk nervus fasialis depan telinga.", "Kedutan sudut bibir pada hipokalsemia.")}, manset {tt("Trousseau sign", "Tanda Trousseau", "Pompa tensi >sistolik 3 menit.", "Spasme karpopedal pada hipokalsemia.")}, dan palpasi struma/gondok tiroid.</li>
            </ul>
          </div>
          <div class="sheet-pane">
            <h4>Alur 10 Poin RPS Fakultas Kedokteran</h4>
            <ul>
              <li><b>Diagnosis Banding Mikrositik:</b> Wajib bedakan Defisiensi Besi ({cl("Ferritin &lt;15 ng/mL")}) vs Thalassemia ({cl("Mentzer Index &lt;13")}) vs Anemia Penyakit Kronis ({cl("Hepcidin naik akibat IL-6")}).</li>
              <li><b>Prognosis &amp; Komplikasi:</b> Kretinisme permanen pada janin ibu kurang iodium; kardiomiopati {tt("Penyakit Keshan", "Penyakit Keshan", "Kardiomiopati kongestif endemik.", "Akibat defisiensi selenium.")}; gagal napas diafragma pada {tt("Refeeding syndrome", "Refeeding Syndrome", "Pergeseran fosfat, K, Mg ke intrasel akibat lonjakan insulin.", "Memicu hipofosfatemia berat <1.0 mg/dL.")}.</li>
            </ul>
          </div>
        </div>
      </article>

      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>2. Farmakologi Suplementasi Mineral (Sinergi Kuliah dr. SAN — Modul EMN Hal. 22 &amp; 44)</h3>
            <p>Di Modul Blok EMN, materi mineral diintegrasikan dengan kuliah <b>Farmakologi Suplementasi (SAN)</b>. Hafalkan sediaan, kandungan elemental, dan aturan resep ini:</p>
          </div>
          <span class="brand-tag" style="background:var(--navy);">FARMAKOLOGI RESEP</span>
        </div>

        <div style="overflow-x:auto;">
          <table style="width:100%;border-collapse:collapse;font-size:0.9rem;background:#fff;border:1px solid var(--border);border-radius:10px;overflow:hidden;">
            <thead>
              <tr style="background:var(--surface-subtle);border-bottom:1px solid var(--border);text-align:left;">
                <th style="padding:12px 14px;">Sediaan Obat</th>
                <th style="padding:12px 14px;">Dosis &amp; Kandungan Elemental</th>
                <th style="padding:12px 14px;">Aturan Pakai &amp; Interaksi Obat (Sering Diuji SAN)</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--border);">
                <td style="padding:12px 14px;"><b>Sulfas Ferosus (FeSO4)</b><br><small style="color:var(--ink-muted);">Tablet 300 mg</small></td>
                <td style="padding:12px 14px;">Mengandung <b>{cl("60 mg besi elemental")} (20%)</b>.<br>Fumarat: 33% Fe; Glukonat: 12% Fe.</td>
                <td style="padding:12px 14px;">Minum saat perut kosong + <b>Vitamin C</b> (asam askorbat mereduksi Fe3+ &rarr; Fe2+ agar mudah diserap). <b>Dilarang bareng teh/kopi (tanin), susu/kalsium, antasida, atau antibiotik tetrasiklin/kuinolon!</b></td>
              </tr>
              <tr style="border-bottom:1px solid var(--border);">
                <td style="padding:12px 14px;"><b>Zinc Sulfate / Dispersible</b><br><small style="color:var(--ink-muted);">Tablet 20 mg</small></td>
                <td style="padding:12px 14px;">Bayi &lt;6 bln: <b>{cl("10 mg/hari")}</b><br>Anak &ge;6 bln: <b>{cl("20 mg/hari")}</b></td>
                <td style="padding:12px 14px;">Wajib diberikan <b>selama 10–14 hari penuh</b> pada diare akut anak meskipun diare sudah berhenti, untuk meregenerasi mikrovili usus dan mencegah kekambuhan 2–3 bulan ke depan.</td>
              </tr>
              <tr style="border-bottom:1px solid var(--border);">
                <td style="padding:12px 14px;"><b>Kalsium Glukonas 10% IV</b><br><small style="color:var(--ink-muted);">vs Kalsium Karbonat Oral</small></td>
                <td style="padding:12px 14px;">Ca Glukonas 10% (10 mL) = <b>{cl("93 mg Ca elemental")}</b>.<br>Ca Karbonat = 40% Ca elemental.</td>
                <td style="padding:12px 14px;">Pada tetani/hipokalsemia akut: injeksi Ca Glukonas 10% IV pelan. Untuk oral: <b>Ca Karbonat butuh asam lambung</b> (diminum bersama makan); pada pasien pengguna PPI (omeprazole), pilih <b>Kalsium Sitrat</b>!</td>
              </tr>
              <tr>
                <td style="padding:12px 14px;"><b>Magnesium Sulfat (MgSO4)</b><br><small style="color:var(--ink-muted);">Injeksi IV 20% / 40%</small></td>
                <td style="padding:12px 14px;">Koreksi hipo-Mg berat / Torsades de pointes: <b>{cl("1–2 gram MgSO4 IV")}</b> dalam 15 menit.</td>
                <td style="padding:12px 14px;">Antidotum keracunan MgSO4 (bila refleks patella hilang / depresi napas &lt;16x/menit / oliguria): segera suntikkan <b>{cl("Kalsium Glukonas 10% 10 mL IV")}</b>!</td>
              </tr>
            </tbody>
          </table>
        </div>
      </article>

      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>3. Integrasi Sains, Kedokteran Haji, &amp; Ulul Albab (CPL 14 &amp; 15 Modul FKIK UIN Malang)</h3>
            <p>Menyatukan keluasan ilmu biomedis, kematangan profesional, dan kedalaman spiritual sesuai visi Fakultas:</p>
          </div>
          <span class="brand-tag" style="background:var(--ochre);">ULUL ALBAB &amp; HAJI</span>
        </div>

        <div class="sheet-columns">
          <div class="sheet-pane">
            <h4>Integrasi Al-Qur'an &amp; Sains (CPL 14)</h4>
            <ul>
              <li><b>QS. Al-Hadid [57]: 25 — <i>"Wa anzalnal-hadida fihi ba'sun syadid..."</i></b> (Dan Kami turunkan besi yang padanya terdapat kekuatan hebat dan berbagai manfaat bagi manusia). Secara astrofisika, atom Besi (Fe) tidak bisa diciptakan di bumi melainkan ditempa dari fusi nuklir bintang raksasa (supernova) dan diturunkan ke bumi—dan di tubuh manusia menjadi inti pengikat oksigen kehidupan.</li>
              <li><b>Prinsip <i>Halalan Thayyiban</i> &amp; Gizi Seimbang (QS. Al-Baqarah: 168 &amp; Al-A'raf: 31):</b> Makan tidak berlebihan dan beragam (hewani + nabati) mencegah defisiensi mikromineral akibat diet monoton tinggi fitat.</li>
            </ul>
          </div>
          <div class="sheet-pane">
            <h4>Kedokteran Haji &amp; Umrah (CPL 15 &amp; 16)</h4>
            <ul>
              <li><b>Keringat Masif &amp; Heat Exhaustion di Arafah/Mina:</b> Jemaah haji lansia yang terpapar suhu &gt;45&deg;C mengalami kehilangan cairan dan elektrolit (Na, K, Mg) masif lewat keringat.</li>
              <li><b>Risiko pada Jemaah Pengguna Diuretik/PPI:</b> Jemaah lansia dengan hipertensi/gagal jantung yang minum furosemid sangat rentan jatuh ke dalam <b>hipokalemia &amp; hipomagnesemia refrakter</b> (kram betis hebat saat tawaf/sa'i hingga aritmia jantung). Wajib edukasi hidrasi elektrolit dan evaluasi Mg-K sebelum keberangkatan!</li>
            </ul>
          </div>
        </div>
      </article>
    </div>

    <!-- =================================================================== -->
    <!-- VIEW 5: CBT SUITE (100% BUG FREE & SATISFYING)                      -->
    <!-- =================================================================== -->
    <div id="view-cbt" class="view-section">
      <div class="cbt-anchor">
        <div class="cbt-score-header">
          <div>
            <h2 style="font-family:var(--font-serif);font-size:2rem;color:var(--ink);">8 Soal Prediksi UAB dr. Iwal</h2>
            <p style="font-size:0.92rem;color:var(--ink-secondary);margin-top:2px;">Disusun persis mengikuti karakter kasus klinis (66.7%) dan perbandingan konsep mirip.</p>
          </div>
          <div style="text-align:right;">
            <span style="font-size:0.8rem;color:var(--ink-muted);text-transform:uppercase;letter-spacing:0.04em;">Skor Ujian:</span>
            <div class="score-number"><span id="cbt-score-display">0</span> / 8</div>
          </div>
        </div>

        <div id="cbt-target-list"></div>
      </div>
    </div>
  </main>

  <!-- Lightbox Modal -->
  <div id="modal-lightbox" class="lightbox-backdrop" onclick="closeLightbox()">
    <img id="modal-lightbox-img" class="lightbox-frame" src="" alt="Slide Zoom" onclick="event.stopPropagation()" />
  </div>

  <script>
    // NAVIGATION CONTROLLER
    function switchNav(viewId, btn) {{
      document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
      document.querySelectorAll('.view-pill').forEach(b => b.classList.remove('active'));
      document.getElementById(viewId).classList.add('active');
      btn.classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // CLOZE MASKING CONTROLLER (RESTORED!)
    let clozeActive = false;
    function toggleCloze() {{
      clozeActive = !clozeActive;
      document.body.classList.toggle('cloze-active', clozeActive);
      const btn = document.getElementById('cloze-toggle');
      const tag = document.getElementById('cloze-status-tag');
      if (clozeActive) {{
        btn.classList.add('active');
        tag.textContent = 'ON';
        document.querySelectorAll('.cloze-mask').forEach(el => el.classList.remove('revealed'));
      }} else {{
        btn.classList.remove('active');
        tag.textContent = 'OFF';
      }}
    }}
    document.addEventListener('keydown', e => {{
      if (e.key.toLowerCase() === 'm' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {{
        toggleCloze();
      }}
    }});

    // THE "WHY" ENIGMA REVELATION ENGINE
    const ENIGMAS = {{
      1: {{
        title: "Misteri 01 Terbuka: Refeeding Syndrome",
        text: "Saat seseorang kelaparan &gt;10 hari, sel-sel tubuhnya beralih ke pembakaran lemak dan cadangan fosfat intraselulernya habis total. Ketika kamu memberinya makan (terutama karbohidrat), pankreas langsung memompa <b>lonjakan insulin masif</b>. Insulin ini memaksa seluruh sisa Fosfat, Kalium, dan Magnesium di dalam darah masuk ke dalam sel. Akibatnya, kadar fosfat darah anjlok di bawah 1.0 mg/dL &rarr; sintesis ATP berhenti mendadak &rarr; <b>otot diafragma gagal berkontraksi (gagal napas)</b> dan pasien meninggal di tempat tidur. Niat baikmu membunuh pasien jika kamu tidak tahu cara mencegahnya (Tiamin dulu, mulai kalori 10–15 kkal/kg/hari)."
      }},
      2: {{
        title: "Misteri 02 Terbuka: Pagophagia & Kelaparan Besi di Otak",
        text: "Pasien perempuan 29 tahun dengan menstruasi banyak sering dilaporkan keluarga 'berperilaku aneh' mengunyah es batu berember-ember (<i>pagophagia</i>). Ini bukan gangguan jiwa, melainkan bentuk pica spesifik akibat deplesi atom Besi di mitokondria otak. Sensasi dingin di rongga mulut merangsang vasokonstriksi perifer dan meningkatkan perfusi darah ke lobus frontal otak yang sedang hipoksia. Menariknya, <b>kadar Hb dan MCV pasien saat ini bisa masih normal!</b> Karena yang habis terlebih dahulu adalah <b>Ferritin serum (&lt;15 ng/mL)</b> di sumsum tulang. Begitu kamu beri tablet besi oral, kebiasaan makan es batu itu hilang seketika."
      }},
      3: {{
        title: "Misteri 03 Terbuka: Gerbang ROMK Ginjal yang Bocor",
        text: "Pasien gagal jantung yang rutin minum furosemid sering mengalami aritmia karena kalium darahnya turun. Dokter jaga sering panik dan terus mengguyur KCl infus. Namun kalium darahnya tidak pernah naik. Mengapa? Karena furosemid membuang Kalium <i>sekaligus Magnesium</i>. Di dalam sel tubulus ginjal, ion Magnesium intraseluler adalah <b>sumbat fisik alami kanal ROMK</b>. Bila sumbat Magnesium lepas karena kadarnya rendah (&lt;1.7 mg/dL), gerbang ROMK terbuka lebar tanpa rem &rarr; kalium infus yang kamu masukkan akan langsung bocor terbuang ke urin. Pasien baru bisa selamat jika kamu <b>menginfus Magnesium sulfat bersamaan dengan Kalium</b>."
      }}
    }};

    function openEnigma(id) {{
      const data = ENIGMAS[id];
      const box = document.getElementById('enigma-reveal-box');
      document.getElementById('reveal-title').innerHTML = data.title;
      document.getElementById('reveal-text').innerHTML = data.text;
      box.classList.add('open');
      box.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
    }}

    function closeEnigma() {{
      document.getElementById('enigma-reveal-box').classList.remove('open');
    }}

    // SIMULATOR 1: IRON DEVIATION
    function setIron(stage) {{
      document.querySelectorAll('.stager-btn').forEach((b, i) => {{
        b.classList.toggle('active', i + 1 === stage);
      }});

      const vcF = document.getElementById('vc-ferr');
      const vcT = document.getElementById('vc-tsat');
      const vcH = document.getElementById('vc-hb');
      const valF = document.getElementById('val-ferr');
      const valT = document.getElementById('val-tsat');
      const valH = document.getElementById('val-hb');
      const tagF = document.getElementById('tag-ferr');
      const tagT = document.getElementById('tag-tsat');
      const tagH = document.getElementById('tag-hb');
      const exp = document.getElementById('explainer-iron');

      vcF.classList.remove('active-vial');
      vcT.classList.remove('active-vial');
      vcH.classList.remove('active-vial');

      if (stage === 1) {{
        vcF.classList.add('active-vial');
        valF.textContent = '< 15 ng/mL';
        tagF.textContent = 'ANJLOK DULUAN (Kritis)';
        tagF.className = 'vial-tag tag-danger';

        valT.textContent = '28% (Normal)';
        tagT.textContent = 'Transpor Masih Cukup';
        tagT.className = 'vial-tag tag-safe';

        valH.textContent = 'Hb 13.5 · MCV 88';
        tagH.textContent = 'Tampak Normal (Belum Anemia)';
        tagH.className = 'vial-tag tag-safe';

        exp.innerHTML = '💡 <b>Stadium 1 (Depletion):</b> Cadangan besi hati dan sumsum tulang habis. Tetapi eritrosit baru masih cukup dibuat dari besi sirkulasi. <b>Pasien belum anemia! MCV normal tidak menyingkirkan defisiensi besi!</b>';
      }} else if (stage === 2) {{
        vcT.classList.add('active-vial');
        valF.textContent = '< 10 ng/mL';
        tagF.textContent = 'Kosong';
        tagF.className = 'vial-tag tag-danger';

        valT.textContent = '12% (Anjlok)';
        tagT.textContent = 'Besi Transpor Kurang';
        tagT.className = 'vial-tag tag-danger';

        valH.textContent = 'Hb 12.0 · MCV 82';
        tagH.textContent = 'Batas Bawah Normal';
        tagH.className = 'vial-tag tag-warn';

        exp.innerHTML = '💡 <b>Stadium 2 (Eritropoiesis Terbatas):</b> Besi transferrin tidak cukup untuk kebutuhan sumsum tulang. TSAT anjlok, TIBC meningkat, produksi eritrosit mulai terhambat.';
      }} else {{
        vcH.classList.add('active-vial');
        valF.textContent = '< 7 ng/mL';
        tagF.textContent = 'Habis Total';
        tagF.className = 'vial-tag tag-danger';

        valT.textContent = '6% (Sangat Rendah)';
        tagT.textContent = 'Kritis';
        tagT.className = 'vial-tag tag-danger';

        valH.textContent = 'Hb 8.9 · MCV 68 fL';
        tagH.textContent = 'ANEMIA MIKROSITIK NYATA';
        tagH.className = 'vial-tag tag-danger';

        exp.innerHTML = '💡 <b>Stadium 3 (Anemia Defisiensi Besi):</b> Hb turun, MCV &lt; 80 fL (mikrositik hipokromik). Muncul lemas, pucat, kuku sendok (koilonychia), dan <b>pagophagia (mengunyah es batu)</b>.';
      }}
    }}

    // SIMULATOR 2: ROMK KIDNEY CHANNEL
    function setROMK(isNormal) {{
      document.getElementById('sw-mg-norm').classList.toggle('active', isNormal);
      document.getElementById('sw-mg-low').classList.toggle('active', !isNormal);

      const door = document.getElementById('romk-door');
      const txt = document.getElementById('romk-txt');
      const urine = document.getElementById('romk-urine');

      if (isNormal) {{
        door.className = 'romk-door plugged';
        txt.textContent = '🔒 KANAL ROMK TERSUMBAT (Mg Normal)';
        urine.textContent = 'Kalium aman di darah, tidak bocor ke urin';
        urine.style.color = 'var(--sage)';
      }} else {{
        door.className = 'romk-door leaking';
        txt.textContent = '⚠️ KANAL ROMK TERBUKA LEBAR (Mg Rendah)';
        urine.textContent = '🚨 Kalium BOCOR TERBUANG KE URIN (Hipokalemia Refrakter!)';
        urine.style.color = 'var(--terracotta)';
      }}
    }}

    // MINERAL DECK SELECTOR
    function pickDeck(key, btn) {{
      document.querySelectorAll('.sheet-card').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.deck-item').forEach(b => b.classList.remove('active'));
      document.getElementById('deck-' + key).classList.add('active');
      btn.classList.add('active');
    }}

    // LIGHTBOX CONTROLLER
    function openLightbox(src) {{
      const modal = document.getElementById('modal-lightbox');
      const img = document.getElementById('modal-lightbox-img');
      img.src = src;
      modal.classList.add('open');
    }}
    function closeLightbox() {{
      document.getElementById('modal-lightbox').classList.remove('open');
    }}
    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') closeLightbox();
    }});

    // 8 SOAL PREDIKSI UAB (100% BUG FREE DYNAMIC EVALUATION)
    const CBT_DATA = [
      {{
        id: 1,
        stem: '1. Seorang perempuan 29 tahun datang ke poliklinik dengan keluhan badan lemas dan sering berdebar saat beraktivitas sejak 2 bulan. Pasien memiliki riwayat menstruasi sangat banyak (ganti pembalut 6–7 kali/hari) selama 8 hari setiap siklusnya. Pemeriksaan konjungtiva pucat tanpa ikterus. Laboratorium: Hb 8,9 g/dL, MCV 68 fL, MCH 21 pg. Pasien mengaku sering sekali mengunyah es batu (pagophagia). Pemeriksaan biomarker manakah yang paling sensitif dan paling awal menurun untuk memastikan diagnosis?',
        options: [
          'Total Iron Binding Capacity (TIBC)',
          'Ferritin serum',
          'Saturasi transferrin (TSAT)',
          'Hemoglobin elektroforesis',
          'Bilirubin indirek serum'
        ],
        correct: 1,
        exp: 'Pasien mengalami Anemia Defisiensi Besi akibat menorrhagia kronik. <i>Pagophagia</i> (pica makan es batu) adalah tanda khas defisiensi besi. Pada perjalanan alami penipisan besi (Slide 10), <b>Ferritin serum adalah biomarker pertama yang anjlok (&lt;15–30 ng/mL)</b> mencerminkan habisnya cadangan besi di hati dan sumsum tulang, sebelum nilai Hb dan MCV turun menjadi anemia.'
      }},
      {{
        id: 2,
        stem: '2. Laki-laki 67 tahun dengan gagal jantung kongestif yang rutin mengonsumsi furosemid mengeluh lemas otot tungkai dan berdebar. EKG menunjukkan depresi segmen ST, gelombang T mendatar, dan muncul gelombang U yang menonjol. Hasil laboratorium: Kalium 2,8 mmol/L. Dokter telah memberikan suplementasi KCl oral dosis tinggi selama 3 hari, namun pada evaluasi ulang kadar Kalium pasien tetap rendah (2,9 mmol/L). Gangguan elektrolit penyerta manakah yang mendasari kondisi refrakter tersebut?',
        options: [
          'Hiponatremia',
          'Hipokalsemia',
          'Hipomagnesemia',
          'Hiperfosfatemia',
          'Hiperkalsiuria'
        ],
        correct: 2,
        exp: 'Furosemid membuang Kalium dan Magnesium sekaligus. Di tubulus distal ginjal, ion Magnesium intrasel adalah penghambat fisik alami kanal ROMK. Pada kondisi hipomagnesemia (Slide 17 & 28), kanal ROMK terbuka bebas tanpa kendali sehingga Kalium terus-menerus bocor ke urin. <b>Koreksi Magnesium wajib diberikan bersamaan agar Kalium bisa naik normal.</b>'
      }},
      {{
        id: 3,
        stem: '3. Anak laki-laki 4 tahun dibawa ibunya dengan keluhan bercak kemerahan bersisik dan berkrusta di area sekitar mulut, perineum, serta sela-sela jari kaki sejak 1 bulan. Pasien juga mengalami diare kronik kambuhan dan rambut rontok hingga tampak botak sebagian. Pasien memiliki riwayat diet monoton tinggi serealia dan bubur gandum tanpa asupan hewani. Defisiensi mikromineral apakah yang mendasari kelainan tersebut?',
        options: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Seng (Zinc / Zn)',
          'Selenium (Se)',
          'Mangan (Mn)'
        ],
        correct: 2,
        exp: 'Trias patognomonik: <b>dermatitis periorifisial & akral, diare kronik, dan alopesia</b> merupakan tanda khas defisiensi Seng (Slide 12). Serealia mengandung asam <b>fitat</b> tinggi yang mengikat seng di lumen usus membentuk kelat tak larut yang tidak dapat diserap enterosit.'
      }},
      {{
        id: 4,
        stem: '4. Pasien laki-laki 46 tahun dengan riwayat malnutrisi berat dan kelaparan selama 12 hari dirawat di bangsal. Dokter segera memberikan nutrisi parenteral tinggi karbohidrat. Dalam waktu 48 jam, pasien mendadak mengalami takipnea berat, kelemahan otot menyeluruh, dan aritmia. Gangguan biokimiawi serum manakah yang menjadi pemicu utama kegagalan napas akut tersebut?',
        options: [
          'Hiponatremia berat',
          'Hipokalsemia terionisasi',
          'Hipofosfatemia berat (&lt;1.0 mg/dL)',
          'Asidosis laktat',
          'Hiperglikemia hiperosmolar'
        ],
        correct: 2,
        exp: 'Pasien mengalami <b>Refeeding Syndrome</b> (Slide 19 & 29). Karbohidrat mendadak memicu lonjakan insulin yang mendorong glukosa dan Fosfat masuk masif ke dalam sel &rarr; hipofosfatemia berat (&lt;1.0 mg/dL) menghentikan sintesis ATP seluler, melumpuhkan otot diafragma (gagal napas akut) dan memicu kardiomiopati akut.'
      }},
      {{
        id: 5,
        stem: '5. Perempuan 35 tahun pasca-operasi bypass lambung datang dengan keluhan baal di kedua tungkai serta ataksia sensorik (gangguan jalan). Laboratorium: Hb 9,0 g/dL, MCV 72 fL (mikrositik), dan neutropenia berat (ANC 750/&mu;L). Pasien mengaku mengonsumsi suplemen Zinc dosis tinggi (80 mg/hari) selama 8 bulan. Defisiensi mineral apakah yang paling tepat menjelaskan kondisi pasien?',
        options: [
          'Besi (Fe)',
          'Tembaga (Cu)',
          'Iodium (I)',
          'Selenium (Se)',
          'Kalsium (Ca)'
        ],
        correct: 1,
        exp: 'Kombinasi <b>anemia mikrositik + neutropenia berat + mielopati ataksia</b> adalah tanda klasik defisiensi Tembaga (Slide 22). Suplemen Zinc dosis tinggi menginduksi protein <i>metallothionein</i> di enterosit yang mengikat tembaga dengan kuat dan menghambat absorpsinya ke sirkulasi darah.'
      }},
      {{
        id: 6,
        stem: '6. Berdasarkan pedoman klinis American Gastroenterological Association (AGA 2024), bagaimanakah aturan suplementasi besi oral yang paling tepat dan dapat ditoleransi optimal pada pasien anemia defisiensi besi?',
        options: [
          'Diberikan dosis tinggi 3 kali sehari bersama makanan',
          'Diberikan dosis terbagi setiap 6 jam disertai antasida',
          'Diberikan maksimal 1 kali sehari atau rejimen selang-hari (alternate-day)',
          'Diberikan bersamaan dengan susu sapi segar',
          'Diberikan 4 kali sehari dalam dosis terbagi'
        ],
        correct: 2,
        exp: 'Pedoman AGA 2024 (Slide 11) menekankan bahwa setiap dosis besi oral memicu lonjakan hormon <b>Hepcidin</b> yang memblokade absorpsi berikutnya selama 24–48 jam. Pemberian maksimal 1x/hari atau selang-hari (alternate-day) memaksimalkan penyerapan dan meminimalkan efek samping saluran cerna.'
      }},
      {{
        id: 7,
        stem: '7. Pemeriksaan fisik pada pasien dengan kecurigaan hipokalsemia menunjukkan adanya spasme karpopedal pada tangan ketika manset tensimeter dipompa di atas tekanan sistolik selama 3 menit. Disebut apakah tanda fisik patognomonik tersebut?',
        options: [
          'Chvostek sign',
          'Trousseau sign',
          'Kernig sign',
          'Brudzinski sign',
          'Babinski sign'
        ],
        correct: 1,
        exp: '<b>Tanda Trousseau</b> (spasme karpopedal saat manset dipompa >sistolik 3 menit) sangat sensitif dan spesifik untuk hipokalsemia simptomatik (Slide 15). Tanda Chvostek adalah kedutan bibir saat saraf fasialis diketuk.'
      }},
      {{
        id: 8,
        stem: '8. Wanita hamil di daerah pegunungan yang jarang mengonsumsi garam beriodium melahirkan bayi dengan keterlambatan perkembangan saraf berat, perawakan pendek, dan tuli-bisu. Mekanisme patofisiologi apakah yang mendasari kondisi kretinisme pada bayi tersebut?',
        options: [
          'Kekurangan iodium memicu hambatan sintesis T3/T4 yang vital bagi mielinisasi dan perkembangan otak janin',
          'Kelebihan TSH ibu merusak kelenjar tiroid janin secara langsung',
          'Defisiensi selenium langsung menghambat enzim deiodinase tanpa melibatkan hormon tiroid',
          'Kadar kalsium yang rendah mengganggu pembentukan neurotransmitter otak',
          'Fosfat yang rendah menyebabkan kegagalan pembentukan mielin saraf'
        ],
        correct: 0,
        exp: 'Iodium adalah substrat esensial sintesis hormon tiroid T3/T4 (Slide 13). Pada kehamilan, hormon tiroid mutlak dibutuhkan untuk neurogenesis dan mielinisasi otak janin. Defisiensi berat memicu sindrom kretinisme permanen.'
      }}
    ];

    let userAnswers = {{}};
    let totalScore = 0;

    function renderCBT() {{
      const container = document.getElementById('cbt-target-list');
      container.innerHTML = CBT_DATA.map((q, qIdx) => `
        <article class="q-card-box" id="q-card-${{qIdx}}">
          <span class="q-tag-line">SOAL #${{q.id}} · PREDIKSI UAB DR. IWAL</span>
          <div class="q-stem-body">${{q.stem}}</div>
          <div class="q-options-col">
            ${{q.options.map((opt, oIdx) => `
              <button type="button" class="opt-choice-btn" onclick="selectAnswer(${{qIdx}}, ${{oIdx}})">
                <span class="opt-key-badge">${{String.fromCharCode(65 + oIdx)}}.</span>
                <span>${{opt}}</span>
              </button>
            `).join('')}}
          </div>
          <div class="feedback-sheet" id="fb-sheet-${{qIdx}}"></div>
        </article>
      `).join('');
    }}

    function selectAnswer(qIdx, chosenIdx) {{
      if (userAnswers[qIdx] !== undefined) return;
      userAnswers[qIdx] = chosenIdx;

      const q = CBT_DATA[qIdx];
      const isCorrect = (chosenIdx === q.correct);
      const card = document.getElementById('q-card-' + qIdx);
      const btns = card.querySelectorAll('.opt-choice-btn');
      const sheet = document.getElementById('fb-sheet-' + qIdx);

      btns.forEach((btn, i) => {{
        if (i === q.correct) btn.classList.add('is-correct');
        else if (i === chosenIdx && !isCorrect) btn.classList.add('is-wrong');
      }});

      if (isCorrect) {{
        totalScore++;
        sheet.className = 'feedback-sheet show tone-correct';
        sheet.innerHTML = `<strong>✅ Benar!</strong><div style="margin-top:6px;">${{q.exp}}</div>`;
      }} else {{
        sheet.className = 'feedback-sheet show tone-wrong';
        sheet.innerHTML = `<strong>❌ Kurang Tepat.</strong> Jawaban yang benar adalah <strong>${{String.fromCharCode(65 + q.correct)}} (${{q.options[q.correct]}})</strong>.<div style="margin-top:6px;">${{q.exp}}</div>`;
      }}

      document.getElementById('cbt-score-display').textContent = totalScore;
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      renderCBT();
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(PEER_HTML)

print(f"Modul Peer-Taught Joyful Edition berhasil dibuat di {OUT_HTML} (ukuran: {len(PEER_HTML)} bytes)")
