import allure
import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from helpers.common_helpers import _print_info
from data import _browser, STATUS_CODES, RESPONSE_KEYS
from helpers.helpers_on_register_user import generate_random_user_data, try_to_create_user, try_to_delete_user


@pytest.fixture
def get_browser():
    """ Открываем окно веб-драйвера """
    _print_info(f'conftest::get_browser: открываем браузер {_browser} ...')
    if _browser == 'Chrome':
        chrome_service = ChromeService(executable_path='C:/WebDriver/bin/chromedriver.exe')
        driver = webdriver.Chrome(service=chrome_service)
        #driver.set_window_size(1920, 1080)
        driver.maximize_window()
    else:
        firefox_service = FirefoxService(executable_path='C:/WebDriver/bin/geckodriver.exe')
        driver = webdriver.Firefox(service=firefox_service)
        driver.maximize_window()
    yield driver

    # Закрываем драйвер по окончании использования
    _print_info(f'\nconftest::get_browser: Закрываем Веб-драйвер {_browser} ...')
    driver.quit()


@pytest.fixture
def get_chrome_driver():
    """ Открываем окно веб-драйвера """
    _print_info('conftest::get_browser: открываем браузер Chrome ...')
    chrome_service = ChromeService(executable_path='C:/WebDriver/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service)
    driver.set_window_size(1920,1080)
    #driver = webdriver.Chrome()
    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    _print_info('\nconftest::get_browser: Закрываем Веб-драйвер ...')
    driver.quit()


@pytest.fixture
def get_firefox_driver():
    """ Открываем окно веб-драйвера """
    _print_info('conftest::get_browser: открываем браузер Firefox ...')
    firefox_service = FirefoxService(executable_path='C:/WebDriver/bin/geckodriver.exe')
    driver = webdriver.Firefox(service=firefox_service)
    #firefox_driver.set_window_size(1920,1080)
    #driver = webdriver.Firefox()
    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    _print_info('\nconftest::get_browser: Закрываем Веб-драйвер ...')
    driver.quit()


# вспомогательный метод создания и удаления нового пользователя
@allure.step('Создаем нового пользователя')
@pytest.fixture
def create_new_user():
    _print_info('conftest::create_new_user: Регистрируем нового пользователя ...')
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
    #return auth_token, refresh_token
    yield user_data

    _print_info('conftest::create_new_user: Удаляем пользователя ...')
    try_to_delete_user(auth_token)
