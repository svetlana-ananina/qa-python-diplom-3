import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains


class BasePage:
    """ Базовый класс для классов страниц - Главной страницы и страницы заказа """

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу по URL')
    def open_page(self, page_url):
        """ Открываем страницу по URL {page_url} """
        return self.driver.get(page_url)

    @allure.step('Ждем загрузку элемента HTML по локатору')
    def wait_for_load_element(self, locator):
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator))

    @allure.step('Ждем пока текст элемента HTML по локатору будет отличаться от значения')
    def wait_for_changed_text(self, locator, text_value):           # Bool
        """ Ждем загрузку элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.none_of(EC.text_to_be_present_in_element(locator, text_value)))

    @allure.step('Ждем открытие страницы при переходе по ссылке URL')
    def wait_for_open_page(self, page_url):
        """ Ждем открытие страницы при переходе по ссылке: {self.page_url} """
        return WebDriverWait(self.driver, 20).until(
                    EC.url_to_be(page_url))

    @allure.step('Ждем загрузку всех элементов HTML по локатору')
    def wait_for_load_all_elements(self, locator):
        """ Ждем загрузку всех элементов HTML по локатору {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located(locator))

    @allure.step('Ждем появление в DOM элемента HTML по локатору')
    def wait_for_presence_of_element(self, locator):
        """ Ждем появление в DOM элемента HTML по локатору {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(locator))

    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        """ Получаем текущий url """
        return self.driver.current_url

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
        return WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))

    @allure.step('Вводим текст в поле по локатору')
    def set_value(self, locator, value):
        """ Вводим текст в поле по локатору: {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)).send_keys(value)

    @allure.step('Получаем значение поля по локатору')
    def get_value(self, locator):
        """ Получаем значение поля по локатору: {locator} """
        return WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)).get_attribute("value")

    @allure.step('Получаем текст в поле по локатору')
    def get_text(self, locator):
        """ Получаем текст в поле по локатору: {locator} """
        return (self.wait_for_load_element(locator)).text

    @allure.step('Прокручиваем страницу до элемента по локатору')
    def scroll_to_element_by_locator(self, locator):
        """ Прокручиваем страницу до элемента по локатору {locator} """
        element = WebDriverWait(self.driver, 20).until(
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
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)).click()

    @allure.step('Ждем кликабельности элемента по локатору и кликаем')
    def click_element_by_locator_when_clickable(self, locator):
        """ Ждем загрузку элемента HTML по локатору и кликаем """
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator))
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

    @allure.step('Проверяем, что в имени класса появляется текст')
    def wait_for_text_in_classname(self, locator, text):        # bool
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_attribute(locator, 'class', text))

    @allure.step('Проверяем что элемент становится невидимым')
    def wait_for_invisibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

