from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import PredictionRequest
from app.model_loader import load_model, load_features
from app.database import get_db
from app.models import PredictionLog

from src.predict import prepare_input

router = APIRouter()

# Load model and features once when API starts
model = load_model()
features = load_features()


@router.get("/")
def home():
    return {
        "message": "Calorie Burnt Predictor API Running"
    }

@router.get("/predictions")
def get_predictions(
    db: Session = Depends(get_db)
):

    predictions = (
        db.query(PredictionLog)
        .order_by(
            PredictionLog.created_at.desc()
        )
        .all()
    )

    return predictions

@router.post("/predict")
def predict(
    request: PredictionRequest,
    db: Session = Depends(get_db)
):
    
    # Convert request to dictionary
    user_input = request.model_dump()

    # Prepare input data
    processed_data = prepare_input(
        user_input,
        features
    )

    # Make prediction
    prediction = model.predict(
        processed_data
    )

    predicted_value = round(
        float(prediction[0]),
        2
    )

    # Save prediction to database
    log = PredictionLog(
        gender=request.Gender,
        age=request.Age,
        height=request.Height,
        weight=request.Weight,
        duration=request.Duration,
        heart_rate=request.Heart_Rate,
        body_temp=request.Body_Temp,
        predicted_calories=predicted_value
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    # Return response
    return {
        "predicted_calories": predicted_value
    }