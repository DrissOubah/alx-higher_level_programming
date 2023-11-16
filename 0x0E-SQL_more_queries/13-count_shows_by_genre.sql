-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
SELECT genres.name AS genre,
       COUNT(*) AS number_of_shows
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS shows_genres ON genres.id = shows_genres.genre_id
GROUP BY genres.name
ORDER BY number_of_shows DESC;
