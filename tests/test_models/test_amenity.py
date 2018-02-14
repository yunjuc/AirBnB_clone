#!/usr/bin/python3
"""
module unittest amenity
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    unittest for amenity class
    """

    def test_amenity(self):
        """
        instance testing
        """
        hi = Amenity()
        self.assertIsInstance(hi, Amenity)

    def test_name(self):
        """
        tests name value
        """
        hi = Amenity()
        self.assertEqual("", hi.name)

    def test_id(self):
        """
        tests id
        """
        hi = Amenity()
        self.assertEqual(str, type(hi.id))
