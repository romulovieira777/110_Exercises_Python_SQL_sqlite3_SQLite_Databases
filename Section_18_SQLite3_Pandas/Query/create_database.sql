BEGIN TRANSACTION;

DROP TABLE IF EXISTS "app_user";
CREATE TABLE IF NOT EXISTS "app_user" (
  "id" integer NOT NULL,
  "first_name" text NOT NULL,
  "last_name" text NOT NULL,
  "age" integer NOT NULL,
  "country" text NOT NULL,
  "city" text NOT NULL,
  "email" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "app_thread";
CREATE TABLE IF NOT EXISTS "app_thread" (
  "id" integer NOT NULL,
  "title" text NOT NULL,
  "creator_id" integer NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT),
  FOREIGN KEY("creator_id") REFERENCES "app_user"("id")
  ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "app_comment";
CREATE TABLE IF NOT EXISTS "app_comment" (
  "id" integer NOT NULL,
  "body" text NOT NULL,
  "created" text NOT NULL,
  "thread_id" integer NOT NULL,
  "user_id" integer NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT),
  FOREIGN KEY("thread_id") REFERENCES "app_thread"("id")
  ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY("user_id") REFERENCES "app_user"("id")
  ON DELETE CASCADE ON UPDATE CASCADE
);

DROP TABLE IF EXISTS "app_group";
CREATE TABLE IF NOT EXISTS "app_group" (
  "id" integer NOT NULL,
  "name" text NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);

