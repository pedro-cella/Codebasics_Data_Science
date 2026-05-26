from typing import Optional

from fastapi import APIRouter
from backend.schemas.game import Game
from backend.database.queries.games_queries import (
    get_all_games,
    get_game_by_id,
    get_top_rated_games,
    get_most_engaged_games,
)
from backend.services.analytics_service import (
    get_summary_metrics,
    get_platform_distribution,
    get_esrb_distribution,
    get_top_tags,
    get_genre_distribution,
    get_year_distribution,
    get_rating_metacritic_data,
    get_engagement_rating_data,
    get_engagement_quartiles,
    get_monthly_releases_for_top_years,
)


router = APIRouter()

# GET /games
@router.get("/games", response_model=list[Game])
def read_games():
    return get_all_games()

# GET /games/top-rated
@router.get("/games/top-rated", response_model=list[Game])
def read_top_rated_games(limit: int = 10):
    return get_top_rated_games(limit)

# GET /games/most-engaged
@router.get("/games/most-engaged", response_model=list[Game])
def read_most_engaged_games(limit: int = 10):
    return get_most_engaged_games(limit)

# GET /games/{game_id}
@router.get("/games/{game_id}", response_model=Optional[Game])
def read_game_by_id(game_id: int):
    return get_game_by_id(game_id)

# GET /analytics/summary
@router.get("/analytics/summary", response_model=dict)
def read_summary_metrics():
    return get_summary_metrics()

# GET /analytics/platforms
@router.get("/analytics/platforms", response_model=list[dict])
def read_platforms_distribution():
    return get_platform_distribution().to_dict(orient="records")

# GET /analytics/esrb
@router.get("/analytics/esrb", response_model=list[dict])
def read_esrb_distribution():
    return get_esrb_distribution().to_dict(orient="records")

# GET /analytics/tags
@router.get("/analytics/tags", response_model=list[dict])
def read_top_tags():
    return get_top_tags().to_dict(orient="records")

# GET /analytics/genres
@router.get("/analytics/genres", response_model=list[dict])
def read_genres_distribution():
    return get_genre_distribution().to_dict(orient="records")

# GET /analytics/years
@router.get("/analytics/years", response_model=list[dict])
def read_years_distribution():
    return get_year_distribution().to_dict(orient="records")

# GET /analytics/rating-metacritic
@router.get("/analytics/rating-metacritic", response_model=list[dict])
def read_rating_metacritic_analysis():
    return get_rating_metacritic_data().to_dict(orient="records")

# GET /analytics/engagement-rating
@router.get("/analytics/engagement-rating", response_model=list[dict])
def read_engagement_rating_analysis():
    return get_engagement_rating_data().to_dict(orient="records")

# GET /analytics/engagement-quartiles
@router.get("/analytics/engagement-quartiles", response_model=list[dict])
def read_engagement_per_quartiles_analysis():
    return get_engagement_quartiles().to_dict(orient="records")

# GET /analytics/monthly-releases-top-years
@router.get("/analytics/monthly-releases-top-years", response_model=list[dict])
def read_monthly_releases_top_years(top_n: int = 3):
    return get_monthly_releases_for_top_years(top_n).to_dict(orient="records")