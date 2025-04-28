from fpdf import FPDF

# Create instance of FPDF
pdf = FPDF()
pdf.add_page()

# Set font for the header
# pdf.set_font('Times', 'B', 8)
#
# # Table header
# header = ['Header 1', 'Header 2']
# for col in header:
#     pdf.cell(65, 8, col, 1)
# pdf.ln()

# Set font for the data
pdf.set_font('Times', 'B', 8)

# Sample data
data = [
    ['Source Code Management', 'GitHub', '***'],
    ['Logging & Monitoring Tools', 'Prometheus', '***'],
    ['Visualization Tool', 'Grafana', '***'],
    ['Scripting & Programming Languages', 'Python', '***'],
    ['Framework', 'Flask', '**'],
    ['Application/Web Servers', 'Apache, Nginx', '**'],
    ['Operating System', 'Linux, Windows', '***'],
    ['Bug Tracking Tools', 'JIRA','***']
]

# Create the table
for row in data:
    for col in row:
        pdf.cell(65, 8, col, 1)
    pdf.ln()

# Output the PDF
pdf.output("table.pdf")
