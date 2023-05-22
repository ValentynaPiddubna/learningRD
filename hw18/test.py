import unittest
from io import StringIO
from unittest.mock import patch

from Lesson18 import Bot, TelegramBot

class TestBot(unittest.TestCase):
    def test_say_name(self):
        bot = Bot('Marvin')
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            bot.say_name()
        self.assertEqual(captured_output.getvalue().strip(), 'Marvin')

    def test_send_message(self):
        bot = Bot('Marvin')
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            bot.send_message('Hello')
        self.assertEqual(captured_output.getvalue().strip(), 'Hello')

class TestTelegramBot(unittest.TestCase):
    def test_say_name(self):
        bot = TelegramBot('TG')
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            bot.say_name()
        self.assertEqual(captured_output.getvalue().strip(), 'TG')

    def test_send_message(self):
        bot = TelegramBot('TG', url='https://example.com', chat_id=1)
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            bot.send_message('Hello')
        self.assertEqual(captured_output.getvalue().strip(), 'TG bot says Hello to chat 1 using https://example.com')

if __name__ == '__main__':
    unittest.main()
