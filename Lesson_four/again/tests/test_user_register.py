import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests
import allure
class TestUserRegister(BaseCase):
    @allure.title("Test Register")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data(email=None, firstName=None)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.title("Test Register")
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = self.prepare_registration_data(email, firstName=None)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f'Unexpected response content {response.content}'

    def test_create_user_without_dog(self):
        email = 'emailwithoutdog.com'
        data = self.prepare_registration_data(email=email, firstName=None)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"Invalid email format", f'Email создался и это не хорошо'

    def test_create_user_with_short_name(self):
        firstName = "n"
        data = self.prepare_registration_data(email=None, firstName=firstName)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"The value of 'firstName' field is too short", f'Имя слишком короткое, но прошло регистрацию'

    def test_create_user_with_long_name(self):
        firstName = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
        data = self.prepare_registration_data(email=None, firstName=firstName)

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"The value of 'firstName' field is too long", f'Имя слишком короткое, но прошло регистрацию'

    fields = [
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName"),
        ("email")
    ]
    @pytest.mark.parametrize('field', fields)
    def test_create_user_without_one_field(self, field):
        data = self.prepare_registration_data(email=None, firstName=None)
        data.pop(field)
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.text == f"The following required params are missed: {field}", f'Ошибка: поле {field} присутствует в запросе'


#python -m pytest -s test_user_register.py -k test_create_user_without_one_field
