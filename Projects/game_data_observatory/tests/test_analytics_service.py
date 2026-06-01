import pandas as pd
import pytest
from unittest.mock import patch

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

# =========================
# FAKE DATA
# =========================

# Este DataFrame substitui o banco de dados durante os testes.
# Toda vez que load_games_dataframe() for chamada, ela retorna isso.
MOCK_GAMES_DF = pd.DataFrame([
    {
        "id": 1,
        "name": "Game A",
        "released": "2020-03-15",
        "rating": 4.5,
        "ratings_count": 5000,
        "metacritic": 90,
        "genres": "Action, RPG",
        "platforms": "PC, PlayStation",
        "tags": "Singleplayer, Open World",
        "esrb_rating": "Mature"
    },
    {
        "id": 2,
        "name": "Game B",
        "released": "2020-07-20",
        "rating": 3.8,
        "ratings_count": 1500,
        "metacritic": 75,
        "genres": "Action, Shooter",
        "platforms": "PC, Xbox",
        "tags": "Multiplayer, Singleplayer",
        "esrb_rating": "Teen"
    },
    {
        "id": 3,
        "name": "Game C",
        "released": "2021-11-05",
        "rating": 4.2,
        "ratings_count": 8000,
        "metacritic": None,
        "genres": "RPG",
        "platforms": "PlayStation",
        "tags": "Open World, Singleplayer",
        "esrb_rating": None
    },
    {
        "id": 4,
        "name": "Game D",
        "released": "2021-02-28",
        "rating": 2.9,
        "ratings_count": 300,
        "metacritic": 60,
        "genres": "Shooter",
        "platforms": "Xbox",
        "tags": "Multiplayer",
        "esrb_rating": "Everyone"
    },
])

# =========================
# FIXTURE
# =========================

# Fixture é uma forma do pytest preparar algo antes dos testes.
# Aqui usamos para aplicar o mock automaticamente em todos os testes
# que receberem "mock_df" como parâmetro.
@pytest.fixture
def mock_df():
    # O patch substitui load_games_dataframe pelo nosso DataFrame fake
    # enquanto o teste estiver rodando. Depois ele restaura o original.
    with patch(
        "backend.services.analytics_service.load_games_dataframe",
        return_value=MOCK_GAMES_DF
    ):
        yield  # os testes rodam aqui

# =========================
# TESTES - SUMMARY METRICS
# =========================

def test_summary_metrics_keys(mock_df):
    """Verifica se o dicionário retornado tem todas as chaves esperadas."""
    result = get_summary_metrics()
    expected_keys = {
        "total_games",
        "average_rating",
        "average_metacritic",
        "total_unique_platforms",
        "total_unique_genres"
    }
    assert set(result.keys()) == expected_keys

def test_summary_metrics_total_games(mock_df):
    """Verifica se o total de jogos está correto."""
    result = get_summary_metrics()
    assert result["total_games"] == 4

def test_summary_metrics_average_rating(mock_df):
    """Verifica se a média de rating está correta."""
    result = get_summary_metrics()
    expected = round((4.5 + 3.8 + 4.2 + 2.9) / 4, 2)
    assert result["average_rating"] == expected

# =========================
# TESTES - PLATFORM DISTRIBUTION
# =========================

def test_platform_distribution_returns_dataframe(mock_df):
    """Verifica se o retorno é um DataFrame."""
    result = get_platform_distribution()
    assert isinstance(result, pd.DataFrame)

def test_platform_distribution_columns(mock_df):
    """Verifica se as colunas estão corretas."""
    result = get_platform_distribution()
    assert list(result.columns) == ["platform", "count"]

def test_platform_distribution_sorted(mock_df):
    """Verifica se está ordenado do maior para o menor."""
    result = get_platform_distribution()
    counts = result["count"].tolist()
    assert counts == sorted(counts, reverse=True)

def test_platform_distribution_pc_count(mock_df):
    """Verifica se o PC foi contado corretamente (aparece em Game A e Game B)."""
    result = get_platform_distribution()
    pc_row = result[result["platform"] == "PC"]
    assert pc_row["count"].values[0] == 2

# =========================
# TESTES - ESRB DISTRIBUTION
# =========================

def test_esrb_distribution_handles_none(mock_df):
    """Verifica se jogos sem ESRB são classificados como 'Not Rated'."""
    result = get_esrb_distribution()
    assert "Not Rated" in result["esrb"].values

def test_esrb_distribution_columns(mock_df):
    """Verifica se as colunas estão corretas."""
    result = get_esrb_distribution()
    assert list(result.columns) == ["esrb", "count"]

# =========================
# TESTES - TOP TAGS
# =========================

def test_top_tags_limit(mock_df):
    """Verifica se o limite de tags é respeitado."""
    result = get_top_tags(limit=2)
    assert len(result) <= 2

def test_top_tags_columns(mock_df):
    """Verifica se as colunas estão corretas."""
    result = get_top_tags()
    assert list(result.columns) == ["tag", "count"]

def test_top_tags_singleplayer_count(mock_df):
    """Verifica se Singleplayer foi contado corretamente (aparece em 3 jogos)."""
    result = get_top_tags()
    singleplayer_row = result[result["tag"] == "Singleplayer"]
    assert singleplayer_row["count"].values[0] == 3

# =========================
# TESTES - YEAR DISTRIBUTION
# =========================

def test_year_distribution_sorted_ascending(mock_df):
    """Verifica se está ordenado por ano crescente."""
    result = get_year_distribution()
    years = result["year"].tolist()
    assert years == sorted(years)

def test_year_distribution_correct_years(mock_df):
    """Verifica se os anos corretos foram extraídos (2020 e 2021)."""
    result = get_year_distribution()
    assert set(result["year"].tolist()) == {2020, 2021}

# =========================
# TESTES - RATING VS METACRITIC
# =========================

def test_rating_metacritic_drops_null(mock_df):
    """Verifica se jogos sem metacritic foram removidos (Game C não tem)."""
    result = get_rating_metacritic_data()
    # Dos 4 jogos, Game C não tem metacritic — devem sobrar 3
    assert len(result) == 3

def test_rating_metacritic_columns(mock_df):
    """Verifica se as colunas estão corretas."""
    result = get_rating_metacritic_data()
    assert list(result.columns) == ["rating", "metacritic"]

# =========================
# TESTES - ENGAGEMENT QUARTILES
# =========================

def test_engagement_quartiles_labels(mock_df):
    """Verifica se os 4 labels de quartil estão presentes."""
    result = get_engagement_quartiles()
    expected_labels = {
        "Low Popularity",
        "Medium Popularity",
        "High Popularity",
        "Very High Popularity"
    }
    assert set(result["quartile"].astype(str).unique()) == expected_labels

def test_engagement_quartiles_columns(mock_df):
    """Verifica se as colunas estão corretas."""
    result = get_engagement_quartiles()
    assert list(result.columns) == ["rating", "quartile"]

# =========================
# TESTES - MONTHLY RELEASES
# =========================

def test_monthly_releases_columns(mock_df):
    """Verifica se as colunas estão corretas."""
    result = get_monthly_releases_for_top_years()
    assert list(result.columns) == ["year", "month", "count"]

def test_monthly_releases_top_n(mock_df):
    """Verifica se apenas os anos do top_n aparecem no resultado."""
    result = get_monthly_releases_for_top_years(top_n=1)
    # Com top_n=1, apenas 1 ano deve aparecer
    assert result["year"].nunique() == 1
