import os
import pytest
from allure import step


from dotenv import load_dotenv
from arm_project.pages.api.account_controller import *
from arm_project.utils.factories import UserFactory
from allure_commons.types import Severity

from tests.conftest import base_url_api

load_dotenv()

url = base_url_api

@allure.parent_suite('API')
@allure.suite('Контроллер account')
@allure.sub_suite('Контроллер account')
@allure.epic('Контроллер account')
@allure.feature('Авторизация и работа с учеткой пользователя')
@allure.story('Контроллер account')
@pytest.mark.api
class TestAccountController:

    @allure.title('POST /account/login успешная авторизация')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Account')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api", ["admin", "expert", "master", "subcontractor", "observer", "supervisor"],
                             indirect=True)
    def test_post_account_login(self, api_logger, authorization_api):
        authorization = Authorization()

        response = authorization_api["response"]

        authorization.authorization_response_status_code_200(response)
        authorization.authorization_response_validate(response)

    @allure.title('GET /account/info запрос данных об аккаунте')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Account')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api", ["admin", "expert", "master", "subcontractor", "observer", "supervisor"],
                             indirect=True)
    def test_get_account_info(self, api_logger, authorization_api):
        info = AccountInfo()

        token = authorization_api["token"]
        account_id = authorization_api["account_id"]

        response = info.get_account_info(
            base_url=url,
            account_id=account_id,
            token=token
        )

        info.get_account_info_status_code_200(response)
        info.get_account_info_validate(response)

    @allure.title('PUT /account/edit редактирование имени другого пользователя')
    @allure.severity(Severity.NORMAL)
    @allure.tag('API', 'Account')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api", ["admin", "expert"], indirect=True)
    def test_edit_user_name(self, api_logger, authorization_api):
        edit_name = AccountEdit()
        user = UserFactory().create_user()

        auth = Authorization()
        observer_email = os.getenv("EMAIL_OBSERVER")
        password = os.getenv("PASSWORD_ADMIN")
        observer_token, observer_response = auth.authorization(url, observer_email, password)
        observer_data = observer_response.json()
        observer_id = observer_data["data"]["id"]

        token = authorization_api["token"]
        response = edit_name.put_account_edit_name(
            base_url=url,
            token=token,
            value=user.name,
            account_id=observer_id
        )

        edit_name.put_account_edit_status_code_200(response)
        edit_name.put_account_edit_validate(response)
        edit_name.put_account_should_edit_name(response, user.name)

        with step("Возвращаем предыдущее имя пользователя"):
            edit_name.put_account_edit_name(
                base_url=url,
                token=token,
                value="Наблюдатель",
                account_id=observer_id
            )



