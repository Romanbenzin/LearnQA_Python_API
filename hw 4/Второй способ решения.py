import requests
import json

url = "https://playground.learnqa.ru/ajax/api/user_agent_check"

failed_list = []

datas = [
    "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
    "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
    "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
]

answer = [
    {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
    {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
    {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
    {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
    {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'},
]

for i in range(len(datas)):
    response1 = requests.get(url, headers={"User-Agent":datas[i]})
    try:
        response_as_dict = response1.json()
        for key, value in answer[i].items():
            if response_as_dict[key] != value:
                print(f"User-Ageng={response_as_dict} Ожидаемый ответ={key}:{value}, Фактический ответ={key}:{response_as_dict[key]}")


        #assert answer[i]["platform"] == response_as_dict["platform"], "бла бла"
        #assert answer[i]["browser"] == response_as_dict["browser"], "бла бла"
        #assert answer[i]["device"] == response_as_dict["device"], "бла бла"
    except:
        print('s')
