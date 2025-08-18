import allure
from selene import have, be


class AdminPanelProjectPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Кликаем на кнопку создать проект")
    def click_project_create(self):
        self.browser.element('[class="ant-btn ant-btn-default primaryButton big colorPrimary "]').click()

    @allure.step("Заполняем поля название проекта")
    def fill_project_name(self, value):
        self.browser.element('#CreateProjectForm_name').type(f"{value}")

    @allure.step("Заполняем поле город проекта")
    def fill_project_city(self, value):
        self.browser.element('#CreateProjectForm_city').type(f"{value}")

    @allure.step("Кликаем на кнопку создать")
    def submit_create_project(self):
        self.browser.element('[type="submit"]').click()

    @allure.step("Проверяем что проект есть в таблице")
    def should_table_have_project_name(self, value):
        self.browser.all(".ant-table-row").element_by(
            have.text(value)
        ).should(be.visible)

    @allure.step("Проверяем, что кнопка создать проект отсутствует")
    def should_button_create_disabled(self):
        self.browser.element('[class="ant-btn ant-btn-default primaryButton big colorPrimary "]').should(have.attribute("disabled"))

    @allure.step("Открываем раздел проекты")
    def open_project_tab(self, value):
        self.browser.open(value + "/projects")