-- lists all genres from hbtn_0d_tvshows and
-- displays the number of shows linked to each
-- lists all shows contained in the database `hbtn_0d_tvshows`
SELECT tv_genres.name, COUNT(tv_show_genres.show_id)
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY tv_show_genres.show_id DESC;