# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy

app = flask.Flask(__name__)


dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

sql_user = os.environ['SQL_USER']
sql_pwd = os.environ['SQL_PASSWORD']
dbuser = os.environ['USER']

database_uri = 'postgresql://{}:{}@localhost/postgres'.format(
    sql_user, sql_pwd)

app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.app = app

import models 

@app.route('/')
def index():
    models.db.create_all()
    addresses = [
        models.Usps("1600 Pennsylvania"),
        models.Usps("121 W 21st Ave"),
        models.Usps("NJIT GITC")]
    for address in addresses:
        db.session.add(address)
    db.session.commit()
    
    return flask.render_template("index.html")
    
    
if __name__ == '__main__':
    app.run(
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
