from ArturTestStore.src.pages.locators.OrderReceivedPageLocator import OrderReceivedPageLocator
from ArturTestStore.src.SeleniumExtended import SeleniumExtended


class OrderReceivedPage (OrderReceivedPageLocator):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def verify_order_received_page_loaded(self):
        self.sl.wait_until_element_cointains_text(self.PAGE_MAIN_HEADER, 'Order received')

    def get_order_number(self):
        return self.sl.wait_and_get_text(self.ORDER_NUMBER)






