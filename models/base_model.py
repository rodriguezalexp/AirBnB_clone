#!usr/bin/python3
"""Defining BaseModel class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.created_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] == value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def save(self):
        """update instance with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of dict"""
        cpy_dict = __dict__.copy()
        cpy_dict["created_at"] = created_at.isoformat()
        cpy_dict["updated_at"] = updated_at.isoformat()
        cpy_dict["__class__"] = __class__.__name__
        return cpy_dict

    def __str__(self):
        """string representacion of object"""
        return ("[{}] ({:d}) {}").format(__class__.__name__, self.id, self.__dict__)
