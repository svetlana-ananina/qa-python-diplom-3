_to_print = True
#_to_print = False

_browser = 'Chrome'
#_browser = 'Firefoxe'

_to_sleep_ff = True

_to_sleep = True
#_to_sleep = False


#class STATUS_CODES:

#    OK              = 200
#    CREATED         = 201
#    ACCEPTED        = 202
#    BAD_REQUEST     = 400
#    UNAUTHORIZED    = 401
#    FORBIDDEN       = 403
#    NOT_FOUND       = 404
#    CONFLICT        = 409
#    ERROR_500       = 500       # Internal Server Error


class RESPONSE_KEYS:

    # поля в ответе API
    #SUCCESS_KEY     = 'success'
    #USER_KEY        = 'user'
    #EMAIL_KEY       = 'email'
    #NAME_KEY        = 'name'
    ACCESS_TOKEN    = 'accessToken'     # str: "Bearer ..."
    REFRESH_TOKEN   = 'refreshToken'    # str: ""

    #INGREDIENTS     = 'ingredients'
    #ID_KEY          = '_id'
    #DATA            = 'data'            # GET /api/ingredients: 'success': True, 'data': [{...}, ... ]

    #TYPE_KEY        = 'type'            # тип ингредиента: "bun", "main", "sauce"
    #TYPE_BUN        = 'bun'
    #TYPE_MAIN       = 'main'            # основной ингредиент - начинка (filling)
    #TYPE_SAUCE      = 'sauce'

    #ORDER_KEY       = 'order'
    #NUMBER_KEY      = 'number'
    #ORDERS_KEY      = 'orders'
    #TOTAL_KEY       = 'total'
    #TOTAL_TODAY_KEY = 'totalToday'

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'   # delete: headers
    #PASSWORD_KEY    = 'password'
    TOKEN_KEY       = 'token'           # logout: body, ="refreshToken"
    #ACCESS_TOKEN_PREFIX = "Bearer "

