#!/usr/bin/python3
"""unittests for models/engine/file_storage.py."""
import os
import models
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        with self.assertRaises(FileNotFoundError):
            models.storage.reload()
            raise FileNotFoundError

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


class TestState_methods(unittest.TestCase):
    """Unittests for testing methods on the State class."""
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
        state = State()
        models.storage.new(state)
        self.assertIn("State." + state.id, models.storage.all().keys())
        self.assertIn(state, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(State(), "hello")

    def test_save(self):
        state = State()
        models.storage.new(state)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("State." + state.id, text)

    def test_reload(self):
        state = State()
        models.storage.new(state)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("State." + state.id, objs)


class TestCity_methods(unittest.TestCase):
    """Unittests for testing methods on the City class."""
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
        city = City()
        models.storage.new(city)
        self.assertIn("City." + city.id, models.storage.all().keys())
        self.assertIn(city, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(City(), "hello")

    def test_save(self):
        city = City()
        models.storage.new(city)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("City." + city.id, text)

    def test_reload(self):
        city = City()
        models.storage.new(city)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("City." + city.id, objs)


class TestPlace_methods(unittest.TestCase):
    """Unittests for testing methods on the Place class."""
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
        place = Place()
        models.storage.new(place)
        self.assertIn("Place." + place.id, models.storage.all().keys())
        self.assertIn(place, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(Place(), "hello")

    def test_save(self):
        place = Place()
        models.storage.new(place)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("Place." + place.id, text)

    def test_reload(self):
        place = Place()
        models.storage.new(place)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Place." + place.id, objs)


class TestAmenity_methods(unittest.TestCase):
    """Unittests for testing methods on the Amenity class."""
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
        amenity = Amenity()
        models.storage.new(amenity)
        self.assertIn("Amenity." + amenity.id, models.storage.all().keys())
        self.assertIn(amenity, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(Amenity(), "hello")

    def test_save(self):
        amenity = Amenity()
        models.storage.new(amenity)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("Amenity." + amenity.id, text)

    def test_reload(self):
        amenity = Amenity()
        models.storage.new(amenity)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Amenity." + amenity.id, objs)


class TestReview_methods(unittest.TestCase):
    """Unittests for testing methods on the Review class."""
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
        review = Review()
        models.storage.new(review)
        self.assertIn("Review." + review.id, models.storage.all().keys())
        self.assertIn(review, models.storage.all().values())

    def test_new_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(Review(), "hello")

    def test_save(self):
        review = Review()
        models.storage.new(review)
        models.storage.save()
        with open("file.json", "r") as file:
            text = file.read()
            self.assertIn("Review." + review.id, text)

    def test_reload(self):
        review = Review()
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("Review." + review.id, objs)
