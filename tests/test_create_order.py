from test_data import order_data, success, ingr_error
from user_methods import User
import pytest
import allure

@pytest.mark.usefixtures('setup')
class TestCreateOrder:
    @allure.title("Проверка создания заказа")
    def test_create_order_with_auth(self, get_token):
        test = User()
        token = get_token
        response = test.create_order(token,order_data)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка создания заказа с ингредиентами")
    def test_create_order_with_ingr(self, get_token):
        test = User()
        token = get_token
        response = test.create_order(token, order_data)
        assert response.status_code == 200 and success in response.text

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_ingr(self, get_token):
        test = User()
        token = get_token
        response = test.create_order(token, {"ingredients": []})
        assert response.status_code == 400 and ingr_error in response.text

    @allure.title("Проверка создания заказа с ингредиентами , которые не существуют")
    def test_create_order_with_unexist_ingr(self, get_token):
        test = User()
        token = get_token
        response = test.create_order(token, {"ingredients": ["1"]})
        assert response.status_code == 500 and "Internal Server Error" in response.text

    @allure.title("Проверка создания заказа без авторизации")
    def test_create_order_without_auth(self, get_token):
        test = User()
        token = get_token
        response = test.create_order(token, order_data)
        assert response.status_code == 200 and success in response.text
