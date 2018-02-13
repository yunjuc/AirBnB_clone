#!/usr/bin/python3
"""
creating FileStorage instance
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


cls_list = {'BaseModel': BaseModel, 'User': User, 'City': City, 'Place': Place,
            'State': State, 'Review': Review, 'Amenity': Amenity}

storage = FileStorage()
storage.reload()
