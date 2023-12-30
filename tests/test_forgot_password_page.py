import allure
import pytest
import time

from helpers import _print_info, _sleep
from pages.base_page import BasePage
from pages.forgot_password_page import FORGOT_PASSWORD_PAGE_URL, FORGOT_PASSWORD_PAGE_TITLE
from pages.login_page import LoginPage
from locators import LoginPageLocators, ForgotPasswordPageLocators

from data import _browser


class TestForgotPasswordPage:

    @allure.title('')
    @allure.description('')
    def test_forgot_password_button(self, get_browser):
        # Открываем окно веб-браузер
        driver = get_browser
        # открываем страницу авторизации
        login_page = LoginPage(driver)
        login_page.open_login_page()
        #_sleep(5)

        # ждем загрузку страницы и кликаем ссылку "Восстановить пароль"
        login_page.scroll_to_click_forgot_password_link()
        #_sleep(5)

        # ждем загрузку страницы и кликаем ссылку "Восстановить пароль"
#        login_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        login_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        _sleep(5)

        # Проверяем что текущий url это url страницы восстановления пароля
        assert login_page.get_current_url() == FORGOT_PASSWORD_PAGE_URL


