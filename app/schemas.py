from pydantic import BaseModel
from datetime import datetime


class PredictionRequest(BaseModel):
    Gender: str
    Age: int
    Height: float
    Weight: float
    Duration: float
    Heart_Rate: float
    Body_Temp: float


class PredictionResponse(BaseModel):
    predicted_calories: float


class PredictionHistory(BaseModel):
    id: int
    gender: str
    age: int
    height: float
    weight: float
    duration: float
    heart_rate: float
    body_temp: float
    predicted_calories: float
    created_at: datetime

    class Config:
        from_attributes = True