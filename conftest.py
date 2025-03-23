import requests
import pytest

import data
import urls


@pytest.fixture
def create_user():
    user = data.generate_user()
    response = requests.post(urls.REGISTER, json=user)
    json = response.json()
    if response.status_code != 200:
        raise RuntimeError(f"user creation failure {response.status_code}")
    yield {'user': user, 'code': response.status_code, 'json': json}
    response = requests.delete(urls.USER, headers={'authorization': json['accessToken']})
    if response.status_code != 202:
        raise RuntimeError(f"user deletion failure {response.status_code}")
