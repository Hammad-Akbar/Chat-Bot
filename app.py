import os
import flask
import flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return flask.render_template('index.html')

@socketio.on('connect')
def on_connect():
    print('Someone connected!')

@socketio.on('disconnect')
def on_disconnect():
    print ('Someone disconnected!')

@socketio.on('new number')
def on_new_number(data):
    print("Got an event for new number with data:", data)
    rand_number = data['number']
    socketio.emit('number received', {
        'number': rand_number
    })

socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 8080)),
    debug=True
)
