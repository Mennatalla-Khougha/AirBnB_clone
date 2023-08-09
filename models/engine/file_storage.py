#!/usr/bin/python3
""""This class serializes and deserializes JSON file """
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """"This class for serializes and deserialize JSON file"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the directory __objects"""
        return self.__objects

    def new(self, obj):
        """"Sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        """"Serialization of __objects to the JSON file """
        objs = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as file:
            json.dump(objs, file)

    def reload(self):
        """"Deserialization from the JSON file into __objects dictionary."""
        try:
            with open(FileStorage.__file_path) as file:
                objs = json.load(file)
                for obj in objs.values():
                    class_name = obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            pass