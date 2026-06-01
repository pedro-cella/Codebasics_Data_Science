"""
views/univariate.py — Page 02 · five distributions.

Reads from df:
    platforms    ('A, B' string)  -> horizontal bar
    esrb_rating  (categorical)    -> donut
    tags         ('A, B' string)  -> lollipop
    genres       ('A, B' string)  -> treemap
    released     (datetime)       -> histogram by year
"""
import plotly.graph_objects as go
import streamlit as st

import theme
from ._data import count_multi

PRI = theme.PALETTE["primary"]
WAY = theme.COLORWAY


def _card(title, kind):
    box = st.container(border=True)
    with box:
        theme.card_title(title, kind)
    return box


def render(df):
    theme.page_header(
        "02 · Univariate Analysis", "Distributions",
        "How the catalog breaks down across each dimension: platforms, "
        "age ratings, tags, genres, and release year.",
    )

    if df is None:
        st.warning("Data unavailable. Make sure the FastAPI server is running at http://127.0.0.1:8000")
        return

    # ---- row 1 : platforms (wide) + ESRB (donut) ----
    c1, c2 = st.columns([1.35, 1], gap="medium")

    with c1:
        with _card("Platform Distribution", "bar · horizontal"):
            s = count_multi(df["platforms"]).sort_values().tail(12)
            fig = go.Figure(go.Bar(
                x=s.values, y=s.index, orientation="h",
                marker_color=PRI,
                hovertemplate="%{y}<br>%{x:,} games<extra></extra>",
            ))
            theme.style_fig(fig, height=340, margin=dict(l=130, r=18, t=8, b=36), bargap=0.34)
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    with c2:
        with _card("ESRB Distribution", "donut"):
            s = df["esrb_rating"].fillna("Not Rated").value_counts()
            fig = go.Figure(go.Pie(
                labels=s.index, values=s.values, hole=0.62, sort=True,
                marker=dict(colors=WAY, line=dict(color="#0d1016", width=2)),
                textfont=dict(family=theme.MONO, color=theme.PALETTE["text"], size=12),
                hovertemplate="%{label}<br>%{value:,} (%{percent})<extra></extra>",
            ))
            theme.style_fig(fig, height=340, margin=dict(l=8, r=8, t=8, b=8),
                            annotations=[dict(text="ESRB", x=.5, y=.5, showarrow=False,
                                              font=dict(family=theme.MONO, color=theme.PALETTE["muted"], size=14))])
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    # ---- row 2 : top tags (lollipop) + genres (treemap) ----
    c3, c4 = st.columns(2, gap="medium")

    with c3:
        with _card("Top Tags", "lollipop"):
            s = count_multi(df["tags"]).sort_values().tail(10)
            fig = go.Figure()
            for tag, val in s.items():
                fig.add_trace(go.Scatter(
                    x=[0, val], y=[tag, tag], mode="lines",
                    line=dict(color="rgba(124,92,255,0.35)", width=3),
                    hoverinfo="skip", showlegend=False))
            fig.add_trace(go.Scatter(
                x=s.values, y=s.index, mode="markers",
                marker=dict(size=13, color=WAY[1], line=dict(color="#0d1016", width=1.5)),
                hovertemplate="%{y}<br>%{x:,} games<extra></extra>", showlegend=False))
            theme.style_fig(fig, height=300, margin=dict(l=165, r=18, t=8, b=36))
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    with c4:
        with _card("Genre Distribution", "treemap"):
            s = count_multi(df["genres"])
            fig = go.Figure(go.Treemap(
                labels=s.index, parents=[""] * len(s), values=s.values,
                marker=dict(colors=[WAY[i % len(WAY)] for i in range(len(s))],
                            line=dict(color="#0d1016", width=2)),
                textfont=dict(family=theme.FONT, color="#0d1016", size=14),
                texttemplate="<b>%{label}</b><br>%{value:,}",
                hovertemplate="%{label}<br>%{value:,} games<extra></extra>",
                tiling=dict(pad=2),
            ))
            theme.style_fig(fig, height=300, margin=dict(l=4, r=4, t=4, b=4))
            st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)

    # ---- row 3 : releases by year (full width) ----
    with _card("Release Year Distribution", "histogram"):
        s = df["released"].dt.year.value_counts().sort_index()
        fig = go.Figure(go.Bar(
            x=s.index, y=s.values, marker_color=WAY[2],
            hovertemplate="%{x}<br>%{y:,} releases<extra></extra>",
        ))
        theme.style_fig(fig, height=240, bargap=0.12, margin=dict(l=56, r=18, t=8, b=36))
        fig.update_xaxes(dtick=3)
        st.plotly_chart(fig, width="stretch", config=theme.PLOTLY_CONFIG)
