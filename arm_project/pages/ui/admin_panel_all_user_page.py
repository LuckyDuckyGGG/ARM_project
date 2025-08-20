from time import sleep

import allure
from selene import have, be


class AdminPanelAllUserPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открываем страницу пользователей в админ панели")
    def open_all_user_page(self, value):
        self.browser.open(value + "/users")

    @allure.step("Открываем модалку редактирования пользователя")
    def open_modal_edit_user(self, role):
        self.browser.all(".ant-table-row").element_by(
            have.text(role)
        ).element('[alt="Edit"]').click()
        self.browser.element('//div[@data-testid="Text" and text()="Редактировать"]').click()

    @allure.step("Изменяем имя пользователя")
    def edit_user_name(self, value):
        self.browser.element('#user_name').type(value)

    @allure.step("Изменяем фамилию пользователя")
    def edit_user_last_name(self, value):
        self.browser.element('#user_last_name').type(value)

    @allure.step("Изменяем фамилию пользователя")
    def edit_user_last_name(self, value):
        self.browser.element('#user_last_name').type(value)

    @allure.step("Изменяем отчество пользователя")
    def edit_user_middle_name(self, value):
        self.browser.element('#user_middleName').type(value)