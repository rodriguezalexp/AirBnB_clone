#!/usr/bin/python3
""" Test_BaseModel: unittest for base_model"""
import unittest
from .. import console

class TestConsole(unittest.TestCase):
	"""Unittests for console.py"""
	def testEOF(self):
		self.with_mock