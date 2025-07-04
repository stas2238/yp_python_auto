import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
print(sys.path)
from Sprint7.utils.courier import register_new_courier, delete_courier

@pytest.fixture
def new_courier():
    data = register_new_courier()
    yield data
    if data:
        delete_courier(data[0], data[1])
