#!/usr/bin/env python3
"""
Generate the "Trade Career Fit Guide" lead-magnet PDF.
Output: assets/careers.guide (extensionless for Surge.sh MIME workaround).

Structure: cover → intro ("How to Land a Trade Job in 90 Days") →
12 trade profile pages → resources page.
Dark industrial theme matching the site.
"""
import os
import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "assets", "careers.guide")

# Theme colors (match generate-roadmaps.py / site)
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

WIDTH, HEIGHT = letter
MARGIN = 54
CONTENT_W = WIDTH - 2 * MARGIN

# --- Trade data (salary bands MUST match the site exactly) --------------------
TRADES = [
    {
        "name": "Electrician",
        "icon": "\u26a1",
        "salary": "$60K\u2013$80K",
        "growth": "8% (Much faster than average)",
        "education": "4\u20135 year apprenticeship",
        "description": "Install, maintain, and repair electrical systems that power homes, businesses, and industrial facilities. Electricians build to the National Electrical Code (NEC), troubleshoot live systems, and remain in high demand nationwide.",
        "pros": ["Excellent job security — every building needs wiring", "Strong union presence with structured pay scales", "Specializations (solar, EV, industrial) boost pay well above median"],
        "cons": ["Physical risk — working with live electricity", "Apprenticeship is 4\u20135 years before full journeyman pay", "Licensing exams vary by state and can be rigorous"],
    },
    {
        "name": "Plumber",
        "icon": "\U0001f527",
        "salary": "$55K\u2013$75K",
        "growth": "5% (Faster than average)",
        "education": "4\u20135 year apprenticeship",
        "description": "Install and repair water supply, drainage, and gas systems that keep buildings safe and habitable. Plumbers work across residential, commercial, and industrial sites with year-round demand.",
        "pros": ["Recession-resistant — plumbing never goes out of style", "Clear path from journeyman to master license and your own shop", "Good work\u2013life balance with mostly regular hours"],
        "cons": ["Physically demanding — crawling, lifting, tight spaces", "Apprenticeship takes 4\u20135 years to complete", "Emergency calls can disrupt personal time"],
    },
    {
        "name": "Welder",
        "icon": "\U0001f525",
        "salary": "$45K\u2013$70K",
        "growth": "4% (As fast as average)",
        "education": "6\u20137 month certificate or 3\u20134 year union apprenticeship",
        "description": "Join metal with precision across construction, fabrication, and repair. Welding is the fastest entry into the trades — a certificate ending in AWS certification can put you in a paying job in about 6\u20137 months.",
        "pros": ["Fastest path from zero experience to paid work", "High ceiling — 6G pipe welders earn $80K\u2013$110K+", "Portable skill — work anywhere in the world"],
        "cons": ["Exposure to fumes, UV radiation, and heat", "Physical wear on eyes and lungs over time", "Certification stacking needed for top-tier pay"],
    },
    {
        "name": "HVAC Technician",
        "icon": "\u2744\ufe0f",
        "salary": "$50K\u2013$70K",
        "growth": "6% (Faster than average)",
        "education": "3\u20135 year apprenticeship or technical program",
        "description": "Install, maintain, and repair heating, cooling, and ventilation systems. Demand never quits — heating in winter, cooling in summer — making HVAC one of the most stable trades.",
        "pros": ["Year-round demand — seasonal peaks in both summer and winter", "Mix of electrical, mechanical, and diagnostic work", "EPA 608 certification is a universal credential"],
        "cons": ["Attics and rooftops in extreme temperatures", "Refrigerant handling requires strict EPA compliance", "On-call work for emergency breakdowns"],
    },
    {
        "name": "Carpenter",
        "icon": "\U0001fa9a",
        "salary": "$45K\u2013$65K",
        "growth": "2% (Slower than average)",
        "education": "3\u20134 year apprenticeship",
        "description": "Build, frame, and finish the wood structures behind every project — from rough framing to custom millwork. The most accessible building trade with endless on-the-job variety.",
        "pros": ["Creative, visible work you can point to proudly", "Foundational skill — leads to foreman and superintendent roles", "Wide variety: residential, commercial, restoration"],
        "cons": ["Lower starting pay compared to electrician/plumber", "Weather exposure on outdoor framing projects", "Physical toll — repetitive heavy lifting and cutting"],
    },
    {
        "name": "Mason",
        "icon": "\U0001f9f1",
        "salary": "$45K\u2013$70K",
        "growth": "3% (As fast as average)",
        "education": "3\u20134 year apprenticeship",
        "description": "Build and finish walls, patios, foundations, and architectural details from brick, block, and stone. Masonry blends physical work with genuine artistry — craftsmanship that outlives the builder.",
        "pros": ["Artistic skill — visible, lasting craftsmanship", "Steady demand in both residential and commercial sectors", "Strong union structure with predictable raises"],
        "cons": ["Physically grueling — heavy lifting in all weather", "Slower entry-level wage growth", "Knee and back strain are common occupational hazards"],
    },
    {
        "name": "Roofer",
        "icon": "\U0001f3e0",
        "salary": "$40K\u2013$65K",
        "growth": "2% (Slower than average)",
        "education": "2\u20133 year apprenticeship",
        "description": "Install, repair, and replace roofs — every building needs one and every roof wears out. Outdoor, see-the-result-today work with year-round demand and a fast apprenticeship.",
        "pros": ["Fast entry — shortest apprenticeship at 2\u20133 years", "Visible daily progress and job satisfaction", "Always in demand — every roof eventually needs replacement"],
        "cons": ["Working at heights in all weather conditions", "Lower starting wage compared to most trades", "Physical wear — heat, cold, and repetitive motion"],
    },
    {
        "name": "Pipefitter",
        "icon": "\U0001f529",
        "salary": "$60K\u2013$85K",
        "growth": "5% (Faster than average)",
        "education": "4\u20135 year apprenticeship",
        "description": "Assemble and install high-pressure pipe systems for steam, chemicals, and gases in power plants, refineries, and industrial facilities. Among the highest-paid trades with serious earning power.",
        "pros": ["Highest starting ceiling among the 12 trades", "Industrial settings pay premium overtime rates", "Stacking 6G weld certs can push pay past $100K"],
        "cons": ["Work is industrial — confined spaces and high pressure", "Long apprenticeship with demanding physical standards", "Travel required for shutdown/turnaround projects"],
    },
    {
        "name": "Ironworker",
        "icon": "\U0001f3d7\ufe0f",
        "salary": "$55K\u2013$80K",
        "growth": "5% (Faster than average)",
        "education": "3 year apprenticeship",
        "description": "Erect and reinforce the steel skeleton of buildings, bridges, and industrial structures. A physically demanding, outdoors-in-all-weather trade with top-tier pay.",
        "pros": ["Top-tier pay for an outdoor, physical trade", "Building iconic structures — bridges, skyscrapers", "Strong union with structured 3-year apprenticeship"],
        "cons": ["Heights are mandatory — not for everyone", "Weather exposure year-round", "High injury rate compared to other trades"],
    },
    {
        "name": "Diesel Mechanic",
        "icon": "\U0001f69b",
        "salary": "$45K\u2013$65K",
        "growth": "5% (As fast as average)",
        "education": "2 year program or apprenticeship",
        "description": "Repair and maintain the diesel engines and heavy equipment that keep trucks, fleets, and construction moving. Steady demand in transportation with flexible schedules.",
        "pros": ["Steady demand — trucks and fleets never stop", "Flexible schedules and overtime opportunities", "Clear path to OEM certifications (Cummins, Detroit)"],
        "cons": ["Dirty, physically demanding work environment", "Diagnostic complexity increasing with modern electronics", "CDL often needed for test-driving heavy vehicles"],
    },
    {
        "name": "Automotive Mechanic",
        "icon": "\U0001f697",
        "salary": "$40K\u2013$65K",
        "growth": "4% (As fast as average)",
        "education": "6 month\u20132 year program",
        "description": "Diagnose and repair vehicles with a mix of hands-on skill and modern diagnostics. Entry is fast — helper or tech-school programs — and ASE credentials keep the ceiling open.",
        "pros": ["Fast entry — programs as short as 6 months", "Every community needs mechanics — universal demand", "Path to shop ownership with ASE mastery"],
        "cons": ["Lower starting pay compared to construction trades", "Specialized tool investment can be expensive", "EV transition shifting required skill sets"],
    },
    {
        "name": "Construction Manager",
        "icon": "\U0001f4cb",
        "salary": "$70K\u2013$100K",
        "growth": "8% (Much faster than average)",
        "education": "8\u201312 year field path (start in a trade)",
        "description": "Oversee budgets, schedules, crews, and safety from planning through closeout. Most construction managers rise from the trades — field experience plus leadership training lands you at the top of the salary range.",
        "pros": ["Highest salary ceiling — many break six figures", "Leadership role with strategic, high-impact work", "Field experience makes you indispensable"],
        "cons": ["Requires 8\u201312 years of field experience first", "High stress — budgets, schedules, and safety accountability", "Office-to-field ratio means less hands-on work"],
    },
]

