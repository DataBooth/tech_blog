-- Query to find the top 10 directors with the highest number of movies in the list
SELECT director, COUNT(*) AS movie_count
FROM movies
GROUP BY director
ORDER BY movie_count DESC
LIMIT 10;