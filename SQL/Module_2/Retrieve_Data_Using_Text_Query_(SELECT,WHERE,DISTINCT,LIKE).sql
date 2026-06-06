SELECT * FROM movies WHERE industry="Bollywood";
SELECT DISTINCT industry FROM movies;
SELECT * FROM movies WHERE title LIKE "THOR";
SELECT * FROM movies WHERE title LIKE "%America%";
SELECT * FROM moviesdb.movies;

## Takeaways
/*
- SELECT, FROM and WHERE are the basic SQL functions
- '*' means all columns. 
Using '*' after the SELECT query will select all columns of a database
- With the help of the USE function, 
you can indicate the query to use a particular database,
especially when there are multiple databases
- The COUNT function will provide the numerical count of rows
- The DISTINCT function will help you see the unique values present in a given column
- '%' is a wild card search
- USe LIKE function and '%' to filter the rows based on a text value
*/