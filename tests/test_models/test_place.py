#!/usr/bin/python3
"""
Module unittest place
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    tests place
    """

    def test_instance(self):
        """
        instance test
        """
        hi = Place()
        self.assertIsInstance(hi, Place)

    def test_id(self):
        """
        tests id
        """
        hi = Place()
        self.assertEqual("", hi.city_id)

    def test_user_id(self):
        """
        tests user id
        """
        hi = Place()
        self.assertEqual("", hi.user_id)

    def test_name(self):
        """
        tests name
        """
        hi = Place()
        self.assertEqual("", hi.name)

