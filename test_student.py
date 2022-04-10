import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """Class for testing, that inherits from unittest"""
    def test_full_name(self):
        """ Test full name, with reference to self"""
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")
        
    def test_email(self):
        """ Test email """
        student = Student("John", "Doe")
        student.alert_santa()
        self.assertEqual(student.email, "john.doe@email.com")

    def test_alert_santa(self):
        """ Test Santa alert if student has been naughty"""
        student = Student("John", "Doe")
        student.alert_santa()
        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()
