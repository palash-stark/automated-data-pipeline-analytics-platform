-- Example analytical queries for a processed table.
-- Replace database/table/column names with your actual AWS Glue/Athena objects.

SELECT COUNT(*) AS total_rows
FROM analytics.processed_data;

-- Example data quality check
SELECT *
FROM analytics.processed_data
LIMIT 20;
