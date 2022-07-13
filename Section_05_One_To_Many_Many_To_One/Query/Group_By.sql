SELECT
    instructor_id
  , COUNT(*) AS "num_courses"
FROM
    esmartdata_course
GROUP BY
    instructor_id;