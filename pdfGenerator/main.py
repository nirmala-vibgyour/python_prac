from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():   # Some method iterrows().
    pdf.add_page()
    # set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R", ln=1)

        for y in range(10, 298, 10):
            pdf.line(10, y, 200, y)

pdf.output("output.pdf")