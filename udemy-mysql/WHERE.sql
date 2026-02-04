-- Obtain all information pertaining to customers that shop in Store_ID 1

SELECT * 
FROM customer
WHERE store_id = 1;

-- What store_id does John shop at? 

SELECT * FROM customer
WHERE first_name = 'JOHN';

-- How many actors are called Nick? 

SELECT * FROM actor 
WHERE first_name = 'NICK'