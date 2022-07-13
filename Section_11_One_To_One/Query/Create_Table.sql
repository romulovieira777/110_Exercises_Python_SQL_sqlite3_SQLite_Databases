DROP TABLE IF EXISTS esmartdata_user;

CREATE TABLE IF NOT EXISTS esmartdata_user
(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

DROP TABLE IF EXISTS esmartdata_developer;

CREATE TABLE IF NOT EXISTS esmartdata_developer
(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    level TEXT NOT NULL,
    FOREIGN KEY ("user_id") REFERENCES "esmartdata_user"("id") ON DELETE CASCADE ON UPDATE CASCADE
);