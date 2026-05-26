from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(
    title="Game Data Observatory API",
    description="API for game analytics and exploration",
    version="1.0.0"
)

app.include_router(router)