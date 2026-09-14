from pathlib import Path
from html import escape
from zipfile import ZipFile, ZIP_STORED, ZIP_DEFLATED
from uuid import uuid4
import re

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
WORK = DIST / "epub"

chapters = [
    ("00-preface", "前言", ROOT / "PREFACE.md"),
    ("01-basic", "01 基礎入門", ROOT / "course/01-basic/README.md"),
    ("02-sessions", "02 互動模式與 Session 工作流", ROOT / "course/02-workflow-sessions/README.md"),
    ("03-security", "03 設定、安全與平台環境", ROOT / "course/03-settings-security/README.md"),
    ("04-models", "04 Provider、模型與本地模型", ROOT / "course/04-providers-models/README.md"),
    ("05-workflows", "05 Prompt Templates、Skills、Themes", ROOT / "course/05-prompts-skills-themes/README.md"),
    ("06-extensions", "06 Extensions 開發", ROOT / "course/06-extensions/README.md"),
    ("07-integration", "07 SDK、RPC 與 JSON 整合", ROOT / "course/07-sdk-rpc-json/README.md"),
    ("08-project", "08 總整專題", ROOT / "course/08-final-project/README.md"),
    ("appendix", "附錄：作業、檢查表與問題排除", None),
]
appendix = [
    ("assignments", "作業與實作題", ROOT / "assignments/ASSIGNMENTS.md"),
    ("checklist", "學習者進度檢查表", ROOT / "LEARNING_CHECKLIST.md"),
    ("troubleshooting", "常見問題排除", ROOT / "docs/TROUBLESHOOTING.md"),
    ("migration", "從其他 Coding Agent 遷移到 Pi", ROOT / "docs/AGENT_MIGRATION_GUIDE.md"),
]

CSS = """body{font-family:serif;line-height:1.7;margin:5%;color:#202938}h1{color:#173b5f;border-bottom:2px solid #38bdf8;padding-bottom:.3em}h2{color:#24577d;margin-top:1.5em}h3{color:#456b85}pre{background:#f1f5f9;padding:1em;overflow-wrap:anywhere;white-space:pre-wrap;font-family:monospace}code{background:#eef2f7;padding:.1em .25em}table{border-collapse:collapse;border:1px solid #64748b;width:100%;margin:1em 0}td,th{border:1px solid #64748b;padding:.4em;text-align:left}th{background:#e2e8f0}li{margin:.25em 0}.cover{text-align:center}.cover img{max-width:100%;height:auto}.cover-title{font-size:2em;font-weight:bold}"""

def md_to_html(text):
    lines = text.replace("\r\n", "\n").split("\n")
    out, code = [], []
    in_code = False
    list_kind = None
    table_open = False
    table_header = False

    def close_list():
        nonlocal list_kind
        if list_kind:
            out.append(f"</{list_kind}>")
            list_kind = None

    def close_table():
        nonlocal table_open, table_header
        if table_open:
            out.append("</tbody></table>")
            table_open = False
            table_header = False

    def close_blocks():
        close_list()
        close_table()

    for line in lines:
        if line.startswith("```"):
            if in_code:
                out.append("<pre><code>" + escape("\n".join(code)) + "</code></pre>")
                code, in_code = [], False
            else:
                close_blocks()
                in_code = True
            continue
        if in_code:
            code.append(line)
            continue
        if not line.strip():
            close_blocks()
            continue
        m = re.match(r"^(#{1,3})\s+(.*)$", line)
        if m:
            close_blocks()
            level = len(m.group(1))
            out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
            continue
        unordered = re.match(r"^[-*]\s+(.*)$", line)
        ordered = re.match(r"^\d+\.\s+(.*)$", line)
        if unordered or ordered:
            kind = "ul" if unordered else "ol"
            if list_kind != kind:
                close_blocks(); out.append(f"<{kind}>"); list_kind = kind
            value = (unordered or ordered).group(1)
            out.append("<li>" + inline(value) + "</li>")
            continue
        if line.startswith("|"):
            close_list()
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
                continue
            if not table_open:
                out.append("<table><thead><tr>" + "".join(f"<th>{inline(cell)}</th>" for cell in cells) + "</tr></thead><tbody>")
                table_open = True
                table_header = True
            else:
                out.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>")
            continue
        close_blocks()
        out.append("<p>" + inline(line) + "</p>")
    if in_code:
        out.append("<pre><code>" + escape("\n".join(code)) + "</code></pre>")
    close_blocks()
    return "\n".join(out)

def inline(value):
    value = escape(value)
    value = re.sub(r"`([^`]+)`", r"<code>\1</code>", value)
    value = re.sub(r"\[([^]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", value)
    return value

