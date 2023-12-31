import requests
import allure

from helpers.common_helpers import _print_info
from data import _to_print

# URL-адрес сервера
__SERVER_URL = 'https://stellarburgers.nomoreparties.site'

# Эндпойнты (ручки) запросов к API
__API_CREATE_USER = '/api/auth/register'  # Регистрация пользователя: POST '/api/auth/register'
__API_LOGIN_USER = '/api/auth/login'      # Авторизация пользователя: POST '/api/auth/login'
#__API_LOGOUT_USER = '/api/auth/logout'    # Выход из системы: POST '/api/auth/logout', body={"token": "{{refreshToken}}"}
__API_DELETE_USER = '/api/auth/user'      # Удаление пользователя: DELETE '/api/auth/user'
                                        # headers={"Authorization": "{auth_token}"}


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


@allure.step('Отправляем API-запрос на удаление пользователя')
def request_on_delete_user(headers):
    request_url = f'{__SERVER_URL}{__API_DELETE_USER}'
    _print_info(f'\nОтправляем запрос на удаление пользователя: DELETE url="{request_url}"\nheaders="{headers}"')
    response = requests.delete(f'{request_url}', headers=headers)
    _print_response(response)
    return response


