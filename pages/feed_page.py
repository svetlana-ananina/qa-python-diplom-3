import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators, FEED_PAGE_URL


class FeedPage(BasePage):

    @allure.step('кликаем на 1-й ингредиент')
    def drag_and_drop_bun(self):
        source = self.wait_for_load_element(MainPageLocators.INGREDIENT_LINK)
        target = self.wait_for_load_element(MainPageLocators.DRAGNDROP_BUN_TARGET)
        self.drag_and_drop(source, target)
        # _sleep(5)


