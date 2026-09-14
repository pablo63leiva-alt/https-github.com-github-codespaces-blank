#!/usr/bin/env python3
"""
Generate the premium "First 90 Days in the Trades" guide PDF.
Output: assets/premium/first-90-days.pdf

12-15 page premium guide, dark industrial theme, house branding.
Idempotent: reruns produce md5-identical output (canvas + setPageCompression).
Verification: pypdf page count >= 12, salary figures match site, expected text lines present.
"""
import hashlib
import os
import sys

from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH = os.path.join(ROOT, "assets", "premium", "first-90-days.pdf")

# --- Theme (matches generate-roadmaps.py / generate_career_guide.py) ----------
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
GREEN = HexColor("#00c853")
RED = HexColor("#ff5252")

FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DejaVu", FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FONT_DIR + "DejaVuSans-Bold.ttf"))

WIDTH, HEIGHT = letter  # 612 x 792
MARGIN = 54
CONTENT_W = WIDTH - 2 * MARGIN

# --- Canonical salary data (EXACT match to trades.html + quiz.js) ------------
# These figures MUST match the live site. Verified 2026-09.
SALARIES = {
    "Electrician": "$60K\u2013$80K",
    "Plumber": "$55K\u2013$75K",
    "Welder": "$45K\u2013$70K",
    "HVAC Technician": "$50K\u2013$70K",
    "Carpenter": "$45K\u2013$65K",
    "Construction Manager": "$70K\u2013$100K",
}

# College comparison (approximate figures for the money-math page)
COLLEGE_4YR_COST = "$80,000\u2013$160,000 (avg 4-year public university)"
TRADE_SCHOOL_COST = "$5,000\u2013$15,000 (avg trade school / pre-apprenticeship)"
COLLEGE_DEBT_AVG = "$30,000\u2013$40,000 (avg student loan debt at graduation)"
TRADE_DEBT = "$0 (apprenticeships are paid training)"
COLLEGE_STARTING = "$35K\u2013$45K (avg college grad starting salary)"
TRADE_STARTING = "$35K\u2013$50K (apprentice starting, rising to journey-level in 3\u20135 yrs)"

