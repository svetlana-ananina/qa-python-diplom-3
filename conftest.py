import allure
import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from helpers.common_helpers import _print_info, _sleep_ff
from data import _browser, RESPONSE_KEYS
from helpers.helpers_on_register_user import generate_random_user_data, try_to_create_user, try_to_delete_user, \
    try_to_login_user
from locators import MainPageLocators, MAIN_PAGE_URL, ProfilePageLocators
from pages.login_page import LoginPage
from pages.main_page import MainPage


#
# Функции для работы с WebDriver
#

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


@allure.step('Регистрируем нового пользователя')
@pytest.fixture
def _user():
    _print_info('conftest::create_new_user: Регистрируем нового пользователя ...')

@allure.title('Создаем нового пользователя через API и авторизуемся на сайте')
@pytest.fixture
def login_new_user(get_browser, create_new_user_by_api):
    # регистрируем нового пользователя
    user_data = create_new_user_by_api
    email = user_data['email']
    password = user_data['password']
    _print_info(f'conftest::register_and_login_new_user: Авторизация нового пользователя\nuser_data = {user_data} ...')
    # Открываем окно веб-браузер
    driver = get_browser
    # открываем страницу авторизации
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.wait_open_login_page()
    # _sleep(5)
    # Вводим email и пароль
    login_page.enter_user_data(email, password)
    _sleep_ff(5)
    # кликаем кнопку "Войти"
    login_page.click_login_button()
    # ждем появления кнопки "Оформить заказ" на Главной странице
    login_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
    #_sleep(5)
    # Проверяем что текущий url это url страницы восстановления пароля
    # assert login_page.get_current_url() == MAIN_PAGE_URL
    # assert MAIN_PAGE_URL in login_page.get_current_url()

    #return driver, email, password
    return driver


@allure.step('Открываем Личный кабинет по ссылке на Главной странице')
@pytest.fixture
def open_profile_page(get_browser, create_new_user_by_api, login_new_user):
    driver = login_new_user
    main_page = MainPage(driver)
    #main_page.open_main_page()
    #main_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
    # _sleep(5)
    # кликаем Личный кабинет в хедере
    #main_page.click_profile_link()
    # ждем перехода в Личный кабинет и появления кнопки "Сохранить"
    #main_page.wait_for_load_element(ProfilePageLocators.SAVE_BUTTON)
    main_page.open_profile_page_by_link()
    # _sleep(5)
    return driver


#
# Функции для работы с API
#
@allure.step('Создаем нового пользователя с помощью API')
@pytest.fixture
def create_new_user_by_api():
    """
    Вспомогательный метод создания и удаления нового пользователя с помощью API
    """
    _print_info('conftest::create_new_user_API: Регистрируем нового пользователя ...')
    # генерируем уникальные данные нового пользователя
    user_data = generate_random_user_data()
    # отправляем запрос на создание пользователя
    response = try_to_create_user(user_data)
    # проверяем что получен код ответа 200
    assert response.status_code == 200, f'Ошибка API: Ошибка регистрации нового пользователя\nuser_data={user_data}\nответ: "{response.text}"'
    # получаем токены пользователя
    received_body = response.json()
    auth_token = received_body[RESPONSE_KEYS.ACCESS_TOKEN]
    refresh_token = received_body[RESPONSE_KEYS.REFRESH_TOKEN]
    #return auth_token, refresh_token
    yield user_data

    _print_info('conftest::create_new_user_API: Удаляем пользователя ...')
    try_to_delete_user(auth_token)


@allure.step('Создаем и авторизуем нового пользователя с помощью API')
@pytest.fixture
def create_and_login_new_user_by_api(create_new_user_by_api):
    """
    Вспомогательный метод создания и удаления нового пользователя с помощью API
    """
    pass


