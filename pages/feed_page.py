import allure

from data import Urls
from locators import FeedPageLocators, MainPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Открываем Ленту заказов')
    def open_feed_page(self):
        self.open_page(Urls.FEED_PAGE_URL)
        self.wait_for_load_element(MainPageLocators.TOTAL_TODAY)

    @allure.step('кликаем ссылку "Конструктор"')
    def click_constructor_link(self):
        self.click_element_by_locator(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Проверяем, что Лента заказов становится активным')
    def feed_is_active(self):
        return self.wait_for_text_in_classname(MainPageLocators.FEED_LINK,
                                               MainPageLocators.ACTIVE_TEXT)

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
        self.open_feed_page()
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

    @allure.step('Получаем счетчик "Выполнено сегодня"')
    def get_orders_today(self):
        elements = self.__get_orders_total()
        return int(str(elements[1].text))



