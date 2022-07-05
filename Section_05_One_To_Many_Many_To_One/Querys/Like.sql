SELECT
    instructor.first_name
  , instructor.last_name
  , course.title
  , course.subcategory
FROM
    esmartdata_course course
LEFT JOIN
    esmartdata_instructor instructor
ON
    course.instructor_id = instructor.id
WHERE
    course.title LIKE '%Exer%';