from tests.conftest import create_delete
from user_methods import User
import pytest
from test_data import success, create_exist_error, create_field_error
import allure



@pytest.mark.usefixtures('create_delete')
class TestCreateUser:
    @allure.title("Проверка регистрации")
    def test_create_user(self):
        test = User()
        assert self.response.status_code == 200 and success in self.response.text

    @allure.title("Проверка попытки регистрации существующего пользователя")
    def test_create_existing_user(self, create_delete):
        test = User()
        response = test.create_user(create_delete)
        assert response.status_code == 403 and create_exist_error in response.text

    @allure.title("Проверка попытки регистрации без почтового адреса")
    def test_create_without_email(self, create_delete):
        test = User()
        user_data = create_delete
        del user_data['email']
        response = test.create_user(user_data)
        assert response.status_code == 403 and create_field_error in response.text
