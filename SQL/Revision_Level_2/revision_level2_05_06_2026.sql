-- =====================================================
-- SQL REVIEW 2 - MODULE 2.6
----------------------------

-- Topics:
-- BETWEEN
-- IN
-- ORDER BY
-- LIMIT
-- OFFSET
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
-- Practice SQL numeric filtering, list filtering,
-- ordering results, limiting returned rows,
-- and skipping records using OFFSET.
------------------------------------------------------------

-- =====================================================


-- =====================================================
-- Exercise 1
--
-- Retrieve all movies released between 2015 and 2022.
-- =====================================================
SELECT *
FROM movies
WHERE release_year BETWEEN 2015 AND 2022;

-- =====================================================
-- Exercise 2
--
-- Retrieve all movies with IMDb rating between 7 and 9.
-- =====================================================
SELECT *
FROM movies
WHERE imdb_rating
BETWEEN 7
AND 9;

-- =====================================================
-- Exercise 3
--
-- Retrieve all movies released in either 2018, 2019, or 2022.
-- =====================================================
SELECT *
FROM movies
WHERE release_year IN (2018, 2019, 2022);


-- =====================================================
-- Exercise 4
--
-- Retrieve all movies produced by either Marvel Studios
-- or Hombale Films.
-- =====================================================
SELECT *
FROM movies
WHERE studio IN ("Marvel Studios", "Hombale Films");

-- =====================================================
-- Exercise 5
--
-- Retrieve all movies ordered by release year,
-- from newest to oldest.
-- =====================================================
SELECT *
FROM movies
ORDER BY release_year DESC;

-- =====================================================
-- Exercise 6
--
-- Retrieve the top 5 movies with the highest IMDb rating.
-- =====================================================
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 5;

-- =====================================================
-- Exercise 7
--
-- Retrieve the 5 movies with the lowest IMDb rating.
-- =====================================================
SELECT *
FROM movies
WHERE imdb_rating IS NOT NULL
ORDER BY imdb_rating
LIMIT 5;

-- =====================================================
-- Exercise 8
--
-- Retrieve movies ordered by IMDb rating from highest to lowest,
-- but skip the first 5 results.
-- =====================================================
SELECT *
FROM movies
ORDER BY imdb_rating DESC
LIMIT 5
OFFSET 5;

-- =====================================================
-- Exercise 9
--
-- Retrieve 5 movies after skipping the first 10 movies,
-- ordered by release year from newest to oldest.
-- =====================================================
SELECT *
FROM movies
ORDER BY release_year DESC
LIMIT 5
OFFSET 10;

-- =====================================================
-- Exercise 10
--
-- Retrieve all movies that:
-- - were released between 2010 and 2022
-- - belong to either Bollywood or Hollywood
-- - are ordered by IMDb rating from highest to lowest
-- - return only the first 10 results
-- =====================================================
SELECT *
FROM movies
WHERE release_year BETWEEN 2010 AND 2022
AND industry in ("Bollywood", "Hollywood")
ORDER BY imdb_rating DESC
LIMIT 10;