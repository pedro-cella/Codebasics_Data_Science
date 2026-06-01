"""
Game Data Observatory — Streamlit app.

Run (com o FastAPI já rodando):
    cd frontend
    streamlit run app.py

Este arquivo é responsável por: page config, CSS, sidebar, navegação e
carregamento dos dados via FastAPI.
"""
import pandas as pd
import requests
import streamlit as st

import theme
from views import overview, univariate, bivariate

st.set_page_config(
    page_title="Game Data Observatory",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

theme.register_template()
theme.load_css()

BASE_URL = "http://127.0.0.1:8000"


# -------------------------------------------------------------------
# DATA — busca os dados da FastAPI e monta um DataFrame unificado
# -------------------------------------------------------------------
@st.cache_data(ttl=300)  # cache de 5 minutos
def load_data() -> pd.DataFrame | None:
    try:
        response = requests.get(f"{BASE_URL}/games", timeout=10)
        response.raise_for_status()
        df = pd.DataFrame(response.json())
        df["released"] = pd.to_datetime(df["released"], errors="coerce")
        # renomeia ratings_count para added para compatibilidade com os charts
        df = df.rename(columns={"ratings_count": "added"})
        return df
    except requests.exceptions.ConnectionError:
        st.error("⚠️ Não foi possível conectar à API. Verifique se o FastAPI está rodando em http://127.0.0.1:8000")
        return None
    except Exception as e:
        st.error(f"⚠️ Erro ao carregar dados: {e}")
        return None


@st.cache_data(ttl=300)
def load_summary() -> dict | None:
    try:
        response = requests.get(f"{BASE_URL}/analytics/summary", timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception:
        return None


df = load_data()
summary = load_summary()


# -------------------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------------------
with st.sidebar:
    st.markdown(
        "<div class='gdo-brand'>"
        "<div class='mark'><span></span></div>"
        "<div><div class='nm'>Game Data<br>Observatory</div>"
        "<div class='sub'>RAWG · analytics</div></div></div>",
        unsafe_allow_html=True,
    )

    st.markdown("<div class='gdo-navlabel'>Páginas</div>", unsafe_allow_html=True)
    page = st.radio(
        "nav", ["Overview", "Univariate", "Bivariate"],
        label_visibility="collapsed",
    )

    n = f"{len(df):,}".replace(",", ".") if df is not None else "—"
    st.markdown(
        f"<div class='gdo-foot'><span class='gdo-pill'>{n} games</span><br><br>"
        "source: RAWG API<br>portfolio · data science</div>",
        unsafe_allow_html=True,
    )


# -------------------------------------------------------------------
# ROUTER
# -------------------------------------------------------------------
if page == "Overview":
    overview.render(df, summary)
elif page == "Univariate":
    univariate.render(df)
else:
    bivariate.render(df)
