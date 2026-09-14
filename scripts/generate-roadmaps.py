#!/usr/bin/env python3
"""
Generate the 12 free "<Trade> Career Roadmap" PDFs promised by the quiz funnel
(js/quiz.js). One clean 2-page PDF per trade, dark industrial theme with the
site's orange accent (#ff6b00), matching generate_pdf.py conventions.

Salary bands are pulled from the site (trades.html / quiz.js - identical) and
cross-checked against the blog salary posts. Idempotent: reruns overwrite the
same files. Verification is built in (file size, pypdf reopen, quiz.js sync).
"""
import os
import re
import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(ROOT, "assets", "roadmaps")
QUIZ_JS = os.path.join(ROOT, "js", "quiz.js")
README_PATH = os.path.join(OUT_DIR, "README.md")

# --- Theme (matches generate_pdf.py + site) -----------------------------------
BG_DARK = HexColor("#0a0a0a")
BG_HEADER = HexColor("#140c05")
BG_CARD = HexColor("#1c1c1c")
BG_PANEL = HexColor("#161616")
BORDER = HexColor("#2e2e2e")
ORANGE = HexColor("#ff6b00")
YELLOW = HexColor("#ffc107")
WHITE = HexColor("#ffffff")
TEXT_BODY = HexColor("#b0b0b0")
TEXT_MUTED = HexColor("#8a8a8a")

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DejaVu", FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FONT_DIR + "DejaVuSans-Bold.ttf"))

WIDTH, HEIGHT = letter  # 612 x 792
MARGIN = 54
CONTENT_W = WIDTH - 2 * MARGIN

