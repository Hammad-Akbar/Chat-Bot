# models.py
import flask_sqlalchemy
import app

import os

from dotenv import load_dotenv
from os.path import join, dirname


dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
dbuser = os.environ['USER']

# app.app = app module app variable
database_uri = 'postgresql://{}:{}@localhost/postgres'.format(sql_user, sql_pwd)
app.app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
db = flask_sqlalchemy.SQLAlchemy(app.app)

class Usps(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # key
    address = db.Column(db.String(120))
    
    def __init__(self, a):
        self.address = a
        
    def __repr__(self):
        return '<Usps address: %s>' % self.address 

