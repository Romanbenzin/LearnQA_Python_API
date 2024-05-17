#Запуск python -m pytest -s /Users/shchetnikov.ra/PycharmProjects/LearnQA_Python_API/Lesson_three/homework/homework_four.py

import requests

request1 = requests.get(
    "https://playground.learnqa.ru/ajax/api/user_agent_check",
    headers={"User-Agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"}
)
print(request1.text)