#!/usr/bin/python3
"""
unnittest user
"""
import unittest
import json
import sys
import uuid
import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    testuser
    """
    def test_instance(self):
        """
        tests instance
        """
        james = User()
        self.assertIsInstance(james, User)

    def test_email(self):
        """
        tests email
        """
        james = User()
        self.assertEqual("", james.email)

    def test_password(self):
        """
        tests password
        """
        james = User()
        self.assertEqual("", james.password)

    def test_first(self):
        """
        tests first name
        """
        james = User()
        self.assertEqual("", james.first_name)

    def test_last(self):
        """
        tests last name
        """
        james = User()
        self.assertEqual("", james.last_name)
