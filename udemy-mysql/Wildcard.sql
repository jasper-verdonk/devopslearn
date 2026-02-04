-- LIKE '%'
SELECT * FROM country
WHERE NAME LIKE 'a%';

SELECT * FROM country
WHERE NAME LIKE '%d';

SELECT * FROM country
WHERE NAME LIKE '%ric%';

-- LIKE '_'
SELECT * FROM country
WHERE Name LIKE '____';

SELECT * FROM country
WHERE Name LIKE '_ra%';

SELECT * FROM country
WHERE Name LIKE '_ra_';

-- REGEXP

SELECT * FROM country
WHERE Name REGEXP '^[A-C]';

-- Select all records from the country table, apart from Aruba

SELECT * FROM country
WHERE NOT Name = 'Aruba';

SELECT * FROM country
WHERE Name != 'Aruba';

SELECT * FROM country
WHERE Name <> 'Aruba';

-- Obtain countries that do not start with the letter 'A'

SELECT * FROM country
WHERE Name LIKE 'A%';

SELECT * FROM country
WHERE NOT Name LIKE 'A%';

-- Select all information pertaining to countries that have a surface area less than 10 or more then 10 million

SELECT * FROM country
WHERE SurfaceArea NOT BETWEEN 10 and 10000000;

-- Select all information for countries that reside outside of Europe & Africa

SELECT * FROM country
WHERE Continent NOT IN ('Europe', 'Africa');

-- Select all countries that have a life expectancy populated

SELECT * FROM country
WHERE LifeExpectancy IS NOT NULL


