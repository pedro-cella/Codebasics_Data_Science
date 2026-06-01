from backend.database.connection import get_connection
from contextlib import contextmanager
import logging

logger = logging.getLogger(__name__)

@contextmanager
def get_db_cursor(commit=False):
    connection = get_connection()

    cursor = connection.cursor(dictionary=True)
    
    try:
        yield cursor
        if commit:
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def get_all_games():
    logger.info("Fetching all games.")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM games;")
        games = cursor.fetchall()
        logger.info(f"Fetched {len(games)} games")
        return games

def get_game_by_id(game_id):
    logger.info(f"Fetching game with id {game_id}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE id = %s;", (game_id,))
        game = cursor.fetchone()
        logger.info(f"Fetched game with id {game_id}")
        return game

def get_top_rated_games(limit=10):
    logger.info(f"Fetch top {limit} rated games")
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT * FROM games
                          ORDER BY rating DESC
                          LIMIT %s;""", (limit,))
        top_rated_games = cursor.fetchall()
        logger.info(f"Fetched {limit} top rated games")
        return top_rated_games
    
def get_most_engaged_games(limit=10):
    logger.info(f"Fetching top {limit} most engaged games")
    with get_db_cursor() as cursor:
        cursor.execute("""SELECT * FROM games
                          ORDER BY ratings_count DESC
                          LIMIT %s;""", (limit,))
        most_engaged_games = cursor.fetchall()
        logger.info(f"Fetched {limit} most engaged games")
        return most_engaged_games
    
def get_games_by_year(year):
    logger.info("Fetch games by year")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE YEAR(released) = %s;", (year,))
        games_by_year = cursor.fetchall()
        logger.info(f"Fetched {len(games_by_year)} from {year}")
        return games_by_year

def get_games_by_esrb(esrb_rate):
    logger.info("Fetch games by esrb")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM games WHERE esrb_rating = %s;", (esrb_rate,))
        games_by_esrb = cursor.fetchall()
        logger.info(f"Fetched {len(games_by_esrb)} in ESRB {esrb_rate}")
        return games_by_esrb