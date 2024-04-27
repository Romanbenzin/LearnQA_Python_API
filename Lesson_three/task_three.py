import requests
import pytest
class TestFirstApi:
    names = [
        ("Roman"),
        ("NotROman"),
        ("")
    ]
    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name":name}

        response = requests.get(url, params=data)

        #Проверка, что url отдает 200
        assert response.status_code == 200, "Wrong response code"

        # Проверка, что в ответе есть ключ answer
        response_dict = response.json()
        assert "answer" in response_dict, "There is not field 'answer' in the response"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            #Проверка, что ожидаемый результат совпадает с фактическим
            expected_response_text = f"Hello, {name}"

        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_text, f"Actual text: '{actual_response_text}' in the response is not correct"