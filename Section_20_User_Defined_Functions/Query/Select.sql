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


SELECT
    *
  , RANDOM_GROUP()
FROM
    instructor;


SELECT
    *
  , RANDOM_GROUP()
  , RANDOM_GROUP(5)
FROM
    instructor;


SELECT
    CSV(id
      , first_name
      , last_name)
FROM
    instructor;
