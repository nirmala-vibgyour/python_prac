from fpdf import FPDF

# an intro
# work experience
# courses & training
# education
# technical skills
# interests
# personal info

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()

# pdf.set_line_width(1)
# pdf.rect(10, 10, pdf.w - 20, pdf.h - 20)
pdf.set_fill_color(230, 230, 230)  # Light gray color
x, y, w, h = 0, 0, 250, 40  # Position and size of the rectangle
pdf.rect(x, y, w, h, 'F')

pdf.set_draw_color(80, 80, 80)
pdf.set_line_width(0.05)

pdf.set_font(family="Times", size=14, style="B")
pdf.set_text_color(80, 80, 80)
pdf.cell(w=50, h=5, txt="Nirmala Chowdhury", ln=1)
pdf.set_font(family="Times", size=9, style="B")
pdf.cell(w=50, h=4, txt="Phone no: 9164419680", ln=1)
pdf.set_font(family="Times", size=9, style="B")
pdf.cell(w=50, h=4, txt="Email: nirmalawrk@gmail.com", ln=1)
pdf.cell(w=50, h=4, txt="LinkedIn: www.linkedin.com/in/nirmala-chowdhury-a003941bb", ln=1)


# pdf.set_font(family="Times", size=14, style="B")
# pdf.cell(w=50, h=20, txt="Profile", ln=1)

pdf.line(00, 40, 250, 40)

pdf.set_font(family="Times", size=10, style="B")
pdf.set_y(45)
pdf.cell(w=45, h=2, txt="Detail oriented, result driven, organised and dependable candidate successful at managing multiple priorities", ln=1)
pdf.cell(w=45, h=5, txt="with a positive attitude.", ln=1)

pdf.set_font(family="Times", size=14, style="B")
pdf.cell(w=50, h=30, txt="Working Experience", ln=1)

# pdf.set_draw_color(80, 80, 80)
# pdf.set_line_width(0.05)
pdf.line(10, 70, 200, 70)

pdf.set_y(75)
pdf.set_font(family="Times", size=12, style="B")
pdf.cell(w=50, h=5, txt="ExactSpace Technologies Pvt Ltd.", ln=1)
pdf.set_font(family="Times", size=8, style="B")
pdf.cell(w=50, h=5, txt="Product Implementation Specialist", ln=1)
pdf.cell(w=50, h=5, txt="Sep, 22 - Dec, 23", ln=1)

# pdf.set_xy(25, 90)
# pdf.cell(w=50, h=5, txt="- worked on the various features of the product", ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- worked on OPCDA integration", ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- worked on Pandas for creating report based on client requirement", ln=1 )


pdf.set_xy(10, 95)
pdf.set_font(family="Times", size=12, style="B")
pdf.cell(w=50, h=5, txt="K12 Techno Services", ln=1)
pdf.set_font(family="Times", size=8, style="B")
pdf.cell(w=50, h=5, txt="Content Reviewer Intern", ln=1)
pdf.cell(w=50, h=5, txt="Oct, 21 - Sep, 22", ln=1)
# pdf.set_xy(25, 125)
# pdf.cell(w=50, h=5, txt="- quality check of the science and mathematics questions", ln=1)


pdf.set_xy(10, 115)
pdf.set_font(family="Times", size=12, style="B")
pdf.cell(w=50, h=5, txt="Self Employed Tutor", ln=1)
pdf.set_font(family="Times", size=8, style="B")
pdf.cell(w=50, h=5, txt="April, 12 - March, 22", ln=1)
# pdf.set_xy(25, 145)
# pdf.cell(w=50, h=5, txt="- given tuition to students from standard 6 - 12", ln=1)

pdf.set_x(10)
pdf.set_font(family="Times", size=14, style="B")
pdf.cell(w=50, h=30, txt="Skills", ln=1)
pdf.line(10, 143, 200, 143)
pdf.set_xy(25, 150)
pdf.set_font(family="Times", size=8, style="B")
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- Python",ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- frameworks: Flask, Django, Loopback",ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- Pandas, Numpy",ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- Jupyter Notebook, Postman, Git, Figma, Grafana", ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- HTML, CSS, JS",ln=1)
# pdf.set_x(25)
# pdf.cell(w=50, h=5, txt="- Other languages: Fortran, C++",ln=1)
data = [
    ['Critical Thinking', '-', '****'],
    ['Problem Solving', '-', '****'],
    ['Team Work', '-', '***'],
    ['Configuration Management', '-', '****'],
    ['Client management', '-', '****']
]

# # Create the table
for row in data:
    pdf.set_x(25)
    for col in row:
        pdf.cell(40, 8, col, 0)
    pdf.ln()

pdf.set_x(10)
pdf.set_font(family="Times", size=14, style="B")
pdf.cell(w=50, h=30, txt="Education", ln=1)
pdf.line(10, 208, 200, 208)
pdf.set_xy(25, 215)
pdf.set_font(family="Times", size=8, style="B")
pdf.cell(w=50, h=5, txt="- MSc (Physics)        [2016 - 2018]", ln=1)
pdf.set_x(25)
pdf.cell(w=50, h=5, txt="- BSc (Physics)        [2013 - 2015]", ln=1)

pdf.set_x(10)
pdf.set_font(family="Times", size=14, style="B")
pdf.cell(w=50, h=25, txt="Technical Skills", ln=1)
pdf.line(10, 240, 200, 240)


dataTech = [
    ['Language:', 'Python', '[***]'],
    ['Framework:', 'Flask', '[***]'],
    ['Other languages:', 'JS, Fortran, HTML, CSS', '[***]']
]
pdf.set_xy(25, 245)
pdf.set_font(family="Times", size=8, style="B")

# Create the table
for row in dataTech:
    pdf.set_x(25)
    for col in row:
        pdf.cell(40, 8, col, 0)
    pdf.ln()


pdf.set_x(10)
pdf.set_font(family="Times", size=14, style="B")
pdf.cell(w=50, h=20, txt="Courses", ln=1)
pdf.line(10, 23, 200, 23)
pdf.set_xy(25, 28)
pdf.set_font(family="Times", size=8, style="B")
pdf.cell(w=50, h=5, txt="- The Complete Pandas Bootcamp 2024: Data Science with Python, Udemy", ln=1)
pdf.set_x(25)
pdf.cell(w=50, h=5, txt="- Python Mega Course, Udemy")


pdf.output("resumeAdmin.pdf")



