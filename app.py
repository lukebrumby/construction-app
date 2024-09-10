import streamlit as st
import pandas as pd
import plotly.express as px

# Sample Data for the bar graph (Signup/Purchase)
data_bar = {
    "Customer engagement": ["First", "Second", "Third", "Fourth"],
    "Interaction": [200, 300, 400, 250],
    "Purchase": [150, 240, 350, 200],
}
df_bar = pd.DataFrame(data_bar)

# Bar graph (Signup vs Purchase with blue and gray colors)
st.header("Signup vs Purchase by Category")
bar_fig = px.bar(
    df_bar, 
    x="Category", 
    y=["Signup", "Purchase"], 
    barmode="group",
    title="Signup and Purchase by Category",
    color_discrete_map={"Signup": "skyblue", "Purchase": "lightgray"}
)
st.plotly_chart(bar_fig)

# Sample Data for the line graph (In-store vs Online purchases over time)
data_line = {
    "Date": pd.date_range(start="2024-01-01", periods=12, freq="M"),
    "In-store Purchases": [120, 135, 140, 155, 170, 160, 175, 180, 195, 200, 210, 220],
    "Online Purchases": [100, 120, 110, 130, 150, 140, 160, 170, 185, 190, 195, 205],
}
df_line = pd.DataFrame(data_line)

# Format the 'Date' column to only show the month
df_line['Month'] = df_line['Date'].dt.strftime('%B')  # Use '%b' for short month names

# Line graph (In-store vs Online Purchases with blue and gray colors)
st.header("In-store vs Online Purchases Over Time")
line_fig = px.line(
    df_line,
    x="Month",  # Use the formatted Month column
    y=["In-store Purchases", "Online Purchases"],
    title="In-store vs Online Purchases Over Time",
    labels={"value": "Number of Purchases"},
    color_discrete_map={"In-store Purchases": "skyblue", "Online Purchases": "lightgray"}
)
st.plotly_chart(line_fig)
