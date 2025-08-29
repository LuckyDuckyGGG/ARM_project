import os
from time import sleep

import pytest
import allure

from faker import Faker
from selene.support.shared import browser

from arm_project.utils.factories import ProjectFactory
from tests.conftest import setup_browser
from dotenv import load_dotenv
from arm_project.pages.ui.admin_panel_project_page import AdminPanelProjectPage
from allure_commons.types import Severity

load_dotenv()

url = os.getenv("BASE_URL_UI")
fake = Faker('ru_RU')

@allure.parent_suite('UI')
@allure.suite('Админ-панель')
@allure.sub_suite('Проект')
@allure.epic('Проект')
@allure.feature('Проект')
@allure.story('Пользователь должен иметь возможность работать с проектом')
@pytest.mark.ui
class TestProject:


    @allure.title('Создание проекта с заполнением обязательных полей')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Создание проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api_ui", ["admin"], indirect=True)
    def test_create_project_admin_fill_required_fields(self, authorization_api_ui, setup_browser):
        create_project = AdminPanelProjectPage(browser)
        project_data = ProjectFactory().create_project()

        create_project.click_project_create()
        create_project.fill_project_name(project_data.name)
        create_project.fill_project_city(fake.city_name())
        create_project.submit_create_project()
        create_project.should_table_have_project_name(project_data.name)


    @allure.title('Создание проекта с заполнением всех полей')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Создание проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api_ui", ["admin"], indirect=True)
    def test_create_project_admin_fill_all_fields(self, authorization_api_ui, setup_browser):
        create_project = AdminPanelProjectPage(browser)
        project_data = ProjectFactory().create_project()

        create_project.click_project_create()
        create_project.fill_all_project_fields(project_data)
        create_project.submit_create_project()
        create_project.should_table_have_project_name(project_data.short_name)


    @allure.title('Недоступно создание проекта ролям: администратор, инспектор, подрядчик, наблюдатель')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Создание проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api_ui", ["expert", "master", "subcontractor", "observer", "supervisor"], indirect=True)
    def test_create_project_except_admin_and_supervisor(self, authorization_api_ui, setup_browser):
        create_project = AdminPanelProjectPage(browser)

        if authorization_api_ui["role"] == "supervisor":
            create_project.open_project_tab(url)

        create_project.should_button_create_disabled()


    @allure.title('Поиск по полному наименованию проекта')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Поиск активного проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api_ui", ["admin", "expert", "master", "subcontractor", "observer", "supervisor"],
                             indirect=True)
    def test_search_active_project_by_name(self, authorization_api_ui, setup_browser):
        search_project = AdminPanelProjectPage(browser)

        if authorization_api_ui["role"] == "supervisor":
            search_project.open_project_tab(url)

        search_project.search_project_name("Search")
        search_project.should_table_have_project_name("Search")


    @allure.title('Поиск по короткому наименованию проекта')
    @allure.severity(Severity.MINOR)
    @allure.tag('Поиск активного проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.skip("Ожидает доработки https://tracker.yandex.ru/ARMS-749")
    @pytest.mark.parametrize("authorization_api_ui", ["admin", "expert", "master", "subcontractor", "observer", "supervisor"],
                             indirect=True)
    def test_search_active_project_by_short_name(self, authorization_api_ui, setup_browser):
        search_project = AdminPanelProjectPage(browser)

        if authorization_api_ui["role"] == "supervisor":
            search_project.open_project_tab(url)

        search_project.search_project_name("Srch")
        search_project.should_table_have_project_name("Srch")


    @allure.title('Завершение активного проекта под ролью владельца')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Завершение проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api_ui", ["admin"], indirect=True)
    def test_complete_project(self, authorization_api_ui, setup_browser):
        complete_project = AdminPanelProjectPage(browser)
        project_data = ProjectFactory().create_project()

        complete_project.click_project_create()
        complete_project.fill_all_project_fields(project_data)
        complete_project.submit_create_project()
        complete_project.complete_project(project_data.short_name)
        complete_project.fill_complete_project_password(os.getenv("PASSWORD_ADMIN"))
        complete_project.open_complete_project_tab()
        complete_project.should_table_have_project_name(project_data.short_name)


    @allure.title('Недоступно завершение проекта, всем ролям, кроме владельца')
    @allure.severity(Severity.NORMAL)
    @allure.tag('Завершение проекта')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api_ui", ["expert", "master", "subcontractor", "observer", "supervisor"], indirect=True)
    def test_should_not_complete_project(self, authorization_api_ui, setup_browser):
        complete_project = AdminPanelProjectPage(browser)
        project_data = ProjectFactory().create_project()

        if authorization_api_ui["role"] == "supervisor":
            complete_project.open_project_tab(url)

        sleep(1.5)
        complete_project.should_not_complete_project(project_data.name)


