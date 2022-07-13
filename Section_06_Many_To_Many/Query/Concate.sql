SELECT
    title
  , rating
  , first_name || ' ' || last_name AS instructor
FROM
    esmartdata_course
LEFT JOIN
    esmartdata_instructor
ON
    esmartdata_course.instructor_id = esmartdata_instructor.id
ORDER BY
    rating DESC
LIMIT
    10;