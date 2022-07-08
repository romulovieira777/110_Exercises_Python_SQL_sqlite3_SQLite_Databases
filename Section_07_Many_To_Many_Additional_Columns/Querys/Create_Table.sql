DROP TABLE IF EXISTS
    esmartdata_membership;


CREATE TABLE esmartdata_membership (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL
  , created TEXT NOT NULL
  , course_id INTEGER NOT NULL
  , learningpath_id INTEGER NOT NULL
  , FOREIGN KEY (course_id) REFERENCES esmartdata_course(id) ON DELETE CASCADE ON UPDATE CASCADE
  , FOREIGN KEY (learningpath_id) REFERENCES esmartdata_learningpath(id) ON DELETE CASCADE ON UPDATE CASCADE
);