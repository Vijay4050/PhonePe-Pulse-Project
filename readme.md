# 📊 PhonePe Pulse Data Analysis

An end-to-end **Data Analytics project** using the PhonePe Pulse dataset to analyze digital payment transactions, user activity, device usage, insurance, and geographical trends across India.

The project uses **Python, Pandas, MySQL, SQL, Plotly, and Streamlit** for data processing, analysis, visualization, and dashboard development.

---

## 🎯 Project Objectives

- Analyze PhonePe transaction trends across states, years, quarters, and categories.
- Identify dominant mobile device brands and user distribution.
- Analyze user engagement across states.
- Study insurance penetration and trends.
- Compare state, district, and geographical patterns.
- Present analytical findings through an interactive Streamlit dashboard.

---

## 🔄 Project Workflow

```text
PhonePe Pulse JSON Data
        ↓
Python + Pandas
        ↓
Data Extraction & Transformation
        ↓
MySQL Database
        ↓
SQL Analysis
        ↓
Python / Pandas
        ↓
Plotly Visualizations
        ↓
Streamlit Dashboard
```

---

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **MySQL**
- **SQL**
- **MySQL Connector**
- **Plotly**
- **Streamlit**
- **Jupyter Notebook**

---

## 📈 Key Analysis Areas

### 1. Transaction Dynamics
Analysis of transaction volume and transaction value across states, years, quarters, and transaction categories.

### 2. Device Dominance
Analysis of device brands and their user distribution to identify dominant devices across the PhonePe ecosystem.

### 3. Insurance Analysis
Analysis of insurance activity across different years and states, including policy counts and transaction values.

### 4. User Engagement
Analysis of registered users and app opens to compare engagement levels across states.

### 5. Toppers & Geographical Analysis
Identification of top-performing regions and analysis of state/district-level variations in PhonePe activity.

---

## 🗄️ SQL Analysis

The project uses MySQL for structured data storage and SQL-based analysis.

SQL techniques used include:

- Aggregations
- `GROUP BY`
- Filtering
- Joins
- CTEs
- `CASE`
- Window functions
- Ranking
- Derived analytical metrics

The SQL analysis is organized into separate files covering transaction dynamics, device share, insurance, top users/insurance, and user engagement.

---

## 📊 Streamlit Dashboard

A multi-page Streamlit application was developed to interactively explore the analysis.

The application includes pages for:

- Transaction Dynamics
- Device Dominance
- Insurance Analysis
- Toppers
- User Engagement

Interactive visualizations are created using **Plotly**.

---

## 📁 Project Structure

```text
PhonePe-Pulse-Project/
│
├── pages/
│   ├── Device_Dominance.py
│   ├── Insurance_analysis.py
│   ├── Toppers.py
│   ├── Transaction_Dynamics.py
│   └── User_Engagement.py
│
├── Power Point Presentation/
│   └── phonepe_pulse_project.pptx
│
├── pulse/
│   └── data/
│
├── data/
│   ├── aggregated_insurance.csv
│   ├── aggregated_transaction.csv
│   ├── aggregated_user.csv
│   ├── map_insurance_geo.csv
│   ├── map_insurance.csv
│   ├── map_transaction.csv
│   ├── map_user.csv
│   ├── top_insurance.csv
│   ├── top_transaction.csv
│   └── top_user.csv
│
├── notebooks/
│   ├── 1_transaction_dynamics.ipynb
│   ├── 2_device_dominance.ipynb
│   ├── 3_insurance_penetration.ipynb
│   ├── 4_toppers.ipynb
│   ├── 5_user_engagement.ipynb
│   └── insurance_heatmap.html
│
├── sql/
│   ├── 1_transaction_dynamics.sql
│   ├── 2_device_share_analysis.sql
│   ├── 3_insurance_analysis.sql
│   ├── 4_top_users_and_insurance.sql
│   └── 5_user_engagement.sql
│
├── src/
│   ├── 1_create_tables.ipynb
│   ├── 2_data_ingestion.ipynb
│   ├── 3_analysis_queries.ipynb
│   ├── 4_geo_spatial_code.ipynb
│   └── Others.ipynb
│
├── app/
│   └── .gitkeep
│
├── app.py
├── .gitignore
├── LICENSE
└── README.md
```

---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install pandas mysql-connector-python plotly streamlit
```

### 2. Configure MySQL

Create the required database and tables using the SQL scripts/notebooks provided in the repository.

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

---

## 💡 Skills Demonstrated

**Data Analytics:** Data extraction, transformation, cleaning, EDA, aggregation, trend analysis and business insights.

**Python:** Pandas, data processing and analytical programming.

**SQL:** MySQL, joins, CTEs, aggregations, conditional logic and window functions.

**Visualization:** Plotly and interactive charts.

**Application Development:** Streamlit and database-driven analytics.

---

## 👨‍💻 Author

**Vijaykrishna PE**

Data Science & AI/ML

**Python | SQL | Pandas | MySQL | Plotly | Streamlit | Machine Learning**
