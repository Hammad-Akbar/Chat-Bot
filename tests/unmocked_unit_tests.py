import unittest
from os.path import dirname, join
import sys
sys.path.insert(1, join(dirname(__file__), '../'))

import app
from app import KEY_RESPONSE

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " Not a valid command",
                }
            },
            {
                KEY_INPUT: "!about me",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " Not a valid command",
                }
            },
            {
                KEY_INPUT: "!! about",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " This is a chat app made with React.",
                }
            },
            {
                KEY_INPUT: "!! help",
                KEY_EXPECTED: {
                    KEY_RESPONSE: ''' 
                    These are the following commands you can use:
                    \n!! about    ->  learn about me
                    \n!! help     ->  list of commands
                    \n!! translate  ->  translate text into good barnacle-covered Corsair speak (thats pirate talk for pirate talk)
                    \n!! norris  ->  get a random Chuck Norris Joke
                    \n!! clear    ->  clear chat log
                    ''',
                }
            },
            {
                KEY_INPUT: "!! clear",
                KEY_EXPECTED: {
                    KEY_RESPONSE: "",
                }
            },
            {
                KEY_INPUT: "!! helps",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " Not a valid command",
                }
            },
            {
                KEY_INPUT: " !! about",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " Not a valid command",
                }
            },
            {
                KEY_INPUT: "!! help ",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " Not a valid command",
                }
            },
            {
                KEY_INPUT: "!! help !! about",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " Not a valid command",
                }
            },
        ]
        
        self.failure_test_params = [
            {
                KEY_INPUT: "!!help",
                KEY_EXPECTED: {
                    KEY_RESPONSE: " This is a chat app made with React.",
                }
            },
        ]


    def test_command_message_success(self):
        for test in self.success_test_params:
            response = app.commands(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertEqual(response[KEY_RESPONSE], expected[KEY_RESPONSE])
            self.assertDictEqual(response, expected)
            
    def test_command_message_failure(self):
        for test in self.failure_test_params:
            response = app.commands(test[KEY_INPUT])
            expected = test[KEY_EXPECTED]
            
            self.assertNotEqual(response[KEY_RESPONSE], expected[KEY_RESPONSE])

if __name__ == 'app':
    unittest.main()