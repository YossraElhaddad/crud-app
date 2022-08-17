# crud-app

The app automatically loads the departments (master) which consists of employees (details).

When a department is deleted, all employees who work at that department are deleted.

When adding an employee, it is only allowed to add the department (which the employee works at) from the list of departments database.
Same goes for adding title, since there are only specific titles.


## Database design

### PSQL queries (inital data)

```
CREATE TABLE Departments(
    id INT GENERATED ALWAYS AS IDENTITY,
    name varchar(50) UNIQUE NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO Departments(name) VALUES ('Software');
INSERT INTO Departments(name) VALUES ('Marketing');
INSERT INTO Departments(name) VALUES ('Human Resources');
INSERT INTO Departments(name) VALUES ('Public Relations');
INSERT INTO Departments(name) VALUES ('Accounting');


CREATE TABLE Salaries(
    employee_title VARCHAR(50) NOT NULL,
    title_salary INT,
    PRIMARY KEY(employee_title)
);

INSERT INTO Salaries(employee_title, title_salary) VALUES ('Junior', 4000);
INSERT INTO Salaries(employee_title, title_salary) VALUES ('Mid-Senior', 7500);
INSERT INTO Salaries(employee_title, title_salary) VALUES ('Senior', 10000);



CREATE TABLE Employees(
    id INT GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(50) NOT NULL,
    title VARCHAR(50) NOT NULL,
    salary INT ,
    years_of_experience INT,
    dept_id INT NOT NULL,
    PRIMARY KEY(id),

    CONSTRAINT fk_department
    FOREIGN KEY(dept_id) REFERENCES Departments(id)
    ON DELETE CASCADE,

    CONSTRAINT fk_salary
    FOREIGN KEY(title) REFERENCES Salaries(employee_title)
    ON DELETE SET NULL
    
);

INSERT INTO EMPLOYEES(name, title, salary, years_of_experience, dept_id) VALUES('Mohamed', 'Junior',3500, 2, 1);

INSERT INTO EMPLOYEES(name, title, salary, years_of_experience, dept_id) VALUES('Mohamed', 'Senior',15000, 7, 1);

INSERT INTO EMPLOYEES(name, title, salary, years_of_experience, dept_id) VALUES('Mohamed', 'Mid-Senior', 7000, 1, 1);

INSERT INTO EMPLOYEES(name, title, salary, years_of_experience, dept_id) VALUES('Mohamed', 'Mid-Senior', 6000, 4, 2);

```

### Relationship between Salary, years of experience, and title

I came up with an equation that binds the relationship, which is:

there is a salary which is based on title, and it gets modified depending on the years of experience,

assuming years of experience is x:

1- if title is junior,
   then expected_salary = junior_salary + x * 1000

2- if title is mid senior,
   then expected_salary = mid_senior_salary + x * 1000

3- if title is senior,
   then expected_salary = senior_salary + x * 1000

There will be a Table called Salaries, with attributes title and the corresponding salary.
