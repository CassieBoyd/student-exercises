-- DROP TABLE IF EXISTS Cohort;
-- DROP TABLE IF EXISTS StudentExercises;

CREATE TABLE 'Cohort' (
    'id'	   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    'name'   TEXT NOT NULL UNIQUE
);

CREATE TABLE 'Student' (
	'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'first_name'	TEXT NOT NULL,
	'last_name'		TEXT NOT NULL,
	'slack_handle' 	TEXT NOT NULL UNIQUE,
	'cohort_id'		INTEGER,
	FOREIGN KEY('cohort_id') REFERENCES 'Cohort'('cohort_id')
);

CREATE TABLE 'Instructor' (
	'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'first_name'	TEXT NOT NULL,
	'last_name'		TEXT NOT NULL,
	'slack_handle' 	TEXT NOT NULL UNIQUE,
	'specialty'		TEXT NOT NULL,
	'cohort_id'		INTEGER,
	FOREIGN KEY('cohort_id') REFERENCES 'Cohort'('cohort_id')
);

CREATE TABLE 'Exercises' (
	'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'name'	TEXT NOT NULL,
	'language'	TEXT NOT NULL
);

CREATE TABLE 'StudentExercises' (
	'id'	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	'student_id'	INTEGER,
	'exercise_id'		INTEGER,
	FOREIGN KEY('student_id') REFERENCES 'Student'('id'),
	FOREIGN KEY('exercise_id') REFERENCES 'Exercise'('id')
);

INSERT INTO Cohort
VALUES (null, 'Cohort 36');

INSERT INTO Cohort
VALUES (null, 'Cohort 37');

INSERT INTO Cohort
VALUES (null, 'Cohort 38');

INSERT INTO Exercises
VALUES (null, 'Four and Twenty', 'Python');

INSERT INTO Exercises
VALUES (null, 'Sunshine Superman', 'JavaScript');

INSERT INTO Exercises
VALUES (null, 'Killer Queen', 'HTML');

INSERT INTO Exercises
VALUES (null, 'Incense and Peppermints', 'Python');

INSERT INTO Exercises
VALUES (null, 'Slow Burn', 'Python');

INSERT INTO Instructor
VALUES (null, 'Nariyoshi', 'Miyagi', 'Mr.Miyagi', 'Crane Kick', 1);

INSERT INTO Instructor
VALUES (null, 'John', 'Kreese', 'NoMercy', 'Sweep The Leg', 2);

INSERT INTO Instructor
VALUES (null, 'Frank', 'Furter', 'Sw337_7ransv3s7173', 'The Time Warp', 3);

INSERT INTO Student
VALUES (null, 'Daniel', 'LaRusso', 'Daniel-san', 1);

INSERT INTO Student
VALUES (null, 'Johnny', 'Lawrence', 'L3g5w33p3r', 2);

INSERT INTO Student
VALUES (null, 'John', 'Doe', 'DoeBoi', 3);

INSERT INTO Student
VALUES (null, 'Janet', 'Doe', 'DammitJanet', 1);

INSERT INTO Student
VALUES (null, 'Freddie', 'Mercury', 'LoverBoi', 2);

INSERT INTO Student
VALUES (null, 'David', 'Bowie', 'StarMan', 3);

INSERT INTO Student
VALUES (null, 'Harry', 'Potter', 'BoyWhoLived', 1);

INSERT INTO StudentExercises
VALUES (null, 1, 1);

INSERT INTO StudentExercises
VALUES (null, 1, 2);

INSERT INTO StudentExercises
VALUES (null, 2, 1);

INSERT INTO StudentExercises
VALUES (null, 2, 3);

INSERT INTO StudentExercises
VALUES (null, 3, 5);

INSERT INTO StudentExercises
VALUES (null, 3, 4);

INSERT INTO StudentExercises
VALUES (null, 4, 4);

INSERT INTO StudentExercises
VALUES (null, 4, 3);

INSERT INTO StudentExercises
VALUES (null, 5, 2);

INSERT INTO StudentExercises
VALUES (null, 5, 5);

INSERT INTO StudentExercises
VALUES (null, 6, 4);

INSERT INTO StudentExercises
VALUES (null, 6, 1);

INSERT INTO StudentExercises
VALUES (null, 7, 2);

INSERT INTO StudentExercises
VALUES (null, 7, 3);
