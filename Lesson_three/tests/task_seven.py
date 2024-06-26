import requests
import pytest
from Lesson_three.lib.base_case import BaseCase
from Lesson_three.lib.assertions import Assertions

class TestUserAuth(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]
    def setup(self):
        data = {
            'email':'vinkotov@example.com',
            'password':'1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        self.auth_sid = self.get_cookie(response1, "auth_sid")
        self.token = self.get_header(response1, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(response1, "user_id")

    def test_auth_user(self):

        response2 = requests.get(
            "https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token":self.token},
            cookies={"auth_sid":self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            error_message="user id from auth method is not equal to user id from check method"
        )

        assert "user_id" in response2.json(), "There is no user id in the second response"
        user_id_from_check_method = response2.json()["user_id"]

        assert self.user_id_from_auth_method == user_id_from_check_method, "user id from auth metod is not equel to user id from check method"

    @pytest.mark.parametrize('condition', exclude_params)
    def test_nagative_auth_check(self, condition):

        if condition == "no_cookie":
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                headers={"x-csrf-token":self.token}
            )
        else:
            response2 = requests.get(
                "https://playground.learnqa.ru/api/user/auth",
                cookies={"auth_sid":self.auth_sid}
            )

            Assertions.assert_json_value_by_name(
                response2,
                "user_id",
                0,
                f"User is authorization with condition {condition}"
            )