"""
Database:
A database is an organized collection of structured information, or data, stored
in our local system.Together, the data and the DBMS, along with the applications that are associated with them,
are referred to as a database system, often shortened to just database.

DBMS:
Database Management Systems (DBMS) are used to store, retrieve, and run queries on data.
A DBMS serves as an interface between an end-user and a database, allowing users to create, read, update,
and delete data in the database.

DBMS manage the data, the database engine, and the database schema, allowing for data to be manipulated
or extracted by users and other programs. This helps provide data security, data integrity, concurrency,
and uniform data administration procedures.


what is progresSQL ?

It is a highly stable database management system, backed by more than 20 years of community development
which has contributed to its high levels of resilience, integrity, and correctness. PostgreSQL is used as
the primary data store or data warehouse for many web, mobile, geospatial, and analytics applications.

What is difference between SQL and PostgreSQL?

SQL server is a database management system which is mainly used for e-commerce and providing different data
warehousing solutions.
PostgreSQL is an advanced version of SQL which provides support to different functions of SQL like
foreign keys, sub queries, triggers, and different user-defined types and functions.

What is OLAP?

Online Analytical Processing, a category of software tools which provide analysis of data for business decisions.
OLAP systems allow users to analyze database information from multiple database systems at one time.
The primary objective is data analysis and not data processing.

What is OLTP?

Online transaction processing shortly known as OLTP supports transaction-oriented applications in a 3-tier
architecture. OLTP administers day to day transaction of an organization.

Application developer tools: sql-dev, oracle designer, oracle developer, sqlplus, pl/sql. postgresql

Data types:

1.Numeric: int, float, decimal, number
2.cheracter/string: char, varchar, varchar(2),
  char - predefined length upto 2000 bytes
  varchar-
  varchar(2) - upto 4000 bytes

Types of languages in sql/ postgresql

1.DDl - Data Defination Language
  create: create table <name> (name varchar(30), age integer)
  alter: alter table  which makes add or delete columns
  drop : removes the entire table from data base

2.DML - Data manupulation Language
  insert: to insert data into row wise row wise
  update: to update the data in table of specific item
  delete : to delete the data in table of speccific item or entire row data.

3.DRL: Data Retrieval language
  select : using select * from table retrieves the data
4.TCL: Transaction control
  roll back: which makes you return the changes done
  commit: It makes the changes done in table saved and not able rollback
  save : It makes save the changes done and you can roll back or commit here.

CREATE TABLE student1(
student1_name varchar(25),
student1_id varchar(25),
student1_mobile varchar(25),
student1_marks integer,
student1_fathername varchar(25),
student1_place varchar(25)
);
INSERT INTO student1 VALUES('mahindra','124g1a0131','9652265878',450,'ramu','anantapur');
INSERT INTO student1 VALUES('kishore','124g1a0132','7965326415',562, 'shyam','anantapur');
SELECT * FROM student1;

INSERT INTO student1 VALUES('kishore','124g1a0132','9658456465',632,'hari','anantapur');
INSERT INTO student1 VALUES('krishna','124g1a0133','7896541231',785,'varma','anantapur');
INSERT INTO student1 VALUES('vinay','124g1a0134','9656878456',564,'kiran','anantapur');
SELECT * FROM student1;

DELETE FROM student1 WHERE student1_marks = 632;
DELETE FROM student1 WHERE student1_name = 'krishna';
DELETE FROM student1 WHERE student1_fathername = 'kiran';
SELECT * FROM student1;

DROP TABLE student1;
SELECT * FROM student1;

ALTER TABLE student1 ADD COLUMN student1_email  varchar(50);
select student1_email from student1;


UPDATE student1 SET student1_email='mahi@gmail.com' WHERE student1_name = 'mahindra';
select * from student1;
UPDATE student1 SET student1_email = 'ki1234@gmail.com' WHERE student1_name='kishore';
UPDATE student1 SET student1_email = 'krishnam@gmail.com' WHERE student1_id = '124g1a0133';
UPDATE student1 SET student1_email = 'vinay456@gmail.com' WHERE student1_marks = 564;
select student1_email FROM student1;


CREATE TABLE student1_copy AS SELECT * FROM student1 WHERE 1 = 1;
SELECT * from student1_copy;


DROP TABLE student1_copy;

CREATE TABLE emp_details(
name varchar(25),
eid integer,
designation varchar(25),
salary integer);
select * from emp_details;

INSERT INTO emp_details values('surya', 11250, 'manager',15000);

INSERT INTO emp_details VALUES('varma',11251, 'manager',15500);
INSERT INTO emp_details VALUES('kalyan',11252,'manager',15500);
INSERT INTO emp_details VALUES('sharma',11253,'manager',15560);
INSERT INTO emp_details VALUES('vihan',10256,'engineer',12000);
INSERT INTO emp_details VALUES('vikram',10258,'engineer',12500);
INSERT INTO emp_details VALUES('vishali',10259,'hr',10000);

SELECT*FROM emp_details;

INSERT INTO emp_details VALUES('sreekanth',10267,'hr',10200);

INSERT INTO emp_details VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_details VALUES('kiran',10269,'supervisor',8000);
SELECT * FROM emp_details;

DELETE FROM emp_details WHERE eid = 10268;
DELETE FROM emp_details WHERE name = 'kiran';
SELECT*FROM emp_details;

INSERT INTO emp_details VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_details VALUES('kiran',10269,'supervisor',8000);
SELECT * FROM emp_details;

SELECT * FROM emp_details;

ALTER TABLE emp_details ADD COLUMN place varchar(15);
ALTER TABLE emp_details ADD COLUMN email varchar(25);
ALTER TABLE emp_details ADD COLUMN benefits integer;
ALTER TABLE emp_details ADD COLUMN bonus integer;

SELECT * FROM emp_details;

ALTER TABLE emp_details drop column place;
SELECT * FROM emp_details;

ALTER TABLE emp_details drop column email;
ALTER TABLE emp_details DROP COLUMN bonus;
ALTER TABLE emp_details DROP COLUMN benefits;


SELECT * FROM emp_details;


UPDATE emp_details SET salary = 10100 where name ='kiran';
select * from emp_details;

CREATE TABLE emp_details_copy as SELECT * FROM  emp_details;
ALTER TABLE emp_details_copy ADD COLUMN branch varchar(50);
select * from emp_details_copy;
DROP TABLE emp_details_copy;


INSERT INTO emp_details values('mani',12345,'engineer',12000);
UPDATE emp_details SET salary = 12500 WHERE name = 'mani';
SELECT * FROM emp_details;
DELETE FROM emp_details where name = 'mani';
SELECT * FROM emp_details;

SELECT name,eid,designation,salary from emp_details WHERE designation = 'hr';
SELECT name,eid,designation from emp_details where salary < 12000;
SELECT name,eid,designation from emp_details where salary > 12000;
SELECT name,eid,salary from emp_details where designation = 'manager';
SELECT name,eid,salary from emp_details where designation = 'supervisor';
SELECT sum(salary) total_sal from emp_details;

SELECT sum(salary) hr_sal from emp_details where designation = 'hr';
SELECT sum(salary) manager_sal from emp_details where designation = 'manager';
SELECT SUM(salary) supervisor_sal from emp_details where designation = 'supervisor';

SELECT * from emp_details;
SELECT sum(salary) engineer_sal from emp_details where designation = 'engineer';
SELECT name,designation,salary from emp_details where name LIKE '%a%';
SELECT name,designation,salary from emp_details where name LIKE '%r%';
SELECT name,designation,salary from emp_details where name LIKE '_u%';
SELECT name,designation,salary from emp_details where designation Like 'm%';
SELECT name,designation,salary from emp_details where designation LIKE '%n%';

SELECT name,designation,salary from emp_details where designation LIKE '%e__';
SELECT name,eid,designation,salary from emp_details where designation LIKE '%e_';
SELECT name,eid,designation,salary from emp_details where name LIKE '__l%';
SELECT name,eid,designation,salary from emp_details where name LIKE '%h%';
---REQUIREMENT
---employee name start with letter s
SELECT name, eid,designation,salary from emp_details where name LIKE 's%';
SELect name, eid,salary from emp_details where name LIKE 'k%';

--employee name start with second letter h
SELECT name,eid,salary from emp_details where name LIKE '_h%';
SELECT name,eid,salary from emp_details where name LIKE '_a%';

--employee name start with third letter r
SELECT name,eid,salary from emp_details where name LIKE '__r%';
SELECT name,eid,salary from emp_details where name LIKE '__l%';

---employee name start with fourth letter y
SELECT name,eid salary from emp_details where name LIKE '___y%';

---employee name start with fifth letter
SELECT name,eid ,salary from emp_details where name LIKE '____a%'

--employee name with letter a
SELECT name,eid,salary from emp_details where name LIKE '%a%';

employee name end with letter a
SELECT name,eid,salary from emp_details where name LIKE '%a';
SELECT name,eid,salary from emp_details where name LIKE '%n';

---employee name end with second letter a
SELECT name,eid,salary from emp_details where name LIKE '%a_';
SELECT name,eid,salary from emp_details where name LIKE '%m_';

---(Using underscore(_)).It represents single character
Requirement:-
--display employee details and employee name third character from last should be
letter "r".
SELECT name,eid,salary from emp_details where name LIKE '%r__';

--display employee details and employee name 4rth  character from last should be
letter "a".
SELECT name,eid,salary from emp_details where name LIKE '%a___';

-----------------

CREATE TABLE emp_details(
name varchar(25),
eid integer,
designation varchar(25),
salary integer);
select * from emp_details;

INSERT INTO emp_details values('surya', 11250, 'manager',15000);

INSERT INTO emp_details VALUES('varma',11251, 'manager',15500);
INSERT INTO emp_details VALUES('kalyan',11252,'manager',15500);
INSERT INTO emp_details VALUES('sharma',11253,'manager',15560);
INSERT INTO emp_details VALUES('vihan',10256,'engineer',12000);
INSERT INTO emp_details VALUES('vikram',10258,'engineer',12500);
INSERT INTO emp_details VALUES('vishali',10259,'hr',10000);

SELECT*FROM emp_details;

INSERT INTO emp_details VALUES('sreekanth',10267,'hr',10200);

INSERT INTO emp_details VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_details VALUES('kiran',10269,'supervisor',8000);
SELECT * FROM emp_details;

DELETE FROM emp_details WHERE eid = 10268;
DELETE FROM emp_details WHERE name = 'kiran';
SELECT*FROM emp_details;

INSERT INTO emp_details VALUES('ishaan',10268,'supervisor',8500);
INSERT INTO emp_details VALUES('kiran',10269,'supervisor',8000);
SELECT * FROM emp_details;

SELECT * FROM emp_details;

ALTER TABLE emp_details ADD COLUMN place varchar(15);
ALTER TABLE emp_details ADD COLUMN email varchar(25);
ALTER TABLE emp_details ADD COLUMN benefits integer;
ALTER TABLE emp_details ADD COLUMN bonus integer;

SELECT * FROM emp_details;

ALTER TABLE emp_details drop column place;
SELECT * FROM emp_details;

ALTER TABLE emp_details drop column email;
ALTER TABLE emp_details DROP COLUMN bonus;
ALTER TABLE emp_details DROP COLUMN benefits;


SELECT * FROM emp_details;


UPDATE emp_details SET salary = 10100 where name ='kiran';
select * from emp_details;

CREATE TABLE emp_details_copy as SELECT * FROM  emp_details;
ALTER TABLE emp_details_copy ADD COLUMN branch varchar(50);
select * from emp_details_copy;
DROP TABLE emp_details_copy;


INSERT INTO emp_details values('mani',12345,'engineer',12000);
UPDATE emp_details SET salary = 12500 WHERE name = 'mani';
SELECT * FROM emp_details;
DELETE FROM emp_details where name = 'mani';
SELECT * FROM emp_details;

SELECT name,eid,designation,salary from emp_details WHERE designation = 'hr';
SELECT name,eid,designation from emp_details where salary < 12000;
SELECT name,eid,designation from emp_details where salary > 12000;
SELECT name,eid,salary from emp_details where designation = 'manager';
SELECT name,eid,salary from emp_details where designation = 'supervisor';
SELECT sum(salary) total_sal from emp_details;

SELECT sum(salary) hr_sal from emp_details where designation = 'hr';
SELECT sum(salary) manager_sal from emp_details where designation = 'manager';
SELECT SUM(salary) supervisor_sal from emp_details where designation = 'supervisor';

SELECT * from emp_details;
SELECT sum(salary) engineer_sal from emp_details where designation = 'engineer';
SELECT name,designation,salary from emp_details where name LIKE '%a%';
SELECT name,designation,salary from emp_details where name LIKE '%r%';
SELECT name,designation,salary from emp_details where name LIKE '_u%';
SELECT name,designation,salary from emp_details where designation Like 'm%';
SELECT name,designation,salary from emp_details where designation LIKE '%n%';

SELECT name,designation,salary from emp_details where designation LIKE '%e__';
SELECT name,eid,designation,salary from emp_details where designation LIKE '%e_';
SELECT name,eid,designation,salary from emp_details where name LIKE '__l%';
SELECT name,eid,designation,salary from emp_details where name LIKE '%h%';
---REQUIREMENT
---employee name start with letter s
SELECT name, eid,designation,salary from emp_details where name LIKE 's%';
SELect name, eid,salary from emp_details where name LIKE 'k%';

--employee name start with second letter h
SELECT name,eid,salary from emp_details where name LIKE '_h%';
SELECT name,eid,salary from emp_details where name LIKE '_a%';

--employee name start with third letter r
SELECT name,eid,salary from emp_details where name LIKE '__r%';
SELECT name,eid,salary from emp_details where name LIKE '__l%';

---employee name start with fourth letter y
SELECT name,eid salary from emp_details where name LIKE '___y%';

---employee name start with fifth letter
SELECT name,eid ,salary from emp_details where name LIKE '____a%'

--employee name with letter a
SELECT name,eid,salary from emp_details where name LIKE '%a%';

employee name end with letter a
SELECT name,eid,salary from emp_details where name LIKE '%a';
SELECT name,eid,salary from emp_details where name LIKE '%n';

---employee name end with second letter a
SELECT name,eid,salary from emp_details where name LIKE '%a_';
SELECT name,eid,salary from emp_details where name LIKE '%m_';

---(Using underscore(_)).It represents single character
Requirement:-
--display employee details and employee name third character from last should be
letter "r".
SELECT name,eid,salary from emp_details where name LIKE '%r__';

--display employee details and employee name 4rth  character from last should be
letter "a".
SELECT name,eid,salary from emp_details where name LIKE '%a___';
                                                                       

"""
