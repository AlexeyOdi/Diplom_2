import pytest

from urls import main_url, create_user_url, login_user_url, user_url
from user_generator  import generate_user
import requests

@pytest.fixture(scope="function")
def setup():
    user_data = generate_user()
    requests.post(main_url + create_user_url, data=user_data)
    response = requests.post(main_url + login_user_url, data=user_data)
    yield response
    token = response.json().get("accessToken")
    requests.delete(main_url + user_url, headers={'authorization': token})

@pytest.fixture()
def get_token(setup):
    response = setup
    token = response.json().get("accessToken")
    return token




