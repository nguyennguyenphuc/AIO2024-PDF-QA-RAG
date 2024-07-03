import unittest
from src.chat_interface import run_chat_interface


class TestChatInterface(unittest.TestCase):
    def test_run_chat_interface(self):
        # Dummy test to check if function is callable
        self.assertIsNotNone(run_chat_interface)


if __name__ == '__main__':
    unittest.main()
