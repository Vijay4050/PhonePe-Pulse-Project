                                            ---- Transaction Dynamics ----
                        -- Purpose: Analyze transaction dynamics across states and categories --

SELECT 
    State,
    SUM(Transaction_amount) AS Total_Amount,
    ROUND(SUM(Transaction_amount)/1000000000000, 2) AS Total_Amount_LakhCrore
FROM aggregated_transaction
GROUP BY State
ORDER BY Total_Amount DESC;
