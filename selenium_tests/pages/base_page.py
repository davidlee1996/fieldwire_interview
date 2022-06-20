import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_tests.utils import config_utils


class BasePage(object):

    def __init__(self, driver):
        self.base_url = config_utils.get_base_url()
        self.driver = driver
        self.timeout = 30

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def open(self, uri):
        url = self.base_url + uri
        self.driver.get(url)
        self.driver.set_page_load_timeout(10)
        time.sleep(2)

    def reload(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url()

    def wait_for_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator))
        return element

    def does_element_exist(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
