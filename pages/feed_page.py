import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL, FeedPageLocators
from pages.main_page import MainPage


class FeedPage(MainPage):
    @allure.step('кликаем на 1-й заказ')
    def click_order_link(self):
        self.click_element_by_locator(FeedPageLocators.ORDER_LINK)

    @allure.step('Проверяем, что открывается модальное окно с деталями заказа')
    def order_details_is_opened(self):
        return self.wait_for_load_element(FeedPageLocators.ORDER_DETAILS_OPENED)

    @allure.step('Проверяем, что открывается карточка деталей')
    def get_order_number_list(self):
        return self.wait_for_load_all_elements(FeedPageLocators.ORDER_NUMBER)


