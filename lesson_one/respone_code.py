import requests

response = requests.post("https://playground.learnqa.ru/api/check_type")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_500")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/something")
print(response.status_code)
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
print(response.status_code)
print(response.text, "\n")

response = requests.post("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
first_response = response.history[0]
second_response = response
print(first_response)
print(second_response, "\n")

response = requests.post("https://playground.learnqa.ru/api/get_303")
print(response.status_code)
print(response.text)