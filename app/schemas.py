from pydantic import BaseModel

class PredictionRequest(BaseModel):
    royalties_last_6_months: float
    instagram_followers: int
    track_release_count: int
    sentiment_score: float

class PredictionResponse(BaseModel):
    estimated_advance: float
