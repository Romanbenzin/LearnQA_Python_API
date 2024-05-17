import requests

url_for_cookie = "https://playground.learnqa.ru/api/homework_cookie"
url_for_header = "https://playground.learnqa.ru/api/homework_header"
response_cookie = requests.get(url_for_cookie)
response_header = requests.get(url_for_header)
cookie_one = response_cookie.cookies["HomeWork"]
header_two = response_header.headers["x-secret-homework-header"]



def test_check_cookoo():
    assert cookie_one == "hw_value", f"Значние куки 'HomeWork' не равно 'hw_value', а равно {cookie_one}"
def test_check_heder():
    assert header_two == "Some secret value", f"Значние хедера 'x-secret-homework-header' не равно 'Some secret value', а равно {header_two}"