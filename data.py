_to_print = True
#_to_print = False

_browser = 'Chrome'
#_browser = 'Firefoxe'

_to_sleep_ff = True

_to_sleep = True
#_to_sleep = False


class RESPONSE_KEYS:

    # поля в ответе API
    ACCESS_TOKEN    = 'accessToken'     # str: "Bearer ..."
    REFRESH_TOKEN   = 'refreshToken'    # str: ""

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'   # delete: headers
    TOKEN_KEY       = 'token'           # logout: body, ="refreshToken"

