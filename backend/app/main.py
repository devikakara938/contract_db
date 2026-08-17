from fastapi import FastAPI

from backend.app.api import user
from backend.app.api import contracts


app = FastAPI(
    title="Contract Obligation Tracking Compliance Management Platform"
)


app.include_router(
    user.router,
    prefix="/users",
    tags=["Users"]
)


app.include_router(
    contracts.router,
    prefix="/contracts",
    tags=["Contracts"]
)


@app.get("/")
def root():
    return {"message": "API is running"}