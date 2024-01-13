import allure
import requests

from data import _to_print
from helpers.common_helpers import _print_info


def _print_response(response):
    if _to_print:
        print(f'response="{response}", response.text="{response.text}"')


class ApiData:
    # URL-адрес сервера
    SERVER_URL = 'https://stellarburgers.nomoreparties.site'

    # Эндпойнты (ручки) запросов к API
    API_CREATE_USER = '/api/auth/register'  # Регистрация пользователя: POST '/api/auth/register'
    API_DELETE_USER = '/api/auth/user'  # Удаление пользователя: DELETE '/api/auth/user'
    # headers={"Authorization": "{auth_token}"}


class HelpersOnRequests:

    @allure.step('Отправляем API-запрос на создание пользователя')
    def request_on_create_user(self, payload):
        request_url = f'{ApiData.SERVER_URL}{ApiData.API_CREATE_USER}'
        response = requests.post(f'{request_url}', json=payload)
        _print_response(response)
        return response

    @allure.step('Отправляем API-запрос на удаление пользователя')
    def request_on_delete_user(self, headers):
        request_url = f'{ApiData.SERVER_URL}{ApiData.API_DELETE_USER}'
        response = requests.delete(f'{request_url}', headers=headers)
        _print_response(response)
        return response

