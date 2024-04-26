import json
import requests

#Задание 1
json_text = {"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}
second_message = json_text["messages"][1]["message"]
print(second_message, "\n")

#Задание 2
url = "https://playground.learnqa.ru/api/long_redirect"
response = requests.get(url, allow_redirects=True)
for resp in response.history:
    print(resp.url)

print(response.url)
print(response.history, "\n")

#Задание 3