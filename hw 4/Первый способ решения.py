import requests
import json

url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

failed_list = []

datas = {
    "browser_1":"Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "browser_2":"Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
    "browser_3":"Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "browser_4":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
    "browser_5":"Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

answer = {
    "browser_1":{'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
    "browser_2":{'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
    "browser_3":{'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
    "browser_4":{'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
    "browser_5":{'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'},
    }

for browser, data in datas.items():
    response = requests.get(url, headers={"User-Agent": data})
    expected_response = json.loads(response.content)
    try:
        for key in ["platform", "browser", "device"]:
            assert expected_response[key] == answer[browser][key]
    except AssertionError:
        #failed_list.append(f"{data}:{key}:{expected_response[key]}")
        print(f"user-agent отдающий неправильный ответ:{data}\nНеправильное поле в ответе: {key}:{expected_response[key]}\n")
#print(failed_list)
