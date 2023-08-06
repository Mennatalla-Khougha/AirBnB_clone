#!/usr/bin/python3
# This is the test suite of the BaseModel class

import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id_type(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_type(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids(self):
        first = BaseModel()
        second = BaseModel()
        self.assertNotEqual(first.id, second.id)

    def test_different_created_at(self):
        first = BaseModel()
        sleep(0.1)
        second = BaseModel()
        self.assertLess(first.created_at, second.created_at)

    def test_different_updated_at(self):
        first = BaseModel()
        sleep(0.1)
        second = BaseModel()
        self.assertLess(first.updated_at, second.updated_at)

    def test_str(self):
        date = datetime.today()
        date_repr = repr(date)
        base = BaseModel()
        base.id = "123456"
        base.created_at = base.updated_at = date
        base_str = base.__str__()
        self.assertIn("[BaseModel] (123456)", base_str)
        self.assertIn("'id': '123456'", base_str)
        self.assertIn("'created_at': " + date_repr, base_str)
        self.assertIn("'updated_at': " + date_repr, base_str)
