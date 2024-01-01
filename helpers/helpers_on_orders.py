import allure
import pytest

from helpers.common_helpers import _print_info
from helpers.helpers_on_requests import request_on_create_order, request_on_get_user_orders


# Вспомогательные методы для работы с заказами
@allure.step('Отправляем запрос на создание заказа')
def try_to_create_order(ingredient_list, auth_token=None):      # ingredient_list - список _id ингредиентов
    _print_info('\nСоздаем заказ ...')
    if auth_token is not None:
        headers = {
            'Authorization': auth_token,
        }
    else:
        headers = None

    payload = {
        'ingredients': ingredient_list,                         #"ingredients": ingredient_list,
    }
    response = request_on_create_order(payload, headers)
    return response


@allure.step('Создаем заказ и проверяем полученные в ответе данные')
def create_order(ingredient_list, auth_token=None):
    # создаем заказ
    response = try_to_create_order(ingredient_list, auth_token)
    # проверяем что получен код ответа 200
    assert response.status_code == 200, f'Ошибка API: Ошибка создания заказа\nполучено: "{response.text}"'
    # Получаем данные заказа - name, number
    order_name = response.json()['name']                #KEYS.NAME_KEY)
    order_data = response.json()['order']               #check_key_in_body(received_body, KEYS.ORDER_KEY)
    order_number = order_data['number']                 #check_key_in_body(received_order_data, KEYS.NUMBER_KEY)

    return order_number, order_name


@allure.step('Отправляем запрос на получение заказов пользователя')
def try_to_get_user_orders(auth_token=None):
    _print_info('\nПолучаем заказы пользователя ...')
    if auth_token is not None:
        headers = {
            'Authorization': auth_token,
        }
    else:
        headers = None
    response = request_on_get_user_orders(headers)
    return response


