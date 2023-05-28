from ArturTestStore.src.SeleniumExtended import SeleniumExtended
from ArturTestStore.src.pages.locators.HomePageLocator import HomePageLocator


class HomePage(HomePageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_home_page(self):
        self.driver.get('http://arturteststore.local/')

    def click_first_add_to_cart_button(self):
        self.sl.wait_and_click(self.ADD_TO_CART_BTN)
