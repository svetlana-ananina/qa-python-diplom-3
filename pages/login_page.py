import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers.common_helpers import _sleep_ff, _sleep
from pages.base_page import BasePage
from locators import LoginPageLocators, LOGIN_PAGE_URL, MainPageLocators


class LoginPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        # Открываем страницу авторизации
        self.open_page(LOGIN_PAGE_URL)
        self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)


    @allure.step('Вводим email и пароль')
    def enter_user_data(self, email, password):
        # Вводим email и пароль
        self.wait_for_load_element(LoginPageLocators.EMAIL_FIELD)
        #_sleep(5)

        # кликаем  поле "email"
        self.click_element_by_locator_when_clickable(LoginPageLocators.EMAIL_FIELD)
        #_sleep(5)

        # вводим email
        self.set_value(LoginPageLocators.EMAIL_FIELD, email)
        #_sleep(5)

        # кликаем  поле "Пароль"
        self.click_element_by_locator_when_clickable(LoginPageLocators.PASSWORD_FIELD)
        #_sleep(5)

        # вводим пароль
        self.set_value(LoginPageLocators.PASSWORD_FIELD, password)
        #_sleep_ff(5)


    @allure.step('кликаем кнопку "Войти"')
    def click_login_button(self):
        # кликаем кнопку "Войти"
        self.click_element_by_locator(LoginPageLocators.LOGIN_BUTTON)
        #_sleep(5)