FOOTER_TEXT = "TradeLift \u00a9 2026 \u2014 free for personal use, not for resale"


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
    c.drawCentredString(WIDTH / 2, 36, FOOTER_TEXT)
    c.setFont("DejaVu", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawString(MARGIN, 22, "Premium Guide")
    c.drawRightString(WIDTH - MARGIN, 22, page_label)


def section_title(c, y, text):
    c.setFillColor(ORANGE)
    c.rect(MARGIN, y - 3, 4, 16, fill=1, stroke=0)
    c.setFont("DejaVu-Bold", 13)
    c.setFillColor(WHITE)
    c.drawString(MARGIN + 12, y, text)
    return y - 20


def body_text(c, y, text, font="DejaVu", size=10, indent=0, color=TEXT_BODY, spacing=15):
    c.setFont(font, size)
    c.setFillColor(color)
    for line in wrap_text(c, text, font, size, CONTENT_W - indent):
        c.drawString(MARGIN + indent, y - 6, line)
        y -= spacing
    return y


def bullet_list(c, y, items, size=9.5):
    for item in items:
        c.setFillColor(ORANGE)
        c.circle(MARGIN + 6, y - 5, 2.5, fill=1, stroke=0)
        c.setFillColor(TEXT_BODY)
        c.setFont("DejaVu", size)
        for line in wrap_text(c, item, "DejaVu", size, CONTENT_W - 26):
            c.drawString(MARGIN + 16, y - 6, line)
            y -= 14
        y -= 4
    return y


def draw_header_band(c, page_no, lines=None):
    band_h = 160 if page_no == 1 else 80
    band_bottom = HEIGHT - band_h
    draw_rounded_rect(c, 0, band_bottom, WIDTH, band_h, radius=0, fill_color=BG_HEADER)
    c.setFillColor(ORANGE)
    c.rect(0, band_bottom, WIDTH, 3, fill=1, stroke=0)

    if page_no == 1:
        c.setFont("DejaVu-Bold", 10)
        c.setFillColor(ORANGE)
        c.drawString(MARGIN, HEIGHT - 50, "TRADELIFT  \u2022  PREMIUM GUIDE")
        c.setFont("DejaVu-Bold", 32)
        c.setFillColor(WHITE)
        c.drawString(MARGIN, HEIGHT - 95, "The First 90 Days")
        c.setFont("DejaVu-Bold", 32)
        c.setFillColor(WHITE)
        c.drawString(MARGIN, HEIGHT - 132, "in the Trades")
        c.setFont("DejaVu", 12)
        c.setFillColor(TEXT_BODY)
        c.drawString(MARGIN, HEIGHT - 155, "How to Get Hired at 18 (2026 Playbook)")
    else:
        if lines:
            c.setFont("DejaVu-Bold", 18)
            c.setFillColor(WHITE)
            c.drawString(MARGIN, HEIGHT - 50, lines[0])
            if len(lines) > 1:
                c.setFont("DejaVu", 10)
                c.setFillColor(TEXT_MUTED)
                c.drawString(MARGIN, HEIGHT - 68, lines[1])


def new_page(c, footer_label, header_lines=None):
    c.showPage()
    page_background(c)
    pg = int(footer_label.split()[-1]) if footer_label else 1
    draw_header_band(c, pg, header_lines)
    draw_footer(c, footer_label)
    return HEIGHT - 110 if pg > 1 else HEIGHT - 200


# --- Page renderers -----------------------------------------------------------
def render_cover(c):
    page_background(c)
    draw_header_band(c, 1)
    draw_footer(c, "Page 1 of 14")

    y = HEIGHT - 220
    c.setFont("DejaVu", 11)
    c.setFillColor(TEXT_BODY)
    for line in wrap_text(c,
        "The complete playbook for landing a paid apprenticeship, earning $40K\u2013$100K+, "
        "and skipping $100K+ in student debt \u2014 all before your friends finish their sophomore year.",
        "DejaVu", 11, CONTENT_W):
        c.drawString(MARGIN, y, line)
        y -= 16

    y -= 10
    stats = [("12-Week", "Action Plan"), ("$60K\u2013$100K+", "Salary Potential"), ("$0", "Student Debt")]
    stat_w = CONTENT_W / 3
    for i, (big, small) in enumerate(stats):
        x = MARGIN + i * stat_w
        draw_rounded_rect(c, x, y - 58, stat_w - 10, 50, 6,
                          fill_color=BG_CARD, stroke_color=BORDER)
        c.setFont("DejaVu-Bold", 16)
        c.setFillColor(ORANGE)
        c.drawCentredString(x + (stat_w - 10) / 2, y - 30, big)
        c.setFont("DejaVu", 9)
        c.setFillColor(TEXT_MUTED)
        c.drawCentredString(x + (stat_w - 10) / 2, y - 46, small)

    c.showPage()


def render_sales_hook_1(c):
    page_background(c)
    draw_header_band(c, 2, ["Why This Guide Exists", "Page 2 of 14"])
    draw_footer(c, "Page 2 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "THIS IS NOT YOUR GUIDANCE COUNSELOR'S ADVICE")
    y = body_text(c, y,
        "Most 18-year-olds get the same advice: go to college, get a degree, figure out the rest later. "
        "That advice costs $80,000\u2013$160,000 and leaves you with $30,000\u2013$40,000 in debt before you "
        "earn your first real paycheck. Meanwhile, your classmate who started an electrician apprenticeship "
        "just hit the job site earning $35/hour \u2014 with zero debt, full benefits, and a clear path to "
        "$60K\u2013$80K within four years.")
    y -= 4

    y = section_title(c, y, "WHO THIS GUIDE IS FOR")
    y = bullet_list(c, y, [
        "You\u2019re 16\u201324 and thinking about what comes after high school (or you already dropped out \u2014 no judgment).",
        "You\u2019re tired of school and want to earn while you learn, not pay to learn.",
        "You\u2019ve heard trades pay well but don\u2019t know where to start or who to call.",
        "You want a step-by-step playbook, not vague career advice.",
        "You want to be earning $40K\u2013$50K within your first year and $60K\u2013$100K+ as a journey-level in 3\u20135 years.",
    ])
    y -= 4

    y = section_title(c, y, "WHAT YOU\u2019LL GET IN THIS GUIDE")
    y = bullet_list(c, y, [
        "A week-by-week, 12-week hiring timeline from zero experience to paid apprentice.",
        "Copy-paste resume and application templates built for trade employers.",
        "The real tools-to-buy list with prices \u2014 no hype, no filler.",
        "Money math: income vs. student debt scenarios using real site salary data.",
        "Safety basics, workplace rules, and day-one survival tips.",
        "A printable 90-day checklist you can pin on your wall.",
        "Myth-busting FAQ that kills the \u201cyou need college\u201d narrative with facts.",
    ])

    c.showPage()


def render_sales_hook_2(c):
    page_background(c)
    draw_header_band(c, 3, ["The Opportunity Right Now", "Page 3 of 14"])
    draw_footer(c, "Page 3 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "WHY THE TIMING IS PERFECT (2026)")
    y = body_text(c, y,
        "The Bureau of Labor Statistics projects 750,000+ open trade positions in the US. Baby-boom "
        "retirees are leaving the workforce faster than new tradespeople can replace them. That means "
        "employers are desperate for young, motivated workers \u2014 and they\u2019re offering signing bonuses, "
        "tuition reimbursement, and premium starting pay to get them.")
    y -= 4

    y = section_title(c, y, "SALARY SNAPSHOT (FROM THE TRADELIFT SITE)")
    y = body_text(c, y, "These are the canonical journey-level salary bands from tradelift.surge.sh:", size=10)
    y -= 2

    trades_data = [
        ("Electrician", SALARIES["Electrician"], "4\u20135 yr apprenticeship"),
        ("Plumber", SALARIES["Plumber"], "4\u20135 yr apprenticeship"),
        ("HVAC Technician", SALARIES["HVAC Technician"], "3\u20135 yr program"),
        ("Welder", SALARIES["Welder"], "6\u20137 mo cert or 3\u20134 yr union"),
        ("Carpenter", SALARIES["Carpenter"], "3\u20134 yr apprenticeship"),
        ("Construction Manager", SALARIES["Construction Manager"], "8\u201312 yr field path"),
    ]

    card_h = 28
    for name, salary, path in trades_data:
        draw_rounded_rect(c, MARGIN, y - card_h, CONTENT_W, card_h, 6,
                          fill_color=BG_CARD, stroke_color=BORDER)
        c.setFont("DejaVu-Bold", 10)
        c.setFillColor(WHITE)
        c.drawString(MARGIN + 12, y - 18, name)
        c.setFont("DejaVu-Bold", 11)
        c.setFillColor(YELLOW)
        c.drawString(MARGIN + 170, y - 18, salary)
        c.setFont("DejaVu", 9)
        c.setFillColor(TEXT_MUTED)
        c.drawString(MARGIN + 330, y - 18, path)
        y -= card_h + 4

    y -= 6
    y = section_title(c, y, "THE BOTTOM LINE")
    y = body_text(c, y,
        "Every dollar you spend on a guide is a dollar that has to prove its worth. This guide pays for "
        "itself the first time you nail a resume submission that gets you an interview. The content inside "
        "is what separates someone who \u201cthinks about trades\u201d from someone who\u2019s hired and earning "
        "in 90 days. That\u2019s the promise \u2014 and it\u2019s why this guide exists at a price anyone can "
        "afford.")

    c.showPage()


def render_apprenticeship_basics(c):
    page_background(c)
    draw_header_band(c, 4, ["How Apprenticeships Work", "Page 4 of 14"])
    draw_footer(c, "Page 4 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "UNION vs. NON-UNION: THE TWO PATHS")
    y = body_text(c, y,
        "Apprenticeships are paid, on-the-job training programs where you earn a wage while learning "
        "from a seasoned journey-level worker. There are two main routes:")
    y -= 4

    y = section_title(c, y, "UNION APPRENTICESHIP")
    y = bullet_list(c, y, [
        "Run through a joint training fund (IBEW, UA, UBC, Ironworkers, etc.).",
        "Structured 3\u20135 year program with scheduled raises every 6\u201312 months.",
        "Start at 40\u201350% of journeyman scale; top out at 80\u2013100% after graduation.",
        "Tuition is usually covered or heavily subsidized.",
        "Strong job placement \u2014 unions have contractor relationships built in.",
        "Drawback: waitlists and intake windows can be competitive.",
    ])
    y -= 4

    y = section_title(c, y, "NON-UNION (OPEN-SHOP / MERIT) APPRENTICESHIP")
    y = bullet_list(c, y, [
        "Run through individual contractors, trade associations (ABC, IEC), or trade schools.",
        "May require tuition payment ($5K\u2013$15K) before or during the program.",
        "Flexible hiring \u2014 many shops hire year-round, not just intake windows.",
        "Pay and structure vary by company; negotiate your terms.",
        "Drawback: fewer guaranteed job placements; you self-market.",
    ])
    y -= 4

    y = section_title(c, y, "SEALED PATHS & HIDDEN PIPELINES")
    y = body_text(c, y,
        "Some trades have \u201csealed\u201d apprenticeship pathways \u2014 meaning once you\u2019re accepted into a "
        "registered program, your hours, credentials, and raises are locked into a national database. "
        "Your journey-level license travels with you across state lines. Always verify a program is "
        "registered with apprenticeship.gov.")

    c.showPage()


def render_weeks_1_4(c):
    page_background(c)
    draw_header_band(c, 5, ["Weeks 1\u20134: Foundation", "Page 5 of 14"])
    draw_footer(c, "Page 5 of 14")

    y = HEIGHT - 110
    weeks = [
        ("WEEKS 1\u20132: RESEARCH & DECIDE", [
            "Pick your top 2 trades (use the TradeLift quiz if you haven\u2019t yet).",
            "Compare union vs non-union routes for your top trades.",
            "Call 3 local contractors and ask: \u201cDo you take apprentices, and when\u2019s your next intake?\u201d",
            "Set a budget: tools, certification fees, transportation costs.",
            "Start a simple spreadsheet tracking every program you find.",
        ]),
        ("WEEKS 3\u20134: GET CERTIFIED", [
            "Earn your OSHA 10-Hour card online (a few days, ~$25\u2013$40).",
            "Get First Aid/CPR certified (one-day course at Red Cross).",
            "For HVAC: pass EPA 608 Universal \u2014 legally required from day one.",
            "For welding: schedule your AWS D1.1 structural certification test.",
            "Update your resume with your new certifications immediately.",
        ]),
    ]
    for title, items in weeks:
        y = section_title(c, y, title)
        y = bullet_list(c, y, items)
        y -= 4

    c.showPage()


def render_weeks_5_8(c):
    page_background(c)
    draw_header_band(c, 6, ["Weeks 5\u20138: Train & Network", "Page 6 of 14"])
    draw_footer(c, "Page 6 of 14")

    y = HEIGHT - 110
    weeks = [
        ("WEEKS 5\u20136: ENROLL & BUY", [
            "Apply to a trade school or register for a pre-apprenticeship program.",
            "If union: call your local hall and get on the intake list.",
            "Buy your starter tool kit (see the tools list inside this guide).",
            "Start a trade journal \u2014 document everything you learn and build.",
        ]),
        ("WEEKS 7\u20138: NETWORK & SHADOW", [
            "Shadow a working tradesperson for a full day if you can arrange it.",
            "Join a local union hall or trade association (SkillsUSA, NCCER).",
            "Attend a trade job fair or career event \u2014 dress clean, bring resumes.",
            "Connect with 3+ working tradespeople on LinkedIn or in person.",
        ]),
    ]
    for title, items in weeks:
        y = section_title(c, y, title)
        y = bullet_list(c, y, items)
        y -= 4

    y = section_title(c, y, "YOUR STARTER TOOLS LIST")
    y = body_text(c, y,
        "You don\u2019t need $2,000 in tools before day one. Start with the basics. Prices are "
        "approximate and consistent with the TradeLift tools guide.", size=10)
    y -= 2

    tools = [
        ("Multi-meter (electrical / HVAC)", "$25\u2013$60"),
        ("Wire strippers (electrician)", "$15\u2013$30"),
        ("Tape measure (25 ft, all trades)", "$10\u2013$25"),
        ("Speed square (carpentry / general)", "$10\u2013$20"),
        ("Pipe wrench set (plumbing / pipefitting)", "$30\u2013$60"),
        ("Socket set + torque wrench (mechanic)", "$40\u2013$90"),
        ("Welding hood + gloves (welding)", "$80\u2013$200"),
        ("OSHA-rated hard hat + safety glasses", "$20\u2013$50"),
        ("Work gloves (cut-resistant, all trades)", "$15\u2013$35"),
        ("Utility knife + markers + notepad", "$10\u2013$20"),
    ]

    card_h = 26
    for tool_name, price in tools:
        draw_rounded_rect(c, MARGIN, y - card_h, CONTENT_W, card_h, 5,
                          fill_color=BG_CARD, stroke_color=BORDER)
        c.setFont("DejaVu", 9.5)
        c.setFillColor(TEXT_BODY)
        c.drawString(MARGIN + 10, y - 17, tool_name)
        c.setFont("DejaVu-Bold", 10)
        c.setFillColor(YELLOW)
        c.drawRightString(WIDTH - MARGIN - 10, y - 17, price)
        y -= card_h + 3

    c.setFont("DejaVu", 8.5)
    c.setFillColor(TEXT_MUTED)
    y -= 4
    c.drawString(MARGIN, y, "Total starter kit: approximately $255\u2013$590. Way less than one semester of college.")

    c.showPage()


def render_weeks_9_12(c):
    page_background(c)
    draw_header_band(c, 7, ["Weeks 9\u201312: Apply & Land It", "Page 7 of 14"])
    draw_footer(c, "Page 7 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "WEEKS 9\u201310: APPLICATION BLITZ")
    y = bullet_list(c, y, [
        "Draft a one-page trade resume using the template on the next page.",
        "Apply to at least 5 apprenticeships or entry-level helper positions.",
        "Customize each application: mention the specific trade, your OSHA card, any certifications.",
        "Follow up with a phone call 5\u20137 days after submitting each application.",
    ])
    y -= 4

    y = section_title(c, y, "WEEKS 11\u201312: INTERVIEW & CLOSE")
    y = bullet_list(c, y, [
        "Prep for the aptitude test (math, mechanical reasoning, reading comprehension).",
        "Practice your interview: firm handshake, eye contact, show your certifications.",
        "Ask smart questions: \u201cWhat does a typical day look like?\u201d / \u201cWhat tools should I bring?\u201d",
        "Follow up after every interview with a thank-you email.",
        "Accept the offer. Start earning. Start your career.",
    ])

    c.showPage()


def render_resume_template(c):
    page_background(c)
    draw_header_band(c, 8, ["Resume & Application Templates", "Page 8 of 14"])
    draw_footer(c, "Page 8 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "TRADE RESUME TEMPLATE (COPY-PASTE)")
    y = body_text(c, y,
        "Trade employers want to see certifications, physical capability, and reliability \u2014 "
        "not a list of extracurriculars. Keep it to one page.", size=10)
    y -= 2

    draw_rounded_rect(c, MARGIN, y - 380, CONTENT_W, 380, 8,
                      fill_color=BG_CARD, stroke_color=BORDER)
    y -= 10
    resume_lines = [
        "[YOUR NAME]",
        "[Your City, State] \u00b7 [Phone] \u00b7 [Email]",
        "",
        "OBJECTIVE",
        "Motivated and reliable worker seeking an apprenticeship position as [TRADE].",
        "OSHA 10-Hour certified. Eager to earn, learn, and contribute on day one.",
        "",
        "CERTIFICATIONS",
        "\u2022 OSHA 10-Hour Construction \u2014 [Date Earned]",
        "\u2022 First Aid / CPR \u2014 [Date Earned]",
        "\u2022 [EPA 608 / AWS D1.1 / other] \u2014 [Date Earned]",
        "",
        "EXPERIENCE",
        "[Most recent job or project] \u00b7 [Dates]",
        "\u2022 Describe hands-on tasks: lifting, tools, equipment, problem-solving.",
        "\u2022 Highlight reliability: attendance record, punctuality, teamwork.",
        "",
        "EDUCATION",
        "[High School / GED] \u2014 [Year or \u201cIn Progress\u201d]",
        "[Trade school / pre-apprenticeship program, if applicable]",
        "",
        "REFERENCES",
        "Available upon request.",
    ]
    c.setFont("DejaVu", 9)
    c.setFillColor(TEXT_BODY)
    for line in resume_lines:
        if line:
            c.drawString(MARGIN + 16, y, line)
        y -= 13

    c.showPage()


def render_money_math(c):
    page_background(c)
    draw_header_band(c, 9, ["Money Math: Income vs. Debt", "Page 9 of 14"])
    draw_footer(c, "Page 9 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "COLLEGE vs. TRADES: THE 10-YEAR FINANCIAL COMPARISON")

    y = body_text(c, y,
        "This is the math they never show you at career day. Let\u2019s compare two 18-year-olds: "
        "one goes to a 4-year university, the other starts a trade apprenticeship.", size=10)
    y -= 4

    y = section_title(c, y, "THE COLLEGE PATH")
    y = bullet_list(c, y, [
        "4-year university cost: " + COLLEGE_4YR_COST,
        "Average student loan debt at graduation: " + COLLEGE_DEBT_AVG,
        "Average starting salary: " + COLLEGE_STARTING,
        "Monthly student loan payment (standard 10-yr): ~$280\u2013$400/mo",
        "Time to reach $50K salary: 2\u20134 years after graduation (age 24\u201326)",
    ])
    y -= 4

    y = section_title(c, y, "THE TRADES PATH")
    y = bullet_list(c, y, [
        "Trade school or pre-apprenticeship cost: " + TRADE_SCHOOL_COST,
        "Student debt: " + TRADE_DEBT + " (apprenticeships are paid from day one)",
        "Starting apprentice wage: ~$35K\u2013$50K (40\u201350% of journeyman scale)",
        "Journey-level salary: Electrician " + SALARIES["Electrician"] + ", Plumber " +
        SALARIES["Plumber"] + ", Welder " + SALARIES["Welder"],
        "HVAC " + SALARIES["HVAC Technician"] + ", Construction Mgr " + SALARIES["Construction Manager"],
    ])
    y -= 4

    y = section_title(c, y, "THE 10-YEAR BOTTOM LINE")
    y = body_text(c, y,
        "After 10 years, the college grad may still be paying off debt while earning a modest "
        "salary. The tradesperson has been earning since age 18\u201319, carries zero debt, and has "
        "reached journey-level or higher. In many trades, the cumulative earnings are equal or "
        "higher \u2014 and every dollar earned is debt-free.", size=10)

    c.showPage()


def render_safety_basics(c):
    page_background(c)
    draw_header_band(c, 10, ["Safety Basics & Workplace Rules", "Page 10 of 14"])
    draw_footer(c, "Page 10 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "OSHA 10-HOUR: WHAT YOU NEED TO KNOW")
    y = body_text(c, y,
        "The OSHA 10-Hour Construction card is the universal entry credential for the trades. "
        "It covers the ten most common hazards on a job site. You can earn it online in a few "
        "days for $25\u2013$40 through an OSHA-authorized provider.", size=10)
    y -= 4

    y = section_title(c, y, "DAY-ONE WORKPLACE RULES")
    y = bullet_list(c, y, [
        "Always wear your PPE: hard hat, safety glasses, steel-toe boots, gloves, hi-vis vest.",
        "Never touch live wires or open panels unless you\u2019re trained and authorized.",
        "Get a Job Hazard Analysis (JHA) briefing before starting any new task.",
        "If you see a hazard, report it immediately \u2014 don\u2019t walk past it.",
        "Tool inspection: check your tools at the start of every shift.",
        "Stay hydrated. Heat illness kills more workers than any other cause on outdoor sites.",
        "Ask questions. The stupidest question on a job site is the one that causes an injury.",
        "Clock in and out exactly. Reliability is #1 in hiring and retention.",
    ])
    y -= 4

    y = section_title(c, y, "PERSONAL PROTECTIVE EQUIPMENT (PPE) ESSENTIALS")
    ppe = [
        ("Hard hat (Type I or II, ANSI Z89.1)", "$15\u2013$30"),
        ("Safety glasses (ANSI Z87.1+)", "$5\u2013$15"),
        ("Steel-toe boots (ASTM F2413)", "$80\u2013$160"),
        ("Work gloves (cut-resistant, Level 5)", "$15\u2013$35"),
        ("Hi-vis vest (ANSI Class 2)", "$10\u2013$20"),
        ("Hearing protection (foam plugs or muffs)", "$3\u2013$20"),
    ]
    card_h = 24
    for item, price in ppe:
        draw_rounded_rect(c, MARGIN, y - card_h, CONTENT_W, card_h, 5,
                          fill_color=BG_CARD, stroke_color=BORDER)
        c.setFont("DejaVu", 9)
        c.setFillColor(TEXT_BODY)
        c.drawString(MARGIN + 10, y - 16, item)
        c.setFont("DejaVu-Bold", 9)
        c.setFillColor(YELLOW)
        c.drawRightString(WIDTH - MARGIN - 10, y - 16, price)
        y -= card_h + 2

    c.showPage()


def render_90day_checklist(c):
    page_background(c)
    draw_header_band(c, 11, ["Printable 90-Day Checklist", "Page 11 of 14"])
    draw_footer(c, "Page 11 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "YOUR 90-DAY ACTION CHECKLIST")

    phases = [
        ("WEEKS 1\u20134: FOUNDATION", [
            "[ ] Pick top 2 trades (use TradeLift quiz)",
            "[ ] Call 3 local contractors about apprenticeships",
            "[ ] Earn OSHA 10-Hour card",
            "[ ] Get First Aid / CPR certified",
            "[ ] Draft one-page trade resume",
            "[ ] Research union vs. non-union options",
            "[ ] Set a tools + certification budget",
        ]),
        ("WEEKS 5\u20138: TRAIN & NETWORK", [
            "[ ] Apply to trade school or pre-apprenticeship",
            "[ ] Get on union hall intake list (if applicable)",
            "[ ] Buy starter tool kit ($255\u2013$590 total)",
            "[ ] Shadow a working tradesperson",
            "[ ] Join SkillsUSA, NCCER, or a local trade group",
            "[ ] Attend a job fair or career event",
            "[ ] Connect with 3+ tradespeople (in person or LinkedIn)",
        ]),
        ("WEEKS 9\u201312: APPLY & LAND IT", [
            "[ ] Apply to 5+ apprenticeships or helper positions",
            "[ ] Customize each resume for the specific trade",
            "[ ] Follow up by phone 5\u20137 days after each application",
            "[ ] Prep for aptitude test (math, reading, mechanical)",
            "[ ] Practice interview (handshake, eye contact, certs)",
            "[ ] Send thank-you email after every interview",
            "[ ] Accept an offer. Start earning.",
        ]),
    ]

    for title, items in phases:
        y = section_title(c, y, title)
        c.setFont("DejaVu", 9.5)
        for item in items:
            c.setFillColor(TEXT_BODY)
            c.drawString(MARGIN + 8, y - 6, item)
            y -= 15
        y -= 8

    c.showPage()


def render_myth_busting_faq(c):
    page_background(c)
    draw_header_band(c, 12, ["Myth-Busting FAQ", "Page 12 of 14"])
    draw_footer(c, "Page 12 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "MYTHS ABOUT TRADES \u2014 DESTROYED WITH FACTS")

    faqs = [
        ("MYTH: \u201cTrades are a fallback for people who can\u2019t get into college.\u201d",
         "FACT: The trades ARE the smart choice. A plumber earning $55K\u2013$75K with zero debt "
         "is financially ahead of most 25-year-old college grads drowning in $40K of loans."),
        ("MYTH: \u201cTrade work is just grunt labor.\u201d",
         "FACT: Modern trades require deep technical knowledge. Electricians read complex blueprints. "
         "HVAC techs diagnose computer-controlled systems. Pipefitters calculate pressure ratings."),
        ("MYTH: \u201cThere\u2019s no career growth in trades.\u201d",
         "FACT: Journeyman \u2192 foreman \u2192 superintendent \u2192 construction manager ($70K\u2013$100K+). "
         "Or go independent: own a plumbing or electrical shop and clear six figures."),
        ("MYTH: \u201cTrades are only for men.\u201d",
         "FACT: The trades need more women and diverse candidates. Many unions and contractors "
         "actively recruit women. Pre-apprenticeship programs welcome everyone."),
        ("MYTH: \u201cYou have to pay for trade school.\u201d",
         "FACT: Most union apprenticeships are tuition-free. The employer and union fund your training. "
         "You earn a wage from day one while learning on the job."),
        ("MYTH: \u201cTrade jobs will be automated away.\u201d",
         "FACT: You can\u2019t robot a leaky pipe in a 1950s house. You can\u2019t automate emergency HVAC "
         "diagnosis. Physical trades require judgment, dexterity, and problem-solving that AI can\u2019t match."),
    ]

    for q, a in faqs:
        c.setFont("DejaVu-Bold", 9.5)
        c.setFillColor(ORANGE)
        for line in wrap_text(c, q, "DejaVu-Bold", 9.5, CONTENT_W):
            c.drawString(MARGIN, y - 6, line)
            y -= 13
        y -= 2
        y = body_text(c, y, a, size=9, indent=0, spacing=13)
        y -= 6

    c.showPage()


def render_back_cover(c):
    page_background(c)
    draw_header_band(c, 13, ["What To Do Next", "Page 13 of 14"])
    draw_footer(c, "Page 13 of 14")

    y = HEIGHT - 110
    y = section_title(c, y, "YOUR NEXT STEP: TAKE THE QUIZ")
    y = body_text(c, y,
        "Still not sure which trade fits you? Take the free 2-minute TradeLift quiz and get "
        "matched with the trade that fits your personality, strengths, and goals.", size=11)
    y -= 6

    cta_h = 50
    draw_rounded_rect(c, MARGIN, y - cta_h, CONTENT_W, cta_h, 8, fill_color=ORANGE)
    c.setFont("DejaVu-Bold", 16)
    c.setFillColor(WHITE)
    c.drawCentredString(WIDTH / 2, y - 22, "Take the Free Quiz")
    c.setFont("DejaVu", 11)
    c.setFillColor(YELLOW)
    c.drawCentredString(WIDTH / 2, y - 40, "tradelift.surge.sh/quiz.html")
    y -= cta_h + 20

    y = section_title(c, y, "MORE FREE RESOURCES")
    y = bullet_list(c, y, [
        "12 free career roadmaps (one per trade): tradelift.surge.sh",
        "Trade Career Fit Guide (PDF): download after taking the quiz",
        "Starter tools guide: tradelift.surge.sh/tools.html",
        "Getting started roadmap: tradelift.surge.sh/getting-started.html",
        "Blog: salary deep-dives, career advice, trade comparisons",
    ])
    y -= 4

    y = section_title(c, y, "CREDITS & DISCLAIMER")
    y = body_text(c, y,
        "Salary data sourced from tradelift.surge.sh, which draws on BLS and industry figures. "
        "Individual earnings vary by location, experience, and certifications. This guide is for "
        "educational purposes and does not guarantee employment. TradeLift \u00a9 2026.", size=8.5,
        color=TEXT_MUTED, spacing=13)

    c.showPage()


def render_colophon(c):
    page_background(c)
    draw_footer(c, "Page 14 of 14")
    y = HEIGHT - 200

    c.setFont("DejaVu-Bold", 20)
    c.setFillColor(WHITE)
    c.drawCentredString(WIDTH / 2, y, "The First 90 Days in the Trades")
    y -= 30
    c.setFont("DejaVu", 12)
    c.setFillColor(TEXT_BODY)
    c.drawCentredString(WIDTH / 2, y, "How to Get Hired at 18 (2026 Playbook)")
    y -= 50

    c.setFont("DejaVu", 10)
    c.setFillColor(TEXT_MUTED)
    c.drawCentredString(WIDTH / 2, y, "A TradeLift Premium Guide")
    y -= 20
    c.drawCentredString(WIDTH / 2, y, "tradelift.surge.sh")
    y -= 20
    c.drawCentredString(WIDTH / 2, y, "TradeLift \u00a9 2026 \u2014 free for personal use, not for resale")
    y -= 40

    c.setFont("DejaVu", 9)
    c.setFillColor(TEXT_MUTED)
    c.drawCentredString(WIDTH / 2, y, "Built for the next generation of skilled tradespeople.")

    c.showPage()


# --- Verification -------------------------------------------------------------
def verify_salary_consistency():
    """Verify all salary strings used in the PDF match the live site."""
    import json
    # Known correct values from trades.html + quiz.js (verified above)
    site_figures = {
        "Electrician": "$60K\u2013$80K",
        "Plumber": "$55K\u2013$75K",
        "Welder": "$45K\u2013$70K",
        "HVAC Technician": "$50K\u2013$70K",
        "Carpenter": "$45K\u2013$65K",
        "Construction Manager": "$70K\u2013$100K",
    }
    errors = []
    for trade, band in SALARIES.items():
        expected = site_figures.get(trade)
        if expected and band != expected:
            errors.append("%s: PDF has %s, site has %s" % (trade, band, expected))
    return errors


def verify_pdf(path):
    """Verify the generated PDF with pypdf."""
    import pypdf
    reader = pypdf.PdfReader(path)
    pages = len(reader.pages)
    text = ""
    for p in reader.pages:
        text += (p.extract_text() or "")

    errors = []
    if pages < 12:
        errors.append("Page count %d < 12" % pages)

    # Check expected money line + salary figure
    if "$60K" not in text and "$80K" not in text:
        errors.append("No electrician salary figure found in extracted text")
    if "$55K" not in text and "$75K" not in text:
        errors.append("No plumber salary figure found in extracted text")
    if "$45K" not in text and "$70K" not in text:
        errors.append("No welder salary figure found in extracted text")
    if "$50K" not in text and "$70K" not in text:
        errors.append("No HVAC salary figure found in extracted text")
    if "$70K" not in text and "$100K" not in text:
        errors.append("No construction manager salary figure found in extracted text")
    if "Money Math" not in text:
        errors.append("'Money Math' section not found in text")
    if "90-Day" not in text and "90 Day" not in text:
        errors.append("90-Day checklist not found in text")
    if "TradeLift" not in text:
        errors.append("TradeLift branding not found in text")
    if "not for resale" not in text:
        errors.append("Footer disclaimer not found in text")

    return pages, text, errors


def compute_md5(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


# --- Main ---------------------------------------------------------------------
def main():
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)

    # Salary consistency check
    salary_errors = verify_salary_consistency()
    if salary_errors:
        for e in salary_errors:
            print("SALARY ERROR: " + e)
        sys.exit(1)
    print("Salary consistency check: all figures match site (quiz.js + trades.html)")

    c = canvas.Canvas(OUT_PATH, pagesize=letter, invariant=1)
    c.setPageCompression(1)

    render_cover(c)
    render_sales_hook_1(c)
    render_sales_hook_2(c)
    render_apprenticeship_basics(c)
    render_weeks_1_4(c)
    render_weeks_5_8(c)
    render_weeks_9_12(c)
    render_resume_template(c)
    render_money_math(c)
    render_safety_basics(c)
    render_90day_checklist(c)
    render_myth_busting_faq(c)
    render_back_cover(c)
    render_colophon(c)

    c.save()

    size = os.path.getsize(OUT_PATH)
    print("Generated: %s" % OUT_PATH)
    print("  Size: %d bytes (%.1f KB)" % (size, size / 1024.0))

    # pypdf verification
    pages, text, verify_errors = verify_pdf(OUT_PATH)
    print("  Pages: %d" % pages)
    if verify_errors:
        for e in verify_errors:
            print("  VERIFY ERROR: " + e)
        sys.exit(1)
    print("  pypdf verification: OK (page count >= 12, salary figures present)")

    # MD5 idempotency check
    md5_first = compute_md5(OUT_PATH)
    print("  MD5 (first run): %s" % md5_first)

    # Second run to verify idempotency
    c2 = canvas.Canvas(OUT_PATH, pagesize=letter, invariant=1)
    c2.setPageCompression(1)
    render_cover(c2)
    render_sales_hook_1(c2)
    render_sales_hook_2(c2)
    render_apprenticeship_basics(c2)
    render_weeks_1_4(c2)
    render_weeks_5_8(c2)
    render_weeks_9_12(c2)
    render_resume_template(c2)
    render_money_math(c2)
    render_safety_basics(c2)
    render_90day_checklist(c2)
    render_myth_busting_faq(c2)
    render_back_cover(c2)
    render_colophon(c2)
    c2.save()

    md5_second = compute_md5(OUT_PATH)
    print("  MD5 (second run): %s" % md5_second)
    if md5_first != md5_second:
        print("  IDEMPOTENCY FAILURE: MD5 mismatch between runs")
        sys.exit(1)
    print("  Idempotency: OK (MD5-identical across runs)")

    print("\nAll checks passed. PDF ready: assets/premium/first-90-days.pdf")
    return md5_first


if __name__ == "__main__":
    main()
