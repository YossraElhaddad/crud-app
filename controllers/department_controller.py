from models.Department import Department
from models.Employee import Employee
from config_db import db
from flask import redirect, render_template, request

def index():
   records = Department.query.order_by(Department.id).all()
   return render_template('index.html', records = records)

#getting the page where the selected department can be updated
def show(id):
   department = Department.query.filter_by(id = id).one()
   return render_template('update_department.html', department=department)


def new():
    dept_name = request.form['dept_name']
    new_department = Department(dept_name)

    db.session.add(new_department)
    db.session.commit()

    return redirect('/departments')


def delete(id):
    department_to_delete = Department.query.get_or_404(id)

    try:
        db.session.delete(department_to_delete)
        db.session.commit()
        return redirect('/departments')
    except:
        return 'There was a problem deleting that department'



def update(id):
    department = Department.query.get_or_404(id)

    try:
        department.name = request.form['dept_name']
        db.session.commit()
        return redirect('/departments')
    except:
        return 'There was a problem updating that department'

def show_employees(id):
    #employees = db.engine.execute(f'SELECT * FROM  Employees INNER JOIN Departments ON dept_id = Departments.id WHERE dept_id = {id}')
    employees = Employee.query.filter_by(dept_id = id).all()
    department = Department.query.filter_by(id = id).one()
    titles = db.engine.execute(f'SELECT employee_title FROM Salaries')

    return render_template('employee.html', records = employees, department=department, titles=titles)

