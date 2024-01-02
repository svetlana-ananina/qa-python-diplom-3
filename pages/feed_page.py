import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL


class FeedPage(BasePage):

    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        self.open_page(MAIN_PAGE_URL)
        #self.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        self.wait_for_load_element(MainPageLocators.ANY_BUTTON)

    @allure.step('Открываем Ленту заказов')
    def open_feed_page(self):
        self.open_page(FEED_PAGE_URL)
        self.wait_for_load_element(MainPageLocators.TOTAL_TODAY)

