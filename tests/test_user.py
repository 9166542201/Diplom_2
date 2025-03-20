import allure
import pytest
import requests
import urls
from data import Responses


@pytest.mark.parametrize('key', ['email', 'name', 'password'])
class TestUser:
    @allure.title('Изменение данных пользователя (с авторизацией)')
    def test_patch_valid_data_200(self, create_user, key):
        access_token = create_user['json']['accessToken']
        user = create_user['user']
        user[key] += '1'
        response = requests.patch(urls.USER, json=user, headers={'authorization': access_token})
        assert response.status_code == 200
        json = response.json()
        assert (json['success'] == True
                and json['user']['email'] == user['email']
                and json['user']['name'] == user['name'])

    @allure.title('Изменение данных пользователя (без авторизации)')
    def test_patch_without_authorization_401(self, create_user, key):
        user = create_user['user']
        user[key] += '1'
        response = requests.patch(urls.USER, json=user)
        assert response.status_code == 401
        assert response.json() == Responses.USER_401
