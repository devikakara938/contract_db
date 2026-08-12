from fastapi import FastAPI

from backend.app.api import user
from backend.app.database import engine, Base
from backend.app.models.user import User



app = FastAPI(
    title="Contract Obligation Tracking Compliance Management Platform"
)


app.include_router(
    user.router,
    prefix="/users",
    tags=["Users"]
)


@app.get("/")
def root():
    return {"message": "API is running"}