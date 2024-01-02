import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains

from helpers.common_helpers import _print_info


class BasePage:
    """ Базовый класс для классов страниц - Главной страницы и страницы заказа """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по URL')
    def open_page(self, page_url):
        """ Открываем страницу по URL {page_url} """
        _print_info(f'\nBasePage: открываем страницу  ...{page_url}')
        return self.driver.get(page_url)

    @allure.step('Ждем загрузку элемента HTML по локатору')
    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Ждем открытие страницы при переходе по ссылке URL')
    def wait_for_open_page(self, page_url):
        """ Ждем открытие страницы при переходе по ссылке: {self.page_url} """
        return WebDriverWait(self.driver, 10).until(
                    EC.url_to_be(page_url))

    @allure.step('Ждем загрузку всех элементов HTML по локатору')
    def wait_for_load_all_elements(self, locator):
        """ Ждем загрузку всех элементов HTML по локатору {locator} """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator))

    @allure.step('Ждем появление в DOM элемента HTML по локатору')
    def wait_for_presence_of_element(self, locator):
        """ Ждем появление в DOM элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator))

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        """ Получаем текущий url """
        #url = self.driver.current_url
        return self.driver.current_url

    @allure.step('Получаем заголовок окна')
    def get_title(self):
        """ Получаем заголовок страницы """
        #title = self.driver.current_url
        return self.driver.title

    @allure.step('Ищем элемент HTML по локатору')
    def find_element(self, locator):
        """ Ищем элемент HTML по локатору {locator} """
        return self.driver.find_element(*locator)

    @allure.step('Ищем все элементы HTML по локатору')
    def find_all_elements(self, locator):
        """ Ищем все элементы HTML по локатору {locator} """
        return self.driver.find_elements(*locator)

    @allure.step('Ждем кликабельности элемента по локатору')
    def wait_for_clickable_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Вводим текст в поле по локатору')
    def set_value(self, locator, value):
        """ Вводим текст в поле по локатору: {locator} """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).send_keys(value)
        #self.driver.find_element(*locator).send_keys(value)

    @allure.step('Получаем значение поля по локатору')
    def check_value(self, locator):
        """ Получаем значение поля по локатору: {locator} """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).get_attribute("value")
        #return self.driver.find_element(*locator).get_attribute("value")

    @allure.step('Получаем текст в поле по локатору')
    def check_text(self, locator):
        """ Получаем текст в поле по локатору: {locator} """
        return self.driver.find_element(*locator).text

    @allure.step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element_by_locator(self, locator):
        """ Прокручиваем страницу до элемента по локатору {locator} """
        #element = self.driver.find_element(*locator)
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element(self, element):
        """ Прокручиваем страницу до элемента по локатору {locator} """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return element

    @allure.step('Ждем видимости элемента по локатору и кликаем')
    def click_element_by_locator(self, locator):
        """ Ждем загрузку элемента HTML по локатору и кликаем """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)).click()
        #self.driver.find_element(*locator).click()

    @allure.step('Ждем кликабельности элемента по локатору и кликаем')
    def click_element_by_locator_when_clickable(self, locator):
        """ Ждем загрузку элемента HTML по локатору и кликаем """
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator))
        #self.driver.find_element(*locator).click()
        element.click()

    @allure.step('Кликаем элемент')
    def click_element(self, element):
        """ Кликаем элемент """
        element.click()

    @allure.step('Перемещаем элемент')
    def drag_and_drop(self, source, target):
        """ Кликаем элемент """
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).perform()


