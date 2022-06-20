import random
import string
import time

import pytest

from selenium_tests.pages.index_projects_page import IndexProjectsPage
from selenium_tests.pages.projects_page import ProjectsPage


@pytest.mark.usefixtures("setup")
@pytest.mark.usefixtures("signup")
class TestProjectsPage:

    def test_create_new_task(self):
        index_projects_page = IndexProjectsPage(self.driver)
        index_projects_page.click_new_project_box()
        index_projects_page.enter_project_name("project_".join(random.choices(string.ascii_uppercase + string.digits, k=5)))
        index_projects_page.create_new_project()
        time.sleep(3)
        index_projects_page.reload()
        projects_page = ProjectsPage(self.driver)
        projects_page.click_sidebar_tasks()
        projects_page.click_new_task()
        projects_page.reload()
        projects_page.open()


