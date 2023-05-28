import pytest
from ArturTestStore.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ArturTestStore.src.pages.MyAccountSignIn import MyAccountSignedIn
from ArturTestStore.src.helpers.generic_helpers import generate_random_email_and_password





@pytest.mark.usefixtures("setup")
class TestRegisterNewUser:

    @pytest.mark.tcid2
    def test_register_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)


        # go to my account
        self.driver.get("http://arturteststore.local/my-account/")
        # my_account_o.go_to_my_account()
        # fill in email
        rand_email = generate_random_email_and_password()
        my_account_o.input_register_email(rand_email['email'])
        # fill in password
        my_account_o.input_register_password("123456Abcefg!")
        # click register
        my_account_o.click_register_button()
        # verify user is registred
        my_account_i.verify_user_is_signed_in()

