#!/usr/bin/python3
"""
FileStorage serializes and deserializes
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes objects to JSON
        """
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            file.write(json.dump(self.__objects))

    def reload(self):
        """
        deserializes JSON file to __objects
        """
        
