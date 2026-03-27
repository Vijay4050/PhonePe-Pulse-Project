import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ---------- PAGE ----------
st.set_page_config(layout="wide")
st.title("🏆 Top Performers (Toppers)")

# ---------- DB CONNECTION ----------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="phonepe_db"
)

# ---------- SELECT METRIC ----------
metric = st.selectbox(
    "Select Metric",
    ["Transaction Amount", "Transaction Count"]
)

# ---------- MAP METRIC TO COLUMN ----------
if metric == "Transaction Amount":
    value_col = "Transaction_amount"
else:
    value_col = "Transaction_count"

# ---------- QUERY ----------
query = f"""
SELECT 
    State,
    SUM({value_col}) AS Total_Value
FROM aggregated_transaction
GROUP BY State
ORDER BY Total_Value DESC
LIMIT 10;
"""

df = pd.read_sql(query, connection)

# ---------- TABLE ----------
st.subheader("📊 Top 10 States")
st.dataframe(df, use_container_width=True)

# ---------- BAR CHART ----------
st.subheader("📈 Top Performers")

fig = px.bar(
    df,
    x="State",
    y="Total_Value",
    color="State",
    text_auto=True,
    title=f"Top 10 States by {metric}"
)

st.plotly_chart(fig, use_container_width=True)

# ---------- TOP STATE ----------
top = df.iloc[0]

st.success(
    f"🥇 Top State: {top['State']} with {round(top['Total_Value'],2)}"
)