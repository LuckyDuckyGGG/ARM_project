import os

from selene import browser
from dotenv import load_dotenv
from arm_project.pages.ui.authorization_page import AuthorizationPage

load_dotenv()

url = os.getenv("BASE_URL_UI")
password = os.getenv("PASSWORD_ADMIN")