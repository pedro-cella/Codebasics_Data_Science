# 1. Show all the movies with their language names
SELECT * FROM movies;
SELECT * FROM languages;

SELECT 
	title,
    release_year,
    l.name
FROM movies m
LEFT JOIN languages l
ON m.language_id = l.language_id;

# 2. Show all Telugu movie names (assuming you don't know the language id for Telugu)
SELECT
    m.title,
    m.release_year,
    l.name
FROM movies m
LEFT JOIN languages l
    ON m.language_id = l.language_id
WHERE TRIM(l.name) = 'Telugu';

# 3. Show the language and number of movies released in that language
SELECT
	l.name,
    COUNT(m.title) AS language_movies_count
FROM languages l
LEFT JOIN movies m
ON l.language_id = m.language_id
GROUP BY l.name;