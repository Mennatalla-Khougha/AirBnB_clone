#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City


class TestCity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the City class."""

    def test_no_args(self):
        self.assertEqual(City, type(City()))

    def test_City_storage(self):
        self.assertIn(City(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_typ(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_email_type(self):
        self.assertEqual(str, type(City.state_id))

    def test_password_type(self):
        self.assertEqual(str, type(City.name))

    def test_unique_ids(self):
        City1 = City()
        City2 = City()
        self.assertNotEqual(City1.id, City2.id)

    def test_different_created_at(self):
        City1 = City()
        sleep(0.1)
        City2 = City()
        self.assertLess(City1.created_at, City2.created_at)

    def test_different_updated_at(self):
        City1 = City()
        sleep(0.1)
        City2 = City()
        self.assertLess(City1.updated_at, City2.updated_at)

    def test_str(self):
        date = datetime.today()
        date_repr = repr(date)
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = date
        City_str = city.__str__()
        self.assertIn("[City] (123456)", City_str)
        self.assertIn("'id': '123456'", City_str)
        self.assertIn("'created_at': " + date_repr, City_str)
        self.assertIn("'updated_at': " + date_repr, City_str)

    def test_unused_args(self):
        city = City(None)
        self.assertNotIn(None, city.__dict__.values())

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        city = City(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(city.id, "345")
        self.assertEqual(city.created_at, date)
        self.assertEqual(city.updated_at, date)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)


class TestCity_save(unittest.TestCase):
    """Unittests for testing save method of the  class."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_save1(self):
        city = City()
        sleep(0.1)
        first_updated_at = city.updated_at
        city.save()
        self.assertLess(first_updated_at, city.updated_at)

    def test_saves2(self):
        city = City()
        sleep(0.1)
        first = city.updated_at
        city.save()
        second = city.updated_at
        self.assertLess(first, second)
        sleep(0.1)
        city.save()
        self.assertLess(second, city.updated_at)

    def test_save_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save("hello")

    def test_file(self):
        city = City()
        city.save()
        usid = "City." + city.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestCity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the City class."""

    def test_type(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_correct_keys(self):
        city = City()
        self.assertIn("id", city.to_dict())
        self.assertIn("created_at", city.to_dict())
        self.assertIn("updated_at", city.to_dict())
        self.assertIn("__class__", city.to_dict())

    def test_added_attributes(self):
        city = City()
        city.middle_name = "Khougha"
        city.number = 98
        self.assertEqual("Khougha", city.middle_name)
        self.assertIn("number", city.to_dict())

    def test_datetime_type(self):
        city = City()
        City_dict = city.to_dict()
        self.assertEqual(str, type(City_dict["id"]))
        self.assertEqual(str, type(City_dict["created_at"]))
        self.assertEqual(str, type(City_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        city = City()
        city.id = "123456"
        city.created_at = city.updated_at = date
        City_dict = {
            'id': '123456',
            '__class__': 'City',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(city.to_dict(), City_dict)

    def test_dict_vs_to_dict(self):
        city = City()
        self.assertNotEqual(city.to_dict(), city.__dict__)

    def test_to_dict_with_arg(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)
