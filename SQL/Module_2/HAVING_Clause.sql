# Print all the years where more than 2 movies were released
SELECT release_year, COUNT(*) AS movies_count
FROM movies
GROUP BY release_year
HAVING movies_count > 2
ORDER BY movies_count DESC;

SELECT release_year, COUNT(*) AS movies_count
FROM movies
WHERE imdb_rating > 6
GROUP BY release_year
HAVING movies_count > 2
ORDER BY movies_count DESC;