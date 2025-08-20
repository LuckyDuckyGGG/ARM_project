from time import sleep

import allure
from selene import have, be


class AdminPanelProjectPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Кликаем на кнопку создать проект")
    def click_project_create(self):
        self.browser.element('[class="ant-btn ant-btn-default primaryButton big colorPrimary "]').click()

    @allure.step("Заполняем поле название проекта")
    def fill_project_name(self, value):
        self.browser.element('#CreateProjectForm_name').type(f"{value}")

    @allure.step("Заполняем поле короткое название проекта")
    def fill_project_short_name(self, value):
        self.browser.element('#CreateProjectForm_shortName').type(f"{value}")

    @allure.step("Заполняем поле код проекта")
    def fill_project_code(self, value):
        self.browser.element('#CreateProjectForm_code').type(f"{value}")

    @allure.step("Заполняем период проекта")
    def fill_project_date(self, start_date, end_date):
        self.browser.element('#CreateProjectForm_startDate').type(f"{start_date}").press_enter()()
        self.browser.element('#CreateProjectForm_endDate').type(f"{end_date}").press_enter()()

    @allure.step("Указываем срок исполнения замечаний по умолчанию, дней")
    def fill_project_deadline_remark(self, value):
        self.browser.element('#CreateProjectForm_defaultDeadlineForRemark').type(f"{value}")

    @allure.step("Заполняем поле страна проекта")
    def fill_project_country(self, value):
        self.browser.element('#CreateProjectForm_country').type(f"{value}")

    @allure.step("Заполняем поле город проекта")
    def fill_project_city(self, value):
        self.browser.element('#CreateProjectForm_city').type(f"{value}")

    @allure.step("Заполняем поле улица проекта")
    def fill_project_street(self, value):
        self.browser.element('#CreateProjectForm_street').type(f"{value}")

    @allure.step("Заполняем поле дом проекта")
    def fill_project_building(self, value):
        self.browser.element('#CreateProjectForm_building').type(f"{value}")

    @allure.step("Заполняем поле офис проекта")
    def fill_project_office(self, value):
        self.browser.element('#CreateProjectForm_office').type(f"{value}")

    @allure.step("Заполняем поле почтовый индекс проекта")
    def fill_project_postal_code(self, value):
        self.browser.element('#CreateProjectForm_postalCode').type(f"{value}")

    @allure.step("Выбираем ответственного по проекту")
    def fill_project_responsible(self):
        self.browser.element('[class="buttonSimple buttonSimple_bordered CreateProjectForm__button"]').click()
        sleep(1)
        self.browser.element('.ant-table-tbody tr:first-child').click()
        self.browser.element('button.primaryButton[type="button"]').click()

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

    @allure.step("Поиск проекта по названию")
    def search_project_name(self, value):
        self.browser.element('[class="Checklists__extraButtonChecklict-search"]').click()
        self.browser.element('[class="ant-input"]').type(value).press_enter()

    @allure.step("Заполняем все поля проекта")
    def fill_all_project_fields(self, project_data):
        self.fill_project_name(project_data.name)
        self.fill_project_short_name(project_data.short_name)
        self.fill_project_code(project_data.code)
        self.fill_project_date(project_data.start_date, project_data.end_date)
        self.fill_project_deadline_remark(project_data.deadline_remark)
        self.fill_project_country(project_data.country)
        self.fill_project_city(project_data.city)
        self.fill_project_street(project_data.street)
        self.fill_project_building(project_data.building)
        self.fill_project_office(project_data.office)
        self.fill_project_postal_code(project_data.postal_code)
        self.fill_project_responsible()

    @allure.step("Завершаем проект")
    def complete_project(self, value):
        self.browser.all(".ant-table-row").element_by(
            have.text(f"{value}")
        ).element('[alt="Edit"]').click()
        self.browser.element('//div[@data-testid="Text" and text()="Завершить"]').click()

    @allure.step("Подтверждаем завершение проекта")
    def fill_complete_project_password(self, value):
        self.browser.element('#EditedPasswordUser_password').type(f"{value}")
        self.browser.element('//button[.//span[text()="Подтвердить"]]').click()


    @allure.step("Открываем таб завершенные проекты")
    def open_complete_project_tab(self):
        self.browser.element('[data-node-key="2"]').click()

    @allure.step("Проверяем, что пользователь не может завершить проект")
    def should_not_complete_project(self, value):
        self.browser.all(".ant-table-row").element_by(
            have.text(f"{value}")
        ).element('[alt="Edit"]').should(be.not_.visible)