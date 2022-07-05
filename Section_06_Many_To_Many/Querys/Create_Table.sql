DROP TABLE IF EXISTS
    esmartdata_learningpath;


CREATE TABLE IF NOT EXISTS esmartdata_learningpath (
    id INTEGER NOT NULL
  , title TEXT NOT NULL
  , subtitle TEXT NOT NULL
  , url TEXT NOT NULL
  , PRIMARY KEY("id" AUTOINCREMENT));


DROP TABLE IF EXISTS
    esmartdata_learningpath_courses;


CREATE TABLE IF NOT EXISTS esmartdata_learningpath_courses (
    id INTEGER NOT NULL
  , learningpath_id INTEGER NOT NULL
  , course_id INTEGER NOT NULL
  , PRIMARY KEY("id" AUTOINCREMENT)
  , FOREIGN KEY("learningpath_id") REFERENCES "esmartdata_learningpath"(id) ON DELETE CASCADE ON UPDATE CASCADE
  , FOREIGN KEY("course_id") REFERENCES "esmartdata_course"(id) ON DELETE CASCADE ON UPDATE CASCADE
);