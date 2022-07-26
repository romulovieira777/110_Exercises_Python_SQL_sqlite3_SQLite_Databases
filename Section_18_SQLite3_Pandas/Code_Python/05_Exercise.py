"""
Exercise No. 05

Using the built-in sqlite3 package, create a SQLite database names "app_archive.db".

Using the pandas package, load the file "comment_archive.csv" into the DataFrame object. Then, using this object, create
a table named "app_comment_archive" in the database "app_archive.db".

In response, create a query and extract all records from the "app_comment_archive" table and print to the console as
shown below:

Expected result:
    (3, 'Herself stuff size inside probably personal.', '2021-05-24 21:25:36')
    (85, 'Painting follow rock whole check health research treatment.', '2021-05-24 19:22:15')
    (258, 'Popular husband less civil customer issue mouth position network particularly.', '2021-05-24 16:39:17')
    (118, 'Deep we who whole race study various house order.', '2021-05-24 15:58:50')
    (169, 'Would woman clear bad season close fast.', '2021-05-24 13:27:35')
    (79, 'Man smile nature let hotel development.', '2021-05-24 12:08:57')
    (207, 'Return win natural with read want recent sea administration room.', '2021-05-24 10:29:49')
    (143, 'Their capital peace PM face feeling cold part third choose.', '2021-05-24 09:19:46')
    (213, 'And area local thus raise yeah produce theory action future strategy.', '2021-05-24 07:49:01')
    (67, 'Truth series manager example game represent various increase.', '2021-05-24 07:42:22')
    (78, 'Answer security move close difficult house state individual over.', '2021-05-24 03:49:06')
    (165, 'Democrat difference painting situation sing pull century.', '2021-05-24 03:13:45')
    (56, 'I available walk near miss.', '2021-05-24 01:31:47')
    (110, 'Foot opportunity sort college I up explain threat relationship life finish.', '2021-05-23 22:05:43')
    (146, 'Alone perform seat ahead.', '2021-05-23 20:11:42')
    (2, 'Purpose start hard fall positive officer various.', '2021-05-23 16:42:10')
    (87, 'Easy majority international exactly likely campaign your.', '2021-05-23 16:22:20')
    (120, 'Begin water manager amount program home father modern edge wonder.', '2021-05-23 15:54:21')
    (188, 'Reach suffer yes reduce party term first order.', '2021-05-23 14:16:16')
    (241, 'Catch rich trip lose.', '2021-05-23 13:00:02')
    (73, 'Work anyone next task crime magazine.', '2021-05-23 12:29:27')
    (42, 'Day his peace culture job thousand idea mother black or.', '2021-05-23 11:45:46')
    (8, 'Save follow image simply interview door vote sport name.', '2021-05-23 08:02:51')
    (287, 'Personal laugh night former fine her mention imagine sort reflect.', '2021-05-23 04:58:25')
    (170, 'Growth large personal main care push cup mention early.', '2021-05-23 02:54:41')
    (153, 'Particular much operation none term.', '2021-05-23 00:28:44')
"""
import pandas as pd
import sqlite3

conn = sqlite3.connect("app_archive.db")  # connect to the database
cur = conn.cursor()  # create a cursor object

df = pd.read_csv("../Dataset/comment_archive.csv")  # read the data from the file
df.to_sql('app_comment_archive', con=conn, index=False, if_exists='replace')  # export the data to a SQLite database

cur.execute("SELECT * FROM app_comment_archive;")  # execute the sql query

for row in cur.fetchall():
    print(row)

conn.close()  # close the connection
