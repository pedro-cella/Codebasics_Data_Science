import requests
from backend.config import RAWG_API_KEY

BASE_URL = "https://api.rawg.io/api/games"

def get_games(page_size=40, page=1):
    params = {
        'key': RAWG_API_KEY,
        'page_size': page_size,
        'page': page
    }

    response = requests.get(BASE_URL, params=params)

    return response.json()

def parse_games(data):
    parsed_games = []

    for game in data["results"]:
        game_info = {
            "id": game.get("id"),
            "name": game.get("name"),
            "released": game.get("released"),
            "rating": game.get("rating"),
            "ratings_count": game.get("ratings_count"),
            "metacritic": game.get("metacritic"),
            "genres": ", ".join([genre["name"] for genre in game.get("genres", [])]),
            "platforms": ", ".join([
                platform["platform"]["name"]
                for platform in game.get("platforms", [])
            ]),
            "tags": ", ".join([tag["name"] for tag in game.get("tags", [])]),
            "esrb_rating": (
                game["esrb_rating"]["name"]
                if game.get("esrb_rating")
                else None
            )
        }
        parsed_games.append(game_info)

    return parsed_games