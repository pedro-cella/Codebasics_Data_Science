SELECT 
	m.title,
    GROUP_CONCAT(a.name SEPARATOR " | ") AS actors
FROM movies m
JOIN movie_actor ma ON ma.movie_id = m.movie_id
JOIN actors a ON a.actor_id = ma.actor_id
GROUP BY m.movie_id;

SELECT
	a.name,
    GROUP_CONCAT(m.title SEPARATOR " | ") AS movies,
    COUNT(m.title) AS movie_count
FROM actors a
JOIN movie_actor ma ON ma.actor_id = a.actor_id
JOIN movies m ON m.movie_id = ma.movie_id
GROUP BY a.actor_id
ORDER BY movie_count DESC;