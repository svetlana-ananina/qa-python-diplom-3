import allure
import pytest

from helpers.common_helpers import _sleep
from locators import MainPageLocators, MAIN_PAGE_URL, FEED_PAGE_URL
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_open_constructor_by_link(self, get_browser):
        driver = get_browser
        main_page = MainPage(driver)
        # Открываем Ленту заказов
        main_page.open_feed_page()
        #_sleep(3)
        # кликаем ссылку "Конструктор" в хедере
        main_page.click_constructor_link()
        # ждем перехода на вкладку "Конструктор" и появления кнопки "Войти в аккаунт"
        main_page.wait_for_load_element(MainPageLocators.LOGIN_BUTTON)
        #_sleep(3)

        # Проверяем что текущий url это url Главной страницы
        #assert main_page.get_current_url() == MAIN_PAGE_URL
        #assert MAIN_PAGE_URL in main_page.get_current_url()
        assert main_page.constructor_is_active() and main_page.get_current_url() == MAIN_PAGE_URL+'/'


    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_open_feed_by_link(self, get_browser):
        driver = get_browser
        main_page = MainPage(driver)
        # Открываем Конструктор
        main_page.open_main_page()
        #_sleep(3)
        # кликаем ссылку "Конструктор" в хедере
        main_page.click_feed_link()
        # ждем перехода на вкладку "Конструктор" и появления кнопки "Войти в аккаунт"
        main_page.wait_for_load_element(MainPageLocators.TOTAL_TODAY)
        #_sleep(3)

        # Проверяем что текущий url это url Ленты заказов
        assert main_page.feed_is_active() and main_page.get_current_url() == FEED_PAGE_URL

    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, get_browser):
        driver = get_browser
        main_page = MainPage(driver)
        # Открываем Конструктор
        main_page.open_main_page()
        #_sleep(3)
        # кликаем на 1-й ингредиент
        main_page.click_ingredient_link()
        # ждем что открывается карточка деталей
        main_page.ingredient_details_is_opened()
        _sleep(3)

        # Проверяем что появился заголовок Детали ингредиента
        assert main_page.details_title_is_visible()

    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_closes_ingredient(self, get_browser):
        driver = get_browser
        main_page = MainPage(driver)
        # Открываем Конструктор
        main_page.open_main_page()
        #_sleep(3)
        # кликаем на 1-й ингредиент
        main_page.click_ingredient_link()
        # ждем, что открывается карточка деталей
        element = main_page.ingredient_details_is_opened()
        # возвращает элемент по локатору MainPageLocators.DETAILS_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
        _sleep(3)
        # кликаем на крестик
        main_page.click_details_close_link()
        #
        main_page.ingredient_details_is_closed()
        #
        assert element.get_attribute('class') == MainPageLocators.DETAILS_LINK_CLASS





