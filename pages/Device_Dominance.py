import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ---------- PAGE CONFIG ----------
st.set_page_config(layout="wide")

st.title("📱 Device Share Analysis")

# ---------- DB CONNECTION ----------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="phonepe_db"
)

# ---------- YOUR SQL QUERY ----------
query = """
SELECT 
    Brand,
    SUM(Registered_users) AS Total_Users,
    AVG(App_opens) AS Avg_App_Opens,
    SUM(Registered_users * App_opens) AS Device_share
FROM aggregated_user
GROUP BY Brand
ORDER BY Device_share DESC;
"""

df = pd.read_sql(query, connection)

# ---------- DISPLAY DATA ----------
st.subheader("📊 Device Share Table")
st.dataframe(df, use_container_width=True)

# ---------- 1. DEVICE SHARE BAR CHART ----------
st.subheader("📈 Device Share Dominance")

fig1 = px.bar(
    df,
    x="Brand",
    y="Device_share",
    text_auto=True,
    color="Brand",
    title="Device Share by Brand"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------- 2. PIE CHART (MARKET SHARE) ----------
st.subheader("🥧 Market Share Distribution")

fig2 = px.pie(
    df,
    names="Brand",
    values="Device_share",
    title="Device Share Contribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------- 3. USERS vs APP OPENS ----------
st.subheader("🔥 Engagement Strength")

fig3 = px.scatter(
    df,
    x="Avg_App_Opens",
    y="Total_Users",
    size="Device_share",
    color="Brand",
    hover_name="Brand",
    title="Users vs App Opens (Bubble = Device Share)"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------- TOP BRAND ----------
top_brand = df.iloc[0]

st.success(
    f"🏆 Top Brand: {top_brand['Brand']} | Device Share: {round(top_brand['Device_share'],2)}"
)