SELECT COUNT(*) AS total_rows
FROM analytics.processed_data;

--Example data quality check
SELECT *
FROM analytics.processed_data
LIMIT 20;
