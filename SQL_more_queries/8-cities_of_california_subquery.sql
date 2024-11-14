-- comment
SELECT cities.name
FROM cities
JOIN states ON states.id = cities.state.id
WHERE state.name = 'California'
