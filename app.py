from flask import Flask, redirect
from flask_migrate import Migrate
from models.Department import Department
from routes.employees import employees
from routes.departments import departments
from config_db import db

app = Flask(__name__)


app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(departments, url_prefix='/departments')
app.register_blueprint(employees, url_prefix='/employees')

@app.route('/', methods=['GET'])
def home():
    return redirect('/departments')



if __name__ == "__main__":
    app.run(debug=True, port=5000)