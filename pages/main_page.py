import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL


class MainPage(BasePage):

    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        self.open_page(MAIN_PAGE_URL)
        #self.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        self.wait_for_load_element(MainPageLocators.ANY_BUTTON)

    @allure.step('Открываем Ленту заказов')
    def open_feed_page(self):
        self.open_page(FEED_PAGE_URL)
        self.wait_for_load_element(MainPageLocators.TOTAL_TODAY)

    @allure.step('кликаем ссылку "Личный кабинет"')
    def click_profile_link(self):
        self.click_element_by_locator(MainPageLocators.PROFILE_LINK)
        #_sleep(5)

    @allure.step('кликаем ссылку "Конструктор"')
    def click_constructor_link(self):
        self.click_element_by_locator(MainPageLocators.CONSTRUCTOR_LINK)
        #_sleep(5)

    @allure.step('кликаем ссылку "Лента заказов"')
    def click_feed_link(self):
        self.click_element_by_locator(MainPageLocators.FEED_LINK)
        #_sleep(5)

    @allure.step('Проверяем, что Конструктор становится активным')
    def constructor_is_active(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                MainPageLocators.CONSTRUCTOR_LINK, 'class', MainPageLocators.ACTIVE_TEXT))

    @allure.step('Проверяем, что Лента заказов становится активным')
    def feed_is_active(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                MainPageLocators.FEED_LINK, 'class', MainPageLocators.ACTIVE_TEXT))

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



