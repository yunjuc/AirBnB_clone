#!/usr/bin/python3
"""
unnittest file storage
"""
import unittest
import uuid
import datetime
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """
    class TestFileStorage
    """

    def setUp(self):
        '''Set up test case'''
        self.f = FileStorage()
        self.base = BaseModel()
        self.model = BaseModel()

    def tearDown(self):
        '''End of test'''
        pass

    def test_exist(self):
        """
        Test instance
        """
        self.assertIsInstance(self.f, FileStorage)

    def test_save(self):
        """
        Test save method
        """
        self.f.save()
        self.assertEqual(True, os.path.exists('file.json'))

    def test_all(self):
        """
        Test return dict
        """
        obj_dict = self.f.all()
        self.assertIsInstance(obj_dict, dict)
        key1 = 'BaseModel.'+self.base.id
        key2 = 'BaseModel.'+self.model.id
        self.assertEqual(obj_dict[key1], self.base)
        self.assertEqual(obj_dict[key2], self.model)

    def test_new(self):
        '''Test add new instance'''
        obj_dict = self.f.all()
        key1 = 'BaseModel.'+self.base.id
        self.assertEqual(obj_dict[key1], self.base)

    def test_reload(self):
        '''Test reload instance'''
        import models
        self.assertEqual(self.f.all(), models.storage.all())
