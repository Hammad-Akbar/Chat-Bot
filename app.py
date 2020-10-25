# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import flask
import flask_sqlalchemy
import flask_socketio
import requests
import json

SQLALCHEMY_TRACK_MODIFICATIONS = True
MESSAGES_RECEIVED_CHANNEL = 'messages received'
USERS_UPDATED_CHANNEL = 'users updated'

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

import models 

BOT_PREFIX = "!!"
KEY_IS_BOT = "is_bot"
KEY_BOT_COMMAND = "bot_command"
KEY_MESSAGE = "message"

def parse_message(message):
    if not message.startswith(BOT_PREFIX):
        return {
            KEY_IS_BOT: False, 
            KEY_BOT_COMMAND: None, 
            KEY_MESSAGE: message,
        }
            
    message_components = message.split(" ", 1)
    if len(message_components) == 1:
        possible_bot_cmd, rest_of_message = message_components[0], ""
    else:
        possible_bot_cmd, rest_of_message = message_components[0], message_components[1]
    
    return {
        KEY_IS_BOT: True, 
        KEY_BOT_COMMAND: possible_bot_cmd[len(BOT_PREFIX):], 
        KEY_MESSAGE: rest_of_message,
    }
    
def commands(text):
    if text == "!! about":
        text = " This is a chat app made with React."
        db.session.add(models.MessageLog(text))
        db.session.commit()
        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    elif text == "!! help":
        text = " These are the following commands you can use: "
        db.session.add(models.MessageLog(text))
        db.session.commit()

        text = " !! about    ->  learn about me"
        db.session.add(models.MessageLog(text))
        db.session.commit()

        text = " !! help     ->  list of commands"
        db.session.add(models.MessageLog(text))
        db.session.commit()

        text = " !! translate  ->  translate text into good barnacle-covered Corsair speak (thats pirate talk for pirate talk)"
        db.session.add(models.MessageLog(text))
        db.session.commit()

        text = " !! norris  ->  get a random Chuck Norris Joke"
        db.session.add(models.MessageLog(text))
        db.session.commit()

        text = " !! clear    ->  clear chat log"
        db.session.add(models.MessageLog(text))
        db.session.commit()

        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    elif text.startswith("!! translate "):
        try:
            text = text.strip("!! translate ")
            text = text.replace(" ", "%20")
            url = "https://api.funtranslations.com/translate/pirate.json?text={}".format(text)
            response = requests.get(url)
            json_body = response.json()
            text = json.dumps(json_body["contents"]["translated"], indent = 2)
            text = text.replace("\\\\", "\\")
            text = " " + text
            db.session.add(models.MessageLog(text))
            db.session.commit()

            emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

        except KeyError:
            text = " Sorry the translator is broken. Try again later."
            db.session.add(models.MessageLog(text))
            db.session.commit()

            emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    elif text == "!! clear":
        clear_data()
        text = ""
        db.session.add(models.MessageLog(text))
        db.session.commit()

        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    
    elif text == "!! clear users":
        clear_users()
        text = " "
        db.session.add(models.MessageLog(text))
        db.session.commit()

        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    elif text == "!! norris":
        try:
            url = "https://api.chucknorris.io/jokes/random"
            response = requests.get(url)
            json_body = response.json()
            text = json.dumps(json_body["value"], indent = 2)
            text.strip('"')
            text = " " + text
            db.session.add(models.MessageLog(text))
            db.session.commit()

            emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

        except KeyError:
            text = " Sorry joke machine is broken. Try again later."
            db.session.add(models.MessageLog(text))
            db.session.commit()

            emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    elif text.startswith("!! "):
        text = " Not a valid command"
        db.session.add(models.MessageLog(text))
        db.session.commit()

        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)

    else:
        db.session.add(models.MessageLog(text))
        db.session.commit()

        emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
        
    return text
    
#clear message log
def clear_data():
    session = db.session()
    f = session.query(models.MessageLog).delete()
    print('records deleted:',f)
    session.commit()
    session.close()

def clear_users():
    session = db.session()
    f = session.query(models.AuthUser).delete()
    print('records deleted:',f)
    session.commit()
    session.close()
    
#send all messages    
def emit_all_messages(channel):
    #content.jsx is looking for a key called allmessages, so we want to emit to all messages 
    all_messages = [ \
        db_message.message for db_message in \
        db.session.query(models.MessageLog).all()
    ]
    
    socketio.emit(channel, {
        'allmessages' : all_messages 
    })

#send the names of all users
def emit_all_oauth_users(channel):
    all_users = [ \
        user.name for user in \
        db.session.query(models.AuthUser).all()
    ]
        
    socketio.emit(channel, {
        'allUsers': all_users
    })

#add username to database if login did not fail
def push_new_user_to_db(name, auth_type):
    if name != "GUEST":
        db.session.add(models.AuthUser(name, auth_type));
        db.session.commit();
    else:
        name == 'GUEST'
        db.session.add(models.AuthUser(name, auth_type));
        db.session.commit();
        
    emit_all_oauth_users(USERS_UPDATED_CHANNEL)

@socketio.on('connect')
def on_connect():
    sid = str(flask.request.sid)
    print(sid + ' connected!')
    socketio.emit('connected', {
        'test': 'Connected'
    })
    
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    
@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

#push the name of the new user
@socketio.on('new google user')
def on_new_google_user(data):
    print("Got an event for new google user input with data:", data)
    name = data['name']
    push_new_user_to_db(name, models.AuthUserType.GOOGLE)
    emit_all_oauth_users(USERS_UPDATED_CHANNEL)

#push messages and deal with commands 
@socketio.on('new message input')
def on_new_message(data):
    print("Got an event for new message input with data:", data)
    text = data["message"]
    commands(text)
    
@app.route('/')
def index():
    emit_all_messages(MESSAGES_RECEIVED_CHANNEL)
    emit_all_oauth_users(USERS_UPDATED_CHANNEL)

    return flask.render_template("index.html")

if __name__ == '__main__': 
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
