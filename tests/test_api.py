from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_prediction():

    payload = {

        "Gender": "male",
        "Age": 25,
        "Height": 175,
        "Weight": 70,
        "Duration": 30,
        "Heart_Rate": 120,
        "Body_Temp": 38.5
    }

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "predicted_calories" in data