NINETY_DAY_STEPS = [
    ("WEEK 1\u20132: RESEARCH & DECIDE", [
        "Take the TradeLift quiz to narrow your top 2 trades",
        "Compare training routes: union vs non-union vs trade school",
        "Check local demand — call 3 contractors and ask about openings",
        "Set a budget: tools, certification fees, transportation",
    ]),
    ("WEEK 3\u20134: GET CERTIFIED", [
        "Earn your OSHA 10-Hour online (a few days, ~$25\u2013$40)",
        "Get First Aid/CPR certified (one-day course)",
        "For HVAC: pass EPA 608 Universal (required from day one)",
        "For welding: schedule your AWS D1.1 structural cert test",
    ]),
    ("WEEK 5\u20138: TRAIN & NETWORK", [
        "Enroll in a trade school or apply to an apprenticeship",
        "Buy your starter tool kit (see tradelift.surge.sh/tools.html)",
        "Shadow a working tradesperson for a day if possible",
        "Join a local union hall or trade association",
    ]),
    ("WEEK 9\u201312: APPLY & LAND IT", [
        "Draft a one-page trade resume with your new certs",
        "Apply to 5+ apprenticeships or entry-level positions",
        "Prep for aptitude tests (math, mechanical reasoning)",
        "Follow up on every application — persistence wins",
    ]),
]

