DROP INDEX IF EXISTS
    esmartdata_course_instructor_id_idx;

CREATE INDEX IF NOT EXISTS
    esmartdata_course_instructor_id_idx
ON
    esmartdata_course('instructor_id');