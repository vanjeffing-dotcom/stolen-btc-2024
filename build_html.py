#!/usr/bin/env python3
"""
Render every Markdown file in this directory to a sibling .html with a clean,
self-contained template. The sealed .md originals stay byte-identical; the .html
versions are *not* covered by the BIP-322 signature — they're a UX aid only.

Run from site/:
    python3 build_html.py
"""
from __future__ import annotations
import hashlib
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("pip install --break-system-packages markdown", file=sys.stderr)
    sys.exit(2)

HERE = Path(__file__).parent.resolve()

# Sealed file hashes (must remain unchanged)
SEALED = {
    "STATEMENT_KO.md": "d6c73c8dc51b5e0b6aa076d15a2fc9b4b9d19c3aaac0ba8ba7b3719272c27f93",
    "STATEMENT_EN.md": "7948e26829024685245479a94c18bdc5760eccbdd34daf7f1d0ade1e6bdd09e4",
    "EVIDENCE_KO.md":  "741390f29fdc6a847382e8762f717a7111fb2eb3b5e753af000c56b37c9039a0",
    "EVIDENCE_EN.md":  "77681db33a7ceb8b33020b1ed913bdba48cec075345bf800ec98e5285c99b5ca",
}

CSS = """
:root {
  --fg: #1a1a1a;
  --fg-mute: #555;
  --bg: #fafafa;
  --bg-card: #ffffff;
  --accent: #0366d6;
  --border: #e1e4e8;
  --code-bg: #f6f8fa;
  --warn-bg: #fffbea;
  --warn-border: #f0c36d;
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Apple SD Gothic Neo", "Noto Sans KR", sans-serif;
  max-width: 900px; margin: 0 auto; padding: 24px;
  line-height: 1.65; color: var(--fg); background: var(--bg);
}
.nav {
  background: var(--bg-card); border: 1px solid var(--border); border-radius: 8px;
  padding: 12px 16px; margin-bottom: 32px; font-size: 0.92em;
  position: sticky; top: 12px; z-index: 10;
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.nav a { margin-right: 14px; color: var(--accent); text-decoration: none; }
.nav a:hover { text-decoration: underline; }
.nav .sep { color: var(--border); margin: 0 4px; }
.nav .lang { float: right; font-size: 0.9em; color: var(--fg-mute); }
.nav .lang a { color: var(--fg-mute); }

h1, h2, h3, h4 { color: #111; line-height: 1.3; }
h1 { border-bottom: 2px solid #333; padding-bottom: 0.3em; margin-top: 0.5em; }
h2 { border-bottom: 1px solid var(--border); padding-bottom: 0.2em; margin-top: 2em; }
h3 { margin-top: 1.5em; }

p, ul, ol { margin: 0.8em 0; }
ul, ol { padding-left: 1.5em; }
li { margin: 0.3em 0; }

table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.95em; }
th, td { border: 1px solid var(--border); padding: 8px 12px; text-align: left; vertical-align: top; }
th { background: #f0f3f6; font-weight: 600; }
tr:nth-child(even) td { background: #fcfcfc; }

code { background: var(--code-bg); padding: 2px 6px; border-radius: 3px; font-family: "SF Mono", Monaco, Consolas, monospace; font-size: 0.88em; color: #333; }
pre { background: #2d2d2d; color: #e8e8e8; padding: 16px; border-radius: 6px; overflow-x: auto; line-height: 1.4; }
pre code { background: transparent; color: inherit; padding: 0; font-size: 0.88em; }

a { color: var(--accent); }
a:hover { text-decoration: underline; }

blockquote {
  border-left: 4px solid var(--warn-border); margin: 1.2em 0; padding: 0.8em 1.2em;
  color: var(--fg); background: var(--warn-bg); border-radius: 0 4px 4px 0;
}
blockquote p:first-child { margin-top: 0; }
blockquote p:last-child { margin-bottom: 0; }

hr { border: none; border-top: 1px solid var(--border); margin: 2.5em 0; }

.footer {
  margin-top: 4em; padding-top: 1em; border-top: 1px solid var(--border);
  color: var(--fg-mute); font-size: 0.85em; text-align: center;
}
.footer a { color: var(--fg-mute); }

.seal-banner {
  background: #e6f4ea; border: 1px solid #34a853; color: #137333;
  padding: 8px 12px; border-radius: 4px; font-size: 0.88em; margin: 0.5em 0 1.5em;
}
.seal-banner code { background: rgba(0,0,0,0.06); }
"""

