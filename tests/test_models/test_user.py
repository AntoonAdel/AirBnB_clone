#!/usr/bin/python3
"""
Test Suites for the User class of the user module
"""


import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ Test the User class """

    def setUp(self):
        """
        Setup resources to be used in the tests
        1) Create a User object
        """
        self.user = User()

    def ShutDown(self):
        """
        Clean up resources after the tests
        1) Delete the instance created
        """
        del self.user

    def test_attrs(self):
        """ Test attributes for the user object """
    
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attrs_types(self):
        """ Asert that object attributes are of the right type """

        self.assertTrue(type(self.user.email) == str)
        self.assertTrue(type(self.user.password) == str)
        self.assertTrue(type(self.user.first_name) == str)
        self.assertTrue(type(self.user.last_name) == str)

    def test_BaseModel_to_dict_method(self):
        """ Test the to_dict method of the BaseModel """

        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertEqual(user_dict["__class__"], "User")

    def test_class_documentation(self):
        """ Test User class docuemntation """
        self.assertIsNotNone(User.__doc__)

    def test_module_documentation(self):
        """ Test module documentation """
        self.assertIsNotNone(User.__module__.__doc__)

    def test_self_docuentation(self):
        """ Test documentation for this class/module """
        self.assertIsNotNone(self.__class__.__doc__)
        self.assertIsNotNone(self.__module__.__doc__)


if __name__ == "__main__":
    unittest.main()
