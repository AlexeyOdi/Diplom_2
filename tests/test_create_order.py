from test_data import order_data, success, ingr_error
from user_methods import User
import pytest

class TestCreateOrder(User):
    @pytest.mark.usefixtures('login_delete')
    def test_create_order_with_auth(self, login_delete):
        token = login_delete
        response = self.create_order(token,order_data)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_create_order_with_ingr(self, login_delete):
        token = login_delete
        response = self.create_order(token, order_data)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_create_order_without_ingr(self, login_delete):
        token = login_delete
        response = self.create_order(token, {"ingredients": []})
        assert response.status_code == 400 and ingr_error in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_create_order_with_unexist_ingr(self, login_delete):
        token = login_delete
        response = self.create_order(token, {"ingredients": ["1"]})
        assert response.status_code == 500 and "Internal Server Error" in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_create_order_without_auth(self, login_delete):
        token = None
        response = self.create_order(token, order_data)
        assert response.status_code == 200 and success in response.text
