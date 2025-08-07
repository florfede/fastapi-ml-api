from fastapi import FastAPI
from app.model import load_model, predict
from app.schemas import PredictionRequest, PredictionResponse

app = FastAPI(title="ML Model API")

model = load_model()

@app.get("/")
def read_root():
    return {"message": "ML API is up and running"}

@app.post("/predict", response_model=PredictionResponse)
def make_prediction(request: PredictionRequest):
    prediction = predict(model, request.features)
    return PredictionResponse(prediction=prediction)
