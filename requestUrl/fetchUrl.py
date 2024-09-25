import requests

url = "https://programmer100.pythonanywhere.com/tours/"

def getUrl(url):
    response = requests.get(url)
    source = response.text
    return source

print(getUrl(url))