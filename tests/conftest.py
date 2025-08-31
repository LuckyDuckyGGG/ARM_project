import json
import logging
import os
import allure
import pytest
import requests
import config
import re

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from allure_commons.types import AttachmentType
from allure import attach as allure_attach

from arm_project.pages.api.project_controller import CreateProject
from arm_project.pages.ui.authorization_page import AuthorizationPage
from arm_project.pages.api.account_controller import Authorization
from arm_project.utils import attach
from arm_project.utils.factories import ProjectFactory

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
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function')
def mobile_management(context):
    options = config.driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    if context == 'bstack':
        session_id = browser.driver.session_id
        attach.add_video_bstack(session_id)


    browser.driver.quit()
    browser.config.driver = None


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


def sanitize_data(data):
    sensitive_keys = ['password', 'token', 'auth', 'authorization',
                      'access_token', 'refresh_token', 'secret',
                      'api_key', 'key', 'credentials', 'login']

    if isinstance(data, dict):
        sanitized = {}
        for key, value in data.items():
            if any(sensitive in key.lower() for sensitive in sensitive_keys):
                sanitized[key] = '***REDACTED***'
            elif isinstance(value, (dict, list)):
                sanitized[key] = sanitize_data(value)
            else:
                sanitized[key] = value
        return sanitized

    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]

    return data


def sanitize_headers(headers):
    sensitive_headers = ['authorization', 'token', 'auth', 'cookie', 'set-cookie']
    sanitized = {}

    for key, value in headers.items():
        if any(sensitive in key.lower() for sensitive in sensitive_headers):
            sanitized[key] = '***REDACTED***'
        else:
            sanitized[key] = value

    return sanitized


@pytest.fixture
def api_logger():
    original_request = requests.Session.request

    def logged_request(self, method, url, **kwargs):

        logging.info(f"🚀 API Request: {method.upper()} {url}")


        headers = kwargs.get('headers', {})
        sanitized_headers = sanitize_headers(headers)
        if sanitized_headers:
            logging.info(f"📋 Request Headers: {sanitized_headers}")


        if kwargs.get('json'):
            sanitized_json = sanitize_data(kwargs['json'])
            pretty_json = json.dumps(sanitized_json, indent=2, ensure_ascii=False)
            logging.info(f"📦 Request Body:\n{pretty_json}")

        response = original_request(self, method, url, **kwargs)


        logging.info(f"✅ API Response: {response.status_code} {response.url}")
        logging.info(f"⏱️  Response time: {response.elapsed.total_seconds() * 1000:.2f}ms")


        response_headers = dict(response.headers)
        sanitized_response_headers = sanitize_headers(response_headers)
        logging.info(f"📋 Response Headers: {sanitized_response_headers}")

        try:
            response_data = response.json()
            sanitized_response = sanitize_data(response_data)
            pretty_response = json.dumps(sanitized_response, indent=2, ensure_ascii=False)
            logging.info(f"📦 Response Body:\n{pretty_response}")
        except:
            response_text = response.text
            response_text = re.sub(r'(?i)(token|auth|password)[=:]\s*[\w\-\.]+', r'\1=***REDACTED***', response_text)
            logging.info(f"📄 Response Text: {response_text[:500]}")

        # Для Allure также используем очищенные данные
        allure_attach(f"API: {method.upper()} {url}", name="API Request", attachment_type=AttachmentType.TEXT)
        allure_attach(f"Status: {response.status_code}", name="API Response", attachment_type=AttachmentType.TEXT)

        return response

    requests.Session.request = logged_request
    yield
    requests.Session.request = original_request


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
def authorization_api_ui(request, setup_browser):
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
    token, response = auth.authorization(os.getenv("BASE_URL_API"), email, password)

    browser.open(os.getenv("BASE_URL_UI"))
    browser.execute_script(f'localStorage.setItem("token", "{token}")')
    browser.driver.refresh()

    return {"token": token, "role": role}

@pytest.fixture
@allure.step("Авторизуемся через API для API тестов")
def authorization_api(request):
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
    token, response = auth.authorization(os.getenv("BASE_URL_API"), email, password)

    response_data = response.json()
    account_id = response_data["data"]["id"]

    return {
        "response": response,
        "token": token,
        "account_id": account_id,
        "role": role,
        "email": email
    }


@pytest.fixture
def admin_authorization():
    email = os.getenv("EMAIL_ADMIN")
    password = os.getenv("PASSWORD_ADMIN")

    auth = Authorization()
    token, response = auth.authorization(os.getenv("BASE_URL_API"), email, password)
    response_data = response.json()

    return {
        "token": token,
        "organization_id": response_data["data"]["organizationId"]
    }

@pytest.fixture()
def create_project_with_required_fields(admin_authorization):

    create_project = CreateProject()
    token = admin_authorization["token"]
    organization_id = admin_authorization["organization_id"]
    url = os.getenv("BASE_URL_API")
    project = ProjectFactory().create_project()

    response = create_project.create_project_with_required_field(
        url=url,
        token=token,
        organization_id=organization_id,
        project_name=project.name,
        project_city=project.city
    )

    return response.json()

def pytest_allure_attach_parametrize(params):
    safe_params = {}
    for key, value in params.items():
        if any(sensitive in key.lower() for sensitive in ['password', 'token', 'secret', 'key', 'auth']):
            safe_params[key] = '***REDACTED***'
        else:
            safe_params[key] = value
    return safe_params