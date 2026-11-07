import os

BASE_DIR = "/Users/dimaswastu/VERTEX-PREP"

SHARED_CSS = """
    :root {
      --bg-page: #F4F6F8;
      --bg-surface: #FFFFFF;
      --bg-Subtle: #EEF2F5;
      --ink-primary: #0F1C24;
      --ink-secondary: #2A3B47;
      --ink-muted: #364958;
      --accent: #0F5C4D;
      --accent-soft: #E3F1EE;
      --warn: #A85B00;
      --warn-soft: #FDF3E3;
      --danger: #B42B22;
      --danger-soft: #FCECEB;
      --info: #175470;
      --info-soft: #E6F2F7;
      --border: #CFD9E0;
      --radius-lg: 14px;
      --radius-md: 10px;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-page);
      color: var(--ink-primary);
      font-family: 'Source Sans 3', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.6;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }

    /* Minimal Sticky Top Navigation */
    .topbar {
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
      padding: 12px 24px;
    }

    .topbar-inner {
      max-width: 1240px;
      margin: 0 auto;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .brand-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .lecture-Select {
      background: var(--bg-Subtle);
      border: 1px solid var(--border);
      color: var(--ink-primary);
      padding: 8px 14px;
      border-radius: 8px;
      font-family: inherit;
      font-size: 0.88rem;
      font-weight: 700;
      cursor: pointer;
    }

    .nav-tabs {
      display: flex;
      gap: 6px;
      background: var(--bg-Subtle);
      padding: 4px;
      border-radius: 10px;
    }

    .nav-tab {
      border: none;
      background: transparent;
      color: var(--ink-secondary);
      font-family: inherit;
      font-size: 0.86rem;
      font-weight: 700;
      padding: 8px 16px;
      border-radius: 7px;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .nav-tab.active {
      background: var(--bg-surface);
      color: var(--accent);
      box-shadow: 0 1px 3px rgba(17, 28, 36, 0.08);
    }

    .top-actions {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .search-btn {
      background: var(--bg-Subtle);
      color: var(--ink-primary);
      border: 1px solid var(--border);
      padding: 8px 14px;
      border-radius: 8px;
      font-family: inherit;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .search-btn:hover {
      border-color: var(--accent);
    }

    .search-btn kbd {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      padding: 1px 6px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
    }

    /* Main Container */
    .container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 28px 24px 80px;
    }

    /* Compact Header */
    .lecture-header {
      margin-bottom: 28px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border);
      display: flex;
      flex-wrap: wrap;
      align-items: flex-end;
      justify-content: space-between;
      gap: 20px;
    }

    .eyebrow {
      font-size: 0.76rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.07em;
      color: var(--accent);
      margin-bottom: 6px;
    }

    h1 {
      font-family: 'Newsreader', Georgia, serif;
      font-size: 2.25rem;
      line-height: 1.18;
      font-weight: 700;
      color: var(--ink-primary);
      margin-bottom: 8px;
    }

    h2 {
      font-size: 1.45rem;
      line-height: 1.28;
      font-weight: 700;
      color: var(--ink-primary);
    }

    h3 {
      font-size: 1.12rem;
      line-height: 1.35;
      font-weight: 700;
      color: var(--ink-primary);
    }

    .header-sub {
      color: var(--ink-secondary);
      font-size: 0.96rem;
      max-width: 68ch;
    }

    .header-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }

    .pill {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 12px;
      border-radius: 999px;
      font-size: 0.78rem;
      font-weight: 700;
    }

    .pill-green { background: var(--accent-soft); color: var(--accent); }
    .pill-red { background: var(--danger-soft); color: var(--danger); }
    .pill-amber { background: var(--warn-soft); color: var(--warn); }
    .pill-blue { background: var(--info-soft); color: var(--info); }

    .view-panel { display: none; }
    .view-panel.active { display: block; }

    /* Quick Jump Chips */
    .jump-bar {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 24px;
    }

    .jump-chip {
      text-decoration: none;
      background: var(--bg-surface);
      color: var(--ink-secondary);
      border: 1px solid var(--border);
      padding: 7px 14px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      transition: all 0.15s ease;
    }

    .jump-chip:hover {
      border-color: var(--accent);
      color: var(--accent);
    }

    /* Study Topic Row: Left = Complete Visual Digest, Right = Clean Slide Proof */
    .topic-block {
      display: grid;
      grid-template-columns: 1.65fr 1fr;
      gap: 24px;
      margin-bottom: 28px;
      align-items: start;
    }

    @media (max-width: 960px) {
      .topic-block {
        grid-template-columns: 1fr;
      }
    }

    .digest-pane {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px;
    }

    .digest-top {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 14px;
    }

    .topic-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      font-weight: 700;
      color: var(--accent);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .digest-lead {
      color: var(--ink-secondary);
      font-size: 0.95rem;
      margin: 8px 0 20px;
    }

    /* Visual Flow Diagram inside Digest */
    .flow-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(145px, 1fr));
      gap: 12px;
      margin-bottom: 20px;
    }

    .flow-step {
      background: var(--bg-Subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 20px;
    }

    .flow-step.step-focus {
      background: var(--accent-soft);
      border-color: #9ECBC0;
    }

    .flow-step.step-alert {
      background: var(--danger-soft);
      border-color: #E5B2AE;
    }

    .flow-step.step-warn {
      background: var(--warn-soft);
      border-color: #E8C99B;
    }

    .step-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--ink-muted);
      margin-bottom: 4px;
    }

    .step-title {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--ink-primary);
      margin-bottom: 4px;
    }

    .step-desc {
      font-size: 0.84rem;
      color: var(--ink-secondary);
      line-height: 1.45;
    }

    /* Clean Key Takeaways List */
    .takeaway-list {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 12px;
    }

    .takeaway-item {
      background: var(--bg-Subtle);
      border-radius: var(--radius-md);
      padding: 20px;
    }

    .takeaway-item.trap-box {
      background: var(--danger-soft);
    }

    .tk-label {
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent);
      margin-bottom: 6px;
    }

    .trap-box .tk-label {
      color: var(--danger);
    }

    .tk-text {
      font-size: 0.88rem;
      color: var(--ink-primary);
      line-height: 1.5;
    }

    /* Clean Slide Proof Pane (Right Side) */
    .proof-pane {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px;
      position: sticky;
      top: 76px;
    }

    .proof-header {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 8px;
      margin-bottom: 12px;
    }

    .proof-label {
      font-size: 0.76rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--ink-muted);
    }

    .slide-switcher {
      display: flex;
      flex-wrap: wrap;
      gap: 5px;
    }

    .slide-pill-btn {
      background: var(--bg-Subtle);
      border: 1px solid var(--border);
      color: var(--ink-secondary);
      padding: 4px 10px;
      border-radius: 6px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.74rem;
      font-weight: 700;
      cursor: pointer;
    }

    .slide-pill-btn.active {
      background: var(--accent);
      color: #FFFFFF;
      border-color: var(--accent);
    }

    .proof-img-wrap {
      position: relative;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border);
      cursor: zoom-in;
      background: #000;
    }

    .proof-img-wrap img {
      display: block;
      width: 100%;
      height: auto;
    }

    .proof-caption {
      margin-top: 10px;
      font-size: 0.82rem;
      color: var(--ink-secondary);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    /* Clean Comparison Table */
    .table-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 28px;
      overflow-x: auto;
    }

    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      font-size: 0.9rem;
    }

    th {
      text-align: left;
      padding: 12px 14px;
      background: var(--bg-Subtle);
      color: var(--ink-primary);
      font-weight: 700;
      border-bottom: 2px solid var(--border);
    }

    td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border);
      color: var(--ink-secondary);
      vertical-align: top;
    }

    /* CBT Quiz Section */
    .quiz-bar {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 20px 24px;
      margin-bottom: 24px;
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }

    .quiz-score {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--accent);
    }

    .filter-group {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
    }

    .filter-btn {
      background: var(--bg-Subtle);
      border: 1px solid var(--border);
      color: var(--ink-secondary);
      padding: 7px 13px;
      border-radius: 8px;
      font-family: inherit;
      font-size: 0.82rem;
      font-weight: 700;
      cursor: pointer;
    }

    .filter-btn.active {
      background: var(--accent);
      color: #FFFFFF;
      border-color: var(--accent);
    }

    .q-item {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 28px;
      margin-bottom: 20px;
    }

    .q-meta {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 14px;
    }

    .q-stem {
      font-size: 1.02rem;
      font-weight: 600;
      color: var(--ink-primary);
      margin-bottom: 18px;
      line-height: 1.6;
    }

    .opt-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .opt-btn {
      text-align: left;
      background: var(--bg-Subtle);
      border: 1px solid var(--border);
      border-radius: var(--radius-md);
      padding: 13px 16px;
      font-family: inherit;
      font-size: 0.92rem;
      color: var(--ink-primary);
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 12px;
      transition: all 0.12s ease;
    }

    .opt-btn:hover {
      border-color: var(--accent);
      background: #FFFFFF;
    }

    .opt-btn.correct {
      background: var(--accent-soft);
      border-color: var(--accent);
      font-weight: 700;
    }

    .opt-btn.wrong {
      background: var(--danger-soft);
      border-color: var(--danger);
    }

    .opt-letter {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      color: var(--accent);
      min-width: 22px;
    }

    .q-feedback {
      display: none;
      margin-top: 20px;
      padding-top: 20px;
      border-top: 1px solid var(--border);
      grid-template-columns: 1.45fr 1fr;
      gap: 20px;
      align-items: start;
    }

    .q-feedback.open {
      display: grid;
    }

    @media (max-width: 860px) {
      .q-feedback.open {
        grid-template-columns: 1fr;
      }
    }

    .fb-text {
      font-size: 0.92rem;
      color: var(--ink-secondary);
      line-height: 1.6;
    }

    .fb-slide-img {
      width: 100%;
      border-radius: 8px;
      border: 1px solid var(--border);
      cursor: zoom-in;
    }

    /* Rapid Recall Cards (Mode 3) */
    .recall-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 20px;
    }

    .recall-card {
      background: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: var(--radius-lg);
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 14px;
    }

    .recall-q {
      font-weight: 700;
      font-size: 1rem;
      color: var(--ink-primary);
    }

    .recall-a {
      display: none;
      padding-top: 14px;
      border-top: 1px solid var(--border);
      font-size: 0.9rem;
      color: var(--accent);
      font-weight: 600;
    }

    .recall-card.revealed .recall-a {
      display: block;
    }

    .reveal-btn {
      align-self: flex-start;
      background: var(--bg-Subtle);
      border: 1px solid var(--border);
      color: var(--ink-primary);
      padding: 7px 14px;
      border-radius: 7px;
      font-family: inherit;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
    }

    /* Full Slide Drawer Modal */
    .lightbox {
      position: fixed;
      inset: 0;
      background: rgba(17, 28, 36, 0.86);
      z-index: 9999;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .lightbox.open { display: flex; }

    .lightbox-box {
      max-width: 1080px;
      width: 100%;
      background: var(--bg-surface);
      border-radius: var(--radius-lg);
      padding: 20px;
    }

    .lightbox-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 12px;
    }

    .lightbox-box img {
      width: 100%;
      max-height: 80vh;
      object-fit: contain;
      border-radius: 8px;
    }

    /* Clean Cmd+K Modal */
    .cmdk-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(17, 28, 36, 0.72);
      z-index: 9998;
      display: none;
      align-items: flex-start;
      justify-content: center;
      padding: 64px 20px 20px;
    }
    .cmdk-backdrop.open { display: flex; }
    .cmdk-dialog {
      width: 100%;
      max-width: 820px;
      background: #FFFFFF;
      border-radius: 14px;
      border: 1px solid var(--border);
      overflow: hidden;
      max-height: 78vh;
      display: flex;
      flex-direction: column;
    }
    .cmdk-top {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 16px 20px;
      border-bottom: 1px solid var(--border);
    }
    .cmdk-input {
      flex: 1;
      border: none;
      font-family: inherit;
      font-size: 1rem;
      outline: none;
      color: var(--ink-primary);
    }
    .cmdk-list {
      overflow-y: auto;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
    .cmdk-row {
      padding: 14px;
      border: 1px solid var(--border);
      border-radius: 10px;
      display: flex;
      gap: 14px;
      align-items: flex-start;
    }
    .cmdk-row img {
      width: 96px;
      border-radius: 6px;
      border: 1px solid var(--border);
    }
    .cmdk-row mark {
      background: #FDE68A;
      padding: 0 2px;
      border-radius: 3px;
    }
"""

