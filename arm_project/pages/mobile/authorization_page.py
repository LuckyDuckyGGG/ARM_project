import allure
from selene import have, by
from appium.webdriver.common.appiumby import AppiumBy

class AuthorizationPageMobile:

    def __init__(self, browser):
        self.browser = browser

    def fill_email(self, value):
        self.browser.element((AppiumBy.ID, ''))