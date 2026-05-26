from pydantic import BaseModel
from datetime import datetime

class Game(BaseModel):
    id: int
    name: str
    released: datetime | None
    rating: float
    ratings_count: int
    metacritic: int | None
    genres: str
    platforms: str
    tags: str
    esrb_rating: str | None