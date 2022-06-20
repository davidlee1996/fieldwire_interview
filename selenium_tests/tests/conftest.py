import random
import string
import time
import pytest

from selenium_tests.pages.index_projects_page import IndexProjectsPage
from selenium_tests.pages.login_page import LoginPage
from selenium_tests.pages.signup_page import SignUpPage
from selenium_tests.utils.driver_factory import DriverFactory
from selenium_tests.utils import config_utils
from selenium_tests.utils.webdriver_listener import WebDriverListener, log_test_start_messages

logger = WebDriverListener.logger


@pytest.fixture(scope='function')
def setup(request):
    config = config_utils.get_config_json()
    driver = DriverFactory.get_driver(config)
    request.cls.driver = driver
    if config["browser"] == "firefox":
        driver.maximize_window()
    yield
    driver.quit()


@pytest.fixture(scope='function')
def login(request, setup):
    login_page = LoginPage(request.cls.driver)
    log_test_start_messages(logger)
    login_page.open(login_page.uri)
    time.sleep(1)
    user_id = config_utils.get_user_id()
    user_pwd = config_utils.get_user_password()
    login_page.enter_email(user_id)
    login_page.click_next()
    login_page.enter_password(user_pwd)
    login_page.click_next_password()
    time.sleep(1)


@pytest.fixture(scope='function')
def signup(request, setup):
    signup_page = SignUpPage(request.cls.driver)
    log_test_start_messages(logger)
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
    signup_page.enter_phone_number("8185555555")
    signup_page.click_create_account()


@pytest.fixture(scope='function')
def create_project(request):
    index_projects_page = IndexProjectsPage(request.cls.driver)
    index_projects_page.click_new_project_box()
    index_projects_page.enter_project_name("project_test_new_user")
    index_projects_page.create_new_project()
    index_projects_page.close_modal()