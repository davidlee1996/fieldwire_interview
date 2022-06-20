import pytest
from selenium_tests.pages.login_page import LoginPage


@pytest.mark.usefixtures("setup")
class TestLogin:

    # Test Case: Test that Next button can't be clicked with empty field
    # Test Case: Entering correct info leads to successful login
    def test_success_login(self):
        login_page = LoginPage(self.driver)
        login_page.open(login_page.uri)
        login_page.enter_email("davidlee1996@gmail.com")
        login_page.click_next()
        login_page.enter_password("dlee06991")
        login_page.click_next_password()

    # Test Case: Right Username but wrong pw
    def test_failure_login_password(self):
        login_page = LoginPage(self.driver)
        login_page.open(login_page.uri)
        login_page.enter_email("davidlee1996@gmail.com")
        login_page.click_next()
        login_page.enter_password("dddddddd")
        login_page.click_next_password()
        assert login_page.does_element_exist(login_page.PASSWORD_INCORRECT_ALERT)

    # Test Case: Invalid username
    def test_failure_login_username(self):
        login_page = LoginPage(self.driver)
        login_page.open(login_page.uri)
        login_page.enter_email("fake_user@gmail.com")
        login_page.click_next()
        assert login_page.does_element_exist(login_page.EMAIL_NOT_FOUND_ALERT)
