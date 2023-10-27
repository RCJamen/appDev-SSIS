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

INSERT INTO `students`(`id`, `firstname`, `lastname`, `coursecode`, `year`, `gender`)
VALUES
    ('2028-1001', 'John Alice', 'Smith', 'BSA', '1', 'Female'),
    ('2028-1002', 'Robert Bob', 'Johnson', 'BSCE', '2', 'Male'),
    ('2028-1003', 'Michael Charlie', 'Davis', 'BSCS', '3', 'Others'),
    ('2028-1004', 'David John', 'Anderson', 'BSM', '4', 'Male'),
    ('2028-1005', 'Emily James', 'Brown', 'BSP', '1', 'Female'),
    ('2028-1006', 'William Frank', 'Lee', 'BSA', '2', 'Male'),
    ('2028-1007', 'Mary Grace', 'Wilson', 'BSCE', '3', 'Female'),
    ('2028-1008', 'James Henry', 'Garcia', 'BSCS', '4', 'Male'),
    ('2028-1009', 'Linda Ivy', 'Hernandez', 'BSM', '1', 'Female'),
    ('2028-1010', 'Robert Jack', 'Martinez', 'BSP', '2', 'Male'),
    ('2028-1011', 'Mary Katherine', 'Lopez', 'BSA', '3', 'Female'),
    ('2028-1012', 'John Leo', 'Taylor', 'BSCE', '4', 'Male'),
    ('2028-1013', 'David Mia', 'Rodriguez', 'BSCS', '1', 'Female'),
    ('2028-1014', 'Sarah Nathan', 'Harris', 'BSM', '2', 'Male'),
    ('2028-1015', 'John Olivia', 'Thomas', 'BSP', '3', 'Female'),
    ('2028-1016', 'William Peter', 'Smith', 'BSA', '4', 'Male'),
    ('2028-1017', 'Nancy Quinn', 'Johnson', 'BSCE', '1', 'Female'),
    ('2028-1018', 'Michael Robert', 'Davis', 'BSCS', '2', 'Male'),
    ('2028-1019', 'Emily Samantha', 'Anderson', 'BSM', '3', 'Female'),
    ('2028-1020', 'David Thomas', 'Brown', 'BSP', '4', 'Male');