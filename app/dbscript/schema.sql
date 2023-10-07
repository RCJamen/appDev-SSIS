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
       ('CASS', 'College of Arts and Social Sciences'),
       ('CON', 'College of Nursing');

INSERT INTO `courses`(`code`, `name`, `collegecode`)
VALUES ('BSCS', 'Bachelor of Science in Computer Science', 'CCS'),
       ('BSIS', 'Bachelor of Science in Information System', 'CCS'),
       ('BSN', 'Bachelor of Science in Nursing', 'CON'),
       ('BSM', 'Bachelor of Science in Mathematics', 'CSM');

INSERT INTO `students`(`id`, `firstname`, `lastname`,`coursecode`,`year`,`gender`) VALUES ('2019-2093','Ramel Cary','Jamen','BSCS','1','Male');