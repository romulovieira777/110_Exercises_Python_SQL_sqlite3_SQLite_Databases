"""
Exercise No. 07

Using the built-in sqlite3 package, SQLite database called 'esmartdata_sqlite3' was prepared, which contains the
following tables:
    - 'esmartdata_instructor'
    - 'esmartdata_course'

Create a query that extracts all courses names from the 'esmartdata_course' table(title column) and print it to the
console as shown below.

Expected Result:
Wprowadzenie do data science w języku Python - Pandas
Deep Learning w języku Python - Konwolucyjne Sieci Neuronowe
Uczenie Maszynowe - Drzewa Decyzyjne i Lasy Losowe - Python
Programowanie w języku Python - od A do Z
Twórz nowoczesne aplikacje webowe w Pythonie - Dash, Plotly
Interaktywne wizualizacje danych w języku Python - Plotly
Big Data, Hadoop oraz MapReduce w języku Python
Wprowadzenie do sieci neuronowych - Tensorflow 2.0 + Keras
Big Data: Analiza danych przy użyciu SQL oraz BigQuery
Artificial Intelligence – Computer Vision w języku Python
Data Science Bootcamp w języku Python - od A do Z
Machine Learning Bootcamp w języku Python cz.I - od A do Z
Machine Learning Bootcamp w języku Python cz.II - od A do Z
200+ Ćwiczeń - Programowanie w języku Python - od A do Z
250+ Ćwiczeń - Data Science Bootcamp w języku Python
200+ Exercises - Programming in Python - from A to Z
250+ Exercises - Data Science Bootcamp in Python
100+ Exercises - Python Programming - Data Science - NumPy
130+ Exercises - Python Programming - Data Science - Pandas
100+ Exercises - Python - Data Science - scikit-learn
Machine Learning Bootcamp w języku Python cz.III - Ćwiczenia
210+ Ćwiczeń - Python - Moduły wbudowane - od A do Z
210+ Exercises - Python Standard Libraries - from A to Z
Programowanie obiektowe w języku Python - OOP - od A do Z
150+ Ćwiczeń - Programowanie obiektowe w języku Python - OOP
150+ Exercises - Object Oriented Programming in Python - OOP
120+ Ćwiczeń w języku Python - Data Science - NumPy
130+ Ćwiczeń w języku Python - Data Science - Pandas
Testy jednostkowe w języku Python - framework unittest
100+ Ćwiczeń - Testy jednostkowe w języku Python - unittest
100+ Exercises - Unit tests in Python - unittest framework
SQL Bootcamp - Bazy danych SQLite - Part I
SQL Bootcamp - Bazy danych SQLite - Part II
SQL Bootcamp - Bazy danych SQLite - Part III - Ćwiczenia
SQL Bootcamp - Bazy danych SQLite - Part IV - Ćwiczenia
SQL Bootcamp - Hands-On Exercises - SQLite - Part I
SQL Bootcamp - Hands-On Exercises - SQLite - Part II
100+ Ćwiczeń - Zaawansowane programowanie w języku Python
100+ Exercises - Advanced Python Programming
150+ Exercises - Data Structures in Python - Hands-On
Programowanie w języku C - od A do Z
150+ Ćwiczeń - Programowanie w języku C - od A do Z
Programowanie w języku C++ - od A do Z
150+ Ćwiczeń - Programowanie w języku C++ - od A do Z
150+ Ćwiczeń - Programowanie obiektowe w języku C++ - OOP
"""
import sqlite3


conn = sqlite3.connect("esmartdata.sqlite3")
cur = conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS "esmartdata_instructor";
CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
    "id" INTEGER NOT NULL,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_course";
CREATE TABLE IF NOT EXISTS "esmartdata_course" (
    "id" INTEGER NOT NULL,
    "title" TEXT NULL,
    "subtitle" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "category" TEXT NOT NULL,
    "subcategory" TEXT NOT NULL,
    "language" TEXT NOT NULL,
    "length" TEXT NOT NULL,
    "rating" REAL NOT NULL,
    "referral_link" TEXT NOT NULL,
    "instructor_id" INTEGER NULL,
    PRIMARY KEY("id" AUTOINCREMENT),
    FOREIGN KEY("instructor_id") REFERENCES "esmartdata_instructor"(id)
    ON DELETE CASCADE ON UPDATE CASCADE
);''')

print("Table created successfully!")

cur.executescript('''INSERT INTO "esmartdata_instructor"
(
    "id",
    "first_name",
    "last_name",
    "description"
) 
VALUES
(
    1,
    "Pawel",
    "Krakowiak",
    "Data Scientist/Python Developer/Securities Broker"
);

INSERT INTO "esmartdata_instructor"
(
    "id",
    "first_name",
    "last_name",
    "description"
)
VALUES
(
    2,
    "takeITeasy",
    "Academy",
    "Akademia Programowania"
)
''')

print('Data entered successfully!')


with open('load_esmartdata_course.sql', 'r', encoding='utf-8') as file:
    sql = file.read()

cur.executescript(sql)

cur.execute('''DROP INDEX IF EXISTS esmartdata_course_instructor_id_idx;''')
cur.execute('''CREATE INDEX IF NOT EXISTS esmartdata_course_instructor_id_idx ON esmartdata_course('instructor_id');
''')

print('Index created successfully!')

conn.commit()

cur.execute('''SELECT title FROM esmartdata_course;''')

for rows in cur.fetchall():
    print(rows[0])

conn.close()
