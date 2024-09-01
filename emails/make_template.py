import jinja2
from jinja2 import Template

# Define the template
template_str = """
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>{{ header }}</h1>
    <ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
    </ul> 
</body>
</html>
"""

# Create a Template object
template = Template(template_str)

# Data to be inserted into the template
data = {
    "title": "My Page",
    "header": "Welcome to My Page",
    "items": ["Item 1", "Item 2", "Item 3"]
}

# Render the template with the data
rendered_html = template.render(data)
print(rendered_html)

# This Python script utilizes Jinja2 to create personalized emails by merging data from a template with recipient details.
#  It establishes a connection to an SMTP server,
#  iterates over a list of recipients, generates customized emails using Jinja2, and sends them using the SMTP server.

# jinja2
# HTML pages for web applications
# Email content with personalized information
# Configuration files with dynamic values
# Documents and reports
# General text files 