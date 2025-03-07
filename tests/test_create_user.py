from user_generator import generate_user
from user_methods import User
import pytest
from test_data import success, create_exist_error, create_field_error
import allure



class TestCreateUser:
    @allure.title("Проверка регистрации")
    @pytest.mark.usefixtures('setup')
    def test_create_user(self, setup):
        response = setup
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка попытки регистрации существующего пользователя")
    @pytest.mark.usefixtures('setup')
    def test_create_existing_user(self, setup):
        test = User()
        user_data = {}
        response = setup
        user = response.json().get("user")
        user_data["email"] = user["email"]
        user_data["name"] = user["name"]
        user_data["password"] = "some_password"
        response = test.create_user(user_data)
        assert response.status_code == 403 and create_exist_error in response.text

    @allure.title("Проверка попытки регистрации без почтового адреса")
    def test_create_without_email(self):
        test = User()
        user_data = generate_user()
        del user_data["email"]
        response = test.create_user(user_data)
        assert response.status_code == 403 and create_field_error in response.text
        token = test.get_token(response)
        test.delete_user(token)

