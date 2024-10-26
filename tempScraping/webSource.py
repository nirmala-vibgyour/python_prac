import requests
import sys
import io

def sourceHtml(url):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    response = requests.get(url)
    source = response.text
    return source