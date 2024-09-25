import requests

url = "https://www.estesparkweather.net/archive_reports.php?date=202408"

response = requests.get(url)
response.encoding = 'utf-8'

print(response.status_code)

content = response.text
with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(content)


# JavaScript: ajaxLoader('clientraw.txt?'+new Date()); setColHeight();    