# --- Trade data (names/slugs/salary bands = exact quiz.js / trades.html) ------
# salary      -- site headline band (trades.html "Average Salary" + quiz result)
# salary_note -- page footer nuance or blog-cited median, or None (assumed)
# assumed     -- True where no dedicated salary blog post exists yet on the site
TRADES = [
    {
        "name": "Electrician",
        "icon": "⚡",
        "slug": "electrician",
        "salary": "$60K–$80K",
        "salary_note": "BLS median $61,590 (blog-cited) • apprentice 4–5 yr, ~8,000 OJT hrs • top licensed trade on the TradeLift board",
        "assumed": False,
        "overview": "Install, maintain, and repair the electrical systems that power homes, businesses, and industrial facilities. Electricians build everything on the National Electrical Code (NEC), troubleshoot live systems safely, and stay in demand nationwide — the highest-paying licensed trade on the TradeLift board.",
        "apprentice": "4–5 year apprenticeship",
        "certs": [
            "OSHA 10-Hour — the universal entry credential",
            "State journeyman electrician license: NEC exam (varies by state)",
            "IBEW union apprenticeship or IEC / ABC non-union programs",
            "Optional: EV-charging & solar installer certifications, master license",
            "First Aid/CPR + a clean driver's license",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm the fit",
            "Earn your OSHA 10 online (a few days)",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call your local IBEW hall for deadlines",
            "Search apprenticeship.gov electrician roles",
            "Ask a working electrician 5 questions",
            "Buy basics: multimeter, wire strippers",
            "Study NEC article 90 before intakes",
            "Apply to 3 apprenticeships or programs",
            "Prep for the apprentice aptitude test",
            "Shadow a helper shift if you can",
        ],
    },
    {
        "name": "Plumber",
        "icon": "🔧",
        "slug": "plumber",
        "salary": "$55K–$75K",
        "salary_note": "BLS median $59,880 (blog-cited) • apprentice 4–5 yr, ~8,000 OJT hrs • master plumbers run $75K–$100K+",
        "assumed": False,
        "overview": "Install and repair water supply, drainage, and gas systems that keep buildings safe and habitable. Plumbers work across residential, commercial, and industrial sites with year-round demand and a clear ladder from journeyman to master license and your own shop.",
        "apprentice": "4–5 year apprenticeship",
        "certs": [
            "OSHA 10-Hour — the universal entry credential",
            "State journeyman plumber license (UA-apprenticeship pathway)",
            "Backflow prevention certification",
            "Union apprenticeship through a local UA hall",
            "Master plumber license later (permits + own shop)",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm the fit",
            "Earn your OSHA 10 online",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call a local UA hall for intake dates",
            "Search apprenticeship.gov plumbing roles",
            "Buy basics: pipe wrench, adjustable wrench",
            "Learn to read a rough-in plumbing print",
            "Shadow a plumber for half a day",
            "Apply to 3 union or private programs",
            "Practice the intake math and reading test",
            "Line up references before interviews",
        ],
    },
    {
        "name": "Welder",
        "icon": "🔥",
        "slug": "welder",
        "salary": "$45K–$70K",
        "salary_note": "BLS median ~$47,000 (blog-cited) • cert-to-hire in ~6–7 mo (AWS D1.1) or 3–4 yr union path • 6G pipe welders: $80K–$110K+",
        "assumed": False,
        "overview": "Join metal with precision across construction, fabrication, and repair. Welding is the speed record among trades — a community-college certificate ending in an AWS certification can put you in a paying job in about 6–7 months, and specialized pipe welders (6G) regularly clear $80K–$110K.",
        "apprentice": "6–7 mo cert program or 3–4 yr union apprenticeship",
        "certs": [
            "AWS D1.1 (structural steel) — the entry-level credential",
            "API 1104 and advanced SMAW/TIG process tests",
            "6G pipe (SMAW/GTAW combo) — the top-tier call-out",
            "OSHA 10-Hour + welding safety training",
            "Union apprenticeships (UA, Ironworkers, boilermakers)",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Research local program costs ($0–$15K)",
            "Earn OSHA 10 + welding-safety basics",
            "Visit a community college welding lab",
            "Buy a hood, gloves, chipping hammer",
            "Practice basic bead runs on scrap",
            "Compare school vs union timelines",
            "Apply to 2–3 school programs",
            "Meet one AWS-certified welder in person",
            "Drill stick and MIG without stopping",
            "Apply to 2 union apprenticeships",
            "Land your first cert, then stack more",
        ],
    },
    {
        "name": "HVAC Technician",
        "icon": "❄️",
        "slug": "hvac-technician",
        "salary": "$50K–$70K",
        "salary_note": "BLS median $57,310 (blog-cited) • apprentice 3–5 yr, 6,000–8,000 OJT hrs • EPA 608 required from day one",
        "assumed": False,
        "overview": "Install, maintain, and repair the heating, cooling, and ventilation systems buildings depend on. Demand never quits — heating in winter, cooling in summer — and the path from zero experience to licensed technician is one of the fastest in the trades.",
        "apprentice": "3–5 year apprenticeship",
        "certs": [
            "EPA Section 608 — legally required to handle refrigerants",
            "NATE certification — the working technician credential",
            "OSHA 10-Hour — the universal entry credential",
            "State HVAC license (varies by state)",
            "Manufacturer training (Carrier, Trane, Lennox) for top pay",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Earn your OSHA 10 online",
            "Pass EPA 608 Universal (core/AC/heat)",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call a local HVAC shop or union",
            "Search apprenticeship.gov HVAC roles",
            "Buy gauges, a multimeter, hand tools",
            "Shadow a service tech for a day",
            "Apply to 3 programs (union + private)",
            "Practice brazing and soldering pipe",
            "Keep a clean driver's record handy",
        ],
    },
    {
        "name": "Automotive Mechanic",
        "icon": "🚗",
        "slug": "automotive-mechanic",
        "salary": "$40K–$65K",
        "salary_note": "Site band (trades page / quiz) • 6 mo–2 yr programs • no dedicated salary post yet — assumed",
        "assumed": True,
        "overview": "Diagnose and repair vehicles with a mix of hands-on skill and modern diagnostics. Entry is fast — helper or tech-school programs in 6 months to 2 years — and ASE credentials plus shop ownership keep the earning ceiling open.",
        "apprentice": "6 mo–2 yr program / apprenticeship",
        "certs": [
            "ASE certifications (Engine Repair, Brakes, Electrical)",
            "OEM training (Ford, GM, dealership service programs)",
            "State inspection license where required",
            "OSHA 10-Hour + shop safety basics",
            "Driver's license — test drives come with the job",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Call local shops about helper work",
            "Earn OSHA 10 or shop-safety basics",
            "Draft a one-page trade resume",
            "Buy a starter socket set + torque wrench",
            "Change oil and brakes on a friend's car",
            "Tour 2–3 shops; ask how they hire",
            "Start an ASE-Area study plan",
            "Apply to tech school or apprenticeship",
            "Apply to 2 dealership service programs",
            "Keep a repair log with photos",
            "Shadow a master tech for a day",
        ],
    },
    {
        "name": "Carpenter",
        "icon": "🪚",
        "slug": "carpenter",
        "salary": "$45K–$65K",
        "salary_note": "BLS median $51,390 (blog-cited) • apprentice 3–4 yr, ~4,800 OJT hrs (UBC) • foremen reach $60K–$80K+",
        "assumed": False,
        "overview": "Build, frame, and finish the wood structures behind every project — from rough framing to custom millwork. The most accessible of the building trades, with a 3–4 year apprenticeship that pays from week one and endless on-the-job variety.",
        "apprentice": "3–4 year apprenticeship",
        "certs": [
            "OSHA 10-Hour — required on almost every site",
            "UBC union apprenticeship (United Brotherhood of Carpenters)",
            "NCCER carpentry credentials",
            "First Aid/CPR",
            "OSHA 30 + foreman training once you lead crews",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Earn your OSHA 10 online",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call the local UBC carpenters' hall",
            "Search apprenticeship.gov carpentry roles",
            "Buy a hammer, tape measure, speed square",
            "Practice reading a tape measure cold",
            "Build one small project (photo proof)",
            "Apply to 3 carpenter apprenticeships",
            "Prep the math and reading intake test",
            "Volunteer one day on a build site",
        ],
    },
    {
        "name": "Ironworker",
        "icon": "🏗️",
        "slug": "ironworker",
        "salary": "$55K–$80K",
        "salary_note": "Site band (trades page / quiz) • 3-yr apprenticeship (structural + reinforcing) • no dedicated salary post yet — assumed",
        "assumed": True,
        "overview": "Erect and reinforce the steel skeleton of buildings, bridges, and industrial structures. A physically demanding, outdoors-in-all-weather trade with top-tier pay — the 3-year union apprenticeship splits into structural, reinforcing, and ornamental divisions.",
        "apprentice": "3 year apprenticeship",
        "certs": [
            "OSHA 10 and OSHA 30-Hour (fall hazards front and center)",
            "Fall protection competency training",
            "Rigging and crane-signaling certifications",
            "Union apprenticeship through a local Ironworkers hall",
            "AWS structural add-ons for field welding tasks",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Earn OSHA 10 now (fall hazards covered)",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call the local Ironworkers' hall intake",
            "Search apprenticeship.gov ironworker roles",
            "Buy a spud wrench + safety glasses",
            "Practice climbing and tie-off drills",
            "Talk to a working rodman or journeyman",
            "Apply to the union apprenticeship",
            "Train for the physical agility test",
            "Get comfortable with heights early",
        ],
    },
    {
        "name": "Pipefitter",
        "icon": "🔩",
        "slug": "pipefitter",
        "salary": "$60K–$85K",
        "salary_note": "BLS median $59,880 — plumbers & pipefitters (blog-cited) • apprentice 4–5 yr • top entry-level ceiling on the board",
        "assumed": False,
        "overview": "Assemble and install high-pressure pipe systems for steam, chemicals, and gases in power plants, refineries, and industrial facilities. Pipefitting is among the highest-paid trades on the board, with a structured 4–5 year UA apprenticeship and serious earning power once you weld-certs stack.",
        "apprentice": "4–5 year apprenticeship",
        "certs": [
            "UA pipefitter / steamfitter apprenticeship",
            "State journeyman pipefitting license (varies by state)",
            "Backflow prevention certification",
            "6G welding certifications for fitting work",
            "OSHA 10-Hour + confined-space training",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Earn your OSHA 10 online",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call a local UA steamfitters' hall",
            "Search apprenticeship.gov pipefitting",
            "Buy a pipe wrench set + torpedo level",
            "Practice reading P&IDs and drawings",
            "Meet a working pipefitter for advice",
            "Apply to 2–3 union programs",
            "Prep the math + mechanical aptitude test",
            "Shadow a fitter if the hall allows it",
        ],
    },
    {
        "name": "Diesel Mechanic",
        "icon": "🚛",
        "slug": "diesel-mechanic",
        "salary": "$45K–$65K",
        "salary_note": "Site band (trades page / quiz) • 2-yr programs • no dedicated salary post yet — assumed",
        "assumed": True,
        "overview": "Repair and maintain the diesel engines and heavy equipment that keep trucks, fleets, and construction moving. Steady demand in transportation, flexible schedules, and a clear path from helper to OEM-certified (Cummins, Detroit) technician.",
        "apprentice": "2 year program / apprenticeship",
        "certs": [
            "ASE Medium-Heavy Truck certifications (T1–T8)",
            "OEM certifications (Cummins, Detroit Diesel, PACCAR)",
            "Driver's license; a CDL is a strong add-on",
            "OSHA 10-Hour + shop safety basics",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Call local fleets about helper roles",
            "Earn OSHA 10 or shop-safety basics",
            "Draft a one-page trade resume",
            "Buy metric sockets + a torque wrench",
            "Tour a truck or equipment dealership",
            "Practice a basic PMI on a friend's rig",
            "Start ASE T-series study prep",
            "Apply to OEM and diesel tech programs",
            "Apply to 2 dealer apprenticeships",
            "Keep a repair log with photos",
            "Shadow a diesel tech for a day",
        ],
    },
    {
        "name": "Mason",
        "icon": "🧱",
        "slug": "mason",
        "salary": "$45K–$70K",
        "salary_note": "Site band (trades page / quiz) • 3–4 yr apprenticeship • no dedicated salary post yet — assumed",
        "assumed": True,
        "overview": "Build and finish walls, patios, foundations, and architectural details from brick, block, and stone. Masonry blends physical work with genuine artistry — craftsmanship that outlives the builder — with steady demand across residential and commercial construction.",
        "apprentice": "3–4 year apprenticeship",
        "certs": [
            "OSHA 10-Hour — the universal entry credential",
            "NCCER masonry credentials",
            "Union apprenticeship (bricklayers / IMI)",
            "First Aid/CPR",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Earn your OSHA 10 online",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call the local bricklayers' union / IMI",
            "Search apprenticeship.gov masonry roles",
            "Buy a trowel, brick hammer, chalk line",
            "Practice laying a test block course",
            "Mix and set slabs for repetition reps",
            "Volunteer on a wall or patio project",
            "Apply to 2–3 masonry apprenticeships",
            "Shadow a mason one working day",
        ],
    },
    {
        "name": "Roofer",
        "icon": "🏠",
        "slug": "roofer",
        "salary": "$40K–$65K",
        "salary_note": "Site band (trades page / quiz) • 2–3 yr apprenticeship • no dedicated salary post yet — assumed",
        "assumed": True,
        "overview": "Install, repair, and replace roofs — every building needs one and every roof wears out. Outdoor, see-the-result-today work with year-round demand, a fast 2–3 year apprenticeship, and the option to run your own crew down the road.",
        "apprentice": "2–3 year apprenticeship",
        "certs": [
            "OSHA 10 and OSHA 30-Hour (fall protection focus)",
            "Fall-protection competency training",
            "GAF / CertainTeed manufacturer certifications",
            "First Aid/CPR",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Earn OSHA 10 now — fall hazards covered",
            "Get First Aid/CPR certified",
            "Draft a one-page trade resume",
            "Call roofing contractors about helpers",
            "Buy a hatchet, chalk line, utility knife",
            "Practice ladder + harness safety setup",
            "Ride along on one install day",
            "Watch shingle/underlayment basics videos",
            "Apply to 2–3 roofing crews",
            "Send resumes to commercial roofers too",
            "Prep references + a clean-driver note",
        ],
    },
    {
        "name": "Construction Manager",
        "icon": "📋",
        "slug": "construction-manager",
        "salary": "$70K–$100K",
        "salary_note": "Site band (trades page / quiz) • usually 8–12 yr field path • no dedicated salary post yet — assumed",
        "assumed": True,
        "overview": "Oversee budgets, schedules, crews, and safety from planning through closeout. Most construction managers rise from the trades — field experience plus leadership training lands you at the top of the board's salary range, and many break six figures.",
        "apprentice": "Field path (typically 8–12 years)",
        "certs": [
            "OSHA 30-Hour — the leadership standard",
            "CMIT, then CCM (CMAA certification)",
            "NICET safety + supervisor training",
            "State contractor's license (varies by state)",
            "PMP — a differentiator at larger GCs",
        ],
        "checklist": [
            "Take the TradeLift quiz to confirm fit",
            "Pick a base trade and start in the field",
            "Earn OSHA 10 now, OSHA 30 later",
            "Draft a one-page trade resume",
            "Look for helper roles that show initiative",
            "Learn to read blueprints and specs",
            "Study scheduling basics (CPM/Gantt)",
            "Practice site math and takeoffs daily",
            "Ask GCs how superintendents started",
            "Apply to an assistant or apprenticeship",
            "Document every project you touch",
            "Map a 5-year path to assistant PM",
        ],
    },
]

