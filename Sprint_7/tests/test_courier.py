import pytest
import requests
from Sprint_7.utils.generate_user import generate_random_string, delete_courier
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

BASE_URL = "https://qa-scooter.praktikum-services.ru/api/v1/courier"

class TestCourierCreation:
    def test_successful_creation(self):
        login = generate_random_string()
        password = generate_random_string()
        first_name = generate_random_string()
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(BASE_URL, json=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        # Удаляем курьера после теста
        delete_courier(login, password)

    def test_cannot_create_duplicate_courier(self, new_courier):
        login, password, first_name = new_courier
        payload = {"login": login, "password": password, "firstName": first_name}
        response = requests.post(BASE_URL, json=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"

    @pytest.mark.parametrize("missing_field", ["login", "password", "firstName"])
    def test_missing_required_fields(self, missing_field):
        data = {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }
        data.pop(missing_field)
        response = requests.post(BASE_URL, json=data)
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"

    def test_cannot_create_courier_with_existing_login(self, new_courier):
        login, _, _ = new_courier
        payload = {
            "login": login,
            "password": generate_random_string(),
            "firstName": generate_random_string()
        }
        response = requests.post(BASE_URL, json=payload)
        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется"
