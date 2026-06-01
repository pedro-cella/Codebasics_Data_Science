from typing import Optional
import mysql.connector
from fastapi import APIRouter, HTTPException
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
    try:
        all_games = get_all_games()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
    
    return all_games 

# GET /games/top-rated
@router.get("/games/top-rated", response_model=list[Game])
def read_top_rated_games(limit: int = 10):
    if limit <= 0:
        raise HTTPException(status_code=400, detail="Limit must be a positive integer")
    
    try:
        top_rated_games = get_top_rated_games(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    return top_rated_games

# GET /games/most-engaged
@router.get("/games/most-engaged", response_model=list[Game])
def read_most_engaged_games(limit: int = 10):

    if limit <= 0:
        raise HTTPException(status_code=400, detail="Limit must be a positive integer")

    try:
        most_engaged =  get_most_engaged_games(limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    return most_engaged

# GET /games/{game_id}
@router.get("/games/{game_id}", response_model=Game)
def read_game_by_id(game_id: int):

    try:
        game = get_game_by_id(game_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

    if game is None:
        raise HTTPException(status_code=404, detail="Game not found")
    
    return game 

# GET /analytics/summary
@router.get("/analytics/summary", response_model=dict)
def read_summary_metrics():
    try:
        summary_metrics = get_summary_metrics()
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return summary_metrics

# GET /analytics/platforms
@router.get("/analytics/platforms", response_model=list[dict])
def read_platforms_distribution():
    try:
        platform_distribution = get_platform_distribution().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return platform_distribution

# GET /analytics/esrb
@router.get("/analytics/esrb", response_model=list[dict])
def read_esrb_distribution():
    try:
        esrb_distribution = get_esrb_distribution().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return esrb_distribution

# GET /analytics/tags
@router.get("/analytics/tags", response_model=list[dict])
def read_top_tags():
    try:
        top_tags = get_top_tags().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return top_tags

# GET /analytics/genres
@router.get("/analytics/genres", response_model=list[dict])
def read_genres_distribution():
    try:
        genres_distribution = get_genre_distribution().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return genres_distribution

# GET /analytics/years
@router.get("/analytics/years", response_model=list[dict])
def read_years_distribution():
    try:
        years_distribution = get_year_distribution().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return years_distribution

# GET /analytics/rating-metacritic
@router.get("/analytics/rating-metacritic", response_model=list[dict])
def read_rating_metacritic_analysis():
    try:
        rating_metacritic_analysis = get_rating_metacritic_data().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return rating_metacritic_analysis

# GET /analytics/engagement-rating
@router.get("/analytics/engagement-rating", response_model=list[dict])
def read_engagement_rating_analysis():
    try:
        engagement_rating_analysis = get_engagement_rating_data().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return engagement_rating_analysis

# GET /analytics/engagement-quartiles
@router.get("/analytics/engagement-quartiles", response_model=list[dict])
def read_engagement_per_quartiles_analysis():
    try:
        engagement_per_quartiles_analysis = get_engagement_quartiles().to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return engagement_per_quartiles_analysis

# GET /analytics/monthly-releases-top-years
@router.get("/analytics/monthly-releases-top-years", response_model=list[dict])
def read_monthly_releases_top_years(top_n: int = 3):

    if top_n <= 0:
        raise HTTPException(status_code=400, detail="Limit must be a positive integer")

    try:
        monthly_releases_top_years = get_monthly_releases_for_top_years(top_n).to_dict(orient="records")
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail="Database error")
    except (KeyError, ValueError) as e:
        raise HTTPException(status_code=500, detail="Data processing error")
    return monthly_releases_top_years