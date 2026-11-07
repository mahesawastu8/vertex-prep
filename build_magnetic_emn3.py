#!/usr/bin/env python3
"""Build the Magnetic, High-Stakes 'Why-First' Preclinical Masterpiece for EMN KUL 3 Defisiensi Mineral.
Incorporates:
1. The Cognitive Curiosity Hook (Loewenstein Curiosity Gap + High-Stakes Clinical Enigmas)
   - 3 Real Medical Thriller Mysteries (The Food that Kills, The Ice-Chewing Brain, The Vanishing Potassium)
   - Evolutionary perspective of minerals forged in supernovas powering 60 trillion human cells
2. Progressive Revelation: From Irresistible Intrigue -> 60-Second Visual Simulators -> 8-Mineral Exploration Deck -> Bug-Free UAB QBank
3. World-Class Impeccable Aesthetic: Serene Alabaster canvas (#F9F8F6), Newsreader editorial drama, zero AI slop.
"""
import os

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"
OUT_HTML = os.path.join(BASE_DIR, "EMN_KUL3_Defisiensi_Mineral.html")

MAGNETIC_HTML = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Defisiensi Mineral · Rahasia Atom Kehidupan & Kasus Klinis</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=JetBrains+Mono:wght@500;600&family=Newsreader:ital,opsz,wght@0,6..72,500;0,6..72,600;0,6..72,700;1,6..72,400;1,6..72,600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #F9F8F6;
      --surface: #FFFFFF;
      --surface-subtle: #F2EFEB;
      --surface-active: #EAE6DF;
      
      --border: #E5E1D8;
      --border-dark: #C8C4B7;
      
      --ink: #141517;
      --ink-secondary: #4E5157;
      --ink-muted: #82858D;
      
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
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html { scroll-behavior: smooth; }

    body {
      background-color: var(--bg);
      color: var(--ink);
      font-family: var(--font-sans);
      font-size: 16px;
      line-height: 1.75;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 120px;
    }

    ::selection { background: #D2E8DB; color: #141517; }

    /* Sticky Clean Topbar */
    .app-header {
      position: sticky;
      top: 0;
      z-index: 200;
      background: rgba(249, 248, 246, 0.92);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--border);
      padding: 12px 28px;
      transition: all 0.2s ease;
    }
    .header-content {
      max-width: 1080px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }
    .brand-mark {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .brand-tag {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      color: #FFFFFF;
      background: var(--ink);
      padding: 3px 8px;
      border-radius: var(--radius-sm);
    }
    .brand-context {
      display: flex;
      flex-direction: column;
    }
    .brand-context-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink);
      line-height: 1.2;
    }
    .brand-context-sub {
      font-size: 0.78rem;
      color: var(--ink-muted);
    }

    .view-pills {
      display: flex;
      background: var(--surface-subtle);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 2px;
    }
    .view-pill {
      border: none;
      background: transparent;
      font-family: var(--font-sans);
      font-size: 0.82rem;
      font-weight: 600;
      color: var(--ink-secondary);
      padding: 7px 16px;
      border-radius: var(--radius-full);
      cursor: pointer;
      transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
      white-space: nowrap;
    }
    .view-pill:hover { color: var(--ink); }
    .view-pill.active {
      background: var(--surface);
      color: var(--ink);
      box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }

    .btn-anki {
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
    }
    .btn-anki:hover {
      background: #154D33;
      transform: translateY(-1px);
    }

    /* Main Container */
    .main-shell {
      max-width: 980px;
      margin: 0 auto;
      padding: 40px 24px 0;
    }

    .view-section { display: none; }
    .view-section.active { display: block; animation: viewIn 0.25s ease-out; }
    @keyframes viewIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* =========================================================================
       THE "WHY" HERO: THE COGNITIVE CURIOSITY HOOK (RASA INGIN TAHU ALAMI)
       ========================================================================= */
    .why-section {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 40px 44px;
      margin-bottom: 40px;
      box-shadow: var(--shadow-ambient);
    }
    .why-kicker {
      font-family: var(--font-mono);
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--terracotta);
      margin-bottom: 12px;
      display: block;
    }
    .why-headline {
      font-family: var(--font-serif);
      font-size: 2.8rem;
      font-weight: 600;
      line-height: 1.2;
      color: var(--ink);
      letter-spacing: -0.02em;
      margin-bottom: 18px;
    }
    .why-lead {
      font-size: 1.15rem;
      line-height: 1.7;
      color: var(--ink-secondary);
      margin-bottom: 28px;
    }
    .why-lead strong { color: var(--ink); }

    /* 3 High-Stakes Enigma Cards */
    .enigma-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 32px;
    }
    .enigma-card {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: all 0.2s ease;
    }
    .enigma-card:hover {
      background: #FFFFFF;
      border-color: var(--ink);
      transform: translateY(-2px);
      box-shadow: var(--shadow-ambient);
    }
    .enigma-num {
      font-family: var(--font-mono);
      font-size: 0.74rem;
      font-weight: 700;
      color: var(--ink-muted);
      letter-spacing: 0.06em;
      margin-bottom: 8px;
    }
    .enigma-title {
      font-family: var(--font-serif);
      font-size: 1.25rem;
      font-weight: 600;
      color: var(--ink);
      line-height: 1.35;
      margin-bottom: 10px;
    }
    .enigma-preview {
      font-size: 0.88rem;
      color: var(--ink-secondary);
      line-height: 1.55;
      margin-bottom: 16px;
    }
    .enigma-trigger {
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
    }
    .enigma-trigger:hover {
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
    }

    /* Enigma Revelation Drawer */
    .enigma-reveal {
      margin-top: 24px;
      padding: 24px 28px;
      background: #FAF6ED;
      border-radius: var(--radius-md);
      border: 1px solid #EADBBE;
      display: none;
      animation: revealIn 0.25s ease-out;
    }
    .enigma-reveal.open { display: block; }
    @keyframes revealIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }
    .reveal-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 10px;
    }
    .reveal-title {
      font-size: 1.1rem;
      font-weight: 700;
      color: #38240D;
    }
    .reveal-close {
      border: none;
      background: transparent;
      font-size: 1.1rem;
      color: var(--ink-muted);
      cursor: pointer;
    }
    .reveal-body {
      font-size: 0.95rem;
      line-height: 1.68;
      color: #2F2110;
    }

    /* Bridge into Lesson */
    .why-bridge-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 16px 22px;
      font-size: 0.94rem;
      color: var(--ink);
    }
    .btn-start-mastery {
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
    }
    .btn-start-mastery:hover {
      background: var(--sage);
      transform: translateY(-1px);
    }

    /* =========================================================================
       SECTION: VISUAL SIMULATORS ("LANGSUNG PAHAM" 60 DETIK)
       ========================================================================= */
    .sim-block {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px 36px;
      margin-bottom: 36px;
      box-shadow: var(--shadow-ambient);
    }
    .sim-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 22px;
    }
    .sim-title-wrap h3 {
      font-family: var(--font-serif);
      font-size: 1.5rem;
      font-weight: 600;
      color: var(--ink);
    }
    .sim-title-wrap p {
      font-size: 0.9rem;
      color: var(--ink-secondary);
      margin-top: 3px;
    }
    .btn-intip-slide {
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
    }
    .btn-intip-slide:hover {
      border-color: var(--ink);
      color: var(--ink);
    }

    /* Iron Staging Stepper */
    .stager-tabs {
      display: flex;
      background: var(--surface-subtle);
      padding: 4px;
      border-radius: var(--radius-full);
      gap: 4px;
      margin-bottom: 22px;
    }
    .stager-btn {
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
    }
    .stager-btn.active {
      background: #FFFFFF;
      color: var(--ink);
      box-shadow: 0 2px 6px rgba(0,0,0,0.06);
    }
    .vial-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
      margin-bottom: 18px;
    }
    .vial-card {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
      transition: all 0.2s ease;
    }
    .vial-card.active-vial {
      background: #FFFFFF;
      border-color: var(--terracotta);
      box-shadow: 0 0 0 2px var(--terracotta-light);
    }
    .vial-lbl {
      font-size: 0.74rem;
      font-weight: 700;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: var(--ink-muted);
    }
    .vial-val {
      font-family: var(--font-mono);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--ink);
      margin: 4px 0 6px;
    }
    .vial-tag {
      font-size: 0.82rem;
      font-weight: 600;
    }
    .tag-danger { color: var(--terracotta); }
    .tag-safe { color: var(--sage); }
    .tag-warn { color: var(--ochre); }
    .stager-explainer {
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 16px 20px;
      font-size: 0.94rem;
      line-height: 1.65;
      color: var(--ink);
    }

    /* ROMK Channel Simulator */
    .romk-box {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 24px;
      align-items: center;
      background: var(--surface-subtle);
      border-radius: var(--radius-md);
      padding: 24px 28px;
    }
    .romk-render {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 22px;
      text-align: center;
    }
    .romk-door {
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
    }
    .romk-door.plugged {
      background: var(--sage-light);
      border-color: var(--sage);
      color: var(--sage);
    }
    .romk-door.leaking {
      background: var(--terracotta-light);
      border-color: var(--terracotta);
      color: var(--terracotta);
    }
    .romk-switches {
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .switch-btn {
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
    }
    .switch-btn:hover { border-color: var(--ink); }
    .switch-btn.active {
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
    }

    /* =========================================================================
       SECTION: MASTER-DETAIL 8 MINERAL DECK (KENYAMANAN TANPA LELAH)
       ========================================================================= */
    .browser-deck {
      display: grid;
      grid-template-columns: 240px 1fr;
      gap: 24px;
      margin-bottom: 48px;
    }
    .deck-nav-col {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .deck-item {
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
    }
    .deck-item:hover {
      background: var(--surface-subtle);
      border-color: var(--border-dark);
      transform: translateX(2px);
    }
    .deck-item.active {
      background: var(--ink);
      color: #FFFFFF;
      border-color: var(--ink);
      box-shadow: var(--shadow-ambient);
    }
    .deck-badge {
      font-size: 0.68rem;
      font-weight: 700;
      padding: 2px 6px;
      border-radius: 4px;
      background: var(--surface-subtle);
      color: var(--ink-secondary);
    }
    .deck-item.active .deck-badge {
      background: rgba(255, 255, 255, 0.2);
      color: #FFFFFF;
    }

    .sheet-card {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 32px 36px;
      box-shadow: var(--shadow-ambient);
      display: none;
      animation: sheetFade 0.2s ease-out;
    }
    .sheet-card.active { display: block; }
    @keyframes sheetFade { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: translateY(0); } }

    .sheet-title-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 22px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }
    .sheet-title-row h2 {
      font-family: var(--font-serif);
      font-size: 2.1rem;
      font-weight: 600;
      color: var(--ink);
      line-height: 1.15;
    }
    .sheet-title-row span {
      font-size: 0.86rem;
      color: var(--ink-muted);
      margin-top: 4px;
      display: block;
    }

    .sheet-columns {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 22px;
    }
    .sheet-pane {
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 18px 20px;
    }
    .sheet-pane h4 {
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
      margin-bottom: 8px;
    }
    .sheet-pane ul {
      padding-left: 18px;
      font-size: 0.94rem;
      line-height: 1.6;
      color: #2D2F33;
    }

    .uab-trap-box {
      background: var(--ochre-light);
      border: 1px solid var(--ochre-border);
      border-radius: var(--radius-md);
      padding: 18px 22px;
      margin-bottom: 22px;
    }
    .uab-trap-box h4 {
      font-size: 0.82rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ochre);
      margin-bottom: 4px;
    }
    .uab-trap-box p {
      font-size: 0.94rem;
      line-height: 1.6;
      color: #38240D;
    }

    .slide-inspector-bar {
      background: var(--surface-subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 14px 18px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .slide-inspector-bar:hover {
      background: #EAE6DF;
      border-color: var(--ink);
    }
    .inspector-meta-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .inspector-pic {
      width: 72px;
      height: 48px;
      object-fit: cover;
      border-radius: 6px;
      border: 1px solid var(--border);
    }
    .inspector-labels strong {
      font-size: 0.9rem;
      color: var(--ink);
      display: block;
    }
    .inspector-labels span {
      font-size: 0.78rem;
      color: var(--ink-muted);
    }

    /* =========================================================================
       SECTION: CBT PRACTICE (100% BUG-FREE EVALUATION)
       ========================================================================= */
    .cbt-anchor {
      margin-top: 36px;
    }
    .cbt-score-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 24px;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border);
    }
    .score-number {
      font-family: var(--font-mono);
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--sage);
    }

    .q-card-box {
      background: #FFFFFF;
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px 32px;
      margin-bottom: 24px;
      box-shadow: var(--shadow-ambient);
    }
    .q-tag-line {
      font-family: var(--font-mono);
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--ink-muted);
      margin-bottom: 8px;
      display: block;
    }
    .q-stem-body {
      font-size: 1.05rem;
      font-weight: 500;
      line-height: 1.68;
      color: var(--ink);
      margin-bottom: 20px;
    }

    .q-options-col {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .opt-choice-btn {
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
    }
    .opt-choice-btn:hover {
      background: var(--bg);
      border-color: var(--border-dark);
      transform: translateX(2px);
    }
    .opt-key-badge {
      font-family: var(--font-mono);
      font-weight: 600;
      color: var(--ink-muted);
      flex: none;
    }

    .opt-choice-btn.is-correct {
      background: var(--sage-light) !important;
      border-color: var(--sage) !important;
      color: var(--sage) !important;
      font-weight: 600;
      box-shadow: 0 0 0 1px var(--sage);
    }
    .opt-choice-btn.is-wrong {
      background: var(--terracotta-light) !important;
      border-color: var(--terracotta) !important;
      color: var(--terracotta) !important;
    }

    .feedback-sheet {
      margin-top: 20px;
      padding: 20px 24px;
      border-radius: var(--radius-md);
      font-size: 0.94rem;
      line-height: 1.65;
      display: none;
      animation: fbIn 0.2s ease-out;
    }
    .feedback-sheet.show { display: block; }
    @keyframes fbIn { from { opacity: 0; transform: translateY(-4px); } to { opacity: 1; transform: translateY(0); } }

    .feedback-sheet.tone-correct {
      background: var(--sage-light);
      border: 1px solid var(--sage-border);
      color: #124029;
    }
    .feedback-sheet.tone-wrong {
      background: var(--terracotta-light);
      border: 1px solid var(--terracotta-border);
      color: #61180C;
    }

    /* Lightbox Modal */
    .lightbox-backdrop {
      position: fixed; inset: 0; z-index: 1000;
      background: rgba(20, 21, 23, 0.85); backdrop-filter: blur(10px);
      display: none; align-items: center; justify-content: center; padding: 24px;
    }
    .lightbox-backdrop.open { display: flex; }
    .lightbox-frame {
      max-width: 92%; max-height: 88vh; border-radius: var(--radius-md);
      box-shadow: var(--shadow-float);
    }

    @media (max-width: 860px) {
      .why-section { padding: 28px 20px; }
      .why-headline { font-size: 2.1rem; }
      .enigma-grid { grid-template-columns: 1fr; }
      .browser-deck { grid-template-columns: 1fr; }
      .vial-grid { grid-template-columns: 1fr; }
      .romk-box { grid-template-columns: 1fr; }
      .sheet-columns { grid-template-columns: 1fr; }
      .view-pills { display: none; }
    }
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
        <button type="button" class="view-pill active" onclick="switchNav('view-story', this)">1. Mengapa Wajib Tahu?</button>
        <button type="button" class="view-pill" onclick="switchNav('view-sim', this)">2. Konsep 60 Detik</button>
        <button type="button" class="view-pill" onclick="switchNav('view-deck', this)">3. Buku 8 Mineral</button>
        <button type="button" class="view-pill" onclick="switchNav('view-cbt', this)">4. Latihan UAB (8)</button>
      </nav>

      <div class="header-actions">
        <a href="anki/VERTEX_EMN_KUL3_Defisiensi_Mineral.apkg" class="btn-anki" download>Deck Anki</a>
      </div>
    </div>
  </header>

  <main class="main-shell">

    <!-- =================================================================== -->
    <!-- VIEW 1: THE "WHY" HOOK (MENGAPA MATERI INI MENYEDOT PERHATIAN)      -->
    <!-- =================================================================== -->
    <div id="view-story" class="view-section active">
      <article class="why-section">
        <span class="why-kicker">Sebelum Membuka Slide Apapun · Bacalah Ini</span>
        <h1 class="why-headline">Tiga Atom Penentu Hidup-Mati yang Sering Mengelabui Dokter Muda</h1>
        <p class="why-lead">
          Di dalam 60 triliun sel tubuhmu, ada atom-atom kuno yang ditempa miliaran tahun lalu di dalam ledakan bintang (supernova): <strong>Besi, Magnesium, Fosfat, dan Seng</strong>. Jumlahnya di darah kita hanya beberapa miligram—tak sampai seberat butir beras. Namun saat seorang pasien tiba di ruang gawat darurat, ketidaktahuanmu tentang perilaku atom-atom renik ini bisa berakibat fatal.
        </p>

        <!-- 3 High-Stakes Clinical Enigmas -->
        <div class="enigma-grid">
          
          <!-- Enigma 1 -->
          <div class="enigma-card">
            <div>
              <span class="enigma-num">MISTERI 01</span>
              <h3 class="enigma-title">Makanan yang Membunuh</h3>
              <p class="enigma-preview">Kamu berniat mulia memberi makan pasien yang kelaparan 12 hari. Dalam 48 jam, diafragmanya mendadak lumpuh dan jantungnya berhenti.</p>
            </div>
            <button type="button" class="enigma-trigger" onclick="openEnigma(1)">Buka Misteri ↗</button>
          </div>

          <!-- Enigma 2 -->
          <div class="enigma-card">
            <div>
              <span class="enigma-num">MISTERI 02</span>
              <h3 class="enigma-title">Otak yang Menjerit Es Batu</h3>
              <p class="enigma-preview">Seorang wanita muda menghabiskan 5 mangkok es batu setiap hari tanpa alasan rasional. Dia tidak gila. Ada satu atom yang sedang habis di sumsum tulangnya.</p>
            </div>
            <button type="button" class="enigma-trigger" onclick="openEnigma(2)">Buka Misteri ↗</button>
          </div>

          <!-- Enigma 3 -->
          <div class="enigma-card">
            <div>
              <span class="enigma-num">MISTERI 03</span>
              <h3 class="enigma-title">Infus yang Ditelan Ginjal</h3>
              <p class="enigma-preview">Pasien aritmia diguyur infus Kalium berkali-kali tapi kalium darahnya tidak pernah naik. Jantungnya di ambang henti karena satu gerbang ginjal bocor.</p>
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
          <span>Siap memahami rantai sains di balik misteri ini selangkah demi selangkah?</span>
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
            <h3>1. Simulator 3 Stadium Defisiensi Besi: Mengapa MCV Normal Menipu?</h3>
            <p>Klik tombol stadium di bawah untuk melihat perubahan nyata di darah dan sumsum tulang.</p>
          </div>
          <button type="button" class="btn-intip-slide" onclick="openLightbox('slides_kul3/slide_10.jpg')">Intip Slide 10 ↗</button>
        </div>

        <div class="stager-tabs">
          <button type="button" class="stager-btn active" onclick="setIron(1)">Stadium 1: Cadangan Turun</button>
          <button type="button" class="stager-btn" onclick="setIron(2)">Stadium 2: Eritropoiesis Terbatas</button>
          <button type="button" class="stager-btn" onclick="setIron(3)">Stadium 3: Anemia Nyata (IDA)</button>
        </div>

        <div class="vial-grid">
          <div class="vial-card active-vial" id="vc-ferr">
            <span class="vial-lbl">Ferritin Serum (Cadangan Besi)</span>
            <div class="vial-val" id="val-ferr">&lt; 15 ng/mL</div>
            <span class="vial-tag tag-danger" id="tag-ferr">ANJLOK DULUAN (Kritis)</span>
          </div>
          <div class="vial-card" id="vc-tsat">
            <span class="vial-lbl">Saturasi Transferrin (TSAT)</span>
            <div class="vial-val" id="val-tsat">28% (Normal)</div>
            <span class="vial-tag tag-safe" id="tag-tsat">Transpor Besi Cukup</span>
          </div>
          <div class="vial-card" id="vc-hb">
            <span class="vial-lbl">Hemoglobin &amp; MCV</span>
            <div class="vial-val" id="val-hb">Hb 13.5 · MCV 88</div>
            <span class="vial-tag tag-safe" id="tag-hb">Tampak Normal (Belum Anemia)</span>
          </div>
        </div>

        <div class="stager-explainer" id="explainer-iron">
          💡 <b>Kunci Ujian dr. Iwal:</b> Pada Stadium 1, pasien <i>belum anemia</i>, tetapi cadangan besinya sudah habis terkuras. <b>MCV normal TIDAK PERNAH menyingkirkan defisiensi besi stadium awal!</b> Ferritin adalah biomarker pertama yang runtuh.
        </div>
      </article>

      <!-- SIMULATOR 2 -->
      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>2. Simulator Kanal ROMK: Mengapa Kalium Susah Naik Bila Mg Rendah?</h3>
            <p>Pecahkan teka-teki klinis: "Kenapa KCl berbotol-botol gagal menaikkan kalium pasien?"</p>
          </div>
          <button type="button" class="btn-intip-slide" onclick="openLightbox('slides_kul3/slide_17.jpg')">Intip Slide 17 ↗</button>
        </div>

        <div class="romk-box">
          <div class="romk-render">
            <span style="font-size:0.78rem;font-weight:700;color:var(--ink-muted);text-transform:uppercase;">Membran Sel Tubulus Distal Ginjal</span>
            <div class="romk-door plugged" id="romk-door">
              <span id="romk-txt">🔒 KANAL ROMK TERSUMBAT (Mg Normal)</span>
            </div>
            <span id="romk-urine" style="font-size:0.84rem;color:var(--sage);font-weight:600;">Kalium aman di darah, tidak bocor ke urin</span>
          </div>

          <div class="romk-switches">
            <button type="button" class="switch-btn active" id="sw-mg-norm" onclick="setROMK(true)">
              <span>Kadar Magnesium Normal (&gt;1.7 mg/dL)</span>
              <span>🔒 Tertutup</span>
            </button>
            <button type="button" class="switch-btn" id="sw-mg-low" onclick="setROMK(false)">
              <span>Magnesium Rendah (Akibat Diuretik / PPI)</span>
              <span>⚠️ Bocor</span>
            </button>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">
              Magnesium intraseluler adalah <b>sumbat alami kanal ROMK</b>. Bila sumbat Mg lepas, kanal ROMK terbuka lebar dan kalium bocor keluar ke urin. <b>Solusi: Koreksi Magnesium dan Kalium bersamaan!</b>
            </p>
          </div>
        </div>
      </article>

      <!-- SIMULATOR 3 -->
      <article class="sim-block">
        <div class="sim-head">
          <div class="sim-title-wrap">
            <h3>3. Refeeding Syndrome: Krisis ATP dalam 48 Jam</h3>
            <p>Bagaimana semangkuk bubur karbohidrat bisa memicu henti napas pada orang kelaparan.</p>
          </div>
          <button type="button" class="btn-intip-slide" onclick="openLightbox('slides_kul3/slide_19.jpg')">Intip Slide 19 ↗</button>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:12px;">
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ink-muted);">01. KELAPARAN</span>
            <div style="font-weight:700;margin:4px 0 6px;">Puasa Lama &gt;10 Hari</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Tubuh membakar lemak. Cadangan fosfat intraseluler habis total.</p>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--ochre);">02. MAKANAN MASUK</span>
            <div style="font-weight:700;color:var(--ochre);margin:4px 0 6px;">Karbohidrat Tiba-Tiba</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Pankreas menyemburkan <b>lonjakan Insulin masif</b> ke pembuluh darah.</p>
          </div>
          <div style="background:var(--bg);border:1px solid var(--border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--terracotta);">03. PENYEDOTAN</span>
            <div style="font-weight:700;color:var(--terracotta);margin:4px 0 6px;">Fosfat Masuk Sel</div>
            <p style="font-size:0.84rem;color:var(--ink-secondary);line-height:1.5;">Insulin memaksa <b>Fosfat (P), K, dan Mg</b> tersedot masuk ke intrasel.</p>
          </div>
          <div style="background:var(--terracotta-light);border:1px solid var(--terracotta-border);border-radius:var(--radius-md);padding:16px;">
            <span style="font-family:var(--font-mono);font-size:0.72rem;color:var(--terracotta);font-weight:700;">04. GAGAL NAPAS</span>
            <div style="font-weight:700;color:var(--terracotta);margin:4px 0 6px;">Fosfat Plasma &lt;1.0 mg/dL</div>
            <p style="font-size:0.84rem;color:#5D150B;line-height:1.5;">Sintesis ATP berhenti &rarr; <b>otot diafragma lumpuh tak bisa bernapas</b>.</p>
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
                <span>Transpor Oksigen Hemoglobin, Mioglobin, dan Enzim Sitokrom</span>
              </div>
              <span class="brand-tag" style="background:var(--terracotta);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Gejala Klinis Patognomonik</h4>
                <ul>
                  <li>Kelelahan, takikardia saat aktivitas ringan.</li>
                  <li><b>Pagophagia:</b> Keinginan kompulsif mengunyah es batu.</li>
                  <li>Kuku sendok (koilonychia) dan atrofi papil lidah (glossitis).</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Biomarker Kunci</h4>
                <ul>
                  <li><b>Ferritin &lt; 15–30 ng/mL:</b> Paling awal anjlok!</li>
                  <li>TSAT &lt; 16–20%, TIBC meningkat.</li>
                  <li>MCV mikrositik (&lt; 80 fL) di stadium lanjut.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Jebakan Ujian UAB dr. Iwal (Pedoman Terapi AGA 2024)</h4>
              <p>Pemberian tablet besi oral <b>maksimal 1x/hari pagi hari atau selang-hari (alternate-day)</b>. Dilarang 3x sehari karena setiap dosis memicu lonjakan hormon <b>Hepcidin</b> selama 24–48 jam yang mengunci ferroportin usus sehingga dosis berikutnya terbuang sia-sia.</p>
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
                <span>Kofaktor &gt;300 Metalloenzim, Imunitas, dan Regenerasi Epitel</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Trias Patognomonik Defisiensi</h4>
                <ul>
                  <li><b>Dermatitis periorifisial &amp; akral:</b> Ruam krusta di sekitar mulut, anus, ujung jari.</li>
                  <li><b>Diare kronik:</b> Akibat atrofi mikrovili mukosa usus.</li>
                  <li><b>Alopesia:</b> Kerontokan rambut menyeluruh.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Manifestasi Klinis Tambahan</h4>
                <ul>
                  <li>Luka lambat sembuh dan stunting pada anak.</li>
                  <li>Hilang sensasi pengecapan (hipogeusia).</li>
                  <li>Bentuk genetik mutasi ZIP4: <b>Acrodermatitis enteropathica</b>.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Faktor Risiko Penghambat Absorpsi</h4>
              <p>Diet tinggi <b>asam fitat</b> (serealia/gandum tak beragi) mengikat seng di lumen usus membentuk senyawa tak larut yang tidak dapat diserap enterosit. Sangat sering keluar pada soal anak dengan diet bubur sereal.</p>
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
                <span>Stabilitas Neuromuskular, Kofaktor ATP, dan Pengatur Transpor Ion Ginjal</span>
              </div>
              <span class="brand-tag" style="background:var(--navy);">Makromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Gejala Klinis (&lt;1.7 mg/dL)</h4>
                <ul>
                  <li>Tremor, kram otot, hiperrefleksia, tetani.</li>
                  <li>Aritmia ventrikel (Torsades de pointes).</li>
                  <li>Kejang bila hipomagnesemia berat.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Faktor Pemicu Utama</h4>
                <ul>
                  <li>Pemakaian diuretik loop (furosemid).</li>
                  <li>Obat maag PPI (omeprazole) menahun.</li>
                  <li>Diare kronik dan alkoholisme.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Jebakan Ujian UAB dr. Iwal: Hipokalemia Refrakter</h4>
              <p>Magnesium intraseluler adalah rem alami kanal <b>ROMK</b> tubulus ginjal. Bila Mg anjlok, kanal ROMK terbuka bebas tanpa kendali &rarr; kalium terus-menerus terbuang ke urin. <b>Kalium tidak akan pernah bisa naik bila Magnesium tidak dikoreksi secara serentak!</b></p>
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
                <span>Mineral Tulang (99%), Potensial Membran Saraf, dan Kontraksi Otot</span>
              </div>
              <span class="brand-tag" style="background:var(--navy);">Makromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Gejala Hipokalsemia Akut</h4>
                <ul>
                  <li>Parestesia perioral (kesemutan bibir) dan ujung jari.</li>
                  <li>Spasme karpopedal, tetani, laringospasme.</li>
                  <li><b>EKG:</b> Pemanjangan interval QT (risiko aritmia).</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Dua Tanda Fisik Patognomonik</h4>
                <ul>
                  <li><b>Tanda Chvostek:</b> Kedutan bibir saat saraf fasialis diketuk di anterior tragus telinga.</li>
                  <li><b>Tanda Trousseau:</b> Spasme karpopedal saat manset tensimeter dipompa &gt;sistolik 3 menit.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Poin Kritis Laboratorium</h4>
              <p>Hanya <b>Ionized Calcium (kalsium bebas 50%)</b> yang aktif secara fisiologis. Kadar kalsium total dipengaruhi oleh albumin serum.</p>
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
                <span>Sintesis Energi Seluler ATP, 2,3-DPG Eritrosit, dan Matriks Tulang</span>
              </div>
              <span class="brand-tag" style="background:var(--navy);">Makromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Refeeding Syndrome Kritis</h4>
                <ul>
                  <li>Lonjakan insulin memicu pergeseran fosfat masif ke intrasel.</li>
                  <li>Fosfat plasma anjlok <b>&lt; 1.0 mg/dL</b>.</li>
                  <li>Pembentukan ATP berhenti mendadak.</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Manifestasi Kegawatan Fatal</h4>
                <ul>
                  <li><b>Gagal napas akut</b> akibat kelemahan otot diafragma.</li>
                  <li>Kardiomiopati akut dan aritmia ventrikel.</li>
                  <li>Rabdomiolisis dan hemolisis eritrosit.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Pencegahan Sesuai Pedoman ASPEN &amp; NICE</h4>
              <p>Berikan <b>Tiamin (B1) sebelum makanan pertama dimulai</b>. Awali kalori rendah <b>10–15 kkal/kg/hari</b> bertahap. Pantau fosfat, kalium, dan magnesium serial tiap 12–24 jam.</p>
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
                <span>Komponen Ceruloplasmin, Transpor Besi, dan Integritas Mielin Saraf</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Trias Klinis Patognomonik</h4>
                <ul>
                  <li><b>Anemia mikrositik:</b> Ceruloplasmin gagal mengoksidasi besi untuk transferrin.</li>
                  <li><b>Neutropenia berat:</b> Penurunan granulosit di sumsum tulang.</li>
                  <li><b>Mielopati sensorik:</b> Ataksia gaya berjalan (menyerupai defisiensi B12).</li>
                </ul>
              </div>
              <div class="sheet-pane">
                <h4>Pemicu Iatrogenik Utama</h4>
                <ul>
                  <li>Konsumsi <b>suplemen Zinc dosis tinggi (&gt;50 mg/hari)</b> jangka panjang.</li>
                  <li>Operasi bariatrik bypass lambung.</li>
                  <li>Pemakaian lem perekat gigi palsu kaya zinc.</li>
                </ul>
              </div>
            </div>
            <div class="uab-trap-box">
              <h4>Mekanisme Interaksi Seng vs Tembaga</h4>
              <p>Seng berlebih merangsang sel usus memproduksi protein <b>metallothionein</b>. Protein ini mengikat tembaga dengan afinitas kuat &rarr; tembaga terperangkap di enterosit dan terbuang saat sel usus terkelupas.</p>
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
                <span>Bahan Baku Utama Hormon Tiroid T3 (Triiodotironin) dan T4 (Tiroksin)</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Dewasa: Struma Endemik</h4>
                <p>Iodium rendah &rarr; sintesis hormon tiroid turun &rarr; umpan balik negatif ke hipofisis berkurang &rarr; sekresi TSH melonjak &rarr; hipertrofi kelenjar tiroid (gondok).</p>
              </div>
              <div class="sheet-pane">
                <h4>Janin: Kretinisme Permanen</h4>
                <p>Kekurangan iodium pada ibu hamil menghambat neurogenesis otak janin &rarr; lahir dengan retardasi mental berat, tuli-bisu, dan perawakan pendek cebol.</p>
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
                <span>Komponen Asam Amino Selenosistein dalam Glutation Peroksidase</span>
              </div>
              <span class="brand-tag" style="background:var(--sage);">Mikromineral</span>
            </div>
            <div class="sheet-columns">
              <div class="sheet-pane">
                <h4>Penyakit Keshan (Kardiomiopati)</h4>
                <p>Kardiomiopati kongestif endemik di daerah tanah miskin selenium. Stres oksidatif memicu dilatasi ventrikel jantung dan gagal jantung pada anak dan wanita muda.</p>
              </div>
              <div class="sheet-pane">
                <h4>Fungsi Enzimatik Kunci</h4>
                <p>Antioksidan glutation peroksidase (GPx) melindungi membran sel dari radikal bebas H2O2, dan enzim deiodinase mengonversi T4 menjadi T3 aktif.</p>
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
    <!-- VIEW 4: CBT SUITE (100% BUG FREE & SATISFYING)                      -->
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
    function switchNav(viewId, btn) {
      document.querySelectorAll('.view-section').forEach(v => v.classList.remove('active'));
      document.querySelectorAll('.view-pill').forEach(b => b.classList.remove('active'));
      document.getElementById(viewId).classList.add('active');
      btn.classList.add('active');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // THE "WHY" ENIGMA REVELATION ENGINE
    const ENIGMAS = {
      1: {
        title: "Misteri 01 Terbuka: Refeeding Syndrome",
        text: "Saat seseorang kelaparan &gt;10 hari, sel-sel tubuhnya beralih ke pembakaran lemak dan cadangan fosfat intraselulernya habis total. Ketika kamu memberinya makan (terutama karbohidrat), pankreas langsung memompa <b>lonjakan insulin masif</b>. Insulin ini memaksa seluruh sisa Fosfat, Kalium, dan Magnesium di dalam darah masuk ke dalam sel. Akibatnya, kadar fosfat darah anjlok di bawah 1.0 mg/dL &rarr; sintesis ATP berhenti mendadak &rarr; <b>otot diafragma gagal berkontraksi (gagal napas)</b> dan pasien meninggal di tempat tidur. Niat baikmu membunuh pasien jika kamu tidak tahu cara mencegahnya (Tiamin dulu, mulai kalori 10–15 kkal/kg/hari)."
      },
      2: {
        title: "Misteri 02 Terbuka: Pagophagia & Kelaparan Besi di Otak",
        text: "Pasien perempuan 29 tahun dengan menstruasi banyak sering dilaporkan keluarga 'berperilaku aneh' mengunyah es batu berember-ember (<i>pagophagia</i>). Ini bukan gangguan jiwa, melainkan bentuk pica spesifik akibat deplesi atom Besi di mitokondria otak. Sensasi dingin di rongga mulut merangsang vasokonstriksi perifer dan meningkatkan perfusi darah ke lobus frontal otak yang sedang hipoksia. Menariknya, <b>kadar Hb dan MCV pasien saat ini bisa masih normal!</b> Karena yang habis terlebih dahulu adalah <b>Ferritin serum (&lt;15 ng/mL)</b> di sumsum tulang. Begitu kamu beri tablet besi oral, kebiasaan makan es batu itu hilang seketika."
      },
      3: {
        title: "Misteri 03 Terbuka: Gerbang ROMK Ginjal yang Bocor",
        text: "Pasien gagal jantung yang rutin minum furosemid sering mengalami aritmia karena kalium darahnya turun. Dokter jaga sering panik dan terus mengguyur KCl infus. Namun kalium darahnya tidak pernah naik. Mengapa? Karena furosemid membuang Kalium <i>sekaligus Magnesium</i>. Di dalam sel tubulus ginjal, ion Magnesium intraseluler adalah <b>sumbat fisik alami kanal ROMK</b>. Bila sumbat Magnesium lepas karena kadarnya rendah (&lt;1.7 mg/dL), gerbang ROMK terbuka lebar tanpa rem &rarr; kalium infus yang kamu masukkan akan langsung bocor terbuang ke urin. Pasien baru bisa selamat jika kamu <b>menginfus Magnesium sulfat bersamaan dengan Kalium</b>."
      }
    };

    function openEnigma(id) {
      const data = ENIGMAS[id];
      const box = document.getElementById('enigma-reveal-box');
      document.getElementById('reveal-title').innerHTML = data.title;
      document.getElementById('reveal-text').innerHTML = data.text;
      box.classList.add('open');
      box.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    function closeEnigma() {
      document.getElementById('enigma-reveal-box').classList.remove('open');
    }

    // SIMULATOR 1: IRON DEVIATION
    function setIron(stage) {
      document.querySelectorAll('.stager-btn').forEach((b, i) => {
        b.classList.toggle('active', i + 1 === stage);
      });

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

      if (stage === 1) {
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
      } else if (stage === 2) {
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
      } else {
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
      }
    }

    // SIMULATOR 2: ROMK KIDNEY CHANNEL
    function setROMK(isNormal) {
      document.getElementById('sw-mg-norm').classList.toggle('active', isNormal);
      document.getElementById('sw-mg-low').classList.toggle('active', !isNormal);

      const door = document.getElementById('romk-door');
      const txt = document.getElementById('romk-txt');
      const urine = document.getElementById('romk-urine');

      if (isNormal) {
        door.className = 'romk-door plugged';
        txt.textContent = '🔒 KANAL ROMK TERSUMBAT (Mg Normal)';
        urine.textContent = 'Kalium aman di darah, tidak bocor ke urin';
        urine.style.color = 'var(--sage)';
      } else {
        door.className = 'romk-door leaking';
        txt.textContent = '⚠️ KANAL ROMK TERBUKA LEBAR (Mg Rendah)';
        urine.textContent = '🚨 Kalium BOCOR TERBUANG KE URIN (Hipokalemia Refrakter!)';
        urine.style.color = 'var(--terracotta)';
      }
    }

    // MINERAL DECK SELECTOR
    function pickDeck(key, btn) {
      document.querySelectorAll('.sheet-card').forEach(s => s.classList.remove('active'));
      document.querySelectorAll('.deck-item').forEach(b => b.classList.remove('active'));
      document.getElementById('deck-' + key).classList.add('active');
      btn.classList.add('active');
    }

    // LIGHTBOX CONTROLLER
    function openLightbox(src) {
      const modal = document.getElementById('modal-lightbox');
      const img = document.getElementById('modal-lightbox-img');
      img.src = src;
      modal.classList.add('open');
    }
    function closeLightbox() {
      document.getElementById('modal-lightbox').classList.remove('open');
    }
    document.addEventListener('keydown', e => {
      if (e.key === 'Escape') closeLightbox();
    });

    // 8 SOAL PREDIKSI UAB (100% BUG FREE DYNAMIC EVALUATION)
    const CBT_DATA = [
      {
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
      },
      {
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
      },
      {
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
      },
      {
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
      },
      {
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
      },
      {
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
      },
      {
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
      },
      {
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
      }
    ];

    let userAnswers = {};
    let totalScore = 0;

    function renderCBT() {
      const container = document.getElementById('cbt-target-list');
      container.innerHTML = CBT_DATA.map((q, qIdx) => `
        <article class="q-card-box" id="q-card-${qIdx}">
          <span class="q-tag-line">SOAL #${q.id} · PREDIKSI UAB DR. IWAL</span>
          <div class="q-stem-body">${q.stem}</div>
          <div class="q-options-col">
            ${q.options.map((opt, oIdx) => `
              <button type="button" class="opt-choice-btn" onclick="selectAnswer(${qIdx}, ${oIdx})">
                <span class="opt-key-badge">${String.fromCharCode(65 + oIdx)}.</span>
                <span>${opt}</span>
              </button>
            `).join('')}
          </div>
          <div class="feedback-sheet" id="fb-sheet-${qIdx}"></div>
        </article>
      `).join('');
    }

    function selectAnswer(qIdx, chosenIdx) {
      if (userAnswers[qIdx] !== undefined) return;
      userAnswers[qIdx] = chosenIdx;

      const q = CBT_DATA[qIdx];
      const isCorrect = (chosenIdx === q.correct);
      const card = document.getElementById('q-card-' + qIdx);
      const btns = card.querySelectorAll('.opt-choice-btn');
      const sheet = document.getElementById('fb-sheet-' + qIdx);

      btns.forEach((btn, i) => {
        if (i === q.correct) btn.classList.add('is-correct');
        else if (i === chosenIdx && !isCorrect) btn.classList.add('is-wrong');
      });

      if (isCorrect) {
        totalScore++;
        sheet.className = 'feedback-sheet show tone-correct';
        sheet.innerHTML = `<strong>✅ Benar!</strong><div style="margin-top:6px;">${q.exp}</div>`;
      } else {
        sheet.className = 'feedback-sheet show tone-wrong';
        sheet.innerHTML = `<strong>❌ Kurang Tepat.</strong> Jawaban yang benar adalah <strong>${String.fromCharCode(65 + q.correct)} (${q.options[q.correct]})</strong>.<div style="margin-top:6px;">${q.exp}</div>`;
      }

      document.getElementById('cbt-score-display').textContent = totalScore;
    }

    document.addEventListener('DOMContentLoaded', () => {
      renderCBT();
    });
  </script>
</body>
</html>
"""

with open(OUT_HTML, "w", encoding="utf-8") as f:
    f.write(MAGNETIC_HTML)

print(f"Modul Magnetic 'Why-First' EMN KUL 3 berhasil dibuat di {OUT_HTML} (ukuran: {len(MAGNETIC_HTML)} bytes)")
