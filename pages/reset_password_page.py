import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import _sleep, _sleep_ff
from pages.base_page import BasePage
from locators import RESET_PASSWORD_PAGE_URL


class ResetPasswordPage(BasePage):

    @allure.step('Открываем страницу сброса пароля')
    def open_reset_password_page(self):
        # Открываем страницу авторизации
        return self.open_page(RESET_PASSWORD_PAGE_URL)

