from selenium.webdriver.common.by import By
from selenium_tests.pages.base_page import BasePage


class ProjectsPage(BasePage):
    NEW_PLAN_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div[1]/div[1]")
    NEW_FOLDER_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div[1]/fw-button")
    ACTIONS_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div["
                                "1]/fw-context-menu")
    FILTER_PLANS_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div[2]/div["
                                     "1]/filter-entities-button")
    VERSION_CONTROL_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div["
                                        "2]/div[2]")
    GRID_VIEW_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div[2]/div["
                                  "3]/fw-button[1]")
    LIST_VIEW_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div[2]/div["
                                  "3]/fw-button[2]")
    GET_STARTED_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div["
                                    "2]/video-modal-opener/div/div/div/div[1]/img[1]")
    SELECT_FILES_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div[1]/button")
    SELECT_FILES_DROP_AREA = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[2]/div[2]/div/div")
    FILESTACK_MY_DEVICE = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[1]")
    FILESTACK_DROPBOX = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[2]")
    FILESTACK_BOX = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[3]")
    FILESTACK_DRIVE = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[4]")
    FILESTACK_ONEDRIVE = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[5]")
    FILESTACK_ONEDRIVE_BUSINESS = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[6]")
    FILESTACK_LINK = (By.XPATH, "//*[@id='__filestack-picker']/div[1]/div[1]/div[1]/div/div[7]")
    LEFT_SIDEBAR_PLANS = (By.XPATH, "//*[@id='sidebar-wrapper']/div/ul/div/li[1]/a")
    LEFT_SIDEBAR_TASKS = (By.XPATH, "//*[@id='sidebar-wrapper']/div/ul/div/li[2]/a")
    LEFT_SIDEBAR_PHOTOS = (By.XPATH, "//*[@id='sidebar-wrapper']/div/ul/div/li[3]/a")
    LEFT_SIDEBAR_FORMS = (By.XPATH, "//*[@id='sidebar-wrapper']/div/ul/div/li[4]/a")
    LEFT_SIDEBAR_FILES = (By.XPATH, "//*[@id='sidebar-wrapper']/div/ul/div/li[5]/a")
    LEFT_SIDEBAR_MENU = (By.XPATH, "//*[@id='page-content-wrapper']/nav/div[1]/button[1]")
    NEW_TASK_BUTTON = (By.XPATH, "//*[@id='page-content-wrapper']/div/div/div[2]/div/div/div[3]/div/div[1]/fw-button[1]")
    CLOSE_MODAL_BUTTON = (By.CLASS_NAME, "close-modal")

    def __init__(self, driver):
        super().__init__(driver)
        self.uri = ""
        self.driver = driver

    def click_new_plan(self):
        self.wait_for_element(self.NEW_PLAN_BUTTON).click()

    def click_new_folder(self):
        self.wait_for_element(self.NEW_FOLDER_BUTTON).click()

    def click_actions_dropdown(self):
        self.wait_for_element(self.ACTIONS_BUTTON).click()

    def click_filter_plans(self):
        self.wait_for_element(self.FILTER_PLANS_BUTTON).click()

    def click_version_control(self):
        self.wait_for_element(self.VERSION_CONTROL_BUTTON).click()

    def click_sidebar_menu(self):
        self.wait_for_element(self.LEFT_SIDEBAR_MENU).click()

    def click_sidebar_tasks(self):
        self.wait_for_element(self.LEFT_SIDEBAR_TASKS).click()

    def click_new_task(self):
        self.wait_for_element(self.NEW_TASK_BUTTON).click()

    def close_modal(self):
        self.wait_for_element(self.CLOSE_MODAL_BUTTON).click()

