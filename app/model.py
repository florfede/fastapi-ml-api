import joblib
import os
import numpy as np

MODEL_PATH = os.getenv("MODEL_PATH", "app/sample_model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, features: dict) -> float:
    input_array = np.array([list(features.values())])
    prediction = model.predict(input_array)[0]
    return float(prediction)
