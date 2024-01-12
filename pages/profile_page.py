import allure

from locators import ProfilePageLocators
from pages.base_page import BasePage
from pages.main_page import MainPage


class ProfilePage(BasePage):

    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def __open_profile_page_by_link(self):
        main_page = MainPage(self.driver)
        main_page.open_profile_page_by_link()
        return main_page

    @allure.step('кликаем ссылку "Личный кабинет"')
    def click_order_history_link(self):
        # кликаем ссылку "Личный кабинет"
        self.click_element_by_locator(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Проверяем, что раздел История заказов становится активным')
    def order_history_is_active(self):
        return self.wait_for_text_in_classname(ProfilePageLocators.ORDER_HISTORY_LINK,
                                               ProfilePageLocators.ORDER_HISTORY_IS_ACTIVE)

    @allure.step('кликаем кнопку "Выход"')
    def click_exit_button(self):
        # кликаем ссылку "Личный кабинет"
        self.click_element_by_locator(ProfilePageLocators.EXIT_BUTTON)

    #
    # вспомогательная функция для других тестов - get_order_history_list
    # Получаем список номеров заказов пользователя
    @allure.step('Получаем список элементов страницы с номерами заказов')
    def __get_order_history_elements(self):
        return self.wait_for_load_all_elements(ProfilePageLocators.ORDER_HISTORY_ORDER_NUMBER)

    @allure.step('Получаем список номеров заказов пользователя')
    def get_order_history_list(self):
        # Открываем Личный кабинет по ссылке на Главной странице
        self.__open_profile_page_by_link()
        # кликаем ссылку История заказов
        self.click_order_history_link()
        # получаем элементы списка с номерами заказов
        elements = self.__get_order_history_elements()
        #
        order_list = []
        for item in elements:
            order_list.append(item.text)
        return order_list

    #
    # вспомогательная функция для других тестов - get_order_from_order_history
    # Получаем номер последнего заказа пользователя
    @allure.step('Получаем элемент страницы с номером заказа')
    def __get_order_history_first_element(self):
        return self.wait_for_load_element(ProfilePageLocators.ORDER_HISTORY_ORDER_NUMBER)

    @allure.step('Получаем номер последнего заказа пользователя')
    def get_order_from_order_history(self):
        # Открываем Личный кабинет по ссылке на Главной странице
        self.__open_profile_page_by_link()
        # кликаем ссылку История заказов
        self.click_order_history_link()
        # получаем 1-й элемент списка с номерами заказов
        element = self.__get_order_history_first_element()
        # получаем номер заказа
        number = element.text
        return number

