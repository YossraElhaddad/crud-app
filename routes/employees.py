from controllers.employee_controller import *
from flask import Blueprint

employees = Blueprint('employees', __name__)

employees.route('/', methods=['GET'])(index)

employees.route('/<int:id>', methods=['GET'])(show)

employees.route('/new', methods=['POST'])(new)

employees.route('/delete/<int:id>')(delete)

employees.route('/update/<int:id>', methods=['POST'])(update)
