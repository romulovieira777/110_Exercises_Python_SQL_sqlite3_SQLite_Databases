SELECT
    *
  , email(first_name, last_name) AS email
FROM
    instructor;


SELECT
    *
  , age(birth_date) AS age
FROM
    instructor;
