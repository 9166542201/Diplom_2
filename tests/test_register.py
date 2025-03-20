import allure
import pytest
import requests
import data
import json_schemas
import urls
from jsonschema import validate
from data import Responses


class TestRegister:
    @allure.title('Создать уникального пользователя')
    def test_register_valid_data_200(self, create_user):
        user = create_user['user']
        json = create_user['json']
        assert create_user['code'] == 200
        validate(json, json_schemas.AUTH)
        assert (json['success'] == True
                and json['user']['email'] == user['email']
                and json['user']['name'] == user['name'])

    @allure.title('Создать пользователя, который уже зарегистрирован')
    def test_register_existed_user_403(self, create_user):
        user = create_user['user']
        response = requests.post(urls.REGISTER, json=user)
        assert response.status_code == 403
        assert response.json() == Responses.REGISTER_403_0

    @allure.title('Создать пользователя и не заполнить одно из обязательных полей')
    @pytest.mark.parametrize('key', ['email', 'name', 'password'])
    def test_register_empty_field_403(self, key):
        user = data.generate_user()
        del user[key]
        response = requests.post(urls.REGISTER, json=user)
        assert response.status_code == 403
        assert response.json() == Responses.REGISTER_403_1
