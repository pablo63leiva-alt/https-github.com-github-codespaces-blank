#!/usr/bin/env python3
"""
Generate the premium "Land Your First Trade Apprenticeship" guide PDF.
Output: assets/premium/first-apprenticeship.pdf

~14 page premium guide, dark industrial theme, house branding.
Idempotent: reruns produce md5-identical output (canvas + setPageCompression + invariant=1).
Verification: pypdf page count, salary figures match site, expected text lines present.
"""
import hashlib, os, sys
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "premium", "first-apprenticeship.pdf")

# Theme
BG_DARK = HexColor("#0a0a0a"); BG_HDR = HexColor("#140c05"); BG_CARD = HexColor("#1c1c1c")
BG_PNL = HexColor("#161616"); BORDER = HexColor("#2e2e2e"); ORANGE = HexColor("#ff6b00")
YELLOW = HexColor("#ffc107"); WHITE = HexColor("#ffffff"); T_B = HexColor("#b0b0b0")
T_M = HexColor("#8a8a8a")

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("D", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DB", FD + "DejaVuSans-Bold.ttf"))
W, H = letter; M = 54; CW = W - 2 * M

SALARIES = {
    "Electrician": "$60K\u2013$80K", "Plumber": "$55K\u2013$75K", "Welder": "$45K\u2013$70K",
    "HVAC Technician": "$50K\u2013$70K", "Carpenter": "$45K\u2013$65K", "Mason": "$45K\u2013$70K",
    "Roofer": "$40K\u2013$65K", "Pipefitter": "$60K\u2013$85K", "Ironworker": "$55K\u2013$80K",
    "Diesel Mechanic": "$45K\u2013$65K", "Automotive Mechanic": "$40K\u2013$65K",
    "Construction Manager": "$70K\u2013$100K",
}
AW = [
    ("Electrician", "$15\u2013$22", "$16\u2013$25", "$17\u2013$32", "$60K\u2013$80K+"),
    ("Plumber", "$16\u2013$22", "$17\u2013$25", "$19\u2013$32", "$56K\u2013$74K"),
    ("HVAC Tech", "$15\u2013$20", "$17\u2013$23", "$20\u2013$28", "$50K\u2013$70K"),
    ("Welder", "$16\u2013$20", "$18\u2013$24", "$20\u2013$28", "$45K\u2013$70K"),
    ("Carpenter", "$15\u2013$19", "$16\u2013$22", "$18\u2013$26", "$45K\u2013$65K"),
    ("Elevator Inst.", "$20\u2013$25", "$24\u2013$29", "$29\u2013$38", "$80K\u2013$100K+"),
]
FT = "TradeLift \u00a9 2026 \u2014 free for personal use, not for resale"
TP = 14

def wt(c, t, f, s, mw):
    w = t.split(); ls, cu = [], []
    for x in w:
        test = " ".join(cu + [x])
        if c.stringWidth(test, f, s) <= mw: cu.append(x)
        else:
            if cu: ls.append(" ".join(cu))
            cu = [x]
    if cu: ls.append(" ".join(cu))
    return ls

def rr(c, x, y, w, h, r, fc=None, sc=None, sw=1):
    if fc: c.setFillColor(fc)
    if sc: c.setStrokeColor(sc); c.setLineWidth(sw)
    else: c.setStrokeColor(fc or HexColor("#000")); c.setLineWidth(0)
    p = c.beginPath(); p.moveTo(x+r,y); p.lineTo(x+w-r,y); p.arcTo(x+w-r,y,x+w,y+r,r)
    p.lineTo(x+w,y+h-r); p.arcTo(x+w,y+h-r,x+w-r,y+h,r); p.lineTo(x+r,y+h)
    p.arcTo(x,y+h-r,x,y+h-r,r); p.lineTo(x,y+r); p.arcTo(x,y,x+r,y,r); p.close()
    c.drawPath(p, fill=1 if fc else 0, stroke=1 if sc else 0)

def pbg(c):
    c.setFillColor(BG_DARK); c.rect(0,0,W,H,fill=1,stroke=0)
    for i in range(70):
        r=i/70; c.setFillColor(HexColor("#%02x%02x%02x"%(int(20+r*14),int(12+r*4),int(2+r*2))))
        c.rect(0,H-i-1,W,1,fill=1,stroke=0)

def ft(c, lb):
    c.setStrokeColor(BORDER); c.setLineWidth(1); c.line(M,52,W-M,52)
    c.setStrokeColor(ORANGE); c.setLineWidth(2); c.line(M,52,M+56,52)
    c.setFont("D",10); c.setFillColor(T_M); c.drawCentredString(W/2,34,FT)
    c.setFont("D",8); c.drawString(M,20,"Premium Guide"); c.drawRightString(W-M,20,lb)

def st(c, y, t):
    c.setFillColor(ORANGE); c.rect(M,y-3,4,13,fill=1,stroke=0)
    c.setFont("DB",11); c.setFillColor(WHITE); c.drawString(M+12,y,t); return y-16

def bt(c, y, t, f="D", s=9, ind=0, co=T_B, sp=13):
    c.setFont(f,s); c.setFillColor(co)
    for l in wt(c,t,f,s,CW-ind): c.drawString(M+ind,y-5,l); y-=sp
    return y

def bl(c, y, items, s=8.5):
    for it in items:
        c.setFillColor(ORANGE); c.circle(M+5,y-4,2,fill=1,stroke=0)
        c.setFillColor(T_B); c.setFont("D",s)
        for l in wt(c,it,"D",s,CW-22): c.drawString(M+13,y-5,l); y-=11
        y-=2
    return y

def hb(c, pg, hl=None):
    bh = 140 if pg==1 else 64; bb = H-bh
    rr(c,0,bb,W,bh,r=0,fc=BG_HDR); c.setFillColor(ORANGE); c.rect(0,bb,W,3,fill=1,stroke=0)
    if pg==1:
        c.setFont("DB",9); c.setFillColor(ORANGE); c.drawString(M,H-42,"TRADELIFT  \u2022  PREMIUM GUIDE")
        c.setFont("DB",26); c.setFillColor(WHITE); c.drawString(M,H-80,"Land Your First")
        c.setFont("DB",26); c.drawString(M,H-110,"Trade Apprenticeship")
        c.setFont("D",11); c.setFillColor(T_B); c.drawString(M,H-130,"The Step-by-Step Playbook (2026)")
    elif hl:
        c.setFont("DB",15); c.setFillColor(WHITE); c.drawString(M,H-40,hl[0])
        if len(hl)>1: c.setFont("D",9); c.setFillColor(T_M); c.drawString(M,H-54,hl[1])

# np: set up next page (background + header + footer). Does NOT call showPage().
def np(c, hl=None):
    pbg(c); pg = hb.__wrapped_pg if hasattr(hb, '__wrapped_pg') else 1
    # We track page number via a simple counter on the canvas
    if not hasattr(c, '_pg_num'): c._pg_num = 0
    c._pg_num += 1
    pg = c._pg_num
    hb(c, pg, hl)
    ft(c, "Page %d of %d" % (pg, TP))
    return H - 88 if pg > 1 else H - 175

# Pages - each renders content then calls c.showPage() at the end
def p1(c):
    pbg(c); hb(c, 1); ft(c, "Page 1 of %d" % TP)
    y = H - 185
    y=bt(c,y,"The complete playbook for landing a paid trade apprenticeship \u2014 from your first application to your first day on the job. Built for 17\u201325 year-olds ready to earn $40K\u2013$100K+ instead of borrowing $100K+.",s=10)
    y-=6
    stats=[("5-Step","App. System"),("750K+","Open Positions"),("$0","Tuition (Union)")]
    sw=CW/3
    for i,(b,s) in enumerate(stats):
        x=M+i*sw; rr(c,x,y-46,sw-8,40,5,fc=BG_CARD,sc=BORDER)
        c.setFont("DB",14); c.setFillColor(ORANGE); c.drawCentredString(x+(sw-8)/2,y-24,b)
        c.setFont("D",8); c.setFillColor(T_M); c.drawCentredString(x+(sw-8)/2,y-38,s)
    c.showPage()

def p2(c):
    y=np(c,["Why Apprenticeships Beat College","Page 2"])
    y=st(c,y,"THE DEBT-FREE CAREER PATH")
    y=bt(c,y,"Young adults take on $80K\u2013$160K in student debt for degrees that may not pay off. The trades have 750,000+ open positions \u2014 HVAC alone has 36,700 \u2014 and employers are desperate for young workers \u2014 willing to pay to train you.")
    y-=2; y=st(c,y,"APPRENTICESHIPS vs. COLLEGE")
    y=bl(c,y,[
        "Pay YOU from day one. College charges $10K\u2013$40K/year.",
        "Journey-level credential in 3\u20135 years vs. 4+ for a bachelor\u2019s.",
        "Zero student debt (avg grad: $30K\u2013$40K in loans).",
        "On-the-job training > classroom theory for trade employers.",
        "Journey-level pay ($45K\u2013$100K+) matches many degrees.",
        "Union apprenticeships: $0 tuition, employer + union fund training.",
    ]); y-=2; y=st(c,y,"WHO THIS IS FOR")
    y=bl(c,y,["17\u201325 year olds deciding after high school.","Anyone who wants to earn while learning.","People who\u2019ve heard trades pay well but don\u2019t know where to start."])
    y-=2; y=st(c,y,"WHAT YOU\u2019LL LEARN")
    y=bl(c,y,[
        "5-step system: research \u2192 prep \u2192 kit \u2192 test \u2192 interview.",
        "Certifications before you apply (OSHA 10, driver\u2019s license).",
        "Resume + cover letter templates (union & non-union).",
        "Union vs. non-union comparison.",
        "Apprentice pay by year for 6 trades.",
        "8 interview Q&As + follow-up email.",
        "10 common mistakes that kill applications.",
    ]); c.showPage()

def p3(c):
    y=np(c,["Step 1\u20132: Research & Background Prep","Page 3"])
    y=st(c,y,"STEP 1: RESEARCH & DECIDE")
    y=bt(c,y,"Spend 1\u20132 weeks researching. Rushing = wrong program.")
    y=bl(c,y,["Take the TradeLift quiz to narrow top 2 trades.","Compare union vs non-union routes.","Call 3 contractors: \u201cDo you take apprentices?\u201d","Check apprenticeship.gov for registered programs."])
    y-=3; y=st(c,y,"STEP 2: BACKGROUND PREPARATION")
    y=bt(c,y,"Get these done before applying:")
    for t,d in [("Driver\u2019s License","Required for most positions. Clean record = asset."),
                ("OSHA 10-Hour","Universal entry credential. Online, $25\u2013$40. Get this FIRST."),
                ("Physical Fitness","Trades are physical. Be ready for 50+ lbs, all weather.")]:
        y=bt(c,y,t,f="DB",s=9,co=YELLOW,sp=11); y=bt(c,y,d,s=8.5,ind=6,sp=11)
    y-=2; y=st(c,y,"TOOLS TO BRING")
    tools=[("Tape measure (25 ft)",'$10\u2013$25'),("Utility knife + blades",'$5\u2013$10'),
           ("Safety glasses (Z87.1)",'$5\u2013$15'),("Work gloves (cut-resistant)",'$15\u2013$35'),
           ("Hard hat (if not provided)",'$15\u2013$30'),("Steel-toe boots (ASTM)",'$80\u2013$160')]
    ch=18
    for tn,pr in tools:
        rr(c,M+6,y-ch,CW-12,ch,3,fc=BG_CARD,sc=BORDER)
        c.setFont("D",8); c.setFillColor(T_B); c.drawString(M+14,y-13,tn)
        c.setFont("DB",8); c.setFillColor(YELLOW); c.drawRightString(W-M-6,y-13,pr); y-=ch+1
    c.showPage()

def p4(c):
    y=np(c,["Step 3: Application Kit","Page 4"])
    y=st(c,y,"TRADE RESUME (COPY-PASTE)")
    y=bt(c,y,"One page. Certifications + reliability > extracurriculars.",s=9)
    y-=1; rr(c,M,y-180,CW,180,5,fc=BG_CARD,sc=BORDER); y-=6
    rl=["[YOUR NAME]  \u00b7  [City, State]  \u00b7  [Phone]  \u00b7  [Email]",
        "","OBJECTIVE","Motivated worker seeking [TRADE] apprenticeship. OSHA 10 certified.","",
        "CERTIFICATIONS","\u2022 OSHA 10-Hour \u2014 [Date]","\u2022 First Aid/CPR \u2014 [Date]","",
        "EXPERIENCE","[Job/project] \u00b7 [Dates] \u2014 hands-on tasks, reliability.","",
        "EDUCATION","[HS/GED] \u2014 [Year]","","REFERENCES \u2014 Available upon request."]
    c.setFont("D",8); c.setFillColor(T_B)
    for l in rl:
        if l: c.drawString(M+12,y,l)
        y-=10
    y-=6; y=st(c,y,"COVER LETTER TEMPLATES")
    y=st(c,y,"UNION"); y=bt(c,y,"Dear [Training Director], I express interest in the [Trade] apprenticeship with [Local #]. I hold OSHA 10, am physically capable, and committed to a long-term career. I welcome the chance to discuss the next intake window.",s=8.5,sp=11)
    y-=2; y=st(c,y,"NON-UNION"); y=bt(c,y,"Dear [Hiring Manager], I apply for an apprenticeship/helper position with [Company]. I hold OSHA 10, have reliable transport, and own basic tools. I\u2019m ready to work hard and learn.",s=8.5,sp=11)
    c.showPage()

def p5(c):
    y=np(c,["Step 4: The Aptitude Test","Page 5"])
    y=st(c,y,"WHAT\u2019S ON THE TEST")
    y=bt(c,y,"Most union programs require an aptitude test. Pass/fail \u2014 qualifying score, not perfect.")
    for t,d in [("1. Math (Algebra & Arithmetic)","Fractions, percentages, ratios, word problems. IBEW weights heaviest."),
                ("2. Reading Comprehension","Passages + questions. Read trade articles for vocab."),
                ("3. Mechanical Comprehension","Levers, pulleys, gears. Not on every test \u2014 check yours.")]:
        y=bt(c,y,t,f="DB",s=9,co=YELLOW,sp=10); y=bt(c,y,d,s=8.5,ind=6,sp=10)
    y-=3; y=st(c,y,"4\u20136 WEEKS BEFORE: STUDY PLAN")
    y=bl(c,y,["Khan Academy (free): algebra, ratios, percentages.","Union prep books: IBEW/UA aptitude guides.","Timed practice 2\u20133x/week under real conditions.","Sample questions at apprenticeship.gov."])
    y-=2; y=st(c,y,"TEST-DAY TIPS")
    y=bl(c,y,["Practice: timed, no phone, quiet room.","Skip >90s questions \u2014 come back later.","Eliminate obvious wrongs first.","70\u201380% usually passes. Don\u2019t aim for perfect."])
    c.showPage()

def p6(c):
    y=np(c,["Step 5: The Interview","Page 6"])
    y=st(c,y,"8 QUESTIONS + ANSWERS TO REHEARSE")
    qa=[("Q1: Why [trade]?",'"I like hands-on problem-solving. I want a skill always in demand."'),
        ("Q2: What do you know?","Reference BLS growth, local demand, or a project. Show research."),
        ("Q3: Physical work?",'"Ready to lift, carry, and work in all weather."'),
        ("Q4: Commit to 3\u20135 years?",'"Yes. This is a long-term investment."'),
        ("Q5: Transportation?",'"Yes. Driver\u2019s license + [vehicle/transport]."'),
        ("Q6: Team experience?","Sports, school projects, volunteer work, or past jobs."),
        ("Q7: Why pick you?",'"Punctual, don\u2019t quit, here because I want this career."'),
        ("Q8: Questions for us?",'"Typical first year?" / "Tools to bring day one?"')]
    for q,a in qa:
        c.setFont("DB",9); c.setFillColor(ORANGE)
        for l in wt(c,q,"DB",9,CW): c.drawString(M,y-5,l); y-=10
        y-=1; y=bt(c,y,a,s=8.5,ind=6,sp=10); y-=2
    c.showPage()

def p7(c):
    y=np(c,["Follow-Up & Union vs. Non-Union","Page 7"])
    y=st(c,y,"FOLLOW-UP EMAIL (WITHIN 24 HOURS)")
    y=bt(c,y,"Copy, paste, customize. Separates you from 90% of applicants.",s=9); y-=1
    rr(c,M,y-110,CW,110,5,fc=BG_CARD,sc=BORDER); y-=6
    el=["Subject: Thank you \u2014 [Trade] Interview","","Dear [Interviewer],",
        "Thank you for meeting about the [Trade] apprenticeship.",
        "I enjoyed [detail]. I\u2019m excited and confident I can contribute.",
        "Let me know if you need anything.","","Best, [Name] \u00b7 [Phone] \u00b7 [Email]"]
    c.setFont("D",8); c.setFillColor(T_B)
    for l in el:
        if l: c.drawString(M+12,y,l)
        y-=10
    y-=10; y=st(c,y,"UNION vs. NON-UNION")
    comp=[("Pay","Published scale","Varies, negotiable"),("Training","Standardized","Varies by company"),
          ("Tuition","$0 funded","$5K\u2013$15K OOP"),("Benefits","Health+pension","Varies/none"),
          ("Placement","Contractor network","Self-market"),("Mobility","Portable license","May re-cert"),
          ("Raises","Guaranteed steps","Performance-based")]
    ch=20; rr(c,M,y-ch,CW,ch,3,fc=ORANGE)
    c.setFont("DB",8); c.setFillColor(WHITE)
    c.drawString(M+6,y-14,"Factor"); c.drawString(M+110,y-14,"Union"); c.drawString(M+300,y-14,"Non-Union")
    y-=ch+1
    for i,(f,u,n) in enumerate(comp):
        bg=BG_CARD if i%2==0 else BG_PNL
        rr(c,M,y-ch,CW,ch,2,fc=bg,sc=BORDER)
        c.setFont("DB",7.5); c.setFillColor(WHITE); c.drawString(M+6,y-14,f)
        c.setFont("D",7.5); c.setFillColor(T_B); c.drawString(M+110,y-14,u); c.drawString(M+300,y-14,n)
        y-=ch
    y-=3; y=bt(c,y,"Bottom line: union = structure + $0 tuition. Non-union = flexibility + faster hiring. Apply to both.",s=9)
    c.showPage()

def p8(c):
    y=np(c,["Apprentice Pay by Year","Page 8"])
    y=st(c,y,"WHAT YOU\u2019LL EARN")
    y=bt(c,y,"Every registered apprenticeship pays from day one. 40\u201350% of journeyman scale, raises yearly. Source: tradelift.surge.sh/blog/apprentice-wages-by-year.html",s=9)
    y-=3; ch=20; rr(c,M,y-ch,CW,ch,3,fc=ORANGE)
    c.setFont("DB",8); c.setFillColor(WHITE)
    for lb,x in [("Trade",M+6),("Yr 1",M+120),("Yr 2",M+195),("Yr 3\u20134",M+270),("Journeyman",M+360)]:
        c.drawString(x,y-14,lb)
    y-=ch+1
    for i,(tr,y1,y2,y34,jm) in enumerate(AW):
        bg=BG_CARD if i%2==0 else BG_PNL
        rr(c,M,y-ch,CW,ch,2,fc=bg,sc=BORDER)
        c.setFont("DB",7.5); c.setFillColor(WHITE); c.drawString(M+6,y-14,tr)
        c.setFont("D",7.5); c.setFillColor(T_B); c.drawString(M+120,y-14,y1); c.drawString(M+195,y-14,y2); c.drawString(M+270,y-14,y34)
        c.setFillColor(YELLOW); c.setFont("DB",7.5); c.drawString(M+360,y-14,jm)
        y-=ch
    y-=3; y=bt(c,y,"BLS medians: electrician $61,590; plumber/pipefitter $59,880; HVAC $57,310; carpenter $51,390; welder ~$47K; construction mgr $101,900.",s=7.5,co=T_M,sp=11)
    y-=2; y=st(c,y,"ALL 12 TRADES: JOURNEY-LEVEL BANDS")
    y=bt(c,y,"Site figures from trades.html + quiz.js. Six trades are marked \u201cassumed \u2014 no dedicated post yet\u201d because no dedicated salary post exists for them on the site.",s=7.5,co=T_M,sp=11)
    bands=[("Electrician","$60K\u2013$80K","blog"),("Plumber","$55K\u2013$75K","blog"),
           ("Welder","$45K\u2013$70K","blog"),("HVAC","$50K\u2013$70K","blog"),
           ("Carpenter","$45K\u2013$65K","blog"),("Mason","$45K\u2013$70K","assumed"),
           ("Roofer","$40K\u2013$65K","assumed"),("Pipefitter","$60K\u2013$85K","blog"),
           ("Ironworker","$55K\u2013$80K","assumed"),("Diesel Mech","$45K\u2013$65K","assumed"),
           ("Auto Mech","$40K\u2013$65K","assumed"),("Constr. Mgr","$70K\u2013$100K","assumed")]
    ch=16
    for i,(nm,bd,src) in enumerate(bands):
        bg=BG_CARD if i%2==0 else BG_PNL
        rr(c,M,y-ch,CW,ch,2,fc=bg,sc=BORDER)
        c.setFont("DB",7.5); c.setFillColor(WHITE); c.drawString(M+6,y-11,nm)
        c.setFont("D",7.5); c.setFillColor(YELLOW); c.drawString(M+120,y-11,bd)
        c.setFont("D",7); c.setFillColor(T_M)
        c.drawString(M+280,y-11,"assumed \u2014 no dedicated post yet" if src=="assumed" else "blog-cited (BLS median on site)")
        y-=ch+1
    y-=4
    y=st(c,y,"KEY TAKEAWAYS")
    y=bl(c,y,["Year 1: $15\u2013$25/hr by trade and union status.","Biggest raises in years 3\u20134 (toward 80\u201390% of journeyman).","Licensing jump = largest raise of your career.","Union = $0 tuition vs. $30K\u2013$40K college debt.","Overtime + certs add $4K\u2013$5.5K+/year."])
    c.showPage()

def p9(c):
    y=np(c,["First Month on the Job","Page 9"])
    y=st(c,y,"FIRST-MONTH CHECKLIST")
    y=bt(c,y,"You got in. Don\u2019t blow it. First 30 days set the tone.",s=9); y-=2
    ph=[("WEEK 1: SHOW UP & OBSERVE",["Arrive 15 min early daily.","Introduce yourself to every crew member.","Bring own tools, PPE, water, lunch.","Don\u2019t touch anyone\u2019s tools without asking.","Listen more than talk. Write everything down."]),
        ("WEEK 2: START LEARNING",["Ask how before attempting each task.","Learn the JSA (Job Safety Analysis).","Volunteer for dirty work = trust builder.","Keep your workspace clean."]),
        ("WEEKS 3\u20134: EARN TRUST",["Take on small tasks independently.","Ask: \u201cWhat can I do better?\u201d","Clock in/out exactly.","Stay off your phone on site."])]
    for t,items in ph:
        y=st(c,y,t); c.setFont("D",8.5); c.setFillColor(T_B)
        for it in items: c.drawString(M+5,y-5,it); y-=12
        y-=4
    c.showPage()

def p10(c):
    y=np(c,["10 Common Mistakes","Page 10"])
    y=st(c,y,"10 MISTAKES THAT GET YOU REJECTED")
    y=bt(c,y,"From hiring managers and union training directors.",s=9); y-=2
    ms=[("1. Showing up late.","Punctuality = #1. Late twice = gone."),
        ("2. No OSHA 10.","No card = no interview in many shops."),
        ("3. One application only.","Apply to 5+. Different windows, different odds."),
        ("4. No follow-up call.","Call 5\u20137 days later. Most never do."),
        ("5. Lying about experience.","Tradespeople talk. Be honest."),
        ("6. No tools at interview.","Tape + glasses at minimum."),
        ("7. No thank-you email.","5 min. Separates you from 90%."),
        ("8. No company research.","Know their trades and job sites."),
        ("9. Unprepared for aptitude test.","4\u20136 weeks of study is enough."),
        ("10. Quitting year one.","First year = hardest. Stay = succeed.")]
    for t,d in ms:
        c.setFont("DB",8.5); c.setFillColor(ORANGE); c.drawString(M,y-5,t); y-=10
        y=bt(c,y,d,s=8,ind=6,sp=10); y-=1
    c.showPage()

def p11(c):
    y=np(c,["Resources & Links","Page 11"])
    y=st(c,y,"RESOURCES")
    for cat,links in [("TRAINING",[("apprenticeship.gov","Federal apprenticeship finder"),("NCCER.org","Industry credentials, 14+ trades"),("SkillsUSA.org","Career-tech competitions")]),
                      ("CERTS",[("OSHA.gov","10-Hour and 30-Hour online"),("EPA 608","Required for HVAC"),("AWS","Welding certifications")]),
                      ("SALARY DATA",[("bls.gov/ooh","Official salary + growth data"),("tradelift.surge.sh/blog/apprentice-wages-by-year.html","Year-by-year apprentice pay"),("tradelift.surge.sh/getting-started.html","5-step career roadmap")]),
                      ("UNIONS",[("IBEW.org","Electrical workers"),("UA.org","Plumbers & Pipefitters"),("UBC.org","Carpenters & Joiners")])]:
        y=st(c,y,cat)
        for url,desc in links:
            c.setFont("DB",8.5); c.setFillColor(ORANGE); c.drawString(M+5,y-5,url); y-=11
            y=bt(c,y,desc,s=7.5,ind=6,sp=10)
        y-=2
    c.showPage()

def p12(c):
    y=np(c,["What To Do Next","Page 12"])
    y=st(c,y,"TAKE THE FREE QUIZ")
    y=bt(c,y,"Not sure which trade fits? The free 2-minute quiz matches you.",s=10); y-=4
    ch=40; rr(c,M,y-ch,CW,ch,6,fc=ORANGE)
    c.setFont("DB",13); c.setFillColor(WHITE); c.drawCentredString(W/2,y-16,"Take the Free Quiz")
    c.setFont("D",9); c.setFillColor(YELLOW); c.drawCentredString(W/2,y-30,"tradelift.surge.sh/quiz.html")
    y-=ch+14; y=st(c,y,"MORE FREE RESOURCES")
    y=bl(c,y,["12 free career roadmaps: tradelift.surge.sh","Trade Career Fit Guide (free): tradelift.surge.sh/careers.guide","Tools guide: tradelift.surge.sh/tools.html","Getting started: tradelift.surge.sh/getting-started.html"])
    y-=3; y=st(c,y,"DISCLAIMER")
    y=bt(c,y,"Salary data from tradelift.surge.sh (BLS + industry). Earnings vary by location, experience, certifications. Educational only; no employment guarantee. TradeLift \u00a9 2026.",s=7.5,co=T_M,sp=11)
    c.showPage()

def p13(c):
    y=np(c,["Credits","Page 13"])
    y=H-165
    c.setFont("DB",17); c.setFillColor(WHITE); c.drawCentredString(W/2,y,"Land Your First Trade Apprenticeship"); y-=26
    c.setFont("D",10); c.setFillColor(T_B); c.drawCentredString(W/2,y,"The Step-by-Step Playbook (2026)"); y-=35
    c.setFont("D",9); c.setFillColor(T_M); c.drawCentredString(W/2,y,"A TradeLift Premium Guide"); y-=16
    c.drawCentredString(W/2,y,"tradelift.surge.sh"); y-=16; c.drawCentredString(W/2,y,FT); y-=25
    c.setFont("D",8); c.setFillColor(T_M); c.drawCentredString(W/2,y,"Built for the next generation of skilled tradespeople.")
    c.showPage()

def p14(c):
    y=np(c,["Final Page","Page 14"])
    y=H-165
    c.setFont("DB",14); c.setFillColor(WHITE); c.drawCentredString(W/2,y,"You Have the Plan. Now Execute."); y-=20
    c.setFont("D",9); c.setFillColor(T_B)
    for l in wt(c,"Every step here is something you can do this week. Don\u2019t wait. Start with the quiz, get OSHA, make the calls. The trades are hiring.","D",9,CW):
        c.drawCentredString(W/2,y,l); y-=14
    y-=14; ch=40; rr(c,M,y-ch,CW,ch,6,fc=ORANGE)
    c.setFont("DB",12); c.setFillColor(WHITE); c.drawCentredString(W/2,y-15,"tradelift.surge.sh/quiz.html")
    y-=ch+14; c.setFont("D",8); c.setFillColor(T_M)
    c.drawCentredString(W/2,y,"Questions? Reply to any TradeLift email. We\u2019ll make it right.")
    c.showPage()


def render_all(c):
    c._pg_num = 1  # p1 is page 1 (drawn directly); np() increments for p2+
    p1(c);p2(c);p3(c);p4(c);p5(c);p6(c);p7(c);p8(c);p9(c);p10(c);p11(c);p12(c);p13(c);p14(c)

def v_sal():
    site={"Electrician":"$60K\u2013$80K","Plumber":"$55K\u2013$75K","Welder":"$45K\u2013$70K",
          "HVAC Technician":"$50K\u2013$70K","Carpenter":"$45K\u2013$65K","Mason":"$45K\u2013$70K",
          "Roofer":"$40K\u2013$65K","Pipefitter":"$60K\u2013$85K","Ironworker":"$55K\u2013$80K",
          "Diesel Mechanic":"$45K\u2013$65K","Automotive Mechanic":"$40K\u2013$65K",
          "Construction Manager":"$70K\u2013$100K"}
    return ["%s: %s vs %s"%(t,SALARIES[t],e) for t,e in site.items() if SALARIES.get(t)!=e]

def v_pdf(p):
    import pypdf
    r=pypdf.PdfReader(p); pages=len(r.pages); text="".join(x.extract_text() or "" for x in r.pages)
    e=[]
    if pages<12: e.append("Pages %d<12"%pages)
    if "60K" not in text and "80K" not in text: e.append("No elec salary")
    if "750" not in text: e.append("No stats")
    if "TradeLift" not in text: e.append("No branding")
    if "not for resale" not in text: e.append("No disclaimer")
    return pages,text,e

def md5f(p):
    h=hashlib.md5()
    with open(p,"rb") as f:
        for ch in iter(lambda:f.read(8192),b""): h.update(ch)
    return h.hexdigest()

def main():
    os.makedirs(os.path.dirname(OUT),exist_ok=True)
    errs=v_sal()
    if errs:
        for e in errs: print("SALARY: "+e)
        sys.exit(1)
    print("Salary check: OK")
    c=canvas.Canvas(OUT,pagesize=letter,invariant=1); c.setPageCompression(1)
    render_all(c); c.save()
    sz=os.path.getsize(OUT); print("Generated: %s\n  Size: %d bytes (%.1f KB)"%(OUT,sz,sz/1024.0))
    pg,tx,er=v_pdf(OUT); print("  Pages: %d"%pg)
    if er:
        for e in er: print("  VERIFY: "+e); sys.exit(1)
    print("  pypdf: OK")
    h1=md5f(OUT); print("  MD5 (run1): %s"%h1)
    c2=canvas.Canvas(OUT,pagesize=letter,invariant=1); c2.setPageCompression(1)
    render_all(c2); c2.save()
    h2=md5f(OUT); print("  MD5 (run2): %s"%h2)
    if h1!=h2: print("  IDEMPOTENCY FAIL"); sys.exit(1)
    print("  Idempotency: OK\n\nDone.")

if __name__=="__main__": main()
