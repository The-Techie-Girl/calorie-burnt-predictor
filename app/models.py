from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime
from datetime import UTC
from app.database import Base


class PredictionLog(Base):

    __tablename__ = "prediction_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    gender = Column(String)

    age = Column(Integer)

    height = Column(Float)

    weight = Column(Float)

    duration = Column(Float)

    heart_rate = Column(Float)

    body_temp = Column(Float)

    predicted_calories = Column(Float)

    created_at = Column(
        DateTime,
        default=lambda: datetime.now(UTC)
    )