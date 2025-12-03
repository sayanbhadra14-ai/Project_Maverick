CREATE DATABASE merger_project;
USE merger_project;
CREATE TABLE target_companies (
    Company_ID INT PRIMARY KEY,
    Company_Name VARCHAR(100),
    Ticker VARCHAR(10),
    Sector VARCHAR(50),
    Business_Segment VARCHAR(100),
    Revenue_Current DECIMAL(15,2),
    Revenue_Growth_Pct DECIMAL(10,4),
    EBITDA_Margin_Pct DECIMAL(10,4),
    EBITDA DECIMAL(15,2),
    Net_Income DECIMAL(15,2),
    Total_Debt DECIMAL(15,2),
    Market_Cap DECIMAL(15,2)
);
SELECT * FROM target_companies;
SELECT COUNT(*) AS Total_Companies FROM target_companies;
SELECT * FROM target_companies WHERE Ticker = 'PVT' LIMIT 5;
SELECT Business_Segment, COUNT(*) FROM target_companies GROUP BY Business_Segment;
SELECT * FROM target_companies 
WHERE Ticker = 'PVT' 
  AND Business_Segment != 'Legacy ERP';
  
  SELECT 
    Company_Name, 
    Business_Segment, 
    Revenue_Growth_Pct, 
    EBITDA_Margin_Pct,
    (Revenue_Growth_Pct + EBITDA_Margin_Pct) * 100 AS Rule_of_40_Score
FROM target_companies
WHERE Ticker = 'PVT'
  AND Business_Segment != 'Legacy ERP'
ORDER BY Rule_of_40_Score DESC;

USE merger_project;
SELECT 
    Company_ID,
    Company_Name,
    Business_Segment,
    Revenue_Current,
    EBITDA,
    Total_Debt,
    (Total_Debt / EBITDA) AS Leverage_Ratio,
    (Revenue_Growth_Pct + EBITDA_Margin_Pct) * 100 AS Rule_of_40_Score
FROM target_companies
WHERE Ticker = 'PVT'
  AND Business_Segment != 'Legacy ERP'
  AND (Revenue_Growth_Pct + EBITDA_Margin_Pct) >= 0.40 -- The Rule of 40 Threshold
  AND (Total_Debt / EBITDA) < 3.0 -- The Safety Threshold
ORDER BY Rule_of_40_Score DESC
LIMIT 5;