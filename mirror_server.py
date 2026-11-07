#!/usr/bin/env python3
"""Server lokal VERTEX-PREP + mirror Drive VERTEXTERIAL dengan sinkronisasi otomatis.

  python3 mirror_server.py [--port 8765] [--interval 600]

Endpoint:
  GET  /api/tree   pohon Drive (JSON)
  GET  /api/meta   {version, crawledAt, checkedAt, syncing, error, stats}
  POST /api/sync   paksa sinkronisasi sekarang (blocking), balas meta
Selain itu menyajikan file statis dari folder ini.
"""
import argparse
import hashlib
import json
import os
import threading
import time
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

import crawl_drive

HERE = os.path.dirname(os.path.abspath(__file__))


class State:
    def __init__(self):
        self.lock = threading.Lock()
        self.sync_lock = threading.Lock()
        self.tree_bytes = b"{}"
        self.version = ""
        self.crawled_at = ""
        self.checked_at = ""
        self.stats = {"folders": 0, "files": 0}
        self.error = ""
        self.syncing = False
        self._sig = ""

    def load(self, tree):
        data = json.dumps(tree, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        sig = crawl_drive.tree_signature(tree)
        with self.lock:
            changed = sig != self._sig
            self._sig = sig
            self.tree_bytes = data
            self.crawled_at = tree.get("crawledAt", "")
            self.stats = tree.get("stats") or count(tree)
            if changed:
                self.version = hashlib.sha1(sig.encode("utf-8")).hexdigest()[:12]
        return changed

    def meta(self):
        with self.lock:
            return {"version": self.version, "crawledAt": self.crawled_at,
                    "checkedAt": self.checked_at, "syncing": self.syncing,
                    "error": self.error, "stats": self.stats}

    def refresh(self):
        """Crawl Drive asli; ganti data hanya bila berubah. Gagal -> data lama dipertahankan."""
        if not self.sync_lock.acquire(blocking=False):
            return False
        try:
            with self.lock:
                self.syncing = True
            try:
                tree = crawl_drive.crawl_all()
            except Exception as e:  # noqa: BLE001
                with self.lock:
                    self.error = str(e)
                return False
            changed = self.load(tree)
            if changed:
                crawl_drive.write_tree(tree)
                # Auto-fabricate newly uploaded lectures automatically without human command
                try:
                    import mass_module_factory
                    threading.Thread(target=mass_module_factory.process_all_missing, daemon=True).start()
                except Exception as ex:
                    print(f"[Auto-Factory Error] {ex}", flush=True)
            with self.lock:
                self.error = ""
                self.checked_at = time.strftime("%Y-%m-%d %H:%M:%S")
            return changed
        finally:
            with self.lock:
                self.syncing = False
            self.sync_lock.release()


def count(tree):
    s = {"folders": 0, "files": 0}

    def walk(n):
        if n.get("isFolder"):
            s["folders"] += 1
            for c in n.get("children", []):
                walk(c)
        else:
            s["files"] += 1
    walk(tree)
    return s


STATE = State()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def _json(self, body, code=200):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/tree":
            with STATE.lock:
                data = STATE.tree_bytes
            return self._json(data)
        if path == "/api/meta":
            return self._json(STATE.meta())
        return super().do_GET()

    def do_POST(self):
        if self.path.split("?", 1)[0] == "/api/sync":
            STATE.refresh()
            return self._json(STATE.meta())
        self.send_error(404)

    def end_headers(self):
        if not self.path.startswith("/api/"):
            self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        if not self.path.startswith("/api/meta"):
            super().log_message(fmt, *args)


def loop(interval):
    while True:
        time.sleep(interval)
        STATE.refresh()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--interval", type=int, default=600, help="detik antar sinkronisasi otomatis")
    args = ap.parse_args()

    cache = os.path.join(HERE, "drive_tree.json")
    if os.path.exists(cache):
        with open(cache, encoding="utf-8") as f:
            STATE.load(json.load(f))
        STATE.checked_at = STATE.crawled_at
    else:
        print("crawl awal dari Drive asli ...", flush=True)
        t = crawl_drive.crawl_all()
        crawl_drive.write_tree(t)
        STATE.load(t)
        STATE.checked_at = STATE.crawled_at
    threading.Thread(target=STATE.refresh, daemon=True).start()  # cek perubahan segera setelah start
    threading.Thread(target=lambda: (time.sleep(2), __import__("mass_module_factory").process_all_missing()), daemon=True).start()
    threading.Thread(target=loop, args=(args.interval,), daemon=True).start()
    srv = ThreadingHTTPServer(("0.0.0.0", args.port), Handler)
    print(f"Serving http://127.0.0.1:{args.port}/  (sync tiap {args.interval}s)", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