RESOURCES = [
    ("Training & Apprenticeships", [
        ("apprenticeship.gov", "Federal apprenticeship finder — search by trade and zip code"),
        ("NCCER.org", "Industry-recognized credentials for 14+ construction trades"),
        ("SkillsUSA.org", "Career and technical education competitions and scholarships"),
    ]),
    ("Certifications", [
        ("OSHA.gov", "OSHA 10-Hour and 30-Hour online training (offered by many providers)"),
        ("EPA 608 Certification", "Required for HVAC — study and test through EPA-approved providers"),
        ("AWS (American Welding Society)", "D1.1 structural, 6G pipe, and advanced welding certifications"),
        ("ASE (National Institute for Automotive Service Excellence)", "A1\u2013A9 auto certs and T1\u2013T8 medium/heavy truck certs"),
    ]),
    ("Salary & Career Research", [
        ("Bureau of Labor Statistics (bls.gov/ooh)", "Official salary data, growth projections, and job outlook"),
        ("tradelift.surge.sh/blog.html", "TradeLift salary deep-dives for electrician, plumber, welder, HVAC"),
        ("tradelift.surge.sh/getting-started.html", "Step-by-step career roadmap with tools and interview tips"),
    ]),
    ("Communities & Support", [
        ("IBEW.org", "International Brotherhood of Electrical Workers — union finder"),
        ("UA.org", "United Association of Plumbers and Pipefitters"),
        ("Ironworkers.org", "International Association of Bridge, Structural, Ornamental, and Reinforcing Ironworkers"),
        ("UBC.org", "United Brotherhood of Carpenters and Joiners"),
    ]),
]


# --- Drawing helpers ---------------------------------------------------------
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
    c.drawCentredString(WIDTH / 2, 36, "TradeLift \u2014 tradelift.surge.sh")
    c.setFont("DejaVu", 9)
    c.drawString(MARGIN, 22, "Trade Career Fit Guide")
    c.drawRightString(WIDTH - MARGIN, 22, page_label)


