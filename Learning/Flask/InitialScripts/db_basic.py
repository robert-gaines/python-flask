
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
import os

db_dir = os.path.abspath(os.path.dirname(__file__))

# Referential call referencing the current file ?

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(db_dir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) # Pass the app to the SQLAlchemy class

Migrate(app,db)

#Setting up the model

class Inventory(db.Model):
    #
    #Table Name will acquire a default value, but it can be set manually
    #
    __tablename__ = 'Inventory'
    #
    #Primary Key
    #
    item_id = db.Column(db.Integer,primary_key=True)
    item_name = db.Column(db.Text)
    item_pn = db.Column(db.Integer)
    item_site = db.Column(db.Text)
    #
    def __init__(self,item_name,item_pn):
        #
        self.item_name = item_name
        self.item_pn = item_pn
        self.item_site = item_site

    def __repr__(self):
        #
        return f"Item is {self.item_name} and the part number is: {self.item_pn}"
