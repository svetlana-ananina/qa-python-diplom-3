from selenium.webdriver.common.by import By


class LoginPageLocators:
    FORGOT_PAGE_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")         # Ссылка "Восстановить пароль" на странице авторизации
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")                      # Кнопка "Войти"
    #FORGOT_PAGE_LINK = (By.XPATH, ".//a[@href='/account']")                    # не прокручивается, не кликается


class ForgotPasswordPageLocators:
    RECOVER_TITLE = (By.XPATH, ".//h2[text()='Восстановление пароля']")     # Заголовок
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")         # Кнопка "Восстановить"