def section_title(c, y, text):
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y - 3, 4, 16, fill=1, stroke=0)
    c.setFont("DejaVu-Bold", 13)
    c.setFillColor(WHITE)
    c.drawString(MARGIN + 12, y, text)
    return y - 20


# --- Page renderers ----------------------------------------------------------
def render_cover(c):
    page_background(c)

    # Dark header band
    draw_rounded_rect(c, 0, HEIGHT - 260, WIDTH, 260, radius=0, fill_color=BG_HEADER)
    c.setFillColor(ORANGE)
    c.rect(0, HEIGHT - 260, WIDTH, 3, fill=1, stroke=0)

    c.setFont("DejaVu-Bold", 10)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, HEIGHT - 60, "TRADELIFT  \u2022  FREE LEAD MAGNET")

    c.setFont("DejaVu-Bold", 38)
    c.setFillColor(WHITE)
    c.drawString(MARGIN, HEIGHT - 120, "Trade Career")
    c.setFont("DejaVu-Bold", 38)
    c.drawString(MARGIN, HEIGHT - 165, "Fit Guide")

    c.setFont("DejaVu", 14)
    c.setFillColor(TEXT_BODY)
    c.drawString(MARGIN, HEIGHT - 200, "12 Trades. One Perfect Fit for You.")

    c.setFont("DejaVu-Bold", 16)
    c.setFillColor(YELLOW)
    c.drawString(MARGIN, HEIGHT - 235, "Salary Ranges \u2022 Growth Outlook \u2022 90-Day Action Plan")

    # Tagline
    y = HEIGHT - 310
    c.setFont("DejaVu", 11)
    c.setFillColor(TEXT_BODY)
    for line in wrap_text(c,
        "Considering a skilled trade? This guide breaks down all 12 trades promoted by TradeLift \u2014 "
        "electrician, plumber, welder, HVAC, carpenter, mason, roofer, pipefitter, ironworker, "
        "diesel mechanic, automotive mechanic, and construction manager. You get honest pros and cons, "
        "real salary data, growth outlook, and a step-by-step plan to land your first trade job in 90 days.",
        "DejaVu", 11, CONTENT_W):
        c.drawString(MARGIN, y, line)
        y -= 16

    # Stats bar
    y -= 10
    stats = [("750K+", "Open Positions"), ("$50K\u2013$118K", "Salary Range"), ("0\u20135 yrs", "Time to Entry")]
    stat_w = CONTENT_W / 3
    for i, (big, small) in enumerate(stats):
        x = MARGIN + i * stat_w
        draw_rounded_rect(c, x, y - 58, stat_w - 10, 50, 6,
                          fill_color=BG_CARD, stroke_color=BORDER)
        c.setFont("DejaVu-Bold", 18)
        c.setFillColor(ORANGE)
        c.drawCentredString(x + (stat_w - 10) / 2, y - 30, big)
        c.setFont("DejaVu", 9)
        c.setFillColor(TEXT_MUTED)
        c.drawCentredString(x + (stat_w - 10) / 2, y - 46, small)

    # Footer
    c.setFont("DejaVu", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawCentredString(WIDTH / 2, 36, "tradelift.surge.sh")

    c.showPage()


def render_ninety_day_plan(c):
    page_background(c)
    draw_footer(c, "90-Day Plan")

    y = HEIGHT - 60
    y = section_title(c, y, "HOW TO LAND A TRADE JOB IN 90 DAYS")

    c.setFont("DejaVu", 10)
    c.setFillColor(TEXT_BODY)
    for line in wrap_text(c,
        "You don\u2019t need a four-year degree to start a high-paying trade career. Follow this 12-week "
        "action plan and you could be on the job site with paid training in three months.",
        "DejaVu", 10, CONTENT_W):
        c.drawString(MARGIN, y - 6, line)
        y -= 15
    y -= 14

    for phase_title, steps in NINETY_DAY_STEPS:
        y = section_title(c, y, phase_title)
        for step in steps:
            c.setFillColor(ORANGE)
            c.circle(MARGIN + 6, y - 5, 2.5, fill=1, stroke=0)
            c.setFillColor(TEXT_BODY)
            c.setFont("DejaVu", 9.5)
            for line in wrap_text(c, step, "DejaVu", 9.5, CONTENT_W - 26):
                c.drawString(MARGIN + 16, y - 6, line)
                y -= 14
            y -= 4

        draw_rounded_rect(c, MARGIN, y - 2, CONTENT_W, 1, 0, fill_color=BORDER)
        y -= 14

    c.setFont("DejaVu-Bold", 10)
    c.setFillColor(YELLOW)
    c.drawCentredString(WIDTH / 2, y, "Every step is mapped at tradelift.surge.sh/getting-started.html")

    c.showPage()


def render_trade_page(c, trade, page_no):
    page_background(c)
    draw_footer(c, "Trade Profile %d of 12" % page_no)

    y = HEIGHT - 50

    # Trade header
    c.setFont("DejaVu", 28)
    c.setFillColor(ORANGE)
    c.drawString(MARGIN, y - 30, trade["icon"])
    c.setFont("DejaVu-Bold", 26)
    c.setFillColor(WHITE)
    c.drawString(MARGIN + 44, y - 28, trade["name"])

    # Salary badge
    badge_y = y - 58
    draw_rounded_rect(c, MARGIN, badge_y, 200, 36, 6,
                      fill_color=BG_CARD, stroke_color=ORANGE, stroke_width=1.5)
    c.setFont("DejaVu-Bold", 16)
    c.setFillColor(YELLOW)
    c.drawString(MARGIN + 12, badge_y + 10, trade["salary"] + " /yr")

    # Growth badge
    draw_rounded_rect(c, MARGIN + 210, badge_y, CONTENT_W - 210, 36, 6,
                      fill_color=BG_CARD, stroke_color=BORDER)
    c.setFont("DejaVu", 10)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN + 222, badge_y + 14, "Growth: " + trade["growth"])

    y = badge_y - 20

    # Education
    c.setFont("DejaVu", 10)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, y, "Education Path:  " + trade["education"])
    y -= 24

    # Divider
    draw_rounded_rect(c, MARGIN, y, CONTENT_W, 1, 0, fill_color=BORDER)
    y -= 16

    # Description
    y = section_title(c, y, "WHAT THEY DO")
    c.setFont("DejaVu", 10)
    c.setFillColor(TEXT_BODY)
    for line in wrap_text(c, trade["description"], "DejaVu", 10, CONTENT_W - 12):
        c.drawString(MARGIN + 4, y - 6, line)
        y -= 15
    y -= 16

    # Pros
    y = section_title(c, y, "PROS")
    draw_rounded_rect(c, MARGIN, y - len(trade["pros"]) * 28 - 4, CONTENT_W,
                      len(trade["pros"]) * 28 + 12, 8,
                      fill_color=BG_CARD, stroke_color=BORDER)
    for pro in trade["pros"]:
        c.setFillColor(HexColor("#00c853"))
        c.setFont("DejaVu-Bold", 12)
        c.drawString(MARGIN + 10, y - 6, "+")
        c.setFillColor(TEXT_BODY)
        c.setFont("DejaVu", 9.5)
        for line in wrap_text(c, pro, "DejaVu", 9.5, CONTENT_W - 30):
            c.drawString(MARGIN + 26, y - 6, line)
            y -= 14
        y -= 14
    y -= 16

    # Cons
    y = section_title(c, y, "CONS")
    draw_rounded_rect(c, MARGIN, y - len(trade["cons"]) * 28 - 4, CONTENT_W,
                      len(trade["cons"]) * 28 + 12, 8,
                      fill_color=BG_CARD, stroke_color=BORDER)
    for con in trade["cons"]:
        c.setFillColor(HexColor("#ff5252"))
        c.setFont("DejaVu-Bold", 12)
        c.drawString(MARGIN + 10, y - 6, "\u2013")
        c.setFillColor(TEXT_BODY)
        c.setFont("DejaVu", 9.5)
        for line in wrap_text(c, con, "DejaVu", 9.5, CONTENT_W - 30):
            c.drawString(MARGIN + 26, y - 6, line)
            y -= 14
        y -= 14
    y -= 16

    # CTA
    cta_h = 44
    draw_rounded_rect(c, MARGIN, y - cta_h, CONTENT_W, cta_h, 8,
                      fill_color=ORANGE)
    c.setFont("DejaVu-Bold", 14)
    c.setFillColor(WHITE)
    c.drawCentredString(WIDTH / 2, y - 28, "Ready to start?  tradelift.surge.sh/quiz.html")

    c.showPage()


