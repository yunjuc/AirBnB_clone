#!/usr/bin/python3
"""
module contains unittest for city
"""
import unittest
from models.city import City


class TestCityClass(unittest.TestCase):
    """
    class TestCity
    """

    def test_type(self):
        """
        instance test
        """
        hi = City()
        self.assertIsInstance(hi, City)

    def test_id(self):
        """
        tests id
        """
        hi = City()
        self.assertEqual(str, type(hi.id))

    def test_stateid(self):
        """
        city state_id
        """
        hi = City()
        self.assertEqual("", hi.state_id)
