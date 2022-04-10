import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """Class for testing, that inherits from unittest"""
    def test_full_name(self):
        """ Method to test full name, with reference to self"""
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")


if __name__ == "__main__":
    unittest.main()
