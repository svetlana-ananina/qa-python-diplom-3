import allure
import random
import string

from helpers.helpers_on_requests import HelpersOnRequests as hr


# Вспомогательные функции для регистрации/удаления пользователя с помощью API
# генерируем логин, пароль и имя пользователя
class HelpersOnRegisterUser:

    @staticmethod
    @allure.step('Генерируем данные нового пользователя: email, password, name')
    def generate_random_user_data():
        email = HelpersOnRegisterUser.generate_random_string(10) + '@mail.ru'
        password = HelpersOnRegisterUser.generate_random_string(10)
        name = HelpersOnRegisterUser.generate_random_string(10)
        # собираем тело запроса
        user_data = {
            'email': email,         # "email"
            'password': password,   # "password"
            'name': name            # "name"
        }
        # возвращаем словарь
        return user_data

    @staticmethod
    def generate_random_string(length):
        """
        Метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки.
        :param length: (int) длина строки
        :return: (str) строка
        """
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Отправляем запрос на создание нового пользователя')
    def try_to_create_user(user_data):
        response = hr.request_on_create_user(user_data)
        return response

    @staticmethod
    @allure.step('Удаляем пользователя')
    def try_to_delete_user(auth_token):
        headers = {'Authorization': auth_token}
        response = hr.request_on_delete_user(headers)
        return response

