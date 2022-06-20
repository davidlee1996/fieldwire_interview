from selenium.webdriver.common.by import By
from selenium_tests.pages.base_page import BasePage


class IndexProjectsPage(BasePage):
    NEW_PROJECT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/ui-view/div[1]/div/button")
    NEW_PROJECT_BOX = (By.CSS_SELECTOR, ".new-project.pointer.project-box.relative-pos")
    SORT_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/ui-view/div[1]/div/div/div/div/button")
    FILTER_PROJECTS_FIELD = (By.XPATH, "/html/body/div[1]/div/div/div/ui-view/div[1]/div/div/input")
    PROJECT_NAME_FIELD = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[1]/input")
    PROJECT_CODE_FIELD = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[2]/input")
    CLONE_EXISTING_PROJECT_DROPDOWN = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[3]/select")
    COPY_CATEGORIES_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[1]/label/input")
    COPY_STATUSES_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[2]/label/input")
    COPY_PEOPLE_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[3]/label/input")
    COPY_CHECKLISTS_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[4]/label/input")
    COPY_REPORTS_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[5]/label/input")
    COPY_LOCATIONS_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[6]/label/input")
    COPY_TAGS_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[7]/label/input")
    COPY_FORM_TEMPLATES_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[8]/label/input")
    COPY_FOLDERS_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[9]/label/input")
    COPY_SETTINGS_CHECKBOX = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/div[4]/div[10]/label/input")
    CREATE_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/form/button")
    CLOSE_MODAL_BUTTON = (By.CLASS_NAME, "close-modal")
    SELECT_FILES_UPLOAD_BUTTON = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/drag-drop-uploader/div/div["
                                            "1]/button")
    FILES_UPLOAD_DROPZONE = (By.XPATH, "//*[@id='project-wizard-drop-zone']/div/div[1]")
    FILESTACK_PICKER_ZONE = (By.XPATH, "//*[@id='fsp-fileUpload']")
    NO_PLANS_LINK = (By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/a")
    NEXT_BUTTON = (By.CLASS_NAME, "btn.next-btn.ng-binding.btn-default")
    COMPLETE_BUTTON = (By.CLASS_NAME, "btn.next-btn.ng-binding.btn-primary")

    def __init__(self, driver):
        super().__init__(driver)
        self.uri = "index/projects"
        self.driver = driver

    def click_new_project_button(self):
        self.wait_for_element(self.NEW_PROJECT_BUTTON).click()

    def click_new_project_box(self):
        self.wait_for_element(self.NEW_PROJECT_BOX).click()

    def enter_project_name(self, project_name):
        self.wait_for_element(self.PROJECT_NAME_FIELD).send_keys(project_name)

    def enter_project_code(self, project_code):
        self.wait_for_element(self.PROJECT_CODE_FIELD).send_keys(project_code)

    def create_new_project(self):
        self.wait_for_element(self.CREATE_BUTTON).click()

    def select_files_upload(self):
        self.wait_for_element(self.SELECT_FILES_UPLOAD_BUTTON).click()

    def drag_file_dropzone(self, filepath):
        self.wait_for_element(self.FILES_UPLOAD_DROPZONE).send_keys(filepath)

    def click_no_plans(self):
        self.wait_for_element(self.NO_PLANS_LINK).click()

    def close_modal(self):
        self.wait_for_element(self.CLOSE_MODAL_BUTTON).click()

    def click_next_button(self):
        self.wait_for_element(self.NEXT_BUTTON).click()

    def click_complete_button(self):
        self.wait_for_element(self.COMPLETE_BUTTON).click()

    def upload_file_filestack(self, file_path):
        self.wait_for_element(self.FILESTACK_PICKER_ZONE).send_keys(file_path)

