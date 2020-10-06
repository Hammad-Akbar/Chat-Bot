# app.py
import os
import flask
import flask_sqlalchemy

app = flask.Flask(__name__)
db = flask_sqlalchemy.SQLAlchemy(app)

import models  # this needs to be here
# notice the SQL_ALCHEMY_CONFIG is removed.


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
