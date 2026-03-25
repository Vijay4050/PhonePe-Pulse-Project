import streamlit as st
import pandas as pd

st.title("📊 PhonePe Dashboard")

# Load data
df = pd.read_csv("D:\Viki\Guvi DS\Capstone Projects\PhonePe-Pulse-Project\Data\phonepe_transactions.csv")

# Clean columns
df.columns = df.columns.str.strip().str.lower()

# Convert to crores
df["amount_in_crores"] = df["amount"] / 10000000

# Filters
state = st.selectbox("Select State", ["All"] + list(df["state"].unique()))
year = st.selectbox("Select Year", ["All"] + list(df["year"].unique()))
quarter = st.selectbox("Select Quarter", ["All"] + list(df["quarter"].unique()))

filtered_df = df.copy()

if state != "All":
    filtered_df = filtered_df[filtered_df["state"] == state]

if year != "All":
    filtered_df = filtered_df[filtered_df["year"] == year]

if quarter != "All":
    filtered_df = filtered_df[filtered_df["quarter"] == quarter]

# KPIs
total_amount = filtered_df["amount_in_crores"].sum()
total_transactions = filtered_df["count"].sum()

avg_amount = total_amount / total_transactions if total_transactions != 0 else 0

col1, col2, col3 = st.columns(3)

col1.metric("Total Amount (Crores)", f"{total_amount:.2f}")
col2.metric("Total Transactions", int(total_transactions))
col3.metric("Avg Transaction Value", f"{avg_amount:.2f}")

# Simple chart
scol1, col2 = st.columns(2)

with col1:
    st.subheader("Year-wise Transaction Amount")
    chart_data = filtered_df.groupby("year")["amount_in_crores"].sum()
    st.line_chart(chart_data)

with col2:
    st.subheader("Top 10 States by Amount")
    top_states = df.groupby("state")["amount_in_crores"].sum().sort_values(ascending=False).head(10)
    st.bar_chart(top_states)