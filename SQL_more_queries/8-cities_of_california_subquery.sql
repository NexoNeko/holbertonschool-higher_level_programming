SELECT cities.name FROM cities
WHERE cities.state_id = (
	SELECT 	id
	FROM 	states
	WHERE	name = 'California'
)
ORDERED BY cities.id ASC;