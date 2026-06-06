SELECT YEAR(CURDATE());
SELECT *, YEAR(CURDATE())-birth_year AS age FROM actors;

SELECT *, (revenue - budget) AS profit FROM financials;

SELECT 
	*, 
    IF (currency='USD', revenue*77, revenue) AS revenue_inr 
FROM financials;

SELECT DISTINCT unit FROM financials;

SELECT 
	*,
    CASE
		WHEN unit="Thousands" THEN revenue/1000
        WHEN unit="Billions" THEN revenue*1000
        ELSE revenue 
    END AS revenue_mln
FROM financials

