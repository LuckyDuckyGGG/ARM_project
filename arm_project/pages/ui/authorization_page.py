import allure
from selene import have, by

class AuthorizationPage:

    def __init__(self, browser):
        self.browser = browser

    @allure.step("Открываем окно авторизации")
    def open_authorization_form(self, value):
        self.browser.open(value + "/login")

    @allure.step("Заполняем поле электронная почта")
    def fill_login(self, email):
        self.browser.element('[type="text"]').type(f"{email}")

    @allure.step("Заполняем поле пароль")
    def fill_password(self, password):
        self.browser.element('[type="password"]').type(f"{password}")

    @allure.step("Принимаем условия использования и политику конфиденциальности")
    def accept_user_agreement(self):
        self.browser.element('#CheckboxComponent').click()

    @allure.step("Кликаем на кнопку войти")
    def submit_authorization(self):
        self.browser.element('[type="submit"]').click()

    @allure.step("Проверяем что пользователь авторизован")
    def should_user_success_authorization(self, value):
        self.browser.element('[class="ant-dropdown-trigger Profile__initials"]').click()
        self.browser.element(by.text("Профиль")).click()
        self.browser.element('[class="InformationProfile__info-role"]').should(
            have.text(f"{value}")
        )