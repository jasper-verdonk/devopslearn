-- This would be regarded as a comment
# This is also regarded as a comment

-- SELECT * FROM customer; -- This is an end of line comment

/* Anything you now type
across multiple lines 
will not get executed
*/

/*
SELECT = keyword to select columns of data 
*= all columns within table
FROM = "Table Name"
; end the code block
*/
-- SELECT ALL DATA WITHIN THE CUSTOMERS TABLE
SELECT * FROM customer;

-- SELECT ALL DATA WITHIN THE STORES TABLE
SELECT * FROM store;

-- SELECT ALL DATA WITHIN THE FILMS TABLE
SELECT * FROM film;

-- SELECT ALL CUSTOMERS NAMES AND THEIR RESPECTIVE CUSTOMER ID (3 columns only)

SELECT customer_id,
first_name,
last_name
FROM customer;

-- SELECT ALL ACTORS NAMES AND THEIR RESPECTIVE ACTOR ID (3 columns only)

SELECT actor_id, 
first_name,
last_name
FROM actor;

-- SELECT ALL DATA WITHIN CUSTOMERS TABLE (specifying schema)
SELECT * from sakila.customer;

-- What are the different ratings that are assinged to films? 
SELECT DISTINCT rating FROM film;

-- What are the different rental rates that are applied to films? 
SELECT DISTINCT rental_rate FROM film;

-- Are there films within each rating at each price level? 
SELECT DISTINCT rating, rental_rate FROM film;







