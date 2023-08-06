#!/usr/bin/python3
# This is the BaseModel class
import uuid
from datetime import datetime


class BaseModel():
    """Base model for all models"""
    def __init__(self, *args, **kwargs):
        """Initialization of BaseModel class"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    date = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, date)
                elif key == "__class__":
                    pass
                else:
                    setattr(self, key, value)

    def __str__(self):
        """Return string representation of the class"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """save the Updated date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary of the class"""
        data_dict = self.__dict__.copy()
        data_dict['created_at'] = data_dict['created_at'].isoformat()
        data_dict['updated_at'] = data_dict['updated_at'].isoformat()
        data_dict['__class__'] = self.__class__.__name__
        return data_dict
