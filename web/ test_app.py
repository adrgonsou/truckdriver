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
        {
            "name": "Fernando Souza",
            "age": 31,
            "gender": "masculino",
            "cnh": "D",
            "truck" : {
                "owner" : True,
                "with_charge": False,
                "type": 1
            },
            "road_trip": {
                "origin": {
                    "state": "SP",
                    "city": "São Paulo",
                    "stret": "Rua Amaral Silva",
                    "number": "598 B",
                    "geometry" : {
                        "lat" : -26.1965843,
                        "lng" : -52.6890572
                    }
                },
                "destiny": {
                    "state": "RJ",
                    "city": "Rio de Janeiro",
                    "stret": "Morro do Alemão",
                    "number": "2",
                    "geometry" : {
                        "lat" : -89.1965844,
                        "lng" : -3.6890573
                    }
                }
            }
        }
    }
    
    response = trucker.post("truck_driver",json=driver)   

    assert response.status_code == status.HTTP_201_CREATED
