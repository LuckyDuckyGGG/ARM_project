import os

from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv

from arm_project import utils

def driver_options(context):
    options = UiAutomator2Options()

    if context == 'local':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv(
            'APP_WAIT_ACTIVITY'))
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))

    if context == 'real':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        options.set_capability('language', 'ru')
        options.set_capability('locale', 'RU')
        load_dotenv(dotenv_path=utils.file.abs_path_from_project(
            '.env.credentials'))
        options.set_capability(
            'bstack:options', {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build',
                'sessionName': 'Wikipedia Test',
                'userName': os.getenv('USER_NAME'),
                'accessKey': os.getenv('ACCESS_KEY')
            },
        )

    return options