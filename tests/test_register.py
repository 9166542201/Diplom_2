import pytest
import requests
from jsonschema import validate

import data
import json_schemas
import urls


class TestRegister:
    def test_register_valid_data_200(self, create_user):
        user, status_code, json = create_user
        assert status_code == 200
        validate(json, json_schemas.AUTH)
        assert (json['success'] == True
                and json['user']['email'] == user['email']
                and json['user']['name'] == user['name'])

    def test_register_existed_user_403(self, create_user):
        response = requests.post(urls.REGISTER, json=create_user[0])
        assert response.status_code == 403
        assert response.json() == {
            "success": False,
            "message": "User already exists"
        }

    @pytest.mark.parametrize('key', ['email', 'name', 'password'])
    def test_register_empty_field_403(self, key):
        user = data.generate_user()
        del user[key]
        response = requests.post(urls.REGISTER, json=user)
        assert response.status_code == 403
        assert response.json() == {
            "success": False,
            "message": "Email, password and name are required fields"
        }
