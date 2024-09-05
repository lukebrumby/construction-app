import streamlit as st
import pandas as pd
import plotly.express as px

# Sample Data for the bar graph (Purchase/Conversion)
data_bar = {
    "Category": ["Electronics", "Clothing", "Home Goods", "Sports", "Books"],
    "Purchases": [150, 240, 120, 200, 180],
    "Conversions": [120, 220, 110, 170, 150],
}
df_bar = pd.DataFrame(data_bar)

# Bar graph (Purchases vs Conversions)
st.header("Purchase vs Conversion by Category")
bar_fig = px.bar(
    df_bar, 
    x="Category", 
    y=["Purchases", "Conversions"], 
    barmode="group",
    title="Purchases and Conversions by Category"
)
st.plotly_chart(bar_fig)

# Sample Data for the line graph (In-store vs Online purchases over time)
data_line = {
    "Date": pd.date_range(start="2024-01-01", periods=12, freq="M"),
    "In-store Purchases": [120, 135, 140, 155, 170, 160, 175, 180, 195, 200, 210, 220],
    "Online Purchases": [100, 120, 110, 130, 150, 140, 160, 170, 185, 190, 195, 205],
}
df_line = pd.DataFrame(data_line)

# Line graph (In-store vs Online Purchases)
st.header("In-store vs Online Purchases Over Time")
line_fig = px.line(
    df_line,
    x="Date",
    y=["In-store Purchases", "Online Purchases"],
    title="In-store vs Online Purchases Over Time",
    labels={"value": "Number of Purchases"},
)
st.plotly_chart(line_fig)

# Optionally, add interactivity such as filters
st.sidebar.header("Filters")
selected_category = st.sidebar.multiselect(
    "Select Category", options=df_bar["Category"].unique(), default=df_bar["Category"].unique()
)

if selected_category:
    filtered_df_bar = df_bar[df_bar["Category"].isin(selected_category)]
    filtered_bar_fig = px.bar(
        filtered_df_bar, 
        x="Category", 
        y=["Purchases", "Conversions"], 
        barmode="group"
    )
    st.plotly_chart(filtered_bar_fig)
