import allure

from data import Urls
from locators import MainPageLocators, ProfilePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Открываем Главную страницу')
    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)
        self.wait_for_load_element(MainPageLocators.ANY_BUTTON)

    @allure.step('Открываем Ленту заказов')
    def open_feed_page(self):
        self.open_page(Urls.FEED_PAGE_URL)
        self.wait_for_load_element(MainPageLocators.TOTAL_TODAY)

    @allure.step('кликаем ссылку "Личный кабинет"')
    def click_profile_link(self):
        self.click_element_by_locator(MainPageLocators.PROFILE_LINK)

    @allure.step('кликаем ссылку "Конструктор"')
    def click_constructor_link(self):
        self.click_element_by_locator(MainPageLocators.CONSTRUCTOR_LINK)

    @allure.step('кликаем ссылку "Лента заказов"')
    def click_feed_link(self):
        self.click_element_by_locator(MainPageLocators.FEED_LINK)

    @allure.step('Проверяем, что Конструктор становится активным')
    def constructor_is_active(self):
        return self.wait_for_text_in_classname(MainPageLocators.CONSTRUCTOR_LINK,
                                               MainPageLocators.ACTIVE_TEXT)

    @allure.step('Проверяем, что Лента заказов становится активным')
    def feed_is_active(self):
        return self.wait_for_text_in_classname(MainPageLocators.FEED_LINK,
                                               MainPageLocators.ACTIVE_TEXT)

    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def open_profile_page_by_link(self):
        self.open_main_page()
        self.wait_for_load_element(MainPageLocators.ORDER_BUTTON)
        # кликаем Личный кабинет в хедере
        self.click_profile_link()
        # ждем перехода в Личный кабинет и появления кнопки "Сохранить"
        self.wait_for_load_element(ProfilePageLocators.SAVE_BUTTON)

