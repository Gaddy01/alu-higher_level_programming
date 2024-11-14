-- comment
SELECT cities.id, cities.name, states.name
FROM cities
RIGHT JOIN states
ON cities.id = cities.state_id
ORDER BY 'cities.id' ASC;
