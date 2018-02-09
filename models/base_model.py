#!/usr/bin/python3
'''Base class model'''
import uuid
from datetime import datetime


class BaseModel():
    '''Base class of all models'''

    id=str(uuid.uuid4())
    created_at=datetime.now()
    updated_at=datetime.now()

    def __init__(self, *args, **kwargs):
        '''Instance instantiation'''


    def __str__(self):
        '''__str__ representation'''


    def save(self):
        ''' '''


    def to_dict(self):
        '''Save __dict__ to a dictionary'''
