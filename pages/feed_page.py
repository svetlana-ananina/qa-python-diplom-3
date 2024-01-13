import allure

from helpers.common_helpers import _print_info
from locators import FeedPageLocators
from pages.constructor_page import ConstructorPage


class FeedPage(ConstructorPage):

    @allure.step('Открываем Ленту заказов по ссылке на Главной странице')
    def open_feed_page_by_link(self):
        self.open_feed_page()

    @allure.step('кликаем на 1-й заказ')
    def click_order_link(self):
        self.click_element_by_locator(FeedPageLocators.ORDER_LINK)

    @allure.step('Проверяем, что открывается модальное окно с деталями заказа')
    def order_details_is_opened(self):
        return self.wait_for_load_element(FeedPageLocators.ORDER_DETAILS_OPENED)

    @allure.step('Получаем список элементов страницы с номерами заказов из раздела Лента заказов')
    def __get_order_number_list_elements(self):
        return self.wait_for_load_all_elements(FeedPageLocators.ORDER_LIST_ORDER_NUMBER)

    @allure.step('Получаем список номеров заказов в Ленте заказов')
    def get_order_number_list(self):
        # Открываем Ленту заказов по ссылке на Главной странице
        self.open_feed_page_by_link()
        # получаем элементы списка с номерами заказов
        elements = self.__get_order_number_list_elements()
        #
        order_list = []
        for item in elements:
            number = item.text
            order_list.append(number)
        return order_list

    @allure.step('Получаем список элементов страницы с номерами заказов в разделе "В работе"')
    def __get_order_list_in_work(self):
        # Открываем Ленту заказов по ссылке на Главной странице
        orders_list = self.wait_for_load_all_elements(FeedPageLocators.ORDER_STATUS_BOX_LIST2_ITEM_DIGIT)
        return orders_list

    @allure.step('Получаем список номеров заказов в разделе "В работе"')
    def get_order_list_in_work(self):
        # Открываем Ленту заказов по ссылке на Главной странице
        elements = self.__get_order_list_in_work()
        orders_list = []
        for element in elements:
            number = str(int(element.text))
            orders_list.append(number)
        return orders_list

    @allure.step('Получаем список элементов страницы со счетчиками "Выполнено за всё время" и "Выполнено за сегодня"')
    def __get_orders_total(self):
        # Открываем Ленту заказов по ссылке на Главной странице
        elements = self.wait_for_load_all_elements(FeedPageLocators.ORDER_FEED_NUMBER)
        return elements

    @allure.step('Получаем счетчик "Выполнено за всё время"')
    def get_orders_total(self):
        elements = self.__get_orders_total()
        return int(str(elements[0].text))

    @allure.step('Получаем счетчик "Выполнено за всё время"')
    def get_orders_today(self):
        elements = self.__get_orders_total()
        return int(str(elements[1].text))



