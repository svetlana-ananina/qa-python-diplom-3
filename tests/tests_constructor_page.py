import allure
import pytest

from helpers.common_helpers import _sleep, _print_info, _sleep_ff
from locators import MainPageLocators, MAIN_PAGE_URL, FEED_PAGE_URL
from pages.constructor_page import ConstructorPage
from pages.main_page import MainPage


class TestConstructorPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_open_constructor_by_link(self, get_browser):
        driver = get_browser
        main_page = ConstructorPage(driver)
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
        main_page = ConstructorPage(driver)
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
        main_page = ConstructorPage(driver)
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
    def test_closes_ingredient_details(self, get_browser):
        driver = get_browser
        main_page = ConstructorPage(driver)
        # Открываем Конструктор
        main_page.open_main_page()
        #_sleep(3)
        # кликаем на 1-й ингредиент
        main_page.click_ingredient_link()
        # ждем, что открывается карточка деталей и получаем элемент с изменившимся классом: (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
        element = main_page.ingredient_details_is_opened()
        _sleep(3)
        # кликаем на крестик
        main_page.click_details_close_link()
        #
        main_page.ingredient_details_is_closed()

        # проверяем что модальное окно с деталями заказа закрылось
        assert element.get_attribute('class') == MainPageLocators.DETAILS_LINK_CLASS

    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_append_ingredient_in_order(self, get_browser):
        driver = get_browser
        main_page = ConstructorPage(driver)
        # Открываем Конструктор
        main_page.open_main_page()
        #_sleep(3)
        # получаем значение счетчика до
        counter_before = main_page.get_buns_counter()
        # Перемещаем булку в бургер
        main_page.drag_and_drop_bun()
        # получаем значение счетчика после добавления ингредиента
        counter_after = main_page.get_buns_counter()
        _sleep(5)

        # Проверяем, что счетчик ингредиента увеличивается
        assert counter_after > counter_before


    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_checkout_order_by_user(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера
        driver = login_new_user
        # открываем Главную страницу
        main_page = ConstructorPage(driver)
        # оформляем заказ
        main_page._create_order()
        #_sleep(5)

        # проверяем, что появилось модальное окно с деталями заказа
        assert main_page.order_details_is_visible()



