#!usr/bin/python3
"""Defining BaseModel class"""

import datetime
import uuid


class BaseModel:
    """BaseModel class"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def save(self):
        """update instance with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of dict"""
        pass

    def __str__(self):
        """string representacion of object"""
        return ("[{}] ({:d}) {}").format(__class__.__name__, self.id, self.__dict__)
