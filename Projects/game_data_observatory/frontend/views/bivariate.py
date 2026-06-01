"""
views/bivariate.py — Page 03 · four relationships between variables.

Reads from df:
    rating       (float 0-5)
    metacritic   (float 0-100)
    added        (int, engagement proxy — mapped from ratings_count)
    released     (datetime)
    name         (str)
"""
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

import theme

PRI = theme.PALETTE["primary"]
WAY = theme.COLORWAY


def _card(title, kind):
    box = st.container(border=True)
    with box:
        theme.card_title(title, kind)
    return box


def render(df):
    theme.page_header(
        "03 · Bivariate Analysis", "Relationships between variables",
        "Where pairs of metrics intersect — correlation between critics and users, "
        "engagement effect, and release seasonality.",
    )

    if df is None:
        st.warning("Data unavailable. Make sure the FastAPI server is running at http://127.0.0.1:8000")
        return

    c1, c2 = st.columns(2, gap="medium")

    # ---- Rating vs Metacritic : scatter + trendline ----
    with c1:
        with _card("Rating vs Metacritic", "scatter + trend"):
            clean = df[["rating", "metacritic", "name"]].dropna()
            x, y = clean["rating"], clean["metacritic"]
            m, b = np.polyfit(x, y, 1)
            xs = np.array([x.min(), x.max()])
            fig = go.Figure()
            fig.add_trace(go.Scattergl(
                x=x, y=y, mode="markers", text=clean["name"],
                marker=dict(size=7, color=PRI, opacity=0.55),
                hovertemplate="%{text}<br>Rating %{x}<br>Metacritic %{y}<extra></extra>"))
            fig.add_trace(go.Scatter(
                x=xs, y=m * xs + b, mode="lines",
                line=dict(color=WAY[4], width=2, dash="dash"), hoverinfo="skip"))
            theme.style_fig(fig, height=320, showlegend=False)
            fig.update_xaxes(title="Rating (0–5)")
            fig.update_yaxes(title="Metacritic")
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    # ---- Engagement vs Rating : bubble ----
    with c2:
        with _card("Engagement vs Rating", "bubble"):
            fig = go.Figure(go.Scattergl(
                x=df["rating"], y=df["added"], text=df["name"],
                mode="markers",
                marker=dict(
                    size=np.clip(np.sqrt(df["added"]) / 8, 5, 34),
                    color=df["rating"],
                    colorscale=[[0, "#36a2ff"], [0.5, "#7c5cff"], [1, "#ff5d8f"]],
                    opacity=0.6, showscale=False),
                hovertemplate="%{text}<br>Rating %{x}<br>Engagement %{y:,}<extra></extra>"))
            theme.style_fig(fig, height=320)
            fig.update_xaxes(title="Rating (0–5)")
            fig.update_yaxes(title="Engagement (ratings_count)")
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    c3, c4 = st.columns(2, gap="medium")

    # ---- Engagement by rating quartile : boxplot ----
    with c3:
        with _card("Engagement by Rating Quartile", "boxplot"):
            q = df.copy()
            labels = ["Q1 · low", "Q2", "Q3", "Q4 · high"]
            q["quartile"] = pd.qcut(q["rating"], 4, labels=labels)
            fig = go.Figure()
            for i, lab in enumerate(labels):
                fig.add_trace(go.Box(
                    y=q.loc[q["quartile"] == lab, "added"], name=lab,
                    marker_color=WAY[i], line=dict(width=1.5),
                    fillcolor="rgba(124,92,255,0.10)", boxpoints="outliers"))
            theme.style_fig(fig, height=320, showlegend=False)
            fig.update_xaxes(title="Rating Quartile")
            fig.update_yaxes(title="Engagement (ratings_count)")
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    # ---- Monthly releases · Top years : multi-line ----
    with c4:
        with _card("Monthly Releases · Top Years", "multi-line"):
            months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            d = df.copy()
            d["year"] = d["released"].dt.year
            d["month"] = d["released"].dt.month
            top_years = d["year"].value_counts().nlargest(5).index.sort_values()
            fig = go.Figure()
            for i, yr in enumerate(top_years):
                counts = (d[d["year"] == yr].groupby("month").size()
                          .reindex(range(1, 13), fill_value=0))
                fig.add_trace(go.Scatter(
                    x=months, y=counts.values, mode="lines+markers", name=str(int(yr)),
                    line=dict(color=WAY[i % len(WAY)], width=2.5, shape="spline"),
                    marker=dict(size=5),
                    hovertemplate=f"{int(yr)} · %{{x}}<br>%{{y}} releases<extra></extra>"))
            theme.style_fig(fig, height=320, margin=dict(l=56, r=18, t=28, b=36),
                            legend=dict(orientation="h", y=1.12, x=0))
            fig.update_yaxes(title="Releases")
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)
