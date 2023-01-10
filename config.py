LEVERAGE = 1
EPSILON = 0.000001
INF = 10 ** 20
WALLET_USAGE_PERCENT = 50.0  # must be between 0.0 and 100.0
STRATEGIES_COUNT = 4
MAXIMUM_NUMBER_OF_API_CALL_TRIES = 5
INDICATORS_DICT_FILENAME = "indicators_dict.pkl"
ORDERS_DICT_FILENAME = "orders_dict.pkl"
ONE_MINUTE_IN_MILLISECONDS = 60 * 1000
MAXIMUM_KLINE_CANDLES_PER_REQUEST = 1000
ERROR = -1
SUCCESSFUL = 0
SLEEP_INTERVAL = 0.25
HANDLING_POSITIONS_TIME_SECOND = 0  # must be between 0 and 59
FIRST_COIN_SYMBOL = "USDT"
SECOND_COIN_SYMBOL = "BTC"
CONTRACT_SYMBOL = SECOND_COIN_SYMBOL + FIRST_COIN_SYMBOL
TIMEFRAME = "h1"    # m1 m15 h1 h2 h4 d1
TAKE_PROFIT_PERCENTS = [2, 3, 1.5, 2]  # len(TAKE_PROFIT_PERCENTS) must equals STRATEGIES_COUNT
STOP_LOSS_PERCENTS = [-1, -1, -1.5, -1.5]  # len(STOP_LOSS_PERCENTS) must equals STRATEGIES_COUNT
PRICE_DECIMAL_DIGITS = 2
INDICATORS_DECIMAL_DIGITS = 2
POSITION_QUANTITY_DECIMAL_DIGITS = 3
PRICE_DIRECTION_INDICATOR_NAME_1 = "ema_20"
PRICE_DIRECTION_INDICATOR_NAME_2 = "ema_50"
NEW_CLIENT_ORDER_ID_PREFIX = "aRandomString"
LAST_ACCOUNT_BALANCES_LIST_MAX_LENGTH = 12
IMPORTANT_CANDLES_COUNT = 100
SEND_TELEGRAM_MESSAGE = False
HEDGE_MOODE = True    # True to allow long and short positions simultaneously
IS_TESTNET = True   # True to enable mode teste for Binance
URL_BASE_PRODUCTION = "https://fapi.binance.com"
URL_BASE_TESTNET = "https://testnet.binancefuture.com"
