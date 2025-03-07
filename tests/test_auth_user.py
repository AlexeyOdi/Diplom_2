from test_data import success, login_field_error
from user_methods import User
import pytest
import allure

class TestAuthUser:
    @pytest.mark.usefixtures('setup')
    @allure.title("Проверка авторизации")
    def test_auth_user(self, setup):
        response = setup
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка авторизации с неккоректными логином и паролем")
    def test_auth_with_incorrect_log_and_pass(self):
        test = User()
        user_data = {}
        user_data['email'] = 'wrong_email'
        user_data['password'] = 'wrong_password'
        response = test.login_user(user_data)
        assert response.status_code == 401 and login_field_error in response.text