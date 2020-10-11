# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import models 
import requests
import json

MESSAGES_RECEIVED_CHANNEL = 'messagees received'

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), 'sql.env')
load_dotenv(dotenv_path)

database_uri = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.create_all()
db.session.commit()

def clear_data():
    session = db.session()
    f = session.query(models.MessageLog).delete()
    print('records deleted:',f)
    session.commit()
    session.close()
    
def emit_all_messagees(channel):
    #content.jsx is looking for a key called allmessagees, so we want to emit to all messagees 
    all_messagees = [ \
        db_message.message for db_message in \
        db.session.query(models.MessageLog).all()
    ]
    
    socketio.emit(channel, {
        'allmessagees' : all_messagees 
    })

@socketio.on('connect')
def on_connect():
    print('Someone connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
    
    emit_all_messagees(MESSAGES_RECEIVED_CHANNEL)
    
@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('new message input')
def on_new_message(data):
    print("Got an event for new message input with data:", data)
    text = data["message"]
    
    if text == "!! about":
        text = "This is a chat app made with React."
    
    elif text == "!! help":
        text = "These are the following commands you can use: "
        db.session.add(models.MessageLog(text));
        db.session.commit();
        
        text = "!! about    ->  learn about me"
        db.session.add(models.MessageLog(text));
        db.session.commit();
        
        text = "!! help     ->  list of commands"
        db.session.add(models.MessageLog(text));
        db.session.commit();
        
        text = "!! translate  ->  translate text into good barnacle-covered Corsair speak (thats pirate talk for pirate talk)"
        db.session.add(models.MessageLog(text));
        db.session.commit();
        
        text = "!! norris  ->  get a random Chuck Norris Joke"
        db.session.add(models.MessageLog(text));
        db.session.commit();
        
        text = "!! clear    ->  clear chat log"
        db.session.add(models.MessageLog(text));
        db.session.commit();
    
    elif text.startswith("!! translate "):
        try:
            text = text.strip("!! translate ")
            text = text.replace(" ", "%20")
            url = "https://api.funtranslations.com/translate/pirate.json?text={}".format(text)
            response = requests.get(url)
            json_body = response.json()
            text = json.dumps(json_body["contents"]["translated"], indent = 2)
            text = text.replace("\\\\", "\\")
            
        except KeyError:
            text = "Sorry the translator is broken. Try again later."
        
    elif text == "!! clear":
        clear_data()
        text = "Successfully cleared all messages."
        
    elif text == "!! norris":
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        json_body = response.json()
        text = json.dumps(json_body["value"], indent = 2)
        text.strip('"')
        
        
    elif text.startswith("!! "):
        text = "Not a valid command"
    
    db.session.add(models.MessageLog(text));
    db.session.commit();
    
    emit_all_messagees(MESSAGES_RECEIVED_CHANNEL)

@app.route('/')
def index():
    emit_all_messagees(MESSAGES_RECEIVED_CHANNEL)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
