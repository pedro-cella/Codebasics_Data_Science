# 1. Print profit % for all the movies
SELECT * FROM financials;

# What is profit ? revenue - budget
SELECT 
	*,
    revenue - budget AS profit
FROM financials;

# How to calculate Profit % ? (Profit / Revenue) * 100 
SELECT
	movie_id,
    budget,
    revenue,
    (revenue - budget) AS profit,
    ROUND(
		((revenue - budget)/budget) * 100
    , 1) AS profit_pct
FROM financials;

# With JOIN
SELECT
	title,
    budget,
    revenue,
    (revenue - budget) AS profit,
    ROUND(
		((revenue - budget)/budget) * 100
    , 1) AS profit_pct
FROM financials
LEFT JOIN movies
ON financials.movie_id = movies.movie_id;
