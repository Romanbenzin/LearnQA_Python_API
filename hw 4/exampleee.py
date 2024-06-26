import requests
import json

url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

datas = {
    'User-Agent':'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
    'User-Agent':'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
    'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
    'User-Agent':'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}
answer = {
    'platform': 'Mobile', 'browser': 'No', 'device': 'Android',
    'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS',
    'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown',
    'platform': 'Web', 'browser': 'Chrome', 'device': 'No',
    'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'
}

for data in datas:
    response_one = requests.get(url, headers={data})
    print(response_one)
    #try:
    #    response_as_dict = response_one.json()
    #except json.JSONDecodeError:
    #    assert False, f"Response is not in JSON format, Response text is {response_one.text}"

    #assert response_as_dict["platform"] == "Mobile" or "Googlebot" or "Web", "ошибка 1"
    #assert response_as_dict["browser"] == "No" or "Chrome" or "device", "ошибка 2"
    #assert response_as_dict["device"] == "Android" or "iOS" or "Unknown" or "iPhone" or "No", "ошибка 3"