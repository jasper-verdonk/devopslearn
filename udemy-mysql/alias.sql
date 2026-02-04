-- Change the column headers so that the column names are capitalised acronyms
SELECT  title AS T, 
		rental_rate AS RR,
		rental_duration AS RD,
		replacement_cost AS RC
FROM film;

-- Change the column headers to remove the underscore in the column name
SELECT title AS Title, 
		rental_duration AS `Rental Duration`, 
		rental_rate AS `Rental Rate`, 
		replacement_cost AS `Replacement Cost`
FROM film;



-- Using the above query, change the table name to be the letter 'f'

FROM film AS `f`; 
