# models.py
import flask_sqlalchemy
from app import db

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return '<User: %s>' % self.name

class MessageLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000))
    
    def __init__(self, a):
        self.message = a
        
    def __repr__(self):
        return '<Messages: %s>' % self.message



