SELECT rating from film
GROUP BY rating;

SELECT rating, rental_duration
FROM film
GROUP BY rating, rental_duration;

SELECT * FROM film;
SELECT SUM(replacement_cost)
FROM film;
SELECT rating, SUM(replacement_cost)
FROM film
GROUP BY rating;

-- The GROUP BY clause is used to group rows that have the same values

-- The GROUP BY clause is included in SELECT statements

-- The GROUP BY clause is included in the SELECT statement when aggregate calculations are performed you on your data to generate summary tables