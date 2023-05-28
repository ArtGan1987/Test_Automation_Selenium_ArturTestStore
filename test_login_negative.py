import pytest
from ArturTestStore.src.pages.MyAccountSignedOut import MyAccountSignedOut
from selenium.webdriver.common.by import By





@pytest.mark.usefixtures("setup")
class TestLoginNegative:

    @pytest.mark.tcid1
    def test_login_none_existing_user(self):

        my_account = MyAccountSignedOut(self.driver)
        # go to my account
        self.driver.get("http://arturteststore.local/my-account/")
        # type username
        my_account.input_login_username("wdwdedw")
        # type password
        my_account.input_login_password("ferfe")
        # click login button
        my_account.click_login_button()
        # verify error message

        expected_err = "Error: The username wdwdedw is not registered on this site." \
                       " If you are unsure of your username, try your email address instead."
        assert expected_err in self.driver.find_element(By.CSS_SELECTOR, "ul.woocommerce-error").text

