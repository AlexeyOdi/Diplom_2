from test_data import success
from user_methods import User
import pytest
import allure

@pytest.mark.usefixtures('setup')
class TestGetOrders:
    @allure.title("Проверка получения заказа неавторизированного пользователя")
    def test_get_unauth_user_order(self, get_token):
        test = User()
        token = get_token
        response = test.get_orders(token)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка получения заказа авторизированного пользователя")
    def test_get_auth_user_order(self, get_token):
        test = User()
        token = get_token
        response = test.get_orders(token)
        assert response.status_code == 200 and success in response.text
