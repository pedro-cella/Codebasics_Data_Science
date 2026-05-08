# Streamlit Introduction

## Takeaways
- **Streamlit** is an open-source Python library that allows developers to create **beatiful, interactive web applications** for machine learning and data analysis with minimal effor
- Creating a web application with Streamlit involves **writing standard Python scripts,** where you define the layout and interactivity of the app using Streamlit's rich set of widgets and functions.
- Streamlit autmatically handles **the frontend and updates the UI based on user interactions,** making it straghtforward to prototype and deploy data-drive applications.
- **The framework supports hot-reloading,** which means changes to the code are immediatly reflected in the app without needing to restart the server, enhancing the development process.

## Streamlit Code

```python
import streamlit as st
import pandas as pd

# Text elements
st.header("Streamlit Core Features")
st.subheader("Text Elements")
st.text("This is a simples text element.")

# Data display
st.subheader("Data Display")
st.write("Here is a simple table:")

df = pd.DataFrame({
    "Date": ["2024-08-01", "2024-08-02", "2024-08-03"],
    "Amount": [250, 134, 340]
})
st.table(df)

# Charts
st.subheader("Charts")
st.line_chart([1, 2, 3, 4])

# User Input
st.subheader("User Input")
value = st.slider("Select a value", 0, 100)
st.write(f"Selected value: {value}")

st.title("Interactive Widgets Example")

# Checkkbox
if st.checkbox("Show/Hide"):
    st.write("Cehckbox is checked!")

# Selectbox
option = st.selectbox("Category", ["Rent", "Food"], label_visibility="collapsed")
st.write(f"You selected: {option}")

# Multiselect
options = st.multiselect("Select multiple numbers", [1, 2, 3])
st.write(f"You selected: {options}")
```