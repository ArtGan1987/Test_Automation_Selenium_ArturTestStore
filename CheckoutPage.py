from ArturTestStore.src.SeleniumExtended import SeleniumExtended
from ArturTestStore.src.pages.locators.CheckoutPageLocator import CheckoutPageLocator



class CheckoutPage(CheckoutPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name=None):
        first_name = first_name if first_name else 'AutomationFName'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'AutomationLName'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME, last_name)

    def input_billing_street_address(self, address1=None):
        address1 = address1 if address1 else 'AutomationStreet'
        self.sl.wait_and_input_text(self.BILLING_ADDRESS, address1)

    def input_billing_postalcode(self, postalcode=None):
        postalcode = postalcode if postalcode else '12-123'
        self.sl.wait_and_input_text(self.BILLING_POSTCODE, postalcode)

    def input_billing_city(self, billing_city=None):
        billing_city = billing_city if billing_city else 'AutomationCity'
        self.sl.wait_and_input_text(self.BILLING_CITY, billing_city)

    def input_billing_phone(self, billing_phone=None):
        billing_phone = billing_phone if billing_phone else '123456789'
        self.sl.wait_and_input_text(self.BILLING_PHONE, billing_phone)

    def input_billing_email(self, billing_email=None):
        billing_email = billing_email if billing_email else 'Test@gmail.com'
        self.sl.wait_and_input_text(self.BILLING_EMAIL, billing_email)

    def fill_billing_info(self, first_name=None, last_name=None, address1=None, postalcode=None, billing_city=None
        , billing_phone=None, billing_email=None):
        self.input_billing_first_name(first_name)
        self.input_billing_last_name(last_name)
        self.input_billing_street_address(address1)
        self.input_billing_postalcode(postalcode)
        self.input_billing_city(billing_city)
        self.input_billing_phone(billing_phone)
        self.input_billing_email(billing_email)

    def click_place_order(self):
        self.sl.wait_and_click(self.PLACE_ORDER_BTN)







