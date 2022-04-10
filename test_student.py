import unittest
from student import Student


class TestStudent(unittest.TestCase):
    """Class for testing, that inherits from unittest"""
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        """ Test full name, with reference to self"""
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")

    def test_email(self):
        """ Test email """
        print("test_email")
        self.student.alert_santa()
        self.assertEqual(self.student.email, "john.doe@email.com")

    def test_alert_santa(self):
        """ Test Santa alert if student has been naughty"""
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


if __name__ == "__main__":
    unittest.main()
