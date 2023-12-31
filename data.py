_to_print = True
#_to_print = False

_browser = 'Chrome'
#_browser = 'Firefoxe'

_to_sleep_ff = True

_to_sleep = True
#_to_sleep = False


class STATUS_CODES:

    OK              = 200
    CREATED         = 201
    ACCEPTED        = 202
    BAD_REQUEST     = 400
    UNAUTHORIZED    = 401
    FORBIDDEN       = 403
    NOT_FOUND       = 404
    CONFLICT        = 409
    ERROR_500       = 500       # Internal Server Error


class RESPONSE_KEYS:

    # поля в ответе API
    ACCESS_TOKEN    = 'accessToken'     # str: "Bearer ..."
    REFRESH_TOKEN   = 'refreshToken'    # str: ""

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'   # delete: headers
    PASSWORD_KEY    = 'password'
    TOKEN_KEY       = 'token'           # logout: body, ="refreshToken"
    ACCESS_TOKEN_PREFIX = "Bearer "

