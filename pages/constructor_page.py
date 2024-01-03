import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers.common_helpers import _print_info
from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL
from pages.main_page import MainPage


class ConstructorPage(MainPage):

    @allure.step('кликаем на 1-й ингредиент')
    def click_ingredient_link(self):
        self.click_element_by_locator(MainPageLocators.INGREDIENT_LINK)
        #_sleep(5)

    @allure.step('Проверяем, что открывается карточка деталей')
    def ingredient_details_is_opened(self):
        return self.wait_for_presence_of_element(MainPageLocators.DETAILS_OPENED_LINK)

    @allure.step('Проверяем, что появился заголовок Детали ингредиента')
    def details_title_is_visible(self):
        return self.wait_for_load_element(MainPageLocators.DETAILS_TITLE_LINK)

    @allure.step('кликаем на крестик')
    def click_details_close_link(self):
        self.click_element_by_locator(MainPageLocators.DETAILS_CLOSE_LINK)
        #_sleep(5)

    @allure.step('кликаем на крестик')
    def click_details_close_link(self):
        self.click_element_by_locator(MainPageLocators.DETAILS_CLOSE_LINK)
        #_sleep(5)

    @allure.step('Проверяем что заголовок Детали ингредиента скрыт')
    def ingredient_details_is_closed(self):
        return WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located(MainPageLocators.DETAILS_TITLE_LINK))

    @allure.step('Добавляем булку в заказ')
    def drag_and_drop_bun(self):
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_LINK)
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BUN_TARGET)
        self.drag_and_drop(source, target)
        # _sleep(5)

    @allure.step('Добавляем булку в заказ')
    def get_buns_counter(self):
        #source = self.wait_for_load_element(MainPageLocators.INGREDIENT_COUNTER_LINK)
        #counter = int(self.check_text(MainPageLocators.INGREDIENT_COUNTER_LINK))
        counter = self.check_text(MainPageLocators.INGREDIENT_COUNTER_LINK)
        #_print_info(f'\ncounter(text)={counter}')
        counter = int(counter)
        #_print_info(f'\ncounter(int)={counter}')
        return counter

    @allure.step('Прокручиваем страницу к соусу')
    def scroll_to_sauce(self):
        # Прокручиваем страницу вниз
        sauce_element = self.scroll_to_element_by_locator(MainPageLocators.INGREDIENT_3_LINK)
        return sauce_element


    @allure.step('Прокручиваем страницу к начинке')
    def scroll_to_filling(self):
        # Прокручиваем страницу вниз
        filling_element = self.scroll_to_element_by_locator(MainPageLocators.INGREDIENT_7_LINK)
        return filling_element

    @allure.step('Добавляем соус в заказ')
    def drag_and_drop_sauce(self):
        #_print_info('drag_and_drop_sauce: scroll_to_sauce ...')
        self.scroll_to_sauce()
        #_print_info('drag_and_drop_sauce: wait_for_load_element - source ...')
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_3_LINK)
        #_print_info('drag_and_drop_sauce: wait_for_load_element - target ...')
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BURGER_TARGET)
        #_print_info('drag_and_drop_sauce: drag_and_drop  ...')
        self.drag_and_drop(source, target)
        # _sleep(5)

    @allure.step('Добавляем начинку в заказ')
    def drag_and_drop_filling(self):
        self.scroll_to_filling()
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_7_LINK)
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BURGER_TARGET)
        self.drag_and_drop(source, target)
        # _sleep(5)

    @allure.step('Ждем видимости элемента по локатору и кликаем')
    def click_order_button(self):
        """ Ждем загрузку элемента HTML по локатору и кликаем """
        self.scroll_to_element_by_locator(MainPageLocators.ORDER_BUTTON)
        self.click_element_by_locator(MainPageLocators.ORDER_BUTTON)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями заказа')
    def order_details_is_visible(self):
        return self.wait_for_load_element(MainPageLocators.ORDER_MODAL_OPENED_LINK)

