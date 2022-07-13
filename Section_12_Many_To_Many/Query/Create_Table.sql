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
    FOREIGN KEY (user_id) REFERENCES esmartdata_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS esmartdata_tech;

CREATE TABLE IF NOT EXISTS esmartdata_tech (
    id integer NOT NULL,
    name text NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS esmartdata_developer_techs;

CREATE TABLE IF NOT EXISTS esmartdata_developer_techs (
    id integer NOT NULL,
    developer_id integer NOT NULL,
    tech_id integer NOT NULL,
    PRIMARY KEY(id AUTOINCREMENT),
    FOREIGN KEY(developer_id) REFERENCES esmartdata_developer(user_id)
    ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY(tech_id) REFERENCES esmartdata_tech(id)
    ON DELETE CASCADE ON UPDATE CASCADE;
