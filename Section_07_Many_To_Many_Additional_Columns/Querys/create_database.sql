BEGIN TRANSACTION;

DROP TABLE IF EXISTS "esmartdata_instructor";

CREATE TABLE IF NOT EXISTS "esmartdata_instructor" (
  "id" integer NOT NULL,
  "first_name" text NOT NULL,
  "last_name" text NOT NULL,
  "description" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_course";

CREATE TABLE IF NOT EXISTS "esmartdata_course" (
  "id" integer NOT NULL,
  "title" text NOT NULL,
  "subtitle" text NOT NULL,
  "category" text NOT NULL,
  "subcategory" text NOT NULL,
  "language" text NOT NULL,
  "length" text NOT NULL,
  "rating" real NOT NULL,
  "referral_link" text NOT NULL,
  "instructor_id" integer NOT NULL,
  FOREIGN KEY("instructor_id") REFERENCES "esmartdata_instructor"("id"),
  PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_learningpath";

CREATE TABLE IF NOT EXISTS "esmartdata_learningpath" (
  "id" integer NOT NULL,
  "title" text NOT NULL,
  "subtitle" text NOT NULL,
  "url" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "esmartdata_membership";

CREATE TABLE IF NOT EXISTS "esmartdata_membership" (
  "id" integer NOT NULL,
  "created" text NOT NULL,
  "course_id" integer NOT NULL,
  "learningpath_id" integer NOT NULL,
  FOREIGN KEY("course_id") REFERENCES "esmartdata_course"("id"),
  FOREIGN KEY("learningpath_id") REFERENCES "esmartdata_learningpath"("id"),
  PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO "esmartdata_instructor" ("id","first_name","last_name","description") VALUES (1,'Paweł','Krakowiak','Data Scientist/Python Developer/Securities Broker');
INSERT INTO "esmartdata_instructor" ("id","first_name","last_name","description") VALUES (2,'takeITeasy','Academy','Akademia Programowania');
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (1,'Wprowadzenie do data science w języku Python - Pandas','Zrób krok w stronę Pythona i analizuj dane jak profesjonalny data scientist!','development','programming languages','pl','12h 18min',4.78,'https://www.udemy.com/course/wprowadzenie-data-science/?referralCode=D85D646D30D785FD5277',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (2,'Deep Learning w języku Python - Konwolucyjne Sieci Neuronowe','Zrób krok w stronę sieci neuronowych dzięki bibliotece Keras!','development','data science','pl','8h 27min',4.5,'https://www.udemy.com/course/deep-learning-w-jezyku-python/?referralCode=24567C4A18A3F17E0B47',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (3,'Uczenie Maszynowe - Drzewa Decyzyjne i Lasy Losowe - Python','Poznaj od podstaw algorytmy uczenia maszynowego w języku Python! Twórz własne modele w bibliotece scikit-learn!','development','data science','pl','5h 43min',4.86,'https://www.udemy.com/course/uczenie-maszynowe-python/?referralCode=706180C6DDA1BE725C57',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (4,'Programowanie w języku Python - od A do Z','Naucz się jednego z najpopularniejszych języków programowania i otwórz sobie drzwi do kariery w IT! - Python','development','programming languages','pl','16h 5min',4.72,'https://www.udemy.com/course/programowanie-w-jezyku-python/?referralCode=C7E5AD6D60ADCBDEF759',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (5,'Twórz nowoczesne aplikacje webowe w Pythonie - Dash, Plotly','Twórz interaktywne aplikacje webowe w prosty i szybki sposób posługując się językiem Python!','development','web development','pl','11h 38min',4.81,'https://www.udemy.com/course/aplikacje-webowe-dash/?referralCode=40C44F12D311213BEC48',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (6,'Interaktywne wizualizacje danych w języku Python -  Plotly','Wizualizuj dane w języku Python przy pomocy bibliotek Seaborn oraz Plotly!','development','programming languages','pl','8h 37min',4.67,'https://www.udemy.com/course/wizualizacje-danych-python/?referralCode=A548AF40A5D2D658DAE6',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (7,'Big Data, Hadoop oraz MapReduce w języku Python','Opanuj budowanie MapReduce Jobs używając biblioteki MRJob oraz usługi Amazon Elastic MapReduce!','development','programming languages','pl','7h 44min',4.64,'https://www.udemy.com/course/big-data-bigquery/?referralCode=10C0A466D6710285AEC6',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (8,'Wprowadzenie do sieci neuronowych - Tensorflow 2.0 + Keras','Naucz się budować sieci neuronowe w języku Python wykorzystując najnowocześniejsze rozwiązania!','development','data science','pl','8h 38min',4.64,'https://www.udemy.com/course/wprowadzenie-tensorflow-keras/?referralCode=74356FE803194F2C3C42',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (9,'Big Data: Analiza danych przy użyciu SQL oraz BigQuery','Analizuj dane rzędu GB czy TB w mgnieniu oka. Wykorzystaj przewagę rozwiązań chmurowych już dziś!','development','database design & development','pl','9h 26min',4.45,'https://www.udemy.com/course/big-data-bigquery/?referralCode=10C0A466D6710285AEC6',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (10,'Artificial Intelligence – Computer Vision w języku Python','Sztuczna inteligencja - Odkryj Computer Vision z bibliotekami OpenCV, Tensorflow, Keras oraz PyTesseract','development','data science','pl','6h 51min',4.87,'https://www.udemy.com/course/artificial-intelligence-computer-vision/?referralCode=09C26CA07A8F6DF74148',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (11,'Data Science Bootcamp w języku Python - od A do Z','Wejdź w świat data science i otwórz sobie drogę do zawodu przyszłości - data scientist!','development','data science','pl','12h 40min',4.48,'https://www.udemy.com/course/data-science-bootcamp-python/?referralCode=7ACF0CA84807A88740FB',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (12,'Machine Learning Bootcamp w języku Python cz.I - od A do Z','Uczenie Maszynowe - Wejdź w świat uczenia nadzorowanego i wykorzystaj przewagę uczenia maszynowego na rynku!','development','data science','pl','11h 1min',4.73,'https://www.udemy.com/course/machine-learning-bootcamp-w-jezyku-python/?referralCode=92994CE6227390CFA9D7',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (13,'Machine Learning Bootcamp w języku Python cz.II - od A do Z','Uczenie Maszynowe - Wejdź w świat uczenia nienadzorowanego i wykorzystaj przewagę uczenia maszynowego na rynku!','development','data science','pl','5h 9min',4.89,'https://www.udemy.com/course/machine-learning-bootcamp-w-jezyku-python-ii/?referralCode=AE397842FEFADB697DC8',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (14,'200+ Ćwiczeń - Programowanie w języku Python - od A do Z','Podnieś poziom swoich umiejętności programowania w języku Python i rozwiąż ponad 200 zadań o różnym poziomie trudności!','development','programming languages','pl','0h 37 min',4.66,'https://www.udemy.com/course/programowanie-w-jezyku-python-od-a-do-z-cwiczenia/?referralCode=F7E8037914EA401783CF',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (15,'250+ Ćwiczeń - Data Science Bootcamp w języku Python','Podnieś poziom swoich umiejętności programowania w języku Python i rozwiąż ponad 250 zadań z data science!','development','programming languages','pl','7h 8min',4.89,'https://www.udemy.com/course/250-data-science-bootcamp-w-jezyku-python/?referralCode=BFFC4AF3CF8B8A6C85AB',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (16,'200+ Exercises - Programming in Python - from A to Z','Improve your Python programming skills and solve over 200 exercises!','development','programming languages','eng','0h 30min',4.29,'https://www.udemy.com/course/200-exercises-programming-in-python-from-a-to-z/?referralCode=B8F5DEBD2FB418EA4147',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (17,'250+ Exercises - Data Science Bootcamp in Python','Improve your Python programming skills and solve over 250 data science exercises!','development','data science','eng','0h 29min',4.29,'https://www.udemy.com/course/250-exercises-data-science-bootcamp-in-python/?referralCode=673FE6893CE253526C4D',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (18,'100+ Exercises - Python Programming - Data Science - NumPy','Improve your Python programming and data science skills and solve over 100 exercises in NumPy!','development','data science','eng','0h 30min',4.13,'https://www.udemy.com/course/100-exercises-python-programming-data-science-numpy/?referralCode=5EBB9741CD12E8CEB744',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (19,'130+ Exercises - Python Programming - Data Science - Pandas','Improve your Python programming and data science skills and solve over 130 exercises in Pandas!','development','data science','eng','0h 28min',4.08,'https://www.udemy.com/course/100-exercises-python-programming-data-science-pandas/?referralCode=9ACF7D5172F2AC8C8A40',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (20,'100+ Exercises - Python - Data Science - scikit-learn','Improve your machine learning skills and solve over 100 exercises in python, numpy, pandas and scikit-learn!','development','data science','eng','0h 28min',3.6,'https://www.udemy.com/course/100-exercises-python-data-science-scikit-learn/?referralCode=4BEED75986FF57D56D59',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (21,'Machine Learning Bootcamp w języku Python cz.III - Ćwiczenia','Podnieś poziom swoich umiejętności programowania w języku Python i rozwiąż ponad 100 zadań z uczenia maszynowego!','development','data science','pl','0h 33min',4.87,'https://www.udemy.com/course/machine-learning-bootcamp-w-jezyku-python-cwiczenia/?referralCode=69411EC2497CD9119831',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (22,'210+ Ćwiczeń - Python - Moduły wbudowane - od A do Z','Podnieś poziom swoich umiejętności programowania w języku Python i rozwiąż ponad 210 zadań z modułów wbudowanych!','development','programming languages','pl','0h 33min',4.61,'https://www.udemy.com/course/cwiczenia-python-moduly-wbudowane/?referralCode=2FC3D3B57972694B5D40',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (23,'210+ Exercises - Python Standard Libraries - from A to Z','Improve your Python programming skills and solve over 210 exercises with Python standard libraries!','development','programming languages','eng','0h 28min',4.41,'https://www.udemy.com/course/exercises-python-standard-libraries/?referralCode=C4B0D9955BD0C79696EE',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (24,'Programowanie obiektowe w języku Python - OOP - od A do Z','Naucz się programowania obiektowego (OOP) w języku Python i otwórz sobie drzwi do kariery w IT! - Python','development','programming languages','pl','10h 5min',4.6,'https://www.udemy.com/course/programowanie-obiektowe-jezyk-python-oop-kurs/?referralCode=A277D1725978D0DA0A9B',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (25,'150+ Ćwiczeń - Programowanie obiektowe w języku Python - OOP','Sprawdź się z programowania obiektowego (OOP) w języku Python i rozwiąż ponad 150 ćwiczeń z OOP! - Python','development','programming languages','pl','0h 43min',4.81,'https://www.udemy.com/course/cwiczenia-programowanie-obiektowe-w-jezyku-python-oop-kurs/?referralCode=0658F3C7E0CF039D280E',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (26,'150+ Exercises - Object Oriented Programming in Python - OOP','Test your Python programming skills in object-oriented programming (OOP) and solve over 150 exercises! - Python','development','programming languages','eng','0h 28min',4.92,'https://www.udemy.com/course/exercises-object-oriented-programming-in-python-oop-course/?referralCode=B53C3A8BD1A72E62EFE1',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (27,'120+ Ćwiczeń w języku Python - Data Science - NumPy','Podnieś poziom swoich umiejętności programowania w języku Python oraz data science i rozwiąż ponad 120 ćwiczeń w NumPy!','development','data science','pl','0h 33min',4.81,'https://www.udemy.com/course/python-data-science-numpy-cwiczenia/?referralCode=CE6EF51049A940B99286',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (28,'130+ Ćwiczeń w języku Python - Data Science - Pandas','Podnieś poziom swoich umiejętności programowania w języku Python oraz data science i rozwiąż ponad 130 ćwiczeń w Pandas!','development','data science','pl','0h 33min',4.78,'https://www.udemy.com/course/cwiczenia-jezyk-python-data-science-pandas/?referralCode=67448BE61AC404315CD5',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (29,'Testy jednostkowe w języku Python - framework unittest','Naucz się pisać testy jednostkowe w języku Python i otwórz sobie drzwi do kariery w IT! - Python, unittest','development','programming languages','pl','4h 58min',4.64,'https://www.udemy.com/course/kurs-testy-jednostkowe-jezyk-python-framework-unittest/?referralCode=F2A5869309BF127E806F',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (30,'100+ Ćwiczeń - Testy jednostkowe w języku Python - unittest','Podnieś poziom swoich umiejętności programowania w języku Python i rozwiąż ponad 100 ćwiczeń z testów jednostkowych!','development','programming languages','pl','0h 33min',4.4,'https://www.udemy.com/course/testy-jednostkowe-w-jezyku-python-unittest-kurs/?referralCode=A923D8BD40476EDDA13B',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (31,'100+ Exercises - Unit tests in Python - unittest framework','Improve your Python programming and unit testing skills and solve over 100 exercises with Python and unittest framework!','development','programming languages','eng','0h 28min',4.76,'https://www.udemy.com/course/unit-testing-python-unittest-framework/?referralCode=876B2AFF6B1E38D534CE',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (32,'SQL Bootcamp - Bazy danych SQLite - Part I','Rozpocznij swoją przygodę z bazami danych i językiem SQL. Otwórz sobie drzwi do kariery w IT!','development','database design & development','pl','5h 17min',4.47,'https://www.udemy.com/course/sql-bootcamp-bazy-danych-sqlite/?referralCode=CBFDC1BBD8C0B3942207',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (33,'SQL Bootcamp - Bazy danych SQLite - Part II','Rozpocznij swoją przygodę z bazami danych i językiem SQL. Otwórz sobie drzwi do kariery w IT!','development','database design & development','pl','4h 56min',4.57,'https://www.udemy.com/course/sql-bootcamp-bazy-danych-sqlite-2/?referralCode=D9C065553AEF8DD7CE45',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (34,'SQL Bootcamp - Bazy danych SQLite - Part III - Ćwiczenia','Rozpocznij przygodę z bazami danych i językiem SQL. Rozwiąż ponad 140 ćwiczeń i otwórz sobie drzwi do kariery w IT!','development','database design & development','pl','0h 36min',4.72,'https://www.udemy.com/course/sql-bootcamp-bazy-danych-sqlite-cwiczenia/?referralCode=D3B2EA9829FC6D4AE308',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (35,'SQL Bootcamp - Bazy danych SQLite - Part IV - Ćwiczenia','Sprawdź się z baz danych i języka SQL. Rozwiąż ponad 130 ćwiczeń i otwórz sobie drzwi do kariery w IT!','development','database design & development','pl','0h 36min',5.0,'https://www.udemy.com/course/sql-bootcamp-bazy-danych-sqlite-cwiczenia-ii/?referralCode=C59DBA99D2FE9EDB3B8E',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (36,'SQL Bootcamp - Hands-On Exercises - SQLite - Part I','Start your journey with SQL and databases. Solve over 150 exercises and open the door to a career in IT! (DQL)','development','database design & development','eng','0h 28min',4.61,'https://www.udemy.com/course/sql-bootcamp-hands-on-exercises-sqlite-part-i/?referralCode=FF68FEF0106BDE6D4950',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (37,'SQL Bootcamp - Hands-On Exercises - SQLite - Part II','Start your journey with SQL and databases. Solve over 150 exercises and open the door to a career in IT! (DDL + DML)','development','database design & development','eng','0h 28min',4.61,'https://www.udemy.com/course/sql-bootcamp-hands-on-exercises-sqlite-part-ii/?referralCode=A12E7493134B4913E53B',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (38,'100+ Ćwiczeń - Zaawansowane programowanie w języku Python','Podnieś poziom swoich umiejętności programowania w języku Python i rozwiąż ponad 100 zaawansowanych zadań w Pythonie!','development','programming languages','pl','0h 33min',4.56,'https://www.udemy.com/course/zaawansowane-programowanie-w-jezyku-python/?referralCode=9F06CF056805CD81EE54',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (39,'100+ Exercises - Advanced Python Programming','Improve your Python programming skills and solve over 100 advanced Python problems!','development','programming languages','eng','0h 28min',5.0,'https://www.udemy.com/course/advanced-exercises-python-programming/?referralCode=24CF0346E66901646D5D',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (40,'150+ Exercises - Data Structures in Python - Hands-On','Improve your Python programming skills and solve over 150 exercises with data structures!','development','programming languages','eng','0h 28min',5.0,'https://www.udemy.com/course/150-exercises-data-structures-in-python/?referralCode=3725F199011E95ED4221',1);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (41,'Programowanie w języku C - od A do Z','Naucz się jednego z najpopularniejszych języków programowania i otwórz sobie drzwi do kariery w IT! - Język C','development','programming languages','pl','6h 28min',4.24,'https://www.udemy.com/course/programowanie-w-jezyku-c/?referralCode=EC17C4A00434490F602F',2);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (42,'150+ Ćwiczeń - Programowanie w języku C - od A do Z','Podnieś poziom swoich umiejętności programowania w języku C i rozwiąż ponad 150 zadań o różnym poziomie trudności!','development','programming languages','pl','0h 31min',4.25,'https://www.udemy.com/course/150-cwiczen-programowanie-w-jezyku-c-od-a-do-z-2020/?referralCode=F5B2E205248F39CE7516',2);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (43,'Programowanie w języku C++ - od A do Z','Naucz się jednego z najpopularniejszych języków programowania i zacznij pisać praktyczne programy w języku C++','development','programming languages','pl','9h 4min',4.61,'https://www.udemy.com/course/programowanie-w-jezyku-cpp-od-a-do-z/?referralCode=DE2D6835B13468381D8A',2);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (44,'150+ Ćwiczeń - Programowanie w języku C++ - od A do Z','Podnieś poziom swoich umiejętności programowania w języku C++ i rozwiąż ponad 150 zadań o różnym poziomie trudności!','development','programming languages','pl','0h 38min',4.56,'https://www.udemy.com/course/150-cwiczen-programowanie-w-jezyku-cpp/?referralCode=8DD53055EC487C303A46',2);
INSERT INTO "esmartdata_course" ("id","title","subtitle","category","subcategory","language","length","rating","referral_link","instructor_id") VALUES (45,'150+ Ćwiczeń - Programowanie obiektowe w języku C++ - OOP','Podnieś poziom swoich umiejętności o programowanie obiektowe w języku C++ i rozwiąż ponad 150 ćwiczeń na różnym poziomie','development','programming languages','pl','0h 30min',5.0,'https://www.udemy.com/course/150-cwiczen-programowanie-obiektowe-w-jezyku-cpp-oop/?referralCode=B516ED45D6F0EA7A9E94',2);
INSERT INTO "esmartdata_learningpath" ("id","title","subtitle","url") VALUES (2,'Ścieżka C Developer','Naucz się jednego z najpopularniejszych języków programowania i otwórz drzwi do kariery w IT!','https://e-smartdata.teachable.com/p/sciezka-c-developer');
INSERT INTO "esmartdata_learningpath" ("id","title","subtitle","url") VALUES (3,'Ścieżka C++ Developer','Naucz się jednego z najpopularniejszych języków programowania i otwórz drzwi do kariery w IT!','https://e-smartdata.teachable.com/p/sciezka-cpp-developer');
INSERT INTO "esmartdata_learningpath" ("id","title","subtitle","url") VALUES (4,'Ścieżka Python Developer','Naucz się jednego z najpopularniejszych języków programowania i otwórz drzwi do kariery w IT!','https://e-smartdata.teachable.com/p/sciezka-python-developer');
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (2,'2021-02-03',41,2);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (3,'2021-02-17',42,2);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (4,'2021-03-15',43,3);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (5,'2021-03-22',44,3);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (6,'2021-05-12',45,3);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (7,'2021-01-05',4,4);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (8,'2021-01-26',14,4);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (9,'2021-02-05',22,4);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (10,'2021-03-08',24,4);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (11,'2021-03-30',25,4);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (12,'2021-05-11',38,4);
INSERT INTO "esmartdata_membership" ("id","created","course_id","learningpath_id") VALUES (13,'2021-04-13',29,4);

COMMIT;
