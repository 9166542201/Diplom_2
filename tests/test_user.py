import pytest
import requests

import urls


@pytest.mark.parametrize('key', ['email', 'name', 'password'])
class TestUser:
    def test_patch_valid_data_200(self, create_user, key):
        user, status_code, json = create_user
        user[key] += '1'
        response = requests.patch(urls.USER, json=user, headers={'authorization': json['accessToken']})
        assert response.status_code == 200
        json = response.json()
        assert (json['success'] == True
                and json['user']['email'] == user['email']
                and json['user']['name'] == user['name'])

    def test_patch_without_authorization_401(self, create_user, key):
        user, status_code, json = create_user
        user[key] += '1'
        response = requests.patch(urls.USER, json=user)
        assert response.status_code == 401
        assert response.json() == {
            "success": False,
            "message": "You should be authorised"
        }
