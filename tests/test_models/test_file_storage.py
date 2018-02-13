"""
unnittest file storage
"""
import unittest
import uuid
import datetime
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def test_exist(self):
        """
        tests instance
        """
        a = FileStorage()
        self.assertIsInstance(a, FileStorage)

    def test_save(self):
        """
        tests save method
        """
        a = BaseModel()
        a.save()
        self.assertEqual(true, os.path.exists('file.json'))

    def test_all(self):
        """
        test returns dict
        """
        a = FileStorage()
        b = a.all()
        self.assertIsInstance(b, dict)

