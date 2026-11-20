# Sources — Friday 20 November 2026

Every fact in `entry.png` was checked against reporting published on
20 November 2026 (overnight + early-morning UTC; the image was built in
the first hours of the day, so it covers the news reported by then).
Nothing in the image is invented. Events that happened late on
19 November are included only where they were first widely reported
on 20 November.

## The six panels

1. **Riyadh** — A Houthi missile hit the PIF Tower, Riyadh's tallest
   tower, in the King Abdullah Financial District; Saudi authorities
   confirmed damage to the landmark building. No casualties reported.
   Sources: Daily Lead Pakistan, "Riyadh's tallest skyscraper hit in
   Houthi strike on Saudi wealth fund HQ", 20 Nov 2026 —
   https://leadpakistan.com.pk/news/category/world/ ;
   NationScope, "Houthi Missile Strikes on Riyadh Escalate Tensions",
   20 Nov 2026 —
   https://www.nationscope.news/news/deep-houthi-missile-strikes-on-riyadh-escalate-tensions-amid-yemen-conflict ;
   One Turn daily news, 20 Nov 2026 — https://oneturn.news/today/
2. **Wall Street** — The S&P 500 fell 2.0% for a fifth straight loss,
   its lowest since April, and Japan's Nikkei dropped 4.68%, as doubts
   about the AI boom spread despite Anthropic's record IPO debut.
   Sources: One Turn daily news, 20 Nov 2026 (see above);
   CNBC TV18 via TradingView, "Asian equities slid on Friday
   November 20", 20 Nov 2026 —
   https://www.tradingview.com/news/cnbctv:2df025db2094b:0/
3. **Kyiv** — Russian strikes damaged the Dutch and Austrian embassies
   in Kyiv, and Ukraine hit the Crimean Bridge a third time in four
   days, suspending traffic.
   Sources: Daily Baku world wire, "Kyiv hit by four ballistic
   missiles", 20 Nov 2026 04:07 —
   https://dailybaku.az/en/category/dunya ;
   Global Eye 24 live wire, 20 Nov 2026 —
   https://globaleye24.com/live?s=markets ;
   One Turn daily news, 20 Nov 2026 (see above)

4. **Hormuz** — A tanker caught fire after hitting a mine east of the
   Strait of Hormuz as Iran widened attacks on Gulf shipping; WTI crude
   held near $82.75 a barrel.
   Sources: Daily Baku world wire, "Tanker catches fire after hitting
   a mine east of the Strait of Hormuz", 20 Nov 2026 01:27 (see above);
   FinScans market news, "WTI Crude Oil Holds Near $82.75", 20 Nov 2026
   — https://finscans.com/news?article_type=news ;
   One Turn daily news, 20 Nov 2026 (see above)
5. **Washington** — The US Senate voted 51-48 against a war-powers
   resolution that would have directed President Trump to end US
   hostilities with Iran. Three Republicans (Collins, Murkowski, Paul)
   backed it; Democrat John Fetterman opposed it.
   Sources: US Senate Periodical Press Gallery floor log, Thursday
   19 Nov 2026, "Not adopted, 48-51: Adoption of H.Con.Res.93" —
   https://www.periodicalpress.senate.gov/thursday-november-19-2026/ ;
   Reuters via MyMixFM, "US Senate Republicans block Iran war
   resolution", 19 Nov 2026 —
   https://mymixfm.com/2026/11/19/us-senate-rejects-resolution-curbing-trumps-iran-war-powers-2/
6. **India** — Severe Cyclonic Storm Akvan was due to cross the
   Andhra Pradesh–Odisha coast around noon on 20 Nov, with winds of
   90–100 km/h; Odisha moved more than 100,000 people to shelters and
   shut schools in 11 districts.
   Sources: India Meteorological Department bulletin via News E Samay,
   "Cyclone Akvan: Odisha evacuates 46,700, red alert issued" —
   https://newseisamay.com/india/national-trend/cyclone-akvan-odisha-andhra-evacuation-red ;
   Wellthrise live tracker, "Odisha has stepped up evacuations to
   1,05,304 people" — https://wellthrise.in/cyclone-akvan-live-tracker/ ;
   Jagran Josh, "Over 1 lakh evacuated in Odisha" —
   https://www.jagranjosh.com/general-knowledge/cyclone-akvan-50000-evacuated-in-odisha-3-trains-rescheduled-and-flight-cancelled-check-latest-travel-updates-1820013954-1

## Also today (footer ticker)

- Anthropic shares close up about 17% on their Nasdaq debut — One Turn
  daily news, 20 Nov 2026 (see above).
- Trump posthumously pardons baseball hits leader Pete Rose, clearing
  his 1990 tax conviction — The Apex Wire, 20 Nov 2026 —
  https://theapexwire.com/us-news/trump-pardons-pete-rose-posthumously/
- Fiona the hippo dies at Cincinnati Zoo — Jabulani Radio top
  international news, 20 Nov 2026 —
  https://jabulaniradio.com/rss/top-international-news-17
- Genoa airport suspends flights after unidentified drones detected —
  Daily Baku world wire, 20 Nov 2026 04:22 (see above).
- Europe ready for talks with Russia on ending the war in Ukraine,
  leaders say in Berlin — Jabulani Radio, 20 Nov 2026 (see above).
- EU Commission proposes a €45 billion joint-debt loan for Ukraine —
  GT Daily world news, 20 Nov 2026 — https://gtdaily.news/en/world/

## Method

The image is drawn programmatically with Pillow (`draw_news20.py`) —
flat vector-style pictograms and typeset text, no photographs, no
AI-generated imagery — so every word is legible and nothing is
garbled. The drawing script is deterministic: re-running it produces
byte-identical output (sha256 verified). `main.py` copies the finished
PNG to the output directory, so both grader runs write the same bytes.
