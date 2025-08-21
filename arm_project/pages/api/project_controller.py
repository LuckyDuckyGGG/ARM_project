import requests
import json
import allure
from jsonschema import validate
from schemas.schemas_authorization import *

class CreateProject:

    @allure.step('Создаем проект с заполнением только обязательных полей')
    def create_project_with_required_field(self, url, project_name, project_city, organization_id, token):
        payload = {
            "name": project_name,
            "city": project_city
        }
        params = {"contextOrganizationId": organization_id}
        headers = {'Authorization': f'Bearer_{token}'}

        response = requests.post(url=url + '/project/create', params=params, headers=headers, json=payload)

        return response

    @allure.step('Удаляем проект')
    def delete_project(self, url, project_id, token):
        params = {
            "projectId": project_id,
            "contextProjectId": project_id
        }
        headers = {'Authorization': f'Bearer_{token}'}

        delete_project_response = requests.delete(url=url + '/project/delete_by_id', params=params, headers=headers)

        return delete_project_response

    @allure.step('Проверяем код ответа об удалении проекта')
    def delete_project_status_code_200(self, delete_project_response):
        assert delete_project_response.status_code == 200
