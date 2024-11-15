-- comment
SELECT tv_shows.title, tv_genres.name
FROM tv_shows

LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id

LEFT JOIN tv_genres
ON tv_show_genres.show_id = tv_genres.id

ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_genres.name ASC
