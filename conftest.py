import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from data import _browser, RESPONSE_KEYS
from helpers.helpers_on_register_user import HelpersOnRegisterUser as u
from locators import MainPageLocators
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


import time
from data import _to_print, _to_sleep, _to_sleep_ff


# Логирование - вывод в <stdout>
def print_value(name, value):
    if _to_print:
        print(f'{name}="{value}"')


def print_info(info_str):
    if _to_print:
        print(info_str)


def sleep(amount=10):
    if _to_sleep:
        time.sleep(amount)


def sleep_ff(amount=10):
    if _to_sleep_ff:
        time.sleep(amount)

#
# Функции для работы с WebDriver
#

@allure.title('Открываем окно веб-браузера')
@pytest.fixture
def get_browser():
    """ Открываем окно веб-драйвера """
    print_info('\nget_browser: открываем окно браузера ...')
    if _browser == 'Chrome':
        chrome_service = ChromeService(executable_path='C:/WebDriver/bin/chromedriver.exe')     # WEBDRIVER_PATH
        driver = webdriver.Chrome(service=chrome_service)

        #driver = webdriver.Chrome()

        driver.set_window_size(1920, 1080)
        driver.maximize_window()
    else:
        firefox_service = FirefoxService(executable_path='C:/WebDriver/bin/geckodriver.exe')
        driver = webdriver.Firefox(service=firefox_service)
        #driver = webdriver.Firefox()
        driver.maximize_window()
    yield driver

    # Закрываем драйвер по окончании использования
    driver.quit()


@allure.title('Создаем нового пользователя через API и авторизуемся на сайте')
@pytest.fixture
def login_new_user(get_browser, create_new_user_by_api):
    print_info('\nlogin_new_user: регистрируем нового пользователя ...')
    # регистрируем нового пользователя
    user_data = create_new_user_by_api
    email = user_data['email']
    password = user_data['password']
    # Открываем окно веб-браузер
    driver = get_browser
    # открываем страницу авторизации
    login_page = LoginPage(driver)
    login_page.open_login_page()
    # Вводим email и пароль
    login_page.enter_user_data(email, password)
    # кликаем кнопку "Войти"
    login_page.click_login_button()
    # ждем появления кнопки "Оформить заказ" на Главной странице
    login_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
    return driver


@allure.title('Создаем заказ для авторизованного пользователя')
@pytest.fixture
def create_order(get_browser, create_new_user_by_api, login_new_user):
    print_info('\ncreate_order: Создаем заказ ...')
    # Открываем окно веб-браузер
    driver = get_browser
    # открываем конструктор
    constructor_page = ConstructorPage(driver)
    # оформляем заказ
    order = constructor_page.create_order()
    return order


#
# Функции для работы с API
#
@allure.title('Создаем нового пользователя с помощью API')
@pytest.fixture
def create_new_user_by_api():
    """
    Вспомогательный метод создания и удаления нового пользователя с помощью API
    """
    # генерируем уникальные данные нового пользователя
    user_data = u.generate_random_user_data()
    # отправляем запрос на создание пользователя
    response = u.try_to_create_user(user_data)
    # получаем токены пользователя
    received_body = response.json()
    auth_token = received_body[RESPONSE_KEYS.ACCESS_TOKEN]
    yield user_data

    # удаляем пользователя
    u.try_to_delete_user(auth_token)

