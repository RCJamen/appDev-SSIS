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
photo VARCHAR(255),
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

INSERT INTO `students`(`id`,`photo`, `firstname`, `lastname`, `coursecode`, `year`, `gender`)
VALUES
    ('2028-1001', 'https://res.cloudinary.com/db52qexfl/image/upload/v1700200973/cld-sample-4.jpg', 'John Alice', 'Smith', 'BSA', '1', 'Female'),
    ('2028-1002', 'https://res.cloudinary.com/db52qexfl/image/upload/v1700200973/cld-sample-4.jpg', 'Robert Bob', 'Johnson', 'BSCE', '2', 'Male'),
    ('2028-1003', 'https://res.cloudinary.com/db52qexfl/image/upload/v1700200973/cld-sample-4.jpg', 'Michael Charlie', 'Davis', 'BSCS', '3', 'Others');