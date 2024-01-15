_browser = 'Chrome'
#_browser = 'Firefoxe'


# тестовые данные для функции восстановления пароля
class UserData:
    USER_EMAIL = 'ivanivanov@mail.ru'
    USER_PASSWORD = '123456'


class Urls:
    FORGOT_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/forgot-password'  # URL страницы восстановления пароля
    LOGIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site/login'  # URL для страницы авторизации
    RESET_PASSWORD_PAGE_URL = 'https://stellarburgers.nomoreparties.site/reset-password'  # URL страницы восстановления пароля
    PROFILE_PAGE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'  # URL для страницы Личный кабинет
    ORDER_HISTORY_URL = 'https://stellarburgers.nomoreparties.site/account/order-history'  # URL для страницы Личный кабинет
    MAIN_PAGE_URL = 'https://stellarburgers.nomoreparties.site'  # URL для Главной страницы
    FEED_PAGE_URL = 'https://stellarburgers.nomoreparties.site/feed'  # URL для Главной страницы


class RESPONSE_KEYS:

    # поля в ответе API
    ACCESS_TOKEN    = 'accessToken'     # str: "Bearer ..."
    REFRESH_TOKEN   = 'refreshToken'    # str: ""

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'   # delete: headers
    TOKEN_KEY       = 'token'           # logout: body, ="refreshToken"

