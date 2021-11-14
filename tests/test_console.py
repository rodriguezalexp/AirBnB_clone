#!/usr/bin/python3
""" Test_BaseModel: unittest for base_model"""
import unittest
from unittest import mock  # we use this library so simulate an object...
                            # a running console


class TestConsole(unittest.TestCase):
    """Unittests for console.py"""

    def test_quit(self):
        """Test quit expression"""
        self.mocked(cmd="quit", expected="")

    def test_EOF(self):
        """Test EOF expression, ctrl+D"""
        self.mocked(cmd="EOF", expected="")

    def test_emptyline(self):
        """"Tests empty line.. do nothing"""
        self.mocked(cmd="\n", expected="")
    
    
