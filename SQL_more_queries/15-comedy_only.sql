--  lists all Comedy shows in the database hbtn_0d_tvshow
SELECT tv_shows.title FROM tv_shows
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
