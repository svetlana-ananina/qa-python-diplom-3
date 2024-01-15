import allure

from data import Urls, UserData
from locators import ForgotPasswordPageLocators
from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestForgotPasswordPage:

    @allure.title('Проверяем переход на страницу восстановления пароля по гиперссылке «Восстановить пароль»')
    def test_forgot_password_button(self, get_browser):
        # Открываем окно веб-браузер
        driver = get_browser
        # открываем страницу авторизации
        login_page = LoginPage(driver)
        login_page.open_login_page()
        # ждем загрузку страницы и кликаем ссылку "Восстановить пароль"
        login_page.scroll_to_click_forgot_password_link()
        # ждем загрузку страницы "Восстановление пароля"
        login_page.wait_for_load_element(ForgotPasswordPageLocators.RECOVER_BUTTON)

        # Проверяем что текущий url это url страницы восстановления пароля
        assert login_page.get_current_url() == Urls.FORGOT_PASSWORD_PAGE_URL


    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_recover_password_button(self, get_browser):
        # Открываем окно веб-браузер
        driver = get_browser
        # создаем элемент POM для страницы сброса пароля
        forgot_password_page = ForgotPasswordPage(driver)
        # Открываем страницу восстановления пароля, вводим почту и кликаем кнопку "Восстановить"
        forgot_password_page.open_and_execute_forgot_password_page(UserData.USER_EMAIL)

        # Проверяем что текущий url это url страницы сброса пароля
        assert forgot_password_page.get_current_url() == Urls.RESET_PASSWORD_PAGE_URL


    @allure.title('Проверяем что клик по кнопке показать/скрыть пароль делает поле активным')
    def test_eye_button(self, get_browser):
        # Открываем окно веб-браузер
        driver = get_browser
        # создаем элемент POM для страницы сброса пароля
        forgot_password_page = ForgotPasswordPage(driver)
        # Открываем страницу восстановления пароля, вводим почту и кликаем кнопку "Восстановить"
        forgot_password_page.open_and_execute_forgot_password_page(UserData.USER_EMAIL)
        # создаем элемент POM для страницы сброса пароля
        reset_password_page = ResetPasswordPage(driver)
        # кликаем по значку глаза - показать/скрыть пароль
        reset_password_page.click_eye_button()

        # Проверяем, что поле "email" становится активным
        assert reset_password_page.password_field_focused()

