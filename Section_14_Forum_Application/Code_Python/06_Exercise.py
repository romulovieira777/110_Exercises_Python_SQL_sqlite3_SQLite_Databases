"""
Exercise No. 06

Using the built-in sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Insert the following records into the "app_user" table:
    1, "John", "Lewis", 61, "Tonga", "East Michael", "johnsonjack@esmardata.org"
    2, "Lance", "Boyer", 21, "Seychelles", "Janicetown", "thodges@esmardata.org"
    3, "Michael", "Larson", 22, "Czech Republic", "West Melissa", "kmalone@esmardata.org"

Commit the changes and in response create a query that will display all the records from the "app_user" table. Print the
result to the console as shown below.

Expected Result:
    (1, 'John', 'Lewis', 61, 'Tonga', 'East Michael', 'johnsonjack@esmardata.org')
    (2, 'Lance', 'Boyer', 21, 'Seychelles', 'Janicetown', 'thodges@esmardata.org')
    (3, 'Michael', 'Larson', 22, 'Czech Republic', 'West Melissa', 'kmalone@esmardata.org')
"""
import sqlite3
conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS app_user;
CREATE TABLE IF NOT EXISTS app_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    city TEXT NOT NULL,
    email TEXT NOT NULL
);

DROP TABLE IF EXISTS app_thread;
CREATE TABLE IF NOT EXISTS app_thread (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    title TEXT NOT NULL,
    creator_id INTEGER NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES app_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS app_comment;
CREATE TABLE IF NOT EXISTS app_comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    body TEXT NOT NULL,
    created TEXT NOT NULL,
    thread_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (thread_id) REFERENCES app_thread(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS app_group;
CREATE TABLE IF NOT EXISTS app_group (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name TEXT NOT NULL
);

DROP TABLE IF EXISTS app_group_user;
CREATE TABLE IF NOT EXISTS app_group_user (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    group_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (group_id) REFERENCES app_group(id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES app_user(id) ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

cur.executescript('''INSERT INTO app_user (id, first_name, last_name, age, country, city, email)
VALUES (1, "John", "Lewis", 61, "Tonga", "East Michael", "johnsonjack@esmartdata.org");
 
INSERT INTO app_user (id, first_name, last_name, age, country, city, email)
VALUES (2, "Lance", "Boyer", 21, "Seychelles", "Janicetown", "thodges@esmartdata.org");
 
INSERT INTO app_user (id, first_name, last_name, age, country, city, email)
VALUES (3, "Michael", "Larson", 22, "Czech Republic", "West Melissa", "kmalone@esmartdata.org" );''')

print("Data entered successfully!")

cur.execute('''SELECT * FROM app_user;''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
