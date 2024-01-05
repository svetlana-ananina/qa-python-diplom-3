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
        #_print_info(f'user_order={user_order}')
        #_sleep(5)
        return user_order

    @allure.title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, get_browser):
        driver = get_browser
        main_page = FeedPage(driver)
        # Открываем Ленту заказов
        main_page.open_feed_page()
        #_sleep(3)
        # кликаем 1й заказ в ленте
        _print_info('кликаем заказ ...')
        main_page.click_order_link()
        #_sleep(3)
        _print_info('проверяем что окно деталей открылось ...')
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
        _print_info(f'user_order={user_order}')

        # получаем список номеров заказов в Ленте
        feed_page = FeedPage(driver)
        feed_order_list = feed_page.get_order_number_list()
        _print_info(f'feed_order_list={feed_order_list}')
        #_sleep(5)

        # проверяем, что заказ в ленте
        assert user_order in feed_order_list, f'Ошибка проверки Ленты заказов: заказ пользователя: {user_order} отсутствует в Ленте'

    @allure.title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_order_is_in_work(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера и страницу профиля
        driver = login_new_user
        # создаем заказ
        _print_info('test_user_order_is_in_work: создаем заказ ...')
        order = self.__create_user_order(driver)
        _print_info(f'test_user_order_is_in_work: заказ создан order={order}')
        # получаем номер заказа из истории в Личном кабинете пользователя
        #user_order = self.__get_order_from_user_history(driver)
        #_print_info(f'user_order={user_order}')

        # получаем список номеров заказов в Ленте
        feed_page = FeedPage(driver)
        _print_info('test_user_order_is_in_work: feed_page.click_feed_link()  ...')
        feed_page.click_feed_link()      # метод MainPage
        #orders_list_in_work = feed_page.get_order_list_in_work()
        #_sleep(5)

        _print_info(f'test_user_order_is_in_work: wait_for_load_all_elements  {FeedPageLocators.ORDER_STATUS_BOX_LIST2_ITEM_DIGIT} ...')
        # ORDER_STATUS_BOX_LIST2_ITEM_DIGIT = (
        # By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]/li[contains(@class,"digits")]')
        orders_list = feed_page.wait_for_load_all_elements(FeedPageLocators.ORDER_STATUS_BOX_LIST2_ITEM_DIGIT)
        _print_info(f'len(orders_list)={len(orders_list)}')

        #if len(orders_list) > 0:
        for element in orders_list:
            _print_info(f'element.text={element.text}')
        _sleep(5)





