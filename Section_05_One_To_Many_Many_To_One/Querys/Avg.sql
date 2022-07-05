SELECT
    course.instructor_id
  , instructor.first_name
  , instructor.last_name
  , ROUND(AVG(course.rating), 2) AS "AVG_Rating"
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