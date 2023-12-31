import allure

from helpers.common_helpers import _sleep, _sleep_ff
from pages.login_page import LoginPage
from locators import ForgotPasswordPageLocators, FORGOT_PASSWORD_PAGE_URL, MAIN_PAGE_URL, MainPageLocators


#RECOVER_EMAIL = 'ivanivanov@mail.ru'


class TestProfilePage:

    @allure.title('')
    @allure.description('')
    def test_login_page(self, get_browser, create_new_user):
        # регистрируем нового пользователя
        user_data = create_new_user
        email = user_data['email']
        password = user_data['password']
        # Открываем окно веб-браузер
        driver = get_browser
        # открываем страницу авторизации
        login_page = LoginPage(driver)
        login_page.open_login_page()
        #_sleep(5)
        # Вводим email и пароль
        login_page.enter_user_data(email, password)
        _sleep_ff(5)
        # кликаем кнопку "Войти"
        login_page.click_login_button()
        # ждем появления кнопки "Оформить заказ" на Главной странице
        login_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        _sleep(5)
        # Проверяем что текущий url это url страницы восстановления пароля
        #assert login_page.get_current_url() == MAIN_PAGE_URL
        assert MAIN_PAGE_URL in login_page.get_current_url()

