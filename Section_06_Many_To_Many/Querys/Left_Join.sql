SELECT
    esmartdata_learningpath.title   AS path_title
  , esmartdata_course.title         AS course_title
  , esmartdata_course.subcategory
FROM
    esmartdata_learningpath
LEFT JOIN
    esmartdata_learningpath_courses
ON
    esmartdata_learningpath.id = esmartdata_learningpath_courses.learningpath_id
LEFT JOIN
    esmartdata_course
ON
    esmartdata_learningpath_courses.course_id = esmartdata_course.id
ORDER BY
    path_title
  , course_title
LIMIT
    10;