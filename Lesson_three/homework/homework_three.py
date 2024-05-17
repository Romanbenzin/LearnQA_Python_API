#Запуск python -m pytest -s /Users/shchetnikov.ra/PycharmProjects/LearnQA_Python_API/Lesson_three/homework/homework_three.py

import requests

url = 'https://playground.learnqa.ru/api/homework_header'
request1 = requests.get(url)
header = request1.headers
print(header)
headeeeeer = header.get('x-secret-homework-header')
print(headeeeeer)
assert headeeeeer == 'Some secret value', f"Значение хереда не 'Some secret value', значит ошибка"