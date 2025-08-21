import os
import pytest

from dotenv import load_dotenv
from arm_project.pages.api.project_controller import CreateProject

load_dotenv()

url = os.getenv("BASE_URL_API")

@pytest.mark.parametrize("authorization_api", ["admin"], indirect=True)
def test_delete_project(api_logger, authorization_api, create_project_with_required_fields):
    delete_project = CreateProject()
    token = authorization_api["token"]
    project_id = create_project_with_required_fields


    response = delete_project.delete_project(url=url, token=token, project_id=project_id)
    delete_project.delete_project_status_code_200(response)