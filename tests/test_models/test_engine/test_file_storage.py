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
