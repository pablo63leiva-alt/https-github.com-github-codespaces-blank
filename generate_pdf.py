#!/usr/bin/env python3
"""
Generate the "5 Trades Paying $60K+ with No Degree" PDF lead magnet
using ReportLab, matching the og-image style (dark industrial, orange/yellow accents).
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

OUTPUT_PATH = "assets/trade-lift-5-trades.pdf"

# Colors matching the site's dark industrial theme
BG_DARK = HexColor("#0a0a0a")
BG_CARD = HexColor("#1c1c1c")
BORDER = HexColor("#2a2a2a")
ORANGE = HexColor("#ff6b00")
YELLOW = HexColor("#ffc107")
WHITE = HexColor("#ffffff")
TEXT_BODY = HexColor("#b0b0b0")
TEXT_MUTED = HexColor("#8a8a8a")

# Trade data
TRADES = [
    {
        "name": "ELECTRICIAN",
        "icon": "⚡",
        "salary": "$60K–$80K",
        "training": "4-Year Apprenticeship",
        "desc": "Install, maintain, and repair electrical systems in homes, businesses, and industrial facilities. Essential to modern infrastructure with strong demand nationwide."
    },
    {
        "name": "PLUMBER",
        "icon": "🔧",
        "salary": "$55K–$75K",
        "training": "4–5 Year Apprenticeship",
        "desc": "Install and repair water supply lines, drainage systems, and fixtures. Critical role in public health and construction with year-round employment."
    },
    {
        "name": "PIPEFITTER",
        "icon": "🔩",
        "salary": "$60K–$85K",
        "training": "4–5 Year Apprenticeship",
        "desc": "Assemble, install, and repair high-pressure pipe systems in power plants and industrial settings. Specializes in steam, chemicals, and gases."
    },
    {
        "name": "IRONWORKER",
        "icon": "🏗️",
        "salary": "$55K–$80K",
        "training": "3-Year Apprenticeship",
        "desc": "Erect structural and reinforcing iron and steel for buildings, bridges, and large structures. High demand for major infrastructure projects."
    },
    {
        "name": "HVAC TECHNICIAN",
        "icon": "❄️",
        "salary": "$50K–$70K",
        "training": "2-Year Program",
        "desc": "Install, maintain, and repair heating, ventilation, and air conditioning systems. Steady year-round demand due to climate control needs."
    }
]

# Register DejaVu fonts
FONT_DIR = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DejaVu", FONT_DIR + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", FONT_DIR + "DejaVuSans-Bold.ttf"))

# Page size
WIDTH, HEIGHT = letter  # 612 x 792 points (8.5 x 11 inches)

def draw_rounded_rect(c, x, y, w, h, radius, fill_color=None, stroke_color=None, stroke_width=1):
    """Draw a rounded rectangle."""
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

def main():
    c = canvas.Canvas(OUTPUT_PATH, pagesize=letter)
    c.setPageCompression(1)

    # Full page background
    c.setFillColor(BG_DARK)
    c.rect(0, 0, WIDTH, HEIGHT, fill=1, stroke=0)

    # Top gradient accent (simulated with rectangles)
    for i in range(90):
        ratio = i / 90
        r = int(26 + ratio * 10)
        g = int(15 + ratio * 5)
        b = int(0 + ratio * 0)
        c.setFillColor(HexColor(f"#{r:02x}{g:02x}{b:02x}"))
        c.rect(0, HEIGHT - i - 1, WIDTH, 1, fill=1, stroke=0)

    # Side accent bars
    for i in range(int(HEIGHT)):
        ratio = i / HEIGHT
        alpha = 0.08 * (1 - abs(ratio - 0.5) * 2)
        if alpha > 0:
            r = int(255 * alpha)
            c.setFillColor(HexColor(f"#{r:02x}0000"))
            c.rect(0, i, 4, 1, fill=1, stroke=0)

    for i in range(int(HEIGHT)):
        ratio = i / HEIGHT
        alpha = 0.05 * (1 - abs(ratio - 0.5) * 2)
        if alpha > 0:
            r = int(255 * alpha)
            g = int(193 * alpha)
            c.setFillColor(HexColor(f"#{r:02x}{g:02x}00"))
            c.rect(WIDTH - 4, i, 4, 1, fill=1, stroke=0)

    # Title section
    title_y = HEIGHT - 80
    c.setFont("DejaVu-Bold", 48)
    c.setFillColor(WHITE)
    title_text = "5 TRADES PAYING $60K+"
    title_w = c.stringWidth(title_text, "DejaVu-Bold", 48)
    c.drawString((WIDTH - title_w) / 2, title_y, title_text)

    # Subtitle
    subtitle_y = title_y - 60
    c.setFont("DejaVu", 22)
    c.setFillColor(YELLOW)
    subtitle_text = "WITH NO DEGREE REQUIRED"
    subtitle_w = c.stringWidth(subtitle_text, "DejaVu", 22)
    c.drawString((WIDTH - subtitle_w) / 2, subtitle_y, subtitle_text)

    # Divider line
    line_y = subtitle_y - 35
    line_w = 150
    c.setStrokeColor(ORANGE)
    c.setLineWidth(3)
    c.line((WIDTH - line_w) / 2, line_y, (WIDTH + line_w) / 2, line_y)

    # Trade cards - 2 columns, 3 rows (last row has 1)
    card_start_y = line_y - 60
    card_width = 280
    card_height = 220
    card_gap_x = 30
    card_gap_y = 30
    left_margin = (WIDTH - (2 * card_width + card_gap_x)) / 2

    for i, trade in enumerate(TRADES):
        row = i // 2
        col = i % 2
        x = left_margin + col * (card_width + card_gap_x)
        y = card_start_y - row * (card_height + card_gap_y)

        # Card background
        draw_rounded_rect(c, x, y - card_height, card_width, card_height, 
                         radius=8, fill_color=BG_CARD, stroke_color=BORDER, stroke_width=2)

        # Left accent bar
        draw_rounded_rect(c, x, y - card_height, 4, card_height, 
                         radius=8, fill_color=ORANGE)

        # Icon
        c.setFont("DejaVu", 36)
        c.setFillColor(ORANGE)
        icon_x = x + 16
        icon_y = y - 40
        c.drawString(icon_x, icon_y, trade["icon"])

        # Trade name
        name_y = icon_y - 45
        c.setFont("DejaVu-Bold", 26)
        c.setFillColor(WHITE)
        c.drawString(icon_x, name_y, trade["name"])

        # Salary
        salary_y = name_y - 35
        c.setFont("DejaVu-Bold", 22)
        c.setFillColor(YELLOW)
        c.drawString(icon_x, salary_y, trade["salary"])

        # Training time
        training_y = salary_y - 30
        c.setFont("DejaVu", 16)
        c.setFillColor(TEXT_MUTED)
        c.drawString(icon_x, training_y, trade["training"])

        # Description (wrapped)
        desc_x = icon_x
        desc_y = training_y - 30
        max_width = card_width - 32
        
        c.setFont("DejaVu", 15)
        c.setFillColor(TEXT_BODY)
        
        # Simple word wrapping
        words = trade["desc"].split()
        lines = []
        current_line = []
        for word in words:
            test_line = " ".join(current_line + [word])
            if c.stringWidth(test_line, "DejaVu", 15) <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
        if current_line:
            lines.append(" ".join(current_line))

        for line in lines[:4]:  # Max 4 lines
            c.drawString(desc_x, desc_y, line)
            desc_y -= 22

    # Footer section
    footer_y = 160
    
    # CTA text
    c.setFont("DejaVu-Bold", 28)
    c.setFillColor(WHITE)
    cta_text = "Ready to Start Your Trade Career?"
    cta_w = c.stringWidth(cta_text, "DejaVu-Bold", 28)
    c.drawString((WIDTH - cta_w) / 2, footer_y, cta_text)

    cta_sub = "Visit https://pablo63leiva-alt.github.io/tradelift for apprenticeships, certifications, and step-by-step guides."
    c.setFont("DejaVu", 16)
    c.setFillColor(TEXT_MUTED)
    cta_sub_w = c.stringWidth(cta_sub, "DejaVu", 16)
    c.drawString((WIDTH - cta_sub_w) / 2, footer_y - 40, cta_sub)

    # Button-like element
    btn_y = footer_y - 80
    btn_text = "EXPLORE ALL TRADES →"
    c.setFont("DejaVu-Bold", 18)
    btn_w = c.stringWidth(btn_text, "DejaVu-Bold", 18) + 30
    btn_h = 40
    btn_x = (WIDTH - btn_w) / 2
    draw_rounded_rect(c, btn_x, btn_y, btn_w, btn_h, radius=20, fill_color=ORANGE)
    c.setFont("DejaVu-Bold", 18)
    c.setFillColor(WHITE)
    c.drawString(btn_x + 15, btn_y + 11, btn_text)

    # Copyright
    copyright_text = "© 2025 TradeLift. All rights reserved. | https://pablo63leiva-alt.github.io/tradelift"
    c.setFont("DejaVu", 12)
    c.setFillColor(TEXT_MUTED)
    copyright_w = c.stringWidth(copyright_text, "DejaVu", 12)
    c.drawString((WIDTH - copyright_w) / 2, 40, copyright_text)

    c.save()
    print(f"PDF generated: {OUTPUT_PATH}")
    print(f"Page size: {WIDTH}x{HEIGHT} points ({WIDTH/72:.1f}x{HEIGHT/72:.1f} inches)")

    # Verify
    import os
    size = os.path.getsize(OUTPUT_PATH)
    print(f"File size: {size} bytes ({size/1024:.1f} KB)")

if __name__ == "__main__":
    main()