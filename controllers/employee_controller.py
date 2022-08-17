from models.Employee import Employee
from models.Salary import Salary
from models.Department import Department
from config_db import db
from flask import redirect, render_template, request

def index():
   records = Employee.query.order_by(Employee.id).all()
   departments = Department.query.order_by(Department.id).all()
   titles = db.engine.execute(f'SELECT employee_title FROM Salaries')
   return render_template('employee.html', records=records, departments=departments, titles=titles, Department=Department)

def show(id):
   employee = Employee.query.filter_by(id = id).one()
   department = Department.query.filter_by(id = employee.dept_id).one()
   titles = db.engine.execute(f'SELECT employee_title FROM Salaries')

   return render_template('update_employee.html', employee=employee, department=department, titles=titles)

#adding a new employee related to the selected department where the employees who work at that department are viewed
def new():
    data = request.form
 
    salary = Salary.query.filter_by(employee_title = data['title']).one()

    #an equation to set up the dependency between salary, title and years of experience
    expected_salary = salary.title_salary + int(data['years_of_experience']) * 1000


    department = Department.query.filter_by(name = data['dept_name']).one()

    new_employee = Employee(data['name'], data['title'], expected_salary, data['years_of_experience'], department.id)


    db.session.add(new_employee)
    db.session.commit()

    return redirect(f'/departments/{department.id}/employees')


def delete(id):
    employee_to_delete = Employee.query.get_or_404(id)
    dept_id = employee_to_delete.dept_id

    try:
        db.session.delete(employee_to_delete)
        db.session.commit()
        return redirect(f'/departments/{dept_id}/employees')
    except:
        return 'There was a problem deleting that employee'

def update(id):
    employee = Employee.query.get_or_404(id)

    try:
        data = request.form

        employee.name = data['name']
        employee.title = data['title']
        employee.salary = data['salary']
        employee.years_of_experience = data['years_of_experience']

        department = Department.query.filter_by(name = data['dept_name']).one()
        employee.dept_id = department.id

        db.session.commit()
        return redirect(f'/departments/{department.id}/employees')
    except:
        return 'There was a problem updating that employee'