DROP TABLE IF EXISTS "app_group_user";
CREATE TABLE IF NOT EXISTS "app_group_user" (
  "id" integer NOT NULL,
  "group_id" integer NOT NULL,
  "user_id" integer NOT NULL,
  PRIMARY KEY("id" AUTOINCREMENT),
  FOREIGN KEY("group_id") REFERENCES "app_group"("id")
  ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY("user_id") REFERENCES "app_user"("id")
  ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (1,'John','Lewis',61,'Tonga','East Michael','johnsonjack@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (2,'Lance','Boyer',21,'Seychelles','Janicetown','thodges@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (3,'Michael','Larson',22,'Czech Republic','West Melissa','kmalone@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (4,'Alexandra','Marshall',50,'Malaysia','Lunamouth','yperry@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (5,'Rebecca','Maldonado',51,'Canada','Lake Sandrastad','mwade@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (6,'Ronald','Ward',61,'French Guiana','Kennethview','lisa46@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (7,'Justin','Wolf',19,'French Southern Territories','Kristinestad','greenjustin@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (8,'Nicole','Fuentes',63,'Gambia','Port Frank','brandonchandler@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (9,'Melissa','Rowland',45,'Sudan','Alexiston','gibsonjennifer@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (10,'Sean','Schmidt',42,'Nauru','Alyssafort','vterry@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (11,'Charles','Rios',54,'Burkina Faso','Sandraside','davidharvey@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (12,'Kimberly','Smith',33,'Saint Pierre and Miquelon','Stokesborough','rhodesanne@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (13,'Patrick','Burke',31,'South Africa','Victorland','omurphy@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (14,'Jerry','Patton',48,'New Caledonia','West Ronald','ashley44@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (15,'Albert','Adams',49,'Botswana','Hartland','lance67@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (16,'Katherine','Williams',50,'Pitcairn Islands','Lake Mark','hicksnathan@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (17,'Michael','Turner',23,'Gambia','West Timothy','matthewcox@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (18,'Paul','Mckinney',65,'Syrian Arab Republic','Shirleyfort','brownjennifer@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (19,'Scott','Berry',20,'Macedonia','New Joshua','uhanson@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (20,'Alexa','Cruz',46,'Iceland','Margarettown','ywilliams@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (21,'Kenneth','Henderson',35,'El Salvador','Brittanyton','tfitzgerald@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (22,'Justin','Anderson',64,'Armenia','Port Jay','wanda97@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (23,'Erin','Stark',41,'Guinea','New Megan','mary43@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (24,'Kimberly','Myers',28,'Aruba','West Lauraland','mccormickdavid@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (25,'Carol','Walton',24,'Mauritania','New Ethan','stephen65@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (26,'Larry','Rowe',27,'Jersey','West Alexander','riverajames@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (27,'Madeline','Stevens',47,'New Caledonia','Rosschester','hickssamuel@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (28,'Benjamin','Lopez',22,'Cape Verde','Nancybury','william31@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (29,'Kenneth','Perry',30,'Guinea-Bissau','Romeroburgh','choidaniel@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (30,'Katherine','Hines',18,'Timor-Leste','New Dylanshire','bartonmary@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (31,'Diane','Castro',33,'Fiji','Lake Traciton','aaron40@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (32,'Denise','Foster',31,'Lithuania','New Josephtown','jeremy68@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (33,'Timothy','Johnson',44,'Norfolk Island','Chaneymouth','andre95@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (34,'Christopher','Leonard',31,'Micronesia','Jacksonchester','philipcastillo@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (35,'Michael','Jenkins',61,'Macedonia','Stewartburgh','tlopez@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (36,'Christopher','Moore',18,'Malawi','North Morganburgh','herringcalvin@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (37,'Brittany','Stewart',60,'El Salvador','Lake Kenneth','murphyjames@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (38,'Jeffrey','Lewis',60,'Isle of Man','New Jessica','melissa42@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (39,'John','Jimenez',38,'Jamaica','Hicksburgh','jonesjennifer@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (40,'Jennifer','Wallace',31,'Czech Republic','Christinachester','frankdodson@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (41,'Dwayne','Nelson',21,'Bulgaria','Port Destiny','larrypace@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (42,'Andrew','Page',35,'Pakistan','Lake Jack','brandy82@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (43,'Kevin','Fisher',65,'Dominica','Shannonmouth','jamesjonathan@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (44,'Nicole','Sanchez',24,'Lesotho','Hallmouth','christina47@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (45,'Rebecca','Brown',18,'Ghana','Jenniferfort','annettemitchell@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (46,'Scott','Wright',47,'Dominican Republic','Nathanielland','stacygarcia@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (47,'David','Mcdonald',48,'Peru','Hugheshaven','sharris@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (48,'Sara','Hensley',28,'Saudi Arabia','Randybury','crystalscott@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (49,'Patrick','Cox',43,'Suriname','West Jeffreyport','steven58@esmartdata.org');
INSERT INTO "app_user" ("id","first_name","last_name","age","country","city","email") VALUES (50,'Emily','Gonzalez',57,'Cocos (Keeling) Islands','Emilyland','zfranklin@esmartdata.org');
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (1,'Picture plant would laugh.',45);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (2,'Positive all method stage paper.',15);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (3,'Film maintain responsibility.',28);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (4,'Media later color.',41);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (5,'Body chance face.',28);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (6,'Argue star in always.',49);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (7,'Just officer worry keep.',22);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (8,'Who study when consider.',21);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (9,'Boy stay great.',21);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (10,'Pick power wear worry.',15);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (11,'Ago should hard away.',5);
INSERT INTO "app_thread" ("id","title","creator_id") VALUES (12,'Adult wind control argue leave.',28);
INSERT INTO "app_group" ("id","name") VALUES (1,'Director member now ready forget.');
INSERT INTO "app_group" ("id","name") VALUES (2,'Sport by.');
INSERT INTO "app_group" ("id","name") VALUES (3,'Particularly sense look.');
INSERT INTO "app_group" ("id","name") VALUES (4,'What recently school try sign.');
INSERT INTO "app_group" ("id","name") VALUES (5,'Officer matter life realize alone.');
INSERT INTO "app_group" ("id","name") VALUES (6,'Game remain accept.');
INSERT INTO "app_group" ("id","name") VALUES (7,'Executive group eye.');
INSERT INTO "app_group" ("id","name") VALUES (8,'Until might hair.');
INSERT INTO "app_group" ("id","name") VALUES (9,'Support bank mission.');
INSERT INTO "app_group" ("id","name") VALUES (10,'Describe government security surface.');
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (1,1,3);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (2,1,37);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (3,1,44);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (4,1,46);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (5,1,22);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (6,1,23);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (7,1,30);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (8,2,4);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (9,2,41);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (10,2,13);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (11,2,47);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (12,2,17);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (13,2,18);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (14,2,31);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (15,3,36);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (16,3,8);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (17,3,11);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (18,3,46);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (19,3,50);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (20,3,23);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (21,3,26);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (22,3,28);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (23,4,36);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (24,4,5);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (25,4,7);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (26,4,47);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (27,4,18);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (28,4,19);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (29,4,23);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (30,4,24);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (31,5,37);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (32,5,12);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (33,5,17);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (34,5,21);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (35,5,22);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (36,5,23);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (37,5,28);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (38,5,29);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (39,6,38);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (40,6,7);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (41,6,40);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (42,6,39);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (43,6,44);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (44,6,13);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (45,6,46);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (46,6,22);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (47,7,3);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (48,7,36);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (49,7,5);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (50,7,38);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (51,7,41);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (52,7,45);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (53,7,17);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (54,7,31);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (55,8,38);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (56,8,9);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (57,8,10);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (58,8,44);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (59,8,15);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (60,8,20);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (61,8,22);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (62,9,4);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (63,9,6);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (64,9,39);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (65,9,7);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (66,9,41);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (67,9,46);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (68,9,28);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (69,9,29);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (70,10,5);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (71,10,8);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (72,10,42);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (73,10,45);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (74,10,48);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (75,10,49);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (76,10,23);
INSERT INTO "app_group_user" ("id","group_id","user_id") VALUES (77,10,25);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (1,'Thank different receive difficult success.','2021-05-21 21:22:15',1,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (2,'Purpose start hard fall positive officer various.','2021-05-23 16:42:10',1,48);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (3,'Herself stuff size inside probably personal.','2021-05-24 21:25:36',1,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (4,'Enjoy yes loss enough middle.','2021-05-08 17:56:25',1,36);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (5,'Threat buy stop culture offer near protect claim particular.','2021-05-15 02:16:13',1,15);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (6,'Really son none will town behind ball effect time.','2021-05-02 09:04:00',1,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (7,'Idea sense choice hospital language customer back all.','2021-05-02 01:47:47',1,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (8,'Save follow image simply interview door vote sport name.','2021-05-23 08:02:51',1,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (9,'Rich think system husband every bill name take imagine issue sense.','2021-05-05 20:43:59',1,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (10,'Mean heavy him term blue shake perhaps former reality some.','2021-05-11 01:07:57',1,6);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (11,'Cut create three five either strong.','2021-05-07 04:55:45',1,50);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (12,'Impact lead land anyone would policy.','2021-05-06 09:31:14',1,2);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (13,'Customer color stuff around serious.','2021-05-14 02:50:15',1,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (14,'Service true various attorney until factor culture let.','2021-05-12 01:05:33',1,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (15,'Yourself education physical much detail suggest.','2021-05-02 18:33:04',1,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (16,'Answer mission radio surface front fill campaign mother.','2021-05-14 00:01:40',1,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (17,'Election business yeah worry interesting fall term dream new.','2021-05-18 11:45:26',1,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (18,'Age candidate election TV away operation however some.','2021-05-09 06:55:43',1,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (19,'All short whose may themselves station need.','2021-05-13 07:16:51',1,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (20,'Any office lead course baby executive international be scientist draw.','2021-05-14 14:48:58',1,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (21,'Hard newspaper although serious skin over some.','2021-05-16 01:15:09',1,18);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (22,'Decade challenge start make be write example would analysis tend.','2021-05-20 03:07:27',1,2);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (23,'National maybe product government.','2021-05-10 00:53:07',1,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (24,'Tough phone main story sure most new computer.','2021-05-02 16:24:12',1,46);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (25,'Social everyone increase music check allow much century practice.','2021-05-01 01:31:02',1,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (26,'Green new early unit suddenly both painting hot change.','2021-05-09 11:25:03',2,38);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (27,'Military tonight ago suffer feeling young lot economic.','2021-05-15 14:26:38',2,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (28,'Mother wind management drop.','2021-05-14 09:28:22',2,44);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (29,'Might guess nothing situation operation.','2021-05-22 07:53:29',2,46);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (30,'Face sure science until nothing policy war describe throughout.','2021-05-16 14:54:12',2,15);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (31,'Billion himself great low growth good.','2021-05-25 00:56:45',2,39);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (32,'Surface political also cup college.','2021-05-07 16:12:46',2,2);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (33,'Interest condition today enough onto word culture.','2021-05-18 23:01:26',2,1);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (34,'Teacher blood positive rule test mind easy.','2021-05-08 13:13:46',2,44);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (35,'Everybody recognize ask group class deal eight.','2021-05-12 16:22:43',2,49);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (36,'Product voice by service leg I paper style forward tend.','2021-05-04 03:05:55',2,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (37,'Remain sure theory son opportunity court perhaps contain.','2021-05-17 15:13:27',2,6);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (38,'Grow sit open my protect during purpose.','2021-05-19 19:08:06',2,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (39,'Cut already I education kid character.','2021-05-01 15:39:22',2,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (40,'Stay size study modern consumer wife.','2021-05-20 16:42:31',2,36);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (41,'Knowledge audience stop specific black boy someone lawyer front firm pattern.','2021-05-05 15:52:05',2,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (42,'Day his peace culture job thousand idea mother black or.','2021-05-23 11:45:46',2,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (43,'Movie first evening soon level.','2021-05-09 00:42:08',2,14);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (44,'Score budget difficult century above ever now citizen.','2021-05-15 01:30:14',2,11);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (45,'Commercial represent produce clearly computer draw figure themselves.','2021-05-17 22:05:15',2,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (46,'Reduce itself clear identify nation card effort.','2021-05-02 21:34:10',2,30);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (47,'List company research sign letter not amount must.','2021-05-08 14:59:36',2,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (48,'Direction argue top believe set season without always so.','2021-05-22 15:01:21',2,6);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (49,'Win catch travel current animal need recently.','2021-05-04 01:48:54',2,30);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (50,'Page Republican care level tree line night.','2021-05-09 03:49:07',2,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (51,'Might family that imagine especially standard season try.','2021-05-18 08:27:38',3,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (52,'Story six discuss up material anything medical film bad discussion.','2021-05-20 14:16:02',3,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (53,'Section various until to message she beautiful what.','2021-05-17 04:05:55',3,14);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (54,'Move their those still address.','2021-05-01 13:43:48',3,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (55,'Whether analysis in industry change difference.','2021-05-22 12:16:05',3,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (56,'I available walk near miss.','2021-05-24 01:31:47',3,1);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (57,'Professional the professor near science.','2021-05-16 04:11:42',3,44);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (58,'Art good easy simply save whose total production.','2021-05-17 13:47:51',3,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (59,'Development sea purpose hit decade business.','2021-05-09 08:53:18',3,18);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (60,'Space forward after certainly between.','2021-05-07 15:22:47',3,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (61,'Prevent moment page dark author.','2021-05-16 07:44:16',3,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (62,'Memory prevent friend majority summer fine measure some wonder talk.','2021-05-14 06:47:59',3,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (63,'To page indicate see generation.','2021-05-15 23:30:19',3,1);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (64,'Of response whatever civil national watch question another on.','2021-05-04 06:04:11',3,11);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (65,'Agree certainly probably force bed myself position such.','2021-05-03 17:53:54',3,46);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (66,'Herself career that table bed mission through agent.','2021-05-03 05:55:11',3,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (67,'Truth series manager example game represent various increase.','2021-05-24 07:42:22',3,26);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (68,'Interesting under hospital seek hope market top career center certain.','2021-05-19 17:23:22',3,42);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (69,'Thought glass car yes impact other impact right degree training manage.','2021-05-17 00:31:39',3,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (70,'Forward security spring answer contain be imagine support one only.','2021-05-19 21:51:22',3,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (71,'Say worry morning left write raise forward.','2021-05-11 03:59:08',3,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (72,'Between financial something thus certainly manage evidence avoid time.','2021-05-16 02:01:46',3,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (73,'Work anyone next task crime magazine.','2021-05-23 12:29:27',3,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (74,'Opportunity customer food situation happen little dark Mrs.','2021-05-10 12:25:14',3,16);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (75,'Sort board boy wait beat reality shoulder song somebody eye.','2021-05-03 12:07:08',3,46);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (76,'Those deep usually artist technology nearly a.','2021-05-04 09:05:50',4,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (77,'Wide cover clear material politics money since discussion country should.','2021-05-02 10:11:17',4,14);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (78,'Answer security move close difficult house state individual over.','2021-05-24 03:49:06',4,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (79,'Man smile nature let hotel development.','2021-05-24 12:08:57',4,37);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (80,'Another present American drug personal pick executive.','2021-05-02 00:10:55',4,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (81,'Memory morning hour bad late east big different avoid development.','2021-05-08 00:04:15',4,25);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (82,'Continue enter garden job itself region game prevent ok simply.','2021-05-08 19:23:14',4,14);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (83,'Outside prevent him radio chair we kind development cut development.','2021-05-10 19:18:12',4,45);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (84,'Type respond term interesting design president go new also.','2021-05-17 18:20:14',4,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (85,'Painting follow rock whole check health research treatment.','2021-05-24 19:22:15',4,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (86,'Citizen important forward resource receive the then head test office.','2021-05-08 07:48:09',4,20);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (87,'Easy majority international exactly likely campaign your.','2021-05-23 16:22:20',4,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (88,'Magazine answer everyone trouble party dog word.','2021-05-22 20:09:46',4,27);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (89,'True election hair local standard.','2021-05-11 06:31:56',4,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (90,'Happen wide garden culture computer again industry realize college certain.','2021-05-14 18:29:59',4,38);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (91,'Film seven name partner discuss they media figure discussion level.','2021-05-07 12:01:51',4,49);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (92,'Catch community board call behind wonder positive behind tax show.','2021-05-01 08:02:24',4,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (93,'Deep character Republican fight may force.','2021-05-11 03:56:30',4,18);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (94,'Produce accept modern town couple article nature issue.','2021-05-03 00:16:59',4,16);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (95,'Data medical laugh animal training organization region.','2021-05-18 02:17:17',4,18);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (96,'Office other cultural manager without else.','2021-05-13 14:05:08',4,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (97,'Eye imagine anything safe couple identify ok instead.','2021-05-13 00:58:45',4,42);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (98,'Expert over and particularly attention drop democratic buy forget various.','2021-05-13 01:03:52',4,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (99,'Item break grow technology politics grow big catch big.','2021-05-15 23:34:01',4,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (100,'Spend tell land use assume region fill we remain.','2021-05-17 11:31:41',4,37);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (101,'First scene population want leg late late talk.','2021-05-19 17:58:11',5,13);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (102,'Girl decade commercial church responsibility fact home.','2021-05-16 05:08:58',5,20);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (103,'Land trial third machine citizen possible.','2021-05-22 19:17:06',5,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (104,'Herself floor behavior among economic just machine develop well modern.','2021-05-15 13:30:10',5,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (105,'Whom experience less worker them work.','2021-05-16 19:45:23',5,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (106,'Door south PM see daughter class wide.','2021-05-13 07:47:18',5,36);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (107,'Officer Democrat economic show there though purpose build wide describe.','2021-05-16 14:14:46',5,1);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (108,'Necessary arm power want sport charge.','2021-05-21 05:01:15',5,15);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (109,'Full condition body easy rest hundred on name.','2021-05-07 22:45:18',5,26);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (110,'Foot opportunity sort college I up explain threat relationship life finish.','2021-05-23 22:05:43',5,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (111,'War live figure Mr.','2021-05-20 13:15:19',5,26);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (112,'Enjoy race company design bank country quite include.','2021-05-21 10:58:19',5,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (113,'Analysis its money make occur east task.','2021-05-19 10:39:12',5,50);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (114,'Though probably eye society way push avoid including example.','2021-05-20 03:54:28',5,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (115,'Away or control save election approach agree toward stuff.','2021-05-02 22:19:11',5,45);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (116,'Money all picture three.','2021-05-01 21:23:57',5,36);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (117,'Great material want memory force stuff quite eat mother.','2021-05-09 04:16:20',5,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (118,'Deep we who whole race study various house order.','2021-05-24 15:58:50',5,42);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (119,'New wide bar practice doctor them.','2021-05-15 10:31:39',5,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (120,'Begin water manager amount program home father modern edge wonder.','2021-05-23 15:54:21',5,30);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (121,'Action news daughter walk result thank full back member church.','2021-05-19 21:29:11',5,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (122,'Among evidence college produce avoid.','2021-05-02 20:41:47',5,50);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (123,'Film rest industry produce decide.','2021-05-10 09:13:52',5,48);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (124,'Interesting themselves total world statement guy song election idea especially.','2021-05-02 13:20:18',5,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (125,'Former short during guess realize range increase economy.','2021-05-20 02:01:23',5,11);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (126,'Create alone already heart boy court write memory scene.','2021-05-21 01:00:42',6,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (127,'Try every child get account than approach will tonight still.','2021-05-10 13:14:33',6,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (128,'Method explain person by challenge plant.','2021-05-10 09:19:01',6,45);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (129,'Give house PM mouth page measure.','2021-05-14 23:31:20',6,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (130,'Never question far hospital need.','2021-05-19 12:52:31',6,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (131,'The national end involve because during school.','2021-05-18 02:08:01',6,36);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (132,'Remember message during clear writer something staff court.','2021-05-21 13:01:14',6,42);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (133,'Deep hold move law necessary according music own our.','2021-05-15 07:05:59',6,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (134,'Senior upon late into someone career treatment.','2021-05-01 04:18:37',6,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (135,'Rock magazine bring nice herself drop.','2021-05-05 06:51:54',6,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (136,'Keep meeting bank new money himself enjoy same some program.','2021-05-16 14:12:45',6,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (137,'Chance person certain student prepare born water form opportunity.','2021-05-12 03:15:25',6,38);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (138,'Late middle compare value long.','2021-05-02 10:31:46',6,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (139,'Them mind send information whatever current offer reason.','2021-05-19 15:36:17',6,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (140,'So Mr identify campaign majority all health relate listen.','2021-05-07 18:50:30',6,36);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (141,'Rise research Congress now blood receive top system night.','2021-05-11 11:47:55',6,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (142,'City large form his ask do.','2021-05-09 11:13:40',6,27);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (143,'Their capital peace PM face feeling cold part third choose.','2021-05-24 09:19:46',6,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (144,'Because individual interview hospital consider support baby social yourself.','2021-05-12 13:10:18',6,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (145,'Participant front situation actually away computer.','2021-05-19 20:01:56',6,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (146,'Alone perform seat ahead.','2021-05-23 20:11:42',6,16);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (147,'Team hit newspaper operation fight type success.','2021-05-11 12:20:48',6,48);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (148,'Pm federal deal owner produce carry office strategy ability.','2021-05-09 10:52:17',6,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (149,'Will your off bed little conference ever mind read.','2021-05-04 03:59:22',6,44);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (150,'Space read everybody meeting rock arrive sometimes argue factor.','2021-05-06 14:49:24',6,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (151,'Option piece those public indeed continue then out book.','2021-05-19 01:38:40',7,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (152,'Conference sea impact black production million suffer.','2021-05-15 00:33:32',7,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (153,'Particular much operation none term.','2021-05-23 00:28:44',7,25);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (154,'Material serve board research nothing loss.','2021-05-15 16:48:46',7,15);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (155,'Similar trouble tend again total remember.','2021-05-19 02:50:06',7,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (156,'Marriage move though professor yet baby paper include anything theory.','2021-05-20 07:53:42',7,30);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (157,'Result point unit available media fact history.','2021-05-17 05:59:51',7,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (158,'Be trouble child half note body campaign.','2021-05-17 08:15:34',7,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (159,'Describe them you smile explain thus add stuff song.','2021-05-02 05:13:12',7,48);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (160,'Next phone tell south like be behavior.','2021-05-12 11:20:27',7,11);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (161,'Phone as health source put stuff national region edge husband.','2021-05-06 07:05:28',7,12);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (162,'Stock difference too seek ago sister past teach grow.','2021-05-10 02:59:50',7,12);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (163,'In someone I light rather they conference.','2021-05-10 04:12:49',7,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (164,'They also among wind up on shoulder.','2021-05-05 11:30:48',7,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (165,'Democrat difference painting situation sing pull century.','2021-05-24 03:13:45',7,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (166,'Guess radio matter yes seat south.','2021-05-18 03:55:18',7,38);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (167,'Peace organization item space where contain.','2021-05-13 15:26:46',7,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (168,'Want see wide artist home population recently summer.','2021-05-18 23:57:24',7,2);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (169,'Would woman clear bad season close fast.','2021-05-24 13:27:35',7,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (170,'Growth large personal main care push cup mention early.','2021-05-23 02:54:41',7,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (171,'Near near new effect stand on level.','2021-05-01 22:40:22',7,44);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (172,'The white finally of report.','2021-05-20 19:10:39',7,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (173,'Task hospital car service fact man center.','2021-05-09 07:39:47',7,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (174,'Example real member place hold should type fast either risk.','2021-05-12 02:49:08',7,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (175,'Day go alone could material.','2021-05-18 23:23:43',7,26);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (176,'College really activity cell audience company.','2021-05-22 20:51:15',8,20);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (177,'Get under lawyer big who cut.','2021-05-20 12:33:51',8,5);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (178,'Ever phone firm minute somebody.','2021-05-18 18:06:30',8,1);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (179,'Season young here box address blood house onto.','2021-05-21 01:42:27',8,10);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (180,'Get husband little talk require.','2021-05-05 16:21:53',8,20);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (181,'Democrat training boy wrong easy.','2021-05-19 05:16:44',8,12);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (182,'Glass heart argue fact past outside area crime you long.','2021-05-03 12:55:20',8,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (183,'That tend black talk music laugh arm thing image at.','2021-05-14 04:01:47',8,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (184,'Light bad rather specific toward plan.','2021-05-02 00:00:59',8,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (185,'Response too especially only finally race poor study style rest.','2021-05-10 15:34:56',8,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (186,'Different ready list lead animal similar.','2021-05-15 07:16:19',8,45);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (187,'National main early station wonder generation film entire hour practice.','2021-05-09 20:02:04',8,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (188,'Reach suffer yes reduce party term first order.','2021-05-23 14:16:16',8,42);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (189,'Three support conference industry glass culture itself evidence full.','2021-05-02 01:06:07',8,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (190,'Live analysis politics movement performance.','2021-05-19 21:38:19',8,23);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (191,'Them medical responsibility quality know left.','2021-05-04 12:46:24',8,34);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (192,'Exist share just church baby.','2021-05-16 03:47:38',8,3);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (193,'Some president six career system treat spend drop worker continue.','2021-05-02 22:02:16',8,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (194,'Everybody customer item population model culture career certain.','2021-05-09 01:27:33',8,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (195,'Short consumer seek trial human be stock.','2021-05-22 03:46:04',8,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (196,'World parent child current girl.','2021-05-02 12:50:08',8,49);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (197,'Order quite finally where western yard.','2021-05-11 22:53:17',8,27);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (198,'Thank most land area still audience.','2021-05-22 00:43:57',8,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (199,'Congress method often customer situation executive cultural mean what position.','2021-05-13 22:31:12',8,38);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (200,'Education across yard two vote no south upon say.','2021-05-06 02:39:00',8,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (201,'Challenge measure avoid news pay stuff.','2021-05-04 20:47:33',9,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (202,'Enter energy example knowledge raise.','2021-05-25 01:13:32',9,49);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (203,'Item model possible on tough success strong.','2021-05-03 09:20:17',9,15);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (204,'Know her itself energy just eight deep sister increase unit.','2021-05-04 14:52:52',9,21);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (205,'Rise what open here I market send.','2021-05-10 05:25:56',9,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (206,'Bill central fast media can image fish later.','2021-05-16 23:07:42',9,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (207,'Return win natural with read want recent sea administration room.','2021-05-24 10:29:49',9,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (208,'Stay operation concern if take I paper recent security TV.','2021-05-16 16:18:05',9,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (209,'Popular final goal available else.','2021-05-20 11:07:03',9,28);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (210,'Instead agent begin letter add fall offer evening reflect.','2021-05-06 18:16:29',9,3);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (211,'Record system maintain media dream PM natural move maintain.','2021-05-02 17:40:19',9,10);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (212,'Direction I him candidate remain fish forward process across example beautiful.','2021-05-07 02:26:07',9,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (213,'And area local thus raise yeah produce theory action future strategy.','2021-05-24 07:49:01',9,23);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (214,'Toward always final necessary similar Democrat rise left.','2021-05-18 19:41:27',9,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (215,'Day opportunity know seem.','2021-05-11 05:33:44',9,4);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (216,'Easy school his whatever experience.','2021-05-03 00:15:42',9,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (217,'Tough here something reason letter little long magazine.','2021-05-17 13:55:21',9,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (218,'Training case heart moment should.','2021-05-16 06:56:29',9,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (219,'Keep mission most talk network reduce get member growth build which.','2021-05-04 17:35:04',9,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (220,'Sometimes serve throughout goal fact suddenly above society.','2021-05-05 14:13:14',9,46);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (221,'Try real teach statement job after environment.','2021-05-22 03:26:04',9,23);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (222,'Pull that special collection method source represent make.','2021-05-09 10:53:24',9,2);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (223,'Challenge structure call sense leg include.','2021-05-02 20:37:30',9,15);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (224,'Answer role whole concern assume national across wrong hotel.','2021-05-13 04:58:28',9,50);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (225,'Half before head upon size call light story.','2021-05-22 06:16:11',9,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (226,'Because program five pressure quality.','2021-05-12 03:26:43',10,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (227,'Somebody across modern street arm.','2021-05-03 04:45:02',10,39);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (228,'About water politics issue culture find.','2021-05-18 01:06:48',10,31);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (229,'Really strategy man party allow outside treatment over could.','2021-05-02 06:08:51',10,28);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (230,'Box energy task approach truth history.','2021-05-25 05:37:03',10,12);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (231,'Growth drive daughter realize opportunity write investment.','2021-05-11 07:58:45',10,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (232,'Miss Mrs Congress less eye rule trial.','2021-05-20 21:38:41',10,16);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (233,'Activity radio adult likely possible around environmental.','2021-05-05 04:37:23',10,14);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (234,'Oil stay find exist sing produce sea buy about.','2021-05-06 00:28:01',10,16);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (235,'Performance blue food lawyer close.','2021-05-15 06:41:38',10,6);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (236,'Behind as take market meeting yourself notice career case.','2021-05-09 18:14:55',10,50);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (237,'National structure ten him believe goal.','2021-05-14 13:44:56',10,16);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (238,'Dinner right material set instead shoulder wonder.','2021-05-21 18:52:04',10,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (239,'Democratic adult represent improve his reflect go sing.','2021-05-08 16:24:53',10,24);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (240,'Record operation set image enjoy field.','2021-05-12 19:09:54',10,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (241,'Catch rich trip lose.','2021-05-23 13:00:02',10,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (242,'Everyone difference say strong through.','2021-05-25 00:58:25',10,44);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (243,'Begin strong many history include similar former employee eye.','2021-05-03 05:22:45',10,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (244,'Should husband cut forget now.','2021-05-15 04:49:50',10,42);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (245,'Strong position increase number base wait many.','2021-05-20 20:25:21',10,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (246,'Vote we so available town may late car college range.','2021-05-06 17:41:12',10,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (247,'Tax effort respond describe this site commercial reality eight hotel.','2021-05-16 17:53:03',10,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (248,'Election particular year eight entire.','2021-05-16 23:34:15',10,10);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (249,'Coach future turn former writer guess stay choose present.','2021-05-13 00:57:16',10,18);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (250,'Wind environment long thank trouble.','2021-05-04 23:27:59',10,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (251,'Son system final establish answer.','2021-05-09 20:10:48',11,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (252,'Policy similar focus so wrong Republican audience line.','2021-05-16 22:11:44',11,29);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (253,'National create without reveal course support whole newspaper director.','2021-05-07 09:39:52',11,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (254,'Group nothing soldier assume her ok might no write.','2021-05-22 09:05:26',11,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (255,'Others spend live central.','2021-05-15 01:31:02',11,46);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (256,'Return population care away stage.','2021-05-13 16:09:34',11,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (257,'Congress after star maybe member generation clear national red.','2021-05-19 10:35:35',11,23);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (258,'Popular husband less civil customer issue mouth position network particularly.','2021-05-24 16:39:17',11,19);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (259,'Four performance what else box state try.','2021-05-20 20:40:58',11,10);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (260,'Similar pick church all.','2021-05-10 20:00:50',11,3);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (261,'Cold herself beat positive fire least professional song hold.','2021-05-10 01:14:52',11,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (262,'Occur return national data outside office discuss way mission.','2021-05-02 11:30:30',11,47);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (263,'Consider realize fish wall sing information through low care instead.','2021-05-02 02:24:12',11,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (264,'A expect during treat heart option receive benefit.','2021-05-01 08:47:02',11,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (265,'Indeed or general often agreement sing public data.','2021-05-09 06:52:10',11,23);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (266,'Second decision rather once investment.','2021-05-11 05:28:41',11,33);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (267,'Born we black article others boy must computer.','2021-05-09 14:24:23',11,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (268,'Yeah company service bed thus never.','2021-05-06 02:47:49',11,6);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (269,'Goal live significant move debate their her foreign.','2021-05-06 10:59:23',11,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (270,'Maybe however former ask property raise travel.','2021-05-17 00:38:03',11,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (271,'Election there exactly place necessary whose firm.','2021-05-09 00:00:16',11,12);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (272,'Short worker away fire when bar door former magazine go.','2021-05-13 08:09:05',11,18);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (273,'Born wonder somebody matter available computer try season cut arm.','2021-05-05 00:38:44',11,35);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (274,'Region surface unit onto chance.','2021-05-21 05:06:09',11,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (275,'Day sit leg appear about certainly ok from Republican.','2021-05-21 16:36:47',11,28);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (276,'Reach key win throughout hope before level ten vote reflect.','2021-05-14 20:56:30',12,38);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (277,'Interesting miss spend man six.','2021-05-20 08:21:59',12,30);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (278,'Professional author bring green fine Mrs cup wear happen.','2021-05-06 17:07:23',12,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (279,'Create authority none Mr baby.','2021-05-08 00:48:48',12,32);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (280,'Put total quite anyone vote out window.','2021-05-18 00:01:03',12,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (281,'Able air wide visit recent brother grow history.','2021-05-12 12:38:54',12,45);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (282,'Really politics hour the trouble than boy visit support.','2021-05-11 09:42:55',12,50);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (283,'History oil establish receive single establish step while.','2021-05-21 10:46:41',12,8);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (284,'Recognize election kitchen coach small effect other.','2021-05-12 01:24:00',12,28);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (285,'Choice what relate pressure bar social new receive.','2021-05-10 19:18:57',12,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (286,'Another building father space successful treat.','2021-05-20 23:39:04',12,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (287,'Personal laugh night former fine her mention imagine sort reflect.','2021-05-23 04:58:25',12,6);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (288,'Agree put page necessary sometimes mention want.','2021-05-06 05:36:28',12,40);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (289,'Partner be according Republican tell if feeling.','2021-05-11 20:18:03',12,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (290,'Mean adult person letter body individual.','2021-05-16 00:29:01',12,3);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (291,'Any air indeed couple.','2021-05-05 03:04:06',12,22);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (292,'Ahead rich off what last leave.','2021-05-03 04:44:11',12,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (293,'Paper activity trip think least with mission network agreement site.','2021-05-08 01:42:47',12,17);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (294,'Despite bill by become.','2021-05-16 20:01:27',12,45);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (295,'Ago expert population relationship artist.','2021-05-18 21:27:19',12,43);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (296,'Everything into second ahead type technology method scene environmental ready.','2021-05-22 00:18:15',12,41);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (297,'Research some be when easy environmental.','2021-05-10 16:26:04',12,7);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (298,'Create guess free seek put everybody rather experience letter discussion.','2021-05-04 13:49:46',12,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (299,'Give sign religious data rate.','2021-05-21 12:38:11',12,9);
INSERT INTO "app_comment" ("id","body","created","thread_id","user_id") VALUES (300,'Unit different wall before over section.','2021-05-06 11:02:29',12,33);

DROP INDEX IF EXISTS "app_thread_creator_id_idx";
CREATE INDEX "app_thread_creator_id_idx" ON "app_thread" ("creator_id");

DROP INDEX IF EXISTS "app_comment_thread_id_idx";
CREATE INDEX IF NOT EXISTS "app_comment_thread_id_idx" ON "app_comment" ("thread_id");

DROP INDEX IF EXISTS "app_comment_user_id_idx";
CREATE INDEX IF NOT EXISTS "app_comment_user_id_idx" ON "app_comment" ("user_id");

DROP INDEX IF EXISTS "app_group_user_group_id_idx";
CREATE INDEX IF NOT EXISTS "app_group_user_group_id_idx" ON "app_group_user" ("group_id");

DROP INDEX IF EXISTS "app_group_user_user_id_idx";
CREATE INDEX IF NOT EXISTS "app_group_user_user_id_idx" ON "app_group_user" ("user_id");

DROP INDEX IF EXISTS "app_group_user_group_id_user_id_idx_uniq";
CREATE UNIQUE INDEX IF NOT EXISTS "app_group_user_group_id_user_id_idx_uniq" ON "app_group_user" ("group_id","user_id");

DROP VIEW IF EXISTS "top_10_users_view";
CREATE VIEW "top_10_users_view" AS
SELECT
  t1.user_id,
  t2.first_name,
  t2.last_name,
  t2.email,
  COUNT(*) AS cnt
FROM
  app_comment AS t1
  LEFT JOIN app_user AS t2 ON t1.user_id = t2.id
GROUP BY
  user_id
ORDER BY
  cnt DESC,
  t2.first_name
LIMIT
  10;

COMMIT;