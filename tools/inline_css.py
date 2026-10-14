"""Opcional p/ deploy: gera dist/index.html com o CSS inline (zero CSS bloqueante)."""
import re, shutil
from pathlib import Path
R = Path(__file__).resolve().parent.parent; D = R / "dist"
D.mkdir(exist_ok=True)
for c in D.iterdir():
    shutil.rmtree(c) if c.is_dir() else c.unlink()
html = (R / "index.html").read_text(encoding="utf-8")
css = (R / "css/styles.css").read_text(encoding="utf-8")
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S); css = re.sub(r"\s+", " ", css)
css = re.sub(r"\s*([{};:,>])\s*", r"\1", css)
html = html.replace('<link rel="stylesheet" href="css/styles.css">', f"<style>{css}</style>")
(D / "index.html").write_text(html, encoding="utf-8")
for f in ["favicon.svg","manifest.webmanifest","robots.txt","sitemap.xml","_headers"]: shutil.copy(R / f, D / f)
shutil.copytree(R / "img", D / "img"); shutil.copytree(R / "js", D / "js")
print("dist/ pronto")
