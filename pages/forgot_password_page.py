import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


FORGOT_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
FORGOT_PASSWORD_PAGE_TITLE = 'Восстановление пароля'                                    # Заголовок страницы восстановления пароля

class Locators:
    RECOVER_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")     # Заголовок
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")         # Кнопка "Восстановить"


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_forgot_password_page(self):
        # Открываем страницу авторизации
        self.open_page(FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Ждем загрузку страницы восстановления пароля')
    def wait_for_load_forgot_password_page(self):
        self.wait_for_load_element(Locators.RECOVER_TITLE)
        self.wait_for_load_element(Locators.RECOVER_BUTTON)



