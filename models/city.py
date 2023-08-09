#!/usr/bin/python3
"""This model inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class for city object."""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of class City"""
        super().__init__(*args, **kwargs)
