import os

from selene import browser
from dotenv import load_dotenv
from arm_project.pages.ui.authorization_page import AuthorizationPage

load_dotenv()

url = os.getenv("BASE_URL_UI")
password = os.getenv("PASSWORD_ADMIN")



def test_admin_authorization(setup_browser):
    authorization_page = AuthorizationPage(browser)
    email = os.getenv("EMAIL_ADMIN")

    authorization_page.open_authorization_form(url)
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()
    authorization_page.should_user_success_authorization("Владелец")

def test_expert_authorization(setup_browser):
    authorization_page = AuthorizationPage(browser)
    email = os.getenv("EMAIL_EXPERT")

    authorization_page.open_authorization_form(url)
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()
    authorization_page.should_user_success_authorization("Администратор проекта")

def test_master_authorization(setup_browser):
    authorization_page = AuthorizationPage(browser)
    email = os.getenv("EMAIL_MASTER")

    authorization_page.open_authorization_form(url)
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()
    authorization_page.should_user_success_authorization("Инспектор")

def test_subcontractor_authorization(setup_browser):
    authorization_page = AuthorizationPage(browser)
    email = os.getenv("EMAIL_SUBCONTRACTOR")

    authorization_page.open_authorization_form(url)
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()
    authorization_page.should_user_success_authorization("Подрядчик")

def test_observer_authorization(setup_browser):
    authorization_page = AuthorizationPage(browser)
    email = os.getenv("EMAIL_OBSERVER")

    authorization_page.open_authorization_form(url)
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()
    authorization_page.should_user_success_authorization("Наблюдатель")

def test_supervisor_authorization(setup_browser):
    authorization_page = AuthorizationPage(browser)
    email = os.getenv("EMAIL_SUPERVISOR")

    authorization_page.open_authorization_form(url)
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()
    authorization_page.should_user_success_authorization("Супервизор")