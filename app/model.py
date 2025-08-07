import joblib
import os
import numpy as np
from app.schemas import PredictionRequest

MODEL_PATH = os.getenv("MODEL_PATH", "app/sample_model.pkl")

def load_model():
    return joblib.load(MODEL_PATH)

def predict(model, input_data: PredictionRequest) -> float:
    features = [
        input_data.royalties_last_6_months,
        input_data.instagram_followers,
        input_data.track_release_count,
        input_data.sentiment_score
    ]
    prediction = model.predict([features])[0]
    return float(prediction)
