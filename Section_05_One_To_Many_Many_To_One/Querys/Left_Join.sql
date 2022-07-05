SELECT
    course.instructor_id
  , instructor.first_name
  , instructor.last_name
  , COUNT(course.subcategory) AS courses
FROM
    esmartdata_course course
LEFT JOIN
    esmartdata_instructor instructor
ON
    course.instructor_id = instructor.id
GROUP BY
    course.instructor_id
  , instructor.first_name
  , instructor.last_name;