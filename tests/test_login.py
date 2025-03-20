import allure
import pytest
import requests
import json_schemas
import urls
from jsonschema import validate
from data import Responses


class TestLogin:
    @allure.title('Логин под существующим пользователем')
    def test_login_valid_data_200(self, create_user):
        user = create_user['user']
        response = requests.post(urls.LOGIN, json=user)
        assert response.status_code == 200
        json = response.json()
        validate(json, json_schemas.AUTH)
        assert (json['success'] == True
                and json['user']['email'] == user['email']
                and json['user']['name'] == user['name'])

    @allure.title('Логин с неверным логином и паролем')
    @pytest.mark.parametrize('key', ['email', 'password'])
    def test_login_invalid_data_401(self, key, create_user):
        user = create_user['user']
        user[key] += '1'
        response = requests.post(urls.LOGIN, json=user)
        assert response.status_code == 401
        assert response.json() == Responses.LOGIN_401
