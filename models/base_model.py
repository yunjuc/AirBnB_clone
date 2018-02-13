#!/usr/bin/python3
'''Base class module'''
import uuid
import datetime
from models import storage


class BaseModel():
    '''Base class of all models'''

    def __init__(self, *arags, **kwargs):
        '''Instance instantiation'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        storage.new(self)

        if kwargs is not None:
            for k, v in kwargs.items():
                if k is 'created_at' or k is 'updated_at':
                    setattr(self, k, datetime.datetime.strptime(v,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif k is '__class__':
                    pass
                else:
                    setattr(self, k, v)

    def __str__(self):
        '''__str__ representation'''
        string = '['+self.__class__.__name__+']'+' ('+self.id+') ' +\
                 str(self.__dict__)
        return string

    def save(self):
        '''Update updated_at time'''
        self.updated_at = datetime.datetime.now()
        storage.save()


    def to_dict(self):
        '''Serialize __dict__ and add class info'''
        j_dict = self.__dict__
        j_dict["updated_at"] = self.updated_at.isoformat()
        j_dict["created_at"] = self.created_at.isoformat()
        j_dict["__class__"] = self.__class__.__name__
        return j_dict