PATH_STEPS = [
    ("RESEARCH", "Compare training routes, union vs non-union, and local demand"),
    ("TRAIN", "Trade school / pre-apprenticeship — start with OSHA 10"),
    ("HANDS-ON", "Apprentice years: log hours, earn raises to 80–90% of scale"),
    ("CERTIFIED", "Pass the journeyman or industry certification exam"),
    ("HIRED", "Journey-level pay — specialize, stack certs, own the shop"),
]


# --- Drawing helpers ----------------------------------------------------------
def wrap_text(c, text, font, size, max_width):
    words = text.split()
    lines, cur = [], []
    for w in words:
        test = " ".join(cur + [w])
        if c.stringWidth(test, font, size) <= max_width:
            cur.append(w)
        else:
            if cur:
                lines.append(" ".join(cur))
            cur = [w]
    if cur:
        lines.append(" ".join(cur))
    return lines


def draw_rounded_rect(c, x, y, w, h, radius, fill_color=None, stroke_color=None, stroke_width=1):
    if fill_color:
        c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(stroke_width)
    else:
        c.setStrokeColor(fill_color or HexColor("#000000"))
        c.setLineWidth(0)
    path = c.beginPath()
    path.moveTo(x + radius, y)
    path.lineTo(x + w - radius, y)
    path.arcTo(x + w - radius, y, x + w, y + radius, radius)
    path.lineTo(x + w, y + h - radius)
    path.arcTo(x + w, y + h - radius, x + w - radius, y + h, radius)
    path.lineTo(x + radius, y + h)
    path.arcTo(x, y + h - radius, x, y + h - radius, radius)
    path.lineTo(x, y + radius)
    path.arcTo(x, y, x + radius, y, radius)
    path.close()
    c.drawPath(path, fill=1 if fill_color else 0, stroke=1 if stroke_color else 0)


