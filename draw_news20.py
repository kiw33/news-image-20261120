#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news image.

Flat vector-style pictograms and typeset text, rendered with Pillow.
No photographs, no network, no randomness: re-running this script
produces byte-identical output.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
MARGIN = 28

PAPER = (247, 243, 234)
INK = (24, 32, 48)
NAVY = (27, 58, 95)
WHITE = (255, 255, 255)
GREY = (96, 104, 116)
RED = (178, 44, 36)
TEAL = (18, 122, 106)
GOLD = (196, 141, 28)
SKY = (64, 130, 184)
ORANGE = (214, 110, 30)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


F_TITLE = font("DejaVuSans-Bold.ttf", 56)
F_KICKER = font("DejaVuSans-Bold.ttf", 21)
F_SUB = font("DejaVuSans.ttf", 22)
F_TAG = font("DejaVuSans-Bold.ttf", 20)
F_HEAD = font("DejaVuSans-Bold.ttf", 26)
F_BODY = font("DejaVuSans.ttf", 19)
F_TICK = font("DejaVuSans-Bold.ttf", 19)
F_TICK_BODY = font("DejaVuSans.ttf", 19)


def wrap(text, fnt, width, draw):
    """Greedy word wrap; returns a list of lines fitting width."""
    words = text.split()
    lines = []
    cur = ""
    for word in words:
        trial = word if not cur else cur + " " + word
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_tower(d, x, y, s, color):
    """Skyscraper with a missile streak and small burst."""
    d.rectangle([x + s * 0.30, y + s * 0.15, x + s * 0.62, y + s * 0.95], fill=color)
    d.polygon([(x + s * 0.30, y + s * 0.15), (x + s * 0.46, y),
               (x + s * 0.62, y + s * 0.15)], fill=color)
    for row in range(5):
        for col in range(2):
            wx = x + s * (0.36 + col * 0.11)
            wy = y + s * (0.28 + row * 0.13)
            d.rectangle([wx, wy, wx + s * 0.06, wy + s * 0.07], fill=GOLD)
    d.line([x + s * 0.05, y + s * 0.30, x + s * 0.28, y + s * 0.12],
           fill=RED, width=4)
    bx, by = x + s * 0.08, y + s * 0.30
    for ang in range(0, 360, 45):
        r = math.radians(ang)
        d.line([bx, by, bx + s * 0.13 * math.cos(r), by + s * 0.13 * math.sin(r)],
               fill=RED, width=3)


def draw_chart(d, x, y, s, color):
    """Falling market line with arrow."""
    d.line([x + s * 0.10, y + s * 0.10, x + s * 0.10, y + s * 0.90],
           fill=GREY, width=3)
    d.line([x + s * 0.10, y + s * 0.90, x + s * 0.92, y + s * 0.90],
           fill=GREY, width=3)
    pts = [(0.14, 0.28), (0.34, 0.38), (0.50, 0.34), (0.66, 0.58),
           (0.80, 0.72), (0.90, 0.86)]
    for (ax, ay), (bx, by) in zip(pts, pts[1:]):
        d.line([x + s * ax, y + s * ay, x + s * bx, y + s * by],
               fill=RED, width=5)
    ex, ey = x + s * 0.90, y + s * 0.86
    d.polygon([(ex, ey), (ex - s * 0.10, ey - s * 0.02),
               (ex - s * 0.02, ey - s * 0.10)], fill=RED)
    d.ellipse([x + s * 0.10, y + s * 0.22, x + s * 0.18, y + s * 0.30],
              fill=TEAL)


def draw_burst(d, x, y, s, color):
    """Explosion burst over a city block."""
    d.rectangle([x + s * 0.12, y + s * 0.62, x + s * 0.38, y + s * 0.95],
                fill=color)
    d.rectangle([x + s * 0.48, y + s * 0.50, x + s * 0.74, y + s * 0.95],
                fill=color)
    d.rectangle([x + s * 0.80, y + s * 0.70, x + s * 0.94, y + s * 0.95],
                fill=color)
    cx, cy = x + s * 0.55, y + s * 0.30
    for ang in range(0, 360, 30):
        r = math.radians(ang)
        ln = s * (0.16 if ang % 60 == 0 else 0.10)
        d.line([cx, cy, cx + ln * math.cos(r), cy + ln * math.sin(r)],
               fill=GOLD, width=4)
    d.ellipse([cx - s * 0.07, cy - s * 0.07, cx + s * 0.07, cy + s * 0.07],
              fill=RED)


def draw_ship(d, x, y, s, color):
    """Tanker hull on waves with a flame."""
    d.polygon([(x + s * 0.08, y + s * 0.55), (x + s * 0.92, y + s * 0.55),
               (x + s * 0.80, y + s * 0.78), (x + s * 0.20, y + s * 0.78)],
              fill=color)
    d.rectangle([x + s * 0.55, y + s * 0.30, x + s * 0.72, y + s * 0.55],
                fill=color)
    d.rectangle([x + s * 0.20, y + s * 0.38, x + s * 0.34, y + s * 0.55],
                fill=color)
    fx, fy = x + s * 0.27, y + s * 0.30
    d.polygon([(fx - s * 0.08, fy + s * 0.10), (fx, fy - s * 0.14),
               (fx + s * 0.08, fy + s * 0.10), (fx, fy + s * 0.02)],
              fill=ORANGE)
    for k in range(3):
        wy = y + s * (0.86 + k * 0.05)
        d.arc([x + s * 0.05, wy - s * 0.03, x + s * 0.95, wy + s * 0.05],
              0, 180, fill=SKY, width=3)


