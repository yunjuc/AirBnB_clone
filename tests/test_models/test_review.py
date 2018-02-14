#!/usr/bin/python3
"""
module unnitest review
"""
import unittest
from models.review import Review


class TestSTate(unittest.TestCase):
    """
    tests state
    """

    def test_instance(self):
        """
        instance testing
        """
        hi = Review()
        self.assertIsInstance(hi, Review)

    def test_place_id(self):
        """
        tests place_id
        """
        hi = Review()
        self.assertEqual("", hi.place_id)

    def test_text(self):
        """
        tests text
        """
        hi = Review()
        self.assertEqual("", hi.text)

    def test_user_id(self):
        """
        tests user id
        """
        hi = Review()
        self.assertEqual("", hi.user_id)
