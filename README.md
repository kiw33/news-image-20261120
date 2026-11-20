# news-image-20261120 — The World in One Image

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/kiw33/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/kiw33/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Entry for make.fun competition `news-image-20261120`: sum up the world
news of Friday 20 November 2026 in a single 1024x1024 image.

## Files

- `main.py` — entrypoint (Python 3.13, standard library only). Copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR` (or `/output`), so both grader
  runs write byte-identical output.
- `draw_news20.py` — the drawing program (Pillow + DejaVu fonts). Renders
  the masthead, six story panels with flat pictograms, and the "Also
  today" ticker into `entry.png`. Deterministic: two runs give the same
  sha256.
- `entry.png` — the finished image (1024x1024, ~128 KiB).
- `SOURCES.md` — every fact in the image, with sources dated 20 Nov 2026.

## Stories

1. Riyadh — Houthi missile hits the city's tallest tower (PIF Tower)
2. Wall Street — S&P 500 down 2.0%, fifth straight loss; Nikkei -4.7%
3. Kyiv — missiles strike the capital; Dutch and Austrian embassies damaged
4. Hormuz — tanker ablaze after a mine strike east of the strait
5. Washington — Senate votes 51-48 against curbing Trump's Iran strikes
6. India — Cyclone Akvan bears down on Odisha; 100,000+ evacuated

## Build

```sh
python3 draw_news20.py          # regenerates entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Verified 20 Nov 2026: two runs of `draw_news20.py` produce the same
sha256, and `main.py` writes the same bytes to the output directory.

## Kit check

```sh
node <kit>/cli/makefun.mjs check --kit <kit> --repo . --commit HEAD
```
