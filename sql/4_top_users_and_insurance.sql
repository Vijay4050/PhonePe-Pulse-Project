                        -- 4. TOP Users and Insurance Analysis --
            -- Purpose: Opportunity Analysis of Top User States Vs Top Insurance Penetration --


WITH user_data AS (
    SELECT 
        State,
        SUM(Registered_users) AS Total_Users
    FROM top_user
    GROUP BY State
),

insurance_data AS (
    SELECT 
        State,
        SUM(Transaction_count) AS Total_Insurance_Count
    FROM top_insurance
    GROUP BY State
)

SELECT 
    u.State,
    u.Total_Users,
    i.Total_Insurance_Count
FROM user_data u
JOIN insurance_data i ON u.State = i.State;