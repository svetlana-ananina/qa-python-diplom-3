import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.common_helpers import _print_info
from locators import PROFILE_PAGE_URL, ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('кликаем ссылку "Личный кабинет"')
    def click_order_history_link(self):
        # кликаем ссылку "Личный кабинет"
        self.click_element_by_locator(ProfilePageLocators.ORDER_HISTORY_LINK)
        #_sleep(5)


    @allure.step('Проверяем, что  становится активным')
    def order_history_is_active(self):
        return WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element_attribute(
                ProfilePageLocators.ORDER_HISTORY_LINK, 'class', ProfilePageLocators.ORDER_HISTORY_ACTIVE_TEXT))     #.visibility_of_element_located(locator))


    @allure.step('кликаем кнопку "Выход"')
    def click_exit_button(self):
        # кликаем ссылку "Личный кабинет"
        self.click_element_by_locator(ProfilePageLocators.EXIT_BUTTON)
        #_sleep(5)

    ##########################################################################
    # вспомогательная функция для других тестов
    @allure.step('Получаем список элементов страницы с номерами заказов')
    def get_order_history_elements(self):
        _print_info(f'get_order_history_elements ...')
        return self.wait_for_load_all_elements(ProfilePageLocators.ORDER_NUMBER_TEXT)

    @allure.step('Получаем список номеров заказов пользователя')
    def get_order_history_list(self):
        # кликаем ссылку История заказов
        _print_info(f'click_order_history_link ...')
        self.click_order_history_link()
        # получаем элементы списка с номерами заказов
        _print_info(f'get_order_history_elements ...')
        elements = self.get_order_history_elements()
        #
        order_list = []
        for item in elements:
            number = item.text
            _print_info(f'number={number}')
            elements.append(number)

