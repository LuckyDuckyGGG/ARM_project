import os
import allure
import pytest

from selene import browser
from dotenv import load_dotenv
from arm_project.pages.ui.authorization_page import AuthorizationPage
from allure_commons.types import Severity

load_dotenv()

url = os.getenv("BASE_URL_UI")
password = os.getenv("PASSWORD_ADMIN")

@allure.parent_suite('UI')
@allure.suite('Авторизация')
@allure.sub_suite('Авторизация')
@allure.epic('Авторизация')
@allure.feature('Авторизация')
@allure.story('Пользователь должен иметь возможность авторизоваться на сайте')
@pytest.mark.ui
class TestAuthorization:

    @allure.title('Успешная авторизация пользователя под учетной записью владельца')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'rominikhom')
    def test_admin_authorization(self, setup_browser):
        authorization_page = AuthorizationPage(browser)
        email = os.getenv("EMAIL_ADMIN")

        authorization_page.open_authorization_form(url)
        authorization_page.fill_login(email)
        authorization_page.fill_password(password)
        authorization_page.accept_user_agreement()
        authorization_page.submit_authorization()
        authorization_page.should_user_success_authorization("Владелец")

    @allure.title('Успешная авторизация пользователя под учетной записью администратора')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'rominikhom')
    def test_expert_authorization(self, setup_browser):
        authorization_page = AuthorizationPage(browser)
        email = os.getenv("EMAIL_EXPERT")

        authorization_page.open_authorization_form(url)
        authorization_page.fill_login(email)
        authorization_page.fill_password(password)
        authorization_page.accept_user_agreement()
        authorization_page.submit_authorization()
        authorization_page.should_user_success_authorization("Администратор проекта")

    @allure.title('Успешная авторизация пользователя под учетной записью инспектора')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'rominikhom')
    def test_master_authorization(self, setup_browser):
        authorization_page = AuthorizationPage(browser)
        email = os.getenv("EMAIL_MASTER")

        authorization_page.open_authorization_form(url)
        authorization_page.fill_login(email)
        authorization_page.fill_password(password)
        authorization_page.accept_user_agreement()
        authorization_page.submit_authorization()
        authorization_page.should_user_success_authorization("Инспектор")

    @allure.title('Успешная авторизация пользователя под учетной записью подрядчика')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'rominikhom')
    def test_subcontractor_authorization(self, setup_browser):
        authorization_page = AuthorizationPage(browser)
        email = os.getenv("EMAIL_SUBCONTRACTOR")

        authorization_page.open_authorization_form(url)
        authorization_page.fill_login(email)
        authorization_page.fill_password(password)
        authorization_page.accept_user_agreement()
        authorization_page.submit_authorization()
        authorization_page.should_user_success_authorization("Подрядчик")

    @allure.title('Успешная авторизация пользователя под учетной записью наблюдателя')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'rominikhom')
    def test_observer_authorization(self, setup_browser):
        authorization_page = AuthorizationPage(browser)
        email = os.getenv("EMAIL_OBSERVER")

        authorization_page.open_authorization_form(url)
        authorization_page.fill_login(email)
        authorization_page.fill_password(password)
        authorization_page.accept_user_agreement()
        authorization_page.submit_authorization()
        authorization_page.should_user_success_authorization("Наблюдатель")

    @allure.title('Успешная авторизация пользователя под учетной записью супервизора')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('Авторизация')
    @allure.label('owner', 'rominikhom')
    def test_supervisor_authorization(self, setup_browser):
        authorization_page = AuthorizationPage(browser)
        email = os.getenv("EMAIL_SUPERVISOR")

        authorization_page.open_authorization_form(url)
        authorization_page.fill_login(email)
        authorization_page.fill_password(password)
        authorization_page.accept_user_agreement()
        authorization_page.submit_authorization()
        authorization_page.should_user_success_authorization("Супервизор")