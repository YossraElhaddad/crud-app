from controllers.department_controller import *
from flask import Blueprint

departments = Blueprint('departments', __name__)

departments.route('/', methods=['GET'])(index)


departments.route('/<int:id>', methods=['GET'])(show)

departments.route('/new', methods=['POST'])(new)

departments.route('/delete/<int:id>')(delete)

departments.route('/update/<int:id>', methods=['POST'])(update)

departments.route('/<int:id>/employees', methods=['GET'])(show_employees)