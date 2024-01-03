import allure
import pytest

from helpers.common_helpers import _sleep, _print_info
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage


class TestFeedPage:

    @allure.title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, get_browser):
        driver = get_browser
        main_page = FeedPage(driver)
        # Открываем Ленту заказов
        main_page.open_feed_page()
        _sleep(3)
        # кликаем 1й заказ в ленте
        _print_info('кликаем заказ ...')
        main_page.click_order_link()
        _sleep(3)
        _print_info('проверяем что окно деталей открылось ...')
        # ждем что открылось модальное окно деталей заказа
        assert main_page.order_details_is_opened()

    @allure.title('Проверяем ')
    def test_user_orders_in_feed(self, get_browser, create_new_user_by_api, login_new_user, open_profile_page):
        # регистрируем нового пользователяm открываем окно веб-браузера и страницу профиля
        driver = open_profile_page

        # открываем Главную страницу
        #self.open_profile_page_by_link(driver)
        # _sleep(5)

        # открываем Личный кабинет и ждем появления кнопки "Сохранить"
        profile_page = ProfilePage(driver)
        # _sleep(5)
        # кликаем ссылку История заказов
        # profile_page.click_order_history_link()
        # _sleep(5)
        # получаем список номеров заказов пользователя в формате "#..."
        _print_info(f'get_order_history_list ...')
        order_list = profile_page.get_order_history_list()
        _print_info(f'order_list={order_list}')
        _sleep(5)





