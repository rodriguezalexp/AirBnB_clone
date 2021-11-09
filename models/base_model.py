#!usr/bin/python3
"""Defining BaseModel class"""

import datetime
import uuid


class BaseModel:
    """"""
    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        pass

    def __str__(self):
        return ("[{}] ({:d}) {}").format(__class__.__name__, self.id, self.__dict__)
