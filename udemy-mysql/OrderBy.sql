-- SELECT Name, IndepYear, Population, Life Expectancy from the country table within the world schema

SELECT Name,
	IndepYear, 
	Population,
	LifeExpectancy 
FROM country;

-- Order the result by Name from Z to A

SELECT Name,
	IndepYear, 
	Population,
	LifeExpectancy 
FROM country
ORDER BY Name ASC;

-- Order the result by Population from highest to lowest

SELECT Name,
	IndepYear, 
	Population,
	LifeExpectancy 
FROM country
ORDER BY Population ASC;


-- Order the result by LifeExpectancy (using LE alias) from highest to lowest

SELECT Name,
	IndepYear, 
	Population,
	LifeExpectancy AS LE
FROM country
ORDER BY LE DESC;

-- Order the result by IndepYear (most recent first) and then Population from lowest to highest

SELECT Name,
	IndepYear, 
	Population,
	LifeExpectancy
FROM country
ORDER BY IndepYear DESC, Population ASC; 


-- Recreate the query above by using column number references

SELECT Name,
	IndepYear, 
	Population,
	LifeExpectancy
FROM country
ORDER BY 2 DESC, 3 ASC;
