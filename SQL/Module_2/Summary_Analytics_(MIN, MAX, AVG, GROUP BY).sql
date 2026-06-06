SELECT COUNT(*) FROM movies WHERE industry="bollywood";

SELECT MAX(imdb_rating) FROM movies WHERE industry="bollywood";

SELECT MIN(imdb_rating) FROM movies WHERE industry="bollywood";

SELECT AVG(imdb_rating) FROM movies WHERE studio="Marvel Studios";

SELECT ROUND(AVG(imdb_rating), 2) AS avg_rating 
FROM movies WHERE studio="Marvel Studios";

SELECT MIN(imdb_rating) AS min_rating,
	MAX(imdb_rating) AS max_rating,
    ROUND(AVG(imdb_rating), 2) AS avg_rating
FROM movies WHERE studio = "Marvel Studios";

SELECT 
	studio, COUNT(*) AS cnt
FROM movies
GROUP BY studio
ORDER BY cnt DESC;

SELECT 
	industry, 
    COUNT(industry) AS cnt,
    ROUND(AVG(imdb_rating), 1) AS avg_rating
FROM movies
GROUP BY industry;

SELECT 
	studio, 
    COUNT(studio) AS cnt,
    ROUND(AVG(imdb_rating), 1) AS avg_rating
FROM movies
GROUP BY studio
ORDER BY avg_rating DESC;

# DATA ISSUES
#'Universal Pictures'
#'Universal Pictures  '

SELECT 
	studio, 
    COUNT(studio) AS cnt,
    ROUND(AVG(imdb_rating), 1) AS avg_rating
FROM movies
WHERE studio !=""
GROUP BY studio
ORDER BY avg_rating DESC;