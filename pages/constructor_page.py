import allure
from selenium.webdriver.support import expected_conditions
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
            expected_conditions.invisibility_of_element_located(MainPageLocators.DETAILS_TITLE_LINK))

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
        _print_info(f'\ncounter(text)={counter}')
        counter = int(counter)
        _print_info(f'\ncounter(int)={counter}')
        return counter



