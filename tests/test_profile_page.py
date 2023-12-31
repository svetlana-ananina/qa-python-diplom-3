import allure

from helpers.common_helpers import _sleep, _sleep_ff
from pages.login_page import LoginPage
from locators import ForgotPasswordPageLocators, FORGOT_PASSWORD_PAGE_URL, MAIN_PAGE_URL, MainPageLocators, \
    PROFILE_PAGE_URL
from pages.main_page import MainPage


#RECOVER_EMAIL = 'ivanivanov@mail.ru'


class TestProfilePage:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    @allure.description('')
    def test_profile_link(self, get_browser, create_new_user, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver, email, password = login_new_user
        # открываем Главную страницу
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        #_sleep(5)
        # кликаем Личный кабинет в хедере
        main_page.click_profile_link()
        # ждем перехода в Личный кабинет и появления кнопки "Сохранить"
        main_page.wait_for_load_element(MainPageLocators.SAVE_BUTTON)
        _sleep(5)
        # Проверяем что текущий url это url Личного кабинета
        #assert main_page.get_current_url() == PROFILE_PAGE_URL
        assert PROFILE_PAGE_URL in main_page.get_current_url()




