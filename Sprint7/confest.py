import pytest
from utils.courier import register_new_courier, delete_courier

@pytest.fixture
def new_courier():
    data = register_new_courier()
    yield data
    if data:
        delete_courier(data[0], data[1])