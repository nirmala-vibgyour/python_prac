import requests


url = "https://upload.wikimedia.org/wikipedia/commons/3/33/Bermuda_Triangle.png"
response = requests.get(url)

# print(response.text)

with open("image.jpg", "wb") as file:
    file.write(response.content)



