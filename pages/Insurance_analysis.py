import streamlit as st
import pandas as pd
import mysql.connector
import plotly.express as px

# ---------- PAGE ----------
st.set_page_config(layout="wide")
st.title("🛡️ Insurance Penetration Analysis")

# ---------- DB CONNECTION ----------
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="phonepe_db"
)

# ---------- QUERY (CORE NOTEBOOK LOGIC) ----------
query = """
SELECT 
    State,
    Year,
    SUM(Insurance_count) AS Total_Policies,
    SUM(Insurance_amount) AS Total_Amount
FROM aggregated_insurance
GROUP BY State, Year
ORDER BY Year, Total_Amount DESC;
"""

df = pd.read_sql(query, connection)

# ---------- TABLE ----------
st.subheader("📊 Insurance Data")
st.dataframe(df, use_container_width=True)

# ---------- FILTER ----------
states = st.multiselect(
    "Select State",
    df['State'].unique(),
    default=df['State'].unique()[:5]
)

filtered_df = df[df['State'].isin(states)]

# ---------- 1. PENETRATION TREND ----------
st.subheader("📈 Insurance Penetration Trend")

trend_df = filtered_df.groupby("Year", as_index=False)["Total_Amount"].sum()

fig1 = px.line(
    trend_df,
    x="Year",
    y="Total_Amount",
    markers=True,
    title="Insurance Growth Over Years"
)

st.plotly_chart(fig1, use_container_width=True)

# ---------- 2. STATE-WISE COMPARISON ----------
st.subheader("📊 State-wise Insurance Penetration")

state_df = filtered_df.groupby("State", as_index=False)["Total_Amount"].sum()

fig2 = px.bar(
    state_df,
    x="State",
    y="Total_Amount",
    color="State",
    text_auto=True,
    title="Insurance Adoption by State"
)

st.plotly_chart(fig2, use_container_width=True)

# ---------- 3. POLICY COUNT ANALYSIS ----------
st.subheader("📦 Policy Count Distribution")

fig3 = px.scatter(
    filtered_df,
    x="Total_Policies",
    y="Total_Amount",
    color="State",
    size="Total_Policies",
    hover_name="State",
    title="Policies vs Amount"
)

st.plotly_chart(fig3, use_container_width=True)

# ---------- TOP STATE ----------
top_state = state_df.sort_values(by="Total_Amount", ascending=False).iloc[0]

st.success(
    f"🏆 Top State: {top_state['State']} with ₹{round(top_state['Total_Amount'],2)}"
)