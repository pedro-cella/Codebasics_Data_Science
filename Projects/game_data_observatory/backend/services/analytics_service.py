import pandas as pd
from backend.database.queries.games_queries import get_all_games

# =========================
# CREATE DATAFRAME
# =========================

def load_games_dataframe():
    return pd.DataFrame(get_all_games())

# =========================
# HELPING FUNCTIONS
# =========================

def get_unique_platforms():
    df = load_games_dataframe()
    unique_platform = set()
    for list_of_platforms in df['platforms']:
        for platform in list_of_platforms.split(","):
            unique_platform.add(platform.strip())

    return list(unique_platform)

def get_unique_genres():
    df = load_games_dataframe()
    unique_genres = set()
    for list_of_genres in df['genres']:
        for genre in list_of_genres.split(","):
            unique_genres.add(genre.strip())

    return list(unique_genres)

# =========================
# SUMMARY METRICS
# =========================

def get_summary_metrics():
    df = load_games_dataframe()
    summary_metrics = {
        "total_games": int(len(df)),
        "average_rating": float(round(df['rating'].mean(), 2)),
        "average_metacritic": float(round(df['metacritic'].mean(), 2)),
        "total_unique_platforms": len(get_unique_platforms()),
        "total_unique_genres": len(get_unique_genres())
    }
    return summary_metrics

# =========================
# UNIVARIATE ANALYSIS
# =========================

def get_platform_distribution():
    # Load all games table
    df = load_games_dataframe()

    # Separate platform and count the occurrencies
    platform_occurrencies = {}
    for list_of_platforms in df['platforms']:
        for platform in list_of_platforms.split(","):
            platform = platform.strip()
            if platform not in platform_occurrencies:
                platform_occurrencies[platform] = 1
            else:
                platform_occurrencies[platform] += 1

    # Transform the dictionary in a pandas DataFrame
    platform_distribution = pd.DataFrame(
        platform_occurrencies.items(),
        columns=["platform", "count"]
    )

    # Return ordering by count
    return platform_distribution.sort_values(
        by="count",
        ascending=False,
    ).reset_index(drop=True)

def get_esrb_distribution():
    # Load all games table
    df = load_games_dataframe()

    esrb_occurrences = {}

    # Count each esrb occurrencies
    for esrb in df['esrb_rating']:
        if pd.isna(esrb):
            esrb = "Not Rated"
        if esrb not in esrb_occurrences:
            esrb_occurrences[esrb] = 1
        else:
            esrb_occurrences[esrb] += 1

    # Transform to a pandas DataFrame 
    esrb_distribution = pd.DataFrame(
        esrb_occurrences.items(),
        columns=["esrb", "count"]
    )

    # Order by count
    return esrb_distribution.sort_values(
        by="count",
        ascending=False
    ).reset_index(drop=True)

def get_top_tags(limit=20):
    # Load all games table
    df = load_games_dataframe()

    # Separate tags and count the occurrencies
    tags_occurrencies = {}
    for list_of_tags in df['tags']:
        for tag in list_of_tags.split(","):
            tag = tag.strip()
            if tag not in tags_occurrencies:
                tags_occurrencies[tag] = 1
            else:
                tags_occurrencies[tag] += 1

    # Transform the dictionary in a pandas DataFrame
    tag_distribution = pd.DataFrame(
        tags_occurrencies.items(),
        columns=["tag", "count"]
    )

    # Order by count
    return tag_distribution.sort_values(
        by="count",
        ascending=False
    ).head(limit).reset_index(drop=True)

    return tag_distribution

def get_genre_distribution():
    # Load all games table
    df = load_games_dataframe()

    # Separate genres and count the occurrencies
    genre_occurrencies = {}
    for list_of_genres in df['genres']:
        for genre in list_of_genres.split(","):
            genre = genre.strip()
            if genre not in genre_occurrencies:
                genre_occurrencies[genre] = 1
            else:
                genre_occurrencies[genre] += 1

    # Transform the dictionary in a pandas DataFrame
    genre_distribution = pd.DataFrame(
        genre_occurrencies.items(),
        columns=["genre", "count"]
    )

    # Order by count
    return genre_distribution.sort_values(
        by="count",
        ascending=False
    ).reset_index(drop=True)

def get_year_distribution():
    # Load all games table
    df = load_games_dataframe()

    # Convert from Object to datetime64
    df['released'] = pd.to_datetime(df['released'], errors="coerce")

    # Extract year and count occurrences
    df["year"] = df["released"].dt.year
    years_occurrencies = df["year"].value_counts()

    # Transform in a DataFrame
    year_distribution = pd.DataFrame(
        years_occurrencies.items(),
        columns=["year", "count"]
    )

    # Order by count
    return year_distribution.sort_values(
        by="year",
        ascending=True
    ).reset_index(drop=True)

# =========================
# BIVARIATE ANALYSIS
# =========================

def get_rating_metacritic_data():
    # Load all games table
    df = load_games_dataframe()

    # Return a DataFrame with rating and metacritic
    return df[["rating", "metacritic"]].dropna()

def get_engagement_rating_data():
    # Load all games table
    df = load_games_dataframe()

    # Order by rating count
    df = df.sort_values(by='ratings_count', ascending=True)

   # Return a DataFrame with rating and rating_counts
    return df[["ratings_count", "rating"]]

def get_engagement_quartiles():
    # Load all games table
    df = load_games_dataframe()

    # Order by rating count
    df = df.sort_values(by='ratings_count', ascending=True)

    # Create the quartiles
    df["quartile"] = pd.qcut(
        df["ratings_count"],
        4,
        labels=[
            'Low Popularity',
            'Medium Popularity',
            'High Popularity',
            'Very High Popularity'
        ]
    )

    # Return rating and created quartiles
    return df[["rating", "quartile"]]

def get_monthly_releases_for_top_years(top_n=3):
    # Load all games table
    df = load_games_dataframe()

    # Convert from Object to datetime64
    df['released'] = pd.to_datetime(df['released'], errors="coerce")

    # Create year column
    df["year"] = df["released"].dt.year

    # Create month column
    df["month"] = df["released"].dt.month

    # Get top 3 years
    top_n_years = df["year"].value_counts() \
    .head(top_n) \
    .index \
    .tolist()

    #  Filter year column by top_n_years
    df = df[df["year"].isin(top_n_years)]

    # Return year and month grouped by count
    return df.groupby(
        ["year", "month"]
    ).size().reset_index(name="count")

if __name__ == "__main__":
    teste = get_monthly_releases_for_top_years()
    print(teste)