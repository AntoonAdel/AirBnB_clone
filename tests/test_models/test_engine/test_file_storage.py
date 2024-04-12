#!/usr/bin/python3
"""
Test Suites for the file_storage module
FileStorage class and the methods
"""


from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import unittest


class TestFileStorage(unittest.TestCase):
    """ Unittests for the FileStorage class """

    def setUp(self):
        """
        Set up resources to be used in the tests
        1) If 'file.json' exists, rename it to 'tempfile'
        2) Initialize objects
        """

        if os.path.isfile('file.json'):
            os.rename('file.json', 'tempfile')
        self.storage = FileStorage()
        self.base = BaseModel()

    def ShutDown(self):
        """
        Shut down resources associated with tests
        1) Rename 'tempfile' back to 'file.json'
        2) Delete the objects created during the tests
        """

        if os.path.isfile('tempfile'):
            os.rename('tempfile', 'file.json')
        del self.storage
        del self.base

    def test_attrs(self):
        """ Test the attributes of objects """

        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertTrue(hasattr(self.base, "id"))
        self.assertTrue(hasattr(self.base, "__class__"))
        self.assertEqual(self.base.__class__.__name__, "BaseModel")
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")
        self.assertTrue(isinstance(self.storage._FileStorage__objects, dict))

    def test_all_method(self):
        """ Test the all method """

        all_objects_dict = self.storage.all()
        base_id = "BaseModel." + self.base.id
        self.assertIsInstance(all_objects_dict, dict)
        self.assertIn(base_id, all_objects_dict)

    def test_reload_method(self):
        """
        Test the reload method
        1) Create a temporaty BaseModel object
        2) Call save on the object
        3) call reload on the storge object and verify that the new
            temporaty object exists in the storage object
        4) Delete temporary object
        """

        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))
        tmp_base = BaseModel()
        tmp_base.save()
        tmp_base_id = "BaseModel." + tmp_base.id
        self.assertIn(tmp_base_id, self.storage.all())
        del tmp_base

if __name__ == "__main__":
    unittest.main()
