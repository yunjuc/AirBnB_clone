#!/usr/bin/python3
'''User class module'''
from models.base_model import BaseModel


class User(BaseModel):
    '''User class'''
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self):
       '''Instance instantiation'''
       super().__init__()
