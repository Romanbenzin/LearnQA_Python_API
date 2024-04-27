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
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
text_response = requests.get(url)
print(text_response.text, "\n")

payload = {"method":"HEAD"}
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
text_response = requests.get(url, params=payload)
print(text_response.text, "\n")

payload = {"method":"GET"}
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
text_response = requests.get(url, params=payload)
print(text_response.text, "\n")

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
# Список возможных типов запросов
request_types = ["GET", "POST", "PUT", "DELETE"]
# Цикл для проверки всех сочетаний
for request_type in request_types:
    # Отправляем запрос с соответствующим типом
    response = requests.request(request_type, url, params={"method": request_type})

    # Проверяем, совпадает ли тип запроса с параметром method
    if response.status_code == 200:
        print(f"Тип запроса: {request_type}, значение параметра method: {request_type}, Ответ сервера: {response.text}")
    else:
        print(
            f"Тип запроса: {request_type}, значение параметра method: {request_type}, Ошибка сервера: {response.status_code}")

    # Проверяем все остальные возможные значения параметра method
    for other_request_type in request_types:
        if other_request_type != request_type:
            response = requests.request(request_type, url, params={"method": other_request_type})
            if response.status_code == 200:
                print(
                    f"Тип запроса: {request_type}, значение параметра method: {other_request_type}, Ответ сервера: {response.text}")
            else:
                print(
                    f"Тип запроса: {request_type}, значение параметра method: {other_request_type}, Ошибка сервера: {response.status_code}")