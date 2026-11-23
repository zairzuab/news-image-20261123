# draw_frontpage.py — composes the 23 November 2026 front page with PIL.
# Own code, written for news-image-20261123. Run: python3 draw_frontpage.py
# Output: entry.png, 1024x1024, a dense newspaper front page with 36 stories.
# All headlines below were verified against wire/search reports of 23 Nov 2026.
# Layout budget (1024 tall): masthead ~150, lead ~150, second row ~130,
# grid 8 rows x 60, brief ~80, footer ~30. An assert catches any overflow.

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)      # newsprint off-white
INK = (18, 18, 18)           # near-black
RED = (178, 34, 34)          # brick red for kickers / rules
GREY = (74, 74, 74)          # deck grey
RULE = (150, 145, 132)       # thin rule grey
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def fit_one_line(draw, text, fnt, max_w):
    """Truncate text with an ellipsis so it fits max_w on one line."""
    if draw.textlength(text, font=fnt) <= max_w:
        return text
    short = text
    while short and draw.textlength(short + "\u2026", font=fnt) > max_w:
        short = short[:-1]
    return short + "\u2026"


def draw_center(draw, text, fnt, y, fill=INK):
    draw.text((W // 2, y), text, font=fnt, fill=fill, anchor="ma")


def rule(draw, y, x0, x1, width=2, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


# ---------------------------------------------------------------- stories
LEAD = {
    "kicker": "CLIMATE  |  COP31, ANTALYA",
    "headline": "CLIMATE TALKS COLLAPSE",
    "deck": ("The longest UN climate summit on record ends with no deal after running "
             "two days into overtime \u2014 split over fossil fuels and finance, the first "
             "full collapse of a COP agreement since Copenhagen in 2009."),
}

SECOND = [
    {
        "kicker": "IRAN WAR  |  THE GULF",
        "headline": "Iran strikes US bases in Bahrain; tankers hit in Hormuz",
        "deck": ("The Revolutionary Guard fires missiles and drones at US positions; "
                 "Bahrain says an industrial site was hit and two people were hurt. "
                 "Three tankers are attacked in the Strait of Hormuz."),
    },
    {
        "kicker": "WAR IN UKRAINE  |  THE MEDITERRANEAN",
        "headline": "Kyiv: sea drones sank a Russian warship off Libya",
        "deck": ("Zelenskyy confirms Ukraine struck two Russian ships in Benghazi port, "
                 "one of them sunk; a Russian cargo ship is also hit in the Baltic Sea."),
    },
]

# (kicker, headline, deck) — 24 items, 3 columns x 8 rows
GRID = [
    ("GAZA", "Truck strike in Gaza kills three",
     "Israeli forces hit a truck; health ministry says three killed."),
    ("WEST BANK", "Settler arson is \u201cJewish terrorism\u201d",
     "PM-elect Eisenkot condemns arson attacks near Ramallah."),
    ("YEMEN", "Houthis claim strike on Saudi refinery",
     "Rebels say they hit the Rabigh oil refinery on the Red Sea coast."),
    ("AFRICA", "Sudan war deepens; Ebola fight hit",
     "Fighting in Ituri disrupts DR Congo\u2019s Ebola response, WHO says."),
    ("UKRAINE", "14 missing after strike near Kyiv",
     "Russian drone partly destroys a flat block in Dymer; rescuers dig on."),
    ("UKRAINE", "Child killed in strike on Zelenskyy\u2019s hometown",
     "Kryvyi Rih attack damages 25 flats, a hospital and schools."),
    ("UKRAINE", "Kindergarten hit in Kharkiv",
     "Russian drone strikes a kindergarten as attacks on cities go on."),
    ("UKRAINE", "Ukraine hits Russian oil plants",
     "Drones strike energy sites in Rostov, Perm and Tatarstan."),
    ("MARKETS", "AI rout: Nasdaq futures rebound",
     "Nasdaq fell 5.3% on Friday; futures rise about 3% as Asia steadies."),
    ("MARKETS", "Kospi sinks 3.3%; Seoul readies $8bn fund",
     "Korea\u2019s index fell 5.8% at the open, triggering a trading halt."),
    ("MARKETS", "Nvidia slides 14% on SEC probe",
     "Chip giant\u2019s shares dive as US regulators open a civil inquiry."),
    ("MARKETS", "Gold nears $3,615 as investors flee stocks",
     "Safe-haven metal gains over 2% in the market turmoil."),
    ("ASIA", "China cuts margin needs to calm markets",
     "Exchanges lower margin financing to 80% from 100%."),
    ("ASIA", "Seoul minister quits in AI exam scandal",
     "South Korea\u2019s education chief resigns over AI-assisted cheating."),
    ("ASIA", "Bangladesh: Hasina will be jailed if she returns",
     "Dhaka warns the ex-premier faces arrest on return from India."),
    ("EUROPE", "Denmark: Russia plotted to kill rapper",
     "Three held in Copenhagen; Moscow\u2019s defence attach\u00e9 expelled."),
    ("EUROPE", "Poland accuses Russia of provocation",
     "Warsaw protests after missiles menace its airspace."),
    ("EUROPE", "EU summons Russian envoy over Kyiv blasts",
     "Embassies damaged in strikes on the Ukrainian capital."),
    ("AMERICAS", "Cartel boss \u201cChapo Isidro\u201d captured",
     "Mexican forces seize the Sinaloa leader after a deadly firefight."),
    ("AMERICAS", "US intel chief: Putin \u201cno friend\u201d",
     "Top spy distances Moscow from Trump\u2019s praise of Putin."),
    ("AMERICAS", "States sue SpaceX over AI safety claims",
     "Oregon and Virginia allege users were misled on AI tools."),
    ("AMERICAS", "US lead over China in Asia at record low",
     "Lowy index shows Washington\u2019s edge narrowest since 2018."),
    ("WORLD", "EU and Indonesia sign landmark trade deal",
     "Brussels seals its biggest Asian trade pact in years."),
    ("SPORT", "Alcaraz wins first ATP Finals title",
     "Spaniard beats Zverev 6\u20132, 7\u20136 in Turin."),
]

BRIEF = [
    "M\u00e1rquez takes eighth MotoGP crown",
    "49ers rout Vikings 35\u201310 in Mexico City",
    "Skubal agrees record $450m Mets deal",
    "UN chief urges global AI rules",
    "China warns citizens off Mount Fuji",
    "Paris wealth-tax drive gathers pace",
    "New Epstein files raise Russia questions",
    "Belgrade floods after record rain",
    "Liverpool hit Man Utd 4\u20130",
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 30                      # side margin
    x1 = W - mx
    y = 18

    # ---- masthead ------------------------------------------------------
    draw_center(d, "THE WORLD TODAY", font(SERIF, 60), y)
    y += 64
    rule(d, y, mx, x1, 3)
    y += 7
    draw_center(d, "MONDAY 23 NOVEMBER 2026", font(SANS_B, 24), y)
    y += 28
    draw_center(d, "THE DAY\u2019S WORLD NEWS IN ONE PAGE  \u00b7  WORLD EDITION",
                font(SANS, 14), y, fill=GREY)
    y += 20
    rule(d, y, mx, x1, 3, fill=RED)
    y += 10

    # ---- lead story ----------------------------------------------------
    d.text((mx, y), LEAD["kicker"], font=font(SANS_B, 15), fill=RED)
    y += 20
    for line in wrap(d, LEAD["headline"], font(SERIF, 48), x1 - mx):
        draw_center(d, line, font(SERIF, 48), y)
        y += 50
    y += 2
    for line in wrap(d, LEAD["deck"], font(SERIF_REG, 18), x1 - mx - 40):
        draw_center(d, line, font(SERIF_REG, 18), y, fill=GREY)
        y += 21
    y += 6
    rule(d, y, mx, x1, 2)
    y += 8

    # ---- second row: two stories side by side --------------------------
    col_w = (x1 - mx - 24) // 2
    row_top = y
    max_y = row_top
    for i, s in enumerate(SECOND):
        cx = mx + i * (col_w + 24)
        cy = row_top
        d.text((cx, cy), s["kicker"], font=font(SANS_B, 13), fill=RED)
        cy += 20
        for line in wrap(d, s["headline"], font(SERIF, 25), col_w)[:2]:
            d.text((cx, cy), line, font=font(SERIF, 25), fill=INK)
            cy += 29
        cy += 2
        for line in wrap(d, s["deck"], font(SERIF_REG, 15), col_w)[:3]:
            d.text((cx, cy), line, font=font(SERIF_REG, 15), fill=GREY)
            cy += 18
        max_y = max(max_y, cy)
    # vertical divider between the two
    d.line([(mx + col_w + 12, row_top), (mx + col_w + 12, max_y)],
           fill=RULE, width=1)
    y = max_y + 5
    rule(d, y, mx, x1, 2)
    y += 8

    # ---- dense grid: 3 columns x 8 rows --------------------------------
    cols, rows = 3, 8
    gutter = 20
    gw = (x1 - mx - (cols - 1) * gutter) // cols
    row_h = 58
    for idx, (kick, head, deck) in enumerate(GRID):
        r, c = divmod(idx, cols)
        gx = mx + c * (gw + gutter)
        gy = y + r * row_h
        d.text((gx, gy), kick, font=font(SANS_B, 11), fill=RED)
        hy = gy + 12
        for line in wrap(d, head, font(SERIF, 15), gw)[:2]:
            d.text((gx, hy), line, font=font(SERIF, 15), fill=INK)
            hy += 17
        d.text((gx, hy), fit_one_line(d, deck, font(SERIF_REG, 11), gw),
               font=font(SERIF_REG, 11), fill=GREY)
    y = y + rows * row_h + 2
    rule(d, y, mx, x1, 2)
    y += 8

    # ---- in brief strip --------------------------------------------------
    d.text((mx, y), "IN BRIEF", font=font(SANS_B, 12), fill=RED)
    y += 16
    per_line = 3
    for li in range(0, len(BRIEF), per_line):
        line = "   \u2022   ".join(BRIEF[li:li + per_line])
        draw_center(d, line, font(SERIF, 14), y)
        y += 19
    y += 4

    # ---- footer ----------------------------------------------------------
    rule(d, y, mx, x1, 2)
    y += 6
    draw_center(d, "MONDAY 23 NOVEMBER 2026  \u00b7  36 STORIES FROM 7 REGIONS  \u00b7  "
                   "AS REPORTED ON THE DAY",
                font(SANS, 12), y, fill=GREY)
    y += 20
    assert y <= H - 6, f"layout overflow: content ends at {y}, canvas is {H}"
    img.save("entry.png", optimize=True)
    print(f"saved entry.png {img.size}, content ends at y={y}")
    print("stories: 1 lead + 2 second + 24 grid + 9 brief = 36")


if __name__ == "__main__":
    main()
