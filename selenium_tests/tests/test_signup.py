import random
import string
import pytest
from selenium_tests.pages.signup_page import SignUpPage


@pytest.mark.usefixtures("setup")
class TestSignup:

    def test_signup(self):
        signup_page = SignUpPage(self.driver)
        signup_page.open(signup_page.uri)
        signup_page.enter_first_name("Tester")
        signup_page.enter_last_name("Test")
        signup_page.enter_email("".join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "@gmail.com")
        signup_page.enter_password("test1234")
        signup_page.check_agree()
        signup_page.click_create_account()
        signup_page.enter_company_name("Testing Company")
        signup_page.choose_company_type("OTHER")
        signup_page.choose_company_size("size_1_10")
        signup_page.enter_phone_number("8181115555")
        signup_page.click_create_account()

    #alert that email exists appears
    def test_email_already_exists(self):
        signup_page = SignUpPage(self.driver)
        signup_page.open(signup_page.uri)
        signup_page.enter_first_name("Tester")
        signup_page.enter_last_name("Test")
        signup_page.enter_email("davidlee1996@gmail.com")
        signup_page.enter_password("test1234")
        signup_page.check_agree()
        signup_page.click_create_account()
        signup_page.does_element_exist(signup_page.EMAIL_ALREADY_EXISTS_ALERT)

    # not clickable until all required fields are filled
    def test_agree_not_checked(self):
        signup_page = SignUpPage(self.driver)
        signup_page.open(signup_page.uri)
        signup_page.enter_first_name("Tester")
        signup_page.enter_last_name("Test")
        signup_page.enter_email("".join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "@gmail.com")
        signup_page.enter_password("test1234")
        assert signup_page.is_create_account_clickable()

    #Bug found
    #Expected Result: should not be clickable
    #Actual Result: It is clickable despite having First name missing
    def test_first_name_missing(self):
        signup_page = SignUpPage(self.driver)
        signup_page.open(signup_page.uri)
        signup_page.enter_last_name("Test")
        signup_page.enter_email("".join(random.choices(string.ascii_uppercase + string.digits, k=10)) + "@gmail.com")
        signup_page.enter_password("test1234")
        signup_page.check_agree()
        assert not signup_page.is_create_account_clickable()
