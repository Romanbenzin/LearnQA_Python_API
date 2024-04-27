import requests

url = "https://playground.learnqa.ru/api/get_text"

response_url = requests.get(url)
print(response_url.text)