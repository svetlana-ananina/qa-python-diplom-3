import allure
import pytest
import time
import random
import string

import requests
import allure

from data import _to_print, _to_sleep, _to_sleep_ff
from helpers.common_helpers import _print_info
from helpers.helpers_on_requests import request_on_create_user, request_on_delete_user, request_on_login_user


# Вспомогательные функции
# генерируем логин, пароль и имя пользователя
@allure.step('Генерируем данные нового пользователя: email, password, name')
def generate_random_user_data():
    email = generate_random_string(10)+'@mail.ru'
    password = generate_random_string(10)
    name = generate_random_string(10)
    # собираем тело запроса
    user_data = {
        'email': email,            # "email"
        'password': password,      # "password"
        'name': name               # "name"
    }
    # возвращаем словарь
    return user_data


def generate_random_string(length):
    """
    Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки.
    :param length: (int) длина строки
    :return: (str) строка
    """
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


#@allure.step('Генерируем новое имя пользователя: поле "name"')
def generate_random_user_name():
    return generate_random_string(10)


#@allure.step('Генерируем email пользователя: поле "email"')
def generate_random_user_login():
    return generate_random_string(10)+'@mail.ru'


#@allure.step('Генерируем пароль пользователя: поле "password"')
def generate_random_user_password():
    return generate_random_string(6)


# вспомогательный метод создания нового пользователя для других тестов
@allure.step('Создаем нового пользователя')
def create_user():
    # генерируем уникальные данные нового пользователя
    user_data = generate_random_user_data()
    # отправляем запрос на создание пользователя
    response = try_to_create_user(user_data)
    # проверяем что получен код ответа 200
    assert response.status_code == 200, f'Ошибка API: Ошибка регистрации нового пользователя\nuser_data={user_data}\nответ: "{response.text}"'
    # получаем токены пользователя
    received_body = response.json()
    auth_token = received_body['accessToken']
    refresh_token = received_body['refreshToken']
    return auth_token, refresh_token


@allure.step('Отправляем запрос на создание нового пользователя')
def try_to_create_user(user_data):
    _print_info('\nСоздаем/регистрируем нового пользователя ...')
    response = request_on_create_user(user_data)
    return response


@allure.step('Удаляем пользователя')
def try_to_delete_user(auth_token):
    _print_info('\nУдаляем пользователя ...')
    headers = {'Authorization': auth_token}
    response = request_on_delete_user(headers)
    return response


@allure.step('Авторизация пользователя')
def try_to_login_user(email, password):
    _print_info('\nАвторизация пользователя ...')
    payload = {'email': email, 'password': password}
    response = request_on_login_user(payload)
    return response

