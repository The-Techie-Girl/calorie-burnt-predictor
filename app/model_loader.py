import joblib


MODEL_PATH = "models/model.pkl"


def load_model():

    model = joblib.load(MODEL_PATH)

    return model


def load_features():

    features = joblib.load(
        "models/features.pkl"
    )

    return features