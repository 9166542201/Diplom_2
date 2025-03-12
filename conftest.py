import requests
import pytest

import data
import urls


@pytest.fixture
def create_user():
    user = data.generate_user()
    response = requests.post(urls.REGISTER, json=user)
    json = response.json()
    yield user, response.status_code, json
    requests.delete(urls.USER, headers={'authorization': json['accessToken']})
