from test_data import success, login_field_error
from user_methods import User
import pytest

class TestAuthUser(User):
    @pytest.mark.usefixtures('login_delete')
    def test_auth_user(self):
        assert self.response.status_code == 200 and success in self.response.text

    @pytest.mark.usefixtures('create_delete')
    def test_auth_with_incorrect_log_and_pass(self, create_delete):
        user_data = create_delete
        user_data['email'] = 'wrong_email'
        user_data['password'] = 'wrong_password'
        response = self.login_user(user_data)
        assert response.status_code == 401 and login_field_error in response.text