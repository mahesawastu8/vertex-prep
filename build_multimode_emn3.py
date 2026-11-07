#!/usr/bin/env python3
"""Build Unified Multi-Mode Mastery Module for EMN KUL 3 Defisiensi Mineral.
Provides 4 seamlessly switchable study paradigms for user testing:
1. Mode Kartu Progresif (Step-by-Step Bite-Sized Mastery Flow with Progress Bar & Instant Feedback)
2. Mode Baca Tenang (Editorial Book Handout with AMBOSS Tooltips & Cloze Masking)
3. Mode Jembatan Lintas Blok (Cross-Block Knowledge Bridge)
4. Mode Latihan CBT (8 Soal Vignette dr. Iwal with UWorld Confidence Metrics)
5. Mode Matriks Kilat H-1 (High-Yield Summary Table)
"""
import os
import json

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

def tt(term, title, desc, pearl):
    return f"""<span class="med-term" tabindex="0">{term}<span class="med-tooltip"><span class="tt-kicker">Catatan Klinis</span><span class="tt-title">{title}</span><span class="tt-desc">{desc}</span><span class="tt-pearl">💡 {pearl}</span></span></span>"""

def cl(text):
    return f"""<span class="cloze-mask" onclick="this.classList.toggle('revealed')" title="Klik untuk membuka">{text}</span>"""

