import requests
from jsonschema import validate

import urls
import json_schemas


class TestOrders:

    def test_get_ingredients_200(self):
        response = requests.get(urls.INGREDIENTS)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0

    def test_create_order_valid_ingredients_200(self, create_user):
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        response = requests.post(urls.ORDERS, headers={'authorization': create_user[2]['accessToken']},
                                 json={'ingredients': [ingredient]})
        assert response.status_code == 200
        json = response.json()
        validate(json, json_schemas.MAKE_ORDERS)
        assert json['success'] == True

    def test_create_order_valid_ingredients_no_auth_200(self, create_user):
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        response = requests.post(urls.ORDERS, json={'ingredients': [ingredient]})
        assert response.status_code == 200
        json = response.json()
        assert json['success'] == True

    def test_create_order_invalid_ingredient_500(self, create_user):
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        response = requests.post(urls.ORDERS, headers={'authorization': create_user[2]['accessToken']},
                                 json={'ingredients': [ingredient + '1']})
        assert response.status_code == 500

    def test_create_order_empty_ingredients_400(self, create_user):
        response = requests.post(urls.ORDERS, headers={'authorization': create_user[2]['accessToken']},
                                 json={"ingredients": []})
        assert response.status_code == 400
        assert response.json() == {"success": False,
                                   "message": "Ingredient ids must be provided"
                                   }

    def test_get_orders_200(self, create_user):
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        requests.post(urls.ORDERS, headers={'authorization': create_user[2]['accessToken']},
                      json={'ingredients': [ingredient]})
        response = requests.get(urls.ORDERS, headers={'authorization': create_user[2]['accessToken']})
        assert response.status_code == 200
        json = response.json()
        validate(json, json_schemas.GET_ORDERS)
        assert json['success'] == True and json['orders'][0]['ingredients'] == [ingredient]

    def test_get_orders_no_auth_401(self, create_user):
        response = requests.get(urls.ORDERS)
        assert response.status_code == 401
        assert response.json() == {"success": False,
                                   "message": "You should be authorised"
                                   }
