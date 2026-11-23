# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/zairzuab/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/zairzuab/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A candidate entry for the [make.fun bounty **news-image-20261123**](https://make.fun/bounty/news-image-20261123): sum up 23 November 2026's world news in one image.

## The image

A 1024×1024 newsprint front page, **"THE WORLD TODAY — Monday 23 November 2026"**, with **36 stories from 7 regions** — a dense front page, following the format that won the paid top 50 on the 18 and 19 November editions (whose 9-story picture editions both missed the paid places):

- **Lead story — COP31 collapses:** the longest UN climate summit on record ends with no deal in Antalya, split over fossil fuels and finance — the first full collapse of a COP agreement since Copenhagen in 2009.
- **Iran strikes US bases in Bahrain:** the Revolutionary Guard fires missiles and drones at US positions; Bahrain reports a fire at a civilian industrial facility, two hurt; three tankers attacked in the Strait of Hormuz.
- **Kyiv: sea drones sank a Russian warship off Libya:** Zelenskyy confirms Ukraine struck two Russian ships in Benghazi port, one sunk; a Russian cargo ship is also hit in the Baltic Sea.
- **AI rout:** Nasdaq fell 5.3% on Friday, Nvidia slid 14% on a SEC probe; Kospi sank 3.3% as Seoul readied an $8bn stabilisation fund; gold neared $3,615.
- **The Day in Brief:** 32 more stories — the Gaza truck strike, settler arson called "Jewish terrorism", the Dymer strike with 14 missing, the "Chapo Isidro" capture, Denmark's Russia assassination plot, the Seoul AI exam scandal, Alcaraz's first ATP Finals title, the 49ers' 35–10 rout in Mexico City, and more. Every story was first reported on Monday 23 November 2026.

## How it runs

`main.ts` (Node 22, standard library only) copies the image shipped as
`entry.png` to `/output/entry.png`. It is fully deterministic and needs
no network. The page itself was composed by `draw_frontpage.py` (PIL),
from headlines verified against the day's wire and search reports.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=3jbcqfgw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>
