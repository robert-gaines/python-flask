from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import os

BaseDirectory = os.path.abspath(os.path.dirname(__file__)) # References the current directory - referenced within DB creation

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(BaseDirectory,'data.sqlite') # Join the current directory to the DB path

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # Tethering the database to the application

Migrate(app,db) # For DB Change Tracking

class Employee(db.Model):

    __tablename__ = "employee"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    roles = db.relationship('Role',backref='',lazy='dynamic') # Relationship -> Connected to Model -> Back Reference -> (Back to the primary model) -> lazy = how the items are to be loaded
    manager = db.relationship('Manager',backref='',uselist=False) # One to One relationship -> One employee has one manager

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if(self.manager):
            return f"Employee's name is {self.name} and the manager is: {self.manager.name}"
        else:
            return f"Employee's name is: {self.name} and the manager has not been assigned"

    def IdentifyRoles(self):
        print("The employee has the following roles: ")
        for r in roles:
            print(r.name)

class Role(db.Model):

    __tablename__ = 'role'

    id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.Text)
    employee_id = db.Column(db.Integer,db.ForeignKey('employee.id'))

    def __init__(self,role,id):
        self.role = role
        self.id = id


class Manager(db.Model):

    __tablename__ = 'managers'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)

    employee_id = db.Column(db.Integer,db.ForeignKey('employee.id'))

    def __init__(self,name,employee_id):
        self.name = name
        self.employee_id = employee_id
