#Запуск python -m pytest -s /Users/shchetnikov.ra/PycharmProjects/LearnQA_Python_API/Lesson_three/homework/homework_two.py

import requests

url = 'https://playground.learnqa.ru/api/homework_cookie'
requests1 = requests.get(url)

cookie = requests1.cookies
print(f"\nэто куки: '{cookie}'")#смотрим тут какой ключ у куки
print(cookie.get('HomeWork'))#Берем значение кук по ключу HomeWork
cookieee = cookie.get('HomeWork')
assert cookieee == 'hw_value', f"Значение куки не 'hw_value', значит ошибка"