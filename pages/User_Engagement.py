import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ---------- PAGE ----------
st.set_page_config(layout="wide")
st.title("📊 User Engagement Analysis")

# ---------- DB CONNECTION ----------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="phonepe_db"
)

# ---------- QUERY ----------
query = """
SELECT 
    State,
    SUM(Registered_users) AS Total_Users,
    SUM(App_opens) AS Total_App_Opens
FROM map_user
GROUP BY State
ORDER BY Total_App_Opens DESC;
"""

df = pd.read_sql(query, connection)

# ---------- CREATE ENGAGEMENT METRIC ----------
df["Engagement_Rate"] = df["Total_App_Opens"] / df["Total_Users"]

# ---------- TABLE ----------
st.subheader("📋 User Engagement Data")
st.dataframe(df, use_container_width=True)

# ---------- TOP ENGAGED STATES ----------
st.subheader("🏆 Top States by Engagement")

top_df = df.sort_values(by="Engagement_Rate", ascending=False).head(10)

fig1 = px.bar(
    top_df,
    x="State",
    y="Engagement_Rate",
    color="State",
    text_auto=True,
    title="Top 10 States by Engagement Rate"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------- USERS vs APP OPENS ----------
st.subheader("📈 Users vs App Opens")

fig2 = px.scatter(
    df,
    x="Total_Users",
    y="Total_App_Opens",
    color="State",
    size="Engagement_Rate",
    hover_name="State",
    title="User Base vs Engagement"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------- DISTRIBUTION ----------
st.subheader("📊 Engagement Distribution")

fig3 = px.histogram(
    df,
    x="Engagement_Rate",
    nbins=20,
    title="Engagement Rate Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------- TOP STATE ----------
top_state = top_df.iloc[0]

st.success(
    f"🥇 Highest Engagement: {top_state['State']} ({round(top_state['Engagement_Rate'],2)})"
)