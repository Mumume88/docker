import requests
url="https://mumume.ru/favicon.ico"
response=requests.get(url)
with open ("favicon.ico","wb") as f:
    f.write(response.content)
