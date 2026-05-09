import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_month_tab():
    st.title("Expense Breakdown By Month")
    response = requests.get(f"{API_URL}/analytics_monthly/")
    data = response.json()

    if data:
      df = pd.DataFrame(data)

      st.bar_chart(data=df.set_index("month_name")["total"], use_container_width=True)

      df_display = df.rename(columns={
         "month_number": "",
         "month_name": "Month Name",
         "total": "Total"
      })

      df_display["Total"] = df_display["Total"].map("{:.2f}".format)

      st.table(df_display)
    else:
      st.info("No data found to analyze")