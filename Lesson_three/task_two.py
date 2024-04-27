import requests
class TestFirstApi:
    def test_hello_call(self):
        url = "https://playground.learnqa.ru/api/hello"
        name = "Roman"
        data = {"name":name}

        response = requests.get(url, params=data)
        #Проверка, что url отдает 200
        assert response.status_code == 200, "Wrong response code"
        # Проверка, что в ответе есть ключ answer
        response_dict = response.json()
        assert "answer" in response_dict, "There is not field 'answer' in the response"
        #Проверка, что ожидаемый результат совпадает с фактическим
        expected_response_text = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, f"Actual text: '{actual_response_text}' in the response is not correct"