import allure
import pytest

from helpers.common_helpers import _sleep, _print_info
from pages.feed_page import FeedPage


class TestFeedPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_open_feed_by_link(self, get_browser):
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



