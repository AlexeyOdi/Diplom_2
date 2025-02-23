from test_data import success
from user_methods import User
import pytest

class TestGetOrders(User):
    @pytest.mark.usefixtures('create_delete')
    def test_get_unauth_user_order(self):
        response = self.get_orders(self.token)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_get_auth_user_order(self, login_delete):
        response = self.get_orders(login_delete)
        assert response.status_code == 200 and success in response.text
