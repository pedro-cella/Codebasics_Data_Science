SELECT 
	*, 
    CONCAT(name, " - ", variant_name) AS full_name,
    (price+variant_price) AS full_price
FROM items
CROSS JOIN variants;

SELECT * FROM moviesdb.movies
CROSS JOIN moviesdb.financials;