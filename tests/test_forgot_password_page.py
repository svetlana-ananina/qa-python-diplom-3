import allure
import pytest
import time

from helpers import _print_info, _sleep
from pages.base_page import BasePage
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from locators import LoginPageLocators, ForgotPasswordPageLocators, FORGOT_PASSWORD_PAGE_URL, ResetPasswordPageLocators, \
    RESET_PASSWORD_PAGE_URL

from data import _browser


RECOVER_EMAIL = 'ivanivanov@mail.ru'

class TestForgotPasswordPage:

    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
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

        # ждем загрузку страницы "Восстановление пароля"
        login_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        _sleep(5)

        # Проверяем что текущий url это url страницы восстановления пароля
        assert login_page.get_current_url() == FORGOT_PASSWORD_PAGE_URL

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    @allure.description('')
    def test_recover_password_button(self, get_browser):
        # Открываем окно веб-браузер
        driver = get_browser
        # открываем страницу авторизации
        recover_page = ForgotPasswordPage(driver)
        recover_page.open_forgot_password_page()
        #_sleep(5)

        # ждем загрузку страницы
        recover_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

        # кликаем по полю "email"
        # прокручиваем страницу до кнопки "Восстановить" и кликаем по полю "email"
        recover_page.scroll_to_click_email_field()
        #_sleep(5)

        # вводим email в поле ввода
        recover_page.set_value(ForgotPasswordPageLocators.EMAIL_FIELD, RECOVER_EMAIL)
        #_sleep(5)

        recover_page.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.RECOVER_BUTTON)
        #_sleep(5)

        # ждем появления кнопки "Сохранить" на странице сброса пароля
        recover_page.wait_for_load_element(ResetPasswordPageLocators.SAVE_BUTTON)

        #_sleep(5)

        # Проверяем что текущий url это url страницы сброса пароля
        assert recover_page.get_current_url() == RESET_PASSWORD_PAGE_URL


    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    @allure.description('')
    def test_password_hide_button(self, get_browser):
        # Открываем окно веб-браузер
        driver = get_browser
        # открываем страницу авторизации
        recover_page = ForgotPasswordPage(driver)
        recover_page.open_forgot_password_page()
        #_sleep(5)

        # ждем загрузку страницы
        recover_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)



