SELECT
    esmartdata_course.category
  , esmartdata_course.subcategory
  , esmartdata_instructor.first_name || ' ' || esmartdata_instructor.last_name  AS instructor
  , COUNT(esmartdata_course.id)                                                 AS num_courses
FROM
    esmartdata_course
LEFT JOIN
    esmartdata_instructor
ON
    esmartdata_course.instructor_id = esmartdata_instructor.id
GROUP BY
   esmartdata_course.category
 , esmartdata_course.subcategory
 , instructor
ORDER BY
    num_courses DESC;