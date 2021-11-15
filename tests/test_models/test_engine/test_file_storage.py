#!/usr/bin/python3
"""
Module: Unittest for file_storage.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestFilestorage(unittest.TestCase):
    """Class to run unittest on FileStorage"""

    def setUp(self):
        self.object = FileStorage()

    def testDocstring_class(self):
        """Check class, docstring"""
        self.assertIsNotNone(FileStorage.__doc__)

    def testinstance(self):
        """test if instance of object belongs to FileStorage"""
        self.assertIsInstance(self.object, FileStorage)

    def test_all(self):
        """check if all() works"""
        nu_dict = FileStorage.all()
        self.assertIsInstance(nu_dict, dict)

    def test_new(self):
        """Check functionality of new()"""
        pass

    def test_save(self):
        """save() method unittest"""
        pass

    def test_reload(self):
        """reload() unittest"""
        pass