def page(slug, title, body):
    # 每個 Markdown 檔案通常已有第一個 H1；頁面標題已由外層產生，避免重複顯示。
    body = re.sub(r'^\s*<h1>.*?</h1>\s*', '', body, count=1, flags=re.S)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="zh-TW"><head><title>{escape(title)}</title><link rel="stylesheet" type="text/css" href="../styles/style.css"/></head><body><h1>{escape(title)}</h1>{body}</body></html>'''

def build():
    if WORK.exists():
        import shutil; shutil.rmtree(WORK)
    (WORK / "META-INF").mkdir(parents=True)
    (WORK / "OEBPS").mkdir()
    (WORK / "OEBPS/text").mkdir()
    (WORK / "OEBPS/images").mkdir()
    (WORK / "OEBPS/styles").mkdir()
    (WORK / "mimetype").write_text("application/epub+zip", encoding="utf-8")
    (WORK / "META-INF/container.xml").write_text('''<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>''', encoding="utf-8")
    (WORK / "OEBPS/styles/style.css").write_text(CSS, encoding="utf-8")
    cover = ROOT / "assets/cover.jpg"
    if not cover.exists():
        raise FileNotFoundError("請先執行 scripts/build_cover_jpg.py 產生封面 JPG")
    (WORK / "OEBPS/images/cover.jpg").write_bytes(cover.read_bytes())
    (WORK / "OEBPS/text/cover.xhtml").write_text('''<?xml version="1.0" encoding="UTF-8"?><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="zh-TW"><head><title>封面</title><link rel="stylesheet" href="../styles/style.css"/></head><body class="cover"><img src="../images/cover.jpg" alt="Pi Coding Agent 100 小時實戰教材"/></body></html>''', encoding="utf-8")
    items = [('cover', 'text/cover.xhtml', 'application/xhtml+xml', ''), ('cover-image', 'images/cover.jpg', 'image/jpeg', 'properties="cover-image"')]
    spine = ['cover']
    nav = []
    all_pages = chapters[:9] + appendix
    for slug, title, path in all_pages:
        if path is None: continue
        html = md_to_html(path.read_text(encoding="utf-8"))
        fn = f"text/{slug}.xhtml"
        (WORK / "OEBPS" / fn).write_text(page(slug, title, html), encoding="utf-8")
        items.append((slug, fn, 'application/xhtml+xml', ''))
        spine.append(slug)
        nav.append((slug, title))
    nav_html = "\n".join(f'<li><a href="{slug}.xhtml">{escape(title)}</a></li>' for slug, title in nav)
    (WORK / "OEBPS/text/nav.xhtml").write_text(f'''<?xml version="1.0" encoding="UTF-8"?><html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="zh-TW"><head><title>目錄</title></head><body><nav epub:type="toc" id="toc"><h1>目錄</h1><ol>{nav_html}</ol></nav></body></html>''', encoding="utf-8")
    items.append(('nav', 'text/nav.xhtml', 'application/xhtml+xml', 'properties="nav"'))
    manifest = "\n".join(f'<item id="{i}" href="{href}" media-type="{media}" {prop}/>' for i, href, media, prop in items)
    spine_xml = "\n".join(f'<itemref idref="{i}"/>' for i in spine)
    modified = "2026-09-14T00:00:00Z"
    opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">https://github.com/e945935/pi-coding-agent-100h</dc:identifier><dc:title>Pi Coding Agent 100 小時實戰教材</dc:title><dc:language>zh-TW</dc:language><dc:creator>Pi Coding Agent 100 小時教材編輯團隊</dc:creator><dc:publisher>Pi Coding Agent 100 小時教材編輯團隊</dc:publisher><dc:subject>Technology / Programming</dc:subject><dc:description>從入門、工作流、客製化到 SDK 與系統整合的繁體中文實作教材。</dc:description><meta property="dcterms:modified">{modified}</meta><meta name="cover" content="cover-image"/></metadata><manifest>{manifest}<item id="css" href="styles/style.css" media-type="text/css"/></manifest><spine><itemref idref="cover" linear="no"/> {spine_xml}</spine></package>'''
    (WORK / "OEBPS/content.opf").write_text(opf, encoding="utf-8")
    output = DIST / "pi-coding-agent-100h.epub"
    with ZipFile(output, "w") as z:
        z.write(WORK / "mimetype", "mimetype", compress_type=ZIP_STORED)
        for f in sorted(WORK.rglob("*")):
            if f.is_file() and f.name != "mimetype":
                z.write(f, f.relative_to(WORK).as_posix(), compress_type=ZIP_DEFLATED)
    print(output)

if __name__ == "__main__":
    build()
