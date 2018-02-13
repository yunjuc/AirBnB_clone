#!/usr/bin/python3
'''Base class module'''
import uuid
import datetime
import models


class BaseModel():
    '''Base class of all models'''

    id = ""
    created_at = None
    updated_at = None

    def __init__(self, *arags, **kwargs):
        '''Instance instantiation'''
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = datetime.datetime.utcnow()
            models.storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.datetime.strptime(v,
                            '%Y-%m-%dT%H:%M:%S.%f'))
                elif k == '__class__':
                    v = models.cls_list[v]
                    setattr(self, k, v)
                else:
                    setattr(self, k, v)

    def __str__(self):
        '''__str__ representation'''
        string = '['+self.__class__.__name__+']'+' ('+self.id+') ' +\
                 str(self.__dict__)
        return string

    def save(self):
        '''Update updated_at time'''
        self.updated_at = datetime.datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        '''Serialize __dict__ and add class info'''
        j_dict = dict(self.__dict__)
        j_dict["updated_at"] = self.updated_at.isoformat()
        j_dict["created_at"] = self.created_at.isoformat()
        j_dict["__class__"] = self.__class__.__name__
        return j_dict
