from selenium.webdriver.common.by import By
from selenium_tests.pages.base_page import BasePage


class LoginPage(BasePage):

    NEXT_BUTTON = (By.XPATH, "//*[@id='auth-sign-in']/div[1]/form/input")
    NEXT_BUTTON_PASSWORD = (By.XPATH, "//*[@id='auth-sign-in-with-password']/div[1]/form/input")
    ACCOUNT_LOCKED_LINK = (By.XPATH, "//*[@id='links']/div/a")
    CREATE_ACCOUNT_LINK = (By.XPATH, "//*[@id='signup-link']/a")
    EMAIL_INPUT_FIELD = (By.XPATH, "//*[@id='email-input']")
    PASSWORD_INPUT_FIELD = (By.XPATH, "//*[@id='password-input']")
    EMAIL_NOT_FOUND_ALERT = (By.CSS_SELECTOR, "#auth-sign-in > div.alert.center.ng-scope.alert-danger")
    PASSWORD_INCORRECT_ALERT = (By.CSS_SELECTOR, "#auth-sign-in-with-password > div.alert.center.ng-scope.alert-danger")

    def __init__(self, driver):
        super().__init__(driver)
        self.uri = "auth/sign_in"
        self.driver = driver

    def enter_email(self, email):
        self.wait_for_element(self.EMAIL_INPUT_FIELD).send_keys(email)

    def enter_password(self, password):
        self.wait_for_element(self.PASSWORD_INPUT_FIELD).send_keys(password)

    def click_next(self):
        self.wait_for_element(self.NEXT_BUTTON).click()

    def click_next_password(self):
        self.wait_for_element(self.NEXT_BUTTON_PASSWORD).click()

    def click_account_locked(self):
        self.wait_for_element(self.ACCOUNT_LOCKED_LINK).click()

    def click_create_account(self):
        self.wait_for_element(self.CREATE_ACCOUNT_LINK).click()
