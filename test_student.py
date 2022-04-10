import unittest
from datetime import timedelta
from student import Student


class TestStudent(unittest.TestCase):
    """Class for testing, that inherits from unittest
    * Create a new test method called test_apply_extension
    * Inside test_apply_extension, store the current end_date for our student
    instance in a varable called old_end_date
    * Call a method named apply_extension that will take the number of days as
    an argument on the student instance to update the end_date
    * Assert whether the instance's end_date equals the old_end_date plus the
    days argument that was passed in using timedelta
    * Run the tests to confirm that the new method is failing
    * In the Student class, create a new method called apply_extension that
    has a parameter called days
    * Use the timedelta method drom datetime to update the end_date property
    * Run the tests t confirm they are working
    """
    @classmethod
    def setUpClass(cls):
        print("set up class")

    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")

    @classmethod
    def tearDownClass(cls):
        print("tear down Class")

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

    def test_apply_extension(self):
        """ Test time extension """
        print("apply_extension")
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date
                         + timedelta(days=5))
        # self.student.apply_extension(5)
        # self.assertEqual(self.student.end_date, self.student._start_date
        #                  + timedelta(days=370))


if __name__ == "__main__":
    unittest.main()
