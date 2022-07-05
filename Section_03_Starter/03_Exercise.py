"""
Exercise No. 03

Using the built-in sqlite3 package and the appropriate SQL command, print the version of SQLite to the console.

Expected Result:
    - 3.35.5
"""
import sqlite3


print(sqlite3.sqlite_version)


# Second option

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

cur.execute('''SELECT sqlite_version()''')
version = cur.fetchone()[0]
print(version)

conn.close()
