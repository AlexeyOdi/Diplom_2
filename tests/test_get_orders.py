from test_data import success
from user_methods import User
import pytest
import allure

class TestGetOrders:
    @pytest.mark.usefixtures('create_delete')
    @allure.title("Проверка получения заказа неавторизированного пользователя")
    def test_get_unauth_user_order(self):
        test = User()
        response = test.get_orders(self.token)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    @allure.title("Проверка получения заказа авторизированного пользователя")
    def test_get_auth_user_order(self, login_delete):
        test = User()
        response = test.get_orders(login_delete)
        assert response.status_code == 200 and success in response.text
