--Q1
Create table student (rollno varchar(50), name varchar(500), course varchar(200));

--Q2
Insert into student (rollno, name, course) values ('1P22', 'suresh', 'Python');
Insert into student (rollno, name, course) values ('1J22', 'Ramesh', 'Java');
Insert into student (rollno, name, course) values ('2P22', 'Harish', 'Python');
Insert into student (rollno, name, course) values ('1JS22', 'suresh', 'JavaScript');

--Q3
select * from student;

--Q4
Update student set name = 'Mohan' where rollno ='1JS22';

--Q5
Delete from student where rollno ='1JS22';

--Q6
Truncate student;

--Q7
drop table student;

--Q8
create table Courses (cid int2, cname varchar(50), 
constraint course_pk primary key(cid));

Create table student (rollno varchar(50), name varchar(500), cid int2,
CONSTRAINT student_pk primary key(rollno), CONSTRAINT student_fk foreign key (cid) REFERENCES Courses(cid));

--Q9
Insert into Courses (cid, cname) values (1, 'Python');
Insert into Courses (cid, cname) values (2, 'Java');
Insert into Courses (cid, cname) values (3, 'JavaScript');
Insert into Courses (cid, cname) values (4, 'C');

Insert into student (rollno, name, cid) values ('1P22', 'suresh', 1);
Insert into student (rollno, name, cid) values ('1J22', 'Ramesh', 1);
Insert into student (rollno, name, cid) values ('2P22', 'Harish', 3);
Insert into student (rollno, name, cid) values ('1JS22', 'suresh', 2);


--Q10
Select * from student where cid = (select cid from courses where cname ='Python')