SHARED_JS = """
  function switchTab(tabId, btn) {
    document.querySelectorAll('.view-panel').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
    document.getElementById('panel-' + tabId).classList.add('active');
    btn.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function swapSlide(topicId, slidePath, slideLabel, btn) {
    const img = document.getElementById('proof-img-' + topicId);
    const cap = document.getElementById('proof-cap-' + topicId);
    if (img) img.src = slidePath;
    if (cap) cap.textContent = slideLabel;
    const parent = btn.parentElement;
    parent.querySelectorAll('.slide-pill-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }

  function zoomSlide(src, title) {
    document.getElementById('lb-img').src = src;
    document.getElementById('lb-title').textContent = title || 'Bukti Slide Asli Dosen';
    document.getElementById('lightbox').classList.add('open');
  }

  function closeLightbox() {
    document.getElementById('lightbox').classList.remove('open');
  }

  // Persistent Simple Quiz Logic
  const STORAGE_KEY = 'vertex_clean_quiz_' + window.MODULE_ID;
  let savedAnswers = {};
  try {
    savedAnswers = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
  } catch (e) {}

  function selectOption(qIdx, optIdx) {
    savedAnswers[qIdx] = optIdx;
    try { localStorage.setItem(STORAGE_KEY, JSON.stringify(savedAnswers)); } catch (e) {}
    renderQuizState();
  }

  function resetQuiz() {
    savedAnswers = {};
    try { localStorage.removeItem(STORAGE_KEY); } catch (e) {}
    renderQuizState();
  }

  function filterQuiz(cat, btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    document.querySelectorAll('.q-item').forEach(item => {
      if (cat === 'all' || item.dataset.cat === cat) {
        item.style.display = 'block';
      } else {
        item.style.display = 'none';
      }
    });
  }

  function renderQuizState() {
    let correctCount = 0;
    let answeredCount = 0;
    window.QUESTIONS.forEach((q, idx) => {
      const chosen = savedAnswers[idx];
      const card = document.getElementById('qcard-' + idx);
      if (!card) return;
      const buttons = card.querySelectorAll('.opt-btn');
      const fb = document.getElementById('qfb-' + idx);
      buttons.forEach((b, bIdx) => {
        b.classList.remove('correct', 'wrong');
        if (chosen !== undefined) {
          if (bIdx === q.ans) b.classList.add('correct');
          else if (bIdx === chosen && chosen !== q.ans) b.classList.add('wrong');
        }
      });
      if (chosen !== undefined) {
        answeredCount++;
        if (chosen === q.ans) correctCount++;
        if (fb) fb.classList.add('open');
      } else {
        if (fb) fb.classList.remove('open');
      }
    });
    const scoreEl = document.getElementById('quiz-score-label');
    if (scoreEl) {
      scoreEl.textContent = `Progres Tersimpan: ${answeredCount}/${window.QUESTIONS.length} Dijawab · ${correctCount} Benar`;
    }
  }

  // Cmd + K Search across 51 UAB files & slides
  function openCmdK() {
    document.getElementById('cmdk-modal').classList.add('open');
    const inp = document.getElementById('cmdk-input');
    inp.focus();
    runCmdKSearch();
  }
  function closeCmdK() {
    document.getElementById('cmdk-modal').classList.remove('open');
  }
  function runCmdKSearch() {
    const q = (document.getElementById('cmdk-input').value || '').trim().toLowerCase();
    const list = document.getElementById('cmdk-list');
    const idx = window.VERTEX_SEARCH_INDEX || [];
    const tokens = q.split(/\\s+/).filter(Boolean);
    const hits = [];
    for (let i = 0; i < idx.length; i++) {
      const it = idx[i];
      if (tokens.length) {
        const hay = (it.source + ' ' + it.block + ' ' + it.text).toLowerCase();
        if (!tokens.every(t => hay.includes(t))) continue;
      }
      hits.push(it);
      if (hits.length >= 30) break;
    }
    if (!hits.length) {
      list.innerHTML = '<div style="padding:20px;color:#647786;text-align:center;">Tidak ditemukan hasil. Coba kata kunci seperti Sentinel, KCl, Gelang, B12, Metformin, Anemia.</div>';
      return;
    }
    list.innerHTML = hits.map(h => `
      <div class="cmdk-row">
        ${h.img ? `<img src="${h.img}" alt="Slide" onclick="closeCmdK();zoomSlide('${h.img}','${h.source}')" style="cursor:zoom-in" />` : ''}
        <div>
          <div style="font-size:0.74rem;font-weight:700;color:#0F5C4D;margin-bottom:3px;">${h.type} · ${h.block} · ${h.source}</div>
          <div style="font-size:0.88rem;color:#111C24;">${h.text}</div>
        </div>
      </div>
    `).join('');
  }

  document.addEventListener('keydown', e => {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
      e.preventDefault();
      openCmdK();
    } else if (e.key === 'Escape') {
      closeLightbox();
      closeCmdK();
    }
  });

  document.addEventListener('DOMContentLoaded', () => {
    renderQuizState();
  });
"""

