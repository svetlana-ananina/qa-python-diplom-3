import allure

from data import Urls
from locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    @allure.step('Открываем страницу сброса пароля')
    def open_reset_password_page(self):
        # Открываем страницу авторизации
        return self.open_page(Urls.RESET_PASSWORD_PAGE_URL)

    @allure.step('Кликаем по значку глаза - показать/скрыть пароль')
    def click_eye_button(self):
        # Открываем страницу авторизации
        return self.click_element_by_locator(ResetPasswordPageLocators.EYE_ICON)

    @allure.step('Проверяем, что поле "пароль" становится активным')
    def password_field_focused(self):
        # Открываем страницу авторизации
        return self.wait_for_text_in_classname(ResetPasswordPageLocators.FOCUSED_FIELD, ResetPasswordPageLocators.FOCUSED_TEXT)

