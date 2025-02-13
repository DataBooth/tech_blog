-- Create a table from a public CSV file of IMDB's Top 250 Movies
CREATE OR REPLACE TABLE movies AS 
SELECT * FROM read_csv('https://github.com/itiievskyi/IMDB-Top-250/blob/master/imdb_top_250.csv');
