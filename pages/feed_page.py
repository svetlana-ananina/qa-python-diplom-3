import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL, FeedPageLocators
from pages.main_page import MainPage


class FeedPage(MainPage):
    @allure.step('кликаем на 1-й ингредиент')
    def click_order_link(self):
        self.click_element_by_locator(FeedPageLocators.ORDER_LINK)

    @allure.step('Проверяем, что открывается карточка деталей')
    def order_details_is_opened(self):
        return self.wait_for_load_element(FeedPageLocators.ORDER_DETAILS_OPENED_LINK)


