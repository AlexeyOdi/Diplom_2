from test_data import email_to_change, success, password_to_change, name_to_change, email_change_error
from tests.conftest import create_delete
from user_methods import User
import pytest

class TestChangeData(User):

    @pytest.mark.usefixtures('login_delete')
    def test_change_email_with_auth(self, login_delete):
        response = self.change_data(login_delete,email_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_change_password_with_auth(self, login_delete):
        response = self.change_data(login_delete, password_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('login_delete')
    def test_change_name_with_auth(self, login_delete):
        response = self.change_data(login_delete, name_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    def test_change_email_without_auth(self):
        response = self.change_data(self.token, email_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    def test_change_password_without_auth(self):
        response = self.change_data(self.token, password_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    def test_change_name_without_auth(self):
        response = self.change_data(self.token, name_to_change)
        assert response.status_code == 200 and success in response.text

    @pytest.mark.usefixtures('create_delete')
    def test_change_email_with_using_email(self, create_delete):
        using_email = {'email':'alex@yandex.ru'}
        print(using_email)
        response = self.change_data(self.token, using_email)
        assert response.status_code == 403 and email_change_error in response.text



