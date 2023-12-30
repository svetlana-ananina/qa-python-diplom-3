from selenium.webdriver.common.by import By


FORGOT_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
LOGIN_PAGE_URL           = 'https://stellarburgers.nomoreparties.site/login'            # URL для страницы авторизации
RESET_PASSWORD_PAGE_URL  = 'https://stellarburgers.nomoreparties.site/reset-password'   # URL страницы восстановления пароля


class LoginPageLocators:
    FORGOT_PAGE_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")         # Ссылка "Восстановить пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")                      # Кнопка "Войти"
    #FORGOT_PAGE_LINK = (By.XPATH, ".//a[@href='/account']")                    # не прокручивается, не кликается


class ForgotPasswordPageLocators:
    RECOVER_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")     # Заголовок
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")         # Кнопка "Восстановить"
    EMAIL_FIELD = (By.XPATH, ".//input[@type='text']")                      # поле ввода "email"
    MODAL_SCROLL_ELEMENT = (By.XPATH, ".//div[@class='Modal_modal_overlay__x2ZCr']")                      # поле ввода "email"


class ResetPasswordPageLocators:
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")               # Кнопка "Сохранить"
    EYE_ICON    = (By.XPATH, ".//dev[@class='input__icon input__icon-action']")
    PASSWORD_PLACEHOLDER = (By.XPATH, ".//label[text()='Пароль']")          # Плейсхолдер поля "Пароль"
    #'input__placeholder text noselect text_type_main-default'
    #'focuced'

