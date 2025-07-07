import requests
import pytest
from Sprint7.utils.urls import COURIER_LOGIN_URL

class TestCourierLogin:
    def test_successful_login(self, new_courier):
        login, password, _ = new_courier
        response = requests.post(COURIER_LOGIN_URL, json={
            "login": login,
            "password": password
        })
        assert response.status_code == 200
        assert "id" in response.json()

    @pytest.mark.parametrize("field", ["login"])
    def test_missing_field(self, field):
        payload = {
            "login": "test_login",
            "password": "test_password"
        }
        payload.pop(field)
        response = requests.post(COURIER_LOGIN_URL, json=payload)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    def test_invalid_credentials(self):
        response = requests.post(COURIER_LOGIN_URL, json={
            "login": "non_existent_user",
            "password": "wrong_password"
        })
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    def test_login_non_existent_user(self):
        response = requests.post(COURIER_LOGIN_URL, json={
            "login": "doesnotexist",
            "password": "doesnotexist"
        })
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"
