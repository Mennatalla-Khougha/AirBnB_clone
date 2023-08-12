#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Place class."""

    def test_no_args(self):
        self.assertEqual(Place, type(Place()))

    def test_Place_storage(self):
        self.assertIn(Place(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_typ(self):
        self.assertEqual(datetime, type(Place().updated_at))

    def test_email_type(self):
        self.assertEqual(str, type(Place.city_id))

    def test_password_type(self):
        self.assertEqual(str, type(Place.user_id))

    def test_first_name_type(self):
        self.assertEqual(str, type(Place.name))

    def test_last_name_type(self):
        self.assertEqual(str, type(Place.description))

    def test_last_name_type(self):
        self.assertEqual(int, type(Place.number_rooms))

    def test_last_name_type(self):
        self.assertEqual(int, type(Place.number_bathrooms))

    def test_last_name_type(self):
        self.assertEqual(int, type(Place.max_guest))

    def test_last_name_type(self):
        self.assertEqual(int, type(Place.price_by_night))

    def test_last_name_type(self):
        self.assertEqual(float, type(Place.latitude))

    def test_last_name_type(self):
        self.assertEqual(float, type(Place.longitude))

    def test_last_name_type(self):
        self.assertEqual(list, type(Place.amenity_ids))

    def test_unique_ids(self):
        Place1 = Place()
        Place2 = Place()
        self.assertNotEqual(Place1.id, Place2.id)

    def test_different_created_at(self):
        Place1 = Place()
        sleep(0.1)
        Place2 = Place()
        self.assertLess(Place1.created_at, Place2.created_at)

    def test_different_updated_at(self):
        Place1 = Place()
        sleep(0.1)
        Place2 = Place()
        self.assertLess(Place1.updated_at, Place2.updated_at)

    def test_str(self):
        date = datetime.today()
        date_repr = repr(date)
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = date
        Place_str = place.__str__()
        self.assertIn("[Place] (123456)", Place_str)
        self.assertIn("'id': '123456'", Place_str)
        self.assertIn("'created_at': " + date_repr, Place_str)
        self.assertIn("'updated_at': " + date_repr, Place_str)

    def test_unused_args(self):
        place = Place(None)
        self.assertNotIn(None, place.__dict__.values())

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        place = Place(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(place.id, "345")
        self.assertEqual(place.created_at, date)
        self.assertEqual(place.updated_at, date)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            Place(id=None, created_at=None, updated_at=None)


class TestPlace_save(unittest.TestCase):
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
        place = Place()
        sleep(0.1)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_saves2(self):
        place = Place()
        sleep(0.1)
        first = place.updated_at
        place.save()
        second = place.updated_at
        self.assertLess(first, second)
        sleep(0.1)
        place.save()
        self.assertLess(second, place.updated_at)

    def test_save_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.save("hello")

    def test_file(self):
        place = Place()
        place.save()
        usid = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestPlace_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Place class."""

    def test_type(self):
        self.assertTrue(dict, type(Place().to_dict()))

    def test_correct_keys(self):
        place = Place()
        self.assertIn("id", place.to_dict())
        self.assertIn("created_at", place.to_dict())
        self.assertIn("updated_at", place.to_dict())
        self.assertIn("__class__", place.to_dict())

    def test_added_attributes(self):
        place = Place()
        place.middle_name = "Khougha"
        place.number = 98
        self.assertEqual("Khougha", place.middle_name)
        self.assertIn("number", place.to_dict())

    def test_datetime_type(self):
        place = Place()
        Place_dict = place.to_dict()
        self.assertEqual(str, type(Place_dict["id"]))
        self.assertEqual(str, type(Place_dict["created_at"]))
        self.assertEqual(str, type(Place_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        place = Place()
        place.id = "123456"
        place.created_at = place.updated_at = date
        Place_dict = {
            'id': '123456',
            '__class__': 'Place',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(place.to_dict(), Place_dict)

    def test_dict_vs_to_dict(self):
        place = Place()
        self.assertNotEqual(place.to_dict(), place.__dict__)

    def test_to_dict_with_arg(self):
        place = Place()
        with self.assertRaises(TypeError):
            place.to_dict(None)
