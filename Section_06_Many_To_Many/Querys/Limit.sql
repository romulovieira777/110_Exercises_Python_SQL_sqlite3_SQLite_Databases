SELECT
    esmartdata_learningpath.title                                               AS path_title
  , esmartdata_course.title                                                     AS course_title
  , esmartdata_instructor.first_name || ' ' || esmartdata_instructor.last_name  AS instructor
FROM
    esmartdata_learningpath_courses
LEFT JOIN
    esmartdata_learningpath
ON
    esmartdata_learningpath_courses.learningpath_id = esmartdata_learningpath.id
LEFT JOIN
    esmartdata_course
ON
    esmartdata_learningpath_courses.course_id = esmartdata_course.id
LEFT JOIN
    esmartdata_instructor
ON
    esmartdata_course.instructor_id = esmartdata_instructor.id
LIMIT
    10;