# ==============================================================================
# MODULE 1: BDT KUL 3 PATIENT SAFETY (SUPER CLEAN & POWERFUL)
# ==============================================================================
BDT_HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BDT Kuliah 3 · Patient Safety — Belajar Tanpa Buka PPT</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600;700&family=Newsreader:opsz,wght@6..72,600;6..72,700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>{SHARED_CSS}</style>
</head>
<body>

  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-group">
        <select class="lecture-Select" aria-label="Pilih Kuliah" onchange="window.location.href=this.value">
          <option value="BDT_KUL3_Patient_Safety.html" selected>Blok 7 BDT · Kuliah 3: Patient Safety (dr. Riskiyah)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html">Blok 9 EMN · Kuliah 2: Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
        </select>
      </div>

      <nav class="nav-tabs" aria-label="Mode Belajar">
        <button type="button" class="nav-tab active" onclick="switchTab('materi', this)">1. Materi Visual (Pengganti 80 Slide)</button>
        <button type="button" class="nav-tab" onclick="switchTab('soal', this)">2. Latihan Soal Asli UAB (9 Soal)</button>
        <button type="button" class="nav-tab" onclick="switchTab('recall', this)">3. Cek Cepat H-1 Ujian</button>
      </nav>

      <div class="top-actions">
        <button type="button" class="search-btn" onclick="openCmdK()">
          <span>Cari Bank Soal UAB</span>
          <kbd>⌘K</kbd>
        </button>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="lecture-header">
      <div>
        <div class="eyebrow">Blok 7 · Dasar Diagnosis & Terapi (BDT) · Kuliah Pakar 3</div>
        <h1>Patient Safety (Keselamatan Pasien)</h1>
        <p class="header-sub">Seluruh isi <strong>80 slide dr. Riskiyah, MMRS</strong> telah dipadatkan menjadi <strong>7 Bab Visual Inti</strong> di bawah ini. Anda tidak perlu membuka file PPT asli lagi; bukti tangkapan layar slide dosen tersedia langsung di samping tiap bab.</p>
      </div>
      <div class="header-pills">
        <span class="pill pill-green">80 Slide → 7 Bab Visual</span>
        <span class="pill pill-red">9 Soal Asli UAB & Remidi BDT</span>
        <span class="pill pill-blue">Waktu Kuasai: ±20 Menit</span>
      </div>
    </section>

    <!-- =================================================================== -->
    <!-- PANEL 1: MATERI VISUAL PADAT (PENGGANTI 80 SLIDE PPT)               -->
    <!-- =================================================================== -->
    <div id="panel-materi" class="view-panel active">

      <div class="jump-bar">
        <a href="#bab-1" class="jump-chip">01 · 5 Jenis Insiden (3 Soal UAB)</a>
        <a href="#bab-2" class="jump-chip">02 · 7 Standar vs 6 SKP vs 7 Langkah (2 Soal UAB)</a>
        <a href="#bab-3" class="jump-chip">03 · SKP 1 Identifikasi & Gelang (1 Soal UAB)</a>
        <a href="#bab-4" class="jump-chip">04 · SKP 2 Komunikasi TBaK & SBAR</a>
        <a href="#bab-5" class="jump-chip">05 · SKP 3 Obat High-Alert & KCl (1 Soal UAB)</a>
        <a href="#bab-6" class="jump-chip">06 · SKP 4 Operasi & Time-Out (1 Soal UAB)</a>
        <a href="#bab-7" class="jump-chip">07 · SKP 5-6 & Pelaporan RCA (2 Soal UAB)</a>
      </div>

      <!-- BAB 1 -->
      <article id="bab-1" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 01 · Merangkum Slide 1–22</span>
            <span class="pill pill-red">Keluar di 3 Soal Asli UAB BDT</span>
          </div>
          <h2>Tangga 5 Insiden Keselamatan Pasien</h2>
          <p class="digest-lead">Kunci membedakan 5 jenis insiden di ujian hanya ada pada 2 pertanyaan: <strong>(1) Apakah sudah terpapar ke tubuh pasien?</strong> dan <strong>(2) Apakah timbul cedera/kematian?</strong></p>

          <div class="flow-strip">
            <div class="flow-step step-warn">
              <div class="step-code">1 · Belum Insiden</div>
              <div class="step-title">KPC (Potensial)</div>
              <div class="step-desc">Kondisi berpotensi cedera, belum ada tindakan salah. <em>Contoh: alat defibrilator rusak di IGD, lantai licin.</em></div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">2 · Belum Ke Pasien</div>
              <div class="step-title">KNC (Near Miss)</div>
              <div class="step-desc">Kesalahan sudah terjadi tetapi <strong>ketahuan sebelum mengenai pasien</strong>. <em>Contoh: salah siapkan obat tapi belum diminum.</em></div>
            </div>
            <div class="flow-step">
              <div class="step-code">3 · Terpapar, Aman</div>
              <div class="step-title">KTC (Tanpa Cedera)</div>
              <div class="step-desc">Sudah terpapar ke pasien, tetapi <strong>pasien tidak mengalami cedera</strong> sama sekali.</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">4 · Pasien Cedera</div>
              <div class="step-title">KTD (Adverse)</div>
              <div class="step-desc">Pasien sudah terpapar dan <strong>mengalami cedera ringan/sedang</strong> yang reversibel.</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">5 · Kematian / Cacat</div>
              <div class="step-title">Sentinel Event</div>
              <div class="step-desc">KTD fatal yang berujung <strong>kematian, cacat permanen, salah sisi operasi, atau bayi tertukar</strong>.</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item">
              <div class="tk-label">Inti Slide 18–20</div>
              <div class="tk-text">Prinsip dasar keselamatan pasien adalah <em>Do No Harm</em> (Slide 19). Semua insiden (KNC, KTD, Sentinel) wajib dicatat untuk perbaikan sistem.</div>
            </div>
            <div class="takeaway-item trap-box">
              <div class="tk-label">Jebakan Soal UAB Asli</div>
              <div class="tk-text">Di <strong>UAB BDT Axonation No. 29 & UAB 22 No. 70</strong>, pasien disuntik Antalgin → syok anafilaktik → <strong>meninggal dunia</strong>. Karena berakhir kematian, jawabannya wajib <strong>Kejadian Sentinel</strong> (bukan KTD biasa).</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b1', 'slides_bdt_kul3/slide_18.jpg', 'Slide 18 · Definisi Resmi 5 Insiden (KTD, KNC, KTC, KPC, Sentinel)', this)">Slide 18</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b1', 'slides_bdt_kul3/slide_19.jpg', 'Slide 19 · Prinsip Utama: Do No Harm', this)">Slide 19</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b1', 'slides_bdt_kul3/slide_20.jpg', 'Slide 20 · 4 Tujuan Patient Safety di RS', this)">Slide 20</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b1').src, document.getElementById('proof-cap-b1').textContent)">
            <img id="proof-img-b1" src="slides_bdt_kul3/slide_18.jpg" alt="Bukti Slide 18" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b1">Slide 18 · Definisi Resmi 5 Insiden</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 2: TABEL PEMBEDA 3 KERANGKA (PENYUMBANG 2 SOAL UAB) -->
      <article id="bab-2" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 02 · Merangkum Slide 23–33 & Slide 60–68</span>
            <span class="pill pill-red">Keluar di 2 Soal Asli UAB BDT (No. 32 & 44)</span>
          </div>
          <h2>Pembeda 7 Standar vs 6 SKP vs 7 Langkah</h2>
          <p class="digest-lead">Ini adalah jebakan favorit dosen di UAB BDT: soal menanyakan <strong>"Yang termasuk 7 Standar Keselamatan Pasien adalah..."</strong>, lalu 4 opsi pengecohnya diambil dari <strong>7 Langkah (Slide 61)</strong>.</p>

          <table>
            <thead>
              <tr>
                <th>7 Standar Keselamatan Pasien<br><small>(Slide 23–24 · Kata Benda)</small></th>
                <th>6 Sasaran Keselamatan Pasien / SKP<br><small>(Slide 32–33 · Tindakan Klinis)</small></th>
                <th>7 Langkah Menuju Keselamatan Pasien<br><small>(Slide 61 · Kata Kerja Aktif)</small></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1. <strong>Hak pasien</strong> <em>(Keluar di UAB No. 44)</em></td>
                <td>1. Ketepatan identifikasi pasien</td>
                <td>1. Membangun kesadaran nilai keselamatan</td>
              </tr>
              <tr>
                <td>2. Pendidikan bagi pasien dan keluarga</td>
                <td>2. Peningkatan komunikasi yang efektif</td>
                <td>2. <strong>Memimpin dan mendukung staf</strong> <em>(Pengecoh!)</em></td>
              </tr>
              <tr>
                <td>3. Keselamatan pasien dlm kesinambungan layanan</td>
                <td>3. Peningkatan keamanan obat <em>High-Alert</em></td>
                <td>3. Mengintegrasikan aktivitas pengelolaan risiko</td>
              </tr>
              <tr>
                <td>4. Penggunaan metode peningkatan kinerja</td>
                <td>4. Kepastian tepat-lokasi, prosedur, pasien operasi</td>
                <td>4. <strong>Mengembangkan sistem pelaporan</strong> <em>(Pengecoh!)</em></td>
              </tr>
              <tr>
                <td>5. <strong>Peran kepemimpinan</strong> dlm keselamatan <em>(UAB No. 32)</em></td>
                <td>5. Pengurangan risiko infeksi (<em>Hand Hygiene</em>)</td>
                <td>5. Melibatkan & berkomunikasi dengan pasien</td>
              </tr>
              <tr>
                <td>6. Pendidikan bagi staf tentang keselamatan pasien</td>
                <td>6. Pengurangan risiko cedera pasien jatuh</td>
                <td>6. Belajar & berbagi pengalaman (RCA)</td>
              </tr>
              <tr>
                <td>7. Komunikasi merupakan kunci bagi staf</td>
                <td>— <em>(Hanya 6 Sasaran)</em></td>
                <td>7. Mencegah cedera melalui implementasi sistem</td>
              </tr>
            </tbody>
          </table>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b2', 'slides_bdt_kul3/slide_23.jpg', 'Slide 23 · 7 Standar Keselamatan Pasien (Standar 1–4)', this)">Slide 23</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b2', 'slides_bdt_kul3/slide_24.jpg', 'Slide 24 · 7 Standar Keselamatan Pasien (Standar 5–7)', this)">Slide 24</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b2', 'slides_bdt_kul3/slide_61.jpg', 'Slide 61 · 7 Langkah Keselamatan Pasien (Sering Jadi Pengecoh!)', this)">Slide 61</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b2').src, document.getElementById('proof-cap-b2').textContent)">
            <img id="proof-img-b2" src="slides_bdt_kul3/slide_23.jpg" alt="Bukti Slide 23" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b2">Slide 23 · 7 Standar Keselamatan Pasien</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 3: SKP 1 IDENTIFIKASI & GELANG -->
      <article id="bab-3" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 03 · Merangkum Slide 32, 34–38</span>
            <span class="pill pill-red">Keluar di Soal UAB BDT-1 Hal. 5</span>
          </div>
          <h2>SKP 1: Ketepatan Identifikasi & 4 Warna Gelang</h2>
          <p class="digest-lead">Wajib memakai minimal <strong>2 dari 4 identitas resmi</strong> (Nama lengkap, Tanggal lahir, Nomor Rekam Medis, NIK). <strong>Dilarang keras</strong> mengidentifikasi pasien menggunakan nomor kamar atau nomor tempat tidur.</p>

          <div class="flow-strip">
            <div class="flow-step">
              <div class="step-code">Gelang Biru</div>
              <div class="step-title">Pasien Laki-Laki</div>
              <div class="step-desc">Dipasang di pergelangan tangan saat admisi rawat inap.</div>
            </div>
            <div class="flow-step">
              <div class="step-code">Gelang Pink</div>
              <div class="step-title">Pasien Perempuan</div>
              <div class="step-desc">Identitas pasien perempuan rawat inap.</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">Gelang Merah</div>
              <div class="step-title">Riwayat Alergi</div>
              <div class="step-desc">Menandakan pasien memiliki alergi obat/makanan derajat tinggi.</div>
            </div>
            <div class="flow-step step-warn">
              <div class="step-code">Gelang Kuning</div>
              <div class="step-title">Risiko Jatuh</div>
              <div class="step-desc">Pasien berisiko tinggi jatuh (Skala Morse / Humpty Dumpty).</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item">
              <div class="tk-label">Kapan Wajib Identifikasi? (Slide 37)</div>
              <div class="tk-text">Sebelum: (1) Pemberian obat, (2) Transfusi darah/produk darah, (3) Pengambilan sampel darah/spesimen lab, (4) Tindakan invasif & operasi.</div>
            </div>
            <div class="takeaway-item trap-box">
              <div class="tk-label">Cara Bertanya yang Benar (Slide 34)</div>
              <div class="tk-text">Wajib kalimat terbuka: <strong>"Siapa nama Bapak?"</strong> (Verbal aktif). Jangan bertanya tertutup <em>"Apakah Bapak Tn. Budi?"</em> karena pasien lansia/mengantuk sering mengangguk saja.</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b3', 'slides_bdt_kul3/slide_35.jpg', 'Slide 35 · Foto Gelang Merah (Alergi), Kuning (Jatuh), dan Biru (Laki-laki)', this)">Slide 35</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b3', 'slides_bdt_kul3/slide_34.jpg', 'Slide 34 · Aturan 2 Identitas & Pertanyaan Terbuka', this)">Slide 34</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b3', 'slides_bdt_kul3/slide_37.jpg', 'Slide 37 · 4 Momen Wajib Identifikasi Pasien', this)">Slide 37</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b3').src, document.getElementById('proof-cap-b3').textContent)">
            <img id="proof-img-b3" src="slides_bdt_kul3/slide_35.jpg" alt="Bukti Slide 35" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b3">Slide 35 · Foto 3 Gelang Pasien</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 4: SKP 2 KOMUNIKASI EFEKTIF -->
      <article id="bab-4" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 04 · Merangkum Slide 39–42</span>
            <span class="pill pill-blue">SKP 2 · Komunikasi Tim Medis</span>
          </div>
          <h2>SKP 2: Komunikasi Efektif (TBaK & SBAR)</h2>
          <p class="digest-lead">Instruksi lisan atau lewat telepon adalah titik paling rawan salah dengar nama obat (LASA) dan dosis. Karena itu wajib mengikuti protokol <strong>TBaK (Tulis – Baca Ulang – Konfirmasi)</strong>.</p>

          <div class="flow-strip">
            <div class="flow-step">
              <div class="step-code">Langkah 1 · Tulis</div>
              <div class="step-title">Write Down</div>
              <div class="step-desc">Penerima pesan menulis lengkap nama obat, dosis, rute, dan frekuensi di rekam medis.</div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">Langkah 2 · Baca</div>
              <div class="step-title">Read Back & Eja</div>
              <div class="step-desc">Membacakan kembali isi catatan; untuk obat <em>Sound-Alike</em> wajib dieja huruf demi huruf.</div>
            </div>
            <div class="flow-step step-warn">
              <div class="step-code">Langkah 3 · Paraf</div>
              <div class="step-title">Konfirmasi 1x24 Jam</div>
              <div class="step-desc">DPJP pemberi instruksi wajib membubuhkan paraf pada stempel <strong>NOTASI</strong> maksimal 1x24 jam.</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item">
              <div class="tk-label">Kerangka SBAR (Slide 41–42)</div>
              <div class="tk-text"><strong>S</strong>ituation (keluhan utama saat ini) → <strong>B</strong>ackground (riwayat klinis/terapi) → <strong>A</strong>ssessment (penilaian tanda vital/lab) → <strong>R</strong>ecommendation (usulan tindakan ke DPJP).</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b4', 'slides_bdt_kul3/slide_41.jpg', 'Slide 41 · Rekam Medis SBAR & Stempel Notasi DPJP', this)">Slide 41</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b4', 'slides_bdt_kul3/slide_42.jpg', 'Slide 42 · Syarat Medication Order Lengkap', this)">Slide 42</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b4').src, document.getElementById('proof-cap-b4').textContent)">
            <img id="proof-img-b4" src="slides_bdt_kul3/slide_41.jpg" alt="Bukti Slide 41" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b4">Slide 41 · Rekam Medis SBAR & Notasi</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 5: SKP 3 HIGH ALERT -->
      <article id="bab-5" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 05 · Merangkum Slide 43–50</span>
            <span class="pill pill-red">Keluar di Soal Remidi BDT No. 39</span>
          </div>
          <h2>SKP 3: Keamanan Obat High-Alert & Elektrolit Pekat</h2>
          <p class="digest-lead">Obat <strong>High-Alert</strong> adalah obat yang paling sering menyebabkan cedera serius/kematian bila terjadi kesalahan pemberian. Mencakup 3 kelompok: <strong>Elektrolit Konsentrat</strong>, <strong>LASA (NORUM)</strong>, dan <strong>Sitostatika/Insulin/Heparin</strong>.</p>

          <div class="flow-strip">
            <div class="flow-step step-alert">
              <div class="step-code">Elektrolit Pekat #1</div>
              <div class="step-title">KCl Pekat (≥2 mEq/mL)</div>
              <div class="step-desc"><em>Concentrated Potassium Chloride</em>. Jika disuntik bolus IV langsung → henti jantung mendadak (Sentinel).</div>
            </div>
            <div class="flow-step step-warn">
              <div class="step-code">Elektrolit Pekat #2–4</div>
              <div class="step-title">NaCl >0,9% & MgSO4</div>
              <div class="step-desc">Termasuk Glukosa Hipertonik (≥20%), MgSO4 ≥20%, dan Natrium Bikarbonat pekat.</div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">Aturan Penyimpanan</div>
              <div class="step-title">Tarik dari Bangsal!</div>
              <div class="step-desc">Dilarang disimpan di ruang rawat biasa; hanya boleh di Instalasi Farmasi / troli emergensi terkunci.</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item trap-box">
              <div class="tk-label">Bedah Soal Remidi BDT No. 39 (Slide 48)</div>
              <div class="tk-text">Dosen menanyakan: <em>"Label yang diberikan pada Concentrated Potassium Chloride adalah..."</em><br>Perhatikan gambar botol di <strong>Slide 48</strong>: tulisan besar di badan botolnya adalah <strong>HIGH ALERT! MEDICATION</strong>. Dosen mengambil tulisan kotak biru di samping botol (<em>Distinct Packaging</em> & <em>Prominent Warning</em>) sebagai opsi pengecoh!</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b5', 'slides_bdt_kul3/slide_48.jpg', 'Slide 48 · Botol HIGH ALERT! MEDICATION (Sumber Soal Remidi No. 39)', this)">Slide 48</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b5', 'slides_bdt_kul3/slide_46.jpg', 'Slide 46 · Daftar Cairan High Concentration (KCl, Heparin, NaCl)', this)">Slide 46</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b5', 'slides_bdt_kul3/slide_47.jpg', 'Slide 47 · 5 Langkah Mengurangi Risiko High-Alert', this)">Slide 47</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b5').src, document.getElementById('proof-cap-b5').textContent)">
            <img id="proof-img-b5" src="slides_bdt_kul3/slide_48.jpg" alt="Bukti Slide 48" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b5">Slide 48 · Botol HIGH ALERT! MEDICATION</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 6: SKP 4 OPERASI AMAN -->
      <article id="bab-6" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 06 · Merangkum Slide 51–54</span>
            <span class="pill pill-red">Keluar di UAB BDT Axonation No. 43</span>
          </div>
          <h2>SKP 4: Tepat Lokasi, Prosedur, & Pasien Operasi</h2>
          <p class="digest-lead">Untuk mencegah salah sisi/lokasi operasi (<em>Wrong-Site Surgery</em>), wajib dilakukan <strong>Penandaan Lokasi (Surgical Marking)</strong> dan prosedur jeda <strong>Surgical Time-Out</strong>.</p>

          <div class="flow-strip">
            <div class="flow-step">
              <div class="step-code">Di Ruang Rawat</div>
              <div class="step-title">Surgical Marking</div>
              <div class="step-desc">Dilakukan oleh dokter operator dengan <strong>melibatkan pasien saat masih sadar</strong> untuk organ bilateral/multipel.</div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">Di Kamar Operasi</div>
              <div class="step-title">Surgical Time-Out</div>
              <div class="step-desc">Verifikasi aktif seluruh tim (bedah, anestesi, perawat) <strong>tepat sebelum insisi kulit dimulai</strong>.</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">Penyebab Error #1</div>
              <div class="step-title">Komunikasi Buruk</div>
              <div class="step-desc">Tertulis nomor 1 di Slide 54: <strong>Komunikasi yang tidak efektif antara anggota tim bedah</strong>.</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item trap-box">
              <div class="tk-label">Bedah Soal UAB BDT Axonation No. 43 (Slide 54)</div>
              <div class="tk-text">Kasus pasien operasi thoraks tetapi kaki ikut dioperasi. Sesuai <strong>Slide 54 urutan ke-1</strong>, penyebab utamanya adalah <strong>komunikasi tidak efektif antar tim medis/bedah</strong> serta tidak dilakukannya verifikasi <em>Time-Out</em> sebelum insisi.</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b6', 'slides_bdt_kul3/slide_54.jpg', 'Slide 54 · Causes of Surgical Errors (Sumber Soal UAB No. 43)', this)">Slide 54</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b6', 'slides_bdt_kul3/slide_51.jpg', 'Slide 51 · 6 Ceklis Verifikasi & Time-Out Sebelum Operasi', this)">Slide 51</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b6', 'slides_bdt_kul3/slide_52.jpg', 'Slide 52 · Prosedur Surgical Timeout', this)">Slide 52</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b6').src, document.getElementById('proof-cap-b6').textContent)">
            <img id="proof-img-b6" src="slides_bdt_kul3/slide_54.jpg" alt="Bukti Slide 54" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b6">Slide 54 · Causes of Surgical Errors</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 7: SKP 5, SKP 6, PELAPORAN 2x24 JAM & RCA -->
      <article id="bab-7" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 07 · Merangkum Slide 55–59 & Slide 69–80</span>
            <span class="pill pill-red">Keluar di UAB 22 No. 85 & Remidi Costa No. 36</span>
          </div>
          <h2>SKP 5–6, Pelaporan 2x24 Jam, Grading Risiko & RCA</h2>
          <p class="digest-lead">Setiap insiden (KNC, KTD, Sentinel) wajib dilaporkan ke Tim Keselamatan Pasien RS maksimal <strong>2 x 24 jam</strong>. Tindak lanjutnya ditentukan oleh <strong>Warna Grading Risiko</strong>:</p>

          <div class="flow-strip">
            <div class="flow-step">
              <div class="step-code">SKP 5 · Infeksi</div>
              <div class="step-title">5 Moments Hand Hygiene</div>
              <div class="step-desc">2 Sebelum (kontak pasien & tindakan aseptik) + 3 Sesudah (cairan tubuh, kontak pasien, lingkungan pasien) + Injeksi aman (<em>single-use</em>).</div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">Grading Biru / Hijau</div>
              <div class="step-title">Investigasi Sederhana</div>
              <div class="step-desc">Dilakukan oleh atasan langsung di unit kerja (Biru maks. 1 minggu, Hijau maks. 2 minggu).</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">Grading Kuning / Merah</div>
              <div class="step-title">Root Cause Analysis (RCA)</div>
              <div class="step-desc">Investigasi komprehensif mencari akar masalah sistem oleh Tim KPRS (maksimal <strong>45 hari</strong>).</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item trap-box">
              <div class="tk-label">Bedah Soal UAB 22 No. 85 (Slide 69 & 75)</div>
              <div class="tk-text">Pasien jatuh dari tempat tidur saat ditransfer dari UGD ke Kamar Operasi. Tim RS melakukan investigasi mendalam agar kejadian serupa tidak terulang. Metode analisis akar masalah tersebut bernama <strong>Root Cause Analysis (RCA)</strong>.</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('b7', 'slides_bdt_kul3/slide_69.jpg', 'Slide 69 · Alur Pelaporan Insiden 2x24 Jam, Grading & RCA', this)">Slide 69</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b7', 'slides_bdt_kul3/slide_71.jpg', 'Slide 71 · Formulir Laporan Insiden Internal (Maks 2x24 Jam)', this)">Slide 71</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b7', 'slides_bdt_kul3/slide_73.jpg', 'Slide 73 · Grading Risiko: Biru, Hijau, Kuning, Merah', this)">Slide 73</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('b7', 'slides_bdt_kul3/slide_75.jpg', 'Slide 75 · Prinsip Analisis Akar Penyebab Masalah (RCA)', this)">Slide 75</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-b7').src, document.getElementById('proof-cap-b7').textContent)">
            <img id="proof-img-b7" src="slides_bdt_kul3/slide_69.jpg" alt="Bukti Slide 69" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-b7">Slide 69 · Pelaporan 2x24 Jam & RCA</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

    </div>

    <!-- =================================================================== -->
    <!-- PANEL 2: LATIHAN 9 SOAL ASLI UAB & REMIDI BDT + BUKTI SLIDE          -->
    <!-- =================================================================== -->
    <div id="panel-soal" class="view-panel">
      <div class="quiz-bar">
        <div class="quiz-score" id="quiz-score-label">Progres Tersimpan: 0/9 Dijawab · 0 Benar</div>
        <div class="filter-group">
          <button type="button" class="filter-btn active" onclick="filterQuiz('all', this)">Semua Soal (9)</button>
          <button type="button" class="filter-btn" onclick="filterQuiz('uab', this)">Soal Asli UAB BDT (7)</button>
          <button type="button" class="filter-btn" onclick="filterQuiz('remidi', this)">Soal Remidi BDT (2)</button>
          <button type="button" class="filter-btn" onclick="resetQuiz()">Reset Jawaban</button>
        </div>
      </div>

      <div id="quiz-container"></div>
    </div>

    <!-- =================================================================== -->
    <!-- PANEL 3: CEK CEPAT H-1 UJIAN (FLASHCARD 1 KLIK)                      -->
    <!-- =================================================================== -->
    <div id="panel-recall" class="view-panel">
      <div class="recall-grid">
        <div class="recall-card">
          <div>
            <span class="pill pill-red" style="margin-bottom:10px;">Slide 18 · Sering Keluar</span>
            <div class="recall-q">1. Apa beda KPC, KNC, KTC, KTD, dan Sentinel?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">
            • KPC: Kondisi berpotensi cedera, belum ada insiden.<br>
            • KNC: Salah tindakan, tapi BELUM kena pasien.<br>
            • KTC: SUDAH kena pasien, tapi TIDAK cedera.<br>
            • KTD: SUDAH kena pasien dan TIMBUL cedera.<br>
            • Sentinel: KTD berujung KEMATIAN / cacat permanen.
          </div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-red" style="margin-bottom:10px;">Slide 23–24 vs 61 · Jebakan Utama</span>
            <div class="recall-q">2. Bagaimana cara membedakan opsi soal "7 Standar" vs "7 Langkah" dalam 5 detik?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">
            • 7 Standar (Slide 23–24) diawali KATA BENDA: "Hak pasien", "Peran kepemimpinan...", "Pendidikan bagi pasien/staf", "Komunikasi merupakan kunci".<br>
            • 7 Langkah (Slide 61) diawali KATA KERJA AKTIF: "Membangun...", "Memimpin...", "Mengembangkan...".
          </div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-green" style="margin-bottom:10px;">Slide 34–35 · SKP 1</span>
            <div class="recall-q">3. Sebutkan arti 4 warna gelang pasien dan 4 identitas resmi!</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">
            • Gelang: Biru (Laki-laki), Pink (Perempuan), Merah (Alergi), Kuning (Risiko Jatuh).<br>
            • Minimal 2 dari 4 identitas: Nama lengkap, Tanggal lahir, No. RM, NIK (Dilarang pakai nomor kamar/bed!).
          </div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-amber" style="margin-bottom:10px;">Slide 46–48 · SKP 3</span>
            <div class="recall-q">4. Apa label resmi untuk botol Concentrated Potassium Chloride (KCl pekat)?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">
            • Label resmi: HIGH ALERT! MEDICATION (Slide 48).<br>
            • Wajib ditarik dari ruang rawat biasa dan hanya disimpan di Instalasi Farmasi / troli emergensi terkunci.
          </div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-blue" style="margin-bottom:10px;">Slide 51–54 · SKP 4</span>
            <div class="recall-q">5. Apa penyebab #1 kesalahan lokasi operasi (Wrong-Site Surgery) menurut Slide 54?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">
            • Urutan #1 di Slide 54: Komunikasi yang tidak efektif antara anggota tim bedah.<br>
            • Pencegahan: Surgical Marking (melibatkan pasien sadar) + Surgical Time-Out tepat sebelum insisi.
          </div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-red" style="margin-bottom:10px;">Slide 69–75 · Pelaporan & RCA</span>
            <div class="recall-q">6. Berapa batas waktu lapor insiden internal, dan kapan dipakai RCA vs Investigasi Sederhana?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">
            • Lapor internal maksimal 2 x 24 jam.<br>
            • Grading Biru/Hijau = Investigasi Sederhana (1–2 minggu).<br>
            • Grading Kuning/Merah = Root Cause Analysis / RCA (maksimal 45 hari).
          </div>
        </div>
      </div>
    </div>

  </main>

  <!-- Lightbox Modal -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <div class="lightbox-box" onclick="event.stopPropagation()">
      <div class="lightbox-top">
        <strong id="lb-title">Bukti Slide Asli Dosen</strong>
        <button type="button" class="search-btn" onclick="closeLightbox()">Tutup (ESC)</button>
      </div>
      <img id="lb-img" src="slides_bdt_kul3/slide_18.jpg" alt="Slide Full" />
    </div>
  </div>

  <!-- Cmd+K Modal -->
  <div id="cmdk-modal" class="cmdk-backdrop" onclick="closeCmdK()">
    <div class="cmdk-dialog" onclick="event.stopPropagation()">
      <div class="cmdk-top">
        <input type="text" id="cmdk-input" class="cmdk-input" placeholder="Ketik kata kunci soal UAB / slide (misal: Sentinel, KCl, Gelang, B12, Metformin)..." oninput="runCmdKSearch()" />
        <button type="button" class="search-btn" onclick="closeCmdK()">ESC</button>
      </div>
      <div id="cmdk-list" class="cmdk-list"></div>
    </div>
  </div>

  <script src="vendor/uab_search_data.js"></script>
  <script>
    window.MODULE_ID = 'bdt_kul3';
    window.QUESTIONS = [
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 29',
        slide: 'slides_bdt_kul3/slide_18.jpg',
        slideCap: 'Bukti Slide 18 · Definisi Kejadian Sentinel',
        stem: 'Seorang perempuan berusia 35 tahun datang ke klinik pratama dengan keluhan nyeri perut. Dokter memberikan suntikan Antalgin untuk mengatasi rasa sakitnya. Beberapa menit kemudian pasien mengalami syok anafilaktik dan meninggal dunia. Termasuk insiden keselamatan pasien manakah kejadian tersebut?',
        opts: ['Kejadian Potensial Cedera (KPC)', 'Kejadian Nyaris Cedera (KNC)', 'Kejadian Tidak Cedera (KTC)', 'Kejadian Tidak Diharapkan (KTD)', 'Kejadian Sentinel'],
        ans: 4,
        exp: '<strong>Kunci: E (Kejadian Sentinel).</strong> Sesuai Slide 18 baris terakhir, <em>Kejadian Sentinel adalah suatu KTD yang mengakibatkan kematian atau cedera yang serius</em>. Karena pasien meninggal dunia pasca-injeksi, insiden ini naik derajatnya dari KTD biasa menjadi Kejadian Sentinel.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · UAB 22 No. 70',
        slide: 'slides_bdt_kul3/slide_18.jpg',
        slideCap: 'Bukti Slide 18 · Sentinel vs KTD',
        stem: 'Pasien datang ke IGD karena nyeri kolik abdomen akut. Setelah diberikan injeksi analgetik, pasien mengalami henti jantung akibat reaksi anafilaksis berat dan dinyatakan meninggal. Kategori insiden keselamatan pasien pada kasus ini adalah...',
        opts: ['Kejadian Tidak Diharapkan (KTD)', 'Kejadian Sentinel', 'Kejadian Nyaris Cedera (KNC)', 'Kejadian Potensial Cedera (KPC)', 'Kejadian Tidak Cedera (KTC)'],
        ans: 1,
        exp: '<strong>Kunci: B (Kejadian Sentinel).</strong> Soal ini mengulang pola yang persis sama dengan Axonation No. 29. Setiap insiden medis yang berujung kematian mendadak yang tidak terkait perjalanan alamiah penyakit wajib diklasifikasikan sebagai Sentinel.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT-1 · Hal. 9–10',
        slide: 'slides_bdt_kul3/slide_18.jpg',
        slideCap: 'Bukti Slide 18 · Definisi KNC (Belum Terpapar ke Pasien)',
        stem: 'Dokter meresepkan obat dengan dosis yang salah akibat kelelahan. Petugas farmasi telah menyiapkan obat tersebut, namun perawat ruangan menyadari ketidaksesuaian dosis saat melakukan pengecekan ulang sehingga obat batal diberikan kepada pasien. Disebut apakah insiden ini?',
        opts: ['Kejadian Potensial Cedera (KPC)', 'Kejadian Nyaris Cedera (KNC)', 'Kejadian Tidak Cedera (KTC)', 'Kejadian Tidak Diharapkan (KTD)', 'Kejadian Sentinel'],
        ans: 1,
        exp: '<strong>Kunci: B (KNC / Near Miss).</strong> Sesuai Slide 18: <em>KNC adalah terjadinya insiden yang belum sampai terpapar ke pasien</em>. Jika obat tersebut sudah telanjur diminum pasien namun pasien tidak mengalami cedera, barulah disebut KTC.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 32',
        slide: 'slides_bdt_kul3/slide_24.jpg',
        slideCap: 'Bukti Slide 24 · Standar 5: Peran Kepemimpinan',
        stem: 'Manakah di bawah ini yang termasuk dalam 7 Standar Keselamatan Pasien Rumah Sakit?',
        opts: [
          'Membangun kesadaran akan nilai keselamatan pasien',
          'Memimpin dan mendukung staf dalam keselamatan pasien',
          'Peran kepemimpinan dalam meningkatkan keselamatan pasien',
          'Mengembangkan sistem pelaporan insiden keselamatan pasien',
          'Mengintegrasikan aktivitas pengelolaan risiko'
        ],
        ans: 2,
        exp: '<strong>Kunci: C (Peran kepemimpinan dalam meningkatkan keselamatan pasien).</strong> Sesuai Slide 24 baris pertama, poin ke-5 dari 7 Standar Keselamatan Pasien adalah <em>Peran kepemimpinan dalam meningkatkan keselamatan pasien</em>. Opsi A, B, D, dan E semuanya diambil dari <strong>Slide 61 (7 Langkah Menuju Keselamatan Pasien)</strong>.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 44',
        slide: 'slides_bdt_kul3/slide_23.jpg',
        slideCap: 'Bukti Slide 23 · Standar 1: Hak Pasien',
        stem: 'Standar keselamatan pasien rumah sakit merupakan acuan bagi fasyankes untuk melaksanakan pelayanannya. Yang termasuk dalam 7 Standar Keselamatan Pasien adalah...',
        opts: [
          'Hak pasien',
          'Ketepatan identifikasi pasien',
          'Peningkatan keamanan obat yang perlu diwaspadai',
          'Pengurangan risiko infeksi terkait pelayanan kesehatan',
          'Membangun kesadaran akan nilai keselamatan pasien'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Hak pasien).</strong> Sesuai Slide 23 poin pertama, <em>Hak Pasien</em> adalah Standar ke-1 dari 7 Standar Keselamatan Pasien. Opsi B, C, D adalah 6 SKP (Slide 32–33), sedangkan Opsi E adalah 7 Langkah (Slide 61).'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT-1 · Hal. 5 & 14',
        slide: 'slides_bdt_kul3/slide_35.jpg',
        slideCap: 'Bukti Slide 32 & 35 · SKP 1 Identifikasi & Gelang Biru',
        stem: 'Seorang pasien laki-laki berusia 58 tahun dirawat di bangsal paru dengan diagnosis pneumonia. Karena petugas admisi sibuk, pasien belum dipasangkan gelang identitas berwarna biru sehingga saat pemberian antibiotik injeksi, obat pasien tertukar dengan pasien di sebelah tempat tidurnya. Sasaran Keselamatan Pasien (SKP) manakah yang dilanggar?',
        opts: [
          'Ketepatan identifikasi pasien',
          'Peningkatan komunikasi yang efektif',
          'Peningkatan keamanan obat yang perlu diwaspadai',
          'Kepastian tepat-lokasi, tepat-prosedur, tepat-pasien operasi',
          'Pengurangan risiko infeksi terkait pelayanan kesehatan'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Ketepatan identifikasi pasien — SKP 1).</strong> Pemasangan gelang identitas (biru untuk laki-laki sesuai Slide 35) dan verifikasi minimal 2 identitas sebelum pemberian obat adalah inti dari SKP 1 (Slide 32 & 34).'
      }},
      {{
        cat: 'remidi',
        source: 'Soal Asli Remidi BDT · No. 39',
        slide: 'slides_bdt_kul3/slide_48.jpg',
        slideCap: 'Bukti Slide 48 · Botol HIGH ALERT! MEDICATION',
        stem: 'Cairan elektrolit pekat seperti Concentrated Potassium Chloride (KCl) dapat menyebabkan kejadian fatal bila diberikan tanpa pengenceran. Berdasarkan standar keselamatan pasien, label apakah yang wajib dipasang pada obat tersebut?',
        opts: ['Distinct', 'High Alert', 'Warning', 'Harmful', 'Caution'],
        ans: 1,
        exp: '<strong>Kunci: B (High Alert).</strong> Lihat langsung gambar botol di <strong>Slide 48</strong>: pada badan botol tertulis <em>HIGH ALERT! MEDICATION</em>. Dosen mengambil kata <em>Distinct</em>, <em>Warning</em>, dan <em>Harmful</em> dari kotak keterangan biru di sekeliling gambar botol pada Slide 48 sebagai pengecoh.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · Rekap Axonation No. 43',
        slide: 'slides_bdt_kul3/slide_54.jpg',
        slideCap: 'Bukti Slide 54 · Causes of Surgical Errors (#1)',
        stem: 'Seorang pasien dijadwalkan menjalani operasi di daerah thoraks, namun saat selesai operasi ternyata bagian tungkai kaki pasien juga ikut dioperasi akibat kesalahpahaman instruksi di meja operasi. Berdasarkan materi Patient Safety, apakah penyebab utama terjadinya kesalahan bedah tersebut?',
        opts: [
          'Komunikasi tidak efektif antar tim medis / bedah',
          'Kurangnya fasilitas kamar operasi',
          'Efek samping obat anestesi',
          'Keluarga pasien terlambat menandatangani informed consent',
          'Tidak tersedianya antibiotik profilaksis'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Komunikasi tidak efektif antar tim medis / bedah).</strong> Tertulis persis pada urutan nomor 1 di <strong>Slide 54 (Causes of Surgical Errors)</strong>: <em>1. Komunikasi yang tidak efektif antara anggota tim bedah</em>.'
      }},
      {{
        cat: 'uab',
        source: 'Soal Asli UAB BDT · UAB 22 No. 85 & Remidi Costa No. 36',
        slide: 'slides_bdt_kul3/slide_75.jpg',
        slideCap: 'Bukti Slide 69 & 75 · Root Cause Analysis (RCA)',
        stem: 'Seorang pasien terjatuh dari brankar saat proses transfer dari UGD menuju kamar operasi sehingga mengalami cedera kepala. Tim keselamatan pasien rumah sakit segera melakukan investigasi terstruktur untuk mencari akar penyebab sistemik agar kejadian serupa tidak terulang. Metode apakah yang digunakan tim tersebut?',
        opts: [
          'Root Cause Analysis (RCA)',
          'Failure Mode and Effects Analysis (FMEA)',
          'Audit Medis Internal',
          'Visum et Repertum',
          'Informed Consent'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Root Cause Analysis / RCA).</strong> Sesuai Slide 69 dan Slide 75, setiap insiden keselamatan pasien dengan derajat risiko Kuning/Merah dianalisis akar masalahnya menggunakan metode <strong>Root Cause Analysis (RCA)</strong>.'
      }}
    ];

    // Render Quiz Cards cleanly
    document.getElementById('quiz-container').innerHTML = window.QUESTIONS.map((q, idx) => `
      <article class="q-item" id="qcard-${{idx}}" data-cat="${{q.cat}}">
        <div class="q-meta">
          <span class="pill pill-red">${{q.source}}</span>
          <span class="topic-num">Soal #${{idx + 1}}</span>
        </div>
        <div class="q-stem">${{q.stem}}</div>
        <div class="opt-list">
          ${{q.opts.map((opt, oIdx) => `
            <button type="button" class="opt-btn" onclick="selectOption(${{idx}}, ${{oIdx}})">
              <span class="opt-letter">${{String.fromCharCode(65 + oIdx)}}.</span>
              <span>${{opt}}</span>
            </button>
          `).join('')}}
        </div>
        <div class="q-feedback" id="qfb-${{idx}}">
          <div class="fb-text">${{q.exp}}</div>
          <div>
            <img src="${{q.slide}}" alt="${{q.slideCap}}" class="fb-slide-img" onclick="zoomSlide('${{q.slide}}', '${{q.slideCap}}')" />
            <div style="font-size:0.78rem;color:#647786;margin-top:6px;">${{q.slideCap}} (Klik untuk perbesar)</div>
          </div>
        </div>
      </article>
    `).join('');

    {SHARED_JS}
  </script>
