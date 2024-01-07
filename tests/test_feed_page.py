import allure
import pytest

from helpers.common_helpers import _sleep, _print_info
from locators import FeedPageLocators
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage


class TestFeedPage:

    @staticmethod
    def __create_user_order(driver):
        # открываем конструктор
        main_page = ConstructorPage(driver)
        # оформляем заказ
        order = main_page.create_order()
        return order


    @staticmethod
    def __get_order_from_user_history(driver):
        # открываем Личный кабинет, кликаем ссылку История заказов и получаем номера заказов пользователя
        profile_page = ProfilePage(driver)
        # получаем список номеров заказов пользователя в формате "#..."
        user_order = profile_page.get_order_from_order_history()
        return user_order


    @allure.title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, get_browser):
        driver = get_browser
        main_page = FeedPage(driver)
        # Открываем Ленту заказов
        main_page.open_feed_page()
        # кликаем 1й заказ в ленте
        main_page.click_order_link()

        # ждем что открылось модальное окно деталей заказа
        assert main_page.order_details_is_opened()


    @allure.title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_are_in_feed(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера и страницу профиля
        driver = login_new_user
        # создаем заказ
        self.__create_user_order(driver)
        # получаем номер заказа из истории в Личном кабинете пользователя
        user_order = self.__get_order_from_user_history(driver)
        # получаем список номеров заказов в Ленте
        feed_page = FeedPage(driver)
        feed_order_list = feed_page.get_order_number_list()

        # проверяем, что заказ в ленте
        assert user_order in feed_order_list, f'Ошибка проверки Ленты заказов: заказ пользователя: {user_order} отсутствует в Ленте'


    @allure.title('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_user_order_is_in_work(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера и страницу профиля
        driver = login_new_user
        # создаем заказ
        new_order = self.__create_user_order(driver)
        # переходим к Ленте заказов на Главной странице
        feed_page = FeedPage(driver)
        # кликаем ссылку на Ленту заказов на главной странице
        feed_page.click_feed_link()      # метод MainPage
        # получаем список номеров заказов в Ленте
        orders_list_in_work = feed_page.get_order_list_in_work()

        # проверяем что новый заказ есть в списке
        assert new_order in orders_list_in_work, f'Ошибка проверки раздела "В работе": созданный заказ не отображается в разделе'


    @allure.title('Проверяем что создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_orders_total_counter(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера и страницу профиля
        driver = login_new_user
        # Открываем Ленту заказов
        feed_page = FeedPage(driver)
        # кликаем ссылку на Ленту заказов на главной странице
        feed_page.open_feed_page_by_link()
        # получаем счетчик заказов за все время
        orders_before = feed_page.get_orders_total()
        # создаем заказ
        self.__create_user_order(driver)
        # Открываем Ленту заказов
        feed_page.open_feed_page_by_link()
        # получаем счетчик заказов за все время
        orders_after = feed_page.get_orders_total()

        # проверяем что счетчик увеличился
        assert orders_after > orders_before, f'Ошибка проверки раздела "Выполнено за все время": счетчик не увеличился'


    @allure.title('Проверяем что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_orders_today_counter(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера и страницу профиля
        driver = login_new_user
        # Открываем Ленту заказов
        feed_page = FeedPage(driver)
        # кликаем ссылку на Ленту заказов на главной странице
        feed_page.open_feed_page_by_link()
        # получаем счетчик заказов за все время
        orders_before = feed_page.get_orders_today()
        # создаем заказ
        self.__create_user_order(driver)
        # Открываем Ленту заказов
        feed_page.open_feed_page_by_link()
        # получаем счетчик заказов за все время
        orders_after = feed_page.get_orders_today()

        # проверяем что счетчик увеличился
        assert orders_after > orders_before, f'Ошибка проверки раздела "Выполнено за сегодня": счетчик не увеличился, было {orders_before}, стало {orders_after}'
        _sleep(5)

