#!/usr/bin/python3
#This is the BaseModel class
import uuid
import datetime


class BaseModel():
    """Base model for all models"""
    def __init__(self):
        """Initialization of BaseModel class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.now()
        
    def to_dict(self):
        data_dict = self.__dict__.copy()
        data_dict['created_at'] = data_dict['created_at'].isoformat()
        data_dict['updated_at'] = data_dict['updated_at'].isoformat()
        data_dict['__class__'] = self.__class__.__name__
        return data_dict
