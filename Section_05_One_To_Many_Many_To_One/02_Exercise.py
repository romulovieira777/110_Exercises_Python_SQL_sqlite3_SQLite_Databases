"""
Exercise No. 02

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
'esmartdata_instructor' table.

The table 'esmartdata_instructor' stores basic information about the instructors on the platform. Each instructor can
have multiple courses on the platform. We will store courses in a separate table called 'esmartdata_course'. Before
creating this table, you should consider the type of relationship between these tables. In this case, the answer is
simple, one instructor -> many courses(one-to-many).

Before creating the table, use the appropriate SQL command that will delete the 'esmartdata_course' table if such a
table already exists in the database.

Then, in the specified database, create a table named 'esmartdata_course' with the following columns(column name - data
type):
    - id - integer
    - title - text
    - subtitle - text
    - description - text
    - category - text
    - subcategory - text
    - language - text
    - length - text
    - rating - real
    - referral_link - text
    - instructor_id - integer

Add a NOT NULL constraint to
"""
