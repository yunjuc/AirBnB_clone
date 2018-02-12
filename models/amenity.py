#!/usr/bin/python3
'''Amenity class module'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''Amenity class'''
    name = ""

    def __init__(self):
        '''Instance instantiation'''
        super().__init__()
