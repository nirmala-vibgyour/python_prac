import requests

api_key = "2778cb8ec8784595ab775cf72c9d4b17"
# api endpoint
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-07-24&sortBy=publishedAt&\
apiKey=2778cb8ec8784595ab775cf72c9d4b17"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(content["title"])


