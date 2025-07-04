import requests
import random
import string
from Sprint7.utils.urls import COURIER_URL, COURIER_LOGIN_URL

def generate_random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def register_new_courier():
    login = generate_random_string()
    password = generate_random_string()
    first_name = generate_random_string()
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    response = requests.post(COURIER_URL, json=payload)
    if response.status_code == 201:
        return [login, password, first_name]
    return []

def delete_courier(login, password):
    response = requests.post(COURIER_LOGIN_URL, json={"login": login, "password": password})
    if response.status_code == 200 and "id" in response.json():
        courier_id = response.json()["id"]
        requests.delete(f"{COURIER_URL}/{courier_id}")
