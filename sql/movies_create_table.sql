-- Create a table from a public CSV file of IMDB's Top 250 Movies
CREATE OR REPLACE TABLE movies AS 
SELECT * FROM read_csv('https://raw.githubusercontent.com/itiievskyi/IMDB-Top-250/refs/heads/master/imdb_top_250.csv');
