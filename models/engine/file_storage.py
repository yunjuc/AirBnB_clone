#!/usr/bin/python3
"""
FileStorage serializes and deserializes
"""
<<<<<<< HEAD


import json
import models

class FileStorage():
    """
    serializes and deserializes
    """

    __file_path = "file.json"
    __object = {}

    def all(self):
        """
        returns filestorage objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets __objects with key class name.id
=======
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    Serializes and deserializes
    """

    __file_path = "file.json"
    __objects = {}
    cls_list = ['BaseModel', 'User', 'City', 'Place', 'State', 'Review', 'Amenity']

    def all(self):
        """
        Return filestorage objects
        """
        return self.__objects

    def new(self, obj):
        """
        Set __objects with key class name.id
>>>>>>> 1644ce3783c78928180325a8df74acb3d6712af8
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
<<<<<<< HEAD
        serializes objects to JSON
=======
        Serializes objects to JSON
>>>>>>> 1644ce3783c78928180325a8df74acb3d6712af8
        """
        result = {}
        for k, v in self.__objects.items():
            result[k] = v.to_dict()
<<<<<<< HEAD
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump(result, file)

    def reload(self):
        """
        deserializes JSON file to __objects
        """
        
=======
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(result, f)

    def reload(self):
        """
        Deserialize JSON file to __object
        """
        try:
            with open(self.__file_path) as f:
                j_dict = json.load(f)
            for k, v in j_dict.items():
                cls = v['__class__']
                self.__objects[k] = cls(**v)
        except FileNotFoundError as e:
            pass
>>>>>>> 1644ce3783c78928180325a8df74acb3d6712af8
