import requests


HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
}


def getUrl(url="https://programmer100.pythonanywhere.com/tours/"):
    response = requests.get(url)
    source = response.text
    return source

