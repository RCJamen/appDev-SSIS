DROP DATABASE IF EXISTS `ssis_web`;
CREATE DATABASE IF NOT EXISTS `ssis_web`;
use `ssis_web`;

DROP TABLE IF EXISTS `colleges`;
CREATE TABLE IF NOT EXISTS `colleges`(
code VARCHAR(10) NOT NULL,
name VARCHAR(50) NOT NULL,
PRIMARY KEY(code)
);

DROP TABLE IF EXISTS `courses`;
CREATE TABLE IF NOT EXISTS `courses`(
code VARCHAR(10) NOT NULL,
name VARCHAR(50) NOT NULL,
collegecode VARCHAR(10) NOT NULL,
PRIMARY KEY(code),
FOREIGN KEY(collegecode) REFERENCES colleges(code)
);

DROP TABLE IF EXISTS `students`;
CREATE TABLE IF NOT EXISTS `students`(
id VARCHAR(9) NOT NULL,
firstname VARCHAR(50) NOT NULL,
lastname VARCHAR(20) NOT NULL,
coursecode VARCHAR(10) NOT NULL,
year INT(1) NOT NULL,
gender VARCHAR(10) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY(coursecode) REFERENCES courses(code)
);

INSERT INTO `colleges`(`code`, `name`)
VALUES ('CCS', 'College of Computer Studies'),
	('CSM', 'College of Science and Mathematics'),
	('COET', 'College of Engineering and Technology'),
	('CASS', 'College of Arts and Social Sciences'),
	('CEBA', 'College of Economics and Business Administration');
	
INSERT INTO `courses`(`code`, `name`, `collegecode`)
VALUES ('BSCS', 'Bachelor of Science in Computer Science', 'CCS'),
		('BSA', 'Bachelor of Science in Accountancy', 'CEBA'),
		('BSM', 'Bachelor of Science in Mathematics', 'CSM'),
		('BSCE', 'Bachelor of Science in Civil Engineering', 'COET'),
		('BSP', 'Bachelor of Science in Philosophy', 'CASS');

INSERT INTO `students`(`id`, `firstname`, `lastname`,`coursecode`,`year`,`gender`) 
VALUES ('2019-2093','Ramel Cary','Jamen','BSCS','1','Male'),
		('2019-0523','Edward Vincent','Escasio','BSCE','4','Male'),
		('2018-5069','Edward James','Bongo','BSA','3','Male'),
		('2019-2932','Kenneth Martin','Gagno','BSM','4','Male');