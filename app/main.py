from fastapi import FastAPI
from app.model import load_model, predict
from app.schemas import PredictionRequest, PredictionResponse

app = FastAPI(title="FastAPI ML API for Artist Advance Prediction")

model = load_model()

@app.get("/status")
def get_status():
    return {"status": "API is running"}

@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest):
    estimated = predict(model, request)
    return PredictionResponse(estimated_advance=estimated)
