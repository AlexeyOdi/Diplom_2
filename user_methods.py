import requests

from urls import main_url, create_user_url, login_user_url, user_url, order_url


class User:
    def create_user(self, user_data):
        return requests.post(main_url+create_user_url, data=user_data)

    def delete_user(self, token):
        return requests.delete(main_url+user_url, headers={'authorization':token})

    def login_user(self, user_data):
        return requests.post(main_url+login_user_url, data=user_data)

    def get_status_code(self, response):
        return response.status_code

    def change_data(self, token, change_data):
        return requests.patch(main_url+user_url, headers={'authorization':token}, data=change_data)

    def create_order(self, token, order_data):
        return requests.post(main_url + order_url, data=order_data, headers={'authorization':token})

    def get_orders(self, token):
        return requests.get(main_url+order_url, headers={'authorization':token})