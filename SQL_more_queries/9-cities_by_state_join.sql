-- comment
SELECT DISTINCT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.id = cities.state_id
ORDER BY 'cities.id' ASC;
