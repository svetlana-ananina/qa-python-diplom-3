import requests
import allure

from helpers.common_helpers import _print_info
from data import _to_print

# URL-адрес сервера
__SERVER_URL = 'https://stellarburgers.nomoreparties.site'

# Эндпойнты (ручки) запросов к API
__API_CREATE_USER = '/api/auth/register'    # Регистрация пользователя: POST '/api/auth/register'
__API_LOGIN_USER = '/api/auth/login'        # Авторизация пользователя: POST '/api/auth/login'
#__API_LOGOUT_USER = '/api/auth/logout'     # Выход из системы: POST '/api/auth/logout', body={"token": "{{refreshToken}}"}
__API_DELETE_USER = '/api/auth/user'        # Удаление пользователя: DELETE '/api/auth/user'
                                            # headers={"Authorization": "{auth_token}"}
__GET_INGREDIENTS = '/api/ingredients'      # GET '/api/ingredients'
                                            # ответ: {'success': True, 'data': [{...}, ... ]
__CREATE_ORDER = '/api/orders'              # POST '/api/orders', payload={ "ingredients": ["...","...", ...] }
                                            # ответ: { "name": "...","order": { "number": 6257 }, "success": true }
__GET_USER_ORDERS = '/api/orders'           # GET '/api/orders' (50 последних заказов)



def _print_response(response):
    if _to_print:
        print(f'response="{response}", response.text="{response.text}"')


@allure.step('Отправляем API-запрос на создание пользователя')
def request_on_create_user(payload):
    request_url = f'{__SERVER_URL}{__API_CREATE_USER}'
    _print_info(f'\nОтправляем запрос на создание пользователя: POST url="{request_url}"\njson="{payload}"')
    response = requests.post(f'{request_url}', json=payload)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на авторизацию пользователя')
def request_on_login_user(payload):
    request_url = f'{__SERVER_URL}{__API_LOGIN_USER}'
    _print_info(f'\nОтправляем запрос на авторизацию пользователя: POST url="{request_url}"\njson="{payload}"')
    response = requests.post(f'{request_url}', json=payload)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на удаление пользователя')
def request_on_delete_user(headers):
    request_url = f'{__SERVER_URL}{__API_DELETE_USER}'
    _print_info(f'\nОтправляем запрос на удаление пользователя: DELETE url="{request_url}"\nheaders="{headers}"')
    response = requests.delete(f'{request_url}', headers=headers)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на получение ингредиентов')
def request_on_get_ingredients():
    request_url = f'{__SERVER_URL}{__GET_INGREDIENTS}'
    _print_info(f'\nОтправляем запрос на получение ингредиентов: GET url="{request_url}"')
    response = requests.get(f'{request_url}')
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на создание заказа')
def request_on_create_order(payload,  headers=None):
    request_url = f'{__SERVER_URL}{__CREATE_ORDER}'
    _print_info(f'\nОтправляем запрос на создание заказа: POST url="{request_url}"\nheaders="{headers}"\njson="{payload}"')
    response = requests.post(f'{request_url}', headers=headers, json=payload)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на получение заказов пользователя')
def request_on_get_user_orders(headers=None):
    request_url = f'{__SERVER_URL}{__GET_USER_ORDERS}'
    _print_info(f'\nОтправляем запрос на получение заказов пользователя: GET url="{request_url}"\nheaders="{headers}"')
    response = requests.get(f'{request_url}', headers=headers)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на создание заказа')
def request_on_create_order(payload,  headers=None):
    request_url = f'{__SERVER_URL}{__CREATE_ORDER}'
    _print_info(f'\nОтправляем запрос на создание заказа: POST url="{request_url}"\nheaders="{headers}"\njson="{payload}"')
    #if headers is not None:
    #    response = requests.post(f'{request_url}', headers=headers, json=payload)
    #else:
    #    response = requests.post(f'{request_url}', json=payload)
    response = requests.post(f'{request_url}', headers=headers, json=payload)
    _print_response(response)
    return response


@allure.step('Отправляем API-запрос на получение заказов пользователя')
def request_on_get_user_orders(headers=None):
    request_url = f'{__SERVER_URL}{__GET_USER_ORDERS}'
    _print_info(f'\nОтправляем запрос на получение заказов пользователя: GET url="{request_url}"\nheaders="{headers}"')
    response = requests.get(f'{request_url}', headers=headers)
    _print_response(response)
    return response

