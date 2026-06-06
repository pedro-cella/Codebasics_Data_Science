-- =====================================================
-- SQL REVIEW 2 - MODULE 2.4
----------------------------

-- Topics:
-- SELECT
-- WHERE
-- DISTINCT
-- LIKE
-- %
----

-- Database:
-- codebasics_movies_db
-----------------------

-- Files used:
-- 1. codebasics-movies-db.sql
--    Responsible for creating the database structure
--    and populating the tables.
--------------------------------

-- 2. movies-db-1.xlsx
--    Used as a visual reference to inspect the data
--    contained in the tables.
------------------------------

-- Main Tables:
-- movies
-- actors
-- financials
-- languages
------------

-- Goal:
-- Practice basic SQL data retrieval using a single table,
-- focusing on filtering, searching, selecting columns,
-- identifying unique values and working with text patterns.
------------------------------------------------------------

-- =====================================================



-- =====================================================
-- Exercise 1
--
-- Retrieve all columns from the movies table.
-- =====================================================
SELECT * FROM moviesdb.movies;


-- =====================================================
-- Exercise 2
--
-- Retrieve only:
-- movie_id
-- title
-- industry
-- =====================================================
SELECT movie_id, title, industry FROM moviesdb.movies;


-- =====================================================
-- Exercise 3
--
-- Retrieve all movies that belong to the Bollywood industry.
-- =====================================================
SELECT * FROM moviesdb.movies WHERE industry="Bollywood";


-- =====================================================
-- Exercise 4
--
-- Retrieve all movies with an IMDb rating greater than 8.
-- =====================================================
SELECT * FROM moviesdb.movies WHERE imdb_rating > 8;


-- =====================================================
-- Exercise 5
--
-- Retrieve all unique industries available in the database.
--
-- Bonus:
-- How many different industries exist?
-- =====================================================
SELECT DISTINCT industry FROM moviesdb.movies;
SELECT COUNT(DISTINCT industry) FROM moviesdb.movies;

-- =====================================================
-- Exercise 6
--
-- Retrieve all movies whose title starts with the letter 'A'.
-- =====================================================
SELECT * FROM moviesdb.movies WHERE title LIKE "A%";


-- =====================================================
-- Exercise 7
--
-- Retrieve all movies whose title ends with the word 'Man'.
-- =====================================================
SELECT * FROM moviesdb.movies WHERE title LIKE "%Man";


-- =====================================================
-- Exercise 8
--
-- Retrieve all movies whose title contains the word 'Love'.
-- =====================================================
SELECT * FROM moviesdb.movies WHERE title LIKE "%Love%";


-- =====================================================
-- Exercise 9
--
-- Retrieve all actors whose name starts with the letter 'R'.
--
-- Bonus:
-- Order the results alphabetically.
-- =====================================================
SELECT * FROM moviesdb.actors WHERE name LIKE "R%" ORDER BY name;


-- =====================================================
-- Exercise 10
--
-- Return:
-- title
-- release_year
-- imdb_rating
--
-- Only for movies that:
-- - belong to Hollywood
-- - have IMDb rating greater than 7
-- =====================================================
SELECT
	title,
    release_year,
    imdb_rating
FROM 
	moviesdb.movies
WHERE
	industry="Hollywood"
AND
	imdb_rating > 7;


-- =====================================================
-- CHALLENGE EXERCISE
--
-- Without looking at previous exercises,
-- retrieve all unique movie languages available
-- in the database.
-- =====================================================
SELECT DISTINCT name FROM moviesdb.languages;