from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/cover.jpg"
W, H = 1600, 2560

image = Image.new("RGB", (W, H))
pix = image.load()
for y in range(H):
    t = y / (H - 1)
    r = int(16 * (1 - t) + 23 * t)
    g = int(24 * (1 - t) + 59 * t)
    b = int(40 * (1 - t) + 95 * t)
    for x in range(W):
        pix[x, y] = (r, g, b)

draw = ImageDraw.Draw(image, "RGBA")
draw.ellipse((900, -100, 1740, 740), fill=(56, 189, 248, 30))
draw.ellipse((-300, 1700, 750, 2750), fill=(167, 139, 250, 25))
draw.rounded_rectangle((130, 180, 1470, 2380), radius=34, outline=(125, 211, 252, 90), width=3)

font_path = "/c/Windows/Fonts/msjh.ttc"
bold_path = "/c/Windows/Fonts/msjhbd.ttc"
latin = "/c/Windows/Fonts/arialbd.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def text(x, y, value, f, fill, **kwargs):
    draw.text((x, y), value, font=f, fill=fill, **kwargs)

text(180, 360, "PI CODING AGENT", font(latin, 72), (125, 211, 252, 255))
draw.rounded_rectangle((180, 555, 780, 567), radius=6, fill=(56, 189, 248, 255))
text(180, 760, "60 小時核心", font(bold_path, 136), (255, 255, 255, 255))
text(180, 960, "實戰教材", font(bold_path, 116), (255, 255, 255, 255))
text(180, 1190, "從入門、工作流、客製化", font(font_path, 54), (203, 213, 225, 255))
text(180, 1280, "到 SDK 與系統整合", font(font_path, 54), (203, 213, 225, 255))
text(180, 1400, "完整課程可延伸至 100 小時", font(font_path, 42), (125, 211, 252, 255))

# Agent workflow graphic
for start, end, color in [((180, 1720), (470, 1720), (56,189,248,255)), ((470,1720),(650,1500),(167,139,250,255)), ((180,1870),(430,1870),(56,189,248,255)), ((430,1870),(600,1660),(167,139,250,255))]:
    draw.line((start[0], start[1], end[0], end[1]), fill=color, width=18)
for x, y, color in [(180,1720,(56,189,248,255)), (470,1720,(167,139,250,255)), (650,1500,(56,189,248,255)), (180,1870,(56,189,248,255)), (430,1870,(167,139,250,255)), (600,1660,(56,189,248,255))]:
    draw.ellipse((x-24,y-24,x+24,y+24), fill=color)

text(180, 2190, "實作導向", font(font_path, 44), (148, 163, 184, 255))
text(180, 2280, "Pi Coding Agent 100 小時學習教材", font(font_path, 34), (100, 116, 139, 255))
image.save(OUT, "JPEG", quality=95, optimize=True, progressive=True, dpi=(300, 300))
print(OUT)