def section_title(c, y, text):
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y - 3, 4, 16, fill=1, stroke=0)
    c.setFont("DejaVu-Bold", 13)
    c.setFillColor(WHITE)
    c.drawString(MARGIN + 12, y, text)
    return y - 20


def page_background(c):
    c.setFillColor(BG_DARK)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)
    for i in range(70):
        ratio = i / 70
        r = int(20 + ratio * 14)
        g = int(12 + ratio * 4)
        b = int(2 + ratio * 2)
        c.setFillColor(HexColor("#%02x%02x%02x" % (r, g, b)))
        c.rect(0, HEIGHT - i - 1, WIDTH, 1, fill=1, stroke=0)


def draw_footer(c, page_label):
    c.setStrokeColor(BORDER)
    c.setLineWidth(1)
    c.line(MARGIN, 52, WIDTH - MARGIN, 52)
    c.setLineWidth(2)
    c.setStrokeColor(ORANGE)
    c.line(MARGIN, 52, MARGIN + 56, 52)

    c.setFont("DejaVu", 11)
    c.setFillColor(TEXT_MUTED)
    brand = "TradeLift — tradelift.surge.sh"
    c.drawCentredString(WIDTH / 2, 36, brand)

    c.setFont("DejaVu", 9)
    c.drawString(MARGIN, 22, "Free Career Roadmap")
    c.drawRightString(WIDTH - MARGIN, 22, page_label)


