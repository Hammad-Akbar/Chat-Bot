""" Testing mocked responses in app.py """

import unittest
import unittest.mock as mock
import sys
from os.path import dirname, join
sys.path.insert(1, join(dirname(__file__), '../'))

import app
import models

from app import MESSAGES_RECEIVED_CHANNEL
from models import AuthUserType

class TestCase(unittest.TestCase):
    """ test cases for socketio fucntionality """

    def setUp(self):
        self.success_test_params = [
            {
                MESSAGES_RECEIVED_CHANNEL: "messages received",
                "message": "hello",
                "name": "Hammad",
                "test": "Connected",
                "connected": "connected"
            }
        ]

        self.failure_test_params = [
            {
                MESSAGES_RECEIVED_CHANNEL: "messages NOT received",
                "message": "!! hello",
                "name": "GuEsT",
                "test": "NOT CONNECTED",
                "connected": "NOT connected"
            }
        ]

    def test_push_new_user_google_to_db(self):
        """ testing push_new_user_to_db """

        with mock.patch('flask_sqlalchemy.SignallingSession.commit', self.mock_session_commit):
            app.push_new_user_to_db("Hammad Akbar", AuthUserType.GOOGLE)

    def test_push_guest_to_db(self):
        """ testing push_new_user_to_db """

        with mock.patch('flask_sqlalchemy.SignallingSession.commit', self.mock_session_commit):
            app.push_new_user_to_db("GUEST", AuthUserType.GOOGLE)

    def test_emit_success_channel(self):
        """ running tests on socketio.emit """

        for test in self.success_test_params:
            with mock.patch('flask_socketio.SocketIO.emit', self.mock_emit_messages_channel):
                try:
                    app.emit_all_messages(test[MESSAGES_RECEIVED_CHANNEL])
                except ValueError as err:
                    self.fail(err)

    def test_emit_success_connected(self):
        """ running tests on socketio.emit """

        for test in self.success_test_params:
            with mock.patch('flask_socketio.SocketIO.emit', self.mock_emit_messages_channel):
                try:
                    app.emit_all_messages(test['connected'])
                except ValueError as err:
                    self.fail(err)

    def test_on_new_message(self):
        """ testing on new message  """

        for test in self.success_test_params:
            with mock.patch('flask_sqlalchemy.SignallingSession.add', self.mock_session_add):
                app.on_new_message(test)

    def test_push_new_user_to_db(self):
        """ testing on_new_google_user """

        for test in self.success_test_params:
            with mock.patch('flask_socketio.SocketIO.on', self.mock_push_new_user_to_db):
                app.on_new_google_user(test)

    def test_emit_failure_channel(self):
        """ running tests on socketio.emit """

        for test in self.failure_test_params:
            with mock.patch('flask_socketio.SocketIO.emit', self.mock_emit_messages_channel):
                try:
                    app.emit_all_messages(test[MESSAGES_RECEIVED_CHANNEL])
                except ValueError as err:
                    self.fail(err)

    def test_emit_failure_connected(self):
        """ running tests on socketio.emit """

        for test in self.failure_test_params:
            with mock.patch('flask_socketio.SocketIO.emit', self.mock_emit_messages_channel):
                try:
                    app.emit_all_messages(test['connected'])
                except ValueError as err:
                    self.fail(err)

    def test_on_new_message_failure(self):
        """ testing on new message  """

        for test in self.failure_test_params:
            with mock.patch('flask_sqlalchemy.SignallingSession.add', self.mock_session_add):
                app.on_new_message(test)

    def test_push_new_user_to_db_failure(self):
        """ testing on_new_google_user """

        for test in self.failure_test_params:
            with mock.patch('flask_socketio.SocketIO.on', self.mock_push_new_user_to_db):
                app.on_new_google_user(test)

    def mock_emit_messages_channel(self, channel, data):
        """ mock emit messages when emitting to a channel"""

        if not isinstance(channel, str):
            raise ValueError(channel)
        if not isinstance(data, dict):
            raise ValueError(data)
        if not isinstance('connected', str):
            raise ValueError(data)

    def mock_session_commit(self):
        """ mock session.commit() for db """
        return

    def mock_session_add(self, holder):
        """ mock session.add() for db """
        return

    def mock_push_new_user_to_db(self, name_holder, holder):
        """ mock pushing new username to db """
        return

if __name__ == '__main__':
    unittest.main()
