import pytest
import requests
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
print(sys.path)
from Sprint7.utils.urls import ORDER_URL



class TestOrderCreation:
    @pytest.mark.parametrize("colors", [
        (["BLACK"]),
        (["GREY"]),
        (["BLACK", "GREY"]),
        ([])
    ])
    def test_order_creation_with_colors(self, colors):
        payload = {
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79999999999",
            "rentTime": 3,
            "deliveryDate": "2025-07-01",
            "comment": "Комментарий",
            "color": colors
        }
        response = requests.post(ORDER_URL, json=payload)
        assert response.status_code == 201
        assert "track" in response.json()

    def test_get_orders_list(self):
        response = requests.get(ORDER_URL)
        assert response.status_code == 200
        assert isinstance(response.json()["orders"], list)
