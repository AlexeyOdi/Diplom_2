from test_data import email_to_change, success, password_to_change, name_to_change, email_change_error
from tests.conftest import create_delete
from user_methods import User
import pytest
import allure

class TestChangeData:

    @pytest.mark.usefixtures('login_delete')
    @allure.title("Проверка смены почтового адреса после авторизации")
    def test_change_email_with_auth(self, login_delete):
        test = User()
        response = test.change_data(login_delete,email_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    @allure.title("Проверка смены пароля после авторизации")
    def test_change_password_with_auth(self, login_delete):
        test = User()
        response = test.change_data(login_delete, password_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    @allure.title("Проверка смены имени после авторизации")
    def test_change_name_with_auth(self, login_delete):
        test = User()
        response = test.change_data(login_delete, name_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    @allure.title("Проверка смены почтового адреса без авторизации")
    def test_change_email_without_auth(self):
        test = User()
        response = test.change_data(self.token, email_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    @allure.title("Проверка смены пароля без авторизации")
    def test_change_password_without_auth(self):
        test = User()
        response = test.change_data(self.token, password_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    @allure.title("Проверка смены имени без авторизации")
    def test_change_name_without_auth(self):
        test = User()
        response = test.change_data(self.token, name_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    @allure.title("Проверка смены почтового адреса на существующий")
    def test_change_email_with_using_email(self, create_delete):
        test = User()
        using_email = {'email':'alex@yandex.ru'}
        response = test.change_data(self.token, using_email)
        assert response.status_code == 403 and email_change_error in response.text



