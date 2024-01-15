import allure

from data import Urls
from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        # Открываем страницу авторизации
        self.open_page(Urls.LOGIN_PAGE_URL)
        self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Ждем загрузку страницы авторизации')
    def wait_open_login_page(self):
        # Открываем страницу авторизации
        self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Вводим email и пароль')
    def enter_user_data(self, email, password):
        # Вводим email и пароль
        self.wait_for_load_element(LoginPageLocators.EMAIL_FIELD)
        # кликаем  поле "email"
        self.click_element_by_locator_when_clickable(LoginPageLocators.EMAIL_FIELD)
        # вводим email
        self.set_value(LoginPageLocators.EMAIL_FIELD, email)
        # кликаем  поле "Пароль"
        self.click_element_by_locator_when_clickable(LoginPageLocators.PASSWORD_FIELD)
        # вводим пароль
        self.set_value(LoginPageLocators.PASSWORD_FIELD, password)

    @allure.step('кликаем кнопку "Войти"')
    def click_login_button(self):
        # кликаем кнопку "Войти"
        self.click_element_by_locator(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Прокручиваем страницу и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_forgot_password_link(self):
        # Прокручиваем страницу вниз
        self.scroll_to_element_by_locator(LoginPageLocators.LOGIN_BUTTON)
        # кликаем ссылку "Восстановить пароль"
        self.click_element_by_locator(LoginPageLocators.FORGOT_PAGE_LINK)