HTML_CODE = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Mineral · Sistem Belajar Terpadu EMN</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=JetBrains+Mono:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #FAF8F5;
      --surface: #FFFFFF;
      --surface-subtle: #F5F3EC;
      --border: #E8E5DC;
      --border-dark: #D4D0C5;
      
      --ink: #1F2022;
      --ink-secondary: #585A5E;
      --ink-muted: #8E9094;
      
      --sage: #2D6A4F;
      --sage-light: #EBF4EF;
      --coral: #C84B31;
      --coral-light: #FBEFEA;
      --ochre: #B87333;
      --ochre-light: #FAF2EA;
      --navy: #1D3557;
      --navy-light: #EDF2F7;
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --radius-full: 999px;
      
      --shadow-sm: 0 1px 3px rgba(31, 32, 34, 0.04);
      --shadow-md: 0 4px 12px rgba(31, 32, 34, 0.06);
      --shadow-lg: 0 16px 36px rgba(31, 32, 34, 0.09);
      
      --font-serif: 'Newsreader', Georgia, serif;
      --font-sans: 'IBM Plex Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
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
      padding-bottom: 90px;
    }}

    ::selection {{ background: #D8EADF; color: #1F2022; }}

    /* Top Sticky Navigation */
    .top-nav {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(250, 248, 245, 0.94);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 10px 24px;
    }}
    .nav-inner {{
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .brand-pill {{
      background: var(--navy);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 6px;
      letter-spacing: 0.04em;
    }}
    .nav-course {{
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      color: var(--ink);
      background: transparent;
      border: none;
      cursor: pointer;
      outline: none;
    }}

    /* Mode Segmented Controls */
    .mode-bar {{
      display: flex;
      background: rgba(232, 229, 220, 0.65);
      padding: 3px;
      border-radius: var(--radius-full);
      gap: 2px;
    }}
    .mode-btn {{
      border: none;
      background: transparent;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--ink-secondary);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.18s ease;
      white-space: nowrap;
    }}
    .mode-btn:hover {{ color: var(--ink); }}
    .mode-btn.active {{
      background: var(--surface);
      color: var(--ink);
      box-shadow: var(--shadow-sm);
    }}

    .nav-actions {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .btn-toggle {{
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--ink-secondary);
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: var(--radius-full);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.15s ease;
    }}
    .btn-toggle:hover {{ border-color: var(--sage); color: var(--ink); }}
    .btn-toggle.active {{ background: var(--ink); color: #fff; border-color: var(--ink); }}
    .badge-status {{
      font-family: var(--font-mono);
      font-size: 0.7rem;
      padding: 1px 6px;
      border-radius: 4px;
      background: var(--bg);
      color: var(--ink);
    }}
    .btn-toggle.active .badge-status {{ background: var(--sage); color: #fff; }}

    .btn-anki {{
      background: var(--sage);
      color: #fff;
      font-family: var(--font-sans);
      font-size: 0.8rem;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: var(--radius-full);
      text-decoration: none;
      transition: opacity 0.15s ease;
    }}
    .btn-anki:hover {{ opacity: 0.9; }}

    /* Layout Shell */
    .shell {{
      max-width: 840px;
      margin: 0 auto;
      padding: 36px 20px 0;
    }}

    .pane-view {{ display: none; }}
    .pane-view.active {{ display: block; }}

    /* =========================================================================
       MODE 1: PROGRESSIVE STEP-BY-STEP MASTERY CARD FLOW
       ========================================================================= */
    .flow-progress-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 24px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .progress-meta-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
      font-size: 0.85rem;
    }}
    .progress-step-lbl {{ font-weight: 700; color: var(--sage); }}
    .progress-count-lbl {{ color: var(--ink-secondary); font-family: var(--font-mono); font-size: 0.8rem; }}
    .progress-bar-bg {{
      height: 6px;
      background: var(--surface-subtle);
      border-radius: var(--radius-full);
      overflow: hidden;
    }}
    .progress-bar-fill {{
      height: 100%;
      background: var(--sage);
      width: 14.28%;
      border-radius: var(--radius-full);
      transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    /* Card Step Container */
    .step-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px 36px;
      box-shadow: var(--shadow-sm);
      display: none;
      animation: cardIn 0.25s ease-out;
    }}
    .step-card.active {{ display: block; }}
    @keyframes cardIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    .step-header {{
      margin-bottom: 24px;
      padding-bottom: 18px;
      border-bottom: 1px solid var(--border);
    }}
    .step-kicker {{
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--sage);
      letter-spacing: 0.05em;
      text-transform: uppercase;
      margin-bottom: 4px;
    }}
    .step-title {{
      font-family: var(--font-serif);
      font-size: 2rem;
      font-weight: 700;
      line-height: 1.25;
      color: var(--ink);
    }}

    .concept-unit {{
      margin-bottom: 24px;
    }}
    .unit-heading {{
      font-size: 0.92rem;
      font-weight: 700;
      color: var(--ink);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      gap: 8px;
    }}
    .unit-box {{
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      font-size: 0.96rem;
      line-height: 1.68;
      color: #2D2F33;
    }}

    .trap-box {{
      background: var(--coral-light);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-top: 14px;
    }}
    .trap-title {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--coral);
      margin-bottom: 4px;
    }}
    .trap-body {{
      font-size: 0.94rem;
      line-height: 1.6;
      color: #3D1C17;
    }}

    /* Quick Active Challenge */
    .challenge-box {{
      background: #FFFFFF;
      border: 1px solid var(--border-dark);
      border-radius: var(--radius-md);
      padding: 22px;
      margin-top: 24px;
    }}
    .challenge-q {{
      font-size: 0.98rem;
      font-weight: 600;
      color: var(--ink);
      margin-bottom: 14px;
      line-height: 1.5;
    }}
    .challenge-options {{
      display: flex;
      flex-direction: column;
      gap: 8px;
    }}
    .ch-btn {{
      padding: 10px 14px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      background: var(--surface);
      text-align: left;
      font-family: var(--font-sans);
      font-size: 0.92rem;
      color: var(--ink);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .ch-btn:hover {{ background: #F8F6F0; border-color: #BDB7AB; }}
    .ch-btn.is-correct {{ background: var(--sage-light); border-color: var(--sage); color: #174230; font-weight: 600; }}
    .ch-btn.is-wrong {{ background: var(--coral-light); border-color: var(--coral); color: #7A2818; }}
    
    .challenge-feedback {{
      margin-top: 12px;
      padding: 12px 14px;
      background: #F4F1EA;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      line-height: 1.55;
      display: none;
    }}
    .challenge-feedback.show {{ display: block; }}

    /* Step Navigation Buttons */
    .step-actions {{
      margin-top: 28px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .btn-nav {{
      padding: 10px 20px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 0.88rem;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.18s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .btn-nav-prev {{
      border: 1px solid var(--border);
      background: var(--surface);
      color: var(--ink-secondary);
    }}
    .btn-nav-prev:hover {{ border-color: var(--ink); color: var(--ink); }}
    .btn-nav-next {{
      border: none;
      background: var(--sage);
      color: #fff;
    }}
    .btn-nav-next:hover {{ opacity: 0.9; transform: translateY(-1px); }}

    /* Completion View */
    .completion-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 44px 36px;
      text-align: center;
      display: none;
      box-shadow: var(--shadow-sm);
    }}
    .completion-card.active {{ display: block; }}
    .comp-badge {{
      display: inline-block;
      font-size: 2.2rem;
      margin-bottom: 12px;
    }}
    .comp-title {{
      font-family: var(--font-serif);
      font-size: 2.2rem;
      font-weight: 700;
      color: var(--ink);
      margin-bottom: 10px;
    }}
    .comp-desc {{
      max-width: 540px;
      margin: 0 auto 24px;
      color: var(--ink-secondary);
      font-size: 1rem;
    }}

    /* =========================================================================
       SHARED EDITORIAL STYLES (MODE 2 & OTHERS)
       ========================================================================= */
    .article-header {{ margin-bottom: 48px; }}
    .meta-tag {{
      display: inline-block;
      font-size: 0.8rem;
      font-weight: 600;
      color: var(--sage);
      background: var(--sage-light);
      padding: 3px 10px;
      border-radius: var(--radius-full);
      margin-bottom: 14px;
    }}
    .article-title {{
      font-family: var(--font-serif);
      font-size: 2.5rem;
      font-weight: 700;
      line-height: 1.25;
      color: var(--ink);
      letter-spacing: -0.015em;
      margin-bottom: 14px;
    }}
    .article-subtitle {{
      font-size: 1.08rem;
      color: var(--ink-secondary);
      line-height: 1.6;
    }}
    .chapter-section {{ margin-bottom: 52px; }}
    .chapter-title {{
      font-family: var(--font-serif);
      font-size: 1.65rem;
      font-weight: 600;
      color: var(--ink);
      margin-bottom: 14px;
      padding-bottom: 8px;
      border-bottom: 1px solid var(--border);
    }}

    .callout-pearl {{
      background: var(--ochre-light);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 22px 0;
    }}
    .callout-title {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ochre);
      margin-bottom: 6px;
    }}
    .callout-body {{ font-size: 0.94rem; line-height: 1.65; color: #3A2E1D; }}

    .callout-danger {{
      background: var(--coral-light);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin: 22px 0;
    }}
    .danger-title {{
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--coral);
      margin-bottom: 6px;
    }}
    .danger-body {{ font-size: 0.94rem; line-height: 1.65; color: #3B1C16; }}

    .table-wrap {{
      overflow-x: auto;
      margin: 22px 0;
      background: var(--surface);
      border-radius: var(--radius-md);
      border: 1px solid var(--border);
    }}
    .reading-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      line-height: 1.5;
    }}
    .reading-table th {{
      background: #F5F3EC;
      text-align: left;
      padding: 12px 16px;
      font-weight: 600;
      color: var(--ink);
      border-bottom: 1px solid var(--border);
    }}
    .reading-table td {{
      padding: 14px 16px;
      border-bottom: 1px solid var(--border);
      vertical-align: top;
      color: #2D2F33;
    }}
    .reading-table tr:last-child td {{ border-bottom: none; }}

    .slide-evidence {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px;
      margin: 20px 0;
      display: flex;
      align-items: center;
      gap: 16px;
      cursor: pointer;
      transition: all 0.18s ease;
    }}
    .slide-evidence:hover {{
      border-color: var(--sage);
      box-shadow: var(--shadow-sm);
      transform: translateY(-1px);
    }}
    .evidence-thumb {{
      width: 96px;
      height: 60px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
      flex: none;
    }}
    .evidence-num {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 600;
      color: var(--sage);
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}
    .evidence-title {{
      font-size: 0.92rem;
      font-weight: 600;
      color: var(--ink);
      margin-top: 2px;
    }}
    .evidence-hint {{
      font-size: 0.8rem;
      color: var(--ink-muted);
      margin-top: 2px;
    }}

    /* Tooltip styling */
    .med-term {{
      border-bottom: 1.5px dotted var(--navy);
      color: var(--navy);
      font-weight: 600;
      cursor: help;
      position: relative;
      display: inline-block;
    }}
    .med-tooltip {{
      visibility: hidden;
      opacity: 0;
      position: absolute;
      bottom: 135%;
      left: 50%;
      transform: translateX(-50%) translateY(4px);
      width: 290px;
      background: #1A1A1A;
      color: #FFFFFF;
      border-radius: var(--radius-md);
      padding: 14px 16px;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 400;
      line-height: 1.5;
      box-shadow: var(--shadow-lg);
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
      border-color: #1A1A1A transparent transparent transparent;
    }}
    .med-term:hover .med-tooltip,
    .med-term:focus .med-tooltip {{
      visibility: visible;
      opacity: 1;
      transform: translateX(-50%) translateY(0);
    }}
    .tt-kicker {{ font-size: 0.68rem; font-weight: 700; color: #A3D9C9; text-transform: uppercase; display: block; margin-bottom: 2px; }}
    .tt-title {{ font-size: 0.92rem; font-weight: 700; color: #FFFFFF; margin-bottom: 4px; display: block; }}
    .tt-desc {{ color: #D6D6D6; display: block; }}
    .tt-pearl {{ margin-top: 8px; padding-top: 8px; border-top: 1px solid #333; color: #F8E7C9; font-size: 0.78rem; display: block; }}

    /* Active Cloze Mask */
    body.cloze-active .cloze-mask {{
      background: #E8E5DC !important;
      color: transparent !important;
      border-radius: 4px;
      padding: 1px 6px;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
      display: inline-block;
    }}
    body.cloze-active .cloze-mask:hover {{ background: #D8D4C8 !important; }}
    body.cloze-active .cloze-mask.revealed {{
      background: var(--sage-light) !important;
      color: var(--sage) !important;
      font-weight: 600;
      padding: 1px 6px;
      border-radius: 4px;
    }}

    /* CBT styles */
    .diag-dashboard {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px 24px;
      margin-bottom: 28px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      box-shadow: var(--shadow-sm);
    }}
    .diag-card {{ display: flex; flex-direction: column; }}
    .diag-val {{ font-family: var(--font-mono); font-size: 1.5rem; font-weight: 700; line-height: 1.2; }}
    .diag-lbl {{ font-size: 0.78rem; color: var(--ink-secondary); margin-top: 4px; }}

    .q-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-sm);
    }}
    .q-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }}
    .q-number {{ font-family: var(--font-mono); font-size: 0.8rem; font-weight: 600; color: var(--ink-muted); }}
    .confidence-picker {{ display: flex; align-items: center; gap: 8px; font-size: 0.8rem; color: var(--ink-secondary); }}
    .conf-btn {{
      border: 1px solid var(--border);
      background: transparent;
      padding: 4px 10px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 0.78rem;
      font-weight: 600;
      cursor: pointer;
      color: var(--ink-secondary);
      transition: all 0.15s ease;
    }}
    .conf-btn.active-high {{ background: var(--sage); color: #fff; border-color: var(--sage); }}
    .conf-btn.active-low {{ background: var(--ochre); color: #fff; border-color: var(--ochre); }}

    .q-stem {{ font-size: 1.02rem; font-weight: 500; line-height: 1.7; color: var(--ink); margin-bottom: 20px; }}
    .q-options-stack {{ display: flex; flex-direction: column; gap: 8px; }}
    .opt-choice {{
      padding: 12px 16px;
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      background: var(--surface);
      text-align: left;
      font-family: var(--font-sans);
      font-size: 0.94rem;
      color: var(--ink);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.15s ease;
    }}
    .opt-choice:hover {{ background: #FAF8F5; border-color: #BDB7AB; }}
    .opt-key-txt {{ font-family: var(--font-mono); font-weight: 600; color: var(--ink-muted); flex: none; }}
    .opt-choice.is-correct {{ background: var(--sage-light); border-color: var(--sage); color: #174230; font-weight: 600; }}
    .opt-choice.is-wrong {{ background: var(--coral-light); border-color: var(--coral); color: #7A2818; }}

    .q-explanation-box {{
      margin-top: 20px;
      padding: 18px 20px;
      background: #F7F5EE;
      border-radius: var(--radius-sm);
      font-size: 0.92rem;
      line-height: 1.65;
      display: none;
    }}
    .q-explanation-box.show {{ display: block; }}
    .outcome-pill {{ display: inline-block; font-size: 0.78rem; font-weight: 700; padding: 2px 10px; border-radius: var(--radius-full); margin-bottom: 10px; }}
    .pill-mastered {{ background: var(--sage-light); color: var(--sage); }}
    .pill-lucky {{ background: var(--ochre-light); color: var(--ochre); }}
    .pill-danger {{ background: var(--coral-light); color: var(--coral); }}
    .pill-gap {{ background: var(--navy-light); color: var(--navy); }}

    /* Bridge Styles */
    .bridge-card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 28px;
      margin-bottom: 24px;
    }}
    .bridge-tabs {{ display: flex; gap: 8px; flex-wrap: wrap; margin: 20px 0 24px; padding-bottom: 14px; border-bottom: 1px solid var(--border); }}
    .bridge-tab-btn {{
      background: transparent;
      border: 1px solid var(--border);
      padding: 6px 14px;
      border-radius: var(--radius-full);
      font-family: var(--font-sans);
      font-size: 0.85rem;
      font-weight: 600;
      color: var(--ink-secondary);
      cursor: pointer;
      transition: all 0.15s ease;
    }}
    .bridge-tab-btn:hover {{ border-color: var(--ink); color: var(--ink); }}
    .bridge-tab-btn.active {{ background: var(--navy); color: #fff; border-color: var(--navy); }}
    .bridge-pane {{ display: none; }}
    .bridge-pane.active {{ display: block; }}
    .bridge-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; margin-top: 16px; }}
    .bridge-box {{ background: #FAF8F5; border: 1px solid var(--border); border-radius: var(--radius-sm); padding: 18px; }}
    .bridge-tag {{ display: inline-block; font-size: 0.72rem; font-weight: 700; padding: 2px 8px; border-radius: 4px; margin-bottom: 8px; }}
    .tag-emn {{ background: var(--sage-light); color: var(--sage); }}
    .tag-bms {{ background: var(--navy-light); color: var(--navy); }}
    .tag-hi  {{ background: var(--coral-light); color: var(--coral); }}
    .tag-bdt {{ background: var(--ochre-light); color: var(--ochre); }}

    /* Lightbox Modal */
    .lightbox-modal {{
      position: fixed; inset: 0; z-index: 1000; background: rgba(26, 26, 26, 0.78);
      backdrop-filter: blur(8px); display: none; align-items: center; justify-content: center; padding: 24px;
    }}
    .lightbox-modal.open {{ display: flex; }}
    .lightbox-img {{ max-width: 90%; max-height: 85vh; border-radius: 8px; box-shadow: var(--shadow-lg); }}

    @media (max-width: 768px) {{
      .article-title {{ font-size: 2rem; }}
      .step-title {{ font-size: 1.6rem; }}
      .diag-dashboard {{ grid-template-columns: 1fr 1fr; }}
      .mode-bar {{ display: none; }}
    }}
  </style>
</head>
<body>

  <!-- Top Sticky Navigation Bar -->
  <header class="top-nav">
    <div class="nav-inner">
      <div class="nav-brand">
        <span class="brand-pill">EMN 3</span>
        <select class="nav-course" onchange="window.location.href=this.value">
          <option value="EMN_KUL3_Defisiensi_Mineral.html" selected>Defisiensi Mineral (dr. Iwal, Sp.PD)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html">Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
          <option value="BDT_KUL3_Patient_Safety.html">Patient Safety (dr. Riskiyah)</option>
        </select>
      </div>

      <!-- 4 Mode Belajar Switcher -->
      <nav class="mode-bar">
        <button type="button" class="mode-btn active" onclick="switchMainPane('pane-flow', this)">1. Kartu Progresif</button>
        <button type="button" class="mode-btn" onclick="switchMainPane('pane-reading', this)">2. Baca Tenang</button>
        <button type="button" class="mode-btn" onclick="switchMainPane('pane-bridge', this)">3. Jembatan Blok</button>
        <button type="button" class="mode-btn" onclick="switchMainPane('pane-cbt', this)">4. Latihan CBT (8)</button>
        <button type="button" class="mode-btn" onclick="switchMainPane('pane-flash', this)">5. Matriks H-1</button>
      </nav>

      <div class="nav-actions">
        <button type="button" id="cloze-toggle" class="btn-toggle" onclick="toggleCloze()" title="Shortcut tombol M">
          <span>Uji Ingatan</span>
          <span class="badge-status" id="cloze-status">OFF</span>
        </button>
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-anki" download>Deck Anki</a>
      </div>
    </div>
  </header>

  <main class="shell">

    <!-- =================================================================== -->
    <!-- MODE 1: KARTU PROGRESIF (STEP-BY-STEP MASTERY DECK)                 -->
    <!-- =================================================================== -->
    <div id="pane-flow" class="pane-view active">
      
      <!-- Flow Progress Tracker -->
      <div class="flow-progress-card">
        <div class="progress-meta-row">
          <span class="progress-step-lbl" id="flow-step-label">Langkah 1 dari 7 · Besi (Fe) &amp; Anemia Mikrositik</span>
          <span class="progress-count-lbl" id="flow-percent-label">14% Dikuasai</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="flow-progress-bar"></div>
        </div>
      </div>

      <!-- STEP 1: BESI -->
      <div class="step-card active" id="sc-1">
        <div class="step-header">
          <div class="step-kicker">Langkah 01 / 07 · Slide 9, 10, 11</div>
          <h2 class="step-title">Besi (Fe): 3 Stadium Penipisan &amp; Pedoman AGA 2024</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            Besi diserap di duodenum dan diatur oleh hormon <b>Hepcidin</b> hati. Bila terjadi perdarahan kronik (seperti menorrhagia) atau malabsorpsi, besi habis dalam <b>3 stadium berurutan</b>:<br>
            <b>1. Cadangan Turun:</b> {cl("Ferritin &lt;15–30 ng/mL")} turun duluan! Hb dan MCV masih normal.<br>
            <b>2. Eritropoiesis Terbatas:</b> TSAT &lt;16–20%, TIBC meningkat. Produksi eritrosit mulai terhambat.<br>
            <b>3. Anemia Defisiensi Besi:</b> Hb turun, MCV &lt;80 fL (mikrositik hipokromik), timbul <b>pagophagia (mengunyah es batu)</b> dan kuku sendok (koilonychia).
          </div>

          <div class="trap-box">
            <div class="trap-title">Jebakan Ujian UAB dr. Iwal (Pedoman AGA 2024)</div>
            <div class="trap-body">
              <b>Jangan beri tablet besi oral 3x sehari!</b> Setiap asupan besi memicu lonjakan hepcidin selama 24–48 jam yang memblokir penyerapan besi berikutnya. Rekomendasi mutakhir: <b>{cl("Maksimal 1x/hari pagi hari atau selang-hari (alternate-day)")}</b>.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_10.jpg')">
            <img src="slides_kul3/slide_10.jpg" class="evidence-thumb" alt="Slide 10" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 10 &amp; 11</span>
              <div class="evidence-title">Perjalanan Defisiensi Besi: Ferritin Turun Lebih Awal</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <!-- Quick Challenge -->
          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Manakah biomarker yang paling awal turun saat cadangan besi mulai habis sebelum terjadi anemia?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(1, 0, false)">A. Hemoglobin (Hb)</button>
              <button class="ch-btn" onclick="checkStepChallenge(1, 1, false)">B. Mean Corpuscular Volume (MCV)</button>
              <button class="ch-btn" onclick="checkStepChallenge(1, 2, true)">C. Ferritin serum</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-1">
              <b>Tepat!</b> Ferritin mencerminkan cadangan intraseluler dan anjlok di stadium 1 saat Hb dan MCV masih normal.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <span></span>
          <button type="button" class="btn-nav btn-nav-next" onclick="goToStep(2)">Lanjut ke Langkah 2: Seng (Zn) →</button>
        </div>
      </div>

      <!-- STEP 2: SENG -->
      <div class="step-card" id="sc-2">
        <div class="step-header">
          <div class="step-kicker">Langkah 02 / 07 · Slide 12</div>
          <h2 class="step-title">Seng (Zn): Trias Gejala Khas &amp; Bahaya Asam Fitat</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            Seng adalah kofaktor &gt;300 metalloenzim dan protein <i>zinc fingers</i> untuk pembelahan sel epitel dan imunitas. Defisiensi berat memunculkan trias klinis patognomonik:<br>
            • <b>{cl("Dermatitis periorifisial &amp; akral")}</b> (ruam krusta di sekitar mulut, anus, ujung jari).<br>
            • <b>Diare kronik</b> (akibat atrofi mikrovili usus).<br>
            • <b>Alopesia</b> (rambut rontok) dan gangguan penyembuhan luka / hipogeusia.
          </div>

          <div class="trap-box">
            <div class="trap-title">Penyebab Malabsorpsi Kunci di Soal Kasus</div>
            <div class="trap-body">
              Diet tinggi <b>{cl("asam fitat")}</b> (serealia/gandum tak beragi) mengikat seng membentuk kelat tak larut di usus. Bayi dengan gejala trias di atas memiliki kelainan herediter <b>Acrodermatitis enteropathica</b> (mutasi transporter ZIP4).
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_12.jpg')">
            <img src="slides_kul3/slide_12.jpg" class="evidence-thumb" alt="Slide 12" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 12</span>
              <div class="evidence-title">Seng (Zn): Pertumbuhan, Kulit, Imunitas &amp; Peran Fitat</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Manakah senyawa pada makanan nabati serealia yang paling kuat menghambat penyerapan seng di usus?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(2, 0, true)">A. Asam fitat</button>
              <button class="ch-btn" onclick="checkStepChallenge(2, 1, false)">B. Vitamin C</button>
              <button class="ch-btn" onclick="checkStepChallenge(2, 2, false)">C. Asam folat</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-2">
              <b>Benar!</b> Fitat membentuk kompleks tak larut dengan Zn di pH duodenum.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <button type="button" class="btn-nav btn-nav-prev" onclick="goToStep(1)">← Kembali</button>
          <button type="button" class="btn-nav btn-nav-next" onclick="goToStep(3)">Lanjut ke Langkah 3: Magnesium →</button>
        </div>
      </div>

      <!-- STEP 3: MAGNESIUM & KALIUM -->
      <div class="step-card" id="sc-3">
        <div class="step-header">
          <div class="step-kicker">Langkah 03 / 07 · Slide 16, 17, 28</div>
          <h2 class="step-title">Magnesium (Mg): Mengapa Kalium Susah Naik Bila Mg Rendah?</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            Pada pasien hipokalemia (lemas otot, EKG gelombang U) yang gagal naik meski sudah diberi KCl berulang kali, <b>penyebab utamanya adalah hipomagnesemia tersembunyi</b> ({cl("&lt;1.7 mg/dL")}).<br><br>
            <b>Rantai Regulasi Ginjal:</b> Magnesium intrasel adalah penghambat alami kanal {cl("ROMK")} di tubulus distal. Bila Mg anjlok &rarr; kanal ROMK terbuka lebar tanpa hambatan &rarr; <b>Kalium bocor masif ke urin</b>.<br>
            <b>Prinsip Terapi:</b> {cl("Wajib koreksi Magnesium bersamaan dengan Kalium!")}
          </div>

          <div class="trap-box">
            <div class="trap-title">Pemicu Hipomagnesemia Paling Sering di Bangsal</div>
            <div class="trap-body">
              Penggunaan <b>diuretik loop (furosemid)</b> jangka panjang, pemakaian obat maag <b>PPI (omeprazole) menahun</b>, diare kronik, dan alkoholisme.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_17.jpg')">
            <img src="slides_kul3/slide_17.jpg" class="evidence-thumb" alt="Slide 17" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 17 &amp; 28</span>
              <div class="evidence-title">Patofisiologi Ekskresi K Renal Akibat Defisiensi Mg</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Kanal ginjal manakah yang mengalami disinhibisi saat kadar magnesium intrasel rendah sehingga memicu hipokalemia refrakter?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(3, 0, false)">A. ENaC</button>
              <button class="ch-btn" onclick="checkStepChallenge(3, 1, true)">B. ROMK</button>
              <button class="ch-btn" onclick="checkStepChallenge(3, 2, false)">C. SGLT-2</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-3">
              <b>Tepat!</b> Renal Outer Medullary Potassium (ROMK) channel bocor bila Mg intrasel kurang.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <button type="button" class="btn-nav btn-nav-prev" onclick="goToStep(2)">← Kembali</button>
          <button type="button" class="btn-nav btn-nav-next" onclick="goToStep(4)">Lanjut ke Langkah 4: Fosfat &amp; Refeeding →</button>
        </div>
      </div>

      <!-- STEP 4: FOSFAT & REFEEDING -->
      <div class="step-card" id="sc-4">
        <div class="step-header">
          <div class="step-kicker">Langkah 04 / 07 · Slide 18, 19, 29</div>
          <h2 class="step-title">Fosfat (P): Refeeding Syndrome &amp; Kelumpuhan Diafragma</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            Terjadi bila pasien malnutrisi berat/puasa lama (&gt;7–10 hari) tiba-tiba diberi <b>nutrisi karbohidrat agresif</b>:<br>
            Karbohidrat masuk &rarr; Pankreas sekresi <b>Insulin masif</b> &rarr; Insulin memaksa glukosa, <b>Fosfat (P), Kalium, dan Mg masuk ke dalam sel</b> &rarr; <b>Hipofosfatemia berat ({cl("&lt;1.0 mg/dL")})</b> di plasma &rarr; Sintesis ATP seluler lumpuh &rarr; <b>Gagal napas akut (otot diafragma lumpuh)</b> dan aritmia fatal.
          </div>

          <div class="trap-box">
            <div class="trap-title">Protokol Pencegahan ASPEN / NICE (Slide 19)</div>
            <div class="trap-body">
              1. Berikan <b>Tiamin (B1) sebelum nutrisi dimulai</b>.<br>
              2. Mulai kalori sangat rendah bertahap: <b>{cl("10–15 kkal/kg/hari")}</b>.<br>
              3. Pantau serial fosfat, kalium, dan magnesium tiap 24 jam.
            </div>
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_19.jpg')">
            <img src="slides_kul3/slide_19.jpg" class="evidence-thumb" alt="Slide 19" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 19 &amp; 29</span>
              <div class="evidence-title">Bagan Alir Patofisiologi Refeeding Syndrome ASPEN 2020</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Hormon manakah yang memicu pergeseran masif fosfat ke intrasel pada Refeeding Syndrome?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(4, 0, false)">A. Kortisol</button>
              <button class="ch-btn" onclick="checkStepChallenge(4, 1, true)">B. Insulin</button>
              <button class="ch-btn" onclick="checkStepChallenge(4, 2, false)">C. Glukagon</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-4">
              <b>Benar!</b> Lonjakan insulin mendorong glukosa dan fosfat masuk sel secara serentak.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <button type="button" class="btn-nav btn-nav-prev" onclick="goToStep(3)">← Kembali</button>
          <button type="button" class="btn-nav btn-nav-next" onclick="goToStep(5)">Lanjut ke Langkah 5: Kalsium →</button>
        </div>
      </div>

      <!-- STEP 5: KALSIUM -->
      <div class="step-card" id="sc-5">
        <div class="step-header">
          <div class="step-kicker">Langkah 05 / 07 · Slide 14, 15</div>
          <h2 class="step-title">Kalsium (Ca): Hipokalsemia, Tanda Fisik, &amp; EKG</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            Hanya <b>kalsium ionisasi bebas (50%)</b> yang aktif secara fisiologis. Bila kadar kalsium ion anjlok, permeabilitas natrium membran saraf meningkat drastis &rarr; hipereksitabilitas neuromuskular (tetani).<br>
            • <b>Parestesia:</b> Kesemutan di sekitar mulut (perioral) dan ujung jari.<br>
            • <b>Tanda Chvostek:</b> Kedutan bibir saat saraf fasialis diketuk anterior telinga.<br>
            • <b>Tanda Trousseau:</b> Spasme karpopedal saat manset tensimeter dipompa &gt;sistolik 3 menit.<br>
            • <b>EKG:</b> {cl("Interval QT memanjang")}, risiko aritmia ventrikel.
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_15.jpg')">
            <img src="slides_kul3/slide_15.jpg" class="evidence-thumb" alt="Slide 15" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 15</span>
              <div class="evidence-title">Hipokalsemia Simptomatik &amp; Pemeriksaan Kalsium Terionisasi</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Tanda fisik spesifik spasme karpopedal yang timbul saat manset tensimeter dipompa selama 3 menit disebut tanda apa?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(5, 0, false)">A. Chvostek sign</button>
              <button class="ch-btn" onclick="checkStepChallenge(5, 1, true)">B. Trousseau sign</button>
              <button class="ch-btn" onclick="checkStepChallenge(5, 2, false)">C. Babinski sign</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-5">
              <b>Tepat!</b> Tanda Trousseau sangat spesifik untuk hipokalsemia simptomatik.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <button type="button" class="btn-nav btn-nav-prev" onclick="goToStep(4)">← Kembali</button>
          <button type="button" class="btn-nav btn-nav-next" onclick="goToStep(6)">Lanjut ke Langkah 6: Tembaga (Cu) →</button>
        </div>
      </div>

      <!-- STEP 6: TEMBAGA -->
      <div class="step-card" id="sc-6">
        <div class="step-header">
          <div class="step-kicker">Langkah 06 / 07 · Slide 22</div>
          <h2 class="step-title">Tembaga (Cu): Anemia + Neutropenia &amp; Jebakan Zinc</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            Tembaga adalah kofaktor enzim <i>ceruloplasmin</i> (ferroksidase transpor besi). Defisiensi tembaga bermanifestasi khas sebagai trias: <b>{cl("Anemia mikrositik + Neutropenia berat + Mielopati ataksia")}</b> (mirip defisiensi vitamin B12).<br><br>
            <b>Pemicu Iatrogenik Utama:</b> Konsumsi suplemen <b>Seng (Zinc) dosis tinggi (&gt;50 mg/hari)</b> jangka panjang. Seng menginduksi protein <i>metallothionein</i> di sel usus yang mengikat tembaga dan membuangnya keluar tubuh!
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_22.jpg')">
            <img src="slides_kul3/slide_22.jpg" class="evidence-thumb" alt="Slide 22" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 22</span>
              <div class="evidence-title">Tembaga (Cu) &amp; Interaksi Kompetitif dengan Seng</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Pasien dengan anemia mikrositik dan neutropenia berat yang rutin minum suplemen seng dosis tinggi mengalami defisiensi apa?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(6, 0, false)">A. Kobalamin (B12)</button>
              <button class="ch-btn" onclick="checkStepChallenge(6, 1, true)">B. Tembaga (Cu)</button>
              <button class="ch-btn" onclick="checkStepChallenge(6, 2, false)">C. Selenium (Se)</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-6">
              <b>Benar!</b> Zinc berlebih menghambat penyerapan Cu via induksi metallothionein.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <button type="button" class="btn-nav btn-nav-prev" onclick="goToStep(5)">← Kembali</button>
          <button type="button" class="btn-nav btn-nav-next" onclick="goToStep(7)">Lanjut ke Langkah 7: Iodium &amp; Se →</button>
        </div>
      </div>

      <!-- STEP 7: IODIUM & SELENIUM -->
      <div class="step-card" id="sc-7">
        <div class="step-header">
          <div class="step-kicker">Langkah 07 / 07 · Slide 13, 23</div>
          <h2 class="step-title">Iodium (I) &amp; Selenium (Se): Kretinisme &amp; Penyakit Keshan</h2>
        </div>

        <div class="concept-unit">
          <div class="unit-heading">Intuisi Mekanisme 60 Detik</div>
          <div class="unit-box">
            • <b>Iodium (I):</b> Bahan baku T3/T4. Defisiensi &rarr; TSH hipofisis melonjak &rarr; <b>Gondok endemik</b> pada dewasa. Bila dialami ibu hamil &rarr; janin mengalami <b>{cl("Kretinisme neurologis")}</b> (retardasi mental permanen, tuli-bisu, perawakan pendek).<br>
            • <b>Selenium (Se):</b> Komponen antioksidan <i>Glutathione Peroxidase</i>. Defisiensi di tanah miskin Se memicu <b>{cl("Penyakit Keshan")}</b> (kardiomiopati kongestif fatal pada anak &amp; wanita muda).
          </div>

          <div class="slide-evidence" onclick="openLightbox('slides_kul3/slide_13.jpg')">
            <img src="slides_kul3/slide_13.jpg" class="evidence-thumb" alt="Slide 13" />
            <div class="evidence-meta">
              <span class="evidence-num">Bukti Slide Asli 13 &amp; 23</span>
              <div class="evidence-title">Iodium, Hormon Tiroid, dan Kardiomiopati Keshan</div>
              <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
            </div>
          </div>

          <div class="challenge-box">
            <div class="challenge-q">🎯 Cek Cepat: Kelainan kardiomiopati kongestif endemik akibat tanah miskin selenium disebut penyakit apa?</div>
            <div class="challenge-options">
              <button class="ch-btn" onclick="checkStepChallenge(7, 0, false)">A. Beriberi</button>
              <button class="ch-btn" onclick="checkStepChallenge(7, 1, true)">B. Penyakit Keshan</button>
              <button class="ch-btn" onclick="checkStepChallenge(7, 2, false)">C. Rakitis</button>
            </div>
            <div class="challenge-feedback" id="ch-fb-7">
              <b>Tepat!</b> Penyakit Keshan adalah kardiomiopati akibat defisiensi selenium.
            </div>
          </div>
        </div>

        <div class="step-actions">
          <button type="button" class="btn-nav btn-nav-prev" onclick="goToStep(6)">← Kembali</button>
          <button type="button" class="btn-nav btn-nav-next" onclick="finishFlow()">Selesaikan Alur Kartu 🎉</button>
        </div>
      </div>

      <!-- COMPLETION SCREEN -->
      <div class="completion-card" id="sc-comp">
        <span class="comp-badge">🎉</span>
        <h2 class="comp-title">Selamat! 7 dari 7 Topik Dikuasai.</h2>
        <p class="comp-desc">Anda telah memahami seluruh rantai mekanisme patofisiologi dari 32 slide dr. Iwal tanpa perlu membuka PPT aslinya. Sekarang, uji kemampuan Anda menjawab soal ujian UAB yang sesungguhnya!</p>
        <button type="button" class="btn-nav btn-nav-next" style="margin: 0 auto; display:inline-flex;" onclick="switchMainPane('pane-cbt', document.querySelectorAll('.mode-btn')[3])">Mulai Latihan CBT (8 Soal) →</button>
      </div>

    </div>

    <!-- =================================================================== -->
    <!-- MODE 2: BACA TENANG (EDITORIAL BOOK HANDOUT)                        -->
    <!-- =================================================================== -->
    <div id="pane-reading" class="pane-view">
      
      <div class="article-header">
        <span class="meta-tag">Catatan Kuliah Pakar</span>
        <h1 class="article-title">Defisiensi Mineral: Patofisiologi, Peta Klinis, dan Keputusan Terapi</h1>
        <p class="article-subtitle">Rangkuman komprehensif 32 slide dr. Iwal Reza Ahdi, Sp.PD-FINASIM. Disusun terfokus pada mekanisme sebab-akibat, interpretasi biomarker laboratorium, dan jebakan ujian UAB.</p>
      </div>

      <!-- BAB 1 -->
      <section class="chapter-section">
        <h2 class="chapter-title">1. Klasifikasi Mineral &amp; Homeostasis Tubuh</h2>
        <div class="chapter-body">
          <p>Kebutuhan harian suatu mineral tidak menentukan tingkat kepentingannya bagi kelangsungan hidup. Mineral esensial terbagi menjadi dua kelompok besar:</p>
          <div class="table-wrap">
            <table class="reading-table">
              <thead>
                <tr><th>Kelompok</th><th>Daftar Mineral</th><th>Karakteristik &amp; Peran Fisiologis</th></tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>Makromineral</b></td><td>{cl("Ca, P, Mg, Na, K, Cl")}</td>
                  <td>Dibutuhkan dalam gram per hari. Berperan dalam struktur tulang/gigi, transmisi potensial aksi saraf-otot, dan osmolaritas cairan.</td>
                </tr>
                <tr>
                  <td><b>Mikromineral (Trace)</b></td><td>{cl("Fe, Zn, I, Se, Cu, Mn")}</td>
                  <td>Dibutuhkan dalam miligram atau mikrogram per hari. Kofaktor enzim redoks, sintesis DNA, serta struktur hormon tiroid.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- BAB 2 -->
      <section class="chapter-section">
        <h2 class="chapter-title">2. Besi (Fe): Perjalanan Defisiensi &amp; Panduan Terapi AGA 2024</h2>
        <div class="chapter-body">
          <p>Penipisan besi terjadi dalam tiga stadium berurutan. Nilai MCV dan Hb yang normal tidak menyingkirkan defisiensi besi dini:</p>
          <ul style="padding-left: 20px; margin-bottom: 18px;">
            <li><b>Stadium 1 (Cadangan Turun):</b> {cl("Ferritin serum turun (&lt;15–30 ng/mL)")}. Hb dan MCV masih normal!</li>
            <li><b>Stadium 2 (Eritropoiesis Terbatas):</b> {cl("TSAT anjlok (&lt;16–20%)")}, TIBC meningkat. Produksi eritrosit mulai terhambat.</li>
            <li><b>Stadium 3 (Anemia Defisiensi Besi):</b> Hb turun, MCV &lt;80 fL (mikrositik hipokromik), timbul {tt("Pagophagia", "Pagophagia", "Bentuk pica spesifik mengunyah es batu berulang kali.", "Tanda patognomonik defisiensi besi.")} dan kuku sendok.</li>
          </ul>
          <div class="callout-pearl">
            <div class="callout-title">Rekomendasi Terapi AGA 2024</div>
            <div class="callout-body">Besi oral maksimal {cl("1 kali sehari atau selang-hari (alternate-day)")} untuk mencegah lonjakan hormon {tt("Hepcidin", "Hepcidin", "Hormon peptida hati pengatur utama besi sistemik.", "Mengunci ferroportin di enterosit usus selama 24–48 jam sehingga dosis besi berikutnya terbuang.")} yang memblokade absorpsi berikutnya.</div>
          </div>
        </div>
      </section>

      <!-- BAB 3 -->
      <section class="chapter-section">
        <h2 class="chapter-title">3. Seng (Zn): Trias Gejala Khas &amp; Fitat</h2>
        <div class="chapter-body">
          <p>Seng esensial untuk epitel dan imunitas. Trias patognomonik defisiensi: {cl("Dermatitis periorifisial &amp; akral, diare kronik, dan alopesia")}. Asam {tt("Fitat", "Asam Fitat", "Senyawa organik pengikat fosfor pada serealia tak beragi.", "Membentuk kelat tak larut dengan seng di usus sehingga menghambat penyerapan.")} pada gandum mentah menghambat penyerapan seng di usus.</p>
        </div>
      </section>

      <!-- BAB 4 -->
      <section class="chapter-section">
        <h2 class="chapter-title">4. Kalsium &amp; Magnesium: Kanal ROMK Ginjal</h2>
        <div class="chapter-body">
          <p>Kalsium ionisasi rendah memicu tetani: {tt("Chvostek sign", "Tanda Chvostek", "Kedutan sudut bibir saat saraf fasialis diketuk.", "Tanda hipokalsemia akut.")} (+), {tt("Trousseau sign", "Tanda Trousseau", "Spasme karpopedal saat manset tensimeter dipompa >sistolik 3 menit.", "Sangat spesifik untuk hipokalsemia.")} (+), dan {cl("QT memanjang")}.</p>
          <div class="callout-danger">
            <div class="danger-title">Mengapa Kalium Susah Naik Bila Magnesium Rendah?</div>
            <div class="danger-body">Magnesium intraseluler menghambat kanal {tt("ROMK", "Renal Outer Medullary Potassium Channel", "Kanal sekresi kalium di tubulus ginjal.", "Bila Mg rendah, kanal ROMK terbuka bebas sehingga kalium bocor masif ke urin.")} di tubulus ginjal. Bila Mg &lt;1.7 mg/dL, kalium bocor terus ke urin. Wajib koreksi Magnesium bersamaan!</div>
          </div>
        </div>
      </section>

      <!-- BAB 5 -->
      <section class="chapter-section">
        <h2 class="chapter-title">5. Fosfat (P) &amp; Refeeding Syndrome</h2>
        <div class="chapter-body">
          <p>Pasien malnutrisi yang diberi karbohidrat mendadak mengalami lonjakan insulin yang mendorong fosfat masuk ke sel &rarr; {cl("Hipofosfatemia berat (&lt;1.0 mg/dL)")} &rarr; krisis ATP &rarr; gagal napas akut diafragma dan aritmia. Pencegahan: Tiamin dulu, kalori awal bertahap {cl("10–15 kkal/kg/hari")}.</p>
        </div>
      </section>

      <!-- BAB 6 -->
      <section class="chapter-section">
        <h2 class="chapter-title">6. Tembaga (Cu), Iodium, &amp; Selenium</h2>
        <div class="chapter-body">
          <p>Defisiensi Tembaga (Cu): {cl("Anemia mikrositik + Neutropenia + Mielopati ataksia")}, dipicu konsumsi suplemen Zinc dosis tinggi yang merangsang protein {tt("Metallothionein", "Metallothionein", "Protein pengikat logam di sel usus.", "Diinduksi oleh zinc dosis tinggi; mengikat tembaga dan membuangnya.")}. Iodium defisiensi memicu gondok dan {tt("Kretinisme", "Kretinisme", "Sindrom defisit mental dan fisik janin akibat kekurangan iodium saat hamil.", "Gejala: retardasi mental, tuli-bisu, perawakan pendek.")} pada janin. Selenium defisiensi memicu {tt("Penyakit Keshan", "Penyakit Keshan", "Kardiomiopati kongestif akibat defisiensi selenium di tanah miskin Se.", "Memicu gagal jantung pada anak dan wanita muda.")}.</p>
        </div>
      </section>

    </div>

    <!-- =================================================================== -->
    <!-- MODE 3: JEMBATAN KLINIS LINTAS BLOK                                -->
    <!-- =================================================================== -->
    <div id="pane-bridge" class="pane-view">
      <div class="bridge-card">
        <h2 class="chapter-title" style="border:none;margin-bottom:6px;">Jembatan Klinis Lintas Blok: Menghubungkan Semester 1 s.d. 3</h2>
        <p style="color:var(--ink-secondary);font-size:0.95rem;margin-bottom:16px;">Konsep mineral saling terkait erat dengan materi patologi, genetika, dan fisiologi blok sebelumnya:</p>

        <div class="bridge-tabs">
          <button type="button" class="bridge-tab-btn active" onclick="switchBridgePane('br-anemia', this)">1. Sindrom Anemia Mikrositik</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridgePane('br-ginjal', this)">2. Fisiologi Ginjal &amp; Kalium</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridgePane('br-atp', this)">3. Refeeding &amp; Glikolisis</button>
          <button type="button" class="bridge-tab-btn" onclick="switchBridgePane('br-tulang', this)">4. Kalsium &amp; Tulang</button>
        </div>

        <div id="br-anemia" class="bridge-pane active">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-emn">Blok 9 EMN</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Anemia Defisiensi Besi (IDA)</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Ferritin anjlok (&lt;15–30 ng/mL), TIBC meningkat, RDW melebar. Sering pada menorrhagia.</p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 2 BMS 1</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Thalassemia Trait</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Ferritin normal/naik, RDW normal, Mentzer Index &lt;13. Konfirmasi: elektroforesis Hb.</p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-hi">Blok 8 HI</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Anemia Penyakit Kronis</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Ferritin normal/naik (reaktan fase akut), hepcidin melonjak akibat sitokin IL-6.</p>
            </div>
          </div>
        </div>

        <div id="br-ginjal" class="bridge-pane">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 5 BMS 4</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Kanal ROMK &amp; Furosemid</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Furosemid membuang K dan Mg. Di tubulus distal, kanal ROMK bocor masif bila Mg intrasel kurang.</p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-bdt">Blok 7 BDT</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Aritmia &amp; Protokol KCl</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Hipokalemia dengan gelombang U berisiko Torsades. Wajib koreksi MgSO4 bila KCl gagal naik.</p>
            </div>
          </div>
        </div>

        <div id="br-atp" class="bridge-pane">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 4 BMS 3</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Fosforilasi Glikolisis</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Insulin memicu heksokinase massal, menyedot fosfat ekstrasel &rarr; sintesis ATP lumpuh.</p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-emn">Blok 9 EMN</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Formula F-75 WHO</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Formula rendah kalori awal (75 kkal/100 mL) sengaja dipakai untuk mencegah refeeding syndrome.</p>
            </div>
          </div>
        </div>

        <div id="br-tulang" class="bridge-pane">
          <div class="bridge-grid">
            <div class="bridge-box">
              <span class="bridge-tag tag-bms">Blok 3 BMS 2</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">RANKL &amp; Osteoklas</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">PTH menaikkan kalsium darah dengan merangsang osteoblas melepas RANKL untuk resorpsi tulang.</p>
            </div>
            <div class="bridge-box">
              <span class="bridge-tag tag-emn">Blok 9 EMN</span>
              <div style="font-weight:700;font-size:0.96rem;margin-bottom:4px;">Kalsitriol 1,25-(OH)2D3</div>
              <p style="font-size:0.86rem;color:var(--ink-secondary);line-height:1.5;">Menginduksi protein calbindin di enterosit usus untuk meningkatkan penyerapan kalsium makanan.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- =================================================================== -->
    <!-- MODE 4: LATIHAN CBT (UWORLD METRICS)                                -->
    <!-- =================================================================== -->
    <div id="pane-cbt" class="pane-view">
      <div class="diag-dashboard">
        <div class="diag-card">
          <span class="diag-val" id="diag-mastered" style="color:var(--sage);">0</span>
          <span class="diag-lbl">Tuntas (Benar + Yakin)</span>
        </div>
        <div class="diag-card">
          <span class="diag-val" id="diag-lucky" style="color:var(--ochre);">0</span>
          <span class="diag-lbl">Tebakan Beruntung (Benar + Ragu)</span>
        </div>
        <div class="diag-card">
          <span class="diag-val" id="diag-danger" style="color:var(--coral);">0</span>
          <span class="diag-lbl">Miskonsepsi Berbahaya (Salah + Yakin)</span>
        </div>
        <div class="diag-card">
          <span class="diag-val" id="diag-gap" style="color:var(--navy);">0</span>
          <span class="diag-lbl">Kesenjangan Pemahaman (Salah + Ragu)</span>
        </div>
      </div>

      <div id="cbt-target"></div>
    </div>

    <!-- =================================================================== -->
    <!-- MODE 5: MATRIKS CEK CEPAT H-1                                      -->
    <!-- =================================================================== -->
    <div id="pane-flash" class="pane-view">
      <div class="table-wrap" style="box-shadow:var(--shadow-sm);margin-top:0;">
        <table class="reading-table">
          <thead>
            <tr><th>Mineral</th><th>Organ Target</th><th>Gejala Patognomonik</th><th>Biomarker Lab Kunci</th><th>Jebakan Ujian UAB</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><b>Besi (Fe)</b></td><td>Darah &amp; Enzim</td><td>Pagophagia (es batu), koilonychia.</td>
              <td><b>Ferritin &lt; 15–30 ng/mL</b> (paling dini).</td>
              <td style="color:var(--coral);font-weight:600;">MCV normal tidak menyingkirkan defisiensi besi dini!</td>
            </tr>
            <tr>
              <td><b>Seng (Zn)</b></td><td>Kulit &amp; Imun</td><td>Dermatitis periorifisial/akral, diare, alopesia.</td>
              <td>Serum Zinc &lt; 70 &mu;g/dL.</td>
              <td style="color:var(--coral);font-weight:600;">Diet tinggi asam fitat menghambat penyerapan seng di usus.</td>
            </tr>
            <tr>
              <td><b>Magnesium (Mg)</b></td><td>Saraf &amp; Ginjal</td><td>Tremor, tetani, <b>hipokalemia refrakter</b>.</td>
              <td>Magnesium &lt; 1.7 mg/dL.</td>
              <td style="color:var(--coral);font-weight:600;">Kalium tidak bisa naik sebelum kadar Mg dikoreksi serentak!</td>
            </tr>
            <tr>
              <td><b>Fosfat (P)</b></td><td>Energi (ATP)</td><td>Kelemahan diafragma (takipnea), aritmia (Refeeding).</td>
              <td>Fosfat &lt; 1.0 mg/dL (berat).</td>
              <td style="color:var(--coral);font-weight:600;">Dipicu lonjakan insulin saat refeeding karbohidrat.</td>
            </tr>
            <tr>
              <td><b>Tembaga (Cu)</b></td><td>Darah &amp; Saraf</td><td>Anemia mikrositik + neutropenia + ataksia.</td>
              <td>Serum Cu rendah, ceruloplasmin rendah.</td>
              <td style="color:var(--coral);font-weight:600;">Dipicu konsumsi suplemen Zinc dosis tinggi jangka panjang!</td>
            </tr>
            <tr>
              <td><b>Kalsium (Ca)</b></td><td>Saraf &amp; Tulang</td><td>Parestesia, tanda Chvostek/Trousseau (+), QT panjang.</td>
              <td>Ionized Calcium (Ca ion bebas).</td>
              <td style="color:var(--coral);font-weight:600;">99% kalsium di tulang, serum total dipengaruhi albumin.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </main>

  <!-- Lightbox Modal -->
  <div id="lightbox-modal" class="lightbox-modal" onclick="closeLightbox()">
    <img id="lightbox-img" src="" class="lightbox-img" alt="Zoom Slide" onclick="event.stopPropagation()" />
  </div>

  <script>
    // VIEW SWITCHER
    function switchMainPane(paneId, btn) {{
      document.querySelectorAll('.pane-view').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(paneId).classList.add('active');
      btn.classList.add('active');
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function switchBridgePane(id, btn) {{
      document.querySelectorAll('.bridge-pane').forEach(p => p.classList.remove('active'));
      document.querySelectorAll('.bridge-tab-btn').forEach(b => b.classList.remove('active'));
      document.getElementById(id).classList.add('active');
      btn.classList.add('active');
    }}

    function openLightbox(src) {{
      const modal = document.getElementById('lightbox-modal');
      const img = document.getElementById('lightbox-img');
      img.src = src;
      modal.classList.add('open');
    }}
    function closeLightbox() {{
      document.getElementById('lightbox-modal').classList.remove('open');
    }}
    document.addEventListener('keydown', e => {{
      if (e.key === 'Escape') closeLightbox();
    }});

    // CLOZE TOGGLE
    let clozeActive = false;
    function toggleCloze() {{
      clozeActive = !clozeActive;
      document.body.classList.toggle('cloze-active', clozeActive);
      const btn = document.getElementById('cloze-toggle');
      const status = document.getElementById('cloze-status');
      if (clozeActive) {{
        btn.classList.add('active');
        status.textContent = 'ON';
        document.querySelectorAll('.cloze-mask').forEach(el => el.classList.remove('revealed'));
      }} else {{
        btn.classList.remove('active');
        status.textContent = 'OFF';
      }}
    }}
    document.addEventListener('keydown', e => {{
      if (e.key.toLowerCase() === 'm' && !['INPUT', 'TEXTAREA'].includes(document.activeElement.tagName)) {{
        toggleCloze();
      }}
    }});

    // MODE 1: STEP-BY-STEP PROGRESSION
    let currentStep = 1;
    const totalSteps = 7;
    const stepNames = [
      "Besi (Fe) & Anemia Mikrositik",
      "Seng (Zn) & Fitat",
      "Magnesium (Mg) & Kanal ROMK",
      "Fosfat (P) & Refeeding Syndrome",
      "Kalsium (Ca) & Tetani",
      "Tembaga (Cu) & Interaksi Zinc",
      "Iodium & Selenium"
    ];

    function goToStep(n) {{
      document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
      document.getElementById('sc-comp').classList.remove('active');
      currentStep = n;
      document.getElementById('sc-' + n).classList.add('active');
      
      const pct = Math.round((n / totalSteps) * 100);
      document.getElementById('flow-step-label').textContent = `Langkah ${{n}} dari ${{totalSteps}} · ${{stepNames[n-1]}}`;
      document.getElementById('flow-percent-label').textContent = `${{pct}}% Dikuasai`;
      document.getElementById('flow-progress-bar').style.width = pct + '%';
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function finishFlow() {{
      document.querySelectorAll('.step-card').forEach(c => c.classList.remove('active'));
      document.getElementById('sc-comp').classList.add('active');
      document.getElementById('flow-step-label').textContent = 'Selesai: 7 dari 7 Topik Dikuasai!';
      document.getElementById('flow-percent-label').textContent = '100% Selesai';
      document.getElementById('flow-progress-bar').style.width = '100%';
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function checkStepChallenge(stepIdx, optIdx, isCorrect) {{
      const card = document.getElementById('sc-' + stepIdx);
      const btns = card.querySelectorAll('.ch-btn');
      btns.forEach((b, i) => {{
        if (i === optIdx) {{
          b.classList.add(isCorrect ? 'is-correct' : 'is-wrong');
        }}
      }});
      const fb = document.getElementById('ch-fb-' + stepIdx);
      if (fb) fb.classList.add('show');
    }}

    // CBT DATA
    const CBT_QUIZ = [
      {{
        stem: '1. Seorang perempuan 29 tahun datang ke poliklinik dengan keluhan lemas dan berdebar saat beraktivitas sejak 2 bulan. Pasien memiliki riwayat menstruasi sangat banyak (ganti pembalut 6–7 kali/hari) selama 8 hari setiap siklusnya. Konjungtiva anemis (+). Laboratorium: Hb 8,9 g/dL, MCV 68 fL, MCH 21 pg. Pasien mengaku memiliki kebiasaan mengunyah es batu berulang kali (pagophagia). Pemeriksaan biomarker manakah yang paling sensitif dan paling awal menurun untuk memastikan diagnosis?',
        opts: ['Total Iron Binding Capacity (TIBC)', 'Ferritin serum', 'Saturasi transferrin (TSAT)', 'Hemoglobin elektroforesis', 'Bilirubin indirek serum'],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Ferritin serum)</b><br>Pasien mengalami Anemia Defisiensi Besi akibat menorrhagia kronik. <i>Pagophagia</i> adalah bentuk pica patognomonik defisiensi besi. Pada perjalanan alami (Slide 10), <b>Ferritin serum adalah biomarker pertama yang anjlok (&lt;15–30 ng/mL)</b> mencerminkan habisnya cadangan besi sebelum Hb dan MCV turun.',
        slide: 'slides_kul3/slide_10.jpg',
        slideTitle: 'Slide 10 · Perjalanan Defisiensi Besi: Ferritin Turun Lebih Awal'
      }},
      {{
        stem: '2. Laki-laki 67 tahun dengan gagal jantung kongestif yang rutin mengonsumsi furosemid mengeluh kelemahan otot tungkai dan berdebar. EKG menunjukkan depresi segmen ST, gelombang T mendatar, dan muncul gelombang U yang menonjol. Hasil laboratorium: Kalium 2,8 mmol/L. Dokter telah memberikan suplementasi KCl oral dosis tinggi selama 3 hari, namun pada evaluasi ulang kadar Kalium pasien tetap rendah (2,9 mmol/L). Gangguan elektrolit penyerta manakah yang mendasari kondisi refrakter tersebut?',
        opts: ['Hiponatremia', 'Hipokalsemia', 'Hipomagnesemia', 'Hiperfosfatemia', 'Hiperkalsiuria'],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Hipomagnesemia)</b><br>Furosemid membuang Kalium dan Magnesium sekaligus. Di tubulus ginjal, ion Magnesium intrasel adalah inhibitor alami kanal ROMK. Pada hipomagnesemia (Slide 17 & 28), kanal ROMK terbuka bebas tanpa rem sehingga Kalium terus menerus bocor ke urin. Wajib koreksi Magnesium bersamaan.',
        slide: 'slides_kul3/slide_17.jpg',
        slideTitle: 'Slide 17 · Mengapa Kalium Sulit Naik Bila Magnesium Rendah'
      }},
      {{
        stem: '3. Anak laki-laki 4 tahun dibawa ibunya dengan keluhan bercak kemerahan bersisik dan berkrusta di area sekitar mulut, perineum, serta sela-sela jari kaki sejak 1 bulan. Pasien juga mengalami diare kronik kambuhan dan rambut rontok hingga tampak botak sebagian. Pasien memiliki riwayat diet monoton tinggi serealia dan bubur gandum tanpa asupan hewani. Defisiensi mikromineral apakah yang mendasari kelainan tersebut?',
        opts: ['Besi (Fe)', 'Tembaga (Cu)', 'Seng (Zn)', 'Selenium (Se)', 'Mangan (Mn)'],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Seng / Zinc)</b><br>Trias patognomonik: <b>dermatitis periorifisial & akral, diare kronik, dan alopesia</b> merupakan tanda khas defisiensi Seng (Slide 12). Serealia mengandung asam <b>fitat</b> tinggi yang mengikat seng di usus membentuk senyawa tak larut.',
        slide: 'slides_kul3/slide_12.jpg',
        slideTitle: 'Slide 12 · Seng (Zn): Integritas Kulit & Peran Inhibitor Fitat'
      }},
      {{
        stem: '4. Pasien laki-laki 46 tahun dengan riwayat malnutrisi berat dan kelaparan selama 12 hari dirawat di bangsal. Dokter segera memberikan nutrisi parenteral tinggi karbohidrat. Dalam waktu 48 jam, pasien mendadak mengalami takipnea berat, kelemahan otot menyeluruh, dan aritmia. Gangguan elektrolit serum manakah yang menjadi pemicu utama kegagalan napas akut tersebut?',
        opts: ['Hiponatremia berat (&lt;120 mEq/L)', 'Hipokalsemia terionisasi', 'Hipofosfatemia berat (&lt;1.0 mg/dL)', 'Asidosis laktat berat', 'Hiperglikemia hiperosmolar'],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Hipofosfatemia berat &lt;1.0 mg/dL)</b><br>Pasien mengalami <i>Refeeding Syndrome</i> (Slide 19 & 29). Karbohidrat mendadak memicu lonjakan insulin yang mendorong glukosa dan Fosfat masuk masif ke dalam sel. Terjadilah hipofosfatemia berat yang menghentikan sintesis ATP, melumpuhkan diafragma dan memicu aritmia.',
        slide: 'slides_kul3/slide_19.jpg',
        slideTitle: 'Slide 19 · Refeeding Syndrome: Pergeseran Elektrolit Akut'
      }},
      {{
        stem: '5. Perempuan 35 tahun pasca-operasi bypass lambung datang dengan keluhan baal dan kesemutan di kedua tungkai serta ataksia sensorik. Laboratorium: Hb 9,0 g/dL, MCV 72 fL (mikrositik), dan neutropenia berat (ANC 750/&mu;L). Pasien mengaku mengonsumsi suplemen Zinc dosis tinggi (80 mg/hari) selama 8 bulan terakhir. Defisiensi mineral apakah yang paling tepat menjelaskan kondisi pasien?',
        opts: ['Besi (Fe)', 'Tembaga (Cu)', 'Iodium (I)', 'Selenium (Se)', 'Kalsium (Ca)'],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Tembaga / Cu)</b><br>Kombinasi <b>anemia mikrositik + neutropenia + mielopati ataksia</b> adalah tanda khas defisiensi Tembaga (Slide 22). Suplemen Zinc dosis tinggi menginduksi <i>metallothionein</i> di enterosit yang mengikat tembaga kuat dan menghambat absorpsinya.',
        slide: 'slides_kul3/slide_22.jpg',
        slideTitle: 'Slide 22 · Tembaga (Cu) & Pemicu Iatrogenik Suplemen Zinc'
      }},
      {{
        stem: '6. Berdasarkan Clinical Practice Update American Gastroenterological Association (AGA 2024), bagaimanakah aturan suplementasi besi oral yang paling tepat dan dapat ditoleransi optimal pada pasien anemia defisiensi besi?',
        opts: ['Diberikan dosis tinggi 3 kali sehari bersama makanan', 'Diberikan dosis terbagi setiap 6 jam disertai antasida', 'Diberikan maksimal 1 kali sehari atau rejimen selang-hari (alternate-day)', 'Diberikan bersamaan dengan susu sapi segar', 'Diberikan 4 kali sehari dalam dosis kecil'],
        ans: 2,
        exp: '<b>Jawaban Benar: C (Maksimal 1 kali sehari atau selang-hari)</b><br>Pedoman AGA 2024 (Slide 11) menekankan bahwa setiap dosis besi memicu lonjakan hormon <b>Hepcidin</b> yang memblokade absorpsi berikutnya selama 24–48 jam. Pemberian 1x/hari atau selang-hari memaksimalkan penyerapan dan meminimalkan efek samping GI.',
        slide: 'slides_kul3/slide_11.jpg',
        slideTitle: 'Slide 11 · Terapi Fe Konsensus AGA 2024'
      }},
      {{
        stem: '7. Pemeriksaan fisik pada pasien dengan kecurigaan hipokalsemia menunjukkan adanya spasme karpopedal pada tangan ketika manset tensimeter dipompa di atas tekanan sistolik selama 3 menit. Disebut apakah tanda fisik klinis patognomonik tersebut?',
        opts: ['Chvostek sign', 'Trousseau sign', 'Kernig sign', 'Brudzinski sign', 'Babinski sign'],
        ans: 1,
        exp: '<b>Jawaban Benar: B (Trousseau sign)</b><br>Tanda Trousseau (spasme karpopedal saat manset tensimeter dipompa >sistolik 3 menit) sangat sensitif dan spesifik untuk hipokalsemia (Slide 15). Chvostek adalah kedutan bibir saat saraf fasialis diketuk.',
        slide: 'slides_kul3/slide_15.jpg',
        slideTitle: 'Slide 15 · Hipokalsemia: Tanda Klinis Trousseau & Chvostek'
      }},
      {{
        stem: '8. Wanita hamil di daerah pegunungan yang jarang mengonsumsi garam beriodium melahirkan bayi dengan keterlambatan perkembangan saraf berat, perawakan pendek, dan tuli-bisu. Mekanisme patofisiologi apakah yang mendasari kondisi kretinisme pada bayi tersebut?',
        opts: ['Kekurangan iodium memicu hambatan sintesis T3/T4 yang vital bagi mielinisasi dan perkembangan otak janin', 'Kelebihan TSH ibu menembus plasenta dan merusak kelenjar tiroid janin', 'Defisiensi selenium langsung menghambat enzim deiodinase perifer tanpa melibatkan hormon tiroid', 'Kadar kalsium yang rendah mengganggu pembentukan neurotransmitter otak', 'Fosfat yang rendah menyebabkan kegagalan pembentukan mielin saraf'],
        ans: 0,
        exp: '<b>Jawaban Benar: A</b><br>Iodium adalah substrat esensial hormon tiroid T3/T4 (Slide 13). Pada kehamilan, hormon tiroid sangat krusial untuk neurogenesis dan mielinisasi otak janin. Defisiensi berat memicu kretinisme endemik.',
        slide: 'slides_kul3/slide_13.jpg',
        slideTitle: 'Slide 13 · Iodium (I): Sintesis Hormon Tiroid & Bahaya Kehamilan'
      }}
    ];

    let cbtAns = {{}};
    let cbtConf = {{}};

    function setCBTConfidence(idx, val) {{
      cbtConf[idx] = val;
      const card = document.getElementById('q-card-' + idx);
      const btns = card.querySelectorAll('.conf-btn');
      btns.forEach(b => b.classList.remove('active-high', 'active-low'));
      if (val === 'high') btns[0].classList.add('active-high');
      else btns[1].classList.add('active-low');
    }}

    function pickCBTAnswer(qIdx, optIdx) {{
      if (cbtAns[qIdx] !== undefined) return;
      cbtAns[qIdx] = optIdx;
      if (!cbtConf[qIdx]) cbtConf[qIdx] = 'high';

      const q = CBT_QUIZ[qIdx];
      const isCorrect = optIdx === q.ans;
      const conf = cbtConf[qIdx];

      const card = document.getElementById('q-card-' + qIdx);
      const rows = card.querySelectorAll('.opt-choice');
      rows.forEach((r, idx) => {{
        if (idx === q.ans) r.classList.add('is-correct');
        else if (idx === optIdx && !isCorrect) r.classList.add('is-wrong');
      }});

      const expBox = document.getElementById('exp-box-' + qIdx);
      const pill = document.getElementById('pill-' + qIdx);
      expBox.classList.add('show');

      if (isCorrect && conf === 'high') {{
        pill.className = 'outcome-pill pill-mastered';
        pill.textContent = '🏆 Tuntas (Benar + Yakin)';
      }} else if (isCorrect && conf === 'low') {{
        pill.className = 'outcome-pill pill-lucky';
        pill.textContent = '⚠️ Tebakan Beruntung (Benar + Ragu) — Review Ulang!';
      }} else if (!isCorrect && conf === 'high') {{
        pill.className = 'outcome-pill pill-danger';
        pill.textContent = '🚨 Miskonsepsi Berbahaya (Salah + Yakin) — Prioritas Evaluasi!';
      }} else {{
        pill.className = 'outcome-pill pill-gap';
        pill.textContent = '📖 Kesenjangan Pemahaman (Salah + Ragu)';
      }}

      updateCBTDiagnostics();
    }}

    function updateCBTDiagnostics() {{
      let mastered = 0, lucky = 0, danger = 0, gap = 0;
      Object.keys(cbtAns).forEach(k => {{
        const idx = parseInt(k);
        const q = CBT_QUIZ[idx];
        const isCorrect = cbtAns[idx] === q.ans;
        const conf = cbtConf[idx] || 'high';

        if (isCorrect && conf === 'high') mastered++;
        else if (isCorrect && conf === 'low') lucky++;
        else if (!isCorrect && conf === 'high') danger++;
        else gap++;
      }});

      document.getElementById('diag-mastered').textContent = mastered;
      document.getElementById('diag-lucky').textContent = lucky;
      document.getElementById('diag-danger').textContent = danger;
      document.getElementById('diag-gap').textContent = gap;
    }}

    function renderCBT() {{
      const container = document.getElementById('cbt-target');
      if (!container) return;
      container.innerHTML = CBT_QUIZ.map((q, idx) => `
        <article class="q-card" id="q-card-${{idx}}">
          <div class="q-header-row">
            <span class="q-number">SOAL #${{idx + 1}}</span>
            <div class="confidence-picker">
              <span>Tingkat Keyakinan:</span>
              <button type="button" class="conf-btn active-high" onclick="setCBTConfidence(${{idx}}, 'high')">🎯 Yakin</button>
              <button type="button" class="conf-btn" onclick="setCBTConfidence(${{idx}}, 'low')">🤔 Ragu-Ragu</button>
            </div>
          </div>
          <div class="q-stem">${{q.stem}}</div>
          <div class="q-options-stack">
            ${{q.opts.map((opt, oIdx) => `
              <button type="button" class="opt-choice" onclick="pickCBTAnswer(${{idx}}, ${{oIdx}})">
                <span class="opt-key-txt">${{String.fromCharCode(65 + oIdx)}}.</span>
                <span>${{opt}}</span>
              </button>
            `).join('')}}
          </div>
          <div class="q-explanation-box" id="exp-box-${{idx}}">
            <span class="outcome-pill" id="pill-${{idx}}"></span>
            <div style="color:#2D2F33;margin-bottom:12px;">${{q.exp}}</div>
            <div class="slide-evidence" onclick="openLightbox('${{q.slide}}')" style="margin:8px 0 0;background:#FFFFFF;">
              <img src="${{q.slide}}" class="evidence-thumb" alt="Slide" />
              <div class="evidence-meta">
                <span class="evidence-num">Bukti Slide Asli</span>
                <div class="evidence-title">${{q.slideTitle}}</div>
                <div class="evidence-hint">Klik untuk melihat slide kuliah ukuran penuh ↗</div>
              </div>
            </div>
          </div>
        </article>
      `).join('');
    }}

    document.addEventListener('DOMContentLoaded', () => {{
      renderCBT();
    }});
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(HTML_CODE)

print(f"Modul Multi-Mode EMN KUL 3 berhasil dibuat di {OUT_HTML} (ukuran: {len(HTML_CODE)} bytes)")
