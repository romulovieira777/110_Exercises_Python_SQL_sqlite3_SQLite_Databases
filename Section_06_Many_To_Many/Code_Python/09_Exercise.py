"""
Exercise No. 09

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'
    - 'esmartdata_learningpath'
    - 'esmartdata_learningpath_courses'

All operations performed so far on this database can be found in the file create_database.sql.

We need to extract the top 10 highest rated courses from this database.

Create a query that will join the tables 'esmartdata_course' and 'esmartdata_instructor'(LEFT JOIN) and extract the top
10 courses(rating column of the 'esmartdata_course' table).

Display the following columns in the output table:
    - title('esmartdata_course' table).
    - rating('esmartdata_course' table).
    - instructor - concatenation of the first_name and last_name columns with a space character
    ('esmartdata_instructor' table).

and sort the records by descending value for the rating column.

Note that the third column is made by concatenating the first_name and last_name columns.

In response, print the result to the console as show below.

Expected Result:
    ('SQL Bootcamp - Bazy danych SQLite - Part IV - Ćwiczenia', 5.0, 'Paweł Krakowiak')
    ('100+ Exercises - Advanced Python Programming', 5.0, 'Paweł Krakowiak')
    ('150+ Exercises - Data Structures in Python - Hands-On', 5.0, 'Paweł Krakowiak')
    ('150+ Ćwiczeń - Programowanie obiektowe w języku C++ - OOP', 5.0, 'takeITeasy Academy')
    ('150+ Exercises - Object Oriented Programming in Python - OOP', 4.92, 'Paweł Krakowiak')
    ('Machine Learning Bootcamp w języku Python cz.II - od A do Z', 4.89, 'Paweł Krakowiak')
    ('250+ Ćwiczeń - Data Science Bootcamp w języku Python', 4.89, 'Paweł Krakowiak')
    ('Artificial Intelligence – Computer Vision w języku Python', 4.87, 'Paweł Krakowiak')
    ('Machine Learning Bootcamp w języku Python cz.III - Ćwiczenia', 4.87, 'Paweł Krakowiak')
    ('Uczenie Maszynowe - Drzewa Decyzyjne i Lasy Losowe - Python', 4.86, 'Paweł Krakowiak')
"""
import sqlite3

conn = sqlite3.connect("../esmartdata.sqlite3")
cur = conn.cursor()

with open('../Query/create_database.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''SELECT title, rating, first_name || ' ' || last_name AS instructor
FROM esmartdata_course
LEFT JOIN esmartdata_instructor
ON esmartdata_course.instructor_id = esmartdata_instructor.id
ORDER BY rating DESC
LIMIT 10;''')

for rows in cur.fetchall():
    print(rows)

conn.commit()
conn.close()
