#!/usr/bin/python3
# This is the test suite of the BaseModel class

import os
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
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

    def test_args(self):
        base = BaseModel(None)
        self.assertNotIn(None, base.__dict__.values())

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        base = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_args_and_kwargs(self):
        date = datetime.today()
        iso = date.isoformat()
        base = BaseModel("12", id="345", created_at=iso, updated_at=iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)


class Test_save(unittest.TestCase):
    """Unittests for testing save method of the BaseModel class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "filetest.json")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("filetest.json", "file.json")
        except IOError:
            pass

    def test_save1(self):
        base = BaseModel()
        sleep(0.1)
        first = base.updated_at
        base.save()
        self.assertLess(first, base.updated_at)

    def test_save2(self):
        base = BaseModel()
        sleep(0.1)
        first = base.updated_at
        base.save()
        second = base.updated_at
        self.assertLess(first, second)
        sleep(0.05)
        base.save()
        self.assertLess(second, base.updated_at)

    def test_save_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.save(None)

    def test_save_file(self):
        base = BaseModel()
        base.save()
        key = "BaseModel." + base.id
        with open("file.json", "r") as file:
            self.assertIn(key, file.read())


class Test_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the BaseModel class."""

    def test_to_dict_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_with_attributes(self):
        base = BaseModel()
        base.name1 = "Geroge"
        base.name2 = "Menna"
        base.my_number = 98
        self.assertIn("name1", base.to_dict())
        self.assertIn("name2", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_datetime_type(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    def test_to_dict(self):
        date = datetime.today()
        base = BaseModel()
        base.id = "12345"
        base.created_at = base.updated_at = date
        dict_base = {
            'id': '12345',
            '__class__': 'BaseModel',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat()
        }
        self.assertDictEqual(base.to_dict(), dict_base)

    def test_dict_vs_to_dict(self):
        base = BaseModel()
        self.assertNotEqual(base.to_dict(), base.__dict__)

    def test_to_dict_with_arg(self):
        base = BaseModel()
        with self.assertRaises(TypeError):
            base.to_dict("hello")
