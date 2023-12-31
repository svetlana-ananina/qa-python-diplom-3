import allure

from pages.base_page import BasePage
from locators import MAIN_PAGE_URL, MainPageLocators


class MainPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_main_page(self):
        # Открываем страницу авторизации
        self.open_page(MAIN_PAGE_URL)

    @allure.step('Ждем загрузку и кликаем ссылку "Восстановить пароль"')
    def register_new_user(self):
        pass

    @allure.step('кликаем ссылку "Личный кабинет"')
    def click_profile_link(self):
        # кликаем ссылку "Личный кабинет"
        self.click_element_by_locator(MainPageLocators.PROFILE_LINK)
        #_sleep(5)


