-- Query to find the top 10 directors with the highest number of movies in the list
SELECT Director, COUNT(*) AS num_movies
FROM movies
GROUP BY Director
ORDER BY num_movies DESC
LIMIT 15;