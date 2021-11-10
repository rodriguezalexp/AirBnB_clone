#!/usr/bin/python3
"""Filestorage class"""
from models.base_model import BaseModel
import json


class FileStorage:
    """class to serialize and deserialize json"""
    def __init__(self):
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects obj with
        key : obj_class_name.id"""
        if obj is not None:
            self.__objects.update(
                {"{}.{}\
".format(obj.__class__.__name__, obj.id): obj})

    def save(self):
        """"selrializes __objects to JSON file
        path: __file_path"""
        dict_new = {}

        for key, value in self.__objects.items():
            dict_new[key] = value.to_dict()
        with open(self.__file_path, 'w') as fd:
            json.dump(dict_new, fd)

    def reload(self):
        """"deserializes JSON file to __objects"""
        pass

    dsfdf