import allure
import pytest
import time
import random
import string

import requests
import allure

from data import _to_print, _to_sleep, _to_sleep_ff, STATUS_CODES, RESPONSE_KEYS
from helpers.common_helpers import _print_info
from helpers.helpers_on_requests import request_on_create_user, request_on_delete_user


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


#@allure.step('Выполняем регистрацмю нового пользователя')
#def register_new_user(email, password):
#    pass


# вспомогательный метод создания нового пользователя для других тестов
#@allure.step('Проверяем код ответа')
#def check_status_code(response, expected_code):
#    # проверяем что получен код ответа expected_code
#    received_code = response.status_code
#    assert received_code == expected_code, f'Ошибка API: Неверный код в ответе, ожидался {expected_code}, получен "{received_code}"\nответ: "{response.text}"'


# вспомогательный метод создания нового пользователя для других тестов
@allure.step('Создаем нового пользователя')
def create_user():
    # генерируем уникальные данные нового пользователя
    user_data = generate_random_user_data()
    # отправляем запрос на создание пользователя
    response = try_to_create_user(user_data)
    # проверяем что получен код ответа 200
    #check_status_code(response, STATUS_CODES.OK)
    assert response.status_code == STATUS_CODES.OK, f'Ошибка API: Ошибка регистрации нового пользователя\nuser_data={user_data}\nответ: "{response.text}"'
    # получаем токены пользователя
    received_body = response.json()
    auth_token = received_body[RESPONSE_KEYS.ACCESS_TOKEN]
    refresh_token = received_body[RESPONSE_KEYS.REFRESH_TOKEN]
    return auth_token, refresh_token


@allure.step('Отправляем запрос на создание нового пользователя')
def try_to_create_user(user_data):
    _print_info('\nСоздаем/регистрируем нового пользователя ...')
    response = request_on_create_user(user_data)
    return response


@allure.step('Удаляем пользователя')
def try_to_delete_user(auth_token):
    _print_info('\nУдаляем пользователя ...')
    headers = {RESPONSE_KEYS.AUTH_TOKEN_KEY: auth_token}
    response = request_on_delete_user(headers)
    return response

