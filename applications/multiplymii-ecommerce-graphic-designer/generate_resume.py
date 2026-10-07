import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def create_ecommerce_resume():
    doc = docx.Document()

    # 0.32 in top/bottom, 0.4 in left/right for clean 1-page ATS fit
    for section in doc.sections:
        section.top_margin = Inches(0.32)
        section.bottom_margin = Inches(0.32)
        section.left_margin = Inches(0.4)
        section.right_margin = Inches(0.4)
        section.page_width = Inches(8.5)
        section.page_height = Inches(11.0)

    # Color Palette: Deep Slate with energetic Vibrant Indigo/Violet accent fitting TCG & E-commerce
    COLOR_PRIMARY = RGBColor(15, 23, 42)      # Deep Slate #0F172A
    COLOR_ACCENT = RGBColor(79, 70, 229)      # Vibrant Indigo #4F46E5
    COLOR_TEXT = RGBColor(51, 65, 85)         # Charcoal Slate #334155
    COLOR_MUTED = RGBColor(100, 116, 139)     # Cool Grey #64748B

    def set_font(run, name="Calibri", size_pt=8.5, bold=False, italic=False, color=COLOR_TEXT):
        run.font.name = name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color

    def add_section_header(title):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(3.5)
        p.paragraph_format.space_after = Pt(1.0)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title.upper())
        set_font(run, name="Calibri", size_pt=9.0, bold=True, color=COLOR_PRIMARY)
        
        # Bottom border
        pPr = p._p.get_or_add_pPr()
        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="6" w:space="1" w:color="4F46E5"/></w:pBdr>')
        pPr.append(pBdr)
        return p

    def add_bullet(text_parts, space_after=0.5):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.line_spacing = 1.02
        p.paragraph_format.left_indent = Inches(0.16)
        for part in text_parts:
            txt = part[0]
            bld = part[1] if len(part) > 1 else False
            col = part[2] if len(part) > 2 else COLOR_TEXT
            run = p.add_run(txt)
            set_font(run, name="Calibri", size_pt=8.2, bold=bld, color=col)
        return p

    # --- HEADER ---
    title_p = doc.add_paragraph()
    title_p.paragraph_format.space_before = Pt(0)
    title_p.paragraph_format.space_after = Pt(0)
    run_name = title_p.add_run("JEZREEL DAVE LEYBAG")
    set_font(run_name, name="Calibri", size_pt=15, bold=True, color=COLOR_PRIMARY)

    sub_p = doc.add_paragraph()
    sub_p.paragraph_format.space_before = Pt(0)
    sub_p.paragraph_format.space_after = Pt(1.5)
    run_sub = sub_p.add_run("E-commerce Graphic Designer | Shopify Visuals, Performance Marketing & TCG Collectibles")
    set_font(run_sub, name="Calibri", size_pt=9.5, bold=True, color=COLOR_ACCENT)

    contact_p = doc.add_paragraph()
    contact_p.paragraph_format.space_before = Pt(0)
    contact_p.paragraph_format.space_after = Pt(1.0)
    
    contacts = [
        ("Email: ", True, COLOR_PRIMARY),
        ("jezreelleybag.graphics@gmail.com  |  ", False, COLOR_TEXT),
        ("Phone/WhatsApp: ", True, COLOR_PRIMARY),
        ("+63 939-399-1289  |  ", False, COLOR_TEXT),
        ("Location: ", True, COLOR_PRIMARY),
        ("Philippines (Remote Eastern Time / 5:00 AM PHT Overlap Ready)", False, COLOR_TEXT)
    ]
    for c_txt, c_bld, c_col in contacts:
        r = contact_p.add_run(c_txt)
        set_font(r, size_pt=8.0, bold=c_bld, color=c_col)

    links_p = doc.add_paragraph()
    links_p.paragraph_format.space_before = Pt(0)
    links_p.paragraph_format.space_after = Pt(2.5)
    
    links = [
        ("Live Portfolio: ", True, COLOR_ACCENT),
        ("https://jezreel-portfolio-brown.vercel.app  |  ", False, COLOR_TEXT),
        ("Drive Vault: ", True, COLOR_PRIMARY),
        ("drive.google.com/drive/folders/1_cBN8MPPfaPkyvYzinhUuSuz0kexx1tx  |  ", False, COLOR_TEXT),
        ("LinkedIn: ", True, COLOR_PRIMARY),
        ("linkedin.com/in/jezreel-dave-leybag-a01528152", False, COLOR_TEXT)
    ]
    for l_txt, l_bld, l_col in links:
        r = links_p.add_run(l_txt)
        set_font(r, size_pt=7.8, bold=l_bld, color=l_col)

    pPr = links_p._p.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="8" w:space="2" w:color="0F172A"/></w:pBdr>')
    pPr.append(pBdr)

    # --- PROFESSIONAL SUMMARY ---
    add_section_header("Professional Summary")
    sum_p = doc.add_paragraph()
    sum_p.paragraph_format.space_before = Pt(1.0)
    sum_p.paragraph_format.space_after = Pt(2.0)
    sum_p.paragraph_format.line_spacing = 1.05
    sum_text = [
        ("Creative, performance-focused ", False),
        ("E-commerce Graphic Designer & Visual Content Creator", True),
        (" with 4+ years of international experience designing high-converting ", False),
        ("Shopify storefront assets", True),
        (", promotional marketing campaigns, private label merchandise graphics, and dynamic short-form video content. Deep, authentic passion for ", False),
        ("Trading Card Games (Pokémon, Magic: The Gathering, One Piece)", True, COLOR_ACCENT),
        (", anime, and gaming collectibles, allowing seamless execution of community-aligned visual hooks without creative friction. Advanced expertise across ", False),
        ("Adobe Photoshop, Illustrator, Premiere Pro, After Effects, Canva Pro, and CapCut", True),
        (". Proven track record managing complete visual refreshes, stream overlay assets, and collection banners for North American and global brands. Ready for immediate full-time start with a 5:00 AM PHT schedule for Eastern Time business hours overlap.", False),
    ]
    for txt, bld, *rest in sum_text:
        col = rest[0] if rest else COLOR_TEXT
        r = sum_p.add_run(txt)
        set_font(r, size_pt=8.2, bold=bld, color=col)

    # --- CORE COMPETENCIES MATRIX (COMPACT 3x2 TABLE) ---
    add_section_header("Core Competencies & Creative Capabilities")
    
    table = doc.add_table(rows=3, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False

    col_widths = [Inches(3.85), Inches(3.85)]
    for row in table.rows:
        for idx, width in enumerate(col_widths):
            row.cells[idx].width = width

    skills_data = [
        [
            ("Shopify & E-commerce Visuals: ", "Homepage hero banners, collection page headers, product badging, promotional popups, seasonal sale asset bundles."),
            ("Performance Ad Creatives & Social: ", "High-CTR social ads (Meta, TikTok), carousel storytelling, data-backed visual hooks, release drop announcements.")
        ],
        [
            ("TCG & Pop Culture Fluency: ", "In-depth understanding of Pokémon TCG sets, Magic: The Gathering, One Piece TCG, League of Legends, sports cards & hobby supplies."),
            ("Short-Form Video & Motion: ", "CapCut, Premiere Pro, After Effects, dynamic unboxing pacing, card reveal teasers, sound design, viral Reels/Shorts edits.")
        ],
        [
            ("Private Label & Packaging Graphics: ", "Branded packaging, product labels, custom playmat layouts, deck box graphics, apparel & merchandise graphics."),
            ("Streaming & Digital Overlays: ", "Twitch/YouTube stream overlays, webcam borders, starting/ending screens, alert badges, tournament graphics.")
        ]
    ]

    for r_idx, row_content in enumerate(skills_data):
        row = table.rows[r_idx]
        for c_idx, cell_data in enumerate(row_content):
            cell = row.cells[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(1.0)
            p.paragraph_format.line_spacing = 1.01
            r_title = p.add_run(cell_data[0])
            set_font(r_title, size_pt=8.0, bold=True, color=COLOR_PRIMARY)
            r_desc = p.add_run(cell_data[1])
            set_font(r_desc, size_pt=7.8, bold=False, color=COLOR_TEXT)

    # --- PROFESSIONAL EXPERIENCE ---
    add_section_header("Professional Experience")

    # ROLE 1: Morpho Studio
    p_r1 = doc.add_paragraph()
    p_r1.paragraph_format.space_before = Pt(2.0)
    p_r1.paragraph_format.space_after = Pt(0.5)
    p_r1.paragraph_format.keep_with_next = True
    
    t_role = p_r1.add_run("Digital Brand & E-commerce Visual Designer")
    set_font(t_role, size_pt=9.0, bold=True, color=COLOR_PRIMARY)
    t_div = p_r1.add_run(" | ")
    set_font(t_div, size_pt=9.0, bold=False, color=COLOR_MUTED)
    t_co = p_r1.add_run("Morpho Studio & Digital Brand Ecosystem")
    set_font(t_co, size_pt=9.0, bold=True, color=COLOR_ACCENT)
    t_dt = p_r1.add_run(" (Jan 2024 – Present)")
    set_font(t_dt, size_pt=8.0, bold=False, color=COLOR_MUTED)

    add_bullet([
        ("Owned complete digital storefront and app visual identity, designing promotional hero banners, category headers, and campaign assets that drove a ", False),
        ("30% increase in digital order volume", True),
        (" within 30 days.", False)
    ])
    add_bullet([
        ("Produced engaging short-form video reels and motion graphics in CapCut and Premiere Pro showcasing product launches and behind-the-scenes content, boosting social engagement by 45%.", False)
    ])
    add_bullet([
        ("Designed private label product packaging, merchandise artwork (custom apparel, tumblers, branded packaging), and in-store promotional displays with meticulous print-ready accuracy.", False)
    ])
    add_bullet([
        ("Built reusable design templates in Canva and Adobe Creative Suite, establishing cohesive brand guidelines that cut ongoing promotional turnaround times by half.", False)
    ])

    # ROLE 2: Commercial Printing & Graphics Studio
    p_r2 = doc.add_paragraph()
    p_r2.paragraph_format.space_before = Pt(2.0)
    p_r2.paragraph_format.space_after = Pt(0.5)
    p_r2.paragraph_format.keep_with_next = True

    t_role2 = p_r2.add_run("Lead Graphic Designer & Merchandise Specialist")
    set_font(t_role2, size_pt=9.0, bold=True, color=COLOR_PRIMARY)
    t_div2 = p_r2.add_run(" | ")
    set_font(t_div2, size_pt=9.0, bold=False, color=COLOR_MUTED)
    t_co2 = p_r2.add_run("Commercial Graphics & Printing Studio")
    set_font(t_co2, size_pt=9.0, bold=True, color=COLOR_ACCENT)
    t_dt2 = p_r2.add_run(" (Jan 2023 – Dec 2024)")
    set_font(t_dt2, size_pt=8.0, bold=False, color=COLOR_MUTED)

    add_bullet([
        ("Designed commercial product graphics, custom merchandise, collector apparel, and marketing collateral for corporate, event, and retail clients.", False)
    ])
    add_bullet([
        ("Pre-flighted complex vector illustrations in Adobe Illustrator and Photoshop, managing resolution, bleed margins, and spot color accuracy for high-volume manufacturing.", False)
    ])
    add_bullet([
        ("Collaborated with clients to translate unstructured visual requests into polished product mockups and digital advertising assets with minimal revision loops.", False)
    ])

    # ROLE 3: International Remote Accounts
    p_r3 = doc.add_paragraph()
    p_r3.paragraph_format.space_before = Pt(2.0)
    p_r3.paragraph_format.space_after = Pt(0.5)
    p_r3.paragraph_format.keep_with_next = True

    t_role3 = p_r3.add_run("Remote Visual Designer & Video Editor")
    set_font(t_role3, size_pt=9.0, bold=True, color=COLOR_PRIMARY)
    t_div3 = p_r3.add_run(" | ")
    set_font(t_div3, size_pt=9.0, bold=False, color=COLOR_MUTED)
    t_co3 = p_r3.add_run("International Accounts (Canada, UAE, Italy)")
    set_font(t_co3, size_pt=9.0, bold=True, color=COLOR_ACCENT)
    t_dt3 = p_r3.add_run(" (Dec 2020 – Dec 2024)")
    set_font(t_dt3, size_pt=8.0, bold=False, color=COLOR_MUTED)

    add_bullet([
        ("Created high-converting Amazon product listings, packaging composites, and e-commerce visual assets for Canadian online retailer TrendNSave under strict marketplace specs.", False)
    ])
    add_bullet([
        ("Edited cinematic event videos and short-form promotional teasers in Adobe Premiere Pro and After Effects with custom Foley sound design, color grading, and dynamic kinetic typography.", False)
    ])
    add_bullet([
        ("Delivered 100% on-time project execution across Canadian and international time zones with proactive daily English communication via Slack and Teams.", False)
    ])

    # --- TECHNICAL SKILLS, SOFTWARE & EQUIPMENT ---
    add_section_header("Technical Skills, Software & Equipment")

    add_bullet([
        ("Design & Vector Software: ", True),
        ("Adobe Photoshop, Adobe Illustrator, Canva Pro, Adobe After Effects, InDesign, Figma (basic), typography hierarchy, digital color theory.", False)
    ])
    add_bullet([
        ("Video Editing & Motion: ", True),
        ("Adobe Premiere Pro, CapCut, DaVinci Resolve, dynamic social pacing, sound design & scoring, YouTube Shorts / TikTok aspect optimization.", False)
    ])
    add_bullet([
        ("E-commerce & Streaming: ", True),
        ("Shopify storefront visual management, collection banners, product card badging, OBS / Streamlabs overlays, Twitch / YouTube stream graphics.", False)
    ])
    add_bullet([
        ("Workstation & Connectivity: ", True),
        ("Windows 11 Creator Workstation (High-Performance GPU/SSD); 300 Mbps Fiber Internet + 4G LTE Hotspot failover; Dual UPS backup systems.", False)
    ])

    output_path = r"d:\Jezreel Dave - Personal Branding\my-personal-website\applications\multiplymii-ecommerce-graphic-designer\Jezreel_Dave_Leybag_Ecommerce_Graphic_Designer.docx"
    doc.save(output_path)
    print(f"Resume generated successfully at: {output_path}")

if __name__ == "__main__":
    create_ecommerce_resume()
