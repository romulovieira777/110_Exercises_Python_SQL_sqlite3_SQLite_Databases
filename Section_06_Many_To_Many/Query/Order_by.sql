SELECT
    esmartdata_learningpath.title                       AS path_title
  , COUNT(esmartdata_learningpath_courses.course_id)    AS num_courses
FROM
    esmartdata_learningpath
LEFT JOIN
    esmartdata_learningpath_courses
ON
    esmartdata_learningpath.id = esmartdata_learningpath_courses.learningpath_id
GROUP BY
    esmartdata_learningpath.title
ORDER BY
    num_courses DESC;