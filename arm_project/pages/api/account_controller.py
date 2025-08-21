import requests
import json
import allure
from jsonschema import validate
from schemas.schemas_authorization import *


class Authorization:

    @allure.step("Отправляем запрос на авторизацию")
    def authorization(self, base_url, login, password):
        payload = {
            "email": login,
            "password": password
        }

        response = requests.post(base_url + "/account/login", json=payload)

        token = response.json()["token"]
        return token, response

    @allure.step("Проверяем статус код ответа авторизации")
    def authorization_response_status_code_200(self, response):
        assert response.status_code == 200

    @allure.step("Проверяем схему ответа авторизации")
    def authorization_response_validate(self, response):
        validate(response.json(), authorization)

class AccountInfo:

    @allure.step("Запрашиваем информацию о пользователе")
    def get_account_info(self, base_url, account_id, token):
        headers = {'Authorization': f'Bearer_{token}'}
        response = requests.get(
            base_url + "/account/info",
            params={'accountId': account_id},
            headers=headers
        )
        return response

    @allure.step("Проверяем статус код ответа информации о пользователе")
    def get_account_info_status_code_200(self, response):
        assert response.status_code == 200

    @allure.step("Проверяем схему ответа информации о пользователе")
    def get_account_info_validate(self, response):
        validate(response.json(), account_info)

class AccountEdit:

    @allure.step('Отправляем запрос редактирования имени пользователя')
    def put_account_edit_name(self, value, token, base_url, account_id):
        headers = {'Authorization': f'Bearer_{token}'}
        payload = {
            "id": account_id,
            "name": value
        }
        response = requests.put(
            base_url + "/account",
            json=payload,
            headers=headers
        )
        return response

    @allure.step("Проверяем статус код ответа редактирования имени пользователя")
    def put_account_edit_status_code_200(self, response):
        assert response.status_code == 200

    @allure.step("Проверяем схему ответа редактирования имени пользователя")
    def put_account_edit_validate(self, response):
        validate(response.json(), account_edit)

    @allure.step("Проверяем, что ответ возвращает новое имя пользователя")
    def put_account_should_edit_name(self, response, value):
        assert response.json()["data"]["name"] == value

