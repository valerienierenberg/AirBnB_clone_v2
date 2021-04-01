#!/usr/bin/python3
""" tests for dbstorage """

from datetime import datetime
import inspect
import models
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json
import os
import pep8
import unittest
DBStorage = db_storage.DBStorage
classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "state": State, "User": User}

class TestDBStorageDoc(unittest.TestCase):
    """ tests docs and style of DBStorage class """
    @classmethod
    def setUpClass(cls):
        """ setting up tests """
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_db_storage(self):
        """tests for PEP8"""
        pep = pep8.StyleGuide(quiet=True)
        result = pep8.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Fix pep")

    def test_db_storage_docstring(self):
        """ tests for docstring """
        self.assertIsNot(db_storage.__doc__, None,
                         "doc string is missing!")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "doc string is missing!")

