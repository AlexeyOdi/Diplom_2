from test_data import email_to_change, success, password_to_change, name_to_change, email_change_error, using_email
from tests.conftest import get_token
from user_methods import User
import pytest
import allure

@pytest.mark.usefixtures('setup')
class TestChangeData:

    @allure.title("Проверка смены почтового адреса после авторизации")
    def test_change_email_with_auth(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token,email_to_change)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка смены пароля после авторизации")
    def test_change_password_with_auth(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token, password_to_change)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка смены имени после авторизации")
    def test_change_name_with_auth(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token, name_to_change)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка смены почтового адреса без авторизации")
    def test_change_email_without_auth(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token, email_to_change)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка смены пароля без авторизации")
    def test_change_password_without_auth(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token, password_to_change)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка смены имени без авторизации")
    def test_change_name_without_auth(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token, name_to_change)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка смены почтового адреса на существующий")
    def test_change_email_with_using_email(self, get_token):
        test = User()
        token = get_token
        response = test.change_data(token, using_email)
        assert response.status_code == 403 and email_change_error in response.text