def render_resources(c):
    page_background(c)
    draw_footer(c, "Resources")

    y = HEIGHT - 60
    y = section_title(c, y, "RESOURCES & NEXT STEPS")

    c.setFont("DejaVu", 10)
    c.setFillColor(TEXT_BODY)
    for line in wrap_text(c,
        "Bookmark these links — they\u2019ll be your go-to references as you research, train, and land your trade career.",
        "DejaVu", 10, CONTENT_W):
        c.drawString(MARGIN, y - 6, line)
        y -= 15
    y -= 14

    for category, links in RESOURCES:
        y = section_title(c, y, category.upper())
        for url, desc in links:
            c.setFont("DejaVu-Bold", 10)
            c.setFillColor(ORANGE)
            c.drawString(MARGIN + 8, y - 6, url)
            y -= 14
            c.setFont("DejaVu", 9)
            c.setFillColor(TEXT_BODY)
            for line in wrap_text(c, desc, "DejaVu", 9, CONTENT_W - 20):
                c.drawString(MARGIN + 12, y - 4, line)
                y -= 12
            y -= 6
        y -= 8

    # Final CTA
    y -= 6
    cta_h = 56
    draw_rounded_rect(c, MARGIN, y - cta_h, CONTENT_W, cta_h, 8,
                      fill_color=ORANGE)
    c.setFont("DejaVu-Bold", 16)
    c.setFillColor(WHITE)
    c.drawCentredString(WIDTH / 2, y - 22, "Find Your Perfect Trade")
    c.setFont("DejaVu", 11)
    c.setFillColor(YELLOW)
    c.drawCentredString(WIDTH / 2, y - 42, "tradelift.surge.sh/quiz.html")

    c.showPage()


