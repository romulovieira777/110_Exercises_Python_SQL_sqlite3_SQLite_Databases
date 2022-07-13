DROP INDEX IF EXISTS
    esmartdata_learningpath_courses_learningpath_id_idx;


CREATE INDEX
    esmartdata_learningpath_courses_learningpath_id_idx
ON
    esmartdata_learningpath_courses(learningpath_id);


DROP INDEX IF EXISTS
    esmartdata_learningpath_courses_course_id_idx;


CREATE INDEX
    esmartdata_learningpath_courses_course_id_idx
ON
    esmartdata_learningpath_courses(course_id);


DROP INDEX IF EXISTS
    esmartdata_learningpath_courses_learningpath_id_course_id_idx;


CREATE UNIQUE INDEX
    esmartdata_learningpath_courses_learningpath_id_course_id_idx
ON
    esmartdata_learningpath_courses(learningpath_id, course_id);