import pytest
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService

from helpers import _print_info
from data import _browser


@pytest.fixture
def get_browser():
    """ Открываем окно веб-драйвера """
    _print_info(f'BasePage: открываем браузер {_browser} ...')
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
    _print_info(f'\nЗакрываем Веб-драйвер {_browser} ...')
    driver.quit()



@pytest.fixture
def get_chrome_driver():
    """ Открываем окно веб-драйвера """
    _print_info('BasePage: открываем браузер Chrome ...')
    chrome_service = ChromeService(executable_path='C:/WebDriver/bin/chromedriver.exe')
    driver = webdriver.Chrome(service=chrome_service)
    driver.set_window_size(1920,1080)
    #driver = webdriver.Chrome()
    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    _print_info('\nЗакрываем Веб-драйвер ...')
    driver.quit()


@pytest.fixture
def get_firefox_driver():
    """ Открываем окно веб-драйвера """
    _print_info('BasePage: открываем браузер Firefox ...')
    firefox_service = FirefoxService(executable_path='C:/WebDriver/bin/geckodriver.exe')
    driver = webdriver.Firefox(service=firefox_service)
    #firefox_driver.set_window_size(1920,1080)
    #driver = webdriver.Firefox()
    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    _print_info('\nЗакрываем Веб-драйвер ...')
    driver.quit()




