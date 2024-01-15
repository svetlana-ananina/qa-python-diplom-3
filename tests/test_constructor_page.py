import allure

from data import Urls
from locators import MainPageLocators
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


class TestConstructorPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_open_constructor_by_link(self, get_browser):
        driver = get_browser
        # Открываем Ленту заказов
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        # кликаем ссылку "Конструктор" в хедере
        feed_page.click_constructor_link()
        # ждем перехода на вкладку "Конструктор" и появления кнопки "Войти в аккаунт"
        constructor_page = ConstructorPage(driver)
        constructor_page.wait_for_load_element(MainPageLocators.LOGIN_BUTTON)

        # Проверяем что текущий url это url Главной страницы
        assert constructor_page.constructor_is_active()
        assert constructor_page.get_current_url() == Urls.MAIN_PAGE_URL+'/'


    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_open_feed_by_link(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        # Открываем Конструктор
        constructor_page.open_constructor_page()
        # кликаем ссылку "Лента заказов" в хедере
        constructor_page.click_feed_link()
        # ждем перехода на вкладку "Лента заказов" и появления счетчика "Выполнено сегодня"
        feed_page = FeedPage(driver)
        feed_page.wait_for_load_element(MainPageLocators.TOTAL_TODAY)

        # Проверяем что текущий url это url Ленты заказов
        assert feed_page.feed_is_active()
        assert feed_page.get_current_url() == Urls.FEED_PAGE_URL


    @allure.title('Проверяем, что если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_ingredient(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        # Открываем Конструктор
        constructor_page.open_constructor_page()
        # кликаем на 1-й ингредиент
        constructor_page.click_ingredient_link()
        # ждем что открывается карточка деталей
        constructor_page.ingredient_details_is_opened()

        # Проверяем что появился заголовок Детали ингредиента
        assert constructor_page.details_title_is_visible()


    @allure.title('Проверяем, что всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        # Открываем Конструктор
        constructor_page.open_constructor_page()
        # кликаем на 1-й ингредиент
        constructor_page.click_ingredient_link()
        # ждем, что открывается карточка деталей и получаем элемент с изменившимся классом: (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
        element = constructor_page.ingredient_details_is_opened()
        # кликаем на крестик
        constructor_page.click_details_close_link()
        # ждем пока закроется модальное окно
        constructor_page.ingredient_details_is_closed()

        # проверяем что модальное окно с деталями заказа закрылось
        assert element.get_attribute('class') == MainPageLocators.DETAILS_LINK_CLASS


    @allure.title('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_append_ingredient_in_order(self, get_browser):
        driver = get_browser
        constructor_page = ConstructorPage(driver)
        # Открываем Конструктор
        constructor_page.open_constructor_page()
        # получаем значение счетчика до
        counter_before = constructor_page.get_buns_counter()
        # Перемещаем булку в бургер
        constructor_page.drag_and_drop_bun()
        # получаем значение счетчика после добавления ингредиента
        counter_after = constructor_page.get_buns_counter()

        # Проверяем, что счетчик ингредиента увеличивается
        assert counter_after > counter_before


    @allure.title('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_checkout_order_by_user(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера
        driver = login_new_user
        # открываем Главную страницу
        constructor_page = ConstructorPage(driver)
        # оформляем заказ
        constructor_page._create_order()

        # проверяем, что появилось модальное окно с деталями заказа
        assert constructor_page.order_details_is_visible()

