class BaseConfig:
    GENERATE_CHECKOUT_URL = "https://payments.ipayafrica.com/v3/ke"
    INITIATOR_URL = "https://apis.ipayafrica.com/payments/v2/transact"
    CARD_PAYMENT_URL = "https://apis.ipayafrica.com/payments/v2/transact/cc"
    PAYMENT_STATUS_URL = "https://apis.ipayafrica.com/payments/v2/transaction/search"
    PAYMENT_REFUND_URL = "https://apis.ipayafrica.com/payments/v2/transaction/refund"
