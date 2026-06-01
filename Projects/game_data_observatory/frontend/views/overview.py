"""
views/overview.py — Page 01 · 5 KPI cards + highlights strip.

Receives:
    df      : DataFrame with all games (from /games)
    summary : dict from /analytics/summary
"""
import streamlit as st

import theme
from ._data import parse_multi


def render(df, summary):
    theme.page_header(
        "01 · Overview", "Catalog at a glance",
        "Key indicators of the dataset — volume, perceived quality, and coverage "
        "across platforms and genres.",
    )

    if df is None or summary is None:
        st.warning("Data unavailable. Make sure the FastAPI server is running at http://127.0.0.1:8000")
        return

    total = f"{summary['total_games']:,}".replace(",", ".")
    avg_rating = f"{summary['average_rating']:.2f}"
    avg_meta = f"{summary['average_metacritic']:.0f}"
    n_plat = summary["total_unique_platforms"]
    n_genre = summary["total_unique_genres"]

    cards = [
        theme.kpi_card(total, "Total Games", "titles in dataset", accent="primary", glyph="sq"),
        theme.kpi_card(avg_rating, "Avg Rating", "user score", unit="/ 5", accent="teal", glyph="ci"),
        theme.kpi_card(avg_meta, "Avg Metacritic", "critic score", unit="/ 100", accent="blue", glyph="di"),
        theme.kpi_card(str(n_plat), "Unique Platforms", "PC, consoles, mobile", accent="amber", glyph="ri"),
        theme.kpi_card(str(n_genre), "Unique Genres", "distinct categories", accent="pink", glyph="tr"),
    ]

    cols = st.columns(5, gap="medium")
    for col, html in zip(cols, cards):
        col.markdown(html, unsafe_allow_html=True)

    yr = df["released"].dt.year
    top_plat = parse_multi(df["platforms"]).value_counts().idxmax()
    top_genre = parse_multi(df["genres"]).value_counts().idxmax()
    esrb_count = df["esrb_rating"].nunique()
    st.markdown(
        "<div class='gdo-strip'>"
        f"<span>📅 Release window &nbsp;<b>{int(yr.min())} – {int(yr.max())}</b></span>"
        f"<span>🖥️ Top platform &nbsp;<b>{top_plat}</b></span>"
        f"<span>🎮 Leading genre &nbsp;<b>{top_genre}</b></span>"
        f"<span>🔞 ESRB coverage &nbsp;<b>{esrb_count} ratings</b></span>"
        "</div>",
        unsafe_allow_html=True,
    )
