-- 1. Device Dominance and User Engagement Analysis --
-- Purpose: Analyze device market share and user engagement across states --

-- 1. Device Market Share Analysis (Top 7 Brands + Others) using the aggregated_user table :

WITH brand_totals AS (
    SELECT 
        Brand,
        SUM(ROUND(Registered_users * Percentage)) AS Total_Users
    FROM aggregated_user
    GROUP BY Brand
),

top_brands AS (
    SELECT Brand
    FROM brand_totals
    ORDER BY Total_Users DESC
    LIMIT 7
)

SELECT 
    Year,
    
    CASE 
        WHEN Brand IN (SELECT Brand FROM top_brands) THEN Brand
        ELSE 'Others'
    END AS Brand_Group,
    
    SUM(ROUND(Registered_users * Percentage)) AS Brand_Users

FROM aggregated_user
GROUP BY Year, Brand_Group;