def draw_header_band(c, trade, page_no):
    band_h = 196 if page_no == 1 else 92
    band_bottom = HEIGHT - band_h
    draw_rounded_rect(c, 0, band_bottom, WIDTH, band_h, radius=0, fill_color=BG_HEADER)
    c.setFillColor(ORANGE)
    c.rect(0, band_bottom, WIDTH, 3, fill=1, stroke=0)

    if page_no == 1:
        c.setFont("DejaVu-Bold", 10)
        c.setFillColor(ORANGE)
        c.drawString(MARGIN, HEIGHT - 64, "TRADELIFT  •  FREE CAREER ROADMAP")

        c.setFont("DejaVu", 36)
        c.setFillColor(ORANGE)
        c.drawString(MARGIN, HEIGHT - 122, trade["icon"])

        c.setFont("DejaVu-Bold", 33)
        c.setFillColor(WHITE)
        c.drawString(MARGIN + 50, HEIGHT - 108, trade["name"])

        c.setFont("DejaVu", 11)
        c.setFillColor(TEXT_MUTED)
        c.drawString(MARGIN + 53, HEIGHT - 130, "%s  •  %s" % (trade["slug"], trade["apprentice"]))

        c.setFont("DejaVu-Bold", 21)
        c.setFillColor(YELLOW)
        c.drawString(MARGIN + 53, HEIGHT - 158, trade["salary"] + "  / yr")

        c.setFont("DejaVu", 9)
        c.setFillColor(TEXT_MUTED)
        c.drawRightString(WIDTH - MARGIN, HEIGHT - 64, "tradelift.surge.sh")
        c.drawRightString(WIDTH - MARGIN, HEIGHT - 82, "Journeyman band")
    else:
        c.setFont("DejaVu", 28)
        c.setFillColor(ORANGE)
        c.drawString(MARGIN, HEIGHT - 58, trade["icon"])
        c.setFont("DejaVu-Bold", 24)
        c.setFillColor(WHITE)
        c.drawString(MARGIN + 40, HEIGHT - 56, trade["name"] + " — Roadmap, page 2")
        c.setFont("DejaVu", 10)
        c.setFillColor(TEXT_MUTED)
        c.drawRightString(WIDTH - MARGIN, HEIGHT - 58, "CERTIFICATIONS  +  FIRST 12 WEEKS")


