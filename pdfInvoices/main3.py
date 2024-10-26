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
    ['Cloud Platforms', 'Azure, AWS'],
    ['Infrastructure Provisioning Tools', 'Terraform, Azure Resource Manager'],
    ['Configuration Management', 'Ansible'],
    ['CI/CD Tools', 'Azure Pipline, Jenkins'],
    ['Build Tools', 'Maven, Webpack'],
    ['Containerization Tools', 'Docker, Kubernetes'],
    ['Source Code Management', 'Bitbucket, GitHub'],
    ['Logging & Monitoring Tools', 'Prometheus, Azure Monitor'],
    ['Visualization Tool', 'Grafana'],
    ['Scripting & Programming Languages', 'PowerShell, Bash/Shell, Python, JavaScript, YAML'],
    ['Framework', 'Flask, Django, LoopBack'],
    ['Application/Web Servers', 'Apache Tomcat'],
    ['Operating System', 'Linux, Windows'],
    ['Bug Tracking Tools', 'JIRA, Azure Boards'],
    ['Project Managing Tool', 'Asana']
]

# Create the table
for row in data:
    for col in row:
        pdf.cell(65, 8, col, 1)
    pdf.ln()

# Output the PDF
pdf.output("table.pdf")
