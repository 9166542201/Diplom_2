import allure
import requests
from jsonschema import validate
import urls
import json_schemas
from data import Responses


class TestOrders:

    @allure.title('Получить все ингредиенты')
    def test_get_ingredients_200(self):
        response = requests.get(urls.INGREDIENTS)
        assert response.status_code == 200
        assert len(response.json()['data']) > 0

    @allure.title('Создать заказ (с авторизацией, с ингредиентами)')
    def test_create_order_valid_ingredients_200(self, create_user):
        access_token = create_user['json']['accessToken']
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        response = requests.post(urls.ORDERS, headers={'authorization': access_token},
                                 json={'ingredients': [ingredient]})
        assert response.status_code == 200
        json = response.json()
        validate(json, json_schemas.MAKE_ORDERS)
        assert json['success'] == True

    @allure.title('Создать заказ (без авторизации, с ингредиентами)')
    def test_create_order_valid_ingredients_no_auth_200(self):
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        response = requests.post(urls.ORDERS, json={'ingredients': [ingredient]})
        assert response.status_code == 200
        json = response.json()
        assert json['success'] == True

    @allure.title('Создать заказ (с авторизацией, с неверным хешем ингредиентов)')
    def test_create_order_invalid_ingredient_500(self, create_user):
        access_token = create_user['json']['accessToken']
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        response = requests.post(urls.ORDERS, headers={'authorization': access_token},
                                 json={'ingredients': [ingredient + '1']})
        assert response.status_code == 500

    @allure.title('Создать заказ (с авторизацией, без ингредиентов)')
    def test_create_order_empty_ingredients_400(self, create_user):
        access_token = create_user['json']['accessToken']
        response = requests.post(urls.ORDERS, headers={'authorization': access_token},
                                 json={"ingredients": []})
        assert response.status_code == 400
        assert response.json() == Responses.ORDERS_400

    @allure.title('Получить заказы пользователя (с авторизацией)')
    def test_get_orders_200(self, create_user):
        access_token = create_user['json']['accessToken']
        ingredient = requests.get(urls.INGREDIENTS).json()['data'][0]['_id']
        requests.post(urls.ORDERS, headers={'authorization': access_token},
                      json={'ingredients': [ingredient]})
        response = requests.get(urls.ORDERS, headers={'authorization': access_token})
        assert response.status_code == 200
        json = response.json()
        validate(json, json_schemas.GET_ORDERS)
        assert json['success'] == True and json['orders'][0]['ingredients'] == [ingredient]

    @allure.title('Получить заказы пользователя (без авторизации)')
    def test_get_orders_no_auth_401(self):
        response = requests.get(urls.ORDERS)
        assert response.status_code == 401
        assert response.json() == Responses.ORDERS_401
