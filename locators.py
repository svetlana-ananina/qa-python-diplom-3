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
    DETAILS_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal")]')
    DETAILS_OPENED_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]')
    #DETAILS_OPENED_TEXT = 'Modal-modal_opened'
    DETAILS_TITLE_LINK = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    DETAILS_CLOSE_LINK = (By.XPATH, './/section[contains(@class,"Modal_modal_opened")]//button')
    DETAILS_LINK_CLASS = 'Modal_modal__P3_V5'
    DRAGNDROP_BUN_TARGET = (By.XPATH, './/span[text()="Перетяните булочку сюда (верх)"]')

    # Вкладка Лента заказов


class ProfilePageLocators:
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")               # Кнопка "Сохранить"
    ORDER_HISTORY_LINK = (By.XPATH, ".//a[@href='/account/order-history']") # Ссылка История заказов
    #ORDER_HISTORY_LINK = (By.XPATH, ".//a[text()='Профиль']")              # Ссылка История заказов
    ORDER_HISTORY_ACTIVE_TEXT = 'Account_link_active'                       # История заказов активна
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Выход']")                   # Кнопка "Выход"


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



