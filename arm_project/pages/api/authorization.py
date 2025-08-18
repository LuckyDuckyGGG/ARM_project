import requests
import json
import allure

class Authorization:

    @allure.step("Авторизуемся для получения токена")
    def authorization(self, base_url, login, password):
        payload = {
            "email": login,
            "password": password
        }

        response = requests.post(base_url + "/account/login", json=payload)

        cookie = response.json()["token"]
        return cookie