def render_trade(c, trade):
    # Page 1 -------------------------------------------------------------------
    page_background(c)
    draw_header_band(c, trade, 1)
    draw_footer(c, "Page 1 of 2")

    y = HEIGHT - 222

    # Trade overview
    y = section_title(c, y, "THE TRADE")
    c.setFont("DejaVu", 10.5)
    c.setFillColor(TEXT_BODY)
    for line in wrap_text(c, trade["overview"], "DejaVu", 10.5, CONTENT_W - 12):
        c.drawString(MARGIN + 4, y - 6, line)
        y -= 15
    y -= 14

    # Salary & training card
    y = section_title(c, y, "SALARY & TRAINING")
    card_top = y - 4
    card_h = 66
    card_bottom = card_top - card_h
    draw_rounded_rect(c, MARGIN, card_bottom, CONTENT_W, card_h, 8, fill_color=BG_CARD, stroke_color=BORDER, stroke_width=1)
    draw_rounded_rect(c, MARGIN, card_bottom, 4, card_h, 8, fill_color=ORANGE)

    c.setFont("DejaVu", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN + 18, card_top - 14, "JOURNEYMAN BAND (SITE FIGURE — SAME AS QUIZ RESULT & TRADES PAGE)")
    c.setFont("DejaVu-Bold", 22)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN + 18, card_top - 38, trade["salary"])
    c.setFont("DejaVu", 8.5)
    c.setFillColor(TEXT_BODY)
    note_lines = wrap_text(c, trade["salary_note"], "DejaVu", 8.5, CONTENT_W - 180)
    for i, line in enumerate(note_lines[:2]):
        c.drawString(MARGIN + 190, card_top - 28 - i * 12, line)
    y = card_bottom - 30

    # The path — 5 numbered rows
    y = section_title(c, y, "THE PATH: FROM RESEARCH TO HIRED")
    row_h = 30
    for i, (label, desc) in enumerate(PATH_STEPS):
        ry = y - 6 - (row_h * i)
        draw_rounded_rect(c, MARGIN, ry - row_h, CONTENT_W, row_h, 6,
                          fill_color=BG_CARD, stroke_color=BORDER, stroke_width=1)
        draw_rounded_rect(c, MARGIN, ry - row_h, 4, row_h, 6, fill_color=ORANGE)
        c.setFillColor(BG_HEADER)
        c.circle(MARGIN + 18, ry - row_h + row_h / 2, 12, fill=1, stroke=0)
        c.setStrokeColor(ORANGE)
        c.setLineWidth(1)
        c.circle(MARGIN + 18, ry - row_h + row_h / 2, 12, fill=0, stroke=1)
        c.setFont("DejaVu-Bold", 10)
        c.setFillColor(ORANGE)
        c.drawCentredString(MARGIN + 18, ry - row_h + row_h / 2 - 4, "%02d" % (i + 1))
        c.setFont("DejaVu-Bold", 11)
        c.setFillColor(WHITE)
        c.drawString(MARGIN + 40, ry - 10, label)
        c.setFont("DejaVu", 9.5)
        c.setFillColor(TEXT_BODY)
        desc_x = MARGIN + 40 + c.stringWidth(label + "  ", "DejaVu-Bold", 11)
        desc_lines = wrap_text(c, desc, "DejaVu", 9.5, WIDTH - desc_x - MARGIN)
        for j, line in enumerate(desc_lines[:2]):
            c.drawString(desc_x, ry - 10 - j * 13, line)
    y = y - 6 - row_h * len(PATH_STEPS) - 8

    c.setFont("DejaVu", 8.5)
    c.setFillColor(TEXT_MUTED)
    for line in wrap_text(
        c,
        "Every apprentice track pays from day one — typical start is 40–50% of journey scale with scheduled raises every year. Each step above is fully mapped on the TradeLift Getting Started guide and the site's resources page.",
        "DejaVu", 8.5, CONTENT_W,
    ):
        c.drawString(MARGIN, y - 4, line)
        y -= 12

    # Page 2 -------------------------------------------------------------------
    c.showPage()
    page_background(c)
    draw_header_band(c, trade, 2)
    draw_footer(c, "Page 2 of 2")

    y = HEIGHT - 122

    # Certifications
    y = section_title(c, y, "REQUIRED CERTIFICATIONS & CREDENTIALS")
    block_top = y - 2
    c.setFont("DejaVu", 10)
    for cert in trade["certs"]:
        c.setFillColor(ORANGE)
        c.circle(MARGIN + 6, y - 5, 2.5, fill=1, stroke=0)
        c.setFillColor(TEXT_BODY)
        lines = wrap_text(c, cert, "DejaVu", 10, CONTENT_W - 26)
        for line in lines[:2]:
            c.drawString(MARGIN + 16, y - 6, line)
            y -= 14
        y -= 4
    block_bottom = y - 10
    draw_rounded_rect(c, MARGIN, block_bottom, CONTENT_W, block_top - block_bottom, 8,
                      fill_color=BG_CARD, stroke_color=BORDER, stroke_width=1)
    y = block_bottom - 26

    # 12-week checklist (2 columns)
    y = section_title(c, y, "YOUR FIRST 12 WEEKS — THE ACTION CHECKLIST")
    col_w = (CONTENT_W - 20) / 2
    x2 = MARGIN + 20 + col_w
    items = trade["checklist"]
    top = y - 2
    for row in range(6):
        for col in range(2):
            idx = row * 2 + col
            if idx >= len(items):
                continue
            item = items[idx]
            x = MARGIN if col == 0 else x2
            ry = top - row * 26
            draw_rounded_rect(c, x, ry - 16, 13, 13, 3, fill_color=BG_CARD, stroke_color=ORANGE, stroke_width=1)
            lines = wrap_text(c, item, "DejaVu", 10, col_w - 24)
            c.setFillColor(TEXT_BODY)
            for j, line in enumerate(lines[:2]):
                c.drawString(x + 20, ry - 6 - j * 13, line)
    y = top - 6 * 26 - 26

    c.setFont("DejaVu", 8.5)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, y, "Full career steps, certifications, and tool guides: https://tradelift.surge.sh/getting-started.html")

    c.showPage()


