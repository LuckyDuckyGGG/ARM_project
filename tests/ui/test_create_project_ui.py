import os
import random
import time
import pytest

from faker import Faker
from selene.support.shared import browser
from tests.conftest import setup_browser
from dotenv import load_dotenv
from arm_project.pages.ui.admin_panel_page import AdminPanelProjectPage

load_dotenv()

url = os.getenv("BASE_URL_UI")
fake = Faker('ru_RU')

@pytest.mark.parametrize("authorization_api", ["admin"], indirect=True)
def test_create_project_admin(authorization_api, setup_browser):
    create_project = AdminPanelProjectPage(browser)
    project_name = f"Проект{random.randint(1, 9999)}"

    create_project.click_project_create()
    create_project.fill_project_name(project_name)
    create_project.fill_project_city(fake.city_name())
    create_project.submit_create_project()
    create_project.should_table_have_project_name(project_name)

@pytest.mark.parametrize("authorization_ui", ["expert", "master", "subcontractor", "observer"], indirect=True)
def test_create_project_except_admin_and_supervisor(authorization_ui, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    create_project.should_button_create_disabled()


@pytest.mark.parametrize("authorization_ui", ["supervisor"], indirect=True)
def test_create_project_supervisor(authorization_ui, setup_browser):
    create_project = AdminPanelProjectPage(browser)

    time.sleep(2)
    create_project.open_project_tab(url)
    create_project.should_button_create_disabled()