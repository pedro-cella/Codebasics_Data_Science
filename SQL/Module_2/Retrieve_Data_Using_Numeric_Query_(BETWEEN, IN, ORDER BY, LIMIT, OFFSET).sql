SELECT * FROM movies WHERE imdb_rating >= 9;

SELECT * FROM movies WHERE imdb_rating <= 5;

SELECT * FROM movies WHERE imdb_rating >= 6 AND imdb_rating <= 8;

SELECT * FROM movies WHERE imdb_rating BETWEEN 6 AND 8;

SELECT * 
FROM movies 
WHERE release_year=2022 OR release_year=2019 OR release_year=2018;

SELECT * 
FROM movies 
WHERE release_year IN (2022, 2019, 2018);

SELECT * 
FROM movies 
WHERE studio IN ("Marvel Studios", "Zee Studios");

SELECT *
FROM movies WHERE imdb_rating is NULL;

SELECT *
FROM movies WHERE imdb_rating is NOT NULL;

SELECT *
FROM movies WHERE industry="Bollywood"
ORDER BY imdb_rating DESC;

SELECT *
FROM movies WHERE industry="Bollywood"
ORDER BY imdb_rating DESC LIMIT 5;


SELECT *
FROM movies WHERE industry="Bollywood"
ORDER BY imdb_rating DESC LIMIT 5 OFFSET 4;