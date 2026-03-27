import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

st.set_page_config(page_title="Transaction Dynamics", layout="wide")

st.title("Transaction Dynamics: State Ranking (Merchant + Financial)")

# Create connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="phonepe_db"
)

# Your exact query
query = """
WITH combined_category AS (
    SELECT 
        State,
        SUM(Transaction_amount) AS Total_Amount
    FROM aggregated_transaction
    WHERE Category_Name IN ('Merchant Payments', 'Financial Services')
    GROUP BY State
),

state_rank AS (
    SELECT 
        State,
        Total_Amount,
        RANK() OVER (ORDER BY Total_Amount DESC) AS State_Rank
    FROM combined_category
)

SELECT 
    State,
    Total_Amount,
    State_Rank
FROM state_rank
ORDER BY State_Rank;
"""

# Load data
df = pd.read_sql(query, conn)

# Visualization
fig = px.bar(
    df,
    x="Total_Amount",
    y="State",
    orientation="h",
    text="State_Rank",
    title="Transaction Dynamics: State Ranking (Merchant + Financial)"
)

fig.update_traces(textposition='outside')

fig.update_layout(
    xaxis_title="Total Transaction Amount",
    yaxis_title="State"
)

# Display chart
st.plotly_chart(fig, use_container_width=True)