import allure
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import _print_info


class BasePage:
    """ Базовый класс для классов страниц - Главной страницы и страницы заказа """

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, page_url):
        """ Открываем страницу по URL {page_url} """
        _print_info(f'\nBasePage: открываем страницу  ...{page_url}')
        self.driver.get(page_url)

    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator))

    def wait_for_open_page(self, page_url):
        """ Ждем открытие страницы при переходе по ссылке: {self.page_url} """
        return WebDriverWait(self.driver, 10).until(
                    expected_conditions.url_to_be(page_url))

    def wait_for_load_all_elements(self, locator):
        """ Ждем загрузку всех элементов HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_all_elements_located(locator))

    def wait_for_presence_of_element(self, locator):
        """ Ждем появление в DOM элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))

    def get_current_url(self):
        """ Получаем текущий url """
        #url = self.driver.current_url
        return self.driver.current_url

    def get_title(self):
        """ Получаем текущий url """
        #title = self.driver.current_url
        return self.driver.title

    def find_element(self, locator):
        """ Ищем элемент HTML по локатору {locator} """
        return self.driver.find_element(*locator)

    def find_all_elements(self, locator):
        """ Ищем все элементы HTML по локатору {locator} """
        return self.driver.find_elements(*locator)

    def click_element(self, locator):
        """ Кликаем элемент по локатору {locator} """
        self.driver.find_element(*locator).click()

    def wait_for_clickable_element(self, locator):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))

    def set_value(self, locator, value):
        """ Вводим текст в поле по локатору: {locator} """
        self.driver.find_element(*locator).send_keys(value)

    def check_value(self, locator):
        """ Получаем значение поля по локатору: {locator} """
        return self.driver.find_element(*locator).get_attribute("value")

    def check_text(self, locator):
        """ Получаем текст в поле по локатору: {locator} """
        return self.driver.find_element(*locator).text

    @allure.step('Прокручиваем страницу до элемента по локатору {locator}')
    def scroll_to_element(self, locator):
        """ Прокручиваем страницу до элемента по локатору {locator} """
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)




