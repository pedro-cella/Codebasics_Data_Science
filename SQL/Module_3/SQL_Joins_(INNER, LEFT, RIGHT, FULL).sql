SELECT 
	m.movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
INNER JOIN financials f
ON m.movie_id = f.movie_id;

# JOIN = INNER JOIN

SELECT 
	m.movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
LEFT JOIN financials f
ON m.movie_id = f.movie_id;

SELECT 
	f.movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id = f.movie_id;

SELECT 
	m.movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
LEFT JOIN financials f
ON m.movie_id = f.movie_id

UNION

SELECT 
	f.movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id = f.movie_id;

SELECT 
	movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
RIGHT JOIN financials f
USING (movie_id);

SELECT 
	m.movie_id,
    title,
    budget,
    revenue,
    currency,
    unit
FROM movies m
RIGHT JOIN financials f
ON m.movie_id = f.movie_id AND m.col2=f.col2;