import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

def test_status_code():
    client = app.test_client()
    response = client.get("/authors")
    assert response.status_code == 200

def test_body():
    client = app.test_client()
    response = client.get("/authors")
    assert response.json == [
      {
        "name": "Julia Donaldson",
        "dob": "1948-09-16"
      },
      {
        "name": "Andrea Beaty",
        "dob": "1961-10-08"
      },
      {
        "name": "Kelly Barnhill",
        "dob": "1973-01-01"
      },
      {
        "name": "Zetta Elliott",
        "dob": "1979-11-11"
      }
    ]
