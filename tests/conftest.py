import os
import allure
import pytest

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

from arm_project.pages.ui.authorization_page import AuthorizationPage
from arm_project.pages.api.authorization import Authorization
from arm_project.utils import attach

DEFAULT_BROWSER_VERSION = "128.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0'
    )
    parser.addoption(
        '--local',
        action='store_true',
        help='Run tests locally instead of Selenoid'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    is_local = request.config.getoption('--local')

    options = Options()

    if is_local:
        driver = webdriver.Chrome(options=options)
    else:
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)
        login = os.getenv('LOGIN_SELENOID')
        password = os.getenv('PASSWORD_SELENOID')
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)

    if not is_local:
        attach.add_video(browser)

    browser.quit()


@pytest.fixture
@allure.step("Авторизуемся перед тестом")
def authorization_ui(setup_browser, request):
    role = request.param
    password = os.getenv("PASSWORD_ADMIN")
    credentials = {
        "admin": (os.getenv("EMAIL_ADMIN"), password),
        "expert": (os.getenv("EMAIL_EXPERT"), password),
        "master": (os.getenv("EMAIL_MASTER"), password),
        "subcontractor": (os.getenv("EMAIL_SUBCONTRACTOR"), password),
        "observer": (os.getenv("EMAIL_OBSERVER"), password),
        "supervisor": (os.getenv("EMAIL_SUPERVISOR"), password)
    }

    email, password = credentials[role]
    authorization_page = AuthorizationPage(browser)

    authorization_page.open_authorization_form(os.getenv("BASE_URL_UI"))
    authorization_page.fill_login(email)
    authorization_page.fill_password(password)
    authorization_page.accept_user_agreement()
    authorization_page.submit_authorization()


@pytest.fixture
@allure.step("Авторизуемся через API перед тестом")
def authorization_api(request, setup_browser):
    role = request.param
    password = os.getenv("PASSWORD_ADMIN")
    credentials = {
        "admin": (os.getenv("EMAIL_ADMIN"), password),
        "expert": (os.getenv("EMAIL_EXPERT"), password),
        "master": (os.getenv("EMAIL_MASTER"), password),
        "subcontractor": (os.getenv("EMAIL_SUBCONTRACTOR"), password),
        "observer": (os.getenv("EMAIL_OBSERVER"), password),
        "supervisor": (os.getenv("EMAIL_SUPERVISOR"), password)
    }

    email, password = credentials[role]
    auth = Authorization()
    token = auth.authorization(os.getenv("BASE_URL_API"), email, password)

    browser.open(os.getenv("BASE_URL_UI"))
    browser.execute_script(f'localStorage.setItem("token", "{token}")')
    browser.driver.refresh()

    return token