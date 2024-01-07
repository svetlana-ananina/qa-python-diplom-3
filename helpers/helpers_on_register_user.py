import allure
import pytest
import random
import requests
import string
import time

from data import _to_print, _to_sleep, _to_sleep_ff
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

