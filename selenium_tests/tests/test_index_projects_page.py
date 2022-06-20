import random
import string

import pytest
from selenium_tests.pages.index_projects_page import IndexProjectsPage
from selenium_tests.pages.projects_page import ProjectsPage


@pytest.mark.usefixtures("setup")
class TestIndexProjectsPage:

    @pytest.mark.usefixtures("signup")
    def test_new_user_create_new_project(self):
        index_projects_page = IndexProjectsPage(self.driver)
        index_projects_page.click_new_project_box()
        index_projects_page.enter_project_name("project_test_new_user")
        index_projects_page.create_new_project()
        index_projects_page.reload()
        projects_page = ProjectsPage(self.driver)
        projects_page.does_element_exist()

    @pytest.mark.usefixtures("login")
    def test_existing_user_create_new_project(self):
        index_projects_page = IndexProjectsPage(self.driver)
        index_projects_page.click_new_project_box()
        index_projects_page.enter_project_name("project_test_existing_user".join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        index_projects_page.create_new_project()
        index_projects_page.reload()
