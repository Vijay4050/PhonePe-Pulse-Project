import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ---------- PAGE ----------
st.set_page_config(layout="wide")
st.title("📱 Device Dominance")

# ---------- DB CONNECTION ----------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="phonepe_db"
)

# ---------- QUERY (STRICTLY YOUR LOGIC) ----------
query = """
SELECT 
    Brand,
    SUM(Registered_users) AS Total_Users
FROM aggregated_user
GROUP BY Brand
ORDER BY Total_Users DESC;
"""

df = pd.read_sql(query, connection)

# ---------- TABLE ----------
st.subheader("📊 Device Dominance Table")
st.dataframe(df, use_container_width=True)

# ---------- BAR CHART ----------
st.subheader("📈 Device Dominance by Brand")

fig = px.bar(
    df,
    x="Brand",
    y="Total_Users",
    text_auto=True,
    color="Brand",
    title="Total Registered Users per Brand"
)

st.plotly_chart(fig, use_container_width=True)

# ---------- PIE CHART ----------
st.subheader("🥧 Market Share (Device Dominance)")

fig2 = px.pie(
    df,
    names="Brand",
    values="Total_Users",
    title="Brand-wise User Share"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------- TOP BRAND ----------
top_brand = df.iloc[0]

st.success(
    f"🏆 Dominant Brand: {top_brand['Brand']} with {int(top_brand['Total_Users'])} users"
)