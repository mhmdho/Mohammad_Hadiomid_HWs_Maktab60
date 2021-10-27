''' Mohammad Hadiomid '''
''' Homework 13 - Question 1 '''


-- part 1
\dt


-- part 2
SELECT 
    first_name 
FROM
    customer 
WHERE
    first_name LIKE 'R%' OR first_name LIKE '%n';


-- part 3
SELECT
    count(customer_id) 
FROM
    customer 
WHERE
    customer_id > 20;


-- part 4
SELECT
    *
FROM
    actor
WHERE
    first_name LIKE 'Nick' OR first_name LIKE 'Ed' OR first_name LIKE 'Bette';


-- part 5
SELECT
    DISTINCT(first_name)
FROM
    actor
ORDER BY first_name;


-- part 6
SELECT
    AVG(rental_duration) AS avg,
    MAX(rental_duration) AS max,
    MIN(rental_duration) AS min,
    SUM(rental_duration) AS sum
FROM
    film;


-- part 7
SELECT
    first_name,
    last_name,
    amount,
    return_date
FROM
    customer
INNER JOIN rental
    ON customer.customer_id = rental.customer_id
INNER JOIN payment
    ON payment.customer_id = customer.customer_id;


-- part 8
SELECT
    CONCATE(first_name , ‘ ‘, last_name),
    address,
    city,
    city.city_id,
    country
FROM
    customer
INNER JOIN address
    ON customer.address_id = address.address_id
INNER JOIN city
    ON city.city_id = address.city_id
INNER JOIN country
    ON country.country_id = city.country_id
ORDER BY country;
