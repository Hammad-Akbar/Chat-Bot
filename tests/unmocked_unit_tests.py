import unittest
from os.path import dirname, join
import sys
sys.path.insert(1, join(dirname(__file__), '../'))

import app
from app import KEY_RESPONSE

KEY_INPUT = "input"

class ChatbotTestCase(unittest.TestCase):
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
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_RESPONSE: " This is a chat app made with React.",
            },
        ]


    def test_command_message_success(self):
        for test in self.success_test_params:
            response = app.commands(test[KEY_INPUT])
            expected = test[KEY_RESPONSE]
            
            self.assertEqual(response, expected)
            
    def test_command_message_failure(self):
        for test in self.failure_test_params:
            response = app.commands(test[KEY_INPUT])
            expected = test[KEY_RESPONSE]
            
            self.assertNotEqual(response[KEY_RESPONSE], expected[KEY_RESPONSE])

if __name__ == '__main__':
    unittest.main()