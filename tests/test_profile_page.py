import allure

from helpers.common_helpers import _sleep, _sleep_ff
from locators import MainPageLocators, PROFILE_PAGE_URL, ProfilePageLocators, ORDER_HISTORY_URL
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def open_profile_page_by_link(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        # _sleep(5)
        # кликаем Личный кабинет в хедере
        main_page.click_profile_link()
        # ждем перехода в Личный кабинет и появления кнопки "Сохранить"
        main_page.wait_for_load_element(ProfilePageLocators.SAVE_BUTTON)
        #_sleep(5)
        return main_page

    # Проверяем что текущий url это url Личного кабинета
    # assert main_page.get_current_url() == PROFILE_PAGE_URL

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    @allure.description('')
    def test_profile_link(self, get_browser, create_new_user, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver, email, password = login_new_user
        # открываем Главную страницу
        main_page = self.open_profile_page_by_link(driver)
        #_sleep(5)
        # Проверяем что текущий url это url Личного кабинета
        assert main_page.get_current_url() == PROFILE_PAGE_URL
        #assert PROFILE_PAGE_URL in main_page.get_current_url()


    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    @allure.description('')
    def test_order_history_link(self, get_browser, create_new_user, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver, email, password = login_new_user

        # открываем Главную страницу
        self.open_profile_page_by_link(driver)
        #_sleep(5)

        # открываем Личный кабинет и ждем появления кнопки "Сохранить"
        profile_page = ProfilePage(driver)
        #_sleep(5)
        # кликаем ссылку История заказов
        profile_page.click_order_history_link()
        _sleep(5)
        # Проверяем что раздел Истории заказов стал активным и текущий url это url Истории заказовS
        assert profile_page.order_history_is_active() and profile_page.get_current_url() == ORDER_HISTORY_URL



