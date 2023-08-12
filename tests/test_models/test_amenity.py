#!/usr/bin/python3
"""Defines unittests for models/amenity.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Amenity class."""

    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_Amenity_storage(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_typ(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_email_type(self):
        self.assertEqual(str, type(Amenity.name))

    def test_unique_ids(self):
        Amenity1 = Amenity()
        Amenity2 = Amenity()
        self.assertNotEqual(Amenity1.id, Amenity2.id)

    def test_different_created_at(self):
        Amenity1 = Amenity()
        sleep(0.1)
        Amenity2 = Amenity()
        self.assertLess(Amenity1.created_at, Amenity2.created_at)

    def test_different_updated_at(self):
        Amenity1 = Amenity()
        sleep(0.1)
        Amenity2 = Amenity()
        self.assertLess(Amenity1.updated_at, Amenity2.updated_at)

    def test_str(self):
        date = datetime.today()
        date_repr = repr(date)
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = date
        Amenity_str = amenity.__str__()
        self.assertIn("[Amenity] (123456)", Amenity_str)
        self.assertIn("'id': '123456'", Amenity_str)
        self.assertIn("'created_at': " + date_repr, Amenity_str)
        self.assertIn("'updated_at': " + date_repr, Amenity_str)

    def test_unused_args(self):
        amenity = Amenity(None)
        self.assertNotIn(None, amenity.__dict__.values())

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        amenity = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amenity.id, "345")
        self.assertEqual(amenity.created_at, date)
        self.assertEqual(amenity.updated_at, date)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
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
        amenity = Amenity()
        sleep(0.1)
        first_updated_at = amenity.updated_at
        amenity.save()
        self.assertLess(first_updated_at, amenity.updated_at)

    def test_saves2(self):
        amenity = Amenity()
        sleep(0.1)
        first = amenity.updated_at
        amenity.save()
        second = amenity.updated_at
        self.assertLess(first, second)
        sleep(0.1)
        amenity.save()
        self.assertLess(second, amenity.updated_at)

    def test_save_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.save("hello")

    def test_file(self):
        amenity = Amenity()
        amenity.save()
        usid = "Amenity." + amenity.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the Amenity class."""

    def test_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_correct_keys(self):
        amenity = Amenity()
        self.assertIn("id", amenity.to_dict())
        self.assertIn("created_at", amenity.to_dict())
        self.assertIn("updated_at", amenity.to_dict())
        self.assertIn("__class__", amenity.to_dict())

    def test_added_attributes(self):
        amenity = Amenity()
        amenity.middle_name = "Khougha"
        amenity.number = 98
        self.assertEqual("Khougha", amenity.middle_name)
        self.assertIn("number", amenity.to_dict())

    def test_datetime_type(self):
        amenity = Amenity()
        Amenity_dict = amenity.to_dict()
        self.assertEqual(str, type(Amenity_dict["id"]))
        self.assertEqual(str, type(Amenity_dict["created_at"]))
        self.assertEqual(str, type(Amenity_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        amenity = Amenity()
        amenity.id = "123456"
        amenity.created_at = amenity.updated_at = date
        Amenity_dict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(amenity.to_dict(), Amenity_dict)

    def test_dict_vs_to_dict(self):
        amenity = Amenity()
        self.assertNotEqual(amenity.to_dict(), amenity.__dict__)

    def test_to_dict_with_arg(self):
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.to_dict(None)
