import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import _sleep, _sleep_ff
from pages.base_page import BasePage
from locators import LoginPageLocators, ForgotPasswordPageLocators, FORGOT_PASSWORD_PAGE_URL

#FORGOT_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
FORGOT_PASSWORD_PAGE_TITLE = 'Восстановление пароля'                                    # Заголовок страницы восстановления пароля


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_forgot_password_page(self):
        # Открываем страницу авторизации
        return self.open_page(FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Ждем загрузку страницы восстановления пароля')
    def wait_for_load_forgot_password_page(self):
        #self.wait_for_load_element(Locators.RECOVER_TITLE)
        return self.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_email_field(self):
        # Ждем загрузку страницы
        #self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_load_element(ForgotPasswordPageLocators.EMAIL_FIELD)

        # прокручиваем страницу до кнопки "Восстановить"
        self.scroll_to_element_by_locator(ForgotPasswordPageLocators.RECOVER_BUTTON)

        # Кликаем по полю "email"
        #WebDriverWait(self.driver, 5).until(
        #    expected_conditions.element_to_be_clickable(ForgotPasswordPageLocators.EMAIL_FIELD))
        _sleep_ff(5)

        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.EMAIL_FIELD)
        #self.click_element(element)




