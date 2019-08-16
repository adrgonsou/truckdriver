import os
import tempfile
import pytest
import status

from app import app

@pytest.fixture
def trucker():
    app.config['TESTING'] = True
    trucker = app.test_trucker()

    yield trucker

def test_valid_truck_driver(trucker):
    driver = {
        "name": "Adriano Souza",
        "age": 31,
        "gender": "masculino",
        "cnh": "D",
        "truck" : {
            "owner" : True,
            "with_charge": False,
            "type": 1
        } 
    }
    
    response = trucker.post("truck_driver",json=driver)   

    assert response.status_code == status.HTTP_201_CREATED
