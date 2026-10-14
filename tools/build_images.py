"""Gera imagens responsivas (WebP) em /img a partir dos originais em /originais.
Uso: python tools/build_images.py   (requer Pillow)"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "img"
SRC = ROOT / "originais"
OUT.mkdir(exist_ok=True)

# slug -> (arquivo original, larguras)
SOURCES = {
    "altino-hero":   ("4019dd256a09b0eac21f49001dbf62e0-_1_.webp", [480, 720, 1080, 1800]),
    "altino-pb":     ("ab20c61efc6ce239af2052a217c77127.webp", [480, 800, 1066]),
    "boa-viagem":    ("c80d8f0789df6b79dad8616c29ae74f6.webp", [480, 582]),
    "brooklin":      ("b2c71b0c31feed9197ee96cd8c354d24.webp", [800, 1200, 1600]),
    "ipiranga":      ("8d72c4de13366ed66fe86a5ac5639513.webp", [480, 800, 1080]),
    "altino-cor":    ("f70991859044123fc9fde109ec2f2e8f.webp", [480, 800, 1066]),
    "paulista":      ("cd4b01c8733e15d52851396e350aee62.webp", [800, 1200, 1600]),
    "luann":         ("ad170591b57d607cdf65079af2f06806 (1).webp", [400, 600]),
    "bg-viaduto":    ("ViadutoReinaldodeOliveira2024.webp", [640, 905]),
    "bg-towers":     ("SaoPauloCorporateTowers2026.webp", [800, 1400]),
    "theatro":       ("0b0245a833f30eb5ffe0e8dddf709d10.webp", [640, 1000, 1400]),
}

for slug, (src, widths) in SOURCES.items():
    im = Image.open(SRC / src).convert("RGB")
    for w in widths:
        h = round(im.height * w / im.width)
        im.resize((w, h), Image.LANCZOS).save(OUT / f"{slug}-{w}.webp", "WEBP", quality=(58 if slug in ("altino-pb", "bg-viaduto", "bg-towers") else 76), method=6)
        print(f"{slug}-{w}.webp {w}x{h}")

# OG image 1200x630 (recorte do hero) e ícones
hero = Image.open(SRC / SOURCES["altino-hero"][0]).convert("RGB")
bg = hero.getpixel((5, 5))
og = Image.new("RGB", (1200, 630), bg)
t = hero.resize((round(hero.width * 630 / hero.height), 630), Image.LANCZOS)
og.paste(t, ((1200 - t.width) // 2, 0))
og.save(OUT / "og.jpg", "JPEG", quality=82, optimize=True, progressive=True)
sq = hero.crop((200, 250, 1600, 1650)).resize((180, 180), Image.LANCZOS)
sq.save(OUT / "apple-touch-icon.png", optimize=True)
sq.resize((192, 192)).save(OUT / "icon-192.png", optimize=True)
sq.resize((512, 512), Image.LANCZOS).save(OUT / "icon-512.png", optimize=True)
print("edge colors", hero.getpixel((5, 5)), hero.getpixel((1795, 5)), hero.getpixel((5, 1200)), hero.getpixel((1795, 1200)), hero.getpixel((900, 2395)), hero.getpixel((5, 2395)))
