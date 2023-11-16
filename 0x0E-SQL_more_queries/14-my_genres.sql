-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT genres.name
FROM tv_genres AS genres
INNER JOIN tv_show_genres AS show_genres ON genres.id = show_genres.genre_id
INNER JOIN tv_shows AS shows ON shows.id = show_genres.show_id
WHERE shows.title = "Dexter"
ORDER BY genres.name;
