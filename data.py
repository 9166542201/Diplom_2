import random
import string


def generate_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    return {
        "email": generate_random_string(10) + '@cvn.ru',
        "password": generate_random_string(10),
        "name": generate_random_string(10)
    }


class Responses:
    LOGIN_401 = {
        "success": False,
        "message": "email or password are incorrect"
    }
    ORDERS_400 = {
        "success": False,
        "message": "Ingredient ids must be provided"
    }
    ORDERS_401 = {
        "success": False,
        "message": "You should be authorised"
    }
    USER_401 = {
        "success": False,
        "message": "You should be authorised"
    }
    REGISTER_403_0 = {
        "success": False,
        "message": "User already exists"
    }
    REGISTER_403_1 = {
        "success": False,
        "message": "Email, password and name are required fields"
    }
