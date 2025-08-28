import allure
import requests
import os
from allure_commons.types import AttachmentType

# Скриншоты
def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=AttachmentType.PNG, extension='.png')

# Логи
def add_logs(browser):
    try:
        devtools = browser.driver.get_devtools()
        logs = devtools.get_logs()
        if logs:
            log_text = "\n".join(str(log) for log in logs)
            allure.attach(log_text, name="devtools_logs", attachment_type=allure.attachment_type.TEXT)
    except Exception as e:
        allure.attach(f"DevTools error: {str(e)}", name="devtools_error", attachment_type=allure.attachment_type.TEXT)

# HTML-код страницы
def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')

# Скринкаст
def add_video(browser):
    video_url = f"https://user1:1234@selenoid.autotests.cloud/video/" + browser.driver.session_id + ".mp4"
    html = "<html><body><video width='100%' height='100%' controls autoplay><source src='" \
           + video_url \
           + "' type='video/mp4'></video></body></html>"
    allure.attach(html, 'video_' + browser.driver.session_id, AttachmentType.HTML, '.html')

def add_xml(browser):
    xml = browser.driver.page_source
    allure.attach(xml, 'page_source', AttachmentType.XML, '.xml')

def add_video_bstack(session_id):
        bstack_session = requests.get(
            f'https://api.browserstack.com/app-automate/sessions/{session_id}.json',
            auth=(os.getenv('USER_NAME'), os.getenv('ACCESS_KEY')),
        ).json()
        print(bstack_session)
        video_url = bstack_session['automation_session']['video_url']

        allure.attach(
            '<html><body>'
            '<video width="100%" height="100%" controls autoplay>'
            f'<source src="{video_url}" type="video/mp4">'
            '</video>'
            '</body></html>',
            name='video recording',
            attachment_type=allure.attachment_type.HTML,
        )