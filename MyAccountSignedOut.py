from ArturTestStore.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ArturTestStore.src.SeleniumExtended import SeleniumExtended
# from ArturTestStore.src.helpers import get_base_url



class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_my_account(self):
        base_url = "http://arturteststore.local/my-account"
        # base_url = get_base_url()
        # my_account_url = base_url + endpoint
        self.driver.get(base_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_USER_NAME)
        #                                      ).send_keys(username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

        #WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_PASSWORD)
        #                                     ).send_keys(password)

    def click_login_button(self):
        self.sl.wait_and_click(self.LOGIN_BTN)

        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BTN)
        #                                     ).click()
    #rejestracja
    def input_register_email(self, email):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, email)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        self.sl.wait_and_click(self.REGISTER_BTN)

