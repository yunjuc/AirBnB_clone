#!/usr/bin/python3
'''Unittest for BaseModel class'''
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Unittest for BaseModel class'''

    def setUp(self):
        '''Set up test case'''
        self.base = BaseModel()
        self.base.name = 'holberton'
        self.base.number = 98

    def tearDown(self):
        '''End of set up'''
        pass

    def test_create(self):
        '''Create an instance with id and datetime'''
        self.assertTrue(self.base.id)
        self.assertTrue(self.base.created_at)
        self.assertTrue(self.base.updated_at)

    def test_str(self):
        '''Test __str__ output'''
        rep = "[BaseModel] ({}) {}".format(self.base.id, self.base.__dict__)
        self.assertEqual(str(self.base), rep)

    def test_to_dict(self):
        '''Test to_dict output'''
        my_dict = self.base.to_dict()
        self.assertEqual(type(my_dict), dict)
        self.assertEqual(my_dict["__class__"], 'BaseModel')
        self.assertEqual(type(my_dict["created_at"]), str)
        self.assertEqual(type(my_dict["updated_at"]), str)

    def test_create_instance(self):
        '''Create a new instatnce from dict'''
        old_dict = self.base.to_dict()
        new = BaseModel(**old_dict)
        self.assertEqual(self.base.id, new.id)
        self.assertEqual(self.base.name, new.name)
        self.assertEqual(self.base.number, new.number)
        self.assertEqual(self.base.created_at, new.created_at)
        self.assertEqual(self.base.updated_at, new.updated_at)
        self.assertIsNot(self.base, new)

    def test_save(self):
        """
        Test save
        """
        updated = self.thing.updated_at
        self.thing.save()
        self.assertNotEqual(updated, self.thing.updated_at)
