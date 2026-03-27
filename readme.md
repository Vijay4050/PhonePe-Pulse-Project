# 📊 PhonePe Pulse Data Analysis Project

## 🔍 Project Overview
This project focuses on analyzing the PhonePe Pulse dataset to extract meaningful insights related to transactions, users, and insurance data across different states and time periods in India.

The objective is to build a complete data pipeline including:
- Data extraction from JSON files
- Data cleaning and transformation
- Database integration using SQL
- Data analysis and visualization

---

## ✅ Work Completed So Far

### 📁 Data Extraction
- Extracted data from PhonePe Pulse GitHub dataset
- Handled multiple categories:
  - Aggregated (Transaction, User, Insurance)
  - Map (Geo-based data)
  - Top (State/District level data)

### 🧹 Data Cleaning & Transformation
- Converted JSON data into structured format using Python (Pandas)
- Handled missing values and inconsistent formats
- Renamed columns for better clarity (e.g., Device_share)

### 🗄️ Database Integration
- Created MySQL database: `phonepe_db`
- Created multiple tables:
  - aggregated_transaction
  - aggregated_user
  - aggregated_insurance
  - map_transaction
  - map_user
  - map_insurance
  - top_transaction
  - top_user
  - top_insurance
- Inserted cleaned data into respective tables

### 📊 Initial Analysis
- Performed SQL queries for:
  - State-wise transaction volume
  - Quarterly trends
  - User growth patterns

### 📈 Visualization (In Progress)
- Started working on visualizations using Python libraries

---

## 🚧 Work in Progress / Pending

- Final integration of all tables for combined insights
- Advanced data analysis and KPI identification
- Visualization dashboard (Streamlit)
- Geo-based visualization improvements
- Final project presentation and documentation

---

## 🛠️ Tools & Technologies Used

- **Programming Language:** Python  
- **Libraries:** Pandas, JSON, Matplotlib (initial stage)  
- **Database:** MySQL  
- **Version Control:** Git & GitHub  
- **Visualization (Planned):** Streamlit / Power BI  

---

## 📁 Project Structure
