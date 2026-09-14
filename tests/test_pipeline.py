from src.predict import prepare_input
from app.model_loader import load_features


def test_prepare_input():

    features = load_features()

    sample_input = {
        "Gender": "male",
        "Age": 25,
        "Height": 175,
        "Weight": 70,
        "Duration": 30,
        "Heart_Rate": 120,
        "Body_Temp": 38.5
    }

    processed = prepare_input(
        sample_input,
        features
    )

    assert processed.shape[0] == 1