from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_JUSTIFY
import os

THRESHOLD = 50  # % score threshold for red vs green

def generate_pdf_report(results, score, output_path):
    doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=40, leftMargin=40, topMargin=60, bottomMargin=40)
    styles = getSampleStyleSheet()

    # ✅ Register Unicode font
    font_path = os.path.join("fonts", "NotoSansDevanagari-Regular.ttf")
    pdfmetrics.registerFont(TTFont("Devanagari", font_path))

    styles.add(ParagraphStyle(
        name='Devanagari',
        fontName='Devanagari',
        fontSize=12,
        leading=18,
        alignment=TA_JUSTIFY,
    ))

    elements = []

    # 📊 Title and Score
    title = Paragraph("<b>Plagiarism Report</b>", styles['Title'])
    score_para = Paragraph(f"<b>Plagiarism Score:</b> {score:.2f}%", styles['Devanagari'])

    elements.append(title)
    elements.append(Spacer(1, 12))
    elements.append(score_para)
    elements.append(Spacer(1, 24))

    # 🔴🟢 Sentence Highlighting
    for sentence, sim in results:
        color = "red" if sim >= THRESHOLD else "green"
        formatted = f'<font color="{color}">{sentence}</font>'
        elements.append(Paragraph(formatted, styles['Devanagari']))
        elements.append(Spacer(1, 10))

    doc.build(elements)
