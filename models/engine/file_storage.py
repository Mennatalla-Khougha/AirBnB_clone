#!/usr/bin/python3
""""This class serializes and deserializes JSON file """
import json
import models.base_model


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
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, obj_data in data.items():
                    print(f"the key: {key}")
                    class_name, obj_id = key.split(".")
                    model_class = getattr(models.base_model, class_name)
                    obj = model_class(**obj_data)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
