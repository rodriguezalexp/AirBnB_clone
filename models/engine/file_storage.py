#!/usr/bin/python3
"""
Module: FileStorage
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.place import Place
import json

class FileStorage:
    """class to serialize and deserialize json"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects obj with key : obj_class_name.id"""

        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
            
    def save(self):
        """"selrializes __objects to JSON file
        path: __file_path"""
        json_new = {}

        for key, value in self.__objects.items():
            json_new[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_new, f)

    def reload(self):
        """Deserializes the JSON
        file to __objects."""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    cl_asses = value['__class__']
                    self.__objects[key] = classes()[cl_asses](**value)
        except Exception:
            pass
