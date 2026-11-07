#!/usr/bin/env python3
"""Crawl folder Google Drive publik VERTEXTERIAL secara rekursif -> drive_tree.json (1:1 dengan Drive asli).

Dipakai langsung (python3 crawl_drive.py) atau oleh mirror_server.py untuk sinkronisasi otomatis.
Penulisan atomik; hasil crawl kosong/gagal TIDAK menimpa data lama.
"""
import html
import json
import os
import re
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

ROOT_ID = "1vrUGhIJuAjfV8R9zKDe8Wr-ojAtnLeJt"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "drive_tree.json")
UA = {"User-Agent": "Mozilla/5.0"}

ENTRY_RE = re.compile(r'<div class="flip-entry" id="entry-([^"]+)".*?(?=<div class="flip-entry" id="entry-|</body>)', re.S)
HREF_RE = re.compile(r'<a href="([^"]+)"')
TITLE_RE = re.compile(r'<div class="flip-entry-title">(.*?)</div>', re.S)
THUMB_RE = re.compile(r'<img src="(https://lh3\.googleusercontent\.com/[^"]+)" alt="([^"]*)"')
MIME_RE = re.compile(r'googleusercontent\.com/\d+/type/([^"]+)"')
MOD_RE = re.compile(r'<div class="flip-entry-last-modified"><div>(.*?)</div>', re.S)


def fetch(folder_id):
    url = f"https://drive.google.com/embeddedfolderview?id={folder_id}"
    err = None
    for attempt in range(5):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001 - retry any network error
            err = e
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"gagal fetch {folder_id}: {err}")


def parse(page):
    out = []
    for m in ENTRY_RE.finditer(page):
        block = m.group(0)
        href = HREF_RE.search(block)
        title = TITLE_RE.search(block)
        if not href or not title:
            continue
        href = html.unescape(href.group(1))
        thumb = THUMB_RE.search(block)
        mime = MIME_RE.search(block)
        mod = MOD_RE.search(block)
        eid = m.group(1)
        is_f = "/drive/folders/" in href
        out.append({
            "id": eid,
            "name": html.unescape(re.sub(r"<[^>]+>", "", title.group(1))).strip(),
            "isFolder": is_f,
            "url": href,
            "mime": html.unescape(mime.group(1)) if mime else "",
            "thumb": "" if is_f else f"https://drive.google.com/thumbnail?id={eid}&sz=w800",
            "modified": html.unescape(re.sub(r"<[^>]+>", "", mod.group(1))).strip() if mod else "",
        })
    return out


def _crawl(folder_id, name, stats, log, depth=0):
    entries = parse(fetch(folder_id))
    stats["folders"] += 1
    subs = [e for e in entries if e["isFolder"]]
    files = [e for e in entries if not e["isFolder"]]
    stats["files"] += len(files)
    node = {"id": folder_id, "name": name, "isFolder": True,
            "url": f"https://drive.google.com/drive/folders/{folder_id}", "children": list(files)}
    if subs:
        with ThreadPoolExecutor(max_workers=4) as ex:
            kids = list(ex.map(lambda s: _crawl(s["id"], s["name"], stats, log, depth + 1), subs))
        for s, kid in zip(subs, kids):
            kid["modified"] = s["modified"]
            node["children"].append(kid)
    node["children"].sort(key=lambda c: (not c["isFolder"], c["name"].lower()))
    if log:
        print(f"{'  ' * depth}{name}: {len(subs)} folder, {len(files)} file", file=sys.stderr)
    return node


def crawl_all(log=False):
    stats = {"folders": 0, "files": 0}
    tree = _crawl(ROOT_ID, "VERTEXTERIAL", stats, log)
    if stats["files"] == 0:
        raise RuntimeError("crawl menghasilkan 0 file; data lama dipertahankan")
    tree["crawledAt"] = time.strftime("%Y-%m-%d %H:%M:%S")
    tree["stats"] = stats
    return tree


def write_tree(tree, out=OUT):
    tmp = out + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(tree, f, ensure_ascii=False, separators=(",", ":"))
    os.replace(tmp, out)


def tree_signature(tree):
    """Tanda tangan isi (tanpa waktu crawl) untuk mendeteksi perubahan di Drive asli."""
    def strip(n):
        d = {k: n[k] for k in ("id", "name", "isFolder", "mime", "modified") if k in n}
        if n.get("isFolder"):
            d["c"] = [strip(c) for c in n["children"]]
        return d
    return json.dumps(strip(tree), sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    t = crawl_all(log=True)
    write_tree(t)
    print(f"SELESAI: {t['stats']['folders']} folder, {t['stats']['files']} file -> {OUT}")
