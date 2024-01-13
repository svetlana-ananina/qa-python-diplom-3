import allure

from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage


class HelpersOnPages:

    # def __open_profile_page_by_link(self):
    @staticmethod
    @allure.step('Открываем Личный кабинет по ссылке на Главной странице')
    def open_profile_page(driver):
        constructor_page = ConstructorPage(driver)
        constructor_page.open_profile_page_by_link()

    @staticmethod
    @allure.step('Получаем номер последнего заказа из Личного кабинета пользователя')
    def get_order_from_user_history(driver):
        # открываем Личный кабинет, кликаем ссылку История заказов и получаем номера заказов пользователя
        profile_page = ProfilePage(driver)
        # получаем список номеров заказов пользователя в формате "#..."
        user_order = profile_page.get_order_from_order_history()
        return user_order