NAV_KO = """<nav class="nav">
<a href="index.html">🏠 홈</a><span class="sep">·</span>
<a href="STATEMENT_KO.html">🇰🇷 성명서</a>
<a href="EVIDENCE_KO.html">증거</a>
<a href="MIRRORS_KO.html">미러</a><span class="sep">·</span>
<a href="signed_message.txt">🔐 서명 (raw)</a>
<a href="https://mempool.space/tx/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4" target="_blank">⛓️ 절도 TX</a>
<span class="lang"><a href="STATEMENT_EN.html">EN ↗</a></span>
</nav>"""

NAV_EN = """<nav class="nav">
<a href="index.html">🏠 Home</a><span class="sep">·</span>
<a href="STATEMENT_EN.html">🇺🇸 Statement</a>
<a href="EVIDENCE_EN.html">Evidence</a>
<a href="MIRRORS_EN.html">Mirrors</a><span class="sep">·</span>
<a href="signed_message.txt">🔐 Signature (raw)</a>
<a href="https://mempool.space/tx/e867f6973fa3fc35487ca38bc9fbf0912bde4612d17d6a444d525aaf8dc173d4" target="_blank">⛓️ Theft TX</a>
<span class="lang"><a href="STATEMENT_KO.html">KO ↗</a></span>
</nav>"""

FOOTER = """<div class="footer">
이 페이지는 sealed .md 파일을 시각화한 보조 뷰입니다. 무결성 검증의 절대 기준은 sealed .md 파일 자체와 <a href="signed_message.txt">signed_message.txt</a> 입니다.<br>
This page is an auxiliary HTML rendering of the sealed .md files. The ground truth for integrity verification is the sealed .md content and <a href="signed_message.txt">signed_message.txt</a>.<br><br>
CC0 1.0 Public Domain.
</div>"""


def is_korean_file(stem: str) -> bool:
    return stem.endswith("_KO") or stem in ("README", "SETUP")  # default to KO nav for repo docs


def render_md_file(md_path: Path) -> None:
    md_text = md_path.read_text(encoding="utf-8")
    body_html = markdown.markdown(
        md_text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
        output_format="html5",
    )
    # Rewrite intra-doc .md links to .html
    body_html = re.sub(r'href="([^"#]+)\.md"', r'href="\1.html"', body_html)
    body_html = re.sub(r'href="([^"#]+)\.md#', r'href="\1.html#', body_html)

    stem = md_path.stem
    is_ko = is_korean_file(stem)
    nav = NAV_KO if is_ko else NAV_EN
    title_lang = "KO" if is_ko else "EN"

    # Seal banner for the 4 sealed files
    seal_html = ""
    md_name = md_path.name
    if md_name in SEALED:
        actual = hashlib.sha256(md_text.encode("utf-8")).hexdigest()
        expected = SEALED[md_name]
        if actual == expected:
            seal_html = (
                f'<div class="seal-banner">✅ <strong>Sealed</strong> · SHA-256 '
                f"<code>{actual}</code> matches the BIP-322 signature commitment in "
                f'<a href="signed_message.txt">signed_message.txt</a>.</div>'
            )
        else:
            seal_html = (
                f'<div class="seal-banner" style="background:#fce8e6;border-color:#ea4335;color:#a50e0e">'
                f"⚠️ <strong>HASH MISMATCH</strong> · expected <code>{expected}</code>, "
                f"got <code>{actual}</code>. This file has been tampered with.</div>"
            )

    out = f"""<!DOCTYPE html>
<html lang="{'ko' if is_ko else 'en'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{stem} — Stolen BTC 2024-11-05</title>
<meta name="description" content="Public statement of 6.318566 BTC stolen on 2024-11-05, cryptographically signed by the rightful owner.">
<style>{CSS}</style>
</head>
<body>
{nav}
{seal_html}
{body_html}
{FOOTER}
</body>
</html>
"""
    out_path = md_path.with_suffix(".html")
    out_path.write_text(out, encoding="utf-8")
    print(f"  rendered: {md_path.name} → {out_path.name}")


def main():
    rendered = 0
    for md in sorted(HERE.glob("*.md")):
        if md.name == "README.md":
            continue  # README is for GitHub viewers, not the IPFS site
        render_md_file(md)
        rendered += 1
    print(f"\nTotal rendered: {rendered}")

    # Sanity check sealed files unchanged
    print("\nSealed-file integrity check:")
    all_ok = True
    for name, expected in SEALED.items():
        path = HERE / name
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        ok = actual == expected
        all_ok = all_ok and ok
        print(f"  {'✅' if ok else '❌'} {name}  {actual}")
    if not all_ok:
        print("\nSEALED FILES TAMPERED — aborting build.")
        sys.exit(1)


if __name__ == "__main__":
    main()
