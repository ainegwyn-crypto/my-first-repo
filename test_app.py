import unittest
from app import greet

class TestGreet(unittest.TestCase):

    def test_greet_with_name(self):
        self.assertEqual(greet("Alice"), "Hi, Alice!")

    def test_greet_with_empty_string(self):
        self.assertEqual(greet(""), "Hello, !")

    def test_greet_with_none(self):
        self.assertEqual(greet(None), "Hello, Anonymous!")

if __name__ == "__main__":
    unittest.main()