def draw_dome(d, x, y, s, color):
    """Capitol dome with columns."""
    d.rectangle([x + s * 0.18, y + s * 0.55, x + s * 0.82, y + s * 0.95],
                fill=color)
    d.pieslice([x + s * 0.25, y + s * 0.12, x + s * 0.75, y + s * 0.62],
               180, 360, fill=color)
    d.rectangle([x + s * 0.47, y + s * 0.02, x + s * 0.53, y + s * 0.14],
                fill=color)
    for col in range(4):
        cx0 = x + s * (0.24 + col * 0.15)
        d.rectangle([cx0, y + s * 0.62, cx0 + s * 0.06, y + s * 0.88],
                    fill=PAPER)
    d.rectangle([x + s * 0.10, y + s * 0.90, x + s * 0.90, y + s * 0.96],
                fill=color)


def draw_cyclone(d, x, y, s, color):
    """Spiral storm with rain streaks."""
    cx, cy = x + s * 0.50, y + s * 0.46
    for k in range(4):
        r = s * (0.08 + k * 0.09)
        d.arc([cx - r, cy - r, cx + r, cy + r], 20 + k * 40,
              300 + k * 40, fill=color, width=4)
    for k in range(5):
        rx = x + s * (0.10 + k * 0.18)
        d.line([rx, y + s * 0.82, rx - s * 0.03, y + s * 0.97],
               fill=SKY, width=3)


ICONS = {
    "tower": draw_tower,
    "chart": draw_chart,
    "burst": draw_burst,
    "ship": draw_ship,
    "dome": draw_dome,
    "cyclone": draw_cyclone,
}

STORIES = [
    ("RIYADH", "Houthi missile hits Riyadh's tallest tower", RED,
     "Saudi Arabia confirms damage to the PIF Tower in the capital's "
     "financial district. No casualties are reported.", "tower"),
    ("WALL STREET", "Stocks slide for a fifth straight day", NAVY,
     "The S&P 500 falls 2.0% to its lowest since April and the Nikkei "
     "drops 4.7% as doubts about the AI boom spread.", "chart"),
    ("KYIV", "Missiles strike Kyiv; embassies damaged", TEAL,
     "Russian strikes damage the Dutch and Austrian embassies. Ukraine "
     "hits the Crimean Bridge a third time in four days.", "burst"),
    ("HORMUZ", "Tanker ablaze after mine strike", ORANGE,
     "A tanker catches fire east of the Strait of Hormuz as attacks on "
     "Gulf shipping widen. Oil holds near $83 a barrel.", "ship"),
    ("WASHINGTON", "Senate keeps the Iran war powers", GOLD,
     "Senators vote 51-48 against curbing Trump's Iran strikes; three "
     "Republicans backed it, one Democrat opposed it.", "dome"),
    ("INDIA", "Cyclone Akvan bears down on Odisha", SKY,
     "Landfall is due around noon. More than 100,000 people are moved "
     "to shelters and schools shut in 11 districts.", "cyclone"),
]

TICKER = ("ALSO TODAY  \u2022  Anthropic +17% on Nasdaq debut  "
          "\u2022  Trump pardons Pete Rose, posthumously  "
          "\u2022  Fiona the hippo dies at Cincinnati Zoo  \u2022  Genoa "
          "airport halts flights after drones  \u2022  Europe ready "
          "for Ukraine talks  \u2022  EU proposes \u20ac45bn loan for Ukraine")


def draw_panel(d, x, y, w, h, story):
    tag, headline, accent, body, icon = story
    d.rectangle([x, y, x + w, y + h], fill=WHITE, outline=(200, 196, 184),
                width=2)
    d.rectangle([x, y, x + w, y + 8], fill=accent)
    ix, iy, isize = x + 16, y + 30, 104
    ICONS[icon](d, ix, iy, isize, accent)
    tx = x + 136
    tw = w - 136 - 18
    d.text((tx, y + 26), tag, font=F_TAG, fill=accent)
    lines = wrap(headline, F_HEAD, tw, d)
    ly = y + 56
    for line in lines[:2]:
        d.text((tx, ly), line, font=F_HEAD, fill=INK)
        ly += 32
    blines = wrap(body, F_BODY, tw, d)
    by = ly + 6
    for line in blines[:4]:
        d.text((tx, by), line, font=F_BODY, fill=(58, 64, 76))
        by += 25


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=NAVY)
    d.text((MARGIN, 30), "THE WORLD IN ONE IMAGE", font=F_KICKER, fill=NAVY)
    d.text((MARGIN, 62), "FRIDAY 20 NOVEMBER 2026", font=F_TITLE, fill=INK)
    d.text((MARGIN, 132),
           "Six stories that defined the day \u2014 from Riyadh to Wall Street",
           font=F_SUB, fill=GREY)
    d.line([MARGIN, 168, W - MARGIN, 168], fill=INK, width=3)
    gx, gy = MARGIN, 184
    pw = (W - 2 * MARGIN - 16) // 2
    ph = 236
    for i, story in enumerate(STORIES):
        px = gx + (i % 2) * (pw + 16)
        py = gy + (i // 2) * (ph + 14)
        draw_panel(d, px, py, pw, ph, story)
    ty = gy + 3 * ph + 2 * 14 + 12
    d.rectangle([0, ty, W, H], fill=NAVY)
    tlines = wrap(TICKER, F_TICK_BODY, W - 2 * MARGIN, d)
    ly = ty + 12
    for line in tlines[:3]:
        d.text((MARGIN, ly), line, font=F_TICK_BODY, fill=WHITE)
        ly += 24
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
