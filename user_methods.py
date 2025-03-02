import requests
import allure

from urls import main_url, create_user_url, login_user_url, user_url, order_url


class User:
    @allure.step("Регистрация пользователя")
    def create_user(self, user_data):
        return requests.post(main_url+create_user_url, data=user_data)

    @allure.step("Удаление пользователя")
    def delete_user(self, token):
        return requests.delete(main_url+user_url, headers={'authorization':token})

    @allure.step("Авторизация пользователя")
    def login_user(self, user_data):
        return requests.post(main_url+login_user_url, data=user_data)

    @allure.step("Получение кода ответа")
    def get_status_code(self, response):
        return response.status_code

    @allure.step("Изменение данных")
    def change_data(self, token, change_data):
        return requests.patch(main_url+user_url, headers={'authorization':token}, data=change_data)

    @allure.step("Создание заказа")
    def create_order(self, token, order_data):
        return requests.post(main_url + order_url, data=order_data, headers={'authorization':token})

    @allure.step("Получение заказа")
    def get_orders(self, token):
        return requests.get(main_url+order_url, headers={'authorization':token})