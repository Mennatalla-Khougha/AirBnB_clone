#!/usr/bin/python3
"""This model inherit from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class for amenity objects."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of class Amenity"""
        super().__init__(*args, **kwargs)