# --- Main --------------------------------------------------------------------
def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

    c = canvas.Canvas(OUT_PATH, pagesize=letter, invariant=1)
    c.setPageCompression(1)

    render_cover(c)
    render_ninety_day_plan(c)
    for i, trade in enumerate(TRADES, 1):
        render_trade_page(c, trade, i)
    render_resources(c)

    c.save()
    size = os.path.getsize(OUT_PATH)

    # Verify
    import pypdf
    reader = pypdf.PdfReader(OUT_PATH)
    pages = len(reader.pages)
    print("Generated: %s" % OUT_PATH)
    print("  Size: %d bytes (%.1f KB)" % (size, size / 1024.0))
    print("  Pages: %d" % pages)
    print("  Trades: %d" % len(TRADES))

    if size < 15 * 1024:
        print("  WARNING: File is under 15KB")
        sys.exit(1)
    if pages < 2:
        print("  WARNING: File has fewer than 2 pages")
        sys.exit(1)

    # Verify salary bands match site expectations
    expected = {
        "Electrician": "$60K\u2013$80K",
        "Plumber": "$55K\u2013$75K",
        "Welder": "$45K\u2013$70K",
        "HVAC Technician": "$50K\u2013$70K",
        "Carpenter": "$45K\u2013$65K",
        "Mason": "$45K\u2013$70K",
        "Roofer": "$40K\u2013$65K",
        "Pipefitter": "$60K\u2013$85K",
        "Ironworker": "$55K\u2013$80K",
        "Diesel Mechanic": "$45K\u2013$65K",
        "Automotive Mechanic": "$40K\u2013$65K",
        "Construction Manager": "$70K\u2013$100K",
    }
    for t in TRADES:
        exp = expected.get(t["name"])
        if exp and t["salary"] != exp:
            print("  SALARY MISMATCH: %s has %s, expected %s" % (t["name"], t["salary"], exp))
            sys.exit(1)
    print("  Salary bands verified: OK")

    print("\nDone. All checks passed.")


if __name__ == "__main__":
    main()
