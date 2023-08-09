#!/usr/bin/python3
"""unittests for models/engine/file_storage.py."""
import os
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the FileStorage class."""

    def test_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_path_type(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_type(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestBaseModel_BaseModel(unittest.TestCase):
    """Unittests for testing methods of the FileStorage class."""

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
        FileStorage._FileStorage__objects = {}

    def test_all_type(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_with_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new(self):
        base = BaseModel()
        models.storage.new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())
        self.assertIn(base, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), "hello")

    def test_new_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("BaseModel." + base.id, text)

    def test_save_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save("HI")

    def test_reload(self):
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base.id, objs)

    def test_reload_no_file(self):
        try:
            models.storage.reload()
        except FileNotFoundError:
            self.fail("Error")

    def test_reload_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload("HI")


class TestUser_methods(unittest.TestCase):
    """Unittests for testing methods on the User class."""
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
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        user = User()
        models.storage.new(user)
        self.assertIn("User." + user.id, models.storage.all().keys())
        self.assertIn(user, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(User(), "hello")

    def test_save(self):
        user = User()
        models.storage.new(user)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("User." + user.id, text)

    def test_reload(self):
        user = User()
        models.storage.new(user)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("User." + user.id, objs)
