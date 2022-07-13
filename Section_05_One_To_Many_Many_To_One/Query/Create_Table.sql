DROP TABLE IF EXISTS "esmartdata_instructor";

CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
  , first_name TEXT NOT NULL
  , last_name TEXT NOT NULL
  , description TEXT NOT NULL
);


DROP TABLE IF EXISTS "esmartdata_course";
CREATE TABLE IF NOT EXISTS "esmartdata_course" (
    id INTEGER NOT NULL
  , title TEXT NULL
  , subtitle TEXT NOT NULL
  , description TEXT NOT NULL
  , category TEXT NOT NULL
  , subcategory TEXT NOT NULL
  , language TEXT NOT NULL
  , length TEXT NOT NULL
  ,  rating REAL NOT NUL,
  ,  referral_link TEXT NOT NULL
  ,  instructor_id INTEGER NULL
  ,  PRIMARY KEY("id" AUTOINCREMENT)
  ,  FOREIGN KEY("instructor_id") REFERENCES "esmartdata_instructor"(id)
  ,  ON DELETE CASCADE ON UPDATE CASCADE
);