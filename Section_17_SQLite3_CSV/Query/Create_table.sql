DROP TABLE IF EXISTS app_user;

CREATE TABLE app_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT
  , first_name TEXT NOT NULL
  , last_name TEXT NOT NULL
  , age INTEGER NOT NULL
  , country TEXT NOT NULL
  , city TEXT NOT NULL
  , email TEXT NOT NULL
);
