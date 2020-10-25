""" models.py - creates database tables """

from enum import Enum
from app import db

class AuthUser(db.Model):
    """ Add user table to database """

    id = db.Column(db.Integer, primary_key=True)
    auth_type = db.Column(db.String(120))
    name = db.Column(db.String(120))

    def __init__(self, name, auth_type):
        #assert type(auth_type) is AuthUserType
        assert isinstance(auth_type, AuthUserType)
        self.name = name
        self.auth_type = auth_type.value

    def __repr__(self):
        return "<User name: {}\ntype: {}".format(self.name, self.auth_type)

class AuthUserType(Enum):
    """ Enum for google """

    GOOGLE = "google"

class MessageLog(db.Model):
    """ Add message table to database """

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(1000))

    def __init__(self, a_message):
        self.message = a_message

    def __repr__(self):
        return '<Messages: %s>' % self.message
