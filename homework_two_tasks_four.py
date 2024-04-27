import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
#Проверяем ответ при использовании get метода на url:
print(response.text)
#Парсим json и достаем token
data = response.json()
token = data.get("token")
print(token)
#Отправляем запрос на url с распарсенным токеном
request = requests.get(url, params={"token":token})
print(request.text)
#Проверяем полученный ответ с авторизацией, проверяем что значение в поле "status" == "Job is NOT ready"
data = request.json()
request_text = data.get("status")
if request_text == "Job is NOT ready":
    print("Все ок, едем дальше")
    time.sleep(15)
    request = requests.get(url, params={"token":token})
    data_new = request.json()
    request_text_one = data_new.get("status")
    if request_text_one == "Job is ready":
        print(request.text)
    elif request_text_one == "Job is NOT ready":
        print("Недостаточно времени ожидания, добавляю еще:")
        time.sleep(15)
        request = requests.get(url, params={"token": token})
        data_new = request.json()
        request_text_one = data_new.get("status")
        if request_text_one == "Job is ready":
            print("все ок")
        else:
            print("Времени ожидания не хватило, перезапусти тест")
else:
    print("не ок")