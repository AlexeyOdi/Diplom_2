import pytest

from urls import main_url, create_user_url, login_user_url, user_url
from user_generator  import generate_user
import requests

@pytest.fixture(scope = "function")
def create_delete(request):
    user_data = generate_user()
    response = requests.post(main_url+create_user_url, data=user_data)
    request.cls.response = response
    token = response.json().get("accessToken")
    request.cls.token = token
    yield user_data
    requests.delete(main_url+user_url, headers={'authorization':token})

@pytest.fixture(scope="function")
def login_delete(request):
    user_data = generate_user()
    requests.post(main_url + create_user_url, data=user_data)
    response = requests.post(main_url + login_user_url, data=user_data)
    request.cls.response = response
    token = response.json().get("accessToken")
    yield token
    requests.delete(main_url + user_url, headers={'authorization': token})