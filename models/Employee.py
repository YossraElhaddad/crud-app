from config_db import db

class Employee(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    title = db.Column(db.String(50), db.ForeignKey('salaries.employee_title'), nullable=False)
    salary = db.Column(db.Integer)
    years_of_experience = db.Column(db.Integer)
    dept_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=False)

    

    def __init__(self, name, title, salary, years_of_experience, dept_id):
        self.name = name
        self.title = title
        self.salary = salary
        self.years_of_experience = years_of_experience
        self.dept_id = dept_id

    def __repr__(self):
        return f"<Employee {self.id}, {self.name}, {self.title}, {self.salary}, {self.years_of_experience}, {self.dept_id}>"