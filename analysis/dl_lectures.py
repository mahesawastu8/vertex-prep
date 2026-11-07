#!/usr/bin/env python3
"""Unduh semua file (PDF) dalam satu folder Drive dari drive_tree.json ke analysis/lectures/<blok>/."""
import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
TREE = os.path.join(HERE, "..", "drive_tree.json")


def find(node, name):
    if node["isFolder"]:
        if node["name"] == name:
            return node
        for c in node["children"]:
            r = find(c, name)
            if r:
                return r


def safe(s):
    return re.sub(r"[^\w\-. ()]+", "_", s).strip()


def download(item, dest_dir):
    name = item["name"] if item["name"].lower().endswith(".pdf") else item["name"] + ".pdf"
    path = os.path.join(dest_dir, safe(name))
    if os.path.exists(path) and os.path.getsize(path) > 1000:
        return path, "cache"
    url = f"https://drive.google.com/uc?export=download&confirm=t&id={item['id']}"
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=120) as r:
                data = r.read()
            if not data.startswith(b"%PDF"):
                raise RuntimeError("bukan PDF (mungkin halaman konfirmasi)")
            with open(path + ".tmp", "wb") as f:
                f.write(data)
            os.replace(path + ".tmp", path)
            return path, "ok"
        except Exception as e:  # noqa: BLE001
            err = e
    return path, f"GAGAL: {err}"


if __name__ == "__main__":
    folder_name = sys.argv[1]
    tree = json.load(open(TREE, encoding="utf-8"))
    folder = find(tree, folder_name)
    if not folder:
        sys.exit(f"folder '{folder_name}' tidak ditemukan")
    dest = os.path.join(HERE, "lectures", safe(folder_name))
    os.makedirs(dest, exist_ok=True)
    files = [c for c in folder["children"] if not c["isFolder"] and (c["mime"] == "application/pdf" or c["name"].lower().endswith(".pdf"))]
    print(f"{folder_name}: {len(files)} PDF -> {dest}", flush=True)
    with ThreadPoolExecutor(max_workers=6) as ex:
        for (p, st), it in zip(ex.map(lambda i: download(i, dest), files), files):
            print(f"{st:>6}  {os.path.getsize(p) // 1024 if os.path.exists(p) else 0:>6} KB  {it['name']}", flush=True)
