import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        # Открываем страницу авторизации
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element_attribute(
                ProfilePageLocators.ORDER_HISTORY_LINK, 'class', ProfilePageLocators.ORDER_HISTORY_ACTIVE_TEXT))     #.visibility_of_element_located(locator))


