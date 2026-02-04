-- Select the first 10 records from the country table
SELECT * FROM country
LIMIT 10;

-- Select rows 6 to 10 from the country table

SELECT * FROM country
LIMIT 5, 5;

-- What are the top 5 countries with the highest populations? 

SELECT * FROM country
ORDER BY Population DESC
LIMIT 5;

-- What country has the 6th highest life expectancy? 

SELECT * FROM country
ORDER BY LifeExpectancy DESC
LIMIT 5, 1; 

-- BONUS - What about the 8th highest? Clue - some may have the same Life Expectancy! 

SELECT *, 
		DENSE_RANK() OVER (
			ORDER BY LifeExpectancy DESC
           ) `LE_Rank`
FROM country;