from backend.database.connection import get_connection


def insert_games(games):

    connection = get_connection()

    cursor = connection.cursor()

    query = """
    INSERT IGNORE INTO games (
        id,
        name,
        released,
        rating,
        ratings_count,
        metacritic,
        genres,
        platforms,
        tags,
        esrb_rating
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    for game in games:

        values = (
            game["id"],
            game["name"],
            game["released"],
            game["rating"],
            game["ratings_count"],
            game["metacritic"],
            game["genres"],
            game["platforms"],
            game["tags"],
            game["esrb_rating"]
        )

        cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()