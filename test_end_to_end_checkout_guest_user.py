import pdb
import pytest
from ArturTestStore.src.helpers.database_helpers import get_order_from_db_by_order_no
from ArturTestStore.src.pages.HomePage import HomePage
from ArturTestStore.src.pages.Header import Header
from ArturTestStore.src.pages.CartPage import CartPage
from ArturTestStore.src.pages.CheckoutPage import CheckoutPage
from ArturTestStore.src.configs.general_configs import GeneralConfigs
from ArturTestStore.src.pages.OrderReceivedPage import OrderReceivedPage


@pytest.mark.usefixtures("setup")
class TestEndToEndCheckoutGuestUser:

    @pytest.mark.tcid3
    def test_end_to_end_checkout_guest_user(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_received_p = OrderReceivedPage(self.driver)

        # go to home page
        home_p.go_to_home_page()
        # add 1 item to cart
        home_p.click_first_add_to_cart_button()
        # make sure the cart is updated before going to cart
        header.wait_until_cart_item_count(1)
        # go to cart and verify products
        header.click_on_cart_on_right_header()
        product_names = cart_p.get_all_product_names_in_cart()
        assert len(product_names) == 1, f"Expected 1 item in cart, but found {len(product_names)}"
        # apply coupon
        coupon_code = GeneralConfigs.FREE_COUPON
        cart_p.apply_coupon(coupon_code)
        # click on proceed checkout
        cart_p.click_on_proceed_to_checkout()
        # fill the form
        checkout_p.fill_billing_info()
        # click on place order, # in this place it stops from time to time...it will be fixed
        checkout_p.click_place_order()
        # verify order is received
        order_received_p.verify_order_received_page_loaded()
        # verify order is recorded in db (via SQL or via API)
        order_no = order_received_p.get_order_number()
        db_order = get_order_from_db_by_order_no(order_no)
        assert db_order, f"After creating order with FE, not found in DB." \
                        f"Order no: {order_no}"
        

