import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import RESET_PASSWORD_PAGE_URL, ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Открываем страницу сброса пароля')
    def open_reset_password_page(self):
        # Открываем страницу авторизации
        return self.open_page(RESET_PASSWORD_PAGE_URL)

    @allure.step('Кликаем по значку глаза - показать/скрыть пароль')
    def click_eye_button(self):
        # Открываем страницу авторизации
        return self.click_element_by_locator(ResetPasswordPageLocators.EYE_ICON)

    @allure.step('Проверяем, что поле "email" становится активным')
    def email_field_focused(self):
        # Открываем страницу авторизации
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                ResetPasswordPageLocators.FOCUSED_FIELD, 'class', ResetPasswordPageLocators.FOCUSED_TEXT))     #.visibility_of_element_located(locator))

