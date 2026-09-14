from fastapi import FastAPI

from app.routes import router

from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Calorie Burnt Predictor API",
    version="1.0"
)

app.include_router(router)