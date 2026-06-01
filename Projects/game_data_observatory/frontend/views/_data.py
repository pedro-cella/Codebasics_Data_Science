"""
views/_data.py — helpers de dados compartilhados entre as páginas.

* parse_multi() : transforma coluna com strings 'A, B, C' em Series flat
* count_multi() : value_counts para esse tipo de coluna
"""
import pandas as pd


def parse_multi(series: pd.Series) -> pd.Series:
    """Explode uma coluna cujas células são strings 'A, B, C'."""
    def split(v):
        if isinstance(v, (list, tuple)):
            return list(v)
        if pd.isna(v):
            return []
        return [s.strip() for s in str(v).split(",") if s.strip()]
    return series.apply(split).explode()


def count_multi(series: pd.Series) -> pd.Series:
    return parse_multi(series).value_counts()
