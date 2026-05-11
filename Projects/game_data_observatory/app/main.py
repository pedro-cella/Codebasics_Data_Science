from src.api.rawg_client import get_games, parse_games
from src.database.insert_games import insert_games

all_games = []

for page in range(1, 4):
    raw_data = get_games(page_size=40, page=page)
    parsed_games = parse_games(raw_data)
    all_games.extend(parsed_games)

insert_games(all_games)

print(f"{len(all_games)} games processed successfully!")