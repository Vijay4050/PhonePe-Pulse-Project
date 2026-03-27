import streamlit as st
import pandas as pd
import mysql.connector

# ------------------ PAGE CONFIG ------------------
st.title("📈 Transaction Dynamics")

# ------------------ DB CONNECTION ------------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",   # change if needed
    database="phonepe_db"
)

# ------------------ YEAR FILTER ------------------
year_query = "SELECT DISTINCT Year FROM aggregated_transaction ORDER BY Year"
years = pd.read_sql(year_query, conn)["Year"].tolist()

selected_year = st.selectbox("📅 Select Year", years)

# ------------------ KPI SECTION ------------------
kpi_query = f"""
SELECT 
    SUM(Transaction_amount) AS Total_Amount,
    SUM(Transaction_count) AS Total_Count
FROM aggregated_transaction
WHERE Year = {selected_year}
"""

kpi_df = pd.read_sql(kpi_query, conn)

col1, col2 = st.columns(2)

with col1:
    st.metric("💰 Total Transaction Amount", f"{kpi_df['Total_Amount'][0]:,.0f}")

with col2:
    st.metric("🔢 Total Transaction Count", f"{kpi_df['Total_Count'][0]:,.0f}")

# ------------------ YEARLY TREND ------------------
st.subheader("📊 Transaction Growth Over Years")

trend_query = """
SELECT 
    Year,
    SUM(Transaction_amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY Year
ORDER BY Year
"""

trend_df = pd.read_sql(trend_query, conn)

st.line_chart(trend_df.set_index("Year"))

# ------------------ CATEGORY ANALYSIS ------------------
st.subheader("💳 Category Breakdown")

cat_query = f"""
SELECT 
    Category_Name,
    SUM(Transaction_amount) AS Total_Amount
FROM aggregated_transaction
WHERE Year = {selected_year}
GROUP BY Category_Name
ORDER BY Total_Amount DESC
"""

cat_df = pd.read_sql(cat_query, conn)

st.bar_chart(cat_df.set_index("Category_Name"))

# ------------------ QUARTER ANALYSIS ------------------
st.subheader("📅 Quarterly Trend")

quarter_query = f"""
SELECT 
    Quarter,
    SUM(Transaction_amount) AS Total_Amount
FROM aggregated_transaction
WHERE Year = {selected_year}
GROUP BY Quarter
ORDER BY Quarter
"""

quarter_df = pd.read_sql(quarter_query, conn)

st.line_chart(quarter_df.set_index("Quarter"))

# ------------------ TOP STATES ------------------
st.subheader("🌍 Top 10 States by Transaction Value")

state_query = f"""
SELECT 
    State,
    SUM(Transaction_amount) AS Total_Amount
FROM aggregated_transaction
WHERE Year = {selected_year}
GROUP BY State
ORDER BY Total_Amount DESC
LIMIT 10
"""

state_df = pd.read_sql(state_query, conn)

st.area_chart(state_df.set_index("State"))

# ------------------ INSIGHTS ------------------
st.subheader("🔍 Key Insights")
st.write(f"""
- 📈 Transactions show consistent growth over the years  
- 💳 Peer-to-peer and bill payments dominate usage  
- 📅 Quarterly trends highlight seasonal spikes  
- 🌍 A few states contribute majority of transaction value  

👉 Indicates strong regional concentration and category dominance in digital payments
""")