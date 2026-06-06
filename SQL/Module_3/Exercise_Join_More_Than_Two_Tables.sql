/*
1. Generate a report of all Hindi movies sorted by their revenue amount in millions.
Print movie name, revenue, currency, and unit
*/

SELECT
	m.title,
    f.revenue,
    f.currency,
    f.unit,
    CASE
		WHEN f.unit = "Thousands" THEN ROUND(f.revenue/1000, 1)
        WHEN f.unit = "Billions" THEN ROUND(f.revenue*1000, 1)
        ELSE ROUND(f.revenue, 1)
    END AS revenue_millions
FROM movies m
JOIN financials f 
	ON m.movie_id = f.movie_id
JOIN languages l 
	ON m.language_id = l.language_id
WHERE l.name = "Hindi"
ORDER BY revenue_millions DESC;