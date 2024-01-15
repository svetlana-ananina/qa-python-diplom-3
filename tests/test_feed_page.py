import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.profile_page import ProfilePage


class TestFeedPage:

    @allure.title('Проверяем что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_click_order(self, create_new_user_by_api, get_browser, login_new_user, create_order):
        # Используем фикстуры для подготовки данных:
        #   регистрируем нового пользователя через API
        #   открываем окно веб-браузера
        #   авторизуем пользователя
        #   создаем заказ

        driver = get_browser
        # Открываем Ленту заказов
        feed_page = FeedPage(driver)
        feed_page.open_feed_page()
        # кликаем 1й заказ в ленте
        feed_page.click_order_link()

        # ждем что открылось модальное окно деталей заказа
        assert feed_page.order_details_is_opened()


    @allure.title('Проверяем что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_are_in_feed(self, create_new_user_by_api, get_browser, login_new_user, create_order):
        # Используем фикстуры для подготовки данных:
        #   регистрируем нового пользователя через API
        #   открываем окно веб-браузера
        #   авторизуем пользователя
        #   создаем заказ

        # получаем веб-драйвер
        driver = get_browser
        # получаем номер заказа из истории в Личном кабинете пользователя
        profile_page = ProfilePage(driver)
        order = profile_page.get_order_from_order_history()
        # получаем список номеров заказов в Ленте
        feed_page = FeedPage(driver)
        feed_order_list = feed_page.get_order_number_list()

        # проверяем, что заказ в ленте
        assert order in feed_order_list, f'Ошибка проверки Ленты заказов: заказ пользователя: {order} отсутствует в Ленте'


    @allure.title('Проверяем что после оформления заказа его номер появляется в разделе В работе')
    def test_user_order_is_in_work(self, create_new_user_by_api, get_browser, login_new_user, create_order):
        # Используем фикстуры для подготовки данных:
        #   регистрируем нового пользователя через API
        #   открываем окно веб-браузера
        #   авторизуем пользователя
        #   создаем заказ

        driver = get_browser        # получаем веб-драйвер
        new_order = create_order    # сохраняем номер созданного заказа
        constructor_page = ConstructorPage(driver)
        # переходим к Ленте заказов по ссылке на Главной странице
        constructor_page.click_feed_link()
        # получаем список номеров заказов в Ленте
        feed_page = FeedPage(driver)
        orders_list_in_work = feed_page.get_order_list_in_work()

        # проверяем что новый заказ есть в списке
        assert new_order in orders_list_in_work, f'Ошибка проверки раздела "В работе": созданный заказ не отображается в разделе'


    @allure.title('Проверяем что создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_orders_total_counter(self, get_browser, create_new_user_by_api, login_new_user):
        # Используем фикстуры для подготовки данных:
        #   регистрируем нового пользователя через API
        #   открываем окно веб-браузера
        #   авторизуем пользователя

        driver = get_browser        # получаем веб-драйвер
        # Открываем Ленту заказов
        feed_page = FeedPage(driver)
        # кликаем ссылку на Ленту заказов на главной странице
        feed_page.open_feed_page()
        # получаем счетчик заказов за все время
        orders_before = feed_page.get_orders_total()
        # открываем страницу Конструктор и оформляем заказ
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order()
        # Открываем Ленту заказов
        feed_page.open_feed_page()
        # получаем счетчик заказов за все время
        orders_after = feed_page.get_orders_total()

        # проверяем что счетчик увеличился
        assert orders_after > orders_before, f'Ошибка проверки раздела "Выполнено за все время": счетчик не увеличился'


    @allure.title('Проверяем что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_orders_today_counter(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузера и страницу профиля
        driver = login_new_user
        # Открываем Ленту заказов
        feed_page = FeedPage(driver)
        # кликаем ссылку на Ленту заказов на главной странице
        feed_page.open_feed_page()
        # получаем счетчик заказов за все время
        orders_before = feed_page.get_orders_today()
        # открываем страницу Конструктор и оформляем заказ
        constructor_page = ConstructorPage(driver)
        constructor_page.create_order()
        # Открываем Ленту заказов
        feed_page.open_feed_page()
        # получаем счетчик заказов за все время
        orders_after = feed_page.get_orders_today()

        # проверяем что счетчик увеличился
        assert orders_after > orders_before, f'Ошибка проверки раздела "Выполнено за сегодня": счетчик не увеличился, было {orders_before}, стало {orders_after}'

