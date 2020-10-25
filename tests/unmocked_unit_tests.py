""" Testing unmocked responses in app.py """

import unittest
import sys
from os.path import dirname, join
sys.path.insert(1, join(dirname(__file__), '../'))

import app
from app import KEY_RESPONSE

KEY_INPUT = "input"

class ChatbotTestCase(unittest.TestCase):
    """ test cases for chatbot fucntionality """

    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_RESPONSE: "!!help",
            },
            {
                KEY_INPUT: "!about me",
                KEY_RESPONSE: "!about me",
            },
            {
                KEY_INPUT: "!! about",
                KEY_RESPONSE: " This is a chat app made with React.",
            },
            {
                KEY_INPUT: "!! clear",
                KEY_RESPONSE: "",
            },
            {
                KEY_INPUT: "hello",
                KEY_RESPONSE: "hello",
            },
            {
                KEY_INPUT: " !! about",
                KEY_RESPONSE: " !! about",
            },
            {
                KEY_INPUT: "!! help ",
                KEY_RESPONSE: " Not a valid command",
            },
            {
                KEY_INPUT: "!! help !! about",
                KEY_RESPONSE: " Not a valid command",
            },
            {
                KEY_INPUT: "!! help",
                KEY_RESPONSE: " These are the following commands you can use: •!! about -> learn about me •!! help -> list of commands •!! translate -> translate text into good barnacle-covered Corsair speak (thats pirate talk for pirate talk) •!! norris -> get a random Chuck Norris Joke •!! clear -> clear chat log",
            },
        ]

        self.failure_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_RESPONSE: " This is a chat app made with React.",
            },
            {
                KEY_INPUT: "!! help",
                KEY_RESPONSE: " Not a valid command",
            },
            {
                KEY_INPUT: "!! about",
                KEY_RESPONSE: " Not a valid command",
            },
            {
                KEY_INPUT: "!! translate ",
                KEY_RESPONSE: " Not a valid command",
            },
            {
                KEY_INPUT: "!! norris",
                KEY_RESPONSE: " Not a valid command",
            },
            {
                KEY_INPUT: "!! clear",
                KEY_RESPONSE: " Not a valid command",
            },
        ]

    def test_command_message_success(self):
        """ running tests on correct messages """

        for test in self.success_test_params:
            response = app.commands(test[KEY_INPUT])
            expected = test[KEY_RESPONSE]

            self.assertEqual(response, expected)

    def test_command_message_failure(self):
        """ running tests on incorrect messages """

        for test in self.failure_test_params:
            response = app.commands(test[KEY_INPUT])
            expected = test[KEY_RESPONSE]

            self.assertNotEqual(response, expected)

if __name__ == '__main__':
    unittest.main()
