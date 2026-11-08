#!/usr/bin/env python3
"""
METRICBUY — Automated Telegram Affiliate Broadcast Bot
Directly broadcasts data-driven Shopee Affiliate deals to Telegram Channels/Groups.
Affiliate Tracking ID: 11316671792
"""

import os
import sys
import json
import urllib.request
import urllib.parse
import argparse

AFFILIATE_ID = "11316671792"
PORTAL_URL = "https://mahesawastu8.github.io/vertex-prep/rekomendasi.html"

# Verified Top E-Commerce Deals in Indonesia
DEALS = [
    {
        "title": "The Originote Hyalucera Gel 50ml (Top #1 Skincare ID)",
        "price": "Rp 42.000",
        "reviews": "810.254 Ulasan Terverifikasi (Rating 4.89/5.0)",
        "features": [
            "Ceramide NP/AP/EOP + 2% Hyaluron",
            "Meresap 15 detik, non-greasy di cuaca tropis",
            "Listing paling banyak dibeli se-Indonesia"
        ],
        "shopee_query": "The Originote Hyalucera Moisturizer Gel 50ml Original"
    },
    {
        "title": "Azarine Hydrasoothe Sunscreen Gel SPF45 (50ml)",
        "price": "Rp 58.000",
        "reviews": "520.400 Ulasan Terverifikasi (Rating 4.91/5.0)",
        "features": [
            "0% Alkohol, 0% Silikon, 0% Whitecast",
            "In-Vitro Lab SPF 45.8 teruji",
            "Ringan seperti air, tidak menyumbat pori"
        ],
        "shopee_query": "Azarine Hydrasoothe Sunscreen Gel SPF45 Original Official"
    },
    {
        "title": "BOLT Cat Dry Food 1kg (Tuna / Salmon)",
        "price": "Rp 21.000",
        "reviews": "182.213 Ulasan Terverifikasi (Rating 4.93/5.0)",
        "features": [
            "Kandungan protein min. 28.0%",
            "Diperkaya Taurin untuk retina & jantung",
            "Barang habis pakai dengan repeat order bulanan tertinggi"
        ],
        "shopee_query": "BOLT Makanan Kucing 1kg Dry Food Original"
    },
    {
        "title": "AMINO 4A Fast Charging Cable (Type-C / Lightning)",
        "price": "Rp 17.900",
        "reviews": "135.597 Ulasan Terverifikasi (Rating 4.87/5.0)",
        "features": [
            "Arus stabil 4.0A (Mendukung QC 20W/30W)",
            "Kabel tembaga tebal tinned copper",
            "Lolos uji tekuk laboratorium >10.000 siklus"
        ],
        "shopee_query": "AMINO Kabel Data Fast Charging 4A Original"
    },
    {
        "title": "Baseus Bowie WM02 TWS Bluetooth 5.3",
        "price": "Rp 139.000",
        "reviews": "110.450 Ulasan Terverifikasi (Rating 4.86/5.0)",
        "features": [
            "Chip Bluetooth 5.3 low-latency 0.06 detik",
            "Baterai total 25 Jam pemakaian",
            "Bobot ultra ringan 3.8 gram per earbud"
        ],
        "shopee_query": "Baseus Bowie WM02 TWS Earphone Bluetooth 5.3 Original"
    }
]

def make_affiliate_url(query):
    encoded = urllib.parse.quote(query)
    return f"https://shopee.co.id/search?keyword={encoded}&aff_id={AFFILIATE_ID}&utm_source=telegram_bot&utm_medium=affiliate&utm_campaign=auto_broadcast"

def format_telegram_message(deal):
    url = make_affiliate_url(deal["shopee_query"])
    features_txt = "\n".join([f"• {f}" for f in deal["features"]])
    
    msg = (
        f"📊 <b>DATA LAPANGAN E-COMMERCE INDONESIA</b>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🔥 <b>{deal['title']}</b>\n"
        f"💰 <b>Harga Resmi:</b> <code>{deal['price']}</code>\n"
        f"★ <b>Bukti Sosial:</b> <i>{deal['reviews']}</i>\n\n"
        f"<b>Parameter Spesifikasi:</b>\n"
        f"{features_txt}\n\n"
        f"👉 <a href=\"{url}\"><b>CEK TOKO OFFICIAL &amp; DISKON DI SHOPEE</b></a>\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🌐 <i>Indeks Lengkap: <a href=\"{PORTAL_URL}\">METRICBUY Hub</a></i>"
    )
    return msg

def send_telegram(token, chat_id, message):
    api_url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(api_url, data=data, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode("utf-8"))
            return res.get("ok", False)
    except Exception as e:
        print(f"Error sending to Telegram: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(description="METRICBUY Telegram Auto-Broadcast Bot")
    parser.add_argument("--token", default=os.environ.get("TELEGRAM_BOT_TOKEN"), help="Telegram Bot Token")
    parser.add_argument("--chat-id", default=os.environ.get("TELEGRAM_CHAT_ID"), help="Telegram Channel/Group Chat ID (e.g. @mychannel)")
    parser.add_argument("--index", type=int, default=0, help="Deal index to post (0 to 4)")
    parser.add_argument("--dry-run", action="store_true", help="Print message preview without sending")
    args = parser.parse_args()

    deal = DEALS[args.index % len(DEALS)]
    msg = format_telegram_message(deal)

    if args.dry_run or not args.token or not args.chat_id:
        print("=== TELEGRAM MESSAGE PREVIEW (DRY-RUN) ===")
        print(msg.replace("<b>", "").replace("</b>", "").replace("<code>", "").replace("</code>", "").replace("<i>", "").replace("</i>", "").replace("&amp;", "&"))
        print("==========================================")
        if not args.token or not args.chat_id:
            print("\n[INFO] Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID or pass --token and --chat-id to broadcast live.")
        return 0

    print(f"Broadcasting deal '{deal['title']}' to {args.chat_id}...")
    success = send_telegram(args.token, args.chat_id, msg)
    if success:
        print("✓ Successfully sent message to Telegram!")
        return 0
    else:
        print("✗ Failed to send message.", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
