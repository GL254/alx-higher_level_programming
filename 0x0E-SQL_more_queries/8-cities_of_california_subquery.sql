-- this script lists all
-- cities of California
-- found in database hbtn_0d_usa
SELECT cities.*
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id
