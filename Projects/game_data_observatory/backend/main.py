from fastapi import FastAPI
from backend.api.routes import router
import logging

# Create root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Define format
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setFormatter(formatter)

# Add both to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

app = FastAPI(
    title="Game Data Observatory API",
    description="API for game analytics and exploration",
    version="1.0.0"
)

app.include_router(router)