import allure

from helpers.common_helpers import _sleep_ff
from pages.base_page import BasePage
from locators import ForgotPasswordPageLocators, FORGOT_PASSWORD_PAGE_URL, ResetPasswordPageLocators


class ForgotPasswordPage(BasePage):

    @allure.step('Открываем страницу восстановления пароля')
    def open_forgot_password_page(self):
        # Открываем страницу авторизации
        return self.open_page(FORGOT_PASSWORD_PAGE_URL)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def scroll_to_click_email_field(self):
        # Ждем загрузку страницы
        #self.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)
        self.wait_for_load_element(ForgotPasswordPageLocators.EMAIL_FIELD)

        # прокручиваем страницу до кнопки "Восстановить"
        self.scroll_to_element_by_locator(ForgotPasswordPageLocators.RECOVER_BUTTON)

        # Кликаем по полю "email"
        #WebDriverWait(self.driver, 5).until(
        #    EC_conditions.element_to_be_clickable(ForgotPasswordPageLocators.EMAIL_FIELD))
        _sleep_ff(5)

        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.EMAIL_FIELD)
        #self.click_element(element)

    @allure.step('Открываем страницу восстановления пароля, вводим почту и кликаем кнопку "Восстановить"')
    def open_and_execute_forgot_password_page(self, email):

        # открываем страницу восстановления пароля
        self.open_forgot_password_page()
        #_sleep(5)

        # ждем загрузку страницы
        self.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

        # кликаем по полю "email"
        # прокручиваем страницу до кнопки "Восстановить" и кликаем по полю "email"
        self.scroll_to_click_email_field()
        #_sleep(5)

        # вводим email
        self.set_value(ForgotPasswordPageLocators.EMAIL_FIELD, email)
        #_sleep(5)

        # кликаем кнопку "Восстановить"
        self.click_element_by_locator_when_clickable(ForgotPasswordPageLocators.RECOVER_BUTTON)
        #_sleep(5)

        # ждем появления кнопки "Сохранить" на странице сброса пароля
        self.wait_for_load_element(ResetPasswordPageLocators.SAVE_BUTTON)



