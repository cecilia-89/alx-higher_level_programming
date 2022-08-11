-- lists all shows contained in hbtn_0d_tvshows
SELECT tv_shows.title, tv_shows_genre.genre_id
FROM tv_show_genres
JOIN tv_shows
ON show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;