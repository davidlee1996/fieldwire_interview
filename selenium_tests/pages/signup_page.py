from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from selenium_tests.pages.base_page import BasePage


class SignUpPage(BasePage):
    FIRST_NAME_INPUT_FIELD = (By.XPATH, "//*[@id='firstNameInput']")
    LAST_NAME_INPUT_FIELD = (By.XPATH, "//*[@id='lastNameInput']")
    WORK_EMAIL_INPUT_FIELD = (By.XPATH, "//*[@id='emailInput']")
    PASSWORD_INPUT_FIELD = (By.XPATH, "//*[@id='passwordInput']")
    AGREE_CHECKBOX = (By.XPATH, "//*[@id='explicitAgreement']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='login']/form/input")
    LOGIN_BUTTON = (By.XPATH, "//*[@id='links']/a")
    PRIVACY_POLICY_LINK = (By.XPATH, "//*[@id='session']/div[2]/p/a")
    COMPANY_NAME_INPUT_FIELD = (By.XPATH, "//*[@id='company']")
    COMPANY_TYPE_DROPDOWN = (By.XPATH, "//*[@id='companyType']")
    COMPANY_SIZE_DROPDOWN = (By.XPATH, "//*[@id='companySize']")
    PHONE_NUMBER_INPUT_FIELD = (By.XPATH, "//*[@id='phone']")
    EMAIL_ALREADY_EXISTS_ALERT = (By.CSS_SELECTOR, "#session > div.alert.center.ng-scope.alert-danger")

    def __init__(self, driver):
        super().__init__(driver)
        self.uri = "auth/register"
        self.driver = driver

    def enter_first_name(self, first_name):
        self.find_element(self.FIRST_NAME_INPUT_FIELD).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.find_element(self.LAST_NAME_INPUT_FIELD).send_keys(last_name)

    def enter_email(self, email):
        self.find_element(self.WORK_EMAIL_INPUT_FIELD).send_keys(email)

    def enter_password(self, password):
        self.find_element(self.PASSWORD_INPUT_FIELD).send_keys(password)

    def check_agree(self):
        self.find_element(self.AGREE_CHECKBOX).click()

    def click_create_account(self):
        self.find_element(self.CREATE_ACCOUNT_BUTTON).click()

    def click_login(self):
        self.find_element(self.LOGIN_BUTTON).click()

    def click_privacy_policy(self):
        self.find_element(self.PRIVACY_POLICY_LINK).click()

    def enter_company_name(self, company_name):
        self.wait_for_element(self.COMPANY_NAME_INPUT_FIELD).send_keys(company_name)

    def choose_company_type(self, company_type):
        select = Select(self.wait_for_element(self.COMPANY_TYPE_DROPDOWN))
        select.select_by_value(company_type)

    def choose_company_size(self, company_size):
        select = Select(self.wait_for_element(self.COMPANY_SIZE_DROPDOWN))
        select.select_by_value(company_size)

    def enter_phone_number(self, phone_number):
        self.wait_for_element(self.PHONE_NUMBER_INPUT_FIELD).send_keys(phone_number)

    def is_create_account_clickable(self):
        return EC.element_to_be_clickable(self.CREATE_ACCOUNT_BUTTON)
