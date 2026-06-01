"""
theme.py — design tokens, Plotly template e helpers de UI.
Importado pelo app.py e por cada view.
"""
from pathlib import Path
import streamlit as st
import plotly.io as pio
import plotly.graph_objects as go

# --------------------------------------------------------------------------
# Palette (espelho do style.css)
# --------------------------------------------------------------------------
PALETTE = {
    "bg":      "#0d1016",
    "surface": "#141925",
    "border":  "#262d3a",
    "text":    "#e6e9ef",
    "muted":   "#8b94a7",
    "faint":   "#5d6678",
    "primary": "#7c5cff",
    "teal":    "#19c3a8",
    "blue":    "#36a2ff",
    "amber":   "#f7b955",
    "pink":    "#ff5d8f",
    "green":   "#4ad991",
}

COLORWAY = ["#7c5cff", "#19c3a8", "#36a2ff", "#f7b955",
            "#ff5d8f", "#4ad991", "#b78bff", "#ff8a5c", "#5cd0ff"]

FONT = "IBM Plex Sans, system-ui, sans-serif"
MONO = "IBM Plex Mono, monospace"


# --------------------------------------------------------------------------
# Plotly template
# --------------------------------------------------------------------------
def register_template() -> None:
    axis = dict(
        gridcolor="rgba(140,150,170,0.12)",
        linecolor="rgba(140,150,170,0.28)",
        zerolinecolor="rgba(140,150,170,0.12)",
        tickfont=dict(color=PALETTE["muted"]),
        title=dict(font=dict(color=PALETTE["muted"], size=13)),
    )
    pio.templates["gdo"] = go.layout.Template(
        layout=dict(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            colorway=COLORWAY,
            font=dict(family=FONT, color=PALETTE["muted"], size=13),
            margin=dict(l=56, r=18, t=14, b=42),
            xaxis=axis, yaxis=axis,
            hoverlabel=dict(
                bgcolor="#1c222e",
                bordercolor="rgba(140,150,170,0.25)",
                font=dict(family=MONO, color=PALETTE["text"], size=12),
            ),
            legend=dict(font=dict(color=PALETTE["muted"], size=12)),
        )
    )
    pio.templates.default = "gdo"


def style_fig(fig: go.Figure, height: int = 320, **layout) -> go.Figure:
    fig.update_layout(template="gdo", height=height, **layout)
    return fig


PLOTLY_CONFIG = {"displayModeBar": False, "responsive": True}


# --------------------------------------------------------------------------
# CSS loader
# --------------------------------------------------------------------------
def load_css(path: str = "style.css") -> None:
    css = Path(__file__).parent.joinpath(path).read_text(encoding="utf-8")
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


# --------------------------------------------------------------------------
# UI helpers
# --------------------------------------------------------------------------
def page_header(eyebrow: str, title: str, desc: str) -> None:
    st.markdown(
        f"<p class='gdo-eyebrow'>{eyebrow}</p>"
        f"<h1 class='gdo-title'>{title}</h1>"
        f"<p class='gdo-desc'>{desc}</p>",
        unsafe_allow_html=True,
    )


def kpi_card(value: str, label: str, note: str = "", unit: str = "",
             accent: str = "primary", glyph: str = "sq") -> str:
    color = PALETTE.get(accent, accent)
    unit_html = f"<small> {unit}</small>" if unit else ""
    note_html = f"<div class='kpi-note'>{note}</div>" if note else ""
    return (
        f"<div class='kpi' style='--accent:{color}'>"
        f"<div class='kpi-glyph {glyph}'><i></i></div>"
        f"<div class='kpi-value'>{value}{unit_html}</div>"
        f"<div class='kpi-label'>{label}</div>{note_html}</div>"
    )


def card_title(title: str, kind: str = "") -> None:
    kind_html = f"<span class='kind'>{kind}</span>" if kind else ""
    st.markdown(f"<div class='card-title'>{title}{kind_html}</div>",
                unsafe_allow_html=True)
