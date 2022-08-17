from config_db import db

class Salary(db.Model):
    __tablename__ = 'salaries'
    employee_title = db.Column(db.String(50), primary_key=True, nullable=False)
    title_salary = db.Column(db.Integer)
   
    
    def __init__(self, employee_title, title_salary):
        self.employee_title = employee_title
        self.title_salary = title_salary

    def __repr__(self):
        return f"<Salary {self.employee_title}, {self.title_salary}>"