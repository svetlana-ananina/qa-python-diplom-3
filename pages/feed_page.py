import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.common_helpers import _print_info
from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL, FeedPageLocators
from pages.main_page import MainPage


class FeedPage(MainPage):

    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def open_feed_page_by_link(self):
        main_page = MainPage(self.driver)
        main_page.open_feed_page()
        return main_page

    @allure.step('кликаем на 1-й заказ')
    def click_order_link(self):
        self.click_element_by_locator(FeedPageLocators.ORDER_LINK)

    @allure.step('Проверяем, что открывается модальное окно с деталями заказа')
    def order_details_is_opened(self):
        return self.wait_for_load_element(FeedPageLocators.ORDER_DETAILS_OPENED)

    @allure.step('Получаем список элементов страницы с номерами заказов')
    def __get_order_number_list_elements(self):
        return self.wait_for_load_all_elements(FeedPageLocators.ORDER_LIST_ORDER_NUMBER)


    @allure.step('Получаем список номеров заказов')
    def get_order_number_list(self):
        # Открываем Личный кабинет по ссылке на Главной странице
        self.open_feed_page_by_link()
        # получаем элементы списка с номерами заказов
        _print_info(f'get_order_number_list_elements ...')
        elements = self.__get_order_number_list_elements()
        _print_info(f'len={len(elements)}')
        #
        _print_info(f'Получаем список номеров заказов в Ленте заказов ...')
        order_list = []
        for item in elements:
            number = item.text
            #_print_info(f'number={number}')
            order_list.append(number)
        return order_list

