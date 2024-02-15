-- lists shows from hbtn_0d_tvsows_rate by rating

SELECT tittle, SUM(tv_show_ratings.rate) 'rating'
FROM tv_shows
LEFT JOIN tv_shows ON tv_show_ratings.show_id = tv_shows.id
GROUP BY tittle
ORDER BY rating DESC;