</body>
</html>
"""

# ==============================================================================
# MODULE 2: EMN KUL 2 DEFISIENSI VITAMIN (SUPER CLEAN & POWERFUL)
# ==============================================================================
EMN_HTML = f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>EMN Kuliah 2 · Defisiensi Vitamin — Belajar Tanpa Buka PPT</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@600;700&family=Newsreader:opsz,wght@6..72,600;6..72,700&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>{SHARED_CSS}</style>
</head>
<body>

  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand-group">
        <select class="lecture-Select" aria-label="Pilih Kuliah" onchange="window.location.href=this.value">
          <option value="BDT_KUL3_Patient_Safety.html">Blok 7 BDT · Kuliah 3: Patient Safety (dr. Riskiyah)</option>
          <option value="VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html" selected>Blok 9 EMN · Kuliah 2: Defisiensi Vitamin (dr. Iwal, Sp.PD)</option>
        </select>
      </div>

      <nav class="nav-tabs" aria-label="Mode Belajar">
        <button type="button" class="nav-tab active" onclick="switchTab('materi', this)">1. Materi Visual (Pengganti 28 Slide)</button>
        <button type="button" class="nav-tab" onclick="switchTab('soal', this)">2. Latihan Kasus Slide & Prediksi (6 Soal)</button>
        <button type="button" class="nav-tab" onclick="switchTab('recall', this)">3. Cek Cepat H-1 Ujian</button>
      </nav>

      <div class="top-actions">
        <button type="button" class="search-btn" onclick="openCmdK()">
          <span>Cari Bank Soal UAB</span>
          <kbd>⌘K</kbd>
        </button>
      </div>
    </div>
  </header>

  <main class="container">
    <section class="lecture-header">
      <div>
        <div class="eyebrow">Blok 9 · Endokrin, Metabolik & Nutrisi (EMN) · Kuliah Pakar 2</div>
        <h1>Defisiensi Vitamin (Larut Lemak & Air)</h1>
        <p class="header-sub">Seluruh isi <strong>28 slide dr. Iwal Reza Ahdi, Sp.PD</strong> telah dipadatkan menjadi <strong>6 Bab Visual Inti</strong>. <em>Catatan Jujur Sumber:</em> Karena arsip Bank Soal UAB belum memuat file Blok 9 (EMN), latihan soal di modul ini memadukan <strong>3 Kasus Diskusi Asli dari Slide Dosen</strong> dan <strong>3 Soal Prediksi Berbasis Slide</strong>.</p>
      </div>
      <div class="header-pills">
        <span class="pill pill-green">28 Slide → 6 Bab Visual</span>
        <span class="pill pill-amber">3 Kasus Asli Slide + 3 Prediksi</span>
        <span class="pill pill-blue">Waktu Kuasai: ±20 Menit</span>
      </div>
    </section>

    <!-- PANEL 1: MATERI VISUAL PADAT -->
    <div id="panel-materi" class="view-panel active">
      <div class="jump-bar">
        <a href="#emn-1" class="jump-chip">01 · 4 Jalur Etiologi & Obat</a>
        <a href="#emn-2" class="jump-chip">02 · Vitamin A (Mata & Epitel)</a>
        <a href="#emn-3" class="jump-chip">03 · Vitamin D, E, K</a>
        <a href="#emn-4" class="jump-chip">04 · Vitamin B1, B2, B3, B6</a>
        <a href="#emn-5" class="jump-chip">05 · Pembeda B9 (Folat) vs B12</a>
        <a href="#emn-6" class="jump-chip">06 · Pembeda Skorbut (Vit C) vs Vit K</a>
      </div>

      <!-- BAB 1 -->
      <article id="emn-1" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 01 · Merangkum Slide 1–7</span>
            <span class="pill pill-green">Fondasi Klinis & Interaksi Obat</span>
          </div>
          <h2>4 Jalur Penyebab Defisiensi & Interaksi Obat Khas</h2>
          <p class="digest-lead">Defisiensi vitamin di klinik jarang berdiri sendiri; selalu telusuri apakah masalahnya di <strong>asupan, absorpsi usus/empedu, peningkatan kebutuhan, atau efek samping obat jangka panjang</strong>.</p>

          <div class="flow-strip">
            <div class="flow-step">
              <div class="step-code">01 · Asupan</div>
              <div class="step-title">Diet & Alkohol</div>
              <div class="step-desc">Diet sangat restriktif, vegan murni tanpa fortifikasi (B12), kemiskinan, alkoholisme kronik (B1).</div>
            </div>
            <div class="flow-step">
              <div class="step-code">02 · Absorpsi</div>
              <div class="step-title">Ileum & Empedu</div>
              <div class="step-desc">Celiac, reseksi ileum terminal / Crohn (B12), operasi bariatrik, kolestasis hepatobilier (Vit A, D, E, K).</div>
            </div>
            <div class="flow-step">
              <div class="step-code">03 · Kebutuhan</div>
              <div class="step-title">Hamil & Tumbuh</div>
              <div class="step-desc">Kehamilan & laktasi (kebutuhan Folat/B9 melonjak), masa pertumbuhan anak, penyakit kritis.</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">04 · Obat Khas</div>
              <div class="step-title">3 Pasangan Obat</div>
              <div class="step-desc"><strong>Metformin → Def. B12</strong><br><strong>Isoniazid (INH) → Def. B6</strong><br><strong>Warfarin → Antagonis Vit K</strong></div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('e1', 'slides_kul2/slide_5.jpg', 'Slide 5 · Empat Jalur Menuju Defisiensi & Interaksi Obat', this)">Slide 5</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e1', 'slides_kul2/slide_6.jpg', 'Slide 6 · Algoritma 4 Langkah: Curiga → Uji → Tangani', this)">Slide 6</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e1', 'slides_kul2/slide_3.jpg', 'Slide 3 · Kasus Pembuka: Metformin & MCV 112 fL', this)">Slide 3</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-e1').src, document.getElementById('proof-cap-e1').textContent)">
            <img id="proof-img-e1" src="slides_kul2/slide_5.jpg" alt="Slide 5" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-e1">Slide 5 · Empat Jalur Defisiensi</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 2 -->
      <article id="emn-2" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 02 · Merangkum Slide 8 & 19</span>
            <span class="pill pill-blue">Vitamin Larut Lemak · Mata & Epitel</span>
          </div>
          <h2>Vitamin A: Siklus Visual (Retinal) & Epitel (Retinoat)</h2>
          <p class="digest-lead">Vitamin A bekerja melalui 2 bentuk aktif: <strong>Retinal</strong> (komponen rodopsin sel batang retina untuk adaptasi gelap) dan <strong>Asam Retinoat</strong> (diferensiasi epitel mukosa bersekresi mukus).</p>

          <div class="flow-strip">
            <div class="flow-step step-warn">
              <div class="step-code">Tahap 1 · Paling Dini</div>
              <div class="step-title">Nyctalopia</div>
              <div class="step-desc">Rabun senja akibat gagalnya regenerasi rodopsin di sel batang retina.</div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">Tahap 2 · Metaplasia</div>
              <div class="step-title">Xerophthalmia & Bitot</div>
              <div class="step-desc">Kekeringan konjungtiva disertai tumpukan keratin berbusa putih keperakan (<strong>Bercak Bitot</strong>).</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">Tahap 3 · Darurat</div>
              <div class="step-title">Keratomalasia</div>
              <div class="step-desc">Pelunakan & nekrosis pencairan kornea yang menyebabkan kebutaan permanen.</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('e2', 'slides_kul2/slide_8.jpg', 'Slide 8 · Vitamin A: Penglihatan, Epitel, & Foto Bercak Bitot', this)">Slide 8</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e2', 'slides_kul2/slide_19.jpg', 'Slide 19 · Tabel Ringkasan Vitamin Larut Lemak (A, D, E, K)', this)">Slide 19</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-e2').src, document.getElementById('proof-cap-e2').textContent)">
            <img id="proof-img-e2" src="slides_kul2/slide_8.jpg" alt="Slide 8" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-e2">Slide 8 · Vitamin A & Bercak Bitot</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 3 -->
      <article id="emn-3" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 03 · Merangkum Slide 9, 10, 19</span>
            <span class="pill pill-amber">Vitamin Larut Lemak · D, E, K</span>
          </div>
          <h2>Vitamin D (Tulang), E (Antioksidan), & K (Koagulasi)</h2>
          <p class="digest-lead">Pahami jalur aktivasi 3 organ pada Vitamin D serta perbedaan target klinis Vitamin E dan K:</p>

          <div class="flow-strip">
            <div class="flow-step step-focus">
              <div class="step-code">1 · Kulit & Hati</div>
              <div class="step-title">25(OH)D (Parameter Lab)</div>
              <div class="step-desc">UVB mengubah 7-dehidrokolesterol → D3 → dihidroksilasi di Hati menjadi <strong>25(OH)D</strong> (parameter baku status Vit D).</div>
            </div>
            <div class="flow-step">
              <div class="step-code">2 · Ginjal & Tulang</div>
              <div class="step-title">1,25-(OH)2-D (Aktif)</div>
              <div class="step-desc">Diaktifkan di Ginjal. Defisiensi pada anak = <strong>Rakitis</strong>; pada dewasa = <strong>Osteomalasia</strong> (nyeri tulang & lemah otot proksimal).</div>
            </div>
            <div class="flow-step step-warn">
              <div class="step-code">3 · Vit E & Vit K</div>
              <div class="step-title">Saraf vs Koagulasi</div>
              <div class="step-desc"><strong>Vit E</strong>: antioksidan membran → defisiensi: ataksia/neuropati.<br><strong>Vit K</strong>: karboksilasi Faktor II, VII, IX, X → defisiensi: <strong>PT/INR memanjang</strong>.</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('e3', 'slides_kul2/slide_9.jpg', 'Slide 9 · Jalur Aktivasi Vitamin D & Rakitis vs Osteomalasia', this)">Slide 9</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e3', 'slides_kul2/slide_10.jpg', 'Slide 10 · Vitamin E (Antioksidan) & Vitamin K (Koagulasi)', this)">Slide 10</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-e3').src, document.getElementById('proof-cap-e3').textContent)">
            <img id="proof-img-e3" src="slides_kul2/slide_9.jpg" alt="Slide 9" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-e3">Slide 9 · Aktivasi Vitamin D</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 4 -->
      <article id="emn-4" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 04 · Merangkum Slide 11, 12, 13, 25</span>
            <span class="pill pill-red">Keluar di Kasus Diskusi Slide 25</span>
          </div>
          <h2>Vitamin B Kompleks: B1 (Tiamin), B2, B3, & B6</h2>
          <p class="digest-lead">Vitamin B bekerja sebagai kofaktor enzim metabolisme energi dan neurotransmiter:</p>

          <div class="flow-strip">
            <div class="flow-step step-alert">
              <div class="step-code">Vit B1 · Tiamin (TPP)</div>
              <div class="step-title">Beriberi & Wernicke</div>
              <div class="step-desc">Kofaktor PDH, α-KGDH, Transketolase. Defisiensi: <strong>Beriberi kering</strong> (neuropati), <strong>Beriberi basah</strong> (gagal jantung edema), <strong>Ensefalopati Wernicke</strong>.</div>
            </div>
            <div class="flow-step">
              <div class="step-code">Vit B2 · Riboflavin</div>
              <div class="step-title">Lesi Mukokutan</div>
              <div class="step-desc">Kofaktor FMN/FAD. Defisiensi: <em>Angular cheilitis</em> (stomatitis sudut bibir), glositis magenta, dermatitis seboroik.</div>
            </div>
            <div class="flow-step step-warn">
              <div class="step-code">Vit B3 · Niasin</div>
              <div class="step-title">Pellagra (3D)</div>
              <div class="step-desc">Kofaktor NAD+/NADP+. Defisiensi menyebabkan <strong>Pellagra</strong>: <em>Dermatitis</em> fotosensitif (Casal necklace), <em>Diare</em>, <em>Demensia</em>.</div>
            </div>
            <div class="flow-step step-focus">
              <div class="step-code">Vit B6 · Piridoksin</div>
              <div class="step-title">Neuropati INH</div>
              <div class="step-desc">Kofaktor PLP (sintesis GABA & heme). Defisiensi akibat obat TB <strong>Isoniazid (INH)</strong> → neuropati perifer & kejang.</div>
            </div>
          </div>

          <div class="takeaway-list">
            <div class="takeaway-item trap-box">
              <div class="tk-label">Aturan Emas IGD (Slide 11 & 25)</div>
              <div class="tk-text">Pada pasien alkoholik kronik, malnutrisi berat, atau hiperemesis gravidarum, <strong>wajib berikan Tiamin (B1) SEBELUM atau bersama infus glukosa</strong> agar tidak memicu Ensefalopati Wernicke akut!</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('e4', 'slides_kul2/slide_11.jpg', 'Slide 11 · Vitamin B1 (Tiamin): Enzim TPP, Beriberi, & Wernicke', this)">Slide 11</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e4', 'slides_kul2/slide_13.jpg', 'Slide 13 · Vitamin B2 & B3 (Pellagra & Casal Necklace)', this)">Slide 13</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e4', 'slides_kul2/slide_25.jpg', 'Slide 25 · Diskusi Kasus 2: Kebingungan Akut & Ataksia (Wernicke)', this)">Slide 25</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-e4').src, document.getElementById('proof-cap-e4').textContent)">
            <img id="proof-img-e4" src="slides_kul2/slide_11.jpg" alt="Slide 11" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-e4">Slide 11 · Vitamin B1 (Tiamin)</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 5: TABEL B9 VS B12 -->
      <article id="emn-5" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 05 · Merangkum Slide 16, 17, 24</span>
            <span class="pill pill-red">Keluar di Kasus Pembuka Slide 3 & Kasus 1 Slide 24</span>
          </div>
          <h2>Pembeda Utama: Folat (B9) vs Kobalamin (B12)</h2>
          <p class="digest-lead">Keduanya sama-sama menimbulkan <strong>Anemia Megaloblastik (MCV > 100 fL)</strong> dan peningkatan homosistein, tetapi <strong>defisit neurologis dan peningkatan MMA hanya terjadi pada defisiensi B12</strong>.</p>

          <table>
            <thead>
              <tr>
                <th>Parameter Pembeda</th>
                <th>Defisiensi Vitamin B9 (Folat)</th>
                <th>Defisiensi Vitamin B12 (Kobalamin)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Gambaran Darah Tepi</strong></td>
                <td>Makrositik megaloblastik (MCV > 100 fL)</td>
                <td>Makrositik megaloblastik (MCV > 100 fL)</td>
              </tr>
              <tr>
                <td><strong>Gejala Neurologis</strong><br><small>(Parestesia, gangguan vibrasi, ataksia)</small></td>
                <td><strong>Tidak khas / Tidak ada</strong></td>
                <td><strong>Khas!</strong> (Bisa muncul walau Hb/MCV belum abnormal)</td>
              </tr>
              <tr>
                <td><strong>Kadar Homosistein</strong></td>
                <td>Meningkat</td>
                <td>Meningkat</td>
              </tr>
              <tr>
                <td><strong>Asam Metilmalonat (MMA)</strong></td>
                <td><strong>Normal</strong></td>
                <td><strong>Meningkat Spesifik!</strong></td>
              </tr>
              <tr>
                <td><strong>Faktor Risiko Utama</strong></td>
                <td>Kehamilan, asupan sayur kurang, alkohol</td>
                <td><strong>Metformin lama</strong>, vegan, gastritis autoimun, reseksi ileum</td>
              </tr>
            </tbody>
          </table>

          <div class="takeaway-list" style="margin-top:16px;">
            <div class="takeaway-item trap-box">
              <div class="tk-label">Jebakan Terapi di Slide 17</div>
              <div class="tk-text">Memberikan suplementasi <strong>Folat saja</strong> pada pasien defisiensi B12 dapat menyembuhkan anemianya secara semu, tetapi <strong>kerusakan mielin saraf jalan terus menjadi permanen</strong>!</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('e5', 'slides_kul2/slide_17.jpg', 'Slide 17 · Tabel Perbandingan B9 (Folat) vs B12 (Kobalamin)', this)">Slide 17</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e5', 'slides_kul2/slide_16.jpg', 'Slide 16 · Jalur Absorpsi B12 (Faktor Intrinsik & Ileum Terminal)', this)">Slide 16</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e5', 'slides_kul2/slide_24.jpg', 'Slide 24 · Diskusi Kasus 1: Metformin, Parestesia, MCV 112 fL', this)">Slide 24</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-e5').src, document.getElementById('proof-cap-e5').textContent)">
            <img id="proof-img-e5" src="slides_kul2/slide_17.jpg" alt="Slide 17" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-e5">Slide 17 · Folat vs B12</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>

      <!-- BAB 6: VIT C VS VIT K -->
      <article id="emn-6" class="topic-block">
        <div class="digest-pane">
          <div class="digest-top">
            <span class="topic-num">Bab 06 · Merangkum Slide 14, 15, 26</span>
            <span class="pill pill-red">Keluar di Kasus Diskusi Slide 26</span>
          </div>
          <h2>Pembeda Perdarahan: Skorbut (Vit C) vs Defisiensi Vit K</h2>
          <p class="digest-lead">Jika ada pasien datang dengan gusi berdarah dan mudah memar, lihat <strong>hasil laboratorium PT/INR</strong> dan <strong>tanda perifolikular</strong> untuk membedakan Vitamin C vs Vitamin K:</p>

          <div class="flow-strip">
            <div class="flow-step step-focus">
              <div class="step-code">Defisiensi Vitamin C (Skorbut)</div>
              <div class="step-title">Defek Kolagen · PT/INR Normal</div>
              <div class="step-desc">Gagal hidroksilasi prolin & lisin → dinding kapiler rapuh. Gejala khas: <strong>gusi bengkak berdarah, petechiae perifolikular, corkscrew hair, luka lama sembuh, namun PT/INR NORMAL</strong>.</div>
            </div>
            <div class="flow-step step-alert">
              <div class="step-code">Defisiensi Vitamin K</div>
              <div class="step-title">Defek Faktor II, VII, IX, X · PT/INR Naik</div>
              <div class="step-desc">Gagal karboksilasi residu glutamat faktor koagulasi di hati. Gejala: perdarahan mukosa/organ dalam disertai <strong>pemanjangan PT/INR dan aPTT</strong>.</div>
            </div>
          </div>
        </div>

        <aside class="proof-pane">
          <div class="proof-header">
            <span class="proof-label">Bukti Slide Asli</span>
            <div class="slide-switcher">
              <button type="button" class="slide-pill-btn active" onclick="swapSlide('e6', 'slides_kul2/slide_26.jpg', 'Slide 26 · Diskusi Kasus 3: Perdarahan Gingiva & PT/INR Normal (Skorbut)', this)">Slide 26</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e6', 'slides_kul2/slide_14.jpg', 'Slide 14 · Vitamin C: Sintesis Kolagen & Gambaran Skorbut', this)">Slide 14</button>
              <button type="button" class="slide-pill-btn" onclick="swapSlide('e6', 'slides_kul2/slide_21.jpg', 'Slide 21 · Pemilihan Pemeriksaan Lab Sesuai Pertanyaan Klinis', this)">Slide 21</button>
            </div>
          </div>
          <div class="proof-img-wrap" onclick="zoomSlide(document.getElementById('proof-img-e6').src, document.getElementById('proof-cap-e6').textContent)">
            <img id="proof-img-e6" src="slides_kul2/slide_26.jpg" alt="Slide 26" />
          </div>
          <div class="proof-caption">
            <span id="proof-cap-e6">Slide 26 · Skorbut vs Vitamin K</span>
            <span>Klik gambar untuk perbesar</span>
          </div>
        </aside>
      </article>
    </div>

    <!-- PANEL 2: SOAL LATIHAN -->
    <div id="panel-soal" class="view-panel">
      <div class="quiz-bar">
        <div class="quiz-score" id="quiz-score-label">Progres Tersimpan: 0/6 Dijawab · 0 Benar</div>
        <div class="filter-group">
          <button type="button" class="filter-btn active" onclick="filterQuiz('all', this)">Semua Soal (6)</button>
          <button type="button" class="filter-btn" onclick="filterQuiz('kasus', this)">Kasus Asli Slide Dosen (3)</button>
          <button type="button" class="filter-btn" onclick="filterQuiz('prediksi', this)">Prediksi Berbasis Slide (3)</button>
          <button type="button" class="filter-btn" onclick="resetQuiz()">Reset Jawaban</button>
        </div>
      </div>

      <div id="quiz-container"></div>
    </div>

    <!-- PANEL 3: CEK CEPAT H-1 -->
    <div id="panel-recall" class="view-panel">
      <div class="recall-grid">
        <div class="recall-card">
          <div>
            <span class="pill pill-red" style="margin-bottom:10px;">Slide 17 & 24</span>
            <div class="recall-q">1. Pasien DM konsumsi Metformin lama + kesemutan + MCV 112 fL. Defisiensi apa dan metabolit apa yang naik spesifik?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">Defisiensi Vitamin B12 (Kobalamin). Metabolit yang meningkat spesifik adalah Asam Metilmalonat (MMA) — sedangkan pada defisiensi Folat (B9), MMA normal.</div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-red" style="margin-bottom:10px;">Slide 11 & 25</span>
            <div class="recall-q">2. Apa trias Ensefalopati Wernicke dan enzim apa yang membutuhkan kofaktor Tiamin Pirofosfat (TPP)?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">Trias Wernicke: Kebingungan akut (ensefalopati), Ataksia, dan Gangguan gerak bola mata (nistagmus/oftalmoplegia). Enzim: Piruvat dehidrogenase, α-ketoglutarat dehidrogenase, Transketolase.</div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-green" style="margin-bottom:10px;">Slide 26</span>
            <div class="recall-q">3. Gusi berdarah + petechiae perifolikular + luka lama sembuh + PT/INR normal. Defisiensi vitamin apa?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">Defisiensi Vitamin C (Skorbut / Scurvy) akibat gangguan hidroksilasi kolagen dinding pembuluh darah kapiler.</div>
        </div>

        <div class="recall-card">
          <div>
            <span class="pill pill-blue" style="margin-bottom:10px;">Slide 9</span>
            <div class="recall-q">4. Apa perbedaan bentuk metabolit Vitamin D yang paling aktif secara biologis vs yang diukur di laboratorium?</div>
          </div>
          <button type="button" class="reveal-btn" onclick="this.parentElement.classList.toggle('revealed')">Buka Kunci Jawaban</button>
          <div class="recall-a">Paling aktif secara biologis: 1,25-(OH)2-D (Kalsitriol, produk ginjal). Yang diukur di lab untuk menilai status Vitamin D: 25(OH)D (Kalsidiol, produk hati).</div>
        </div>
      </div>
    </div>

  </main>

  <!-- Lightbox Modal -->
  <div id="lightbox" class="lightbox" onclick="closeLightbox()">
    <div class="lightbox-box" onclick="event.stopPropagation()">
      <div class="lightbox-top">
        <strong id="lb-title">Bukti Slide Asli Dosen</strong>
        <button type="button" class="search-btn" onclick="closeLightbox()">Tutup (ESC)</button>
      </div>
      <img id="lb-img" src="slides_bdt_kul3/slide_18.jpg" alt="Slide Full" />
    </div>
  </div>

  <!-- Cmd+K Modal -->
  <div id="cmdk-modal" class="cmdk-backdrop" onclick="closeCmdK()">
    <div class="cmdk-dialog" onclick="event.stopPropagation()">
      <div class="cmdk-top">
        <input type="text" id="cmdk-input" class="cmdk-input" placeholder="Ketik kata kunci soal UAB / slide (misal: B12, Metformin, Anemia, Vitamin, Kalsium)..." oninput="runCmdKSearch()" />
        <button type="button" class="search-btn" onclick="closeCmdK()">ESC</button>
      </div>
      <div id="cmdk-list" class="cmdk-list"></div>
    </div>
  </div>

  <script src="vendor/uab_search_data.js"></script>
  <script>
    window.MODULE_ID = 'emn_kul2';
    window.QUESTIONS = [
      {{
        cat: 'kasus',
        source: 'Kasus Asli Slide Dosen · Slide 3 & Slide 24',
        slide: 'slides_kul2/slide_24.jpg',
        slideCap: 'Bukti Slide 24 · Diskusi Kasus 1 (Metformin & Defisiensi B12)',
        stem: 'Seorang laki-laki berusia 62 tahun dengan riwayat DM tipe 2 dan konsumsi metformin jangka panjang datang dengan keluhan kesemutan pada kedua kaki selama 6 bulan, mudah lelah, dan lidah terasa nyeri (glossitis). Pemeriksaan fisik menunjukkan gangguan sensasi vibrasi. Laboratorium: Hb 9,8 g/dL dan MCV 112 fL. Defisiensi vitamin manakah yang paling mungkin beserta pemeriksaan metabolit konfirmasinya?',
        opts: [
          'Vitamin B9 (Folat) — kadar homosistein normal',
          'Vitamin B12 (Kobalamin) — peningkatan asam metilmalonat (MMA)',
          'Vitamin B1 (Tiamin) — penurunan aktivitas transketolase',
          'Vitamin B6 (Piridoksin) — peningkatan feritin serum',
          'Vitamin E (Tokoferol) — pemanjangan PT/INR'
        ],
        ans: 1,
        exp: '<strong>Kunci: B (Defisiensi Vitamin B12 — peningkatan MMA).</strong> Sesuai Slide 3, 17, dan 24, penggunaan metformin jangka panjang menghambat absorpsi B12 di ileum terminal, memicu anemia megaloblastik (MCV 112 fL) disertai neuropati sensorik/vibrasi. Peningkatan MMA membedakannya secara spesifik dari defisiensi folat.'
      }},
      {{
        cat: 'kasus',
        source: 'Kasus Asli Slide Dosen · Slide 25',
        slide: 'slides_kul2/slide_25.jpg',
        slideCap: 'Bukti Slide 25 · Diskusi Kasus 2 (Ensefalopati Wernicke)',
        stem: 'Seorang pasien dengan riwayat malnutrisi berat dan muntah berkepanjangan dibawa ke IGD dalam kondisi kebingungan akut (konfusi), langkah jalan sempoyongan (ataksia), serta gangguan gerak bola mata (nistagmus/oftalmoplegia) setelah sebelumnya mendapat cairan infus dekstrosa. Defisiensi vitamin apakah yang mendasari kegawatan neurologis ini?',
        opts: [
          'Vitamin B1 (Tiamin)',
          'Vitamin B2 (Riboflavin)',
          'Vitamin B3 (Niasin)',
          'Vitamin B12 (Kobalamin)',
          'Vitamin C (Asam Askorbat)'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Vitamin B1 / Tiamin).</strong> Sesuai Slide 11 dan Slide 25, trias konfusi akut, ataksia, dan oftalmoplegia/nistagmus adalah tanda klasik <strong>Ensefalopati Wernicke</strong> akibat defisiensi Tiamin Pirofosfat (TPP).'
      }},
      {{
        cat: 'kasus',
        source: 'Kasus Asli Slide Dosen · Slide 26',
        slide: 'slides_kul2/slide_26.jpg',
        slideCap: 'Bukti Slide 26 · Diskusi Kasus 3 (Skorbut / Defisiensi Vit C)',
        stem: 'Seorang pria berusia 41 tahun dengan diet sangat terbatas datang dengan keluhan gusi sering berdarah, mudah memar, bintik perdarahan perifolikular di kedua tungkai, dan luka yang lama sembuh. Hasil pemeriksaan darah menunjukkan jumlah trombosit normal serta nilai PT dan INR normal. Diagnosis yang paling tepat adalah...',
        opts: [
          'Defisiensi Vitamin K',
          'Defisiensi Vitamin C (Skorbut)',
          'Defisiensi Vitamin D (Osteomalasia)',
          'Defisiensi Vitamin B3 (Pellagra)',
          'Defisiensi Vitamin A (Xerophthalmia)'
        ],
        ans: 1,
        exp: '<strong>Kunci: B (Defisiensi Vitamin C / Skorbut).</strong> Sesuai Slide 26, perdarahan gusi + petechiae perifolikular + luka lama sembuh dengan <strong>PT/INR yang normal</strong> membuktikan bahwa kelainannya terletak pada kerapuhan kolagen dinding kapiler (Vitamin C), bukan faktor koagulasi (Vitamin K).'
      }},
      {{
        cat: 'prediksi',
        source: 'Prediksi Berbasis Slide · Slide 8',
        slide: 'slides_kul2/slide_8.jpg',
        slideCap: 'Bukti Slide 8 · Peran Retinal vs Retinoat & Bercak Bitot',
        stem: 'Seorang anak berusia 4 tahun dibawa ibunya karena sering menabrak benda saat senja hari. Pada pemeriksaan konjungtiva tampak bercak putih keperakan berbusa di sisi temporal (Bercak Bitot). Bentuk aktif vitamin manakah yang berperan menjaga diferensiasi epitel konjungtiva agar tidak mengalami metaplasia keratin tersebut?',
        opts: [
          'Asam retinoat',
          '11-cis-retinal',
          'Kalsitriol',
          'Alfa-tokoferol',
          'Menakuinon'
        ],
        ans: 0,
        exp: '<strong>Kunci: A (Asam retinoat).</strong> Sesuai Slide 8: <em>Retinal → siklus visual (rodopsin)</em>, sedangkan <em>Retinoat → diferensiasi epitel</em>. Hilangnya asam retinoat menyebabkan epitel konjungtiva mengalami metaplasia skuamosa berkeratin (Bercak Bitot).'
      }},
      {{
        cat: 'prediksi',
        source: 'Prediksi Berbasis Slide · Slide 9',
        slide: 'slides_kul2/slide_9.jpg',
        slideCap: 'Bukti Slide 9 · Parameter Status Vitamin D: 25(OH)D',
        stem: 'Seorang perempuan berusia 50 tahun mengeluhkan nyeri tulang difus dan kelemahan otot proksimal. Dokter mencurigai adanya osteomalasia akibat defisiensi Vitamin D. Pemeriksaan laboratorium manakah yang paling tepat dipilih untuk mencerminkan status cadangan Vitamin D tubuh pasien?',
        opts: [
          '1,25-dihidroksivitamin D [1,25(OH)2D]',
          '25-hidroksivitamin D [25(OH)D]',
          '7-dehidrokolesterol',
          'Kalsitonin serum',
          'Alkaline phosphatase urin'
        ],
        ans: 1,
        exp: '<strong>Kunci: B (25-hidroksivitamin D / 25(OH)D).</strong> Sesuai catatan kaki di Slide 9: <em>25(OH)D mencerminkan status vitamin D</em> karena waktu paruhnya panjang di sirkulasi.'
      }},
      {{
        cat: 'prediksi',
        source: 'Prediksi Berbasis Slide · Slide 13',
        slide: 'slides_kul2/slide_13.jpg',
        slideCap: 'Bukti Slide 13 · Defisiensi B3 (Niasin) → Pellagra',
        stem: 'Seorang petani yang hanya mengonsumsi jagung tanpa variasi protein hewani datang dengan keluhan ruam kulit hiperpigmentasi simetris di area leher yang terpapar matahari (Casal necklace), disertai diare kronik dan penurunan daya ingat. Defisiensi kofaktor vitamin apakah yang dialami pasien?',
        opts: [
          'Vitamin B1 (Tiamin)',
          'Vitamin B2 (Riboflavin)',
          'Vitamin B3 (Niasin / NAD+ & NADP+)',
          'Vitamin B6 (Piridoksin)',
          'Vitamin B7 (Biotin)'
        ],
        ans: 2,
        exp: '<strong>Kunci: C (Vitamin B3 / Niasin).</strong> Sesuai Slide 13, trias Dermatitis fotosensitif (Casal necklace), Diare, dan Demensia adalah sindrom klasik <strong>Pellagra</strong> akibat defisiensi Vitamin B3 (prekursor NAD+ dan NADP+).'
      }}
    ];

    document.getElementById('quiz-container').innerHTML = window.QUESTIONS.map((q, idx) => `
      <article class="q-item" id="qcard-${{idx}}" data-cat="${{q.cat}}">
        <div class="q-meta">
          <span class="pill pill-amber">${{q.source}}</span>
          <span class="topic-num">Soal #${{idx + 1}}</span>
        </div>
        <div class="q-stem">${{q.stem}}</div>
        <div class="opt-list">
          ${{q.opts.map((opt, oIdx) => `
            <button type="button" class="opt-btn" onclick="selectOption(${{idx}}, ${{oIdx}})">
              <span class="opt-letter">${{String.fromCharCode(65 + oIdx)}}.</span>
              <span>${{opt}}</span>
            </button>
          `).join('')}}
        </div>
        <div class="q-feedback" id="qfb-${{idx}}">
          <div class="fb-text">${{q.exp}}</div>
          <div>
            <img src="${{q.slide}}" alt="${{q.slideCap}}" class="fb-slide-img" onclick="zoomSlide('${{q.slide}}', '${{q.slideCap}}')" />
            <div style="font-size:0.78rem;color:#647786;margin-top:6px;">${{q.slideCap}} (Klik untuk perbesar)</div>
          </div>
        </div>
      </article>
    `).join('');

    {SHARED_JS}
  </script>
</body>
</html>
"""

with open(os.path.join(BASE_DIR, "BDT_KUL3_Patient_Safety.html"), "w", encoding="utf-8") as f:
    f.write(BDT_HTML)

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(BDT_HTML)

with open(os.path.join(BASE_DIR, "VERTEX-PREP_PoC_KUL2_Defisiensi_Vitamin.html"), "w", encoding="utf-8") as f:
    f.write(EMN_HTML)

print("Successfully rebuilt super clean & powerful BDT KUL 3 and EMN KUL 2 modules!")
