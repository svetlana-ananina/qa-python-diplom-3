from selenium.webdriver.common.by import By


#RECOVER_EMAIL = 'ivanivanov@mail.ru'
USER_EMAIL = 'ivanivanov@mail.ru'
USER_PASSWORD = '123456'


FORGOT_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
LOGIN_PAGE_URL           = 'https://stellarburgers.nomoreparties.site/login'            # URL для страницы авторизации
RESET_PASSWORD_PAGE_URL  = 'https://stellarburgers.nomoreparties.site/reset-password'   # URL страницы восстановления пароля
PROFILE_PAGE_URL         = 'https://stellarburgers.nomoreparties.site/account/profile'  # URL для страницы Личный кабинет
ORDER_HISTORY_URL        = 'https://stellarburgers.nomoreparties.site/account/order-history'  # URL для страницы Личный кабинет
MAIN_PAGE_URL            = 'https://stellarburgers.nomoreparties.site'                  # URL для Главной страницы
FEED_PAGE_URL            = 'https://stellarburgers.nomoreparties.site/feed'             # URL для Главной страницы


class MainPageLocators:
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")         # Кнопка "Оформить заказ" на Главной странице
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")        # Кнопка "Войти в аккаунт" на Главной странице
    PROFILE_LINK = (By.XPATH, ".//a[@href='/account']")                     # Ссылка Личный кабинет
    CONSTRUCTOR_LINK = (By.XPATH, ".//a[@href='/']")                        # ссылка на Конструктор
    FEED_LINK = (By.XPATH, ".//a[@href='/feed']")                           # ссылка на Ленту заказов
    ACTIVE_TEXT = 'link_active'                                             # текст в классе активной вкладки
    TOTAL_TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']")        # Последний элемент нв странице Лента заказов
    ANY_BUTTON = (By.XPATH, ".//button")                                    # Кнопка "Оформить заказ"/"Войти в аккаунт" на Главной странице

    # Вкладка Конструктор:
    INGREDIENT_LINK = (By.XPATH, '//*[contains(@href,"/ingredient/")]')     # 1й ингредиент из 15 (булка)
#    DETAILS_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal")]')
    DETAILS_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
    #DETAILS_OPENED_TEXT = 'Modal-modal_opened'
    DETAILS_TITLE_LINK = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    DETAILS_CLOSE_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]//button')
    DETAILS_LINK_CLASS = 'Modal_modal__P3_V5'
    DRAGNDROP_BUN_TARGET = (By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]')
    INGREDIENT_COUNTER_LINK = (By.XPATH, '//*[contains(@href,"/ingredient/")]//p[contains(@class,"counter_counter__num")]')     # счетчик ингредиента
    INGREDIENT_3_LINK = (By.XPATH, '(//*[contains(@href,"/ingredient/")])[3]')     # 3й ингредиент из 15 (соус)
    INGREDIENT_7_LINK = (By.XPATH, '(//*[contains(@href,"/ingredient/")])[7]')     # 7й ингредиент из 15 (начинка)
    #DRAGNDROP_BURGER_TARGET = (By.XPATH, './/span[@class="constructor-element__row"]')      # 1й элемент бургера
    #DRAGNDROP_BURGER_TARGET = (By.XPATH, '//*[contains(@class,"BurgerConstructor_basket")]')
    DRAGNDROP_BURGER_TARGET = (By.XPATH, '//*[contains(@class,"BurgerConstructor_basket__list")]')

    # Модальное окно - заказ оформлен
    ORDER_ID_LINK = (By.XPATH, './/p[text()="Ваш заказ начали готовить"]')
    ORDER_MODAL_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_")]')                    # common/hidden
    #ORDER_MODAL_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened__")]')     # visible
    ORDER_MODAL_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened__3ISw4")]')     # visible
    ORDER_CLOSE_BUTTON = (By.XPATH, './/button[contains(@class,"Modal_modal__close")]')     # visible
    ORDER_MODAL_ORDER_NUMBER = (By.XPATH, './/h2[contains(@class,"Modal_modal__title_shadow")]')     # номер нового заказа

# h2 class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"


class FeedPageLocators:
    # Вкладка Лента заказов
    ORDER_LINK = (By.XPATH, '//*[contains(@href,"/feed/")]')
    ORDER_DETAILS_OPENED = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
    ORDER_LIST_ITEM = (By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]')
    #ORDER_LIST_ORDER_NUMBER = (By.XPATH, './/li/a/div/p[contains(@class,"digits")]')
    ORDER_LIST_ORDER_NUMBER = (By.XPATH, './/p[@class="text text_type_digits-default"]')
    ORDER_STATUS_BOX = (By.XPATH, './/div[contains(@class,"OrderFeed_orderStatusBox")]')
    ORDER_STATUS_BOX_LIST = (By.XPATH, './/ul[contains(@class,"OrderFeed_orderList")]')
    ORDER_STATUS_BOX_LIST1 = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[1]')
    ORDER_STATUS_BOX_LIST2 = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]')
    ORDER_STATUS_BOX_LIST1_ITEM = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[1]/li')
    ORDER_STATUS_BOX_LIST2_ITEM = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]/li')
    ORDER_STATUS_BOX_LIST2_ITEM_DIGIT = (By.XPATH, '(.//ul[contains(@class,"OrderFeed_orderList")])[2]/li[contains(@class,"digits")]')
# div 'OrderFeed_orderStatusBox'
# ul 'OrderFeed_orderList'
# li class="text text_type_main-small" 'Все текущие заказы готовы!
# li class = "text text_type_digits-default mb-2"

class ProfilePageLocators:
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")               # Кнопка "Сохранить"
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[@href='/account/order-history']") # Ссылка История заказов
    #ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='Профиль']")              # Ссылка История заказов
    ORDER_HISTORY_IS_ACTIVE = 'Account_link_active'                       # История заказов активна
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")                   # Кнопка "Выход"
    ORDER_HISTORY_ORDER_NUMBER = (By.XPATH, './/li[contains(@class,"OrderHistory_listItem")]/a/div/p[contains(@class,"digits")]')
    #ORDER_NUMBER_TEXT = (By.XPATH, './/p[@class="text text_type_digits-default"]')


class LoginPageLocators:
    FORGOT_PAGE_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")         # Ссылка "Восстановить пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")                      # Кнопка "Войти"
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")                          # Поле "email"
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")                   # Поле "Пароль"
    #FORGOT_PAGE_LINK = (By.XPATH, ".//a[@href='/account']")                    # не прокручивается, не кликается


class ForgotPasswordPageLocators:
    RECOVER_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")     # Заголовок
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")         # Кнопка "Восстановить"
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")                      # поле ввода "email"
    #MODAL_SCROLL_ELEMENT = (By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']")                      # поле ввода "email"


class ResetPasswordPageLocators:
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")               # Кнопка "Сохранить"
    #EYE_ICON    = (By.XPATH, ".//dev[@class='input__icon input__icon-action']")
    EYE_ICON    = (By.XPATH, '//*[contains(@class,"input__icon")]')
    PASSWORD_PLACEHOLDER = (By.XPATH, ".//label[text()='Пароль']")          # Плейсхолдер поля "Пароль"
    #'input__placeholder text noselect text_type_main-default'
    #'focuced'
    #FOCUSED_FIELD = (By.XPATH, '//*[contains(@class,"input__placeholder-focused")]')
    FOCUSED_FIELD = (By.XPATH, '//*[contains(@class,"input__placeholder")]')
    FOCUSED_TEXT = 'input__placeholder-focused'



