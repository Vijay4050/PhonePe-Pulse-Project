--                                  -- 5. USER ENGAGEMENT ANALYSIS --
            -- Purpose: Analyze user engagement by comparing app opens to registered users across states -- 

WITH user_data AS (
    -- 🔷 Top users from top_user table
    SELECT 
        State,
        SUM(Registered_users) AS Total_Users
    FROM top_user
    GROUP BY State
),

engagement_data AS (
    -- 🔷 Engagement from aggregated_user table
    SELECT 
        State,
        SUM(App_opens) AS Total_App_Opens,
        SUM(Registered_users) AS Users_For_Engagement,
        
        ROUND(
            SUM(App_opens) * 1.0 / NULLIF(SUM(Registered_users), 0),
        4) AS Engagement_Per_User
    FROM aggregated_user
    GROUP BY State
),

combined AS (
    SELECT 
        u.State,
        u.Total_Users,
        e.Total_App_Opens,
        e.Engagement_Per_User
    FROM user_data u
    JOIN engagement_data e 
        ON u.State = e.State
),

avg_engagement AS (
    SELECT AVG(Engagement_Per_User) AS avg_eng
    FROM combined
),

ranked AS (
    SELECT 
        c.*,
        a.avg_eng,
        RANK() OVER (ORDER BY Total_Users DESC) AS user_rank
    FROM combined c
    CROSS JOIN avg_engagement a
)

SELECT 
    State,
    Total_Users,
    Total_App_Opens,
    Engagement_Per_User,

    CASE 
        WHEN Engagement_Per_User >= avg_eng * 1.2 THEN 'High Engagement'
        WHEN Engagement_Per_User >= avg_eng * 0.8 THEN 'Medium Engagement'
        ELSE 'Low Engagement'
    END AS Engagement_Status

FROM ranked
WHERE user_rank <= 10
ORDER BY Total_Users DESC;