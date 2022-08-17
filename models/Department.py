from config_db import db

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True, )
    name = db.Column(db.String(50), unique=True, nullable=False)
   
    employees = db.relationship('Employee', backref='departments', cascade = 'all, delete-orphan', lazy = 'dynamic')
    
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Department {self.id}, {self.name}>"