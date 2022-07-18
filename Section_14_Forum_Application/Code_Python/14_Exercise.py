"""
Exercise No. 14

Using the sqlite3 package, SQLite database called "app.db" was prepared, which contains the following tables:
    - "app_user"
    - "app_thread"
    - "app_comment"
    - "app_group"
    - "app_group_user"

Create a query that will extract names (sorted in ascending order) of all indexes in the database and print them to the
console as shown below.

Expected Result:
    ('index', 'app_comment_thread_id_idx')
    ('index', 'app_comment_user_id_idx')
    ('index', 'app_group_user_group_id_idx')
    ('index', 'app_group_user_group_id_user_idx_uniq')
    ('index', 'app_group_user_user_id_idx')
    ('index', 'app_thread_creator_id_idx')
"""
import sqlite3

conn = sqlite3.connect("app.db")
cur = conn.cursor()

cur.executescript('''DROP INDEX IF EXISTS app_thread_creator_id_idx;
CREATE INDEX app_thread_creator_id_idx ON app_thread (creator_id);

DROP INDEX IF EXISTS app_comment_thread_id_idx;
CREATE INDEX app_comment_thread_id_idx ON app_comment (thread_id);

DROP INDEX IF EXISTS app_comment_user_id_idx;
CREATE INDEX app_comment_user_id_idx ON app_comment (user_id);

DROP INDEX IF EXISTS app_group_user_group_id_idx;
CREATE INDEX app_group_user_group_id_idx ON app_group_user (group_id);

DROP INDEX IF EXISTS app_group_user_user_id_idx;
CREATE INDEX app_group_user_user_id_idx ON app_group_user (user_id)
;

DROP INDEX IF EXISTS app_group_user_group_id_user_idx_uniq;
CREATE UNIQUE INDEX app_group_user_group_id_user_idx_uniq ON app_group_user (group_id, user_id);
''')

print("Index created successfully!")

cur.execute('''SELECT type, name FROM sqlite_master WHERE type='index' ORDER BY name;''')

for row in cur.fetchall():
    print(row)

conn.commit()
conn.close()
