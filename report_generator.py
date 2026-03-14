from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_report(skills, score):

    file = "static/report.pdf"

    c = canvas.Canvas(file, pagesize=letter)

    c.drawString(100,750,"Resume Analysis Report")

    y = 700

    c.drawString(100,y,"Extracted Skills:")
    y -= 20

    for skill in skills:
        c.drawString(120,y,skill)
        y -= 20

    c.drawString(100,y-20,f"ATS Score: {score}")

    c.save()

    return file