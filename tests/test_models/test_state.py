#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the State class."""

    def test_no_args(self):
        self.assertEqual(State, type(State()))

    def test_State_storage(self):
        self.assertIn(State(), models.storage.all().values())

    def test_id_type(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_type(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_updated_at_typ(self):
        self.assertEqual(datetime, type(State().updated_at))

    def test_email_type(self):
        self.assertEqual(str, type(State.name))

    def test_unique_ids(self):
        State1 = State()
        State2 = State()
        self.assertNotEqual(State1.id, State2.id)

    def test_different_created_at(self):
        State1 = State()
        sleep(0.1)
        State2 = State()
        self.assertLess(State1.created_at, State2.created_at)

    def test_different_updated_at(self):
        State1 = State()
        sleep(0.1)
        State2 = State()
        self.assertLess(State1.updated_at, State2.updated_at)

    def test_str(self):
        date = datetime.today()
        date_repr = repr(date)
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = date
        State_str = state.__str__()
        self.assertIn("[State] (123456)", State_str)
        self.assertIn("'id': '123456'", State_str)
        self.assertIn("'created_at': " + date_repr, State_str)
        self.assertIn("'updated_at': " + date_repr, State_str)

    def test_unused_args(self):
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        state = State(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(state.id, "345")
        self.assertEqual(state.created_at, date)
        self.assertEqual(state.updated_at, date)

    def test_None_kwargs(self):
        with self.assertRaises(TypeError):
            State(id=None, created_at=None, updated_at=None)


class TestState_save(unittest.TestCase):
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
        state = State()
        sleep(0.1)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_saves2(self):
        state = State()
        sleep(0.1)
        first = state.updated_at
        state.save()
        second = state.updated_at
        self.assertLess(first, second)
        sleep(0.1)
        state.save()
        self.assertLess(second, state.updated_at)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save("hello")

    def test_file(self):
        state = State()
        state.save()
        usid = "State." + state.id
        with open("file.json", "r") as f:
            self.assertIn(usid, f.read())


class TestState_to_dict(unittest.TestCase):
    """Unittests for testing to_dict method of the State class."""

    def test_type(self):
        self.assertTrue(dict, type(State().to_dict()))

    def test_correct_keys(self):
        state = State()
        self.assertIn("id", state.to_dict())
        self.assertIn("created_at", state.to_dict())
        self.assertIn("updated_at", state.to_dict())
        self.assertIn("__class__", state.to_dict())

    def test_added_attributes(self):
        state = State()
        state.middle_name = "Khougha"
        state.number = 98
        self.assertEqual("Khougha", state.middle_name)
        self.assertIn("number", state.to_dict())

    def test_datetime_type(self):
        state = State()
        State_dict = state.to_dict()
        self.assertEqual(str, type(State_dict["id"]))
        self.assertEqual(str, type(State_dict["created_at"]))
        self.assertEqual(str, type(State_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        state = State()
        state.id = "123456"
        state.created_at = state.updated_at = date
        State_dict = {
            'id': '123456',
            '__class__': 'State',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(state.to_dict(), State_dict)

    def test_contrast_to_dict_dunder_dict(self):
        state = State()
        self.assertNotEqual(state.to_dict(), state.__dict__)

    def test_to_dict_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.to_dict(None)
