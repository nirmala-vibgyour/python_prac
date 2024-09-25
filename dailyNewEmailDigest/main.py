import requests
from send_email import send_email


api_key = "2778cb8ec8784595ab775cf72c9d4b17"
# api endpoint
topic = "tesla"

url = "https://newsapi.org/v2/everything?"\
       f"q={topic}&"\
       "from=2024-08-16&"\
       "sortBy=publishedAt&"\
       "apiKey=2778cb8ec8784595ab775cf72c9d4b17&"\
       "language=en"

request = requests.get(url)
content = request.json()

# print(content['articles']) # get the content in json format
# print(request) # returns a response object

body = ""
headers = "Subject: Today's News\n"
for article in content["articles"][:10]:
    if article["title"] and article["description"] is not None:
        body = body + article["title"] + "\n" \
                + article["description"] \
                + "\n" + article["url"] + 2*"\n"


body = body.encode("utf-8")
headers = headers.encode("utf-8")
message = headers + body
send_email(message=message)