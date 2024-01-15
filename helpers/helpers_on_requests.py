import allure
import requests


class ApiData:
    # URL-адрес сервера
    SERVER_URL = 'https://stellarburgers.nomoreparties.site'

    # Эндпойнты (ручки) запросов к API
    API_CREATE_USER = '/api/auth/register'  # Регистрация пользователя: POST '/api/auth/register'
    API_DELETE_USER = '/api/auth/user'  # Удаление пользователя: DELETE '/api/auth/user'
    # headers={"Authorization": "{auth_token}"}


class HelpersOnRequests:

    @staticmethod
    @allure.step('Отправляем API-запрос на создание пользователя')
    def request_on_create_user(payload):
        request_url = f'{ApiData.SERVER_URL}{ApiData.API_CREATE_USER}'
        response = requests.post(f'{request_url}', json=payload)
        return response

    @staticmethod
    @allure.step('Отправляем API-запрос на удаление пользователя')
    def request_on_delete_user(headers):
        request_url = f'{ApiData.SERVER_URL}{ApiData.API_DELETE_USER}'
        response = requests.delete(f'{request_url}', headers=headers)
        return response

