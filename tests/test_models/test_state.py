#!/usr/bin/python3
"""
module unittest state
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """
    tests state
    """

    def test_instance(self):
        """
        instance testing
        """
        hi = State()
        self.assertIsInstance(hi, State)

    def test_state_name(self):
        """
        state name
        """
        hi = State()
        self.assertEqual("", hi.name)

    def test_id(self):
        """
        tests id
        """
        hi = State()
        self.assertEqual(str, type(hi.id))
