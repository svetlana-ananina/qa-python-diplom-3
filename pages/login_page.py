import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import _sleep
from pages.base_page import BasePage
from locators import LoginPageLocators, ForgotPasswordPageLocators, LOGIN_PAGE_URL


#LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'  # URL для страницы авторизации


class LoginPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        # Открываем страницу авторизации
        self.open_page(LOGIN_PAGE_URL)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_forgot_password_link(self):
        # Ждем загрузку страницы авторизации и текст с гиперссылкой "Восстановить пароль"
        #self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_load_element(LoginPageLocators.FORGOT_PAGE_LINK)
        #self.wait_for_clickable_element(Locators.FORGOT_PAGE_LINK)
        # прокручиваем страницу до кнопки "Войти"
        #element = self.driver.find_element(*(LoginPageLocators.FORGOT_PAGE_LINK))
        #self.scroll_to_element(element)
        self.scroll_to_element_by_locator(LoginPageLocators.LOGIN_BUTTON)
        #WebDriverWait(self.driver, 10).until(
        #    expected_conditions.visibility_of_element_located(Locators.FORGOT_PAGE_LINK))
        #WebDriverWait(self.driver, 5).until(
        #    expected_conditions.element_to_be_clickable(Locators.FORGOT_PAGE_LINK))
        #_to_sleep_ff(5)
        # Кликаем по ссылке "Восстановить пароль"
        self.click_element_by_locator(LoginPageLocators.FORGOT_PAGE_LINK)
        #self.click_element(element)


