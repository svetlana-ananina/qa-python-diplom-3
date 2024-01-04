import allure
import pytest

from helpers.common_helpers import _sleep, _sleep_ff
from locators import PROFILE_PAGE_URL, ORDER_HISTORY_URL, LoginPageLocators, LOGIN_PAGE_URL
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def __open_profile_page_by_link(self, driver):
        main_page = MainPage(driver)
        main_page.open_profile_page_by_link()
        return main_page

    # Проверяем что текущий url это url Личного кабинета
    # assert main_page.get_current_url() == PROFILE_PAGE_URL

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    @allure.description('')
    def test_profile_link(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver = login_new_user
        self.__open_profile_page_by_link(driver)
        # Проверяем что текущий url это url Личного кабинета
        #assert #main_page.get_current_url() == PROFILE_PAGE_URL
        assert driver.current_url == PROFILE_PAGE_URL
        #assert PROFILE_PAGE_URL in main_page.get_current_url()


    @allure.title('Проверяем переход в раздел «История заказов»')
    @allure.description('')
    def test_order_history_link(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver = login_new_user

        # открываем Главную страницу
        self.__open_profile_page_by_link(driver)
        #open_profile_page_by_link(driver)
        #_sleep(5)

        # открываем Личный кабинет и ждем появления кнопки "Сохранить"
        profile_page = ProfilePage(driver)
        #_sleep(5)
        # кликаем ссылку История заказов
        profile_page.click_order_history_link()
        #_sleep(5)
        # Проверяем что раздел Истории заказов стал активным и текущий url это url Истории заказовS
        assert profile_page.order_history_is_active() and profile_page.get_current_url() == ORDER_HISTORY_URL


    @allure.title('Проверяем выход из аккаунта')
    @allure.description('')
    def test_exit_button(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver = login_new_user

        # открываем Главную страницу
        self.__open_profile_page_by_link(driver)
        #open_profile_page_by_link(driver)
        #_sleep(5)

        # открываем Личный кабинет и ждем появления кнопки "Сохранить"
        profile_page = ProfilePage(driver)
        #_sleep(5)
        # кликаем кнопку Выход
        profile_page.click_exit_button()
        #_sleep(5)

        # ждем что произошел переход на страницу авторизации
        profile_page.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)
        #_sleep(5)

        # Проверяем что текущий url это url страницы авторизации
        assert profile_page.get_current_url() == LOGIN_PAGE_URL



