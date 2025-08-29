import os
import pytest
import allure

from dotenv import load_dotenv
from arm_project.pages.api.project_controller import CreateProject
from allure_commons.types import Severity

load_dotenv()

url = os.getenv("BASE_URL_API")

@allure.parent_suite('API')
@allure.suite('Контроллер project')
@allure.sub_suite('Контроллер project')
@allure.epic('Контроллер project')
@allure.feature('Работа с проектами')
@allure.story('Контроллер project')
@pytest.mark.api
class TestProjectController:

    @allure.title('DELETE /project/delete удаление проекта')
    @allure.severity(Severity.CRITICAL)
    @allure.tag('API', 'Project')
    @allure.label('owner', 'rominikhom')
    @pytest.mark.parametrize("authorization_api", ["admin"], indirect=True)
    def test_delete_project(api_logger, authorization_api, create_project_with_required_fields):
        delete_project = CreateProject()
        token = authorization_api["token"]
        project_id = create_project_with_required_fields


        response = delete_project.delete_project(url=url, token=token, project_id=project_id)
        delete_project.delete_project_status_code_200(response)