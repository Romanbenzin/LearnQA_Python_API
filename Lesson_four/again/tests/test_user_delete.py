from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import requests
import allure

class TestUserDelete(BaseCase):
    @allure.title("Test Delete")
    def test_delete_nodelete_user(self):
        #AUTH
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response,"user_id")

        #GET
        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        #DELETE
        url = f"/user/{user_id_from_auth_method}"
        response3 = MyRequests.delete(url,
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid})
        Assertions.assert_code_status(response3, 400)
        response3_dict = response3.json()
        id_from_response3_dict = response3_dict["error"]
        assert id_from_response3_dict == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", "Ошибка"
        #GET after DELETE
        response2 = MyRequests.get(
            f"/user/{user_id_from_auth_method}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        assert response2.text == ('{"id":"2","username":"Vitaliy","email":"vinkotov@example.com","firstName":"Vitalii",'
                                  '"lastName":"Kotov"}'), "Удалился id 2 и это плохо"

    @allure.title("Test Delete")
    def test_create_delete_get_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            "email": email,
            "password": password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #GET
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        response3_dict = response3.json()
        id_from_response3_dict = response3_dict["id"]

        #DELETE
        url = f"/user/{id_from_response3_dict}"
        response4 = MyRequests.delete(url,
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )
        response4_dict = response4.json()
        id_from_response4_dict = response4_dict["success"]
        assert id_from_response4_dict == "!", "Ошибка"

        # GET
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        assert response3.text == "User not found", "юзер не удален"

    #Тест ниже удаляется любой id любого пользователя, если авторизация корректна, что является багом