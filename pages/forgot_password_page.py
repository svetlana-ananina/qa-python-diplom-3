import allure

from data import Urls
from locators import ForgotPasswordPageLocators, ResetPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        # Открываем страницу авторизации
        return self.open_page(Urls.FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_email_field(self):
        # Ждем загрузку страницы
        self.wait_for_load_element(ForgotPasswordPageLocators.EMAIL_FIELD)
        # прокручиваем страницу до кнопки "Восстановить"
        self.scroll_to_element_by_locator(ForgotPasswordPageLocators.RECOVER_BUTTON)
        # Кликаем по полю "email"
        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.EMAIL_FIELD)

    @allure.step('Открываем страницу восстановления пароля, вводим почту и кликаем кнопку "Восстановить"')
    def open_and_execute_forgot_password_page(self, email):

        # открываем страницу восстановления пароля
        self.open_forgot_password_page()
        # ждем загрузку страницы
        self.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)
        # прокручиваем страницу до кнопки "Восстановить" и кликаем по полю "email"
        self.scroll_to_click_email_field()
        # вводим email
        self.set_value(ForgotPasswordPageLocators.EMAIL_FIELD, email)
        # кликаем кнопку "Восстановить"
        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.RECOVER_BUTTON)
        # ждем появления кнопки "Сохранить" на странице сброса пароля
        self.wait_for_load_element(ResetPasswordPageLocators.SAVE_BUTTON)

