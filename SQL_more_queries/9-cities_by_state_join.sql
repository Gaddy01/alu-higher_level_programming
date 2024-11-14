-- comment
SELECT cities.id, cities.name, states.name
FROM cities
FULL OUTER JOIN states
ON cities.id = cities.state_id
ORDER BY 'cities.id' ASC;
