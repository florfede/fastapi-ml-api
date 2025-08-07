from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "API is running"}

def test_predict():
    payload = {
        "royalties_last_6_months": 95431.5,
        "instagram_followers": 1200000,
        "track_release_count": 5,
        "sentiment_score": 0.72
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "estimated_advance" in response.json()
