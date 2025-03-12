import pytest
import requests
from jsonschema import validate

import json_schemas
import urls


class TestLogin:
    def test_login_valid_data_200(self, create_user):
        user = create_user[0]
        response = requests.post(urls.LOGIN, json=user)
        assert response.status_code == 200
        json = response.json()
        validate(json, json_schemas.AUTH)
        assert (json['success'] == True
                and json['user']['email'] == user['email']
                and json['user']['name'] == user['name'])

    @pytest.mark.parametrize('key', ['email', 'password'])
    def test_login_invalid_data_401(self, key, create_user):
        user = create_user[0]
        user[key] += '1'
        response = requests.post(urls.LOGIN, json=user)
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "email or password are incorrect"
        }
