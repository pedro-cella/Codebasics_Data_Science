SELECT
	m.movie_id, title, budget, revenue, currency, unit,
    CASE
		WHEN unit = "Thousands" THEN ROUND((revenue-budget)/1000, 1)
        WHEN unit = "Billions" THEN ROUND((revenue-budget)*1000, 1)
        ELSE ROUND((revenue-budget), 1)
    END AS profit_mln
FROM movies m 
JOIN financials f ON m.movie_id = f.movie_id
WHERE industry="Bollywood"
ORDER BY profit_mln DESC;