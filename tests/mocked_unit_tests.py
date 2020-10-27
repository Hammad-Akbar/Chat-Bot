""" Testing mocked responses in app.py """

import unittest
import sys
import app
import models
import unittest.mock as mock
from os.path import dirname, join
sys.path.insert(1, join(dirname(__file__), '../'))
from app import MESSAGES_RECEIVED_CHANNEL, USERS_UPDATED_CHANNEL
from models import AuthUserType 

class SocketTestCase(unittest.TestCase):
    """ test cases for socketio fucntionality """

    def setUp(self):
        self.success_test_params = [
            {
                MESSAGES_RECEIVED_CHANNEL: "messages received", 
                "message": "hello"
            }
        ]

        self.failure_test_params = [
        ]
    
    def test_push_new_user_to_db(self):
        """ testing push_new_user_to_db """
        with mock.patch('flask_sqlalchemy.SignallingSession.commit', self.mock_session_commit):
            app.push_new_user_to_db("Hammad Akbar", AuthUserType.GOOGLE)
            
    def test_push_guest_to_db(self):
        """ testing push_new_user_to_db """
        with mock.patch('flask_sqlalchemy.SignallingSession.commit', self.mock_session_commit):
            app.push_new_user_to_db("GUEST", AuthUserType.GOOGLE)
            
    def test_emit_success(self):
        """ running tests on socketio.emit """
    
        for test in self.success_test_params:
            with mock.patch('flask_socketio.SocketIO.emit', self.mock_emit_messages):
                try:
                    app.emit_all_messages(test[MESSAGES_RECEIVED_CHANNEL])
                    #expected = test[MESSAGES_RECEIVED_CHANNEL]
                except ValueError as ve:
                    self.fail(ve)
    
    def test_on_new_message(self):
        """ testing on new message  """
        for test in self.success_test_params:
            with mock.patch('flask_sqlalchemy.SignallingSession.add', self.mock_session_add):
                app.on_new_message(test)
    
    def mock_emit_messages(self, channel, data):
        """ mock app.clear_data() """
        if not isinstance(channel, str):
            raise ValueError(channel)
        if not isinstance(data, dict):
            raise ValueError(data)

    def mock_session_commit(self):
        """ mock session.commit() for db """
        return
    
    def mock_session_add(self, apple):
        """ mock session.add() for db """
        return
   
if __name__ == '__main__':
    unittest.main()
