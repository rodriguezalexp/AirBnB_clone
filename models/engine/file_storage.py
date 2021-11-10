#!/usr/bin/python3
"""Filestorage class"""
import json


class FileStorage:
    """class to serialize and deserialize json"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return dictionary objects"""
        return self.__objects

    def new(self, obj):
        """"""
        if obj is not None:
            
        self.__objects = obj


    