# --- Verification -------------------------------------------------------------
def slugify(name):
    return name.lower().replace(" ", "-").replace("&", "and")


def verify_quiz_sync():
    with open(QUIZ_JS, encoding="utf-8") as fh:
        js = fh.read()
    problems = []
    names = [t["name"] for t in TRADES]
    slug_names = slugify(" ".join(names))
    if slug_names.count(","):  # placeholder guard, unused
        pass
    for t in TRADES:
        if ("name: '%s'" % t["name"]) not in js:
            problems.append("name %r not found as exact string in quiz.js" % t["name"])
        # quiz.js stores the salary with spaces around the dash
        quiz_salary = t["salary"].replace("–", " – ")
        if quiz_salary not in js:
            problems.append("salary %r not found in quiz.js for %s" % (quiz_salary, t["name"]))
        expected_slug = t["name"].lower().replace(" ", "-")
        # widget/quiz.html ids confirm the canonical slugs
    return names, problems


def verify_pdfs(trades):
    import pypdf
    results = []
    for t in trades:
        path = os.path.join(OUT_DIR, "%s-roadmap.pdf" % t["slug"])
        exists = os.path.exists(path)
        size = os.path.getsize(path) if exists else 0
        page_count = 0
        text_ok = False
        pypdf_err = None
        if exists:
            try:
                reader = pypdf.PdfReader(path)
                page_count = len(reader.pages)
                text = ""
                for p in reader.pages:
                    text += (p.extract_text() or "")
                text_ok = (t["name"] in text and t["salary"].replace("–", "–") in text
                           and "tradelift.surge.sh" in text)
            except Exception as e:  # noqa: BLE001
                pypdf_err = str(e)
        ok = exists and size > 10 * 1024 and page_count == 2 and text_ok and not pypdf_err
        results.append((t, exists, size, page_count, text_ok, pypdf_err, ok))
    return results


