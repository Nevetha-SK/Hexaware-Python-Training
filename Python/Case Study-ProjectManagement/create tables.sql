----------Create Tables for ProjectManagement DB----------
--Create Project table
CREATE TABLE dbo.Project (
  id INT PRIMARY KEY,
  project_name VARCHAR(100) NOT NULL,
  description TEXT NULL,
  start_date DATE NULL,
  status VARCHAR(20) NOT NULL
    CHECK(status IN ('started','dev','build','test','deployed'))
);

--Create Employee table
CREATE TABLE dbo.Employee (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  designation VARCHAR(100) NULL,
  gender VARCHAR(10) NULL,
  salary FLOAT NULL,
  project_id INT NULL,
  FOREIGN KEY (project_id) REFERENCES dbo.Project(id)
);
drop table if exists dbo.Task;
--Create Task table
CREATE TABLE dbo.Task (
  task_id INT PRIMARY KEY,
  task_name VARCHAR(100) NOT NULL,
  project_id INT NULL,
  employee_id INT,
  status VARCHAR(20)
    CHECK(status IN ('Assigned','Started','Completed')),
  FOREIGN KEY (project_id) REFERENCES dbo.Project(id),
  FOREIGN KEY (employee_id) REFERENCES dbo.Employee(id)
);

SELECT * FROM Employee WHERE id = 100; --Added an Employee
SELECT * FROM Project WHERE id = 200;  --Added  Project
SELECT * FROM Task WHERE task_id = 300; --Added Task


DELETE FROM Task WHERE employee_id = 100;
DELETE FROM Employee WHERE id = 100;

DELETE FROM Task WHERE project_id = 200;
DELETE FROM Project WHERE id = 200;



----------TestDB Create Tables----------

--Drop tables if they exist
DROP TABLE IF EXISTS dbo.Task;
DROP TABLE IF EXISTS dbo.Employee;
DROP TABLE IF EXISTS dbo.Project;
GO

--Create Project table
CREATE TABLE dbo.Project (
  id INT PRIMARY KEY,
  project_name VARCHAR(100) NOT NULL,
  description TEXT NULL,
  start_date DATE NULL,
  status VARCHAR(20) NOT NULL
    CHECK(status IN ('started','dev','build','test','deployed'))
);

--Create Employee table
CREATE TABLE dbo.Employee (
  id INT PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  designation VARCHAR(100) NULL,
  gender VARCHAR(10) NULL,
  salary FLOAT NULL,
  project_id INT NULL,
  FOREIGN KEY (project_id) REFERENCES dbo.Project(id)
    ON DELETE SET NULL
);

--Create Task table (with nullable project_id)
CREATE TABLE dbo.Task (
  task_id INT PRIMARY KEY,
  task_name VARCHAR(100) NOT NULL,
  project_id INT NULL,
  employee_id INT NULL,
  status VARCHAR(20) NULL
    CHECK(status IN ('Assigned','Started','Completed')),
  FOREIGN KEY (project_id) REFERENCES dbo.Project(id)
    ON DELETE SET NULL,
  FOREIGN KEY (employee_id) REFERENCES dbo.Employee(id)
    ON DELETE CASCADE
);
