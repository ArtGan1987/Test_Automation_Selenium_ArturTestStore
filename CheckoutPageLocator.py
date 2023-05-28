from selenium.webdriver.common.by import By


class CheckoutPageLocator:

    BILLING_FIRST_NAME = (By.ID, 'billing_first_name')
    BILLING_LAST_NAME = (By.ID, 'billing_last_name')
    BILLING_ADDRESS = (By.ID, 'billing_address_1')
    BILLING_POSTCODE = (By.ID, 'billing_postcode')
    BILLING_CITY = (By.ID, 'billing_city')
    BILLING_PHONE = (By.ID, 'billing_phone')
    BILLING_EMAIL = (By.ID, 'billing_email')

    PLACE_ORDER_BTN = (By.ID, 'place_order')