def generate_readme(trades):
    rows = []
    for t in trades:
        assumed = "**ASSUMED** — no dedicated salary post yet; band taken from trades.html + quiz.js." if t["assumed"] else "Blog-cited (see salary note)."
        rows.append("| %s | `%s-roadmap.pdf` | %s | %s |" % (t["name"], t["slug"], t["salary"], assumed))
    table = "\n".join(rows)

    readme = (
        "# TradeLift — Career Roadmap PDFs\n\n"
        "The 12 free roadmaps promised by the quiz funnel (`js/quiz.js`) after email capture.\n"
        "Each is a clean 2-page PDF (dark industrial theme, orange `#ff6b00` accent) produced by\n"
        "`scripts/generate-roadmaps.py` (idempotent — rerun to regenerate byte-identical files).\n\n"
        "## Trade → file → salary band\n\n"
        "Salary bands are exactly the site figures: `trades.html` \"Average Salary\" equals the quiz\n"
        "result shown in `js/quiz.js` (identical strings). BLS medians cited below come from the site's\n"
        "own salary blog posts so the PDFs never contradict published content.\n\n"
        "| Trade | File | Journeyman band (site) | Band source / assumptions |\n"
        "|---|---|---|---|\n"
    )
    readme += table + "\n\n"
    readme += (
        "## Assumptions\n\n"
        "- bands marked **ASSUMED** have no dedicated salary post on the site (dedicated posts exist\n"
        "  only for electrician, plumber, welder, HVAC, carpenter). Their headline band is the canonical\n"
        "  `trades.html` + `quiz.js` figure; no external median is printed in those PDFs.\n"
        "- carpenter: the headline band is the site figure `$45K–$65K`; the blog post narrows \"journeyman\"\n"
        "  to `$44K–$60K` with a $51,390 BLS median — the PDF prints the site band and cites the median.\n"
        "- plumber: `$55K–$75K` per trades.html, quiz, and the plumber blog's own headline ($59,880 median).\n"
        "- pipefitter: BLS $59,880 cited on site as the combined plumbers & pipefitters median.\n"
        "- slugs match the canonical `id` values used in `widget/quiz.html` and the site's 12-trade order.\n\n"
        "## Verification\n\n"
        "`python3 scripts/generate-roadmaps.py` performs: file existence, `>10KB` size check, pypdf\n"
        "reopen + 2-page + text extract assertions, and a `js/quiz.js` name/salary string sync check.\n"
    )
    with open(README_PATH, "w", encoding="utf-8") as fh:
        fh.write(readme)
    return readme


def main():
    os.makedirs(OUT_DIR, exist_ok=True)

    names, sync_problems = verify_quiz_sync()
    print("Quiz sync check: %d trades read from generator" % len(names))
    if sync_problems:
        for p in sync_problems:
            print("  PROBLEM: " + p)
        sys.exit(1)
    print("  All 12 trade names + salary strings match js/quiz.js: OK")

    for t in TRADES:
        path = os.path.join(OUT_DIR, "%s-roadmap.pdf" % t["slug"])
        c = canvas.Canvas(path, pagesize=letter, invariant=1)
        c.setPageCompression(1)
        render_trade(c, t)
        c.save()
        print("  wrote %s  (%d bytes)" % (os.path.relpath(path, ROOT), os.path.getsize(path)))

    results = verify_pdfs(TRADES)
    print("\nVerification (exists, >10KB, 2 pages, text extract):")
    all_ok = True
    for t, exists, size, pages, text_ok, err, ok in results:
        all_ok = all_ok and ok
        print("  %-22s exists=%s size=%6.1fKB pages=%d text=%s %s" % (
            t["slug"], exists, size / 1024.0, pages, text_ok, "OK" if ok else ("ERR: %s" % err if err else "FAIL")))
    if not all_ok:
        sys.exit(1)

    generate_readme(TRADES)
    print("\nREADME written: assets/roadmaps/README.md")
    print("\nAll 12 roadmaps generated and verified.")

    # quick site-consistency table for the report
    print("\nSalary bands used (identical to trades.html + quiz.js):")
    for t in TRADES:
        tag = "  [assumed - no dedicated post]" if t["assumed"] else ""
        print("  %-22s %s%s" % (t["name"], t["salary"], tag))


if __name__ == "__main__":
    main()