-- ===============================
-- Database: PhonePe Pulse Analysis
-- Purpose: Transaction and user analytics queries
-- Created: 2024

-- PHONEPE DATA ANALYSIS QUERIES
-- ===============================

-- 1. Top 10 states by transaction amount
SELECT State, SUM(Amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY State
ORDER BY Total_Amount DESC
LIMIT 10;

-- 2. Year-wise transaction trend
SELECT Year, SUM(Amount) AS Total_Amount
FROM aggregated_transaction
GROUP BY Year
ORDER BY Year;

-- 3. Top 10 states by transaction count
SELECT State, SUM(Count) AS Total_Count
FROM aggregated_transaction
GROUP BY State
ORDER BY Total_Count DESC
LIMIT 10;