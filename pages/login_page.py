import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'  # URL для страницы авторизации


#class LoginPageLocators:
class Locators:
    #FORGOT_PAGE_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")         # Ссылка "Восстановить пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")                      # Кнопка "Войти"
    FORGOT_PAGE_LINK = (By.XPATH, ".//a[@href='/account']")


class LoginPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        # Открываем страницу авторизации
        self.open_page(LOGIN_PAGE_URL)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_forgot_password_link(self):
        # Ждем страницу авторизации и текст с гиперссылкой "Восстановить пароль"
        self.wait_for_load_element(Locators.LOGIN_BUTTON)
        self.wait_for_load_element(Locators.FORGOT_PAGE_LINK)
        #self.wait_for_clickable_element(Locators.FORGOT_PAGE_LINK)
        #WebDriverWait(self.driver, 5).until(
        #    expected_conditions.element_to_be_clickable(Locators.FORGOT_PAGE_LINK))
        # прокручиваем страницу до кнопки "Войти"
        self.scroll_to_element(Locators.LOGIN_BUTTON)
        #time.sleep(5)
        # Кликаем по ссылке "Восстановить пароль"
        self.click_element(Locators.FORGOT_PAGE_LINK)


