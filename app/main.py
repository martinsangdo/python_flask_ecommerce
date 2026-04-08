from fastapi import FastAPI
from app.controllers.user_controller import router as user_router

app = FastAPI(title="FastAPI MVC MongoDB")

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "API is running"}