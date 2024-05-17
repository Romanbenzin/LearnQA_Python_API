import requests
import json
import pytest

class TestFourTask():
    def setup_method(self):
        data = {
            ["Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"],
            ["Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"],
            ["Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"],
            ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"],
            ["Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"]
        }

        Expected_values = [
            {'platform': 'Mobile', 'browser': 'No', 'device': 'Android'},
            {'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'},
            {'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'},
            {'platform': 'Web', 'browser': 'Chrome', 'device': 'No'},
            {'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'}
        ]

    def test_testik(self):
        for i in range(len(self.data)):
            print(i)
            print(self.data[i])
            response1 = requests.get(
                "https://playground.learnqa.ru/ajax/api/user_agent_check",
                headers={"User-Agent": data[i]}
            )
            try:
                response_as_dict = response1.json()
            except json.JSONDecodeError:
                assert False, f"Response is not in JSON format, Response text is {response1.text}"

            if response_as_dict["platform"] == Expected_values[i]["platform"]:
                print("sdasdsad")
            assert response_as_dict["browser"] == Expected_values[i]["browser"]
            assert response_as_dict["device"] == Expected_values[